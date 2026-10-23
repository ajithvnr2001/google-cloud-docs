---
url: https://docs.cloud.google.com/kms/docs/samples/kms-verify-asymmetric-signature-rsa/
title: Verify asymmetric signature of an RSA key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:46.730494+00:00
---

# Verify asymmetric signature of an RSA key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-verify-asymmetric-signature-rsa/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Verify asymmetric signature of an RSA key Stay organized with collections  Save and categorize content based on your preferences. 

Verify the signature of a message signed with an asymmetric RSA key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and validating digital signatures](https://docs.cloud.google.com/kms/docs/create-validate-signatures)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using System;
    using System.Security.Cryptography;
    using System.Text;
    
    public class VerifyAsymmetricSignatureRsaSample
    {
        public bool VerifyAsymmetricSignatureRsa(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123",
          string message = "my message",
          byte[] signature = null)
        {
            // Build the key version name.
            [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId);
    
            // Calculate the digest of the message.
            SHA256 sha256 = SHA256.Create();
            byte[] digest = sha256.ComputeHash(Encoding.UTF8.GetBytes(message));
    
            // Get the public key.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
            [PublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.html) publicKey = client.[GetPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetPublicKey_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_)(keyVersionName);
    
            // Split the key into blocks and base64-decode the PEM parts.
            string[] blocks = publicKey.[Pem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.html#Google_Cloud_Kms_V1_PublicKey_Pem).Split("-", StringSplitOptions.RemoveEmptyEntries);
            byte[] pem = Convert.FromBase64String(blocks[1]);
    
            // Create a new RSA key.
            RSA rsa = RSA.Create();
            rsa.ImportSubjectPublicKeyInfo(pem, out _);
    
            // Verify the signature.
            bool verified = rsa.VerifyHash(digest, signature, HashAlgorithmName.SHA256, RSASignaturePadding.Pss);
    
            // Return the result.
            return verified;
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"crypto"
    	"crypto/rsa"
    	"crypto/sha256"
    	"crypto/x509"
    	"encoding/pem"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // verifyAsymmetricSignatureRSA will verify that an 'RSA_SIGN_PSS_2048_SHA256' signature
    // is valid for a given message.
    func verifyAsymmetricSignatureRSA(w io.Writer, name string, message, signature []byte) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    	// message := "my message"
    	// signature := []byte("...")  // Response from a sign request
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Retrieve the public key from KMS.
    	response, err := client.GetPublicKey(ctx, &kmspb.GetPublicKeyRequest{Name: name})
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
    
    	// Verify the RSA signature.
    	digest := sha256.Sum256(message)
    	if err := rsa.VerifyPSS(rsaKey, crypto.SHA256, digest[:], signature, &rsa.PSSOptions{
    		SaltLength: len(digest),
    		Hash:       crypto.SHA256,
    	}); err != nil {
    		return fmt.Errorf("failed to verify signature: %w", err)
    	}
    
    	fmt.Fprint(w, "Verified signature!\n")
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
    import java.security.Signature;
    import java.security.spec.X509EncodedKeySpec;
    import java.util.Base64;
    import java.util.stream.Collectors;
    
    public class VerifyAsymmetricRsa {
    
      public void verifyAsymmetricRsa() throws IOException, GeneralSecurityException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        String message = "my message";
        byte[] signature = null;
        verifyAsymmetricRsa(projectId, locationId, keyRingId, keyId, keyVersionId, message, signature);
      }
    
      // Verify the signature of a message signed with an RSA key.
      public void verifyAsymmetricRsa(
          String projectId,
          String locationId,
          String keyRingId,
          String keyId,
          String keyVersionId,
          String message,
          byte[] signature)
          throws IOException, GeneralSecurityException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, and key ring, key, and key version.
          [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName =
              [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html).of(projectId, locationId, keyRingId, keyId, keyVersionId);
    
          // Convert the message into bytes. Cryptographic plaintexts and
          // ciphertexts are always byte arrays.
          byte[] plaintext = message.getBytes(StandardCharsets.UTF_8);
    
          // Get the public key.
          [PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey = client.getPublicKey(keyVersionName);
    
          // Convert the public PEM key to a DER key (see helper below).
          byte[] derKey = convertPemToDer(publicKey.[getPem](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html#com_google_cloud_kms_v1_PublicKey_getPem__)());
          X509EncodedKeySpec keySpec = new X509EncodedKeySpec(derKey);
          java.security.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) rsaKey = KeyFactory.getInstance("RSA").generatePublic(keySpec);
    
          // Verify the 'RSA_SIGN_PKCS1_2048_SHA256' signature.
          // For other key algorithms:
          // http://docs.oracle.com/javase/7/docs/technotes/guides/security/StandardNames.html#Signature
          Signature rsaVerify = Signature.getInstance("SHA256withRSA");
          rsaVerify.initVerify(rsaKey);
          rsaVerify.update(plaintext);
    
          // Verify the signature.
          boolean verified = rsaVerify.verify(signature);
          System.out.printf("Signature verified: %s", verified);
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
    // const projectId = 'your-project-id';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // const versionId = '1';
    // const message = 'my message to verify';
    // const signatureBuffer = Buffer.from('...');
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const versionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      keyId,
      versionId
    );
    
    async function verifyAsymmetricSignatureRsa() {
      // Get public key
      const [publicKey] = await client.getPublicKey({
        name: versionName,
      });
    
      // Create the verifier. The algorithm must match the algorithm of the key.
      const crypto = require('crypto');
      const verify = crypto.createVerify('sha256');
      verify.update(message);
      verify.end();
    
      // Build the key object
      const key = {
        key: publicKey.pem,
        padding: crypto.constants.RSA_PKCS1_PSS_PADDING,
      };
    
      // Verify the signature using the public key
      const verified = verify.verify(key, signatureBuffer);
      return verified;
    }
    
    return verifyAsymmetricSignatureRsa();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    function verify_asymmetric_rsa(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123',
        string $message = '...',
        string $signature = '...'
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
    
    
    # Import hashlib.
    import hashlib
    
    # Import cryptographic helpers from the cryptography package.
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import padding
    from cryptography.hazmat.primitives.asymmetric import utils
    
    # Import the client library.
    from google.cloud import kms
    
    
    def verify_asymmetric_rsa(
        project_id: str,
        location_id: str,
        key_ring_id: str,
        key_id: str,
        version_id: str,
        message: str,
        signature: str,
    ) -> bool:
        """
        Verify the signature of an message signed with an asymmetric RSA key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the version to use (e.g. '1').
            message (string): Original message (e.g. 'my message')
            signature (bytes): Signature from a sign request.
    
        Returns:
            bool: True if verified, False otherwise
    
        """
    
        # Convert the message to bytes.
        message_bytes = message.encode("utf-8")
    
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
        hash_ = hashlib.sha256(message_bytes).digest()
    
        # Attempt to verify.
        try:
            sha256 = hashes.SHA256()
            pad = padding.PKCS1v15()
            rsa_key.verify(signature, hash_, pad, utils.Prehashed(sha256))
            print("Signature verified")
            return True
        except InvalidSignature:
            print("Signature failed to verify")
            return False
    
    

### Ruby

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    # version_id  = "123"
    # message     = "my message"
    # signature   = "..."
    
    # Require the library.
    require "google/cloud/kms"
    require "openssl"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the key version name.
    key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project:            project_id,
                                                      location:           location_id,
                                                      key_ring:           key_ring_id,
                                                      crypto_key:         key_id,
                                                      crypto_key_version: version_id
    
    # Get the public key.
    public_key = client.get_public_key name: key_version_name
    
    # Parse the public key.
    rsa_key = OpenSSL::PKey::RSA.new public_key.pem
    
    # Verify the signature.
    #
    # Note: The verify_pss() method only exists in Ruby 2.5+.
    verified = rsa_key.verify_pss "sha256", signature, message, salt_length: :digest, mgf1_hash: "sha256"
    puts "Verified: #{verified}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
