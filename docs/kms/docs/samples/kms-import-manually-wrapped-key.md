---
url: https://docs.cloud.google.com/kms/docs/samples/kms-import-manually-wrapped-key/
title: Import a manually wrapped key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:54.838491+00:00
---

# Import a manually wrapped key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-import-manually-wrapped-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Import a manually wrapped key Stay organized with collections  Save and categorize content based on your preferences. 

Import a key into Cloud KMS that you have wrapped manually.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Import a key version into Cloud KMS](https://docs.cloud.google.com/kms/docs/importing-a-key)



## Code sample

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"crypto/ecdsa"
    	"crypto/elliptic"
    	"crypto/rand"
    	"crypto/rsa"
    	"crypto/sha1"
    	"crypto/x509"
    	"encoding/pem"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"github.com/google/tink/go/kwp/subtle"
    )
    
    // importManuallyWrappedKey wraps key material and imports it into KMS.
    func importManuallyWrappedKey(w io.Writer, importJobName, cryptoKeyName string) error {
    	// importJobName := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/importJobs/my-import-job"
    	// cryptoKeyName := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/cryptoKeys/my-imported-key"
    
    	// Generate a ECDSA keypair, and format the private key as PKCS #8 DER.
    	key, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
    	if err != nil {
    		return fmt.Errorf("failed to generate keypair: %w", err)
    	}
    	keyBytes, err := x509.MarshalPKCS8PrivateKey(key)
    	if err != nil {
    		return fmt.Errorf("failed to format private key: %w", err)
    	}
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Generate a temporary 32-byte key for AES-KWP and wrap the key material.
    	kwpKey := make([]byte, 32)
    	if _, err := rand.Read(kwpKey); err != nil {
    		return fmt.Errorf("failed to generate AES-KWP key: %w", err)
    	}
    	kwp, err := subtle.NewKWP(kwpKey)
    	if err != nil {
    		return fmt.Errorf("failed to create KWP cipher: %w", err)
    	}
    	wrappedTarget, err := kwp.Wrap(keyBytes)
    	if err != nil {
    		return fmt.Errorf("failed to wrap target key with KWP: %w", err)
    	}
    
    	// Retrieve the public key from the import job.
    	importJob, err := client.GetImportJob(ctx, &kmspb.GetImportJobRequest{
    		Name: importJobName,
    	})
    	if err != nil {
    		return fmt.Errorf("failed to retrieve import job: %w", err)
    	}
    	pubBlock, _ := pem.Decode([]byte(importJob.PublicKey.Pem))
    	pubAny, err := x509.ParsePKIXPublicKey(pubBlock.Bytes)
    	if err != nil {
    		return fmt.Errorf("failed to parse import job public key: %w", err)
    	}
    	pub, ok := pubAny.(*rsa.PublicKey)
    	if !ok {
    		return fmt.Errorf("unexpected public key type %T, want *rsa.PublicKey", pubAny)
    	}
    
    	// Wrap the KWP key using the import job key.
    	wrappedWrappingKey, err := rsa.EncryptOAEP(sha1.New(), rand.Reader, pub, kwpKey, nil)
    	if err != nil {
    		return fmt.Errorf("failed to wrap KWP key: %w", err)
    	}
    
    	// Concatenate the wrapped KWP key and the wrapped target key.
    	combined := append(wrappedWrappingKey, wrappedTarget...)
    
    	// Build the request.
    	req := &kmspb.ImportCryptoKeyVersionRequest{
    		Parent:     cryptoKeyName,
    		ImportJob:  importJobName,
    		Algorithm:  kmspb.[CryptoKeyVersion_EC_SIGN_P256_SHA256](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU_CryptoKeyVersion_AES_256_KWP),
    		WrappedKey: combined,
    	}
    
    	// Call the API.
    	result, err := client.ImportCryptoKeyVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to import crypto key version: %w", err)
    	}
    	fmt.Fprintf(w, "Created crypto key version: %s\n", result.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html);
    import com.google.cloud.kms.v1.[ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.html);
    import com.google.cloud.kms.v1.[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html);
    import com.google.cloud.kms.v1.[ImportJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.crypto.tink.subtle.Kwp;
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.security.GeneralSecurityException;
    import java.security.KeyFactory;
    import java.security.KeyPair;
    import java.security.KeyPairGenerator;
    import java.security.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html);
    import java.security.SecureRandom;
    import java.security.spec.ECGenParameterSpec;
    import java.security.spec.MGF1ParameterSpec;
    import java.security.spec.X509EncodedKeySpec;
    import java.util.Base64;
    import javax.crypto.Cipher;
    import javax.crypto.spec.OAEPParameterSpec;
    import javax.crypto.spec.PSource;
    
    public class ImportManuallyWrappedKey {
    
      public void importManuallyWrappedKey() throws GeneralSecurityException, IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String cryptoKeyId = "my-crypto-key";
        String importJobId = "my-import-job";
        importManuallyWrappedKey(projectId, locationId, keyRingId, cryptoKeyId, importJobId);
      }
    
      // Generates and imports local key material into Cloud KMS.
      public void importManuallyWrappedKey(
          String projectId, String locationId, String keyRingId, String cryptoKeyId, String importJobId)
          throws GeneralSecurityException, IOException {
    
        // Generate a new ECDSA keypair, and format the private key as PKCS #8 DER.
        KeyPairGenerator generator = KeyPairGenerator.getInstance("EC");
        generator.initialize(new ECGenParameterSpec("secp256r1"));
        KeyPair kp = generator.generateKeyPair();
        byte[] privateBytes = kp.getPrivate().getEncoded();
    
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the crypto key and import job names from the project, location,
          // key ring, and ID.
          final [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName =
              [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, cryptoKeyId);
          final [ImportJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) importJobName =
              [ImportJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html).of(projectId, locationId, keyRingId, importJobId);
    
          // Generate a temporary 32-byte key for AES-KWP and wrap the key material.
          byte[] kwpKey = new byte[32];
          new SecureRandom().nextBytes(kwpKey);
          Kwp kwp = new Kwp(kwpKey);
          final byte[] wrappedTargetKey = kwp.[wrap](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DiscardUnknownFieldsParser.html#com_google_protobuf_DiscardUnknownFieldsParser__T_wrap_com_google_protobuf_Parser_T__)(privateBytes);
    
          // Retrieve the public key from the import job.
          [ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) importJob = client.getImportJob(importJobName);
          String publicKeyStr = importJob.[getPublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getPublicKey__)().getPem();
          // Manually convert PEM to DER. :-(
          publicKeyStr = publicKeyStr.replace("-----BEGIN PUBLIC KEY-----", "");
          publicKeyStr = publicKeyStr.replace("-----END PUBLIC KEY-----", "");
          publicKeyStr = publicKeyStr.replaceAll("\n", "");
          byte[] publicKeyBytes = Base64.getDecoder().decode(publicKeyStr);
          [PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey =
              KeyFactory.getInstance("RSA").generatePublic(new X509EncodedKeySpec(publicKeyBytes));
    
          // Wrap the KWP key using the import job key.
          Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA-1AndMGF1Padding");
          cipher.init(
              Cipher.ENCRYPT_MODE,
              publicKey,
              new OAEPParameterSpec(
                  "SHA-1", "MGF1", MGF1ParameterSpec.SHA1, PSource.PSpecified.DEFAULT));
          byte[] wrappedWrappingKey = cipher.doFinal(kwpKey);
    
          // Concatenate the wrapped KWP key and the wrapped target key.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) combinedWrappedKeys =
              [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(wrappedWrappingKey).[concat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_concat_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(wrappedTargetKey));
    
          // Import the wrapped key material.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) version =
              client.importCryptoKeyVersion(
                  [ImportCryptoKeyVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.html).newBuilder()
                      .setParent(cryptoKeyName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__)())
                      .setImportJob(importJobName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html#com_google_cloud_kms_v1_ImportJobName_toString__)())
                      .setAlgorithm([CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).CryptoKeyVersionAlgorithm.EC_SIGN_P256_SHA256)
                      .[setRsaAesWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportCryptoKeyVersionRequest.Builder.html#com_google_cloud_kms_v1_ImportCryptoKeyVersionRequest_Builder_setRsaAesWrappedKey_com_google_protobuf_ByteString_)(combinedWrappedKeys)
                      .build());
    
          System.out.printf("Imported: %s%n", version.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const cryptoKeyId = 'my-imported-key';
    // const importJobId = 'my-import-job';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the crypto key and importjob resource names
    const cryptoKeyName = client.cryptoKeyPath(
      projectId,
      locationId,
      keyRingId,
      cryptoKeyId
    );
    const importJobName = client.importJobPath(
      projectId,
      locationId,
      keyRingId,
      importJobId
    );
    
    async function wrapAndImportKey() {
      // Generate a 32-byte key to import.
      const crypto = require('crypto');
      const targetKey = crypto.randomBytes(32);
    
      const [importJob] = await client.getImportJob({name: importJobName});
    
      // Wrap the target key using the import job key
      const wrappedTargetKey = crypto.publicEncrypt(
        {
          key: importJob.publicKey.pem,
          oaepHash: 'sha256',
          padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
        },
        targetKey
      );
    
      // Import the target key version
      const [version] = await client.importCryptoKeyVersion({
        parent: cryptoKeyName,
        importJob: importJobName,
        algorithm: 'GOOGLE_SYMMETRIC_ENCRYPTION',
        wrappedKey: wrappedTargetKey,
      });
    
      console.log(`Imported key version: ${version.name}`);
      return version;
    }
    
    return wrapAndImportKey();

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    # Import the client library and Python standard cryptographic libraries.
    from cryptography.hazmat import backends
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives import keywrap
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.asymmetric import padding
    from google.cloud import kms
    
    
    def import_manually_wrapped_key(
        project_id: str,
        location_id: str,
        key_ring_id: str,
        crypto_key_id: str,
        import_job_id: str,
    ) -> None:
        """
        Generates and imports local key material to Cloud KMS.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            crypto_key_id (string): ID of the key to import (e.g. 'my-asymmetric-signing-key').
            import_job_id (string): ID of the import job (e.g. 'my-import-job').
        """
    
        # Generate some key material in Python and format it in PKCS #8 DER as
        # required by Google Cloud KMS.
        key = ec.generate_private_key(ec.SECP256R1, backends.default_backend())
        formatted_key = key.private_bytes(
            serialization.Encoding.DER,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
    
        print(f"Generated key bytes: {formatted_key!r}")
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Retrieve the fully-qualified crypto_key and import_job string.
        crypto_key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(
            project_id, location_id, key_ring_id, crypto_key_id
        )
        import_job_name = client.[import_job_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_job_path)(
            project_id, location_id, key_ring_id, import_job_id
        )
    
        # Generate a temporary 32-byte key for AES-KWP and wrap the key material.
        kwp_key = os.urandom(32)
        wrapped_target_key = keywrap.aes_key_wrap_with_padding(
            kwp_key, formatted_key, backends.default_backend()
        )
    
        # Retrieve the public key from the import job.
        import_job = client.[get_import_job](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_import_job)(name=import_job_name)
        import_job_pub = serialization.load_pem_public_key(
            bytes(import_job.public_key.pem, "UTF-8"), backends.default_backend()
        )
    
        # Wrap the KWP key using the import job key.
        wrapped_kwp_key = import_job_pub.encrypt(
            kwp_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA1()),
                algorithm=hashes.SHA1(),
                label=None,
            ),
        )
    
        # Import the wrapped key material.
        client.[import_crypto_key_version](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_crypto_key_version)(
            {
                "parent": crypto_key_name,
                "import_job": import_job_name,
                "algorithm": kms.[CryptoKeyVersion](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).EC_SIGN_P256_SHA256,
                "rsa_aes_wrapped_key": wrapped_kwp_key + wrapped_target_key,
            }
        )
    
        print(f"Imported: {import_job.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
