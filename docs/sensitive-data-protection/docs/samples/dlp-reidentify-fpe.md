---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-reidentify-fpe/
title: Re-identify content encrypted by FPE \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:13.832362+00:00
---

# Re-identify content encrypted by FPE  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-reidentify-fpe/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Re-identify content encrypted by FPE Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates re-identifying de-identified content.

## Explore further

For detailed documentation that includes this code sample, see the following: 

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
    
    public class ReidentifyContentUsingFpe
    {
        public static ReidentifyContentResponse ReidentifyContent(
            string projectId,
            string text,
            string keyName,
            string wrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the type of info the inspection will re-identify. This must use the same custom
            // info type that was used as a surrogate during the initial encryption.
            var infotype = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "SSN_TOKEN" };
    
            // Specify how to un-encrypt the previously de-identified information.
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
                CommonAlphabet = alphabet,
                SurrogateInfoType = infotype
            };
    
            // Construct reidentify config using above created crypto replace config.
            var reidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig,
                            },
                            InfoTypes = { infotype }
                        }
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
                    {
                        InfoType = infotype,
                        SurrogateType = new CustomInfoType.Types.SurrogateType()
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectConfig = inspectConfig,
                ReidentifyConfig = reidentifyConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text },
            };
    
            // Call the API.
            var response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Reidentified content: {response.Item.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
    
            return response;
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
    
    // reidentifyFPE reidentifies the input with FPE (Format Preserving Encryption).
    // keyFileName is the file name with the KMS wrapped key and cryptoKeyName is the
    // full KMS key resource name used to wrap the key. surrogateInfoType is an
    // the identifier used during deidentification.
    // Info types can be found with the infoTypes.list method or on https://cloud.google.com/dlp/docs/infotypes-reference
    func reidentifyFPE(w io.Writer, projectID, input, kmsKeyName, wrappedAesKey, surrogateInfoType string) error {
    	// projectID := "my-project-id"
    	// input := "My SSN is 123456789"
    	// keyFileName := "projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME"
    	// cryptoKeyName := "YOUR_ENCRYPTED_AES_256_KEY"
    	// surrogateInfoType := "AGE"
    	ctx := context.Background()
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	kmsWrappedCryptoKey, err := base64.StdEncoding.DecodeString(wrappedAesKey)
    	if err != nil {
    		fmt.Fprintf(w, "error %v", err)
    		return err
    	}
    
    	// Specify the crypto key configuration that will used for encryption.
    	cryptoKey := &dlppb.CryptoKey{
    		Source: &dlppb.CryptoKey_KmsWrapped{
    			KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    				WrappedKey:    kmsWrappedCryptoKey,
    				CryptoKeyName: kmsKeyName,
    			},
    		},
    	}
    
    	// Create a configured request.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    				InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    					Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    						{
    							InfoTypes: []*dlppb.InfoType{},
    							PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    								Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    									CryptoReplaceFfxFpeConfig: &dlppb.CryptoReplaceFfxFpeConfig{
    										CryptoKey: cryptoKey,
    										// Set the alphabet used for the encrypted fields.
    										Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    											CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    										},
    										// Set the surrogate info type used during deidentification.
    										SurrogateInfoType: &dlppb.InfoType{
    											Name: surrogateInfoType,
    										},
    									},
    								},
    							},
    						},
    					},
    				},
    			},
    		},
    		// The InspectConfig must identify the surrogate info type to reidentify.
    		InspectConfig: &dlppb.InspectConfig{
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				{
    					InfoType: &dlppb.InfoType{
    						Name: surrogateInfoType,
    					},
    					Type: &dlppb.CustomInfoType_SurrogateType_{
    						SurrogateType: &dlppb.CustomInfoType_SurrogateType{},
    					},
    				},
    			},
    		},
    		// The item to analyze.
    		Item: &dlppb.ContentItem{
    			DataItem: &dlppb.ContentItem_Value{
    				Value: input,
    			},
    		},
    	}
    	// Send the request.
    	r, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return fmt.Errorf("ReidentifyContent: %w", err)
    	}
    	// Print the result.
    	fmt.Fprint(w, r.GetItem().GetValue())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class ReIdentifyWithFpe {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToReIdentify = "My SSN is SSN_TOKEN(9):731997681";
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        String wrappedAesKey = "YOUR_ENCRYPTED_AES_256_KEY";
        reIdentifyWithFpe(projectId, textToReIdentify, kmsKeyName, wrappedAesKey);
      }
    
      public static void reIdentifyWithFpe(
          String projectId, String textToReIdentify, String kmsKeyName, String wrappedAesKey)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToReIdentify).build();
    
          // Specify the type of info the inspection will re-identify. This must use the same custom
          // into type that was used as a surrogate during the initial encryption.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("SSN_TOKEN").build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(surrogateInfoType)
                  .[setSurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setSurrogateType_com_google_privacy_dlp_v2_CustomInfoType_SurrogateType_)([SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html).getDefaultInstance())
                  .build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType).build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) kmsWrappedCryptoKey =
              [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(wrappedAesKey)))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(kmsKeyName)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(kmsWrappedCryptoKey).build();
    
          // Specify how to un-encrypt the previously de-identified information
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html).NUMERIC)
                  .setSurrogateInfoType(surrogateInfoType)
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .addInfoTypes(surrogateInfoType)
                  .build();
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) reidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().setInfoTypeTransformations(transformations).build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request =
              [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(reidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results
          System.out.println("Text after re-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html#com_google_privacy_dlp_v2_ReidentifyContentResponse_getItem__)().getValue());
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
    
    // The string to reidentify
    // const string = 'My SSN is PHONE_TOKEN(9):#########';
    
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
    
    async function reidentifyWithFpe() {
      // Construct deidentification request
      const item = {value: string};
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  cryptoReplaceFfxFpeConfig: {
                    cryptoKey: {
                      kmsWrapped: {
                        wrappedKey: wrappedKey,
                        cryptoKeyName: keyName,
                      },
                    },
                    commonAlphabet: alphabet,
                    surrogateInfoType: {
                      name: surrogateType,
                    },
                  },
                },
              },
            ],
          },
        },
        inspectConfig: {
          customInfoTypes: [
            {
              infoType: {
                name: surrogateType,
              },
              surrogateType: {},
            },
          ],
        },
        item: item,
      };
    
      // Run reidentification request
      const [response] = await dlp.reidentifyContent(request);
      const reidentifiedItem = response.item;
      console.log(reidentifiedItem.value);
    }
    reidentifyWithFpe();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig\FfxCommonNativeAlphabet;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\SurrogateType;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReidentifyContentRequest;
    
    /**
     * Reidentify a deidentified string using Format-Preserving Encryption (FPE).
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under
     * @param string $string            The string to reidentify
     * @param string $keyName           The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key
     * @param string $wrappedKey        The name of the Cloud KMS key use, encrypted with the KMS key in $keyName
     * @param string $surrogateTypeName (Optional) Surrogate custom info type to enable reidentification
     */
    function reidentify_fpe(
        string $callingProjectId,
        string $string,
        string $keyName,
        string $wrappedKey,
        string $surrogateTypeName
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The infoTypes of information to mask
        $ssnInfoType = (new InfoType())
            ->setName('US_SOCIAL_SECURITY_NUMBER');
        $infoTypes = [$ssnInfoType];
    
        // The set of characters to replace sensitive ones with
        // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        $commonAlphabet = FfxCommonNativeAlphabet::NUMERIC;
    
        // Create the wrapped crypto key configuration object
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedKey))
            ->setCryptoKeyName($keyName);
    
        // Create the crypto key configuration object
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Create the surrogate type object
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        $customInfoType = (new CustomInfoType())
            ->setInfoType($surrogateType)
            ->setSurrogateType(new SurrogateType());
    
        // Create the crypto FFX FPE configuration object
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet($commonAlphabet)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the inspect configuration object
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Create the reidentification configuration object
        $reidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        $item = (new ContentItem())
            ->setValue($string);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results
        $reidentifiedValue = $response->getItem()->getValue();
        print($reidentifiedValue);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def reidentify_with_fpe(
        project: str,
        input_str: str,
        alphabet: str = None,
        surrogate_type: str = None,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to reidentify sensitive data in a
        string that was encrypted by Format Preserving Encryption (FPE).
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
            surrogate_type: The name of the surrogate custom info type to used
                during the encryption process.
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ('wrapped') AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        wrapped_key = base64.b64decode(wrapped_key)
    
        # Construct Deidentify Config
        reidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_replace_ffx_fpe_config": {
                                "crypto_key": {
                                    "kms_wrapped": {
                                        "wrapped_key": wrapped_key,
                                        "crypto_key_name": key_name,
                                    }
                                },
                                "common_alphabet": alphabet,
                                "surrogate_info_type": {"name": surrogate_type},
                            }
                        }
                    }
                ]
            }
        }
    
        inspect_config = {
            "custom_info_types": [
                {"info_type": {"name": surrogate_type}, "surrogate_type": {}}
            ]
        }
    
        # Convert string to item
        item = {"value": input_str}
    
        # Call the API
        response = dlp.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_reidentify_content)(
            request={
                "parent": parent,
                "reidentify_config": reidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print results
        print(response.item.value)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
