---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/examples-deid-tables/
title: Examples of de-identifying tabular data \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:54.787295+00:00
---

# Examples of de-identifying tabular data  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/examples-deid-tables/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Examples of de-identifying tabular data Stay organized with collections  Save and categorize content based on your preferences. 

Sensitive Data Protection can detect, classify, and [de-identify](https://docs.cloud.google.com/sensitive-data-protection/docs/classification-redaction) sensitive data within structured data. When de-identifying content as a table, the structure and columns provide Sensitive Data Protection with additional clues that may enable it to provide better results for some use cases. For example, you can scan a single column for a certain data type instead of the entire table structure.

This topic provides examples of how to configure de-identification of sensitive data within structured text. De-identification is enabled through [record transformations](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#record_transformations). These transformations are applied to values within tabular text data that are identified as a specific infoType, or to an entire column of tabular data.

This topic also provides examples of tabular data transformations using the cryptographic hash method. The cryptographic transformation methods are unique because of their requirement of a cryptographic key.

The JSON given in the following examples can be inserted into any [de-identification](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data) request inside the `"deidentifyConfig"` ([`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig)) attribute. Click the "APIs Explorer example" link to try out the example JSON in [APIs Explorer](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true).

## Transform a column without inspection

To transform a specific column in which the content is already known, you can skip inspection and specify a transformation directly. The example following the table [buckets](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing) the "HAPPINESS SCORE" column into increments of 10.

Input | Transformed table   
---|---  
| AGE | PATIENT | HAPPINESS SCORE  
---|---|---  
101 | Charles Dickens | 95  
22 | Jane Austen | 21  
55 | Mark Twain | 75  
| AGE | PATIENT | HAPPINESS SCORE  
---|---|---  
101 | Charles Dickens | 90:100  
22 | Jane Austen | 20:30  
55 | Mark Twain | 70:80  
  
**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyUsingTableBucketing
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
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "101" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "95" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Jane Austin" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "21" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "55" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "75" }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" }
                    },
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
    
            // Specify how the content should be de-identified.
            var fixedSizeBucketingConfig = new [FixedSizeBucketingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FixedSizeBucketingConfig.html)
            {
                BucketSize = 10,
                LowerBound = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 0 },
                UpperBound = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 100 },
            };
    
            // Specify the fields to be encrypted.
            var fields = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" } };
    
            // Associate the encryption with the specified field.
            var fieldTransformation = new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
            {
                PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                {
                    FixedSizeBucketingConfig = fixedSizeBucketingConfig
                },
                Fields = { fields }
            };
    
            // Construct the deidentify config.
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
            var response = dlp.DeidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
    
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
    
    // deIdentifyTableBucketing de-identifies data using table bucketing
    func deIdentifyTableBucketing(w io.Writer, projectID string) error {
    	// projectId := "your-project-id"
    	// table := "your-table-value"
    
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "22"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Jane Austen"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "21"}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "55"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "75"}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "101"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "95"}},
    		},
    	}
    
    	table := &dlppb.Table{
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
    			Table: table,
    		},
    	}
    
    	// Specify how the content should be de-identified.
    	fixedSizeBucketingConfig := &dlppb.FixedSizeBucketingConfig{
    		BucketSize: 10,
    		LowerBound: &dlppb.Value{
    			Type: &dlppb.Value_IntegerValue{
    				IntegerValue: 0,
    			},
    		},
    		UpperBound: &dlppb.Value{
    			Type: &dlppb.Value_IntegerValue{
    				IntegerValue: 100,
    			},
    		},
    	}
    	primitiveTransformation := &dlppb.PrimitiveTransformation_FixedSizeBucketingConfig{
    		FixedSizeBucketingConfig: fixedSizeBucketingConfig,
    	}
    
    	// Specify field to be encrypted.
    	fieldId := &dlppb.FieldId{
    		Name: "HAPPINESS SCORE",
    	}
    
    	// Associate the encryption with the specified field.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    			PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    				Transformation: primitiveTransformation,
    			},
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
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    				RecordTransformations: recordTransformations,
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
    import com.google.privacy.dlp.v2.[FixedSizeBucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FixedSizeBucketingConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    
    public class DeIdentifyTableBucketing {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("PATIENT").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("101").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charles Dickens").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("95").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("22").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Jane Austen").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("21").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("55").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("75").build())
                        .build())
                .build();
    
        deIdentifyTableBucketing(projectId, tableToDeIdentify);
      }
    
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyTableBucketing(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify how the content should be de-identified.
          [FixedSizeBucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FixedSizeBucketingConfig.html) fixedSizeBucketingConfig =
              [FixedSizeBucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FixedSizeBucketingConfig.html).newBuilder()
                  .setBucketSize(10)
                  .[setLowerBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FixedSizeBucketingConfig.Builder.html#com_google_privacy_dlp_v2_FixedSizeBucketingConfig_Builder_setLowerBound_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(0).build())
                  .[setUpperBound](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FixedSizeBucketingConfig.Builder.html#com_google_privacy_dlp_v2_FixedSizeBucketingConfig_Builder_setUpperBound_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(100).build())
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setFixedSizeBucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setFixedSizeBucketingConfig_com_google_privacy_dlp_v2_FixedSizeBucketingConfig_)(fixedSizeBucketingConfig)
                  .build();
    
          // Specify field to be encrypted.
          [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html) fieldId = [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build();
    
          // Associate the encryption with the specified field.
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize google DLP Client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // Construct the tabular data
    const tablularData = {
      headers: [{name: 'AGE'}, {name: 'PATIENT'}, {name: 'HAPPINESS SCORE'}],
      rows: [
        {
          values: [
            {integerValue: 101},
            {stringValue: 'Charles Dickens'},
            {integerValue: 95},
          ],
        },
        {
          values: [
            {integerValue: 22},
            {stringValue: 'Jane Austen'},
            {integerValue: 21},
          ],
        },
        {
          values: [
            {integerValue: 55},
            {stringValue: 'Mark Twain'},
            {integerValue: 75},
          ],
        },
      ],
    };
    async function deIdentifyTableBucketing() {
      // Specify field to be de-identified.
      const targetColumn = {name: 'HAPPINESS SCORE'};
    
      // Specify how the content should be de-identified.
      const bucketingConfig = {
        bucketSize: 10,
        lowerBound: {
          integerValue: 0,
        },
        upperBound: {
          integerValue: 100,
        },
      };
    
      const primitiveTransformation = {
        fixedSizeBucketingConfig: bucketingConfig,
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: {
          table: tablularData,
        },
        deidentifyConfig: {
          recordTransformations: {
            fieldTransformations: [
              {
                fields: [targetColumn],
                primitiveTransformation,
              },
            ],
          },
        },
      };
      // Send the request and receive response from the service
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results.
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    
    deIdentifyTableBucketing();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\FixedSizeBucketingConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify data using table bucketing
     * Transform a column without inspection. To transform a column in which the content is
     * already known, you can skip inspection and specify a transformation directly.
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to deidentify
     * @param string $outputCsvFile         The oupt file path to save deidentify content
     *
     */
    function deidentify_table_bucketing(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table2.csv',
        string $outputCsvFile = './test/data/deidentify_table_bucketing_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
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
    
        // Construct the table object
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify what content you want the service to de-identify.
        $contentItem = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify how the content should be de-identified.
        $fixedSizeBucketingConfig = (new FixedSizeBucketingConfig())
            ->setBucketSize(10)
            ->setLowerBound((new Value())
                ->setIntegerValue(10))
            ->setUpperBound((new Value())
                ->setIntegerValue(100));
    
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setFixedSizeBucketingConfig($fixedSizeBucketingConfig);
    
        // Specify the field to to apply bucketing transform on
        $fieldId = (new FieldId())
            ->setName('HAPPINESS_SCORE');
    
        // Associate the encryption with the specified field.
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields([$fieldId]);
    
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
            ->setItem($contentItem);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print results
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf($outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    from google.cloud.dlp_v2 import [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html)
    
    
    def deidentify_table_bucketing(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        deid_content_list: List[str],
        bucket_size: int,
        bucketing_lower_bound: int,
        bucketing_upper_bound: int,
    ) -> types.dlp.Table:
        """Uses the Data Loss Prevention API to de-identify sensitive data in a
        table by replacing them with fixed size bucket ranges.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_data: Dictionary representing table data.
            deid_content_list: A list of fields in table to de-identify.
            bucket_size: Size of each bucket for fixed sized bucketing
                (except for minimum and maximum buckets). So if ``bucketing_lower_bound`` = 10,
                ``bucketing_upper_bound`` = 89, and ``bucket_size`` = 10, then the
                following buckets would be used: -10, 10-20, 20-30, 30-40,
                40-50, 50-60, 60-70, 70-80, 80-89, 89+.
           bucketing_lower_bound: Lower bound value of buckets.
           bucketing_upper_bound:  Upper bound value of buckets.
    
        Returns:
           De-identified table is returned;
           the response from the API is also printed to the terminal.
    
        Example:
        >> $ python deidentify_table_bucketing.py \
            '{"header": ["email", "phone number", "age"],
            "rows": [["robertfrost@example.com", "4232342345", "35"],
            ["johndoe@example.com", "4253458383", "68"]]}' \
            ["age"] 10 0 100
            >>  '{"header": ["email", "phone number", "age"],
                "rows": [["robertfrost@example.com", "4232342345", "30:40"],
                ["johndoe@example.com", "4253458383", "60:70"]]}'
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item`.
        item = {"table": table}
    
        # Construct fixed sized bucketing configuration
        fixed_size_bucketing_config = {
            "bucket_size": bucket_size,
            "lower_bound": {"integer_value": bucketing_lower_bound},
            "upper_bound": {"integer_value": bucketing_upper_bound},
        }
    
        # Specify fields to be de-identified
        deid_content_list = [{"name": _i} for _i in deid_content_list]
    
        # Construct Deidentify Config
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "fields": deid_content_list,
                        "primitive_transformation": {
                            "fixed_size_bucketing_config": fixed_size_bucketing_config
                        },
                    }
                ]
            }
        }
    
        # Call the API.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={"parent": parent, "deidentify_config": deidentify_config, "item": item}
        )
    
        # Print the results.
        print(f"Table after de-identification: {response.item.table}")
    
        # Return the response.
        return response.item.table
    
    

[ API Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2Ftestff%22%2C%22resource%22%3A%7B%22deidentifyConfig%22%3A%7B%22recordTransformations%22%3A%7B%22fieldTransformations%22%3A%5B%7B%22fields%22%3A%5B%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22fixedSizeBucketingConfig%22%3A%7B%22bucketSize%22%3A10%2C%22lowerBound%22%3A%7B%22integerValue%22%3A%220%22%7D%2C%22upperBound%22%3A%7B%22integerValue%22%3A%22100%22%7D%7D%7D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22AGE%22%7D%2C%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22integerValue%22%3A%22101%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%22%7D%2C%7B%22integerValue%22%3A%2295%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2225%22%7D%2C%7B%22stringValue%22%3A%22Jane%20Austen%22%7D%2C%7B%22integerValue%22%3A%2221%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2255%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%22%7D%2C%7B%22integerValue%22%3A%2275%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.
    
    
    "deidentifyConfig":{
      "recordTransformations":{
        "fieldTransformations":[
          {
            "fields":[
              {
                "name":"HAPPINESS SCORE"
              }
            ],
            "primitiveTransformation":{
              "fixedSizeBucketingConfig":{
                "bucketSize":10,
                "lowerBound":{
                  "integerValue":"0"
                },
                "upperBound":{
                  "integerValue":"100"
                }
              }
            }
          }
        ]
      }
    }
    

## Transform a column based on the value of another column

You can transform a column based on the value of another. This example redacts "HAPPINESS SCORE" for all patients over 89.

Input | Transformed table   
---|---  
| AGE | PATIENT | HAPPINESS SCORE  
---|---|---  
101 | Charles Dickens | 95  
22 | Jane Austen | 21  
55 | Mark Twain | 75  
| AGE | PATIENT | HAPPINESS SCORE  
---|---|---  
101 | Charles Dickens | **  
22 | Jane Austen | 21  
55 | Mark Twain | 75  
  
**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableUsingMaskingAndLogic
    {
        public static Table DeidentifyTable(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "101" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "95" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens name was a curse invented by Shakespeare." }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Jane Austin" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "21" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "There are 14 kisses in Jane Austen's novels." }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "55" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "75" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain loved cats." }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "FACTOID" }
                    },
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
    
            //Specify how the content should be de-identified.
            var primitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
            {
                CharacterMaskConfig = new [CharacterMaskConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharacterMaskConfig.html)
                {
                    MaskingCharacter = "*"
                }
            };
    
            // Specify the fields to be de-identified.
            var fields = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" } };
    
            // Specify when the above fields should be de-identified using condition.
            var condition = new RecordCondition.Types.Conditions
            {
                Conditions_ =
                {
                    new RecordCondition.Types.Condition
                    {
                        Field = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        Operator = [RelationalOperator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator.html).[GreaterThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator.html#Google_Cloud_Dlp_V2_RelationalOperator_GreaterThan),
                        Value = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 89 }
                    }
                }
            };
    
            // Apply the condition to records
            var recordCondition = new [RecordCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.html)
            {
                Expressions = new RecordCondition.Types.Expressions
                {
                    Conditions = condition
                }
            };
    
            // Associate the de-identification and conditions with the specified fields.
            var deidentifiedConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            PrimitiveTransformation = primitiveTransformation,
                            Fields = { fields },
                            Condition = recordCondition
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifiedConfig,
                Item = contentItem
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
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
    
    // deidentifyTableMaskingCondition de-identifies the table data using masking
    // and conditional logic
    func deidentifyTableMaskingCondition(w io.Writer, projectID string) error {
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
    			{Type: &dlppb.Value_StringValue{StringValue: "55"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "75"}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "101"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "95"}},
    		},
    	}
    
    	table := &dlppb.Table{
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
    			Table: table,
    		},
    	}
    
    	// Specify how the content should be de-identified.
    	charMaskConfig := &dlppb.CharacterMaskConfig{
    		MaskingCharacter: "*",
    	}
    	primitiveTransformation := &dlppb.PrimitiveTransformation_CharacterMaskConfig{
    		CharacterMaskConfig: charMaskConfig,
    	}
    
    	// Specify field to be de-identified.
    	fieldId := &dlppb.FieldId{
    		Name: "HAPPINESS SCORE",
    	}
    
    	// Apply the condition to the records present in table.
    	recordCondition := &dlppb.RecordCondition_Condition{
    		Field:    fieldId,
    		Operator: dlppb.[RelationalOperator_GREATER_THAN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_RelationalOperator_RELATIONAL_OPERATOR_UNSPECIFIED_RelationalOperator_EQUAL_TO_RelationalOperator_NOT_EQUAL_TO_RelationalOperator_GREATER_THAN_RelationalOperator_LESS_THAN_RelationalOperator_GREATER_THAN_OR_EQUALS_RelationalOperator_LESS_THAN_OR_EQUALS_RelationalOperator_EXISTS),
    		Value: &dlppb.Value{
    			Type: &dlppb.Value_IntegerValue{
    				IntegerValue: 89,
    			},
    		},
    	}
    
    	expression := &dlppb.RecordCondition_Expressions{
    		Type: &dlppb.RecordCondition_Expressions_Conditions{
    			Conditions: &dlppb.RecordCondition_Conditions{
    				Conditions: []*dlppb.RecordCondition_Condition{
    					recordCondition,
    				},
    			},
    		},
    	}
    
    	// Specify when the above field should be de-identified.
    	condition := &dlppb.RecordCondition{
    		// Apply the condition to records
    		Expressions: expression,
    	}
    
    	// Associate the de-identification and conditions with the specified field.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Fields: []*dlppb.FieldId{
    			fieldId,
    		},
    		Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    			PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    				Transformation: primitiveTransformation,
    			},
    		},
    		Condition: condition,
    	}
    
    	recordTransformations := &dlppb.RecordTransformations{
    		FieldTransformations: []*dlppb.FieldTransformation{
    			fieldTransformation,
    		},
    	}
    
    	// Combine configurations into a request for the service.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    				RecordTransformations: recordTransformations,
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
    	fmt.Fprintf(w, "Table after de-identification : %v", resp.GetItem().GetTable())
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
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Conditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Conditions.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Expressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Expressions.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[RelationalOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RelationalOperator.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    
    public class DeIdentifyTableConditionMasking {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("PATIENT").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("101").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charles Dickens").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("95").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("22").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Jane Austen").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("21").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("55").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("75").build())
                        .build())
                .build();
    
        deIdentifyTableConditionMasking(projectId, tableToDeIdentify);
      }
    
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyTableConditionMasking(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify how the content should be de-identified.
          [CharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.html) characterMaskConfig =
              [CharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.html).newBuilder().[setMaskingCharacter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.Builder.html#com_google_privacy_dlp_v2_CharacterMaskConfig_Builder_setMaskingCharacter_java_lang_String_)("*").build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder().[setCharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCharacterMaskConfig_com_google_privacy_dlp_v2_CharacterMaskConfig_)(characterMaskConfig).build();
    
          // Specify field to be de-identified.
          [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html) fieldId = [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build();
    
          // Specify when the above field should be de-identified.
          [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html) condition =
              [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html).newBuilder()
                  .setField([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                  .[setOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.Builder.html#com_google_privacy_dlp_v2_RecordCondition_Condition_Builder_setOperator_com_google_privacy_dlp_v2_RelationalOperator_)([RelationalOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RelationalOperator.html).GREATER_THAN)
                  .setValue([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(89).build())
                  .build();
          // Apply the condition to records
          [RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html) recordCondition =
              [RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).newBuilder()
                  .setExpressions(
                      [Expressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Expressions.html).newBuilder()
                          .setConditions([Conditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Conditions.html).newBuilder().addConditions(condition).build())
                          .build())
                  .build();
    
          // Associate the de-identification and conditions with the specified field.
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .[addFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addFields_com_google_privacy_dlp_v2_FieldId_)(fieldId)
                  .setCondition(recordCondition)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize google DLP Client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // Construct the tabular data
    const tablularData = {
      headers: [{name: 'AGE'}, {name: 'PATIENT'}, {name: 'HAPPINESS SCORE'}],
      rows: [
        {
          values: [
            {integerValue: 101},
            {stringValue: 'Charles Dickens'},
            {integerValue: 95},
          ],
        },
        {
          values: [
            {integerValue: 22},
            {stringValue: 'Jane Austen'},
            {integerValue: 21},
          ],
        },
        {
          values: [
            {integerValue: 55},
            {stringValue: 'Mark Twain'},
            {integerValue: 75},
          ],
        },
      ],
    };
    
    async function deIdentifyTableConditionalCharMasking() {
      // Column that needs to be transformed
      const fieldIds = [{name: 'HAPPINESS SCORE'}];
    
      // Construct PrimitiveTransformation configuration
      const primitiveTransformation = {
        characterMaskConfig: {
          maskingCharacter: '*',
        },
      };
    
      // Construct condition
      const condition = {
        expressions: {
          conditions: {
            conditions: [
              {
                field: {name: 'AGE'},
                operator: '[GREATER_THAN](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.relationaloperator.html)',
                value: {integerValue: 89},
              },
            ],
          },
        },
      };
    
      // Construct RecordTransformations configurations
      const recordTransformations = {
        fieldTransformations: [
          {
            primitiveTransformation,
            fields: fieldIds,
            condition,
          },
        ],
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: {
          table: tablularData,
        },
        deidentifyConfig: {
          recordTransformations,
        },
      };
      // Send the request and receive response from the service
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    
    deIdentifyTableConditionalCharMasking();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\CharacterMaskConfig;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordCondition;
    use Google\Cloud\Dlp\V2\RecordCondition\Condition;
    use Google\Cloud\Dlp\V2\RecordCondition\Conditions;
    use Google\Cloud\Dlp\V2\RecordCondition\Expressions;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\RelationalOperator;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data using masking and conditional logic.
     * Transform a column based on the value of another column.
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to deidentify
     * @param string $outputCsvFile         The oupt file path to save deidentify content
     */
    
    function deidentify_table_condition_masking(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table2.csv',
        string $outputCsvFile = './test/data/deidentify_table_condition_masking_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
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
    
        // Construct the table object
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify what content you want the service to de-identify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify how the content should be de-identified.
        $characterMaskConfig = (new CharacterMaskConfig())
            ->setMaskingCharacter('*');
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCharacterMaskConfig($characterMaskConfig);
    
        // Specify field to be de-identified.
        $fieldId = (new FieldId())
            ->setName('HAPPINESS_SCORE');
    
        // Specify when the above fields should be de-identified.
        $condition = (new Condition())
            ->setField((new FieldId())
                ->setName('AGE'))
            ->setOperator(RelationalOperator::GREATER_THAN)
            ->setValue((new Value())
                ->setIntegerValue(89));
    
        // Apply the condition to records
        $recordCondition = (new RecordCondition())
            ->setExpressions((new Expressions())
                    ->setConditions((new Conditions())
                            ->setConditions([$condition])
                    )
            );
    
        // Associate the de-identification and conditions with the specified fields.
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields([$fieldId])
            ->setCondition($recordCondition);
    
        $recordtransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print results
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf('After de-identify the table data (Output File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    from google.cloud.dlp_v2 import [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html)
    
    
    def deidentify_table_condition_masking(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        deid_content_list: List[str],
        condition_field: str = None,
        condition_operator: str = None,
        condition_value: int = None,
        masking_character: str = None,
    ) -> types.dlp.Table:
        """ Uses the Data Loss Prevention API to de-identify sensitive data in a
          table by masking them based on a condition.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_data: Json string representing table data.
            deid_content_list: A list of fields in table to de-identify.
            condition_field: A table Field within the record this condition is evaluated against.
            condition_operator: Operator used to compare the field or infoType to the value. One of:
                RELATIONAL_OPERATOR_UNSPECIFIED, EQUAL_TO, NOT_EQUAL_TO, GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUALS,
                LESS_THAN_OR_EQUALS, EXISTS.
            condition_value: Value to compare against. [Mandatory, except for ``EXISTS`` tests.].
            masking_character: The character to mask matching sensitive data with.
    
        Returns:
            De-identified table is returned;
            the response from the API is also printed to the terminal.
    
        Example:
        >> $ python deidentify_table_condition_masking.py \
        '{"header": ["email", "phone number", "age", "happiness_score"],
        "rows": [["robertfrost@example.com", "4232342345", "35", "21"],
        ["johndoe@example.com", "4253458383", "64", "34"]]}' \
        ["happiness_score"] "age" "GREATER_THAN" 50
        >> '{"header": ["email", "phone number", "age", "happiness_score"],
            "rows": [["robertfrost@example.com", "4232342345", "35", "21"],
            ["johndoe@example.com", "4253458383", "64", "**"]]}'
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item`
        item = {"table": table}
    
        # Specify fields to be de-identified
        deid_content_list = [{"name": _i} for _i in deid_content_list]
    
        # Construct condition list
        condition = [
            {
                "field": {"name": condition_field},
                "operator": condition_operator,
                "value": {"integer_value": condition_value},
            }
        ]
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "primitive_transformation": {
                            "character_mask_config": {
                                "masking_character": masking_character
                            }
                        },
                        "fields": deid_content_list,
                        "condition": {
                            "expressions": {"conditions": {"conditions": condition}}
                        },
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
    
        # Print the result
        print(f"Table after de-identification: {response.item.table}")
    
        # Return the response
        return response.item.table
    
    

[ API Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2Ftestff%22%2C%22resource%22%3A%7B%22deidentifyConfig%22%3A%7B%22recordTransformations%22%3A%7B%22fieldTransformations%22%3A%5B%7B%22fields%22%3A%5B%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22characterMaskConfig%22%3A%7B%22maskingCharacter%22%3A%22*%22%7D%7D%2C%22condition%22%3A%7B%22expressions%22%3A%7B%22conditions%22%3A%7B%22conditions%22%3A%5B%7B%22field%22%3A%7B%22name%22%3A%22AGE%22%7D%2C%22operator%22%3A%22GREATER_THAN%22%2C%22value%22%3A%7B%22integerValue%22%3A%2289%22%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22AGE%22%7D%2C%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22integerValue%22%3A%22101%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%22%7D%2C%7B%22integerValue%22%3A%2295%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2225%22%7D%2C%7B%22stringValue%22%3A%22Jane%20Austen%22%7D%2C%7B%22integerValue%22%3A%2221%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2255%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%22%7D%2C%7B%22integerValue%22%3A%2275%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.
    
    
    "deidentifyConfig":{
      "recordTransformations":{
        "fieldTransformations":[
          {
            "fields":[
              {
                "name":"HAPPINESS SCORE"
              }
            ],
            "primitiveTransformation":{
              "characterMaskConfig":{
                "maskingCharacter":"*"
              }
            },
            "condition":{
              "expressions":{
                "conditions":{
                  "conditions":[
                    {
                      "field":{
                        "name":"AGE"
                      },
                      "operator":"GREATER_THAN",
                      "value":{
                        "integerValue":"89"
                      }
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    }
    

## Transform findings found in columns

You can transform findings that make up either only part of a cell's content or all of it. In this example, all instances of `PERSON_NAME` are anonymized.

Input | Transformed table   
---|---  
| AGE | PATIENT | HAPPINESS SCORE | FACTOID  
---|---|---|---  
101 | Charles Dickens | 95 | Charles Dickens name was a curse, possibly invented by Shakespeare.  
22 | Jane Austen | 21 | There are 14 kisses in Jane Austen's novels.  
55 | Mark Twain | 75 | Mark Twain loved cats.  
| AGE | PATIENT | HAPPINESS SCORE | FACTOID  
---|---|---|---  
101 | [PERSON_NAME] | 95 | [PERSON_NAME] name was a curse, possibly invented by Shakespeare.  
22 | [PERSON_NAME] | 21 | There are 14 kisses in [PERSON_NAME] novels.  
55 | [PERSON_NAME] | 75 | [PERSON_NAME] loved cats.  
  
**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableWithInfoTypes
    {
        public static Table DeidentifyTable(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null,
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "101" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "95" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens name was a curse invented by Shakespeare." }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Jane Austin" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "21" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "There are 14 kisses in Jane Austen's novels." }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "55" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "75" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain loved cats." }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "FACTOID" }
                    },
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
    
            // Construct Replace With InfoTypes config to replace the match.
            var replaceInfoTypesConfig = new [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceWithInfoTypeConfig.html)();
    
            // Construct Fields to be de-identified.
            var fieldIds = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" }, new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "FACTOID" } };
    
            // Construct InfoType Transformation.
            var infoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
            {
                Transformations =
                {
                    new InfoTypeTransformations.Types.InfoTypeTransformation
                    {
                        PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                        {
                            ReplaceWithInfoTypeConfig = replaceInfoTypesConfig
                        },
                        InfoTypes = { infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } } }
                    }
                }
            };
    
            // Construct the de-identify config using replace config.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            InfoTypeTransformations = infoTypeTransformations,
                            Fields = { fieldIds }
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
            Console.WriteLine(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
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
    
    // deidentifyTableInfotypes de-identifies table data with info types
    func deidentifyTableInfotypes(w io.Writer, projectID string) error {
    	// projectId := "your-project-id"
    
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "22"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Jane Austen"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "21"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "There are 14 kisses in Jane Austen's novels."}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "55"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "75"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain loved cats."}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "101"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "95"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens name was a curse invented by Shakespeare."}},
    		},
    	}
    
    	table := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "AGE"},
    			{Name: "PATIENT"},
    			{Name: "HAPPINESS SCORE"},
    			{Name: "FACTOID"},
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
    	client, err := dlp.[NewRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewRESTClient)(ctx)
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
    
    	// Specify how the content should be de-identified.
    	// Select type of info to be replaced.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PERSON_NAME"},
    	}
    
    	// Specify that findings should be replaced with corresponding info type name.
    	replaceWithInfoTypeConfig := &dlppb.ReplaceWithInfoTypeConfig{}
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_ReplaceWithInfoTypeConfig{
    			ReplaceWithInfoTypeConfig: replaceWithInfoTypeConfig,
    		},
    	}
    
    	// Associate info type with the replacement strategy
    	infoTypeTransformations := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			{
    				InfoTypes:               infoTypes,
    				PrimitiveTransformation: primitiveTransformation,
    			},
    		},
    	}
    
    	// Specify fields to be de-identified.
    	fields := []*dlppb.FieldId{
    		{Name: "PATIENT"},
    		{Name: "FACTOID"},
    	}
    
    	// Associate the de-identification and conditions with the specified field.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Fields: fields,
    		Transformation: &dlppb.FieldTransformation_InfoTypeTransformations{
    			InfoTypeTransformations: infoTypeTransformations,
    		},
    	}
    
    	recordTransformations := &dlppb.RecordTransformations{
    		FieldTransformations: []*dlppb.FieldTransformation{
    			fieldTransformation,
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    				RecordTransformations: recordTransformations,
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
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class DeIdentifyTableInfoTypes {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("PATIENT").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("FACTOID").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("101").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charles Dickens").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("95").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "Charles Dickens name was a curse invented by Shakespeare.")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("22").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Jane Austen").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("21").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("There are 14 kisses in Jane Austen's novels.")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("55").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("75").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain loved cats.").build())
                        .build())
                .build();
    
        deIdentifyTableInfoTypes(projectId, tableToDeIdentify);
      }
    
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyTableInfoTypes(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify how the content should be de-identified.
          // Select type of info to be replaced.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
          // Specify that findings should be replaced with corresponding info type name.
          [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html) replaceWithInfoTypeConfig =
              [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html).getDefaultInstance();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setReplaceWithInfoTypeConfig_com_google_privacy_dlp_v2_ReplaceWithInfoTypeConfig_)(replaceWithInfoTypeConfig)
                  .build();
          // Associate info type with the replacement strategy
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) infoTypeTransformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          // Specify fields to be de-identified.
          List<FieldId> fieldIds =
              Stream.of("PATIENT", "FACTOID")
                  .map(id -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(id).build())
                  .collect(Collectors.toList());
    
          // Associate the de-identification and conditions with the specified field.
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .setInfoTypeTransformations(infoTypeTransformations)
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(fieldIds)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize google DLP Client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // Construct the tabular data
    const tablularData = {
      headers: [
        {name: 'AGE'},
        {name: 'PATIENT'},
        {name: 'HAPPINESS SCORE'},
        {name: 'FACTOID'},
      ],
      rows: [
        {
          values: [
            {integerValue: 101},
            {stringValue: 'Charles Dickens'},
            {integerValue: 95},
            {
              stringValue:
                'Charles Dickens name was a curse invented by Shakespeare.',
            },
          ],
        },
        {
          values: [
            {integerValue: 22},
            {stringValue: 'Jane Austen'},
            {integerValue: 21},
            {stringValue: "There are 14 kisses in Jane Austen's novels."},
          ],
        },
        {
          values: [
            {integerValue: 55},
            {stringValue: 'Mark Twain'},
            {integerValue: 75},
            {stringValue: 'Mark Twain loved cats.'},
          ],
        },
      ],
    };
    
    async function deIdentifyTableWithInfoType() {
      // Column that needs to be transformed
      const fieldIds = [{name: 'PATIENT'}, {name: 'FACTOID'}];
    
      // Construct InfoTypeTransformations configurations
      const infoTypeTransformations = {
        transformations: [
          {
            infoTypes: [{name: 'PERSON_NAME'}],
            primitiveTransformation: {
              replaceWithInfoTypeConfig: {},
            },
          },
        ],
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: {
          table: tablularData,
        },
        deidentifyConfig: {
          recordTransformations: {
            fieldTransformations: [
              {
                infoTypeTransformations,
                fields: fieldIds,
              },
            ],
          },
        },
      };
      // Send the request and receive response from the service
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    
    deIdentifyTableWithInfoType();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\ReplaceWithInfoTypeConfig;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data with infoTypes
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to deidentify
     * @param string $outputCsvFile         The oupt file path to save deidentify content
     */
    
    function deidentify_table_infotypes(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table1.csv',
        string $outputCsvFile = './test/data/deidentify_table_infotypes_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
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
    
        // Construct the table object
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify the content to be inspected.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify the type of info the inspection will look for.
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
    
        // Specify that findings should be replaced with corresponding info type name.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setReplaceWithInfoTypeConfig(new ReplaceWithInfoTypeConfig());
    
        // Associate info type with the replacement strategy
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes([$personNameInfoType]);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Specify fields to be de-identified.
        $fieldIds = [
            (new FieldId())->setName('PATIENT'),
            (new FieldId())->setName('FACTOID'),
        ];
    
        // Associate the de-identification and transformation with the specified fields.
        $fieldTransformation = (new FieldTransformation())
            ->setInfoTypeTransformations($infoTypeTransformations)
            ->setFields($fieldIds);
    
        $recordtransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf('After de-identify the table data (Output File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    
    
    def deidentify_table_replace_with_info_types(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        info_types: List[str],
        deid_content_list: List[str],
    ) -> None:
        """ Uses the Data Loss Prevention API to de-identify sensitive data in a
          table by replacing them with info type.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_data: Json string representing table data.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            deid_content_list: A list of fields in table to de-identify
    
        Returns:
            None; the response from the API is printed to the terminal.
    
        Example:
        >> $ python deidentify_table_infotypes.py \
        '{
            "header": ["name", "email", "phone number"],
            "rows": [
                ["Robert Frost", "robertfrost@example.com", "4232342345"],
                ["John Doe", "johndoe@example.com", "4253458383"]
            ]
        }' \
        ["PERSON_NAME"] ["name"]
        >> '{
                "header": ["name", "email", "phone number"],
                "rows": [
                    ["[PERSON_NAME]", "robertfrost@example.com", "4232342345"],
                    ["[PERSON_NAME]", "johndoe@example.com", "4253458383"]
                ]
            }'
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct item
        item = {"table": table}
    
        # Specify fields to be de-identified
        deid_content_list = [{"name": _i} for _i in deid_content_list]
    
        # Construct inspect configuration dictionary
        inspect_config = {"info_types": [{"name": info_type} for info_type in info_types]}
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "info_type_transformations": {
                            "transformations": [
                                {
                                    "primitive_transformation": {
                                        "replace_with_info_type_config": {}
                                    }
                                }
                            ]
                        },
                        "fields": deid_content_list,
                    }
                ]
            }
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "item": item,
                "inspect_config": inspect_config,
            }
        )
    
        # Print the result
        print(f"Table after de-identification: {response.item.table}")
    
    

[APIs Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2Ftestff%22%2C%22resource%22%3A%7B%22deidentifyConfig%22%3A%7B%22recordTransformations%22%3A%7B%22fieldTransformations%22%3A%5B%7B%22infoTypeTransformations%22%3A%7B%22transformations%22%3A%5B%7B%22infoTypes%22%3A%5B%7B%22name%22%3A%22PERSON_NAME%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22replaceWithInfoTypeConfig%22%3A%7B%7D%7D%7D%5D%7D%2C%22fields%22%3A%5B%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22FACTOID%22%7D%5D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22AGE%22%7D%2C%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%2C%7B%22name%22%3A%22FACTOID%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22integerValue%22%3A%22101%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%22%7D%2C%7B%22integerValue%22%3A%2295%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%20name%20was%20a%20curse%2C%20possibly%20invented%20by%20Shakespeare.%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2225%22%7D%2C%7B%22stringValue%22%3A%22Jane%20Austen%22%7D%2C%7B%22integerValue%22%3A%2221%22%7D%2C%7B%22stringValue%22%3A%22There%20are%2014%20kisses%20in%20Jane%20Austen%27s%20novels.%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2255%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%22%7D%2C%7B%22integerValue%22%3A%2275%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%20loved%20cats.%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.
    
    
    "deidentifyConfig":{
      "recordTransformations":{
        "fieldTransformations":[
          {
            "infoTypeTransformations":{
              "transformations":[
                {
                  "infoTypes":[
                    {
                      "name":"PERSON_NAME"
                    }
                  ],
                  "primitiveTransformation":{
                    "replaceWithInfoTypeConfig":{
    
                    }
                  }
                }
              ]
            },
            "fields":[
              {
                "name":"PATIENT"
              },
              {
                "name":"FACTOID"
              }
            ]
          }
        ]
      }
    }
    

## Suppress a row based on the content of a column

You can remove a row entirely based on the content that appears in any column. This example suppresses the record for "Charles Dickens," as this patient is over 89 years old.

Input | Transformed table   
---|---  
| AGE | PATIENT | HAPPINESS SCORE  
---|---|---  
101 | Charles Dickens | 95  
22 | Jane Austen | 21  
55 | Mark Twain | 75  
| AGE | PATIENT | HAPPINESS SCORE  
---|---|---  
22 | Jane Austen | 21  
55 | Mark Twain | 75  
  
**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableWithRowSuppress
    {
        public static Table DeidentifyTable(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "101" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "95" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Jane Austin" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "21" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "55" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "75" }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" }
                    },
                    Rows =
                    {
                        new Table.Types.Row { Values = { row1 } },
                        new Table.Types.Row { Values = { row2 } },
                        new Table.Types.Row { Values = { row3 } }
                    }
                };
            }
    
            // Construct the byte content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToInspect };
    
            // Construct the conditions.
            var conditions = new RecordCondition.Types.Conditions
            {
                Conditions_ =
                {
                    new RecordCondition.Types.Condition
                    {
                        Field = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        Operator = [RelationalOperator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator.html).[GreaterThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator.html#Google_Cloud_Dlp_V2_RelationalOperator_GreaterThan),
                        Value = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 89 }
                    }
                }
            };
    
            // Construct the deidentify config using the record suppression and conditions.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    RecordSuppressions =
                    {
                        new [RecordSuppression](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordSuppression.html)
                        {
                            Condition = new [RecordCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.html)
                            {
                                Expressions = new RecordCondition.Types.Expressions
                                {
                                    Conditions = conditions
                                }
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
            Console.WriteLine(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
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
    
    // deidentifyTableRowSuppress de-identifies table data and
    // suppress a row based on the content of column
    func deidentifyTableRowSuppress(w io.Writer, projectID string) error {
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
    			{Type: &dlppb.Value_StringValue{StringValue: "55"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "75"}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "101"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "95"}},
    		},
    	}
    
    	table := &dlppb.Table{
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
    			Table: table,
    		},
    	}
    
    	// Apply the condition to record suppression.
    	condition := &dlppb.RecordCondition{
    		Expressions: &dlppb.RecordCondition_Expressions{
    			Type: &dlppb.RecordCondition_Expressions_Conditions{
    				Conditions: &dlppb.RecordCondition_Conditions{
    					Conditions: []*dlppb.RecordCondition_Condition{
    						{
    							Field:    &dlppb.FieldId{Name: "AGE"},
    							Operator: dlppb.[RelationalOperator_GREATER_THAN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_RelationalOperator_RELATIONAL_OPERATOR_UNSPECIFIED_RelationalOperator_EQUAL_TO_RelationalOperator_NOT_EQUAL_TO_RelationalOperator_GREATER_THAN_RelationalOperator_LESS_THAN_RelationalOperator_GREATER_THAN_OR_EQUALS_RelationalOperator_LESS_THAN_OR_EQUALS_RelationalOperator_EXISTS),
    							Value: &dlppb.Value{
    								Type: &dlppb.Value_IntegerValue{IntegerValue: 89},
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    	recordSupression := &dlppb.RecordSuppression{
    		Condition: condition,
    	}
    
    	// Use record suppression as the only transformation
    	recordTransformations := &dlppb.RecordTransformations{
    		RecordSuppressions: []*dlppb.RecordSuppression{
    			recordSupression,
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    				RecordTransformations: recordTransformations,
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
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Conditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Conditions.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Expressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Expressions.html);
    import com.google.privacy.dlp.v2.[RecordSuppression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordSuppression.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[RelationalOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RelationalOperator.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    
    public class DeIdentifyTableRowSuppress {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("PATIENT").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("101").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charles Dickens").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("95").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("22").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Jane Austen").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("21").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("55").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("75").build())
                        .build())
                .build();
    
        deIdentifyTableRowSuppress(projectId, tableToDeIdentify);
      }
    
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyTableRowSuppress(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify when the content should be de-identified.
          [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html) condition =
              [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html).newBuilder()
                  .setField([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                  .[setOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.Builder.html#com_google_privacy_dlp_v2_RecordCondition_Condition_Builder_setOperator_com_google_privacy_dlp_v2_RelationalOperator_)([RelationalOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RelationalOperator.html).GREATER_THAN)
                  .setValue([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(89).build())
                  .build();
          // Apply the condition to record suppression.
          [RecordSuppression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordSuppression.html) recordSuppressions =
              [RecordSuppression](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordSuppression.html).newBuilder()
                  .setCondition(
                      [RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).newBuilder()
                          .setExpressions(
                              [Expressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Expressions.html).newBuilder()
                                  .setConditions(
                                      [Conditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Conditions.html).newBuilder().addConditions(condition).build())
                                  .build())
                          .build())
                  .build();
          // Use record suppression as the only transformation
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) transformations =
              [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder().[addRecordSuppressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.Builder.html#com_google_privacy_dlp_v2_RecordTransformations_Builder_addRecordSuppressions_com_google_privacy_dlp_v2_RecordSuppression_)(recordSuppressions).build();
    
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize google DLP Client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // Construct the tabular data
    const tablularData = {
      headers: [{name: 'AGE'}, {name: 'PATIENT'}, {name: 'HAPPINESS SCORE'}],
      rows: [
        {
          values: [
            {integerValue: 101},
            {stringValue: 'Charles Dickens'},
            {integerValue: 95},
          ],
        },
        {
          values: [
            {integerValue: 22},
            {stringValue: 'Jane Austen'},
            {integerValue: 21},
          ],
        },
        {
          values: [
            {integerValue: 55},
            {stringValue: 'Mark Twain'},
            {integerValue: 75},
          ],
        },
      ],
    };
    async function deIdentifyTableRowSuppress() {
      // Specify when the content should be de-identified.
      const condition = {
        expressions: {
          conditions: {
            conditions: [
              {
                field: {name: 'AGE'},
                operator: '[GREATER_THAN](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.relationaloperator.html)',
                value: {integerValue: 89},
              },
            ],
          },
        },
      };
    
      // Apply the condition to record suppression.
      const recordTransformations = {
        recordSuppressions: [
          {
            condition,
          },
        ],
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: {
          table: tablularData,
        },
        deidentifyConfig: {
          recordTransformations,
        },
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results.
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    
    deIdentifyTableRowSuppress();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\RecordCondition;
    use Google\Cloud\Dlp\V2\RecordCondition\Condition;
    use Google\Cloud\Dlp\V2\RecordCondition\Conditions;
    use Google\Cloud\Dlp\V2\RecordCondition\Expressions;
    use Google\Cloud\Dlp\V2\RecordSuppression;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\RelationalOperator;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data: Suppress a row based on the content of a column
     * Suppress a row based on the content of a column. You can remove a row entirely based on the content that appears in any column. This example suppresses the record for "Charles Dickens," as this patient is over 89 years old.
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to deidentify
     * @param string $outputCsvFile         The oupt file path to save deidentify content */
    
    function deidentify_table_row_suppress(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table2.csv',
        string $outputCsvFile = './test/data/deidentify_table_row_suppress_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
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
    
        // Construct the table object
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify what content you want the service to de-identify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify when the content should be de-identified.
        $condition = (new Condition())
            ->setField((new FieldId())
                ->setName('AGE'))
            ->setOperator(RelationalOperator::GREATER_THAN)
            ->setValue((new Value())
                ->setIntegerValue(89));
    
        // Apply the condition to record suppression.
        $recordSuppressions = (new RecordSuppression())
            ->setCondition((new RecordCondition())
                    ->setExpressions((new Expressions())
                            ->setConditions((new Conditions())
                                    ->setConditions([$condition])
                            )
                    )
            );
    
        // Use record suppression as the only transformation
        $recordtransformations = (new RecordTransformations())
            ->setRecordSuppressions([$recordSuppressions]);
    
        // Create the deidentification configuration object
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf($outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    
    
    def deidentify_table_suppress_row(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        condition_field: str,
        condition_operator: str,
        condition_value: int,
    ) -> None:
        """ Uses the Data Loss Prevention API to de-identify sensitive data in a
          table by suppressing entire row/s based on a condition.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_data: Dictionary representing table data.
            condition_field: A table field within the record this condition is evaluated against.
            condition_operator: Operator used to compare the field or infoType to the value. One of:
                RELATIONAL_OPERATOR_UNSPECIFIED, EQUAL_TO, NOT_EQUAL_TO, GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUALS,
                LESS_THAN_OR_EQUALS, EXISTS.
            condition_value: Value to compare against. [Mandatory, except for ``EXISTS`` tests.].
    
        Example:
    
        >> $ python deidentify_table_row_suppress.py \
        '{"header": ["email", "phone number", "age"],
        "rows": [["robertfrost@example.com", "4232342345", "35"],
        ["johndoe@example.com", "4253458383", "64"]]}' \
        "age" "GREATER_THAN" 50
        >> '{"header": ["email", "phone number", "age"],
            "rows": [["robertfrost@example.com", "4232342345", "35", "21"]]}'
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item` containing the table data.
        item = {"table": table}
    
        # Construct condition list.
        condition = [
            {
                "field": {"name": condition_field},
                "operator": condition_operator,
                "value": {"integer_value": condition_value},
            }
        ]
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "record_transformations": {
                "record_suppressions": [
                    {
                        "condition": {
                            "expressions": {"conditions": {"conditions": condition}}
                        }
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
    
        # Print the result.
        print(f"Table after de-identification: {response.item.table}")
    
    

[APIs Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2Ftestff%22%2C%22resource%22%3A%7B%22deidentifyConfig%22%3A%7B%22recordTransformations%22%3A%7B%22recordSuppressions%22%3A%5B%7B%22condition%22%3A%7B%22expressions%22%3A%7B%22conditions%22%3A%7B%22conditions%22%3A%5B%7B%22field%22%3A%7B%22name%22%3A%22AGE%22%7D%2C%22operator%22%3A%22GREATER_THAN%22%2C%22value%22%3A%7B%22integerValue%22%3A%2289%22%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22AGE%22%7D%2C%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22integerValue%22%3A%22101%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%22%7D%2C%7B%22integerValue%22%3A%2295%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2225%22%7D%2C%7B%22stringValue%22%3A%22Jane%20Austen%22%7D%2C%7B%22integerValue%22%3A%2221%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2255%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%22%7D%2C%7B%22integerValue%22%3A%2275%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.
    
    
    "deidentifyConfig":{
      "recordTransformations":{
        "recordSuppressions":[
          {
            "condition":{
              "expressions":{
                "conditions":{
                  "conditions":[
                    {
                      "field":{
                        "name":"AGE"
                      },
                      "operator":"GREATER_THAN",
                      "value":{
                        "integerValue":"89"
                      }
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    }
    

## Transform findings only when specific conditions are met on another field

In this example, the `PERSON_NAME` findings are only redacted if the "AGE" column indicates the patient is over the age of 89.

Input | Transformed table   
---|---  
| AGE | PATIENT | HAPPINESS SCORE | FACTOID  
---|---|---|---  
101 | Charles Dickens | 95 | Charles Dickens name was a curse, possibly invented by Shakespeare.  
22 | Jane Austen | 21 | There are 14 kisses in Jane Austen's novels.  
55 | Mark Twain | 75 | Mark Twain loved cats.  
| AGE | PATIENT | HAPPINESS SCORE | FACTOID  
---|---|---|---  
101 | [PERSON_NAME] | 95 | [PERSON_NAME] name was a curse, possibly invented by [PERSON_NAME].  
22 | Jane Austen | 21 | There are 14 kisses in Jane Austen's novels.  
55 | Mark Twain | 75 | Mark Twain loved cats.  
  
**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableUsingLogicInfoTypes
    {
        public static Table Deidentify(
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
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "101" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "95" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Charles Dickens name was a curse invented by Shakespeare." }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Jane Austin" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "21" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "There are 14 kisses in Jane Austen's novels." }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "55" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "75" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Mark Twain loved cats." }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "HAPPINESS SCORE" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "FACTOID" }
                    },
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
    
            // Specify that findings should be replaced with corresponding info type name.
            var infoTypeTransformation = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
            {
                Transformations =
                {
                    new InfoTypeTransformations.Types.InfoTypeTransformation
                    {
                        InfoTypes = { infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } } },
                        PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                        {
                            ReplaceWithInfoTypeConfig = new [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceWithInfoTypeConfig.html)()
                        }
                    }
                }
            };
    
            // Specify the fields to be de-identified.
            var fields = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "PATIENT" }, new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "FACTOID" } };
    
            // Specify when the above fields should be de-identified using condition.
            var condition = new RecordCondition.Types.Conditions
            {
                Conditions_ =
                {
                    new RecordCondition.Types.Condition
                    {
                        Field = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "AGE" },
                        Operator = [RelationalOperator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator.html).[GreaterThan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RelationalOperator.html#Google_Cloud_Dlp_V2_RelationalOperator_GreaterThan),
                        Value = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 89 }
                    }
                }
            };
    
            // Apply the condition to records.
            var recordCondition = new [RecordCondition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordCondition.html)
            {
                Expressions = new RecordCondition.Types.Expressions
                {
                    Conditions = condition
                }
            };
    
            // Associate the de-identification and conditions with the specified fields.
            var deidentifiedConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            InfoTypeTransformations = infoTypeTransformation,
                            Fields = { fields },
                            Condition = recordCondition
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifiedConfig,
                Item = contentItem
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
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
    
    // deidentifyTableConditionInfoTypes de-identifies table data
    // using conditional logic and replace with infoTypes
    func deidentifyTableConditionInfoTypes(w io.Writer, projectID string, columnNames []string) error {
    	// projectId := "your-project-id"
    	// columnNames := []string{"PATIENT", "FACTOID"}
    
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "22"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Jane Austen"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "21"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "There are 14 kisses in Jane Austen's novels."}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "55"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "75"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain loved cats."}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "101"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "95"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens name was a curse invented by Shakespeare."}},
    		},
    	}
    
    	table := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "AGE"},
    			{Name: "PATIENT"},
    			{Name: "HAPPINESS SCORE"},
    			{Name: "FACTOID"},
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
    
    	// Specify how the content should be de-identified.
    	// Select type of info to be replaced.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PERSON_NAME"},
    	}
    
    	// Specify that findings should be replaced with corresponding info type name.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_ReplaceWithInfoTypeConfig{},
    	}
    
    	// Associate info type with the replacement strategy
    	infoTypeTransformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		InfoTypes:               infoTypes,
    		PrimitiveTransformation: primitiveTransformation,
    	}
    
    	infoTypeTransformations := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			infoTypeTransformation,
    		},
    	}
    
    	// Specify fields to be de-identified.
    	var f []*dlppb.FieldId
    	for _, c := range columnNames {
    		f = append(f, &dlppb.FieldId{Name: c})
    	}
    
    	// Specify when the above fields should be de-identified.
    	condition := &dlppb.RecordCondition{
    		Expressions: &dlppb.RecordCondition_Expressions{
    			Type: &dlppb.RecordCondition_Expressions_Conditions{
    				Conditions: &dlppb.RecordCondition_Conditions{
    					Conditions: []*dlppb.RecordCondition_Condition{
    						{
    							Field: &dlppb.FieldId{
    								Name: "AGE",
    							},
    							Operator: dlppb.[RelationalOperator_GREATER_THAN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_RelationalOperator_RELATIONAL_OPERATOR_UNSPECIFIED_RelationalOperator_EQUAL_TO_RelationalOperator_NOT_EQUAL_TO_RelationalOperator_GREATER_THAN_RelationalOperator_LESS_THAN_RelationalOperator_GREATER_THAN_OR_EQUALS_RelationalOperator_LESS_THAN_OR_EQUALS_RelationalOperator_EXISTS),
    							Value: &dlppb.Value{
    								Type: &dlppb.Value_IntegerValue{
    									IntegerValue: 89,
    								},
    							},
    						},
    					},
    				},
    			},
    		},
    	}
    
    	// Associate the de-identification and conditions with the specified fields.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Fields:    f,
    		Condition: condition,
    		Transformation: &dlppb.FieldTransformation_InfoTypeTransformations{
    			InfoTypeTransformations: infoTypeTransformations,
    		},
    	}
    
    	recordTransformations := &dlppb.RecordTransformations{
    		FieldTransformations: []*dlppb.FieldTransformation{
    			fieldTransformation,
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    				RecordTransformations: recordTransformations,
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
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Conditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Conditions.html);
    import com.google.privacy.dlp.v2.[RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).[Expressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Expressions.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[RelationalOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RelationalOperator.html);
    import com.google.privacy.dlp.v2.[ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class DeIdentifyTableConditionInfoTypes {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("PATIENT").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("FACTOID").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("101").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charles Dickens").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("95").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "Charles Dickens name was a curse invented by Shakespeare.")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("22").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Jane Austen").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("21").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("There are 14 kisses in Jane Austen's novels.")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("55").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("75").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain loved cats.").build())
                        .build())
                .build();
    
        deIdentifyTableConditionInfoTypes(projectId, tableToDeIdentify);
      }
    
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyTableConditionInfoTypes(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify how the content should be de-identified.
          // Select type of info to be replaced.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
          // Specify that findings should be replaced with corresponding info type name.
          [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html) replaceWithInfoTypeConfig =
              [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html).getDefaultInstance();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setReplaceWithInfoTypeConfig_com_google_privacy_dlp_v2_ReplaceWithInfoTypeConfig_)(replaceWithInfoTypeConfig)
                  .build();
          // Associate info type with the replacement strategy
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) infoTypeTransformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          // Specify fields to be de-identified.
          List<FieldId> fieldIds =
              Stream.of("PATIENT", "FACTOID")
                  .map(id -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(id).build())
                  .collect(Collectors.toList());
    
          // Specify when the above fields should be de-identified.
          [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html) condition =
              [Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.html).newBuilder()
                  .setField([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                  .[setOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Condition.Builder.html#com_google_privacy_dlp_v2_RecordCondition_Condition_Builder_setOperator_com_google_privacy_dlp_v2_RelationalOperator_)([RelationalOperator](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RelationalOperator.html).GREATER_THAN)
                  .setValue([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(89).build())
                  .build();
          // Apply the condition to records
          [RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html) recordCondition =
              [RecordCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.html).newBuilder()
                  .setExpressions(
                      [Expressions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Expressions.html).newBuilder()
                          .setConditions([Conditions](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordCondition.Conditions.html).newBuilder().addConditions(condition).build())
                          .build())
                  .build();
    
          // Associate the de-identification and conditions with the specified fields.
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .setInfoTypeTransformations(infoTypeTransformations)
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(fieldIds)
                  .setCondition(recordCondition)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize google DLP Client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // Construct the tabular data
    const tablularData = {
      headers: [
        {name: 'AGE'},
        {name: 'PATIENT'},
        {name: 'HAPPINESS SCORE'},
        {name: 'FACTOID'},
      ],
      rows: [
        {
          values: [
            {integerValue: 101},
            {stringValue: 'Charles Dickens'},
            {integerValue: 95},
            {
              stringValue:
                'Charles Dickens name was a curse invented by Shakespeare.',
            },
          ],
        },
        {
          values: [
            {integerValue: 22},
            {stringValue: 'Jane Austen'},
            {integerValue: 21},
            {stringValue: "There are 14 kisses in Jane Austen's novels."},
          ],
        },
        {
          values: [
            {integerValue: 55},
            {stringValue: 'Mark Twain'},
            {integerValue: 75},
            {stringValue: 'Mark Twain loved cats.'},
          ],
        },
      ],
    };
    
    async function deIdentifyTableConditionalInfoType() {
      // Specify fields to be de-identified.
      const fieldIds = [{name: 'PATIENT'}, {name: 'FACTOID'}];
    
      // Associate info type with the replacement strategy
      const infoTypeTransformations = {
        transformations: [
          {
            infoTypes: [{name: 'PERSON_NAME'}],
            primitiveTransformation: {
              replaceWithInfoTypeConfig: {},
            },
          },
        ],
      };
    
      // Specify when the above fields should be de-identified.
      const condition = {
        expressions: {
          conditions: {
            conditions: [
              {
                field: {name: 'AGE'},
                operator: '[GREATER_THAN](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.relationaloperator.html)',
                value: {integerValue: 89},
              },
            ],
          },
        },
      };
    
      // Apply the condition to records.
      const recordTransformations = {
        fieldTransformations: [
          {
            infoTypeTransformations,
            fields: fieldIds,
            condition: condition,
          },
        ],
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: {
          table: tablularData,
        },
        deidentifyConfig: {
          recordTransformations,
        },
      };
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results.
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    
    deIdentifyTableConditionalInfoType();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordCondition;
    use Google\Cloud\Dlp\V2\RecordCondition\Condition;
    use Google\Cloud\Dlp\V2\RecordCondition\Conditions;
    use Google\Cloud\Dlp\V2\RecordCondition\Expressions;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\RelationalOperator;
    use Google\Cloud\Dlp\V2\ReplaceWithInfoTypeConfig;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data using conditional logic and replace with infoTypes.
     * Transform findings only when specific conditions are met on another field.
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to deidentify
     * @param string $outputCsvFile         The oupt file path to save deidentify content
     */
    
    function deidentify_table_condition_infotypes(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table1.csv',
        string $outputCsvFile = './test/data/deidentify_table_condition_infotypes_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
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
    
        // Construct the table object
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify what content you want the service to de-identify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify the type of info the inspection will look for.
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
    
        // Specify that findings should be replaced with corresponding info type name.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setReplaceWithInfoTypeConfig(new ReplaceWithInfoTypeConfig());
    
        // Associate info type with the replacement strategy
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes([$personNameInfoType]);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Specify fields to be de-identified.
        $fieldIds = [
            (new FieldId())->setName('PATIENT'),
            (new FieldId())->setName('FACTOID'),
        ];
    
        // Specify when the above fields should be de-identified.
        $condition = (new Condition())
            ->setField((new FieldId())
                ->setName('AGE'))
            ->setOperator(RelationalOperator::GREATER_THAN)
            ->setValue((new Value())
                ->setIntegerValue(89));
    
        // Apply the condition to records
        $recordCondition = (new RecordCondition())
            ->setExpressions((new Expressions())
                    ->setConditions((new Conditions())
                            ->setConditions([$condition])
                    )
            );
    
        // Associate the de-identification and conditions with the specified fields.
        $fieldTransformation = (new FieldTransformation())
            ->setInfoTypeTransformations($infoTypeTransformations)
            ->setFields($fieldIds)
            ->setCondition($recordCondition);
    
        $recordtransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print results
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf($outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    from google.cloud.dlp_v2 import [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html)
    
    
    def deidentify_table_condition_replace_with_info_types(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        deid_content_list: List[str],
        info_types: List[str],
        condition_field: str = None,
        condition_operator: str = None,
        condition_value: int = None,
    ) -> types.dlp.Table:
        """Uses the Data Loss Prevention API to de-identify sensitive data in a
        table by replacing them with info-types based on a condition.
        Args:
           project: The Google Cloud project id to use as a parent resource.
           table_data: Json string representing table data.
           deid_content_list: A list of fields in table to de-identify.
           info_types: A list of strings representing info types to look for.
               A full list of info categories and types is available from the API.
               Examples include "FIRST_NAME", "LAST_NAME", "EMAIL_ADDRESS". '
           condition_field: A table field within the record this condition is evaluated against.
           condition_operator: Operator used to compare the field or infoType to the value. One of:
               RELATIONAL_OPERATOR_UNSPECIFIED, EQUAL_TO, NOT_EQUAL_TO, GREATER_THAN, LESS_THAN, GREATER_THAN_OR_EQUALS,
               LESS_THAN_OR_EQUALS, EXISTS.
           condition_value: Value to compare against. [Mandatory, except for ``EXISTS`` tests.].
    
        Returns:
           De-identified table is returned;
           the response from the API is also printed to the terminal.
    
        Example:
        >> $ python deidentify_table_condition_infotypes.py \
        '{"header": ["email", "phone number", "age"],
        "rows": [["robertfrost@example.com", "4232342345", "45"],
        ["johndoe@example.com", "4253458383", "63"]]}' ["email"] \
        ["EMAIL_ADDRESS"] "age" "GREATER_THAN" 50
        >> '{"header": ["email", "phone number", "age"],
            "rows": [["robertfrost@example.com", "4232342345", "45"],
            ["[EMAIL_ADDRESS]", "4253458383", "63"]]}'
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the item
        item = {"table": table}
    
        # Specify fields to be de-identified
        deid_field_list = [{"name": _i} for _i in deid_content_list]
    
        # Construct inspect configuration dictionary
        inspect_config = {"info_types": [{"name": info_type} for info_type in info_types]}
    
        # Construct condition list
        condition = [
            {
                "field": {"name": condition_field},
                "operator": condition_operator,
                "value": {"integer_value": condition_value},
            }
        ]
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "info_type_transformations": {
                            "transformations": [
                                {
                                    "primitive_transformation": {
                                        "replace_with_info_type_config": {}
                                    }
                                }
                            ]
                        },
                        "fields": deid_field_list,
                        "condition": {
                            "expressions": {"conditions": {"conditions": condition}}
                        },
                    }
                ]
            }
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "item": item,
                "inspect_config": inspect_config,
            }
        )
    
        print(f"Table after de-identification: {response.item.table}")
    
        return response.item.table
    
    

[APIs Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2Ftestff%22%2C%22resource%22%3A%7B%22deidentifyConfig%22%3A%7B%22recordTransformations%22%3A%7B%22fieldTransformations%22%3A%5B%7B%22infoTypeTransformations%22%3A%7B%22transformations%22%3A%5B%7B%22infoTypes%22%3A%5B%7B%22name%22%3A%22PERSON_NAME%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22replaceWithInfoTypeConfig%22%3A%7B%7D%7D%7D%5D%7D%2C%22fields%22%3A%5B%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22FACTOID%22%7D%5D%2C%22condition%22%3A%7B%22expressions%22%3A%7B%22conditions%22%3A%7B%22conditions%22%3A%5B%7B%22field%22%3A%7B%22name%22%3A%22AGE%22%7D%2C%22operator%22%3A%22GREATER_THAN%22%2C%22value%22%3A%7B%22integerValue%22%3A%2289%22%7D%7D%5D%7D%7D%7D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22AGE%22%7D%2C%7B%22name%22%3A%22PATIENT%22%7D%2C%7B%22name%22%3A%22HAPPINESS%20SCORE%22%7D%2C%7B%22name%22%3A%22FACTOID%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22integerValue%22%3A%22101%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%22%7D%2C%7B%22integerValue%22%3A%2295%22%7D%2C%7B%22stringValue%22%3A%22Charles%20Dickens%20name%20was%20a%20curse%2C%20possibly%20invented%20by%20Shakespeare.%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2225%22%7D%2C%7B%22stringValue%22%3A%22Jane%20Austen%22%7D%2C%7B%22integerValue%22%3A%2221%22%7D%2C%7B%22stringValue%22%3A%22There%20are%2014%20kisses%20in%20Jane%20Austen%27s%20novels.%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22integerValue%22%3A%2255%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%22%7D%2C%7B%22integerValue%22%3A%2275%22%7D%2C%7B%22stringValue%22%3A%22Mark%20Twain%20loved%20cats.%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.
    
    
    "deidentifyConfig":{
      "recordTransformations":{
        "fieldTransformations":[
          {
            "infoTypeTransformations":{
              "transformations":[
                {
                  "infoTypes":[
                    {
                      "name":"PERSON_NAME"
                    }
                  ],
                  "primitiveTransformation":{
                    "replaceWithInfoTypeConfig":{
    
                    }
                  }
                }
              ]
            },
            "fields":[
              {
                "name":"PATIENT"
              },
              {
                "name":"FACTOID"
              }
            ],
            "condition":{
              "expressions":{
                "conditions":{
                  "conditions":[
                    {
                      "field":{
                        "name":"AGE"
                      },
                      "operator":"GREATER_THAN",
                      "value":{
                        "integerValue":"89"
                      }
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    }
    

## Transform findings using a cryptographic hash transformation

The following JSON examples use [infoType transformations](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#infotype_transformations) to instruct the DLP API to inspect the entire table structure for specific [infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes), and then to encrypt the matching values using a [transient `CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.TransientCryptoKey).

**Note:** For simplicity, this example uses a transient key, which is generated for the transformation and then discarded. The scope of this key is a single API call. To keep integrity of hashes or other tokenization methods across API calls, you could also use other kinds of [`CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptokey)s, though using a raw [`UnwrappedCryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#unwrappedcryptokey) is less secure and not recommended.

The following example demonstrates de-identifying two infoTypes using a cryptographic hash transformation.

**Input:**

userid | comments  
---|---  
user1@example.org | my email is user1@example.org and phone is 858-555-0222  
user2@example.org | my email is user2@example.org and phone is 858-555-0223  
user3@example.org | my email is user3@example.org and phone is 858-555-0224  
  
**Transformed table:**

userid | comments  
---|---  
1kSfj3Op64MH1BiznupEpX0BdQrHMm62X6abgsPH5zM= | my email is 1kSfj3Op64MH1BiznupEpX0BdQrHMm62X6abgsPH5zM= and phone is hYXPcsJNBCe1rr51sHiVw2KhtoyMe4HEFKNHWFcDVm0=  
4ESy7+rEN8NVaUJ6J7kwvcgW8wcm0cm5gbBAcu6SfdM= | my email is 4ESy7+rEN8NVaUJ6J7kwvcgW8wcm0cm5gbBAcu6SfdM= and phone is KKqW1tQwgvGiC6iWJHhLiz2enNSEFRzhmLOf9fSTxRw=  
bu1blyd/mbjLmpF2Rdi6zpgsLatSwpJLVki2fMeudM0= | my email is bu1blyd/mbjLmpF2Rdi6zpgsLatSwpJLVki2fMeudM0= and phone is eNt7qtZVLmxRb8z8NBR/+z00In07CI3hEMStbwofWoc=  
  
[APIs Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2F%5BPROJECT-ID%5D%22%2C%22resource%22%3A%7B%22inspectConfig%22%3A%7B%22infoTypes%22%3A%5B%7B%22name%22%3A%22EMAIL_ADDRESS%22%7D%2C%7B%22name%22%3A%22PHONE_NUMBER%22%7D%5D%7D%2C%22deidentifyConfig%22%3A%7B%22infoTypeTransformations%22%3A%7B%22transformations%22%3A%5B%7B%22infoTypes%22%3A%5B%7B%22name%22%3A%22EMAIL_ADDRESS%22%7D%2C%7B%22name%22%3A%22PHONE_NUMBER%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22cryptoHashConfig%22%3A%7B%22cryptoKey%22%3A%7B%22transient%22%3A%7B%22name%22%3A%22%5BTRANSIENT-CRYPTO-KEY%5D%22%7D%7D%7D%7D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22userid%22%7D%2C%7B%22name%22%3A%22comments%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22abby_abernathy%40example.org%22%7D%2C%7B%22stringValue%22%3A%22my%20email%20is%20abby_abernathy%40example.org%20and%20phone%20is%20858-555-0222%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22bert_beauregard%40example.org%22%7D%2C%7B%22stringValue%22%3A%22my%20email%20is%20bert_beauregard%40example.org%20and%20phone%20is%20858-555-0223%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22cathy_crenshaw%40example.org%22%7D%2C%7B%22stringValue%22%3A%22my%20email%20is%20cathy_crenshaw%40example.org%20and%20phone%20is%20858-555-0224%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableWithCryptoHash
    {
        public static Table Deidentify(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToDeidentify = null,
            IEnumerable<InfoType> infoTypes = null,
            string transientKeyName = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToDeidentify == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "user1@example.org" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "my email is user1@example.org and phone is 858-555-0222" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "user2@example.org" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "my email is user2@example.org and phone is 858-555-0223" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "user3@example.org" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "my email is user3@example.org and phone is 858-555-0224" }
                };
    
                tableToDeidentify = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "User ID" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "comments" }
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
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToDeidentify };
    
            // Construct the infoTypes by specifying the type of info to be inspected if null.
            var infotypes = infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
            {
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" }
            };
    
            // Construct the crypto hash config using transient crypto key name.
            var cryptoHashConfig = new [CryptoHashConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoHashConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    Transient = new [TransientCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransientCryptoKey.html)
                    {
                        Name = transientKeyName ?? "[TRANSIENT-CRYPTO-KEY]"
                    }
                }
            };
    
            // Construct the de-identify config using crypto hash config.
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
                                CryptoHashConfig = cryptoHashConfig
                            },
                            InfoTypes = { infotypes }
                        }
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infotypes },
                IncludeQuote = true
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            // Call the API.
            [DeidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html) response = dlp.DeidentifyContent(request);
    
            // Print the table.
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
    
    // deIdentifyTableWithCryptoHash transforms findings using a cryptographic hash transformation.
    func deIdentifyTableWithCryptoHash(w io.Writer, projectID, transientKeyName string) error {
    	// projectId := "your-project-id"
    	// transientKeyName := "YOUR_TRANSIENT_CRYPTO_KEY_NAME"
    
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "user1@example.org"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "my email is user1@example.org and phone is 858-555-0222"}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "user2@example.org"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "my email is user2@example.org and phone is 858-555-0232"}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "user3@example.org"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "my email is user3@example.org and phone is 858-555-0224"}},
    		},
    	}
    
    	tableToDeidentify := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "userid"},
    			{Name: "comments"},
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
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PHONE_NUMBER"},
    		{Name: "EMAIL_ADDRESS"},
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: infoTypes,
    	}
    
    	// Specify the transient key which will encrypt the data.
    	if transientKeyName == "" {
    		transientKeyName = "YOUR_TRANSIENT_CRYPTO_KEY_NAME"
    	}
    
    	// Specify the transient key which will encrypt the data.
    	cryptoKey := &dlppb.CryptoKey{
    		Source: &dlppb.CryptoKey_Transient{
    			Transient: &dlppb.TransientCryptoKey{
    				Name: transientKeyName,
    			},
    		},
    	}
    
    	// Specify how the info from the inspection should be encrypted.
    	cryptoHashConfig := &dlppb.CryptoHashConfig{
    		CryptoKey: cryptoKey,
    	}
    
    	// Define type of de-identification as cryptographic hash transformation.
    	primitiveTransformation := &dlppb.PrimitiveTransformation_CryptoHashConfig{
    		CryptoHashConfig: cryptoHashConfig,
    	}
    
    	infoTypeTransformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		InfoTypes: infoTypes,
    		PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    			Transformation: primitiveTransformation,
    		},
    	}
    
    	transformations := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			infoTypeTransformation,
    		},
    	}
    
    	// Specify the config for the de-identify request.
    	deidentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: transformations,
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deidentifyConfig,
    		InspectConfig:    inspectConfig,
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
    import com.google.privacy.dlp.v2.[CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class DeIdentifyTableWithCryptoHash {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
    
        // The table to de-identify.
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("userid").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("comments").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("user1@example.org").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "my email is user1@example.org and phone is 858-555-0222")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("user2@example.org").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "my email is user2@example.org and phone is 858-555-0223")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("user3@example.org").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "my email is user3@example.org and phone is 858-555-0224")
                                .build())
                        .build())
                .build();
    
        // The randomly generated crypto key to encrypt the data.
        String transientKeyName = "YOUR_TRANSIENT_CRYPTO_KEY";
        deIdentifyWithCryptHashTransformation(projectId, tableToDeIdentify, transientKeyName);
      }
    
      // Transforms findings using a cryptographic hash transformation.
      public static void deIdentifyWithCryptHashTransformation(
          String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify, String transientKeyName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to DeIdentify
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .build();
    
          // Specify the transient key which will encrypt the data.
          [TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html) transientCryptoKey = [TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html).newBuilder()
                  .setName(transientKeyName)
                  .build();
    
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder()
                  .[setTransient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setTransient_com_google_privacy_dlp_v2_TransientCryptoKey_)(transientCryptoKey)
                  .build();
    
          // Specify how the info from the inspection should be encrypted.
          [CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html) cryptoHashConfig = [CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  .build();
    
          // Define type of de-identification as cryptographic hash transformation.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation = [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoHashConfig_com_google_privacy_dlp_v2_CryptoHashConfig_)(cryptoHashConfig)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .addAllInfoTypes(infoTypes)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations = [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder()
                  .[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation)
                  .build();
    
          // Specify the config for the de-identify request
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig = [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(transformations)
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
          System.out.println("Table after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable());
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
    
    // Crypto key
    // const transientKeyName = 'YOUR_TRANSIENT_CRYPTO_KEY';
    
    // The table to de-identify.
    const tableToDeIdentify = {
      headers: [{name: 'userid'}, {name: 'comments'}],
      rows: [
        {
          values: [
            {stringValue: 'user1@example.org'},
            {
              stringValue:
                'my email is user1@example.org and phone is 858-555-0222',
            },
          ],
        },
        {
          values: [
            {stringValue: 'user2@example.org'},
            {
              stringValue:
                'my email is user2@example.org and phone is 858-555-0223',
            },
          ],
        },
        {
          values: [
            {stringValue: 'user3@example.org'},
            {
              stringValue:
                'my email is user3@example.org and phone is 858-555-0224',
            },
          ],
        },
      ],
    };
    async function deIdentifyTableWithCryptoHash() {
      // Specify crypto hash configuration that uses transient key.
      const cryptoHashConfig = {
        cryptoKey: {
          transient: {
            name: transientKeyName,
          },
        },
      };
    
      // Construct de-identify request that uses crypto hash configuration.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  cryptoHashConfig: cryptoHashConfig,
                },
                infoTypes: [{name: 'PHONE_NUMBER'}, {name: 'EMAIL_ADDRESS'}],
              },
            ],
          },
        },
        item: {table: tableToDeIdentify},
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
      const deidentifiedTable = response.item.table;
    
      // Print the results.
      console.log(
        `Table after de-identification:\n${JSON.stringify(
          deidentifiedTable,
          null,
          2
        )}`
      );
    }
    
    deIdentifyTableWithCryptoHash();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoHashConfig;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\TransientCryptoKey;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data with crypto hash.
     * Transform findings using a cryptographic hash transformation.
     *
     * @param string $callingProjectId          The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile              The input file(csv) path  to deidentify.
     * @param string $outputCsvFile             The oupt file path to save deidentify content.
     * @param string $transientCryptoKeyName    Specify the random string.
     */
    
    function deidentify_table_with_crypto_hash(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table5.csv',
        string $outputCsvFile = './test/data/deidentify_table_with_crypto_hash_output.csv',
        string $transientCryptoKeyName = 'YOUR-TRANSIENT-CRYPTO-KEY'
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
    
        // Specify what content you want the service to de-identify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify the type of info the inspection will look for.
        // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
        $infoTypes = [
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('PHONE_NUMBER')
        ];
    
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes);
    
        // Specify the transient key which will encrypt the data.
        $cryptoKey = (new CryptoKey())
            ->setTransient((new TransientCryptoKey())
                ->setName($transientCryptoKeyName));
    
        // Specify how the info from the inspection should be encrypted.
        $cryptoHashConfig = (new CryptoHashConfig())
            ->setCryptoKey($cryptoKey);
    
        // Define type of de-identification as cryptographic hash transformation.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoHashConfig($cryptoHashConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes($infoTypes);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Specify the config for the de-identify request
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Send the request and receive response from the service.
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
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
        printf('Table after deidentify (File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    
    
    def deidentify_table_with_crypto_hash(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        info_types: List[str],
        transient_key_name: str,
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data
        in a table using a cryptographic hash transformation.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_data: Dictionary representing table data.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            transient_key_name: Name of the transient crypto key used for encryption.
                The scope of this key is a single API call. It is generated for
                the transformation and then discarded.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item` that service will de-identify.
        item = {"table": table}
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct cryptographic hash configuration using the transient key
        # which will encrypt the data.
        crypto_hash_config = {"crypto_key": {"transient": {"name": transient_key_name}}}
    
        # Specify the type of info the inspection will look for.
        inspect_config = {
            "info_types": info_types,
        }
    
        # Construct deidentify configuration dictionary.
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "info_types": info_types,
                        "primitive_transformation": {
                            "crypto_hash_config": crypto_hash_config
                        },
                    }
                ]
            }
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print the result.
        print(f"Table after de-identification: {response.item.table}")
    
    

### REST
    
    
        {
          "inspectConfig":{
            "infoTypes":[
              {
                "name":"EMAIL_ADDRESS"
              },
              {
                "name":"PHONE_NUMBER"
              }
            ]
          },
          "deidentifyConfig":{
            "infoTypeTransformations":{
              "transformations":[
                {
                  "infoTypes":[
                    {
                      "name":"EMAIL_ADDRESS"
                    },
                    {
                      "name":"PHONE_NUMBER"
                    }
                  ],
                  "primitiveTransformation":{
                    "cryptoHashConfig":{
                      "cryptoKey":{
                        "transient":{
                          "name":"[TRANSIENT-CRYPTO-KEY]"
                        }
                      }
                    }
                  }
                }
              ]
            }
          },
          "item":{
            "table":{
              "headers":[
                {
                  "name":"userid"
                },
                {
                  "name":"comments"
                }
              ],
              "rows":[
                {
                  "values":[
                    {
                      "stringValue":"abby_abernathy@example.org"
                    },
                    {
                      "stringValue":"my email is abby_abernathy@example.org and phone is 858-555-0222"
                    }
                  ]
                },
                {
                  "values":[
                    {
                      "stringValue":"bert_beauregard@example.org"
                    },
                    {
                      "stringValue":"my email is bert_beauregard@example.org and phone is 858-555-0223"
                    }
                  ]
                },
                {
                  "values":[
                    {
                      "stringValue":"cathy_crenshaw@example.org"
                    },
                    {
                      "stringValue":"my email is cathy_crenshaw@example.org and phone is 858-555-0224"
                    }
                  ]
                }
              ]
            }
          }
        }
    

## Transform findings using two separate cryptographic hash transformations

This example demonstrates how you can use different cryptographic keys in different transformations within a single de-identification configuration. First, a field transformation on the "userid" field is declared. That transformation does not include any infoType transformations, so the "userid" field in each row is transformed, regardless of its data type. Then, another field transformation is declared, this one on the "comments" field.

**Input:**

userid | comments  
---|---  
user1@example.org | my email is user1@example.org and phone is 858-555-0222  
abbyabernathy1 | my userid is abbyabernathy1 and my email is aabernathy@example.com  
  
**Transformed table:**

userid | comments  
---|---  
5WvS4+aJtCCwWWG79cmRNamDgyvJ+CkuwNpA2gaR1VQ= | my email is vjqGLaA6+NUUnZAWXpI72lU1GfwQdOKu7XqWaJPcvQQ= and phone is BY+mSXXTu6mOoX5pr0Xbse60uelsSHmwRCq6HcscKtk=  
t0dOmHvkT0VsM++SVmESVKHenLkmhBmFezH3hSDldDg= | my userid is abbyabernathy1 and my email is TQ3ancdUn9zgwO5qe6ahkmVrBuNhvlMknxjPjIt0N2w=  
  
[APIs Explorer example](https://cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify?apix=true&apix_params=%7B%22parent%22%3A%22projects%2F%5BPROJECT-ID%5D%22%2C%22resource%22%3A%7B%22inspectConfig%22%3A%7B%22infoTypes%22%3A%5B%7B%22name%22%3A%22EMAIL_ADDRESS%22%7D%2C%7B%22name%22%3A%22PHONE_NUMBER%22%7D%5D%7D%2C%22deidentifyConfig%22%3A%7B%22recordTransformations%22%3A%7B%22fieldTransformations%22%3A%5B%7B%22fields%22%3A%5B%7B%22name%22%3A%22userid%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22cryptoHashConfig%22%3A%7B%22cryptoKey%22%3A%7B%22transient%22%3A%7B%22name%22%3A%22%5BTRANSIENT-CRYPTO-KEY-1%5D%22%7D%7D%7D%7D%7D%2C%7B%22fields%22%3A%5B%7B%22name%22%3A%22comments%22%7D%5D%2C%22infoTypeTransformations%22%3A%7B%22transformations%22%3A%5B%7B%22infoTypes%22%3A%5B%7B%22name%22%3A%22PHONE_NUMBER%22%7D%2C%7B%22name%22%3A%22EMAIL_ADDRESS%22%7D%5D%2C%22primitiveTransformation%22%3A%7B%22cryptoHashConfig%22%3A%7B%22cryptoKey%22%3A%7B%22transient%22%3A%7B%22name%22%3A%22%5BTRANSIENT-CRYPTO-KEY-2%5D%22%7D%7D%7D%7D%7D%5D%7D%7D%5D%7D%7D%2C%22item%22%3A%7B%22table%22%3A%7B%22headers%22%3A%5B%7B%22name%22%3A%22userid%22%7D%2C%7B%22name%22%3A%22comments%22%7D%5D%2C%22rows%22%3A%5B%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22user1%40example.org%22%7D%2C%7B%22stringValue%22%3A%22my%20email%20is%20user1%40example.org%20and%20phone%20is%20858-333-2222%22%7D%5D%7D%2C%7B%22values%22%3A%5B%7B%22stringValue%22%3A%22abbyabernathy1%22%7D%2C%7B%22stringValue%22%3A%22my%20userid%20is%20abbyabernathy1%20and%20my%20email%20is%20aabernathy%40example.com%22%7D%5D%7D%5D%7D%7D%7D%7D)

**Tip:** To run the example in APIs Explorer, uncheck **Google OAuth 2.0**.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableWithMultipleCryptoHash
    {
        public static Table Deidentify(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToDeidentify = null,
            IEnumerable<InfoType> infoTypes = null,
            string transientKeyName1 = null,
            string transientKeyName2 = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToDeidentify == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "user1@example.org" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "my email is user1@example.org and phone is 858-555-0222" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "user2@example.org" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "my email is user2@example.org and phone is 858-555-0223" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "user3@example.org" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "my email is user3@example.org and phone is 858-555-0224" }
                };
    
                tableToDeidentify = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "User ID" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "comments" }
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
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToDeidentify };
    
            // Construct the crypto hash config for primitive transformation using
            // transient crypto key name.
            var cryptoHashConfig1 = new [CryptoHashConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoHashConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    Transient = new [TransientCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransientCryptoKey.html)
                    {
                        Name = transientKeyName1 ?? "[TRANSIENT-CRYPTO-KEY-1]"
                    }
                }
            };
    
            // Construct the crypto hash config for infoType transformation using
            // transient crypto key name.
            var cryptoHashConfig2 = new [CryptoHashConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoHashConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    Transient = new [TransientCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TransientCryptoKey.html)
                    {
                        Name = transientKeyName2 ?? "[TRANSIENT-CRYPTO-KEY-2]"
                    }
                }
            };
    
            // Construct the infoTypes by specifying the type of info to be inspected if null.
            var infotypes = infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
            {
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" }
            };
    
            // Construct the deidentify config using crypto hash configs.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            Fields = { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "User ID" } } },
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoHashConfig = cryptoHashConfig1
                            }
                        },
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            Fields = { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "comments" } } },
                            InfoTypeTransformations =  new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                            {
                                Transformations =
                                {
                                    new InfoTypeTransformations.Types.InfoTypeTransformation
                                    {
                                        PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                                        {
                                            CryptoHashConfig = cryptoHashConfig2
                                        },
                                        InfoTypes = { infotypes }
                                    }
                                }
                            }
                        }
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infotypes },
                IncludeQuote = true
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Print the table.
            Console.WriteLine(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
    
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
    
    // deIdentifyTableWithMultipleCryptoHash Transforms findings using two separate cryptographic hash transformations.
    func deIdentifyTableWithMultipleCryptoHash(w io.Writer, projectID, transientKeyName1, transientKeyName2 string) error {
    	// projectId := "your-project-id"
    	// transientKeyName1 := "YOUR_TRANSIENT_CRYPTO_KEY_1"
    	// transientKeyName2 := "YOUR_TRANSIENT_CRYPTO_KEY_2"
    
    	// The table to de-identify.
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "user1@example.org"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "my email is user1@example.org and phone is 858-555-0222"}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "abbyabernathy1"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "my userid is abbyabernathy1 and my email is aabernathy@example.com"}},
    		},
    	}
    
    	tableToDeidentify := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "userid"},
    			{Name: "comments"},
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
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PHONE_NUMBER"},
    		{Name: "EMAIL_ADDRESS"},
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: infoTypes,
    	}
    
    	// Specify the transient key names.
    
    	transientCryptoKey1 := &dlppb.TransientCryptoKey{
    		Name: transientKeyName1,
    	}
    
    	transientCryptoKey2 := &dlppb.TransientCryptoKey{
    		Name: transientKeyName2,
    	}
    
    	cryptoKey1 := &dlppb.CryptoKey_Transient{
    		Transient: transientCryptoKey1,
    	}
    
    	cryptoKey2 := &dlppb.CryptoKey_Transient{
    		Transient: transientCryptoKey2,
    	}
    
    	// Specify the CryptoHashConfig for transientKey1.
    	cryptoHashConfig1 := &dlppb.CryptoHashConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: cryptoKey1,
    		},
    	}
    
    	// Specify the CryptoHashConfig for transientKey1.
    	cryptoHashConfig2 := &dlppb.CryptoHashConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: cryptoKey2,
    		},
    	}
    
    	// Define type of de-identification as cryptographic hash transformation.
    
    	// Specify the transformation for transientKey1
    	primitiveTransformation1 := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoHashConfig{
    			CryptoHashConfig: cryptoHashConfig1,
    		},
    	}
    
    	// Specify the transformation for transientKey2
    	primitiveTransformation2 := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoHashConfig{
    			CryptoHashConfig: cryptoHashConfig2,
    		},
    	}
    
    	infoTypeTransformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		PrimitiveTransformation: primitiveTransformation2,
    	}
    
    	transformations := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			infoTypeTransformation,
    		},
    	}
    
    	// Specify fields to be de-identified.
    	fieldIds := []*dlppb.FieldId{
    		{Name: "userid"},
    		{Name: "comments"},
    	}
    
    	fieldTransformations := []*dlppb.FieldTransformation{
    		{
    			Fields: []*dlppb.FieldId{
    				fieldIds[0],
    			},
    			Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    				PrimitiveTransformation: primitiveTransformation1,
    			},
    		},
    		{
    			Fields: []*dlppb.FieldId{
    				fieldIds[1],
    			},
    			Transformation: &dlppb.FieldTransformation_InfoTypeTransformations{
    				InfoTypeTransformations: transformations,
    			},
    		},
    	}
    
    	recordTransformations := &dlppb.RecordTransformations{
    		FieldTransformations: fieldTransformations,
    	}
    
    	// Specify the config for the de-identify request
    	deidentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    			RecordTransformations: recordTransformations,
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deidentifyConfig,
    		InspectConfig:    inspectConfig,
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
    import com.google.privacy.dlp.v2.[CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class DeIdentifyTableWithMultipleCryptoHash {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
    
        // The table to de-identify.
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("userid").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("comments").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("user1@example.org").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "my email is user1@example.org and phone is 858-555-0222")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("user2@example.org").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "my email is user2@example.org and phone is 858-555-0223")
                                .build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("user3@example.org").build())
                        .addValues(
                            [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder()
                                .[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(
                                    "my email is user3@example.org and phone is 858-555-0224")
                                .build())
                        .build())
                .build();
    
        // The names of the keys used to encrypt the data.
        String transientKeyName1 = "YOUR_TRANSIENT_CRYPTO_KEY";
        String transientKeyName2 = "YOUR_TRANSIENT_CRYPTO_KEY_2";
    
        deIdentifyWithCryptHashTransformation(
            projectId, tableToDeIdentify, transientKeyName1, transientKeyName2);
      }
    
      // Transforms findings using two separate cryptographic hash transformations.
      public static void deIdentifyWithCryptHashTransformation(
          String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify, String transientKeyName1, String transientKeyName2)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to DeIdentify
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("PHONE_NUMBER", "EMAIL_ADDRESS")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .build();
    
          // Specify the transient key which will encrypt the data.
          [TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html) transientCryptoKey = [TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html).newBuilder()
                  .setName(transientKeyName1)
                  .build();
          [TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html) transientCryptoKey2 = [TransientCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransientCryptoKey.html).newBuilder()
                  .setName(transientKeyName2)
                  .build();
    
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder()
                  .[setTransient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setTransient_com_google_privacy_dlp_v2_TransientCryptoKey_)(transientCryptoKey)
                  .build();
    
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey2 = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder()
                  .[setTransient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setTransient_com_google_privacy_dlp_v2_TransientCryptoKey_)(transientCryptoKey2)
                  .build();
    
          [CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html) cryptoHashConfig = [CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html).newBuilder()
                      .setCryptoKey(cryptoKey)
                      .build();
    
          [CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html) cryptoHashConfig2 = [CryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoHashConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey2)
                  .build();
    
          // Define type of de-identification as cryptographic hash transformation.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation = [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoHashConfig_com_google_privacy_dlp_v2_CryptoHashConfig_)(cryptoHashConfig)
                  .build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation2 = [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoHashConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoHashConfig_com_google_privacy_dlp_v2_CryptoHashConfig_)(cryptoHashConfig2)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation2)
                  .addAllInfoTypes(infoTypes)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          // Specify fields to be de-identified.
          List<FieldId> fieldIds =
              Stream.of("userid")
                  .map(id -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(id).build())
                  .collect(Collectors.toList());
    
          List<FieldId> fieldIds1 =
              Stream.of("comments")
                  .map(id -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(id).build())
                  .collect(Collectors.toList());
    
          List<FieldTransformation> fieldTransformations = new ArrayList<>();
          fieldTransformations.add(
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(fieldIds)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build());
          fieldTransformations.add(
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(fieldIds1)
                  .setInfoTypeTransformations(transformations)
                  .build());
    
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) recordTransformations = [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder()
                  .addAllFieldTransformations(fieldTransformations)
                  .build();
    
          // Specify the config for the de-identify request
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig = [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .[setRecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.Builder.html#com_google_privacy_dlp_v2_DeidentifyConfig_Builder_setRecordTransformations_com_google_privacy_dlp_v2_RecordTransformations_)(recordTransformations)
                  .build();
    
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
          System.out.println("Table after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable());
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
    
    // Crypto key 1
    // const transientKey1 = 'YOUR_TRANSIENT_CRYPTO_KEY';
    
    // Crypto key 2
    // const transientKey2 = 'YOUR_TRANSIENT_CRYPTO_KEY_2';
    
    // The table to de-identify.
    const tableToDeIdentify = {
      headers: [{name: 'userid'}, {name: 'comments'}],
      rows: [
        {
          values: [
            {stringValue: 'user1@example.org'},
            {
              stringValue:
                'my email is user1@example.org and phone is 858-555-0222',
            },
          ],
        },
        {
          values: [
            {stringValue: 'user2@example.org'},
            {
              stringValue:
                'my email is user2@example.org and phone is 858-555-0223',
            },
          ],
        },
        {
          values: [
            {
              stringValue: 'user3@example.org',
            },
            {
              stringValue:
                'my email is user3@example.org and phone is 858-555-0224',
            },
          ],
        },
      ],
    };
    
    async function deIdentifyTableWithMultipleCryptoHash() {
      // The type of info the inspection will look for.
      const infoTypes = [{name: 'PHONE_NUMBER'}, {name: 'EMAIL_ADDRESS'}];
    
      // The fields to be de-identified.
      const fieldIds1 = [{name: 'userid'}];
    
      const fieldIds2 = [{name: 'comments'}];
    
      // Construct two primitive transformations using two different keys.
      const primitiveTransformation1 = {
        cryptoHashConfig: {
          cryptoKey: {
            transient: {
              name: transientKey1,
            },
          },
        },
      };
    
      const primitiveTransformation2 = {
        cryptoHashConfig: {
          cryptoKey: {
            transient: {
              name: transientKey2,
            },
          },
        },
      };
    
      // Construct infoType transformation using transient key 2
      const infoTypeTransformation = {
        primitiveTransformation: primitiveTransformation2,
        infoTypes: infoTypes,
      };
    
      // Associate each field with transformation defined above.
      const fieldTransformations = [
        {
          fields: fieldIds1,
          primitiveTransformation: primitiveTransformation1,
        },
        {
          fields: fieldIds2,
          infoTypeTransformations: {
            transformations: [infoTypeTransformation],
          },
        },
      ];
    
      // Use transformation confiugrations and construct de-identify configuration.
      const deidentifyConfig = {
        recordTransformations: {
          fieldTransformations: fieldTransformations,
        },
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: deidentifyConfig,
        inspectConfig: {
          infoTypes: infoTypes,
        },
        item: {
          table: tableToDeIdentify,
        },
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
    
      const deidentifiedTable = response.item.table;
    
      // Print the results.
      console.log(
        `Deidentified table: ${JSON.stringify(deidentifiedTable, null, 2)}`
      );
    }
    deIdentifyTableWithMultipleCryptoHash();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoHashConfig;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\TransientCryptoKey;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data with multiple crypto hash.
     * Transform findings using two separate cryptographic hash transformations.
     *
     * @param string $callingProjectId          The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile              The input file(csv) path  to deidentify.
     * @param string $outputCsvFile             The oupt file path to save deidentify content.
     * @param string $transientCryptoKeyName1   Specify the random string.
     * @param string $transientCryptoKeyName2   Specify the random string.
     */
    
    function deidentify_table_with_multiple_crypto_hash(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table6.csv',
        string $outputCsvFile = './test/data/deidentify_table_with_multiple_crypto_hash_output.csv',
        string $transientCryptoKeyName1 = 'YOUR-TRANSIENT-CRYPTO-KEY-1',
        string $transientCryptoKeyName2 = 'YOUR-TRANSIENT-CRYPTO-KEY-2'
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
    
        // Specify what content you want the service to de-identify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify the type of info the inspection will look for.
        // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
        $infoTypes = [
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('PHONE_NUMBER')
        ];
    
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes);
    
        // ---- First Crypto Hash Rule ----
    
        // Specify the transient key which will encrypt the data.
        $cryptoHashConfig1 = (new CryptoHashConfig())
            ->setCryptoKey((new CryptoKey())
                ->setTransient((new TransientCryptoKey())
                    ->setName($transientCryptoKeyName1)));
    
        // Define type of de-identification as cryptographic hash transformation.
        $primitiveTransformation1 = (new PrimitiveTransformation())
            ->setCryptoHashConfig($cryptoHashConfig1);
    
        $fieldTransformation1 = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation1)
            // Specify fields to be de-identified.
            ->setFields([
                (new FieldId())->setName('userid')
            ]);
    
        // ---- Second Crypto Hash Rule ----
    
        // Specify the transient key which will encrypt the data.
        $cryptoHashConfig2 = (new CryptoHashConfig())
            ->setCryptoKey((new CryptoKey())
                ->setTransient((new TransientCryptoKey())
                    ->setName($transientCryptoKeyName2)));
    
        // Define type of de-identification as cryptographic hash transformation.
        $primitiveTransformation2 = (new PrimitiveTransformation())
            ->setCryptoHashConfig($cryptoHashConfig2);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation2)
            ->setInfoTypes($infoTypes);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        $fieldTransformation2 = (new FieldTransformation())
            ->setInfoTypeTransformations($infoTypeTransformations)
            // Specify fields to be de-identified.
            ->setFields([
                (new FieldId())->setName('comments')
            ]);
    
        $recordtransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation1, $fieldTransformation2]);
    
        // Specify the config for the de-identify request
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Send the request and receive response from the service.
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
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
        printf('Table after deidentify (File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Dict, List, Union
    
    import google.cloud.dlp
    
    
    def deidentify_table_with_multiple_crypto_hash(
        project: str,
        table_data: Dict[str, Union[List[str], List[List[str]]]],
        info_types: List[str],
        transient_key_name_1: str,
        transient_key_name_2: str,
        deid_fields_1: List[str],
        deid_fields_2: List[str],
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data
        in table using multiple transient cryptographic hash keys.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_data: Dictionary representing table data.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            transient_key_name_1: Name of the first transient crypto key used
                for encryption. The scope of this key is a single API call.
                It is generated for the transformation and then discarded.
            transient_key_name_2: Name of the second transient crypto key used
                for encryption. The scope of this key is a single API call.
                It is generated for the transformation and then discarded.
            deid_fields_1: List of column names in table to de-identify using
                transient_key_name_1.
            deid_fields_2: List of column names in table to de-identify using
                transient_key_name_2.
    
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_data["header"]]
        rows = []
        for row in table_data["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item`
        item = {"table": table}
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct cryptographic hash configurations using two transient keys
        # which will encrypt the data.
        crypto_hash_config_1 = {"crypto_key": {"transient": {"name": transient_key_name_1}}}
        crypto_hash_config_2 = {"crypto_key": {"transient": {"name": transient_key_name_2}}}
    
        # Prepare fields to be de-identified by converting list of strings
        # into list of dictionaries.
        deid_fields_1 = [{"name": field} for field in deid_fields_1]
        deid_fields_2 = [{"name": field} for field in deid_fields_2]
    
        # Specify the type of info the inspection will look for.
        inspect_config = {
            "info_types": info_types,
        }
    
        # Construct deidentify configuration dictionary.
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "fields": deid_fields_1,
                        "primitive_transformation": {
                            "crypto_hash_config": crypto_hash_config_1
                        },
                    },
                    {
                        "fields": deid_fields_2,
                        "info_type_transformations": {
                            "transformations": [
                                {
                                    "info_types": info_types,
                                    "primitive_transformation": {
                                        "crypto_hash_config": crypto_hash_config_2
                                    },
                                }
                            ]
                        },
                    },
                ]
            }
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print the result.
        print(f"Table after de-identification: {response.item.table}")
    
    

### REST

{ "inspectConfig":{ "infoTypes":[ { "name":"EMAIL_ADDRESS" }, { "name":"PHONE_NUMBER" } ] }, "deidentifyConfig":{ "recordTransformations":{ "fieldTransformations":[ { "fields":[ { "name":"userid" } ], "primitiveTransformation":{ "cryptoHashConfig":{ "cryptoKey":{ "transient":{ "name":"[TRANSIENT-CRYPTO-KEY-1]" } } } } }, { "fields":[ { "name":"comments" } ], "infoTypeTransformations":{ "transformations":[ { "infoTypes":[ { "name":"PHONE_NUMBER" }, { "name":"EMAIL_ADDRESS" } ], "primitiveTransformation":{ "cryptoHashConfig":{ "cryptoKey":{ "transient":{ "name":"[TRANSIENT-CRYPTO-KEY-2]" } } } } } ] } } ] } }, "item":{ "table":{ "headers":[ { "name":"userid" }, { "name":"comments" } ], "rows":[ { "values":[ { "stringValue":"user1@example.org" }, { "stringValue":"my email is user1@example.org and phone is 858-333-2222" } ] }, { "values":[ { "stringValue":"abbyabernathy1" }, { "stringValue":"my userid is abbyabernathy1 and my email is aabernathy@example.com" } ] } ] } } } 

## Transform findings using format-preserving encryption

This example demonstrates how to use Sensitive Data Protection to replace a sensitive string with a token that has the same length and alphabet as the original string. This example uses the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method. For more information, see [Format-preserving encryption](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference#fpe).

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
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "11111" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "2015" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "$10" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "33333" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "2016" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "$20" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "22222" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "2016" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "$15" }
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
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
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
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("11111").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("2015").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("$10").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("22222").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("2016").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("$20").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("33333").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("2016").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("$15").build())
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
    
    

## Re-identify findings de-identified using format-preserving encryption

This example demonstrates how to use Sensitive Data Protection to re-identify sensitive data in tables that were de-identified through the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method. For more information, see [Format-preserving encryption](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference#fpe).

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
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "28777" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "Justin" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "28778" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html) { StringValue = "Gary" }
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
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html);
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
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html).newBuilder().setStringValue("28777").build())
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
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
