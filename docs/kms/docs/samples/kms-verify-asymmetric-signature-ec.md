---
url: https://docs.cloud.google.com/kms/docs/samples/kms-verify-asymmetric-signature-ec/
title: Verify an asymmetric signature of an EC key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:31.932711+00:00
---

# Verify an asymmetric signature of an EC key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-verify-asymmetric-signature-ec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Verify an asymmetric signature of an EC key Stay organized with collections  Save and categorize content based on your preferences. 

Verify the signature of a message signed with an asymmetric EC key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and validating digital signatures](https://docs.cloud.google.com/kms/docs/create-validate-signatures)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public class VerifyAsymmetricSignatureEcSample
    {
        // Cloud KMS returns signatures in a DER-encoded format. .NET requires
        // signatures to be in IEEE 1363 format, and converting between these formats
        // is a few hundred lines of code.
        //
        // https://github.com/dotnet/runtime/pull/1612 exposes these helpers, but will
        // not be available until .NET 5. Until then, you will need to use an external
        // library or package to validate signatures.
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"crypto/ecdsa"
    	"crypto/sha256"
    	"crypto/x509"
    	"encoding/asn1"
    	"encoding/pem"
    	"fmt"
    	"io"
    	"math/big"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // verifyAsymmetricSignatureEC will verify that an 'EC_SIGN_P256_SHA256' signature is
    // valid for a given message.
    func verifyAsymmetricSignatureEC(w io.Writer, name string, message, signature []byte) error {
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
    	// ECDSA format.
    	block, _ := pem.Decode([]byte(response.Pem))
    	publicKey, err := x509.ParsePKIXPublicKey(block.Bytes)
    	if err != nil {
    		return fmt.Errorf("failed to parse public key: %w", err)
    	}
    	ecKey, ok := publicKey.(*ecdsa.PublicKey)
    	if !ok {
    		return fmt.Errorf("public key is not elliptic curve")
    	}
    
    	// Verify Elliptic Curve signature.
    	var parsedSig struct{ R, S *big.Int }
    	if _, err = asn1.Unmarshal(signature, &parsedSig); err != nil {
    		return fmt.Errorf("asn1.Unmarshal: %w", err)
    	}
    
    	digest := sha256.Sum256(message)
    	if !ecdsa.Verify(ecKey, digest[:], parsedSig.R, parsedSig.S) {
    		return fmt.Errorf("failed to verify signature")
    	}
    	fmt.Fprintf(w, "Verified signature!")
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
    
    public class VerifyAsymmetricEc {
    
      public void verifyAsymmetricEc() throws IOException, GeneralSecurityException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        String message = "my message";
        byte[] signature = null;
        verifyAsymmetricEc(projectId, locationId, keyRingId, keyId, keyVersionId, message, signature);
      }
    
      // CPD-OFF
      // Verify the signature of a message signed with an RSA key.
      public void verifyAsymmetricEc(
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
          java.security.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) ecKey = KeyFactory.getInstance("EC").generatePublic(keySpec);
    
          // Verify the 'RSA_SIGN_PKCS1_2048_SHA256' signature.
          // For other key algorithms:
          // http://docs.oracle.com/javase/7/docs/technotes/guides/security/StandardNames.html#Signature
          Signature ecVerify = Signature.getInstance("SHA256withECDSA");
          ecVerify.initVerify(ecKey);
          ecVerify.update(plaintext);
    
          // Verify the signature.
          boolean verified = ecVerify.verify(signature);
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
    
    async function verifyAsymmetricSignatureEc() {
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
      };
    
      // Verify the signature using the public key
      const verified = verify.verify(key, signatureBuffer);
      return verified;
    }
    
    return verifyAsymmetricSignatureEc();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\GetPublicKeyRequest;
    
    function verify_asymmetric_ec(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123',
        string $message = '...',
        string $signature = '...'
    ): bool {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key version name.
        $keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Get the public key.
        $getPublicKeyRequest = (new GetPublicKeyRequest())
            ->setName($keyVersionName);
        $publicKey = $client->getPublicKey($getPublicKeyRequest);
    
        // Verify the signature. The hash algorithm must correspond to the key
        // algorithm. The openssl_verify command returns 1 on success, 0 on falure.
        $verified = openssl_verify($message, $signature, $publicKey->getPem(), OPENSSL_ALGO_SHA256) === 1;
        printf('Signature verified: %s', $verified);
    
        return $verified;
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
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.asymmetric import utils
    
    # Import the client library.
    from google.cloud import kms
    
    
    def verify_asymmetric_ec(
        project_id: str,
        location_id: str,
        key_ring_id: str,
        key_id: str,
        version_id: str,
        message: str,
        signature: str,
    ) -> bool:
        """
        Verify the signature of an message signed with an asymmetric EC key.
    
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
    
        # Extract and parse the public key as a PEM-encoded EC key.
        pem = public_key.pem.encode("utf-8")
        ec_key = serialization.load_pem_public_key(pem, default_backend())
        hash_ = hashlib.sha256(message_bytes).digest()
    
        # Attempt to verify.
        try:
            sha256 = hashes.SHA256()
            ec_key.verify(signature, hash_, ec.ECDSA(utils.Prehashed(sha256)))
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
    ec_key = OpenSSL::PKey::EC.new public_key.pem
    
    # Verify the signature.
    verified = ec_key.verify "sha256", signature, message
    puts "Verified: #{verified}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
