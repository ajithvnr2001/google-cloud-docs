---
url: https://docs.cloud.google.com/kms/docs/encapsulate-decapsulate/
title: Encapsulate and decapsulate using KEMs \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:43.781328+00:00
---

# Encapsulate and decapsulate using KEMs  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/encapsulate-decapsulate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Encapsulate and decapsulate using KEMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes using key encapsulation mechanisms (KEMs) with Cloud KMS keys to establish shared secrets.

Encapsulation uses the public key of the KEM key pair, and decapsulation uses the private key of the key pair. Cloud KMS lets you retrieve the public key, which you can then use with standard libraries to encapsulate your shared secret. To decapsulate the shared secret, use Cloud KMS decapsulation methods. You can't use the private key material outside of Cloud KMS.

## Before you begin

  * This document provides examples that run at the command line. To simplify using the examples, use [Cloud Shell](https://docs.cloud.google.com/shell). The encryption example uses [OpenSSL](https://www.openssl.org/), which is pre-installed on Cloud Shell. Otherwise, install OpenSSL on your machine.
  * [Create a KEM key](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys) with [key purpose](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes) of `KEY_ENCAPSULATION`. To see which algorithms are supported for key purpose `KEY_ENCAPSULATION`, see [key encapsulation algorithms](https://docs.cloud.google.com/kms/docs/algorithms#key_encapsulation_algorithms).



## Grant permissions on the key

  * Grant the [`roles/cloudkms.publicKeyViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.publicKeyViewer) role on the key to each user or principal that must retrieve the public key to encapsulate the secret.
  * Grant the ['roles/cloudkms.decapsulator'](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.decapsulator) role on the key to each user or principal that must decapsulate secrets with this key.



For more information about permissions and roles in Cloud KMS, see [Permissions and Roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

## Encapsulation

To encapsulate using a KEM key, retrieve the public key and use the public key to encapsulate.

### gcloud

This sample requires [OpenSSL](https://www.openssl.org) to be installed on your local system.

### Download the public key
    
    
    gcloud kms keys versions get-public-key KEY_VERSION \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION  \
        --output-file PUBLIC_KEY_FILE \
        --public-key-format PUBLIC_KEY_FORMAT
    

Replace the following:

  * `KEY_VERSION`: The version number of the key that you want to use for encapsulation—for example, `2`.
  * `KEY_NAME`: The name of the key that you want to use for encapsulation.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `PUBLIC_KEY_FILE`: The local file path where the public key will be saved.
  * `PUBLIC_KEY_FORMAT`: The target format for the public key—for example, `nist-pqc`. The default format is `pem`.



### Reformat the public key

The encapsulate command requires the public key to be in PEM format. If you have downloaded the public key in another format, like `nist-pqc`, then you must convert the key to PEM format. If your public key is already in the PEM format, continue from Encapsulate.

Use the following command to convert the public key for a `ML-KEM-768` key:
    
    
    { echo -n "MIIEsjALBglghkgBZQMEBAIDggShAA==" | base64 -d ; cat PUBLIC_KEY_FILE; } | \
    openssl pkey -inform DER -pubin -pubout -out PEM_PUBLIC_KEY_FILE
    

Use the following command to convert the public key for a `ML-KEM-1024` key:
    
    
    { echo -n "MIIGMjALBglghkgBZQMEBAMDggYhAA==" | base64 -d ; cat PUBLIC_KEY_FILE; } | \
    openssl pkey -inform DER -pubin -pubout -out PEM_PUBLIC_KEY_FILE
    

Replace the following:

  * `PUBLIC_KEY_FILE`: The path to the downloaded public key file in raw format.
  * `PEM_PUBLIC_KEY_FILE`: The path and file name to save the public key in PEM format.



### Encapsulate

To create a shared secret and ciphertext, you can use the following command:
    
    
    openssl pkeyutl \
        -encap \
        -pubin \
        -inkey PEM_PUBLIC_KEY_FILE \
        -out CIPHERTEXT_FILE \
        -secret SHARED_SECRET_FILE
    

Replace the following:

  * `PEM_PUBLIC_KEY_FILE`: The path to the downloaded public key file in PEM format.
  * `CIPHERTEXT_FILE`: The path where you want to save the resulting ciphertext.
  * `SHARED_SECRET_FILE`: The path where you want to save the resulting shared secret.



### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"crypto/mlkem"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // encapsulateMLKEM demonstrates how to encapsulate a shared secret using an ML-KEM-768 public key
    // from Cloud KMS.
    func encapsulateMLKEM(w io.Writer, keyVersionName string) error {
    	// keyVersionName := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// crc32c calculates the CRC32C checksum of the given data.
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    	}
    
    	// Build the request to get the public key in NIST PQC format.
    	req := &kmspb.GetPublicKeyRequest{
    		Name:            keyVersionName,
    		PublicKeyFormat: kmspb.[PublicKey_NIST_PQC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_PublicKey_PUBLIC_KEY_FORMAT_UNSPECIFIED_PublicKey_PEM_PublicKey_DER_PublicKey_NIST_PQC_PublicKey_XWING_RAW_BYTES),
    	}
    
    	// Call the API to get the public key.
    	response, err := client.GetPublicKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get public key: %w", err)
    	}
    
    	// Optional, but recommended: perform integrity verification on the response.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	if response.GetName() != req.GetName() {
    		return fmt.Errorf("GetPublicKey: request corrupted in-transit")
    	}
    	if response.GetPublicKeyFormat() != req.GetPublicKeyFormat() {
    		return fmt.Errorf("GetPublicKey: request corrupted in-transit")
    	}
    	if int64(crc32c(response.GetPublicKey().GetData())) != response.GetPublicKey().GetCrc32CChecksum().GetValue() {
    		return fmt.Errorf("GetPublicKey: response corrupted in-transit")
    	}
    
    	// Use the public key with crypto/mlkem to encapsulate a shared secret.
    	ek, err := mlkem.NewEncapsulationKey768(response.GetPublicKey().GetData())
    	if err != nil {
    		return fmt.Errorf("NewEncapsulationKey768: %w", err)
    	}
    	sharedSecret, ciphertext := ek.Encapsulate()
    
    	fmt.Fprintf(w, "Encapsulated ciphertext: %x\n", ciphertext)
    	fmt.Fprintf(w, "Shared secret: %x\n", sharedSecret)
    	return nil
    }
    

## Decapsulation

Use Cloud KMS to decapsulate a ciphertext.

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms decapsulate \
        --version KEY_VERSION \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION  \
        --ciphertext-file CIPHERTEXT_FILE \
        --shared-secret-file SHARED_SECRET_FILE
    

Replace the following:

  * `KEY_VERSION`: the key version to use for decapsulation—for example, `3`.
  * `KEY_NAME`: the name of the key to use for decapsulation.
  * `KEY_RING`: the name of the key ring where the key is located.
  * `LOCATION`: the Cloud KMS location for the key ring.
  * `CIPHERTEXT_FILE`: the local file path for the input ciphertext.
  * `SHARED_SECRET_FILE`: the local file path for saving the output shared secret.



### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"google.golang.org/protobuf/types/known/wrapperspb"
    )
    
    // decapsulate decapsulates the given ciphertext using a saved private key of purpose
    // KEY_ENCAPSULATION stored in KMS.
    func decapsulate(w io.Writer, keyVersionName string, ciphertext []byte) error {
    	// keyVersionName := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1"
    	// ciphertext := []byte("...")
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// crc32c calculates the CRC32C checksum of the given data.
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    	}
    
    	// Optional but recommended: Compute ciphertext's CRC32C.
    	ciphertextCRC32C := crc32c(ciphertext)
    
    	// Build the request.
    	req := &kmspb.DecapsulateRequest{
    		Name:             keyVersionName,
    		Ciphertext:       ciphertext,
    		CiphertextCrc32C: wrapperspb.Int64(int64(ciphertextCRC32C)),
    	}
    
    	// Call the API.
    	result, err := client.Decapsulate(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to decapsulate: %w", err)
    	}
    
    	// Optional, but recommended: perform integrity verification on the response.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	if !result.GetVerifiedCiphertextCrc32C() {
    		return fmt.Errorf("Decapsulate: request corrupted in-transit")
    	}
    	if result.GetName() != req.GetName() {
    		return fmt.Errorf("Decapsulate: request corrupted in-transit")
    	}
    	if int64(crc32c(result.GetSharedSecret())) != result.GetSharedSecretCrc32C() {
    		return fmt.Errorf("Decapsulate: response corrupted in-transit")
    	}
    
    	fmt.Fprintf(w, "Decapsulated plaintext: %x", result.GetSharedSecret())
    	return nil
    }
    

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

Use the [`CryptoKeyVersions.decapsulate`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/decapsulate) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION:decapsulate" \
      --request "POST" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data '{"ciphertext": "CIPHERTEXT"}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key to use for encryption.
  * `KEY_VERSION`: the ID of the key version to use for encryption
  * `CIPHERTEXT`: the base64-encoded ciphertext that you want to decapsulate. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
