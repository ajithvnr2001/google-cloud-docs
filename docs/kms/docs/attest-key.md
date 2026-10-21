---
url: https://docs.cloud.google.com/kms/docs/attest-key/
title: Verify attestations \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:36.047228+00:00
---

# Verify attestations  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/attest-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Verify attestations Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to verify attestations for [Cloud HSM keys](https://docs.cloud.google.com/kms/docs/hsm), which are always stored in a hardware security module (HSM). This guide applies to both Multi-tenant Cloud HSM and Single-tenant Cloud HSM keys.

## Overview

In cryptography, an _attestation_ is a machine-readable, programmatically provable statement that a piece of software makes about itself. Attestations are an important component of trusted computing, and may be required for compliance reasons.

To view and verify the attestations, you request a cryptographically-signed _attestation statement_ from the HSM, along with the certificate chains used to sign it. The attestation statement is produced by the HSM hardware, and signed by certificates owned by Google and by the HSM manufacturer.

**Note:** All Cloud HSM devices are manufactured by Marvell (formerly Cavium).

After downloading the attestation statement and the certificate chains, you can check its attributes or verify the validity of the attestation using the certificate chains.

The [attestation script](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/kms/attestations/verify_attestation_chains.py) is an open source Python script developed by Google. You can view the source code for the script to learn more about the attestation format and how verification works, or as a model for a customized solution.

The examples in this document are designed for Linux environments, including the [Cloud Shell](https://docs.cloud.google.com/shell). To follow along on macOS or Windows clients, you may need to make modifications.

## Before you begin

  * If necessary, [create a Cloud HSM key](https://docs.cloud.google.com/kms/docs/hsm#create_a_key) on a key ring in a [region supported by Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).
  * Download and install the [scripts for parsing the attestation's values](https://www.marvell.com/products/security-solutions/liquid-security-hsm-adapters-and-appliances/software-key-attestation.html). from the HSM manufacturer. Download each of these scripts:

    * `verify_pubkey.py`
    * `parse_v1.py`
    * `parse_v2.py`
**Note:** Don't download `verify_attest.py`. Instead, use the verification script provided by Google.

Look over the documentation for using the scripts, provided at the same location.

  * Download and install the [script for verifying attestations](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/kms/attestations/verify_attestation_chains.py) and its prerequisites, and look over the documentation for the script.




## Verify the attestation

The attestation verification process can either be performed automatically through the Google Cloud console, or manually by downloading the attestation bundle and [attestation verification script](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/kms/attestations/verify_attestation_chains.py) and running it locally or in the Cloud Shell.

### Verify attestation using the Google Cloud console

You can verify the attestation through the Google Cloud console, which will open a Cloud Shell and pre-populate it with the code snippets needed to perform the entire attestation verification process.

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring that contains the key you want to attest, then select the key.

  3. Click **More** _more_vert_ for the key version you want to attest, and select **Verify attestation**.

  4. In the **Verify attestation** dialog, click **Open Cloud Shell**. This will open the Cloud Shell and pre-populate it with the code snippet needed to go through the entire verification process.

  5. Inspect the pre-populated code snippet in the Cloud Shell. The snippet downloads the [attestation verification script](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/kms/attestations/verify_attestation_chains.py) and its dependencies, runs the gcloud CLI commands to download the attestation and certificate chains, and then runs the script to verify the attestation.

  6. Run the code snippet to verify the attestation.




### Verify the attestation manually

The attestation, certificate chains, and attestation verification script need to be downloaded before manually verifying the attestation.

  1. Download the attestation and certificate chains.

###  Console 

     1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

     2. Select the key ring that contains the key you want to attest, then select the key.

     3. Click **More** _more_vert_ for the key version you want to attest, and select **Verify attestation**.

     4. In the **Verify attestation** dialog, click **Download Attestation Bundle**. This will download a zip file containing the attestation and certificate chains.

     5. Extract the attestation and certificate chains from the attestation bundle.

###  gcloud 

     1. Click **Activate Cloud Shell** at the top of the console window.

A Cloud Shell session opens inside a new frame at the bottom of the console and displays a command-line prompt. It can take a few seconds for the shell session to be initialized.

     2. At the Cloud Shell command-line prompt, use the `gcloud kms keys versions describe` command to retrieve the attestation for the key that you want to attest. The `--attestation-file` flag specifies the path and filename destination for the retrieved attestation.
            
            gcloud kms keys versions describe KEY_VERSION \
             --key KEY_NAME \
             --location LOCATION \
             --keyring KEY_RING \
             --attestation-file ATTESTATION_FILE_PATH \
            

     3. At the Cloud Shell command-line prompt, use the `gcloud kms keys versions get-certificate-chain` command to retrieve the certificate chains for the key that you want to attest. The `--output-file` flag specifies the path and filename destination for the retrieved certificates.
            
            gcloud kms keys versions get-certificate-chain KEY_VERSION \
             --key KEY_NAME \
             --location LOCATION \
             --keyring KEY_RING \
             --output-file CERTIFICATE_FILE_PATH \
            

  2. Download the [script for verifying attestations](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/kms/attestations/verify_attestation_chains.py) and its prerequisites, and go through the [documentation for the script](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/kms/attestations) to verify the attestation in the attestation file using the certificates in the certificates file.




## Parse the attestation's values

The [HSM manufacturer's documentation](https://www.marvell.com/products/security-solutions/liquid-security-hsm-adapters-and-appliances/software-key-attestation.html) includes full instructions for using their scripts to parse an attestation's values and verify the public key for an asymmetric key pair. The attestation will need to be decompressed with the following command before it can be parsed.

  * Extract the compressed attestation.
        
        gzip -d < compressed_attestation.dat > attestation.dat
        




These links go directly to specific instructions from the HSM manufacturer:

  * [Verify an asymmetric keypair's public key](https://www.marvell.com/products/security-solutions/liquid-security-hsm-adapters-and-appliances/software-key-attestation.html#VerifyPubKey)
  * [Parse the attestation's values](https://www.marvell.com/products/security-solutions/liquid-security-hsm-adapters-and-appliances/software-key-attestation.html#ParseAttestation)



The instructions for parsing the attestation's value include a reference of general fields in the attestation, not specific to HSM keys in Cloud HSM.

The following sections illustrate how to verify information about your keys that is specific to Cloud HSM.

### Verify the key's version ID

You can verify whether the SHA-256 hash of the key version resource ID is present in the attestation. The key's resource name is part of the `0x0102` field or key ID field in the attestation file. The key ID is composed of two concatenated SHA-256 hash digests in hex format. The second one should match the key's resource name.

  1. Get the key version resource ID for the key version. You can use the Google Cloud console to [get the key version resource ID](https://docs.cloud.google.com/kms/docs/object-hierarchy#key_version_resource_id) or you can run the following command:
         
         gcloud kms keys versions list \
            --location LOCATION \
            --keyring KEY_RING \
            --key KEY_NAME
         

  2. At the command line, assign `resource_name` to the key version resource ID that you just retrieved.
         
         RESOURCE_NAME="projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION"
         

  3. Since the parse script dumps all attestation fields in hex format, the key ID would have been formatted into hex format twice. (Once while creating the keyID, the other while parsing the attestation). To verify that the resource name matches with the key ID, convert the resource name to a SHA-256 hex digest, revert one hex conversion of the key ID in the attestation file, and compare the two.
         
         RESOURCE_NAME_HEX="$(echo -n ${RESOURCE_NAME} | openssl dgst -sha256 -hex | awk '{print $2}')"
         

  4. The parse script dumps all attestation fields in hex format, and the key ID is internally hex-encoded a second time. Set the `KEYID_HEX` environment variable to the value of the key ID with one layer of hex-encoding decoded:
         
         KEYID_HEX=$(grep -m 1 0x0102 /path/to/parsed/attestation.dat | awk '{print $2}' | xxd -p -r)
         

  5. Compare the values of `RESOURCE_NAME_HEX` and `KEYID_HEX` as strings:
         
         test ${RESOURCE_NAME_HEX} == ${KEYID_HEX:(-64)} || echo "Values don't match"
         

If the values match, no output is returned and the command exits with code `0`.




### Verify other properties of the key

You can view various key properties, which correspond to fields in the [PKCS #11 standard](https://docs.oasis-open.org/pkcs11/pkcs11-base/v2.40/errata01/csprd01/include/pkcs11-v2.40/pkcs11t.h). Use the following examples as guides to verify other properties of the key.

  * **Whether a key is extractable** is stored in the `0x0102` field of the parsed output. To determine whether a key is extractable, examine the `0x0162` field. A value of `\x01` is `true` and a value of `\x00` is `false`.

Cloud HSM keys are not extractable.
        
        grep '0x0162:' /path/to/parsed/attestation.dat
        

  * **How the key got into the HSM** (whether it was created directly or [imported](https://docs.cloud.google.com/kms/docs/importing-a-key)) is stored in the `0x0163` field. If the key was created locally on the HSM, the field is set to `\x01`. An imported key's field is set to `\x00`.

You can infer a few pieces of information from how the key came to be on the HSM. If the key was created in Cloud HSM, that means the key has never been stored unencrypted outside of an HSM. If the key was imported, then the key was protected during transit by the import job wrapping key and then remained in Cloud HSM afterward.
        
        grep '0x0163:' /path/to/parsed/attestation.dat
        

  * **A key's type** is stored in the `0x0100` field. Key types are documented in the PCKS#11 standard with prefix `CKK_*`. For example, an AES key has a type of `\x1f`.
        
        grep '0x0100:' /path/to/parsed/attestation.dat
        




## Additional information

You verify an attestation to determine whether a key version was created inside an HSM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
