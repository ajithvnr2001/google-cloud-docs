---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-reidentify-deterministic/
title: Re-identify content encrypted by deterministic encryption \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:17.511569+00:00
---

# Re-identify content encrypted by deterministic encryption  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-reidentify-deterministic/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Re-identify content encrypted by deterministic encryption Stay organized with collections  Save and categorize content based on your preferences. 

Re-identify content that was previously de-identified through deterministic encryption.

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
    
    public class ReidentifyContentUsingDeterministic
    {
        public static ReidentifyContentResponse ReidentifyDeterministic(
            string projectId,
            string text,
            string keyName,
            string wrappedKey,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the infoType if null which will be used as surrogate type and infoType both.
            var infoType = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_TOKEN" };
    
            // Construct crypto deterministic config using the crypto key name and wrapped key.
            var cryptoDeterministicConfig = new [CryptoDeterministicConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoDeterministicConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey)
                    }
                },
                SurrogateInfoType = infoType,
            };
    
            // Construct the reidentify config using crypto config.
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
                                CryptoDeterministicConfig = cryptoDeterministicConfig
                            }
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
                        InfoType = infoType,
                        SurrogateType = new CustomInfoType.Types.SurrogateType()
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                ReidentifyConfig = reidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text },
            };
    
            // Call the API.
            [ReidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html) response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Reidentified content: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html#Google_Cloud_Dlp_V2_ReidentifyContentResponse_Item).[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
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
    
    // reidentifyWithDeterministic re-identifies content encrypted by deterministic encryption.
    func reidentifyWithDeterministic(w io.Writer, projectID, inputStr, surrogateType, keyName, wrappedKey string) error {
    	// projectId := "my-project-id"
    	// inputStr := "EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q"
    	// surrogateType := "EMAIL_ADDRESS_TOKEN"
    	/* keyName :=  "projects/YOUR_PROJECT/"
    	   + "locations/YOUR_KEYRING_REGION/"
    	   + "keyRings/YOUR_KEYRING_NAME/"
    	   + "cryptoKeys/YOUR_KEY_NAME"
    	*/
    	// wrappedKey := "YOUR_ENCRYPTED_AES_256_KEY"
    
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
    
    	// The wrapped key is base64-encoded, but the library expects a binary
    	// string, so decode it here.
    	keyBytes, err := base64.StdEncoding.DecodeString(wrappedKey)
    	if err != nil {
    		return err
    	}
    
    	// Create crypto deterministic config.
    	cryptoDeterministicConfig := &dlppb.CryptoDeterministicConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: &dlppb.CryptoKey_KmsWrapped{
    				KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    					WrappedKey:    keyBytes,
    					CryptoKeyName: keyName,
    				},
    			},
    		},
    		SurrogateInfoType: &dlppb.InfoType{
    			Name: surrogateType,
    		},
    	}
    
    	// Create a config for primitive transformation.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoDeterministicConfig{
    			CryptoDeterministicConfig: cryptoDeterministicConfig,
    		},
    	}
    
    	transformation := &dlppb.DeidentifyConfig_InfoTypeTransformations{
    		InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    			Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    				{
    					PrimitiveTransformation: primitiveTransformation,
    				},
    			},
    		},
    	}
    
    	// Construct config to re-identify the config.
    	reIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: transformation,
    	}
    
    	// Construct a config for inspection.
    	inspectConfig := &dlppb.InspectConfig{
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			{
    				InfoType: &dlppb.InfoType{
    					Name: surrogateType,
    				},
    				Type: &dlppb.CustomInfoType_SurrogateType_{
    					SurrogateType: &dlppb.CustomInfoType_SurrogateType{},
    				},
    			},
    		},
    	}
    
    	// Item to be analyzed.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: inputStr,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: reIdentifyConfig,
    		InspectConfig:    inspectConfig,
    		Item:             item,
    	}
    
    	// Send the request.
    	r, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output: %v", r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import org.apache.commons.codec.binary.Base64;
    
    public class ReidentifyWithDeterministicEncryption {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify.
        String textToIdentify = "My SSN is 372819127";
        // The encrypted ('wrapped') AES-256 key to use.
        // This key should be encrypted using the Cloud KMS key specified by key_name.
        String wrappedKey = "YOUR_ENCRYPTED_AES_256_KEY";
        // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key.
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        // The string to re-identify.
        String textToReIdentify =
            DeIdenitfyWithDeterministicEncryption.deIdentifyWithDeterministicEncryption(
                projectId, textToIdentify, wrappedKey, kmsKeyName);
        reIdentifyWithDeterminsiticEncryption(projectId, textToReIdentify, wrappedKey, kmsKeyName);
      }
    
      // Re-identifies sensitive data in a string that was previously de-identified through
      // deterministic encryption.
      public static void reIdentifyWithDeterminsiticEncryption(
          String projectId, String textToReIdentify, String wrappedKey, String key) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToReIdentify).build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html) surrogateType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).SurrogateType.newBuilder().build();
    
          // Specify the surrogate type used at time of de-identification.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder()
                  .setName("SSN_TOKEN")
                  .build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType = [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(surrogateInfoType)
                  .[setSurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setSurrogateType_com_google_privacy_dlp_v2_CustomInfoType_SurrogateType_)(surrogateType)
                  .build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) unwrappedCryptoKey = [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)(
                      [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(
                              Base64.decodeBase64(wrappedKey.getBytes(StandardCharsets.UTF_8))))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(key)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder()
                  .[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(unwrappedCryptoKey)
                  .build();
    
          [CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html) cryptoDeterministicConfig = [CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html).newBuilder()
                  .setSurrogateInfoType(surrogateInfoType)
                  .setCryptoKey(cryptoKey)
                  .build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation = [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoDeterministicConfig_com_google_privacy_dlp_v2_CryptoDeterministicConfig_)(cryptoDeterministicConfig)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations = [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder()
                  .[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation)
                  .build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig = [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(transformations)
                  .build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request = [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service.
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results.
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
    
    // The string to deidentify
    // const string = 'My name is Alicia Abernathy, and my email address is EMAIL_ADDRESS_TOKEN(52):XXXXXX';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // The name of the surrogate custom info type to use
    // Only necessary if you want to reverse the de-identification process
    // Can be essentially any arbitrary string, as long as it doesn't appear
    // in your dataset otherwise.
    // const surrogateType = 'EMAIL_ADDRESS_TOKEN';
    
    async function reidentifyDeterministic() {
      // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
      const cryptoDeterministicEncryption = {
        cryptoKey: {
          kmsWrapped: {
            wrappedKey: wrappedKey,
            cryptoKeyName: keyName,
          },
        },
        surrogateInfoType: {name: surrogateType},
      };
    
      // Construct custom infotype to match information
      const customInfoTypes = [
        {
          infoType: {
            name: surrogateType,
          },
          surrogateType: {},
        },
      ];
    
      // Associate the encryption with the infotype transformation.
      const infoTypeTransformations = {
        transformations: [
          {
            infoTypes: [{name: surrogateType}],
            primitiveTransformation: {
              cryptoDeterministicConfig: cryptoDeterministicEncryption,
            },
          },
        ],
      };
    
      // Construct item to inspect
      const item = {value: string};
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          infoTypeTransformations: infoTypeTransformations,
        },
        inspectConfig: {customInfoTypes},
        item,
      };
    
      // Run re-identification request
      const [response] = await dlp.reidentifyContent(request);
      const deidentifiedItem = response.item;
    
      // Print results
      console.log(deidentifiedItem.value);
    }
    await reidentifyDeterministic();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoDeterministicConfig;
    use Google\Cloud\Dlp\V2\CryptoKey;
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
     * Re-identify content encrypted by deterministic encryption.
     * Re-identify content that was previously de-identified through deterministic encryption.
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under.
     * @param string $string            The string to reidentify.
     * @param string $keyName           The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key.
     * @param string $wrappedKey        The name of the Cloud KMS key use, encrypted with the KMS key in $keyName.
     * @param string $surrogateTypeName Surrogate custom info type to enable reidentification.
     */
    function reidentify_deterministic(
        string $callingProjectId,
        string $string,
        string $surrogateTypeName,
        string $keyName,
        string $wrappedKey
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify what content you want the service to Re-identify.
        $item = (new ContentItem())
            ->setValue($string);
    
        // Specify the surrogate type used at time of de-identification.
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        $customInfoType = (new CustomInfoType())
            ->setInfoType($surrogateType)
            ->setSurrogateType(new SurrogateType());
    
        // Create the inspect configuration object.
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedKey))
            ->setCryptoKeyName($keyName);
    
        // Create the crypto key configuration object.
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Create the crypto deterministic configuration object.
        $cryptoDeterministicConfig = (new CryptoDeterministicConfig())
            ->setCryptoKey($cryptoKey)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoDeterministicConfig($cryptoDeterministicConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the reidentification configuration object.
        $reidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Run request.
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results.
        printf($response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def reidentify_with_deterministic(
        project: str,
        input_str: str,
        surrogate_type: str = None,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """Re-identifies content that was previously de-identified through deterministic encryption.
        Args:
            project: The Google Cloud project ID to use as a parent resource.
            input_str: The string to be re-identified. Provide the entire token. Example:
                EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q
            surrogate_type: The name of the surrogate custom infoType used
                during the encryption process.
            key_name: The name of the Cloud KMS key used to encrypt ("wrap") the
                AES-256 key. Example:
                keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ("wrapped") AES-256 key previously used to encrypt the content.
                This key must have been encrypted using the Cloud KMS key specified by key_name.
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
    
        # Construct reidentify Configuration
        reidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_deterministic_config": {
                                "crypto_key": {
                                    "kms_wrapped": {
                                        "wrapped_key": wrapped_key,
                                        "crypto_key_name": key_name,
                                    }
                                },
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
