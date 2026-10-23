---
url: https://docs.cloud.google.com/kms/docs/creating-managing-labels/
title: Labeling keys \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:28.702241+00:00
---

# Labeling keys  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/creating-managing-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Labeling keys Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Key Management Service provides the option to add labels to your Cloud KMS keys. Labels are key-value pairs that you can use to group related Cloud KMS keys and store metadata about a Cloud KMS key.

Labels are included in your bill, so you can see the distribution of costs across your labels.

You can add, update, and remove key labels using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and the Cloud KMS REST API.

You can use labels with other Google Cloud resources, such as [virtual machine resources](https://docs.cloud.google.com/compute/docs/labeling-resources) and [storage buckets](https://docs.cloud.google.com/storage/docs/managing-buckets#manage-labels). For more information about using labels in Google Cloud, see [Creating and Managing Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

## What are labels?

A label is a key-value pair that you can assign to Google Cloud Cloud KMS keys. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

## Requirements for labels

The labels applied to a resource must meet the following requirements:

  * Each resource can have up to 64 labels.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty, and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. Keys must start with a lowercase letter or international character.
  * The key portion of a label must be unique within a single resource. However, you can use the same key with multiple resources.



These limits apply to the key and value for each label, and to the individual Google Cloud resources that have labels. There is no limit on how many labels you can apply across all resources within a project.

## Common uses of labels

Here are some common use cases for labels:

  * **Team or cost center labels** : Add labels based on team or cost center to distinguish Cloud KMS keys owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage labels** : For example, `environment:production` and `environment:test`.

  * **State labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Creating a key with labels

When creating a key, you can add labels by providing one or more key value pairs as labels when you create your key.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring for which you want to create a key.

  3. Click **Create key**.

  4. For **Key name** , enter a name for the key.

  5. Configure the key according to your needs.

  6. Click **Additional settings**.

  7. For each label you want to add, click **Add label** , and then enter the **Key** and **Value**.

  8. Click **Create**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

This example shows how to create a new key and assign labels to the key. You can also add labels to an existing key.
    
    
    gcloud kms keys create KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --purpose PURPOSE \
        **--labels " LABEL_LIST"**
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the key ring where you want to create the key.
  * `LOCATION`: the location of the key ring—for example, `global`.
  * `PURPOSE`: the purpose of the key—for example, `encryption`.
  * `LABEL_LIST`: a comma-separated list of key-value pairs, where each pair is formatted as `LABEL_KEY=LABEL_VALUE`. For example, `env=prod,team=research`. Each label key can be used only once on a Cloud Key Management Service key. If a label key is specified multiple times with different values, each new value overwrites the previous value.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class CreateKeyLabelsSample
    {
        public CryptoKey CreateKeyLabels(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring",
          string id = "my-asymmetric-encrypt-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the parent key ring name.
            [KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html)(projectId, locationId, keyRingId);
    
            // Build the key.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
            {
                Purpose = [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html).[CryptoKeyPurpose](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html).[EncryptDecrypt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_EncryptDecrypt),
                VersionTemplate = new [CryptoKeyVersionTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
                {
                    Algorithm = [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html).[GoogleSymmetricEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_GoogleSymmetricEncryption),
                }
            };
    
            key.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html#Google_Cloud_Kms_V1_CryptoKey_Labels)["team"] = "alpha";
            key.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html#Google_Cloud_Kms_V1_CryptoKey_Labels)["cost_center"] = "cc1234";
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[CreateCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_)(keyRingName, id, key);
    
            // Return the result.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // createKeyLabels creates a new KMS key with labels.
    func createKeyLabels(w io.Writer, parent, id string) error {
    	// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring"
    	// id := "my-labeled-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.CreateCryptoKeyRequest{
    		Parent:      parent,
    		CryptoKeyId: id,
    		CryptoKey: &kmspb.CryptoKey{
    			Purpose: kmspb.[CryptoKey_ENCRYPT_DECRYPT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION_CryptoKey_AES_WRAPPING),
    			VersionTemplate: &kmspb.CryptoKeyVersionTemplate{
    				Algorithm: kmspb.[CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU_CryptoKeyVersion_AES_256_KWP),
    			},
    
    			Labels: map[string]string{
    				"team":        "alpha",
    				"cost_center": "cc1234",
    			},
    		},
    	}
    
    	// Call the API.
    	result, err := client.CreateCryptoKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create key: %w", err)
    	}
    	fmt.Fprintf(w, "Created key: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html);
    import java.io.IOException;
    
    public class CreateKeyLabels {
    
      public void createKeyLabels() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String id = "my-key";
        createKeyLabels(projectId, locationId, keyRingId, id);
      }
    
      // Create a new key with labels.
      public void createKeyLabels(String projectId, String locationId, String keyRingId, String id)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html).of(projectId, locationId, keyRingId);
    
          // Build the key to create with labels.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key =
              [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder()
                  .[setPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_)([CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html).ENCRYPT_DECRYPT)
                  .[setVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_)(
                      [CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html).newBuilder()
                          .setAlgorithm([CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).GOOGLE_SYMMETRIC_ENCRYPTION))
                  .[putLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_putLabels_java_lang_String_java_lang_String_)("team", "alpha")
                  .[putLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_putLabels_java_lang_String_java_lang_String_)("cost_center", "cc1234")
                  .build();
    
          // Create the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client.createCryptoKey(keyRingName, id, key);
          System.out.printf("Created key with labels %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const id = 'my-labeled-key';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent key ring name
    const keyRingName = client.keyRingPath(projectId, locationId, keyRingId);
    
    async function createKeyLabels() {
      const [key] = await client.createCryptoKey({
        parent: keyRingName,
        cryptoKeyId: id,
        cryptoKey: {
          purpose: 'ENCRYPT_DECRYPT',
          versionTemplate: {
            algorithm: 'GOOGLE_SYMMETRIC_ENCRYPTION',
          },
          labels: {
            team: 'alpha',
            cost_center: 'cc1234',
          },
        },
      });
    
      console.log(`Created labeled key: ${key.name}`);
      return key;
    }
    
    return createKeyLabels();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CreateCryptoKeyRequest;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose;
    use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm;
    use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate;
    
    function create_key_labels(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $id = 'my-key-with-labels'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the parent key ring name.
        $keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setPurpose(CryptoKeyPurpose::ENCRYPT_DECRYPT)
            ->setVersionTemplate((new CryptoKeyVersionTemplate())
                ->setAlgorithm(CryptoKeyVersionAlgorithm::GOOGLE_SYMMETRIC_ENCRYPTION)
            )
            ->setLabels([
                'team' => 'alpha',
                'cost_center' => 'cc1234',
            ]);
    
        // Call the API.
        $createCryptoKeyRequest = (new CreateCryptoKeyRequest())
            ->setParent($keyRingName)
            ->setCryptoKeyId($id)
            ->setCryptoKey($key);
        $createdKey = $client->createCryptoKey($createCryptoKeyRequest);
        printf('Created labeled key: %s' . PHP_EOL, $createdKey->getName());
    
        return $createdKey;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def create_key_labels(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Creates a new key in Cloud KMS with labels.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to create (e.g. 'my-labeled-key').
    
        Returns:
            CryptoKey: Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the parent key ring name.
        key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path)(project_id, location_id, key_ring_id)
    
        # Build the key.
        purpose = kms.[CryptoKey](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html).ENCRYPT_DECRYPT
        algorithm = (
            kms.[CryptoKeyVersion](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).GOOGLE_SYMMETRIC_ENCRYPTION
        )
        key = {
            "purpose": purpose,
            "version_template": {
                "algorithm": algorithm,
            },
            "labels": {"team": "alpha", "cost_center": "cc1234"},
        }
    
        # Call the API.
        created_key = client.[create_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key)(
            request={"parent": key_ring_name, "crypto_key_id": key_id, "crypto_key": key}
        )
        print(f"Created labeled key: {created_key.name}")
        return created_key
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # id          = "my-key-with-labels"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key ring name.
    key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project: project_id, location: location_id, key_ring: key_ring_id
    
    # Build the key.
    key = {
      purpose:          :ENCRYPT_DECRYPT,
      version_template: {
        algorithm: :GOOGLE_SYMMETRIC_ENCRYPTION
      },
      labels:           {
        "team"        => "alpha",
        "cost_center" => "cc1234"
      }
    }
    
    # Call the API.
    created_key = client.create_crypto_key parent: key_ring_name, crypto_key_id: id, crypto_key: key
    puts "Created labeled key: #{created_key.name}"

### API

Add labels when you create a new key by using the [`CryptoKeys.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method, and include the `labels` property in your request body. For example:
    
    
    {
      "purpose": "ENCRYPT_DECRYPT",
      "labels": [
        {
          "key": "LABEL_KEY",
          "value": "LABEL_VALUE"
        }
      ]
    }
    

Replace the following:

  * `LABEL_KEY`: the label's key—for example, `env`.
  * `LABEL_VALUE`: the value for the label—for example, `prod`.



You can add multiple label keys, each with its own value. Each label key can be used only once on a Cloud Key Management Service key. If a label key is specified multiple times with different values, each new value overwrites the previous value.

## Viewing labels on a key

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring for the key you want to inspect.

  3. In the header, click **Show info panel**.

  4. In the panel, choose the **Labels** tab.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys describe KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION
    

Replace the following:

  * `KEY_NAME`: the name of the key for which you want to view labels.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the location of the key ring.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using System;
    
    public class GetKeyLabelsSample
    {
        public CryptoKey GetKeyLabels(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) keyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[GetCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetCryptoKey_Google_Cloud_Kms_V1_CryptoKeyName_Google_Api_Gax_Grpc_CallSettings_)(keyName);
    
            // Example of iterating over labels.
            foreach (var item in result.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html#Google_Cloud_Kms_V1_CryptoKey_Labels))
            {
                String key = item.Key;
                String value = item.Value;
                // ...
            }
    
            // Return the ciphertext.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // getKeyLabels fetches the labels on a KMS key.
    func getKeyLabels(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.GetCryptoKeyRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetCryptoKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get key: %w", err)
    	}
    
    	// Extract and print the labels.
    	for k, v := range result.Labels {
    		fmt.Fprintf(w, "%s=%s\n", k, v)
    	}
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import java.io.IOException;
    
    public class GetKeyLabels {
    
      public void getKeyLabels() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        getKeyLabels(projectId, locationId, keyRingId, keyId);
      }
    
      // Get the labels associated with a key.
      public void getKeyLabels(String projectId, String locationId, String keyRingId, String keyId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, key ring, and keyId.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) keyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Get the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = client.getCryptoKey(keyName);
    
          // Print out each label.
          key.[getLabelsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getLabelsMap__)().forEach((k, v) -> System.out.printf("%s=%s%n", k, v));
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function getKeyLabels() {
      const [key] = await client.getCryptoKey({
        name: keyName,
      });
    
      for (const k in key.labels) {
        console.log(`${k}: ${key.labels[k]}`);
      }
    
      return key;
    }
    
    return getKeyLabels();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\GetCryptoKeyRequest;
    
    function get_key_labels(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Call the API.
        $getCryptoKeyRequest = (new GetCryptoKeyRequest())
            ->setName($keyName);
        $key = $client->getCryptoKey($getCryptoKeyRequest);
    
        // Example of iterating over labels.
        foreach ($key->getLabels() as $k => $v) {
            printf('%s = %s' . PHP_EOL, $k, $v);
        }
    
        return $key;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def get_key_labels(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Get a key and its labels.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
    
        Returns:
            CryptoKey: Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # Call the API.
        key = client.[get_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_crypto_key)(request={"name": key_name})
    
        # Example of iterating over labels.
        for k, v in key.labels.items():
            print(f"{k} = {v}")
    
        return key
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Call the API.
    key = client.get_crypto_key name: key_name
    
    # Example of iterating over labels.
    key.labels.each do |k, v|
      puts "#{k} = #{v}"
    end

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To see the labels applied to the key, use the [`CryptoKeys.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/get) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" \
        --request "GET" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --header "x-goog-user-project: PROJECT_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `KEY_NAME`: the name of the key for which you want to view labels.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the location of the key ring.



## Adding or updating labels

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring for the key you want to inspect.

  3. In the header, click **Show info panel**.

  4. In the panel, choose the **Labels** tab.

  5. Edit the value of a label directly in the corresponding text field.

  6. Edit the key of a label by adding a new label with the desired key name and delete the old label by clicking the **Delete** delete next to the label you want to delete.

  7. Click **Save**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys update KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        **--update-labels " LABEL_LIST"**
    

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the key ring that contains the key.
  * `LOCATION`: the location of the key ring.
  * `LABEL_LIST`: a comma-separated list of key-value pairs, where each pair is formatted as `LABEL_KEY=LABEL_VALUE`. For example, `env=prod,team=research`. Each label key can be used only once on a Cloud Key Management Service key. If a label key is specified multiple times with different values, each new value overwrites the previous value.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class UpdateKeyUpdateLabelsSample
    {
        public CryptoKey UpdateKeyUpdateLabels(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) keyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            //
            // Step 1 - get the current set of labels on the key
            //
    
            // Get the current key.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = client.[GetCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetCryptoKey_Google_Cloud_Kms_V1_CryptoKeyName_Google_Api_Gax_Grpc_CallSettings_)(keyName);
    
    
            //
            // Step 2 - add a label to the list of labels
            //
    
            // Add a new label
            key.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html#Google_Cloud_Kms_V1_CryptoKey_Labels)["new_label"] = "new_value";
    
            // Build the update mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
            {
                Paths = { "labels" }
            };
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[UpdateCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKey_Google_Cloud_Kms_V1_CryptoKey_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(key, fieldMask);
    
            // Return the updated key.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	fieldmask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateKeyUpdateLabels updates an existing KMS key, adding a new label.
    func updateKeyUpdateLabels(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	//
    	// Step 1 - get the current set of labels on the key
    	//
    
    	// Build the request.
    	getReq := &kmspb.GetCryptoKeyRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetCryptoKey(ctx, getReq)
    	if err != nil {
    		return fmt.Errorf("failed to get key: %w", err)
    	}
    
    	//
    	// Step 2 - add a label to the list of labels
    	//
    
    	labels := result.Labels
    	labels["new_label"] = "new_value"
    
    	// Build the request.
    	updateReq := &kmspb.UpdateCryptoKeyRequest{
    		CryptoKey: &kmspb.CryptoKey{
    			Name:   name,
    			Labels: labels,
    		},
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"labels"},
    		},
    	}
    
    	// Call the API.
    	result, err = client.UpdateCryptoKey(ctx, updateReq)
    	if err != nil {
    		return fmt.Errorf("failed to update key: %w", err)
    	}
    
    	// Print the labels.
    	for k, v := range result.Labels {
    		fmt.Fprintf(w, "%s=%s\n", k, v)
    	}
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    public class UpdateKeyUpdateLabels {
    
      public void updateKeyUpdateLabels() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        updateKeyUpdateLabels(projectId, locationId, keyRingId, keyId);
      }
    
      // Create a new key that is used for symmetric encryption and decryption.
      public void updateKeyUpdateLabels(
          String projectId, String locationId, String keyRingId, String keyId) throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          //
          // Step 1 - get the current set of labels on the key
          //
    
          // Get the current key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = client.getCryptoKey(cryptoKeyName);
    
          //
          // Step 2 - add a label to the list of labels
          //
    
          // Add a new label.
          key = key.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_toBuilder__)().[putLabels](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_putLabels_java_lang_String_java_lang_String_)("new_label", "new_value").build();
    
          // Construct the field mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("labels");
    
          // Update the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) updatedKey = client.updateCryptoKey(key, fieldMask);
          System.out.printf("Updated key %s%n", updatedKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // const versionId = '123';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function updateKeyUpdateLabels() {
      const [key] = await client.updateCryptoKey({
        cryptoKey: {
          name: keyName,
          labels: {
            new_label: 'new_value',
          },
        },
        updateMask: {
          paths: ['labels'],
        },
      });
    
      console.log(`Updated labels for: ${key.name}`);
      return key;
    }
    
    return updateKeyUpdateLabels();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyRequest;
    use Google\Protobuf\FieldMask;
    
    function update_key_update_labels(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setName($keyName)
            ->setLabels(['new_label' => 'new_value']);
    
        // Create the field mask.
        $updateMask = (new FieldMask())
            ->setPaths(['labels']);
    
        // Call the API.
        $updateCryptoKeyRequest = (new UpdateCryptoKeyRequest())
            ->setCryptoKey($key)
            ->setUpdateMask($updateMask);
        $updatedKey = $client->updateCryptoKey($updateCryptoKeyRequest);
        printf('Updated key: %s' . PHP_EOL, $updatedKey->getName());
    
        return $updatedKey;
    }

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Build the key.
    key = {
      name:   key_name,
      labels: {
        "new_label" => "new_value"
      }
    }
    
    # Build the field mask.
    update_mask = { paths: ["labels"] }
    
    # Call the API.
    updated_key = client.update_crypto_key crypto_key: key, update_mask: update_mask
    puts "Updated key: #{updated_key.name}"

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def update_key_update_labels(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Update labels on an existing key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
    
        Returns:
            CryptoKey: Updated Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        key = {"name": key_name, "labels": {"new_label": "new_value"}}
    
        # Build the update mask.
        update_mask = {"paths": ["labels"]}
    
        # Call the API.
        updated_key = client.[update_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key)(
            request={"crypto_key": key, "update_mask": update_mask}
        )
        print(f"Updated key: {updated_key.name}")
        return updated_key
    
    

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

Add or update labels to an existing key by using the [CryptoKeys.patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch) method, and include the `labels` property in your request body. For example:
    
    
    {
      "labels": [
        {
          "key": "LABEL_KEY",
          "value": "LABEL_VALUE"
        }
      ]
    }
    

## Removing labels

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring for the key you want to inspect.

  3. In the header, click **Show info panel**.

  4. In the panel, choose the **Labels** tab.

  5. Click the **Delete** delete icon next to the labels you want to delete.

  6. Click **Save**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys update KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        **--remove-labels " LABEL_KEYS"**
    

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the key ring that contains the key.
  * `LOCATION`: the location of the key ring.
  * `LABEL_LIST`: a comma-separated list of label keys that you want to remove from the key—for example, `env,team`.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class UpdateKeyRemoveLabelsSample
    {
        public CryptoKey UpdateKeyRemoveLabels(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
            {
                CryptoKeyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId),
            };
    
            // Build the update mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
            {
                Paths = { "labels" },
            };
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[UpdateCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKey_Google_Cloud_Kms_V1_CryptoKey_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(key, fieldMask);
    
            // Return the updated key.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	fieldmask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateKeyRemoveLabels removes all labels from an existing Cloud KMS key.
    func updateKeyRemoveLabels(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.UpdateCryptoKeyRequest{
    		CryptoKey: &kmspb.CryptoKey{
    			Name:   name,
    			Labels: nil,
    		},
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"labels"},
    		},
    	}
    
    	// Call the API.
    	result, err := client.UpdateCryptoKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update key: %w", err)
    	}
    	fmt.Fprintf(w, "Updated key: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    public class UpdateKeyRemoveLabels {
    
      public void updateKeyRemoveLabels() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        updateKeyRemoveLabels(projectId, locationId, keyRingId, keyId);
      }
    
      // Update a key to remove all labels.
      public void updateKeyRemoveLabels(
          String projectId, String locationId, String keyRingId, String keyId) throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, key ring, and keyId.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Build an empty key with no labels.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder().setName(cryptoKeyName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__)()).build();
    
          // Construct the field mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("labels");
    
          // Create the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client.updateCryptoKey(key, fieldMask);
          System.out.printf("Updated key %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // const versionId = '123';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function updateKeyRemoveLabels() {
      const [key] = await client.updateCryptoKey({
        cryptoKey: {
          name: keyName,
          labels: null,
        },
        updateMask: {
          paths: ['labels'],
        },
      });
    
      console.log(`Removed labels from: ${key.name}`);
      return key;
    }
    
    return updateKeyRemoveLabels();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyRequest;
    use Google\Protobuf\FieldMask;
    
    function update_key_remove_labels(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setName($keyName)
            ->setLabels([]);
    
        // Create the field mask.
        $updateMask = (new FieldMask())
            ->setPaths(['labels']);
    
        // Call the API.
        $updateCryptoKeyRequest = (new UpdateCryptoKeyRequest())
            ->setCryptoKey($key)
            ->setUpdateMask($updateMask);
        $updatedKey = $client->updateCryptoKey($updateCryptoKeyRequest);
        printf('Updated key: %s' . PHP_EOL, $updatedKey->getName());
    
        return $updatedKey;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def update_key_remove_labels(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Remove labels from an existing key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
    
        Returns:
            CryptoKey: Updated Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        key = {
            "name": key_name,
            "labels": [],
        }
    
        # Build the update mask.
        update_mask = {"paths": ["labels"]}
    
        # Call the API.
        updated_key = client.[update_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key)(
            request={"crypto_key": key, "update_mask": update_mask}
        )
        print(f"Updated key: {updated_key.name}")
        return updated_key
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Build the key.
    key = {
      name:   key_name,
      labels: {}
    }
    
    # Build the field mask.
    update_mask = { paths: ["labels"] }
    
    # Call the API.
    updated_key = client.update_crypto_key crypto_key: key, update_mask: update_mask
    puts "Updated key: #{updated_key.name}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

Remove labels from an existing key by using the [CryptoKeys.patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch) method, and include the `labels` property as an empty array in your request body. For example:
    
    
    {
      "labels": []
    }
    

## Audit logging

[Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) for Cloud KMS can be used to log label information when keys are created or updated. Key creation and updates are both [admin activities](https://docs.cloud.google.com/logging/docs/audit#admin-activity), and changes to labels are noted in the admin activity log.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
