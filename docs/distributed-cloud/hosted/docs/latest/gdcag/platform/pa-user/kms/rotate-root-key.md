---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/kms/rotate-root-key/
title: Rotate a root key \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:37.609410+00:00
---

# Rotate a root key  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/kms/rotate-root-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Rotate a root key Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to rotate a root key. If your root key becomes compromised, or if you choose to periodically rotate root keys to enhance security, you can rotate your keys to a new root key using the [`RotationJob`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/kms/kms-api-overview#rotationjob) resource.

Rotating a root key creates a new root key, which becomes the primary key and wraps all non-root keys. You can't delete a root key; rotation is the only way to replace it. See [Root key types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/kms/kms#root_key_types) for more information about root keys.

Refer to the [KMS API overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/kms-api-overview) for details on the KMS API and the [Key Management Service KRM API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/kms-krm-api) to view the full API definition.

## Before you begin

Before rotating a root key, you must have the necessary permissions and prepare your environment.

### Request IAM roles

To rotate keys, contact your Organization IAM Admin to request the **KMS Rotation Job Admin** (`kms-rotationjob-admin`) role.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Install the kubectl CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl).

  * [Generate a kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to configure `kubectl` access.




## Rotate a root key

To rotate a root key, you first need to identify the resource name of the root key in use. You can find this information by examining any `AEADKey` resource within your project, as all these keys are protected by the same root key.

Create a new root key and rotate your keys:

  1. List the `AEADKey` resources in your project:
         
         kubectl get AEADKey -n PROJECT
         

Replace `PROJECT` with the name of your project namespace.

From the output, note the name of any `AEADKey`.

  2. Get the `ROOT_KEY_RESOURCE_NAME` from the `AEADKey`. The following command extracts and reformats the root key identifier needed for the `RotationJob` resource:
         
         kubectl describe aeadkey KEY_NAME -n PROJECT | grep "Root Key ID:" | awk '{print $4}' | awk -F/ '{print "namespaces/" $1 "/secrets/" $2}'
         

Replace the following:

     * `KEY_NAME`: the name of any `AEADKey` in your project
     * `PROJECT`: the name of your project namespace

The output might look similar to the following:
    
    namespaces/kms-system/secrets/kms-key-local-root
    

  3. Create a YAML file, and add in the `RotationJob` resource and the following contents:
         
         apiVersion: "kms.gdc.goog/v1"
         kind: RotationJob
         metadata:
           name: ROTATION_NAME
         spec:
           rootKeyResourceName: ROOT_KEY_RESOURCE_NAME
         

Replace the following:

     * `ROTATION_NAME`: a name for the rotation job — for example: `rotate-job1`.
     * `ROOT_KEY_RESOURCE_NAME`: the output you obtained in the preceding step
  4. Apply the contents of the YAML file to the KMS:
         
         kubectl apply -f FILENAME.yaml
         

Replace FILENAME with the name of the YAML file.

After running the command, the KMS creates a new root key and rotates every key with the new root key.

  5. To verify the root key rotation is complete, run the following:
         
         kubectl get rotationjobs ROTATION_NAME
         

Replace ROTATION_NAME with the name of the rotation job.

After running the command, you see the status of the rotation job as `Completed` if successful.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
