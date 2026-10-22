---
url: https://docs.cloud.google.com/kms/docs/wrapping-a-key/
title: Wrapping a key using OpenSSL on Linux \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:52.408253+00:00
---

# Wrapping a key using OpenSSL on Linux  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/wrapping-a-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Wrapping a key using OpenSSL on Linux Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows how to manually wrap a key before [importing the key](https://docs.cloud.google.com/kms/docs/importing-a-key) into Cloud KMS. You only need to follow the instructions in this topic if you do not want to use the Google Cloud CLI to automatically wrap the key before importing it. For an overview of the differences, refer to [How key import works](https://docs.cloud.google.com/kms/docs/key-import#key_import_flow).

You can complete the steps in this topic in 5 to 10 minutes, not including the Before you begin steps.

## Before you begin

Before you can wrap a key, you must complete the following prerequisites.

  1. [Create a target key ring and key, and create an import job](https://docs.cloud.google.com/kms/docs/importing-a-key).
  2. [Verify that your key is available locally and formatted correctly](https://docs.cloud.google.com/kms/docs/formatting-keys-for-import) for import into Cloud KMS.
  3. [Patch and recompile OpenSSL](https://docs.cloud.google.com/kms/docs/configuring-openssl-for-manual-key-wrapping)



## Retrieve the wrapping key

This section shows how to retrieve the wrapping key from the import job you created in Before you begin. Using the Google Cloud console is recommended.

###  Console 

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains your import job.

  3. Click the **Import Jobs** tab at the top of the page.

  4. Click **More** _more_vert_ , then **Download wrapping key** in the pop-up menu.




###  gcloud 

To verify that the import job is active, run the `gcloud kms import-jobs describe` command:
    
    
    gcloud kms import-jobs describe IMPORT_JOB \
      --location LOCATION \
      --keyring KEY_RING \
      --format="value(state)"
    
    
    
    state: ACTIVE

Run the following command to save the public key from the import job to `${HOME}/wrapping-key.pem`
    
    
    gcloud kms import-jobs describe \
      --location=LOCATION \
      --keyring=KEY_RING \
      --format="value(publicKey.pem)" \
      IMPORT_JOB > ${HOME}/wrapping-key.pem
    

**Note:** You only need to download the public key once and can use it until the import job expires.

###  REST 

  1. Call the [`ImportJob.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get) method.

  2. Retrieve the public key via the [`publicKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#ImportJob.FIELDS.public_key) field of the `ImportJob.get` response. This value is of type [`WrappingPublicKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#WrappingPublicKey). The [`pem`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#WrappingPublicKey.FIELDS.pem) field of the `WrappingPublicKey` type is the public key encoded in Privacy Enhanced Mail (PEM) format.




**Note:** Remember to verify that your key's [algorithm and length](https://docs.cloud.google.com/kms/docs/algorithms) are supported. Allowable algorithms for a key depend upon whether the key is used for symmetric encryption, asymmetric encryption or asymmetric signing, as well as whether the key is stored in software or a Hardware Security Module (HSM).

For more information about the PEM-encoded format, see [RFC 7468](https://tools.ietf.org/html/rfc7468), especially the [General Considerations](https://tools.ietf.org/html/rfc7468#section-2) and [Textual Encoding of Subject Public Key Info](https://tools.ietf.org/html/rfc7468#section-2) sections.

## Set up environment variables

The OpenSSL commands require several file paths as input values. Define environment variables for the file paths to make it easier to run the commands. Make sure you have access to write to the directories you define below.

**Note:** If desired, you can save all of these commands to a shell script and run the script to set the variables all at once. You may need to adjust some of the values for each key you want to wrap.

  1. Set the `PUB_WRAPPING_KEY` variable to the full path to the wrapping key you downloaded from the import job. The wrapping key ends in `.pem`.
         
         PUB_WRAPPING_KEY="WRAPPING_KEY_PATH"
         

  2. Set the `TARGET_KEY` variable to the full path to the unwrapped (target) key.
         
         TARGET_KEY="TARGET_KEY_PATH"
         

Replace `TARGET_KEY_PATH` with the path to the `.bin` file for symmetric keys or the path to the `.der` file for asymmetric keys.

  3. If wrapping with RSA-AES, set the `TEMP_AES_KEY` variable to the full path to the temporary AES key.
         
         TEMP_AES_KEY=TEMP_AES_KEY_PATH
         

  4. Set the `WRAPPED_KEY` variable to the full path where you want to save the wrapped target key that is ready for import.
         
         WRAPPED_KEY=WRAPPED_KEY_PATH
         

  5. Verify that all the environment variables are set correctly using the following commands:
         
         echo "PUB_WRAPPING_KEY: " ${PUB_WRAPPING_KEY}; \
         echo "TARGET_KEY: " ${TARGET_KEY}; \
         echo "TEMP_AES_KEY: " ${TEMP_AES_KEY}; \
         echo "WRAPPED_KEY: " ${WRAPPED_KEY}
         




When the variables are set correctly, you are ready to wrap the key. There are two approaches as described below: with RSA only or with RSA-AES.

## Wrap the key

### Wrap the key with RSA

In this approach, the target key is wrapped in an RSA block. The target key size is therefore limited. For example, you can't use this method to wrap another RSA key. The supported import methods are `rsa-oaep-3072-sha256` and `rsa-oaep-4096-sha256`.

  * Wrap the target key with the wrapping public key using the `CKM_RSA_PKCS_OAEP` algorithm:
        
        openssl pkeyutl \
          -encrypt \
          -pubin \
          -inkey ${PUB_WRAPPING_KEY} \
          -in ${TARGET_KEY} \
          -out ${WRAPPED_KEY} \
          -pkeyopt rsa_padding_mode:oaep \
          -pkeyopt rsa_oaep_md:sha256 \
          -pkeyopt rsa_mgf1_md:sha256
        




### Wrap the key with RSA-AES

In this approach, the target key is wrapped with a temporary AES key. The temporary AES key is then wrapped by the RSA key. These two wrapped keys are concatenated and imported. Because the target key is wrapped using AES rather than RSA, this approach can be used to wrap large keys. The supported import methods are `rsa-oaep-3072-sha1-aes-256`, `rsa-oaep-4096-sha1-aes-256`, `rsa-oaep-3072-sha256-aes-256` and `rsa-oaep-4096-sha256-aes-256`.

  1. Generate a temporary random AES key that is 32 bytes long, and save it to the location identified by `${TEMP_AES_KEY}`:
         
         openssl rand -out "${TEMP_AES_KEY}" 32
         

  2. Wrap the temporary AES key with the wrapping public key using the `CKM_RSA_PKCS_OAEP` algorithm. If the import method is either `rsa-oaep-3072-sha1-aes-256` or `rsa-oaep-4096-sha1-aes-256`, use `sha1` for `rsa_oaep_md` and `rsa_mgf1_md`. Use `sha256` for `rsa-oaep-3072-sha256-aes-256` and `rsa-oaep-4096-sha256-aes-256`.
         
         openssl pkeyutl \
           -encrypt \
           -pubin \
           -inkey ${PUB_WRAPPING_KEY} \
           -in ${TEMP_AES_KEY} \
           -out ${WRAPPED_KEY} \
           -pkeyopt rsa_padding_mode:oaep \
           -pkeyopt rsa_oaep_md:{sha1|sha256} \
           -pkeyopt rsa_mgf1_md:{sha1|sha256}
         

  3. Set the `OpenSSL_V110` variable to the path of your `openssl.sh` script. If you followed the instructions for [patching and recompiling OpenSSL](https://docs.cloud.google.com/kms/docs/configuring-openssl-for-manual-key-wrapping) exactly, you can use this command without modifying the value of the variable.
         
         OPENSSL_V110="${HOME}/local/bin/openssl.sh"
         

  4. Wrap the target key with the temporary AES key using the `CKM_AES_KEY_WRAP_PAD` algorithm, and append it to the `WRAPPED_KEY`.
         
         "${OPENSSL_V110}" enc \
           -id-aes256-wrap-pad \
           -iv A65959A6 \
           -K $( hexdump -v -e '/1 "%02x"' < "${TEMP_AES_KEY}" ) \
           -in "${TARGET_KEY}" >> "${WRAPPED_KEY}"
         

The `-iv A65959A6` flag sets A65959A6 as the Alternate Initial Value. This is required by the [RFC 5649](https://tools.ietf.org/html/rfc5649) specification.




## What's next

  * The wrapped key saved at `WRAPPED_KEY` is now ready to be imported. To import the key, follow the instructions in [Importing a manually-wrapped key](https://docs.cloud.google.com/kms/docs/importing-a-key#importing_a_manually-wrapped_key).



[ Previous arrow_back  Configure OpenSSL for manual key wrapping  ](https://docs.cloud.google.com/kms/docs/configuring-openssl-for-manual-key-wrapping)

[ Next Quantum-safe key import  arrow_forward  ](https://docs.cloud.google.com/kms/docs/quantum-safe-key-import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
