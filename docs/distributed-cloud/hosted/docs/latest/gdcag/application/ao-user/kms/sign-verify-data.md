---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/sign-verify-data/
title: Sign and verify data \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:20.196650+00:00
---

# Sign and verify data  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/sign-verify-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Sign and verify data Stay organized with collections  Save and categorize content based on your preferences. 

Digital signatures are used to ensure data integrity and authenticity. This document explains how to use the gdcloud CLI to sign data and verify signatures using asymmetric keys managed by the Key Management System (KMS).

This page is for audiences within the application operator group, such as DevOps teams, when performing key management operations within Google Distributed Cloud (GDC) air-gapped. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To sign and verify data using keys, request the necessary permissions, prepare your environment, and create a signing key if you don't already have one.

### Request IAM roles

Contact your IAM Org Admin to grant you the following role in your project namespace:

  * **KMS Developer** (`kms-developer`): view keys and perform cryptographic operations such as encrypting, decrypting, signing, and verifying data within a project.



### Prepare your environment

  1. Install and initialize the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview), if you haven't already done so.

  2. Authenticate to GDC using the gdcloud CLI. This process requires the Certificate Authority (CA) certificate for your organization's console:

     1. Download the CA certificate:
            
            echo -n | openssl s_client -showcerts -connect CONSOLE_URL:443 | sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' > CA_CERT_PATH
            

Replace the following:

        * `CONSOLE_URL`: your organization's console URL (such as `console.org-1.zone1.google.gdch.test`)
        * `CA_CERT_PATH`: the full path where you want to save the CA certificate file (such as `/tmp/my-org-ca.crt`)
     2. Sign in using the downloaded CA certificate:
            
            gdcloud auth login --login-config-cert=CA_CERT_PATH
            

**Note:** The `gdcloud auth login` command generates an authentication token that expires in approximately 15 minutes. If your token expires, re-run `gdcloud auth login` to re-establish the session. Permissions might take a short time to become fully effective after re-authenticating.



### Make sure a signing key exists

To sign and verify data, you must use a signing key. Key creation and verification require separate IAM permissions, as detailed on the linked pages.

  * If you need to create a signing key, follow the instructions in [Create a signing key](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#create-signingkey).
  * To verify a signing key exists, follow the instructions in [Verify signing key creation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#verify-signingkey).



## Sign data

To sign data, use the `gdcloud kms keys asymmetric-sign` command. This command creates a digital signature of an input file using a signing key, and saves the base64 encoded signature:
    
    
      gdcloud kms keys asymmetric-sign \
      namespaces/NAMESPACE/signingKeys/KEY_NAME \
      --input-file=INPUT_PATH \
      --signature-file=SIGNATURE_FILE
    

Replace the following:

  * NAMESPACE: the project namespace—for example: `kms-test1`
  * KEY_NAME: the name of the key used to sign—for example: `key-1`
  * INPUT_PATH: the path of the input file you want signed
  * SIGNATURE_FILE: the path of the output file to save the base64 encoded signature



After running the command, you see an output file you specified in the `--signature-file` flag that contains the base64 encoded signature.

## Verify data

After signing your data, verify the base64 digital signature using the `gdcloud kms keys asymmetric-verify` command. This command verifies whether or not the base64 encoded digital signature you receive after running the `gdcloud kms keys asymmetric-sign` command is valid:
    
    
    gdcloud kms keys asymmetric-verify \
    namespaces/NAMESPACE/signingKeys/KEY_NAME \
      --input-file=INPUT_PATH \
      --signature-file=SIGNATURE_FILE
    

Replace the following:

  * NAMESPACE: the project namespace—for example: `kms-test1`
  * KEY_NAME: the name of the key used to sign —for example: `key-1`
  * INPUT_PATH: the path of the original input file that was signed
  * SIGNATURE_FILE: the path of the file containing the base64 encoded signature to verify



After running the command, you see the output `Verification OK` if successful. If not successful, you see the failure output `Verification Failure`.

**Note:** The failure output `Verification Failure` might result if the paths of the signature and input files are not correct, and if the signature file is empty.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
