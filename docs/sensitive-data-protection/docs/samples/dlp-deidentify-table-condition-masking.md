---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-table-condition-masking/
title: De-identify table data using masking and conditional logic \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:59.349944+00:00
---

# De-identify table data using masking and conditional logic  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-table-condition-masking/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  De-identify table data using masking and conditional logic Stay organized with collections  Save and categorize content based on your preferences. 

Transform a column based on the value of another column.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Examples of de-identifying tabular data](https://docs.cloud.google.com/sensitive-data-protection/docs/examples-deid-tables)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
