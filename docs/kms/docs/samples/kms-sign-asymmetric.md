---
url: https://docs.cloud.google.com/kms/docs/samples/kms-sign-asymmetric/
title: Retrieve an asymmetric signature \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:45.170354+00:00
---

# Retrieve an asymmetric signature  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-sign-asymmetric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Retrieve an asymmetric signature Stay organized with collections  Save and categorize content based on your preferences. 

Get an asymmetric signature of the SHA-256 hash of an input message using the KMS API.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and validating digital signatures](https://docs.cloud.google.com/kms/docs/create-validate-signatures)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Security.Cryptography;
    using System.Text;
    
    public class SignAsymmetricSample
    {
        public byte[] SignAsymmetric(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123",
          string message = "Sample message")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key version name.
            [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId);
    
            // Convert the message into bytes. Cryptographic plaintexts and
            // ciphertexts are always byte arrays.
            byte[] plaintext = Encoding.UTF8.GetBytes(message);
    
            // Calculate the digest.
            SHA256 sha256 = SHA256.Create();
            byte[] hash = sha256.ComputeHash(plaintext);
    
            // Build the digest.
            //
            // Note: Key algorithms will require a varying hash function. For
            // example, EC_SIGN_P384_SHA384 requires SHA-384.
            [Digest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Digest.html) digest = new [Digest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Digest.html)
            {
                Sha256 = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(hash),
            };
    
            // Call the API.
            [AsymmetricSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse.html) result = client.[AsymmetricSign](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_AsymmetricSign_Google_Cloud_Kms_V1_AsymmetricSignRequest_Google_Api_Gax_Grpc_CallSettings_)(keyVersionName, digest);
    
            // Get the signature.
            byte[] signature = result.[Signature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse.html#Google_Cloud_Kms_V1_AsymmetricSignResponse_Signature).ToByteArray();
    
            // Return the result.
            return signature;
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"crypto/sha256"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"google.golang.org/protobuf/types/known/wrapperspb"
    )
    
    // signAsymmetric will sign a plaintext message using a saved asymmetric private
    // key stored in Cloud KMS.
    func signAsymmetric(w io.Writer, name string, message string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    	// message := "my message"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Convert the message into bytes. Cryptographic plaintexts and
    	// ciphertexts are always byte arrays.
    	plaintext := []byte(message)
    
    	// Calculate the digest of the message.
    	digest := sha256.New()
    	if _, err := digest.Write(plaintext); err != nil {
    		return fmt.Errorf("failed to create digest: %w", err)
    	}
    
    	// Optional but recommended: Compute digest's CRC32C.
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    
    	}
    	digestCRC32C := crc32c(digest.Sum(nil))
    
    	// Build the signing request.
    	//
    	// Note: Key algorithms will require a varying hash function. For example,
    	// EC_SIGN_P384_SHA384 requires SHA-384.
    	req := &kmspb.AsymmetricSignRequest{
    		Name: name,
    		Digest: &kmspb.Digest{
    			Digest: &kmspb.Digest_Sha256{
    				Sha256: digest.Sum(nil),
    			},
    		},
    		DigestCrc32C: wrapperspb.Int64(int64(digestCRC32C)),
    	}
    
    	// Call the API.
    	result, err := client.AsymmetricSign(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to sign digest: %w", err)
    	}
    
    	// Optional, but recommended: perform integrity verification on result.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	if result.VerifiedDigestCrc32C == false {
    		return fmt.Errorf("AsymmetricSign: request corrupted in-transit")
    	}
    	if result.Name != req.Name {
    		return fmt.Errorf("AsymmetricSign: request corrupted in-transit")
    	}
    	if int64(crc32c(result.Signature)) != result.SignatureCrc32C.Value {
    		return fmt.Errorf("AsymmetricSign: response corrupted in-transit")
    	}
    
    	fmt.Fprintf(w, "Signed digest: %s", result.Signature)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[AsymmetricSignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricSignResponse.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[Digest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.Digest.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.security.GeneralSecurityException;
    import java.security.MessageDigest;
    
    public class SignAsymmetric {
    
      public void signAsymmetric() throws IOException, GeneralSecurityException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        String message = "my message";
        signAsymmetric(projectId, locationId, keyRingId, keyId, keyVersionId, message);
      }
    
      // Get the public key associated with an asymmetric key.
      public void signAsymmetric(
          String projectId,
          String locationId,
          String keyRingId,
          String keyId,
          String keyVersionId,
          String message)
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
    
          // Convert the message into bytes. Cryptographic plaintexts and
          // ciphertexts are always byte arrays.
          byte[] plaintext = message.getBytes(StandardCharsets.UTF_8);
    
          // Calculate the digest.
          MessageDigest sha256 = MessageDigest.getInstance("SHA-256");
          byte[] hash = sha256.digest(plaintext);
    
          // Build the digest object.
          [Digest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.Digest.html) digest = [Digest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.Digest.html).newBuilder().[setSha256](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.Digest.Builder.html#com_google_cloud_kms_v1_Digest_Builder_setSha256_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(hash)).build();
    
          // Sign the digest.
          [AsymmetricSignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricSignResponse.html) result = client.asymmetricSign(keyVersionName, digest);
    
          // Get the signature.
          byte[] signature = result.[getSignature](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricSignResponse.html#com_google_cloud_kms_v1_AsymmetricSignResponse_getSignature__)().toByteArray();
    
          System.out.printf("Signature %s%n", signature);
        }
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
    // const versionId = '123';
    // const message = Buffer.from('...');
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the version name
    const versionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      keyId,
      versionId
    );
    
    async function signAsymmetric() {
      // Create a digest of the message. The digest needs to match the digest
      // configured for the Cloud KMS key.
      const crypto = require('crypto');
      const hash = crypto.createHash('sha256');
      hash.update(message);
      const digest = hash.digest();
    
      // Optional but recommended: Compute digest's CRC32C.
      // Ensure fast-crc32c has been installed, `npm i fast-crc32c`.
      const crc32c = require('fast-crc32c');
      const digestCrc32c = crc32c.calculate(digest);
    
      // Sign the message with Cloud KMS
      const [signResponse] = await client.asymmetricSign({
        name: versionName,
        digest: {
          sha256: digest,
        },
        digestCrc32c: {
          value: digestCrc32c,
        },
      });
    
      // Optional, but recommended: perform integrity verification on signResponse.
      // For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
      // https://cloud.google.com/kms/docs/data-integrity-guidelines
      if (signResponse.name !== versionName) {
        throw new Error('AsymmetricSign: request corrupted in-transit');
      }
      if (!signResponse.verifiedDigestCrc32c) {
        throw new Error('AsymmetricSign: request corrupted in-transit');
      }
      if (
        crc32c.calculate(signResponse.signature) !==
        Number(signResponse.signatureCrc32c.value)
      ) {
        throw new Error('AsymmetricSign: response corrupted in-transit');
      }
    
      // Example of how to display signature. Because the signature is in a binary
      // format, you need to encode the output before printing it to a console or
      // displaying it on a screen.
      const encoded = signResponse.signature.toString('base64');
      console.log(`Signature: ${encoded}`);
    
      return signResponse.signature;
    }
    
    return signAsymmetric();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Kms\V1\AsymmetricSignRequest;
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\Digest;
    
    function sign_asymmetric(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123',
        string $message = '...'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key version name.
        $keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Calculate the hash.
        $hash = hash('sha256', $message, true);
    
        // Build the digest.
        //
        // Note: Key algorithms will require a varying hash function. For
        // example, EC_SIGN_P384_SHA384 requires SHA-384.
        $digest = (new Digest())
            ->setSha256($hash);
    
        // Call the API.
        $asymmetricSignRequest = (new AsymmetricSignRequest())
            ->setName($keyVersionName)
            ->setDigest($digest);
        $signResponse = $client->asymmetricSign($asymmetricSignRequest);
        printf('Signature: %s' . PHP_EOL, $signResponse->getSignature());
    
        return $signResponse;
    }

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import base64 for printing the ciphertext.
    import base64
    
    # Import hashlib for calculating hashes.
    import hashlib
    
    # Import the client library.
    from google.cloud import kms
    
    
    def sign_asymmetric(
        project_id: str,
        location_id: str,
        key_ring_id: str,
        key_id: str,
        version_id: str,
        message: str,
    ) -> kms.AsymmetricSignResponse:
        """
        Sign a message using the private key part of an asymmetric key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): Version to use (e.g. '1').
            message (string): Message to sign.
    
        Returns:
            AsymmetricSignResponse: Signature.
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        # Convert the message to bytes.
        message_bytes = message.encode("utf-8")
    
        # Calculate the hash.
        hash_ = hashlib.sha256(message_bytes).digest()
    
        # Build the digest.
        #
        # Note: Key algorithms will require a varying hash function. For
        # example, EC_SIGN_P384_SHA384 requires SHA-384.
        digest = {"sha256": hash_}
    
        # Optional, but recommended: compute digest's CRC32C.
        # See crc32c() function defined below.
        digest_crc32c = crc32c(hash_)
    
        # Call the API
        sign_response = client.[asymmetric_sign](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_asymmetric_sign)(
            request={
                "name": key_version_name,
                "digest": digest,
                "digest_crc32c": digest_crc32c,
            }
        )
    
        # Optional, but recommended: perform integrity verification on sign_response.
        # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not sign_response.verified_digest_crc32c:
            raise Exception("The request sent to the server was corrupted in-transit.")
        if not sign_response.name == key_version_name:
            raise Exception("The request sent to the server was corrupted in-transit.")
        if not sign_response.signature_crc32c == crc32c(sign_response.signature):
            raise Exception(
                "The response received from the server was corrupted in-transit."
            )
        # End integrity verification
    
        print(f"Signature: {base64.b64encode(sign_response.signature)!r}")
        return sign_response
    
    
    def crc32c(data: bytes) -> int:
        """
        Calculates the CRC32C checksum of the provided data.
        Args:
            data: the bytes over which the checksum should be calculated.
        Returns:
            An int representing the CRC32C checksum of the provided bytes.
        """
        import crcmod  # type: ignore
    
        crc32c_fun = crcmod.predefined.mkPredefinedCrcFun("crc-32c")
        return crc32c_fun(data)
    
    

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
    
    # Require the library.
    require "google/cloud/kms"
    
    # Require digest.
    require "digest"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the key version name.
    key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project:            project_id,
                                                      location:           location_id,
                                                      key_ring:           key_ring_id,
                                                      crypto_key:         key_id,
                                                      crypto_key_version: version_id
    
    # Calculate the hash.
    #
    # Note: Key algorithms will require a varying hash function. For
    # example, EC_SIGN_P384_SHA384 requires SHA-384.
    digest = { sha256: Digest::SHA256.[digest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-AsymmetricSignRequest.html)(message) }
    
    # Call the API.
    sign_response = client.asymmetric_sign name: key_version_name, digest: digest
    puts "Signature: #{Base64.strict_encode64 sign_response.[signature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-AsymmetricSignResponse.html)}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
