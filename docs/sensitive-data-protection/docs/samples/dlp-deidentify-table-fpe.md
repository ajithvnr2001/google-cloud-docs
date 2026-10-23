---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-table-fpe/
title: De-identify table data with format-preserving encryption \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:21.956281+00:00
---

# De-identify table data with format-preserving encryption  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-table-fpe/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  De-identify table data with format-preserving encryption Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates encrypting sensitive data in a table while maintaining format. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Examples of de-identifying tabular data](https://docs.cloud.google.com/sensitive-data-protection/docs/examples-deid-tables)
  * [Transformation reference](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference)



## Code sample

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
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "11111" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "2015" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "$10" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "33333" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "2016" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "$20" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22222" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "2016" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "$15" }
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
