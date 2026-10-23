---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-table-with-crypto-hash/
title: Transform findings using a cryptographic hash transformation \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:20.329418+00:00
---

# Transform findings using a cryptographic hash transformation  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-table-with-crypto-hash/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Transform findings using a cryptographic hash transformation Stay organized with collections  Save and categorize content based on your preferences. 

This sample transforms tabular data through a cryptographic hash transformation.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Examples of de-identifying tabular data](https://docs.cloud.google.com/sensitive-data-protection/docs/examples-deid-tables)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
