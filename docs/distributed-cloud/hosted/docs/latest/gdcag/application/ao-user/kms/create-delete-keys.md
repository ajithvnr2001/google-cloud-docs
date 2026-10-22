---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys/
title: Create and delete keys \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:58.700684+00:00
---

# Create and delete keys  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create and delete keys Stay organized with collections  Save and categorize content based on your preferences. 

The Key Management System (KMS) supports different types of keys for cryptographic operations such as encryption, decryption, signing, and verification. See [Supported keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/kms#supported_keys) for more information on the available key types and algorithms.

This page is for audiences within the application operator group, such as DevOps teams, when performing key management operations within Google Distributed Cloud (GDC) air-gapped. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create and manage keys, request the necessary permissions and prepare your environment.

### Request IAM roles

Contact your IAM Org Admin to grant you the following roles in your project namespace:

  * **KMS Creator** (`kms-creator`): view and create `AEADKey` and `SigningKey` resources within a project.
  * **KMS Admin** (`kms-admin`): view, create, and delete keys within a project.



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
            

**Note:** The `gdcloud auth login` command generates an authentication token that expires in approximately 15 minutes. If your token expires, re-run `gdcloud auth login` to re-establish the session. After re-running, wait about 90 seconds for role propagation before `kubectl` commands succeed.
  3. [Get a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) for the Management API server using the gdcloud CLI.




## Create a key

You can create keys for different cryptographic purposes.

### Create an AEAD key

To perform authenticated encryption with associated data (AEAD), create an `AEADKey` resource in your project namespace:
    
    
    kubectl --kubeconfig KUBECONFIG_PATH \
    apply -f - << EOF
    apiVersion: "kms.gdc.goog/v1"
    kind: AEADKey
    metadata:
      name: KEY_NAME
      namespace: PROJECT
    spec:
      algorithm: AES_256_GCM
    EOF
    

Replace the following:

  * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server
  * `KEY_NAME`: a name for the AEAD key you want to create—for example: `key-1`
  * `PROJECT`: the name of the project—for example: `kms-test1`



### Create a signing key

To sign and verify data, create a `SigningKey` resource in your project namespace:
    
    
    kubectl --kubeconfig KUBECONFIG_PATH \
    apply -f - << EOF
    apiVersion: "kms.gdc.goog/v1"
    kind: SigningKey
    metadata:
      name: KEY_NAME
      namespace: PROJECT
    spec:
      algorithm: EC_SIGN_P384_SHA384
    EOF
    

Replace the following:

  * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server
  * `KEY_NAME`: a name for the signing key you want to create—for example: `key-1`
  * `PROJECT`: the name of the project—for example: `kms-test1`



## Verify key creation

After creating a key, verify that the operation was successful and the key resource is ready.

### Verify AEAD key creation

Check the status of an AEAD key:
    
    
    kubectl --kubeconfig KUBECONFIG_PATH \
      get aeadkey KEY_NAME \
      --namespace=PROJECT -o yaml
    

Replace the following:

  * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server
  * `KEY_NAME`: the name of AEAD key to verify—for example: `key-1`
  * `PROJECT`: the name of the project—for example: `kms-test1`



If the key creation was successful, check the output for a `Ready` condition with a status of `True`.

### Verify signing key creation

Check the status of a signing key:
    
    
    kubectl --kubeconfig KUBECONFIG_PATH \
      get signingkey KEY_NAME \
      --namespace=PROJECT -o yaml
    

Replace the following:

  * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server
  * `KEY_NAME`: the name of the signing key to verify—for example: `key-1`
  * `PROJECT`: the name of the project—for example: `kms-test1`



If the key creation was successful, check the output for a `Ready` condition with a status of `True`.

## Delete a key

To delete a key resource, specify the key type and name.

  1. Delete the key in the project namespace:
         
         kubectl --kubeconfig KUBECONFIG_PATH \
           delete KEY_PRIMITIVE KEY_NAME \
           --namespace=PROJECT
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to the kubeconfig file for the Management API server
     * `KEY_PRIMITIVE`: the type of key resource that you want to delete such as `aeadkey` for the AEAD key or `signingkey` for the signing key
     * `KEY_NAME`: the name of the key you want to delete—for example: `key-1`.
     * `PROJECT`: the name of the project—for example: `kms-test1`.
  2. Verify the key deletion by attempting to retrieve the key:
         
         kubectl --kubeconfig KUBECONFIG_PATH \
           get KEY_PRIMITIVE  KEY_NAME \
           --namespace=PROJECT
         

If the key was successfully deleted, the command won't return the key object.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
