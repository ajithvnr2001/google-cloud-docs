---
url: https://docs.cloud.google.com/kms/docs/samples/kms-encrypt-asymmetric/
title: Encrypt with an asymmetric key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:45.774317+00:00
---

# Encrypt with an asymmetric key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-encrypt-asymmetric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Encrypt with an asymmetric key Stay organized with collections  Save and categorize content based on your preferences. 

Encrypt plaintext using the public key portion of an asymmetric key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Encrypting and decrypting data with an asymmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using System;
    using System.Security.Cryptography;
    using System.Text;
    
    public class EncryptAsymmetricSample
    {
        public byte[] EncryptAsymmetric(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123",
          string message = "Sample message")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key version name.
            [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId);
    
            // Get the public key.
            [PublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.html) publicKey = client.[GetPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetPublicKey_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_)(keyVersionName);
    
            // Split the key into blocks and base64-decode the PEM parts.
            string[] blocks = publicKey.[Pem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.html#Google_Cloud_Kms_V1_PublicKey_Pem).Split("-", StringSplitOptions.RemoveEmptyEntries);
            byte[] pem = Convert.FromBase64String(blocks[1]);
    
            // Create a new RSA key.
            RSA rsa = RSA.Create();
            rsa.ImportSubjectPublicKeyInfo(pem, out _);
    
            // Convert the message into bytes. Cryptographic plaintexts and
            // ciphertexts are always byte arrays.
            byte[] plaintext = Encoding.UTF8.GetBytes(message);
    
            // Encrypt the data.
            byte[] ciphertext = rsa.Encrypt(plaintext, RSAEncryptionPadding.OaepSHA256);
            return ciphertext;
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"crypto/rand"
    	"crypto/rsa"
    	"crypto/sha256"
    	"crypto/x509"
    	"encoding/pem"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // encryptAsymmetric encrypts data on your local machine using an
    // 'RSA_DECRYPT_OAEP_2048_SHA256' public key retrieved from Cloud KMS.
    func encryptAsymmetric(w io.Writer, name string, message string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    	// message := "Sample message"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Retrieve the public key from Cloud KMS. This is the only operation that
    	// involves Cloud KMS. The remaining operations take place on your local
    	// machine.
    	response, err := client.GetPublicKey(ctx, &kmspb.GetPublicKeyRequest{
    		Name: name,
    	})
    	if err != nil {
    		return fmt.Errorf("failed to get public key: %w", err)
    	}
    
    	// Parse the public key. Note, this example assumes the public key is in the
    	// RSA format.
    	block, _ := pem.Decode([]byte(response.Pem))
    	publicKey, err := x509.ParsePKIXPublicKey(block.Bytes)
    	if err != nil {
    		return fmt.Errorf("failed to parse public key: %w", err)
    	}
    	rsaKey, ok := publicKey.(*rsa.PublicKey)
    	if !ok {
    		return fmt.Errorf("public key is not rsa")
    	}
    
    	// Convert the message into bytes. Cryptographic plaintexts and
    	// ciphertexts are always byte arrays.
    	plaintext := []byte(message)
    
    	// Encrypt data using the RSA public key.
    	ciphertext, err := rsa.EncryptOAEP(sha256.New(), rand.Reader, rsaKey, plaintext, nil)
    	if err != nil {
    		return fmt.Errorf("rsa.EncryptOAEP: %w", err)
    	}
    	fmt.Fprintf(w, "Encrypted ciphertext: %s", ciphertext)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html);
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.StringReader;
    import java.nio.charset.StandardCharsets;
    import java.security.GeneralSecurityException;
    import java.security.KeyFactory;
    import java.security.spec.MGF1ParameterSpec;
    import java.security.spec.X509EncodedKeySpec;
    import java.util.Base64;
    import java.util.stream.Collectors;
    import javax.crypto.Cipher;
    import javax.crypto.spec.OAEPParameterSpec;
    import javax.crypto.spec.PSource;
    
    public class EncryptAsymmetric {
    
      public void encryptAsymmetric() throws IOException, GeneralSecurityException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        String plaintext = "Plaintext to encrypt";
        encryptAsymmetric(projectId, locationId, keyRingId, keyId, keyVersionId, plaintext);
      }
    
      // Encrypt data that was encrypted using the public key component of the given
      // key version.
      public void encryptAsymmetric(
          String projectId,
          String locationId,
          String keyRingId,
          String keyId,
          String keyVersionId,
          String plaintext)
          throws IOException, GeneralSecurityException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the key version name from the project, location, key ring, key,
          // and key version.
          [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName =
              [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html).of(projectId, locationId, keyRingId, keyId, keyVersionId);
    
          // Get the public key.
          [PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey = client.getPublicKey(keyVersionName);
    
          // Convert the public PEM key to a DER key (see helper below).
          byte[] derKey = convertPemToDer(publicKey.[getPem](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html#com_google_cloud_kms_v1_PublicKey_getPem__)());
          X509EncodedKeySpec keySpec = new X509EncodedKeySpec(derKey);
          java.security.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) rsaKey = KeyFactory.getInstance("RSA").generatePublic(keySpec);
    
          // Encrypt plaintext for the 'RSA_DECRYPT_OAEP_2048_SHA256' key.
          // For other key algorithms:
          // https://docs.oracle.com/javase/7/docs/api/javax/crypto/Cipher.html
          Cipher cipher = Cipher.getInstance("RSA/ECB/OAEPWithSHA-256AndMGF1Padding");
          OAEPParameterSpec oaepParams =
              new OAEPParameterSpec(
                  "SHA-256", "MGF1", MGF1ParameterSpec.SHA256, PSource.PSpecified.DEFAULT);
          cipher.init(Cipher.ENCRYPT_MODE, rsaKey, oaepParams);
          byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));
          System.out.printf("Ciphertext: %s%n", ciphertext);
        }
      }
    
      // Converts a base64-encoded PEM certificate like the one returned from Cloud
      // KMS into a DER formatted certificate for use with the Java APIs.
      private byte[] convertPemToDer(String pem) {
        BufferedReader bufferedReader = new BufferedReader(new StringReader(pem));
        String encoded =
            bufferedReader
                .lines()
                .filter(line -> !line.startsWith("-----BEGIN") && !line.startsWith("-----END"))
                .collect(Collectors.joining());
        return Base64.getDecoder().decode(encoded);
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
    // const keyId = 'my-key';
    // const versionId = '123';
    // const plaintextBuffer = Buffer.from('...');
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key version name
    const versionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      keyId,
      versionId
    );
    
    async function encryptAsymmetric() {
      // Get public key from Cloud KMS
      const [publicKey] = await client.getPublicKey({
        name: versionName,
      });
    
      // Optional, but recommended: perform integrity verification on publicKey.
      // For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
      // https://cloud.google.com/kms/docs/data-integrity-guidelines
      const crc32c = require('fast-crc32c');
      if (publicKey.name !== versionName) {
        throw new Error('GetPublicKey: request corrupted in-transit');
      }
      if (crc32c.calculate(publicKey.pem) !== Number(publicKey.pemCrc32c.value)) {
        throw new Error('GetPublicKey: response corrupted in-transit');
      }
    
      // Import and setup crypto
      const crypto = require('crypto');
    
      // Encrypt plaintext locally using the public key. This example uses a key
      // that was configured with sha256 hash with OAEP padding. Update these
      // values to match the Cloud KMS key.
      //
      // NOTE: In Node < 12, this function does not properly consume the OAEP
      // padding and thus produces invalid ciphertext. If you are using Node to do
      // public key encryption, please use version 12+.
      const ciphertextBuffer = crypto.publicEncrypt(
        {
          key: publicKey.pem,
          oaepHash: 'sha256',
          padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
        },
        plaintextBuffer
      );
    
      console.log(`Ciphertext: ${ciphertextBuffer.toString('base64')}`);
      return ciphertextBuffer;
    }
    
    return encryptAsymmetric();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    function encrypt_asymmetric(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123',
        string $plaintext = '...'
    ): void {
        // PHP has limited support for asymmetric encryption operations.
        // Specifically, openssl_public_encrypt() does not allow customizing
        // algorithms or padding. Thus, it is not currently possible to use PHP
        // core for asymmetric operations on RSA keys.
        //
        // Third party libraries like phpseclib may provide the required
        // functionality. Google does not endorse this external library.
    }

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import base64 for printing the ciphertext.
    import base64
    
    # Import cryptographic helpers from the cryptography package.
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    
    # Import the client library.
    from google.cloud import kms
    
    
    def encrypt_asymmetric(
        project_id: str,
        location_id: str,
        key_ring_id: str,
        key_id: str,
        version_id: str,
        plaintext: str,
    ) -> bytes:
        """
        Encrypt plaintext using the public key portion of an asymmetric key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the key version to use (e.g. '1').
            plaintext (string): message to encrypt
    
        Returns:
            bytes: Encrypted ciphertext.
    
        """
    
        # Convert the plaintext to bytes.
        plaintext_bytes = plaintext.encode("utf-8")
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        # Get the public key.
        public_key = client.[get_public_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_public_key)(request={"name": key_version_name})
    
        # Extract and parse the public key as a PEM-encoded RSA key.
        pem = public_key.pem.encode("utf-8")
        rsa_key = serialization.load_pem_public_key(pem, default_backend())
    
        # Construct the padding. Note that the padding differs based on key choice.
        sha256 = hashes.SHA256()
        mgf = padding.MGF1(algorithm=sha256)
        pad = padding.OAEP(mgf=mgf, algorithm=sha256, label=None)
    
        # Encrypt the data using the public key.
        ciphertext = rsa_key.encrypt(plaintext_bytes, pad)
        print(f"Ciphertext: {base64.b64encode(ciphertext)!r}")
        return ciphertext
    
    

### Ruby

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Ruby has limited support for asymmetric encryption operations. Specifically,
    # public_encrypt() does not allow customizing the MGF hash algorithm. Thus, it
    # is not currently possible to use Ruby core for asymmetric encryption
    # operations on RSA keys from Cloud KMS.
    #
    # Third party libraries may provide the required functionality. Google does
    # not endorse these external libraries.

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
