---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/import-key/
title: Import and export keys \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:47:54.758199+00:00
---

# Import and export keys  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/import-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Import and export keys Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to import and export Key Management System (KMS) keys. These operations use the `kubectl` command line interface (CLI) and interact with the following Kubernetes resources:

  * [`KeyImport`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/kms-api-overview#keyimport)
  * [`KeyExport`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/kms-api-overview#keyexport)



To view more details on these resources, see the [KMS API overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/kms-api-overview).

Refer to the [Supported keys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/kms#supported-keys) section in the Key management system document to view the full list and details of KMS supported keys.

This document is for audiences within the application operator group when performing key management operations within Google Distributed Cloud (GDC) air-gapped. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before importing or exporting keys, you must have the necessary permissions and prepare your environment.

### Request IAM roles

Contact your Organization IAM Admin to request the following roles in your project:

  * **KMS Key Import Admin** (`kms-keyimport-admin`): create, update, and delete `KeyImport` resources.
  * **KMS Key Export Admin** (`kms-keyexport-admin`): create, update, and delete `KeyExport` resources.



### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Import an exported key

To import an exported key, complete the following steps:

  1. Create a YAML file, and add in the `KeyImport` resource as the value of the `kind` object:
         
         apiVersion: "kms.gdc.goog/v1"
         kind: KeyImport
         metadata:
           name: KEY_IMPORT_NAME
           namespace: PROJECT
         spec:
           context:
             mechanism: MECHANISM
         

Replace the following variables:

     * KEY_IMPORT_NAME: the name of the `KeyImport` resource — for example: `key-import-test`.
     * PROJECT: the name of the project namespace — for example: `kms-test1`.
     * MECHANISM: the key sharing mechanism of the key — for example: `EDCH_P521_AES256` .
  2. Apply the contents of the YAML file to the KMS and create the `KeyImport` resource:
         
         kubectl apply -f FILENAME.yaml
         

Replace FILENAME with the name of the YAML file.

With the public key of an internally generated key pair, the KMS updates the status of the `KeyImport` resource to `AwaitingKeyToImport`. To continue, you need to view the status of the resource and obtain the KMS generated public key.

  3. To view the status of `KeyImport` resource and obtain the KMS generated public key, run the following:
         
         kubectl describe keyimport KEY_IMPORT_NAME --namespace PROJECT
         

Replace the following variables:

     * KEY_IMPORT_NAME: the `KeyImport` resource name — for example, `key-import-test`.
     * PROJECT: the name of the project namespace — for example: `kms-test1`.

After running the command, you see output similar to the following:
    
    ...
    Status:
      Conditions:
        Last Transition Time:  2022-12-14T20:43:50Z
        Message:               waiting for user to provide KeyToImport
        Observed Generation:   1
        Reason:                AwaitingKeyToImport
        Status:                False
        Type:                  Ready
      Imported Key Ref:
        Kind: KeyImport
        Name: key-import-test
      Peer Context:
        Private Key:
        Public Key: PUBLIC_KEY
    Events:           <none>
    

The value PUBLIC_KEY represents the KMS generated public key. Copy the public key, and add it to the `KeyExport` resource in the following step.

  4. Create another YAML file, add in the `KeyExport` resource as the value of the `kind` object, and the following contents:
         
         apiVersion: "kms.gdc.goog/v1"
         kind: KeyExport
         metadata:
           name: KEY_EXPORT_NAME
           namespace: PROJECT
         spec:
           context:
             mechanism: MECHANISM
             publicKey: PUBLIC_KEY
           keyToExport:
             kind: KEY_PRIMITIVE
             name: KEY_NAME
         

Replace the following variables:

     * KEY_EXPORT_NAME: the name of the `KeyExport` resource — for example: `key-export-test`.
     * PROJECT: the name of the project namespace — for example: `kms-test1`.

**Important:** The `KeyExport` custom resource definition (CRD) must reside in the same project namespace of the imported key. If the imported key resides in the project namespace `kms-test1`, the `KeyExport` CRD must also reside in the same project namespace.
     * MECHANISM: the key sharing mechanism of the key — for example: `EDCH_P521_AES256` .

     * PUBLIC_KEY: the public key from `keyImport.Status.PeerContext.PublicKey`.

     * KEY_PRIMITIVE: the CRD of the key—for example, aeadkey and signingkey.

     * KEY_NAME: the name of the key—for example, `key-1`.

  5. Apply the contents of the YAML file to the KMS and create the `KeyExport` resource:
         
         kubectl apply -f FILENAME.yaml
         

Replace FILENAME with the name of the YAML file.

After running the command, the KMS updates the status of the `KeyExport` resource and generates an exported key. To obtain the exported key, view the resource's status.

  6. To view the resource's status, run the following:
         
         kubectl describe keyexport KEY_EXPORT_NAME --namespace PROJECT
         

Replace the following variables:

     * KEY_EXPORT_NAME: the name of the `KeyExport` resource — for example, `key-export-test`.
     * PROJECT: the name of the project namespace—for example: `kms-test1`.

After running the command, you see an output similar to the following:
    
    ...
    Status:
    Conditions:
    Last Transition Time:  2022-12-14T20:45:57Z
    Message:               key successfully exported
    Observed Generation:   1
    Reason:                KeyExportCompleted
    Status:                True
    Type:                  Ready
    Exported Key: EXPORTED_KEY
    

EXPORTED_KEY represents the metadata of the exported key. Copy the contents in EXPORTED_KEY to continue to the following step.

  7. Edit the YAML file that contains the `KeyImport` resource, and add in the contents you copied from the output in `keyexport.status.exportedkey`.
         
         apiVersion: "kms.gdc.goog/v1"
         kind: KeyImport
         metadata:
           name: key-import-test
           namespace: kms-test1
         spec:
           context:
             mechanism: EDCH_P521_AES256
           keyToImport: EXPORTED_KEY
         

  8. After editing the YAML file, apply the contents to the KMS:
         
         kubectl apply -f FILENAME.yaml
         

After running the command, the KMS imports the exported key you provided.

  9. To view details on the imported key, run the following:
         
         kubectl get keyimport KEY_IMPORT_NAME
         

You see output similar to the following:
         
         NAMESPACE   NAME             AGE    READY   REASON              KEY KIND
         kms-test1  KEY_IMPORT_NAME   60s    True    KeyImportCompleted  KEY_PRIMITIVE
         

KEY_PRIMITIVE represents the kind of key you imported, between the AEAD and Signing keys.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
