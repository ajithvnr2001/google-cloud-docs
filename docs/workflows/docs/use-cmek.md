---
url: https://docs.cloud.google.com/workflows/docs/use-cmek/
title: Use customer-managed encryption keys \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:02.859230+00:00
---

# Use customer-managed encryption keys  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Workflows encrypts customer content at rest. Workflows handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Workflows. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Workflows resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

You can protect your workflow and associated data at rest using an encryption key that only you can access, and that you can control and manage using Cloud KMS.

## What is protected with CMEK

When deploying a workflow, you can specify a Cloud KMS key. This key is used to encrypt the workflow and its executions:

  * A **workflow** requires a source file that contains a valid workflow definition. This source file is encrypted using the key.

  * A **workflow execution** runs the current workflow definition (a specific _workflow revision_). Using the key associated with the workflow revision at the time of its deployment, the compiled workflow, as well as any stored execution input, output, and runtime data is encrypted. This includes execution arguments, results, errors, and exceptions; delivered [Eventarc events](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc); and callback and HTTP requests and responses.




## Before you begin

Before using CMEK in Workflows, complete the following steps:

  1. Enable the APIs.

###  Console 

     1. Enable the Cloud KMS and Workflows APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com,workflows.googleapis.com)

###  gcloud 

     1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

     2. Update `gcloud` components. 
            
            gcloud components update

     3. Enable the Cloud KMS and Workflows APIs for the project that will store your encryption keys. 
            
            gcloud services enable cloudkms.googleapis.com workflows.googleapis.com

  2. Cloud KMS produces Cloud Audit Logs when keys are enabled, disabled, or used by Workflows resources to encrypt and decrypt data. Make sure that [logging is enabled ](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project, and that you have decided which logging-specific permissions and roles apply to your use case. For more information, see [Cloud KMS audit logging information](https://docs.cloud.google.com/kms/docs/audit-logging).




## Create a Cloud KMS key ring and key

You can create a new key ring or use an existing one. Within the key ring, you can add a new key or use an existing key.

**Note:** The Cloud KMS key ring and the protected workflow must be in the same region. For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations) and [Workflows locations](https://docs.cloud.google.com/workflows/docs/locations). The Cloud KMS key ring and the protected workflow can be in different projects but as a best practice, consider [setting up Cloud KMS in a separate project](https://docs.cloud.google.com/kms/docs/separation-of-duties#using_separate_project).

  1. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring).

  2. [Create a key for a specified key ring](https://docs.cloud.google.com/kms/docs/create-key).




## Retrieve the resource ID for a Cloud KMS key

The resource ID for a Cloud KMS key is required when you enable CMEK for a workflow. In this document, see Enable CMEK for a workflow.

### Console

  1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms/keyrings)

  2. Click the key ring that contains the key.

  3. For the key whose resource ID you are retrieving, click _more_vert_ **More**.

  4. Click **Copy resource name**.

The resource ID for the key is copied to your clipboard. Its format is similar to the following:
         
         projects/PROJECT_NAME/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
         

  5. A key contains zero or more key versions. The resource ID for a key version is the key ID, plus a slash (`/`), plus the version ID. To list all versions for a key:

     1. Click the key's name.
     2. For a specific version, click more_vert **More**.
     3. Click **Copy resource name**.



### gcloud

  1. List all keys on a given key ring:
         
         gcloud kms keys list --keyring RING_NAME --location LOCATION
         

Replace the following:

     * `RING_NAME`: the name of the key ring
     * `LOCATION`: the region of the key ring

The output includes the resource ID for each key. For example:
    
    NAME: projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
    

  2. A key has zero or more key versions. The resource ID for a key version is the key ID, plus a slash (`/`), plus the version ID. List all versions for a key:
         
         gcloud kms keys versions list --location LOCATION --keyring RING_NAME --key KEY_NAME
         

The output includes the resource ID for each key version. For example:
         
         NAME: projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME/2
         




## Grant the Workflows service agent access to the key

You must grant the [Workflows service agent](https://docs.cloud.google.com/iam/docs/service-agents) the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) Identity and Access Management (IAM) role so that it can access the Cloud KMS key:

###  Console 

When you enable CMEK for a workflow through the console, you are prompted to grant the **Cloud KMS CryptoKey Encrypter/Decrypter** role to the service account. For more information, in this document, see Enable CMEK for a workflow.

###  gcloud 
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --keyring RING_NAME \
        --location LOCATION \
        --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-workflows.iam.gserviceaccount.com \
        --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace the following:

  * `KEY_NAME`: the name of the key. For example, `my-key`.
  * `RING_NAME`: the name of the key ring. For example, `my-keyring`.
  * `LOCATION`: the location of the key. For example, `us-central1`.
  * `PROJECT_NUMBER`: your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
        
        export PROJECT=$(gcloud info --format='value(config.project)')
        gcloud projects describe ${PROJECT} --format="value(projectNumber)"




As long as the service agent has the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role, a workflow in your project can encrypt and decrypt its data using the CMEK key. If you revoke this role, or if you disable or destroy the CMEK key, that data can't be accessed. In this document, see Disable Cloud KMS.

## Enable CMEK for a workflow

When [creating a workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow) or updating it afterwards, you can specify the Cloud KMS key that the workflow should use for data encryption.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page. 

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to update.

The **Workflows details** page appears.

  3. Click edit **Edit**.

  4. Select **Cloud KMS key**.

  5. Select a **Key type**.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the Autokey option is disabled, it isn't yet integrated with the current resource type.

  6. In the **Select a Cloud KMS key** list, select or filter for a Cloud KMS key.

  7. Optional: To manually enter the resource name of the key, in the **Select a customer-managed key** list, click **Enter key manually** , and enter the key resource name in the specified format.

  8. If prompted, grant the `cloudkms.cyptoKeyEncrypterDecrypter` role to the Workflows service account with the `workflows.serviceAgent` role.

  9. Click **Next**.

  10. To save your changes and deploy the updated workflow, click **Deploy**.




###  gcloud 
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --source=SOURCE_FILE \
        --kms-key=KEY \
        --location LOCATION \
        --service-account=SERVICE_ACCOUNT

Replace the following:

  * `WORKFLOW_NAME`: the name of your workflow
  * `SOURCE_FILE`: your workflow source file with a `yaml` file extension for a YAML file, or with a `json` file extension for a JSON file; for example, `myWorkflow.yaml`.
  * `KEY`: the key's resource ID in the format `projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`. You can [retrieve the key ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version).

**Important:** Even if you omit the `--kms-key` flag for subsequent deployments of the workflow, any previously deployed Cloud KMS key is applied until the key is disabled. In this document, see Disable CMEK for a workflow.
  * `LOCATION`: the location of the workflow

  * `SERVICE_ACCOUNT`: the service account your workflow will use to access other Google Cloud services; for example, `SERVICE_ACCOUNT_NAME@PROJECT_NAME.iam.gserviceaccount.com`. We strongly recommend using a service account with the least privileges necessary to access the required resources. If left blank, the default service account is used. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).




Note the following:

  * Workflow revisions and executions are encrypted with the key specified at the time of deployment; resources previously encrypted with an earlier key remain encrypted with that earlier key. If a workflow is subsequently edited and a new key is specified, that revision of the workflow is encrypted with the new key, and any subsequent executions will use the new key.
  * Previously non-CMEK encrypted workflow revisions and executions remain not encrypted.
  * If you disable CMEK for a workflow revision, any subsequent executions are created without CMEK encryption. In this document, see Disable CMEK for a workflow. Existing workflow revisions and executions remain encrypted with the keys with which they were previously encrypted.



## Verify the Cloud KMS integration

You can verify the CMEK integration by displaying the metadata for a workflow.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page. 

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to verify.

The **Workflows details** page appears.

  3. Click the **Details** tab.

The **Encryption** value displays the resource ID of the Cloud KMS key used to secure the workflow and its execution.




###  gcloud 
    
    
    gcloud workflows describe WORKFLOW_NAME \
        --location=LOCATION

The output should be similar to the following:
    
    
    createTime: '2022-08-10T19:57:58.233177709Z'
    **cryptoKeyName: projects/PROJECT_NAME/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME**
    name: projects/PROJECT_NAME/locations/LOCATION/workflows/WORKFLOW_NAME
    revisionCreateTime: '2022-11-18T19:44:04.933633237Z'
    revisionId: 000009-8be
    serviceAccount: projects/PROJECT_NAME/serviceAccounts/SA_NAME@PROJECT_NAME.iam.gserviceaccount.com
    sourceContents:
    [...]
    state: ACTIVE
    updateTime: '2022-11-18T19:44:05.171793128Z'
    

The `cryptokeyName` value is the resource ID of the Cloud KMS key used to secure the workflow and its execution.

## Disable CMEK for a workflow

You can disable CMEK for a workflow so that it no longer uses the associated Cloud KMS key.

###  Console 

  1. In the Google Cloud console, go to the **Workflows** page. 

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click the name of the workflow you want to update.

The **Workflows details** page appears.

  3. Click edit **Edit**.

  4. To clear the **Cloud KMS key** radio button, select **Google-managed encryption key**.

  5. Click **Next**.

  6. To save your changes and deploy the updated workflow, click **Deploy**.




###  gcloud 
    
    
    gcloud workflows deploy WORKFLOW_NAME \
        --source=SOURCE_FILE \
        --clear-kms-key \
        --service-account=SERVICE_ACCOUNT

This disables CMEK for the current workflow revision and any subsequent executions are created without CMEK encryption. Existing workflow revisions and executions remain encrypted with the keys with which they were previously encrypted.

## Disable Cloud KMS

If you want to revoke data access to your workflow or workflow executions, you can do either of the following to disable Cloud KMS:

  * [Disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy) the primary key version of your customer-managed encryption key. Disabling a CMEK key version suspends access to all data protected by that key version. Destroying a key version is the permanent counterpart of this action. Both affect only the workflows and workflow executions that are associated with the specific key. You can't create new executions or view the resources associated with the disabled or destroyed key. Any active executions will fail with a corresponding error message.

  * [Revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) the `cloudkms.cryptoKeyEncrypterDecrypter`IAM role from the Workflows service agent. This affects all workflows in the Google Cloud project that support encryption using CMEK. You can't create new CMEK-integrated workflows and executions, or view any CMEK-encrypted resources. Any active executions will fail with a corresponding error message.




Although neither operation guarantees instantaneous access revocation, IAM changes generally propagate faster. For more information, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Troubleshooting

You might encounter errors when using Cloud KMS with Workflows. The following table describes different issues and how to resolve them.

Issue | Description  
---|---  
Permission `cloudkms.cryptoKeyVersions.useToEncrypt` is denied | Either the provided Cloud KMS key does not exist or the permission is not properly configured. Solution: 

  * Check that the Cloud KMS key exists. [List the keys for a specified key ring](https://docs.cloud.google.com/workflows/docs/use-cmek#retrieve-id) and [verify its usage](https://docs.cloud.google.com/workflows/docs/use-cmek#verify-cmek).
  * Ensure that the Workflows service agent has [ access to the key](https://docs.cloud.google.com/workflows/docs/use-cmek#key-access) and has been granted the `cloudkms.cryptoKeyEncrypterDecrypter` role.

  
Key version is not enabled | The provided Cloud KMS key version has been disabled. Solution: [Re-enable the Cloud KMS key version](https://docs.cloud.google.com/kms/docs/enable-disable#enable).  
Key ring region does not match the resource to be protected | The provided KMS key ring region is different from the region of the workflow. Solution: Use a Cloud KMS key ring and protected workflow from the same region. (Note that they can be in different projects.) For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations) and [Workflows locations](https://docs.cloud.google.com/workflows/docs/locations).   
Cloud KMS quota limit is exceeded | Your quota limit for Cloud KMS requests has been reached. Solution: Limit the number of Cloud KMS calls or increase the quota limit. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).  
  
### How an unavailable key status is handled

If for some reason Cloud KMS is unavailable, Workflows might be unable to retrieve the status of your key from Cloud KMS.

If the key status is unavailable, the workflow or its execution will return a `state: UNAVAILABLE` value and related details in the `stateError` field.

If the key status becomes unavailable in the course of a workflow execution (for example, a permission is revoked during a callback), a runtime error occurs, returning a `state: FAILED` value, and related details in the `error` field.

## Pricing

This integration does not incur additional costs beyond the key operations, which are billed to your Google Cloud project. For current pricing information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
