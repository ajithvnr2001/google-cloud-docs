---
url: https://docs.cloud.google.com/tasks/docs/use-cmek/
title: Use customer-managed encryption keys \u00a0|\u00a0 Cloud Tasks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:26.988755+00:00
---

# Use customer-managed encryption keys  |  Cloud Tasks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tasks/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Tasks ](https://docs.cloud.google.com/tasks/docs)
  * [ Guides ](https://docs.cloud.google.com/tasks/docs/dual-overview)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Tasks encrypts customer content at rest. Cloud Tasks handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud Tasks. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud Tasks resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## What is protected with CMEK

When you enable CMEK in Cloud Tasks, you enable it for a region. When enabled, the body and header of tasks created in that region are protected with your key when at rest. If a task was created while CMEK was enabled, and the key is later made inactive (by disabling or deleting the key, or by disabling CMEK) the task is encrypted with your key but cannot be executed.

Tasks are not protected with CMEK in the following cases:

  * Task was created before enabling CMEK
  * Task is not in the region for which CMEK is enabled
  * Task is affected by a compatibility limitation



### Compatibility limitations

The Cloud Tasks integration with CMEK does not support the following:

  * **[`google-gax`](https://www.npmjs.com/package/google-gax) versions below `4.0.0`:** The NPM package `google-gax` for Node.js has limited support at versions earlier than `4.0.0`. For these versions, CMEK is only supported in the region `us-central1`. Even if you only have tasks in that region, it is recommended that you upgrade to version `4.0.0` or later.

  * **App Engine built-in Taskqueue service:** Tasks created using the App Engine built-in Taskqueue service are not protected by CMEK, even if they are in a region for which it is enabled. Enabling CMEK does not prevent the creation or operation (for example, execution or deletion) of these tasks.

  * **Pull queues:** If you enable CMEK, you can create and execute tasks on pull queues, but these tasks are not protected by CMEK. Pull queues are uncommon. To check if your queue is a pull queue, run the following gcloud CLI command in your terminal:
        
        gcloud tasks queues describe QUEUE_NAME

Replace `QUEUE_NAME` with the name of your queue.

If the `type` listed is `pull`, your queue is a pull queue. If the `type` listed is `push`, this limitation does not affect tasks on your queue.

  * **Queue-level routing:** When CMEK is enabled, you cannot apply [queue-level routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#configure_queue-level_routing_for_http_tasks). And if queue-level routing is enabled, you cannot enable CMEK. To check if you have queue-level routing enabled, do the following:

    1. Run the following gcloud CLI command in your terminal: 
           
           gcloud tasks queues describe QUEUE_NAME

Replace `QUEUE_NAME` with the name of your queue.
    2. In the output, look for the field `httpTarget` and check if the `uriOverride` has been set. If a `host` is specified, your queue has queue-level routing enabled and is not compatible with CMEK. To remove queue-level routing, see [Update or remove queue-level routing](https://docs.cloud.google.com/tasks/docs/configuring-queues#update_or_remove_queue-level_routing). If the output does not show `uriOverride` with a `host` specified, your queue does not use queue-level routing.

  * **Task TTL:** When CMEK is enabled, you cannot set [`task_ttl`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2beta3#queue) to greater than 60 days. And if you have a `task_ttl` set to greater than 60 days, you cannot enable CMEK.




## Before you begin

Before using CMEK in Cloud Tasks, complete the following steps:

  1. Enable the APIs.

###  Console 

     1. Enable the Cloud KMS and Cloud Tasks APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com,cloudtasks.googleapis.com)

###  gcloud 

     1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

     2. Set your default project. This should be the project that contains the Cloud Tasks resources that you want to protect with CMEK. If you need to run a command in a different project, such as the project containing your Cloud KMS resources, this page will include the `--project` flag in the gcloud CLI command and tell you which project to specify.
            
            gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with the ID of the project that contains your Cloud Tasks resources.

     3. Update `gcloud` components. 
            
            gcloud components update

     4. Enable the Cloud KMS and Cloud Tasks APIs for the project that will store your encryption keys. 
            
            gcloud services enable cloudkms.googleapis.com cloudtasks.googleapis.com \
                --project=PROJECT_ID

Replace `PROJECT_ID` with the ID of the project that will store your encryption keys. This could be the same project as your Cloud Tasks resources, but to limit access to your Cloud KMS keys, consider [Setting up Cloud KMS in a separate project](https://docs.cloud.google.com/kms/docs/separation-of-duties#using_separate_project).

  2. Cloud KMS produces Cloud Audit Logs when keys are enabled, disabled, or used by Cloud Tasks resources to encrypt and decrypt data. Make sure that [logging is enabled ](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project, and that you have decided which logging-specific permissions and roles apply to your use case. For more information, see [Cloud KMS audit logging information](https://docs.cloud.google.com/kms/docs/audit-logging).

  3. Get Identity and Access Management roles. 

To get the permissions that you need to use CMEK with Cloud Tasks, ask your administrator to grant you the following IAM roles on your project: 

     * Enable or disable CMEK: `roles/cloudtasks.admin`
     * View the key in use: `roles/cloudtasks.viewer`

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create a Cloud KMS key ring and key

If you already have a key ring in the same region as your Cloud Tasks resources and you want to use that key and key ring, skip this section. If not, use these instructions to create your Cloud KMS key and key ring.

  1. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring).

     * The key ring must be in the region that contains the Cloud Tasks resources that you want to protect. For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations) and [Cloud Tasks locations](https://docs.cloud.google.com/tasks/docs/dual-overview#supported_regions_by_target).

     * The key ring and the CMEK-protected Cloud Tasks resources can be in the same project, but to limit access to your Cloud KMS keys, consider [setting up Cloud KMS in a separate project](https://docs.cloud.google.com/kms/docs/separation-of-duties#using_separate_project).

  2. [Create a key for a specified key ring](https://docs.cloud.google.com/kms/docs/create-key).




## Retrieve the ID for a Cloud KMS key

The resource ID for a Cloud KMS key is required when you enable CMEK for Cloud Tasks.

### Console

  1. In the Google Cloud console, go to the **Key management** page and select the **Key inventory** tab. 

[Go to Key inventory](https://console.cloud.google.com/security/kms/keys)

  2. For the key whose resource ID you are retrieving, click _more_vert_ **Actions**.

  3. Click **Copy resource name**.

The resource ID for the key is copied to your clipboard. Its format is similar to the following:
         
         projects/PROJECT_NAME/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
         




###  gcloud 

  1. List all keys on a given key ring:
         
         gcloud kms keys list --keyring=KEY_RING --location=LOCATION --project=PROJECT_ID

Replace the following:

     * `KEY_RING`: the name of the key ring
     * `LOCATION`: the region of the key ring
     * `PROJECT_ID`: the ID of the project that contains the key ring

The output includes the key ID for each key. For example:
    
    NAME: projects/PROJECT_NAME/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    




## Grant the Cloud Tasks service agent access to the key

You must grant the [Cloud Tasks service agent](https://docs.cloud.google.com/iam/docs/service-agents) the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) Identity and Access Management (IAM) role so that it can access the Cloud KMS key:

###  Console 

  1. In the Google Cloud console, go to the **IAM** (Identity and Access Management) page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **Include Google-provided role grants** checkbox.

  3. Find the Cloud Tasks service account by typing `cloudtasks.iam.gserviceaccount.com` in the filter.

The Cloud Tasks service account has the form `service-PROJECT_NUMBER@gcp-sa-cloudtasks.iam.gserviceaccount.com`.

  4. Click the **Edit principal** pencil icon.

  5. In the panel that opens, click **Add another role**.

  6. Search for and select the **Cloud KMS CryptoKey Encrypter/Decrypter** role.

  7. Click **Save**.




###  gcloud 
    
    
    gcloud kms keys add-iam-policy-binding KEY_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudtasks.iam.gserviceaccount.com \
        --role=roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace the following:

  * `KEY_ID`: the fully qualified resource ID for your key. For instructions on finding this, see Retrieve the ID for a Cloud KMS key. Don't include a key version number. Including a key version number may cause this command to fail.
  * `PROJECT_NUMBER`: your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following command:
        
        PROJECT=$(gcloud info --format='value(config.project)')
        gcloud projects describe ${PROJECT} --format="value(projectNumber)"




As long as the service agent has the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role, a task in your CMEK-enabled region can encrypt and decrypt its data using the CMEK key. If you revoke this role, or if you disable or destroy the CMEK key, that data can't be accessed. In this document, see Disable CMEK for Cloud Tasks.

## Enable CMEK for Cloud Tasks

You can enable CMEK using the API or the gcloud CLI. For Cloud Tasks, CMEK is enabled by region. It is not enabled by individual tasks. When CMEK is enabled for a given region in Cloud Tasks, all tasks in that region are protected by CMEK.

###  gcloud 

To enable CMEK using the Google Cloud CLI, run the following command:
    
    
    gcloud tasks cmek-config update --location=LOCATION --kms-key-name=KEY_ID

Replace the following:

  * `LOCATION`: the [region](https://docs.cloud.google.com/tasks/docs/locations) of your Cloud Tasks resource
  * `KEY_ID`: the fully qualified resource ID for your key. For instructions on finding this, see Retrieve the ID for a Cloud KMS key. Don't include a key version number. Including a key version number may cause this command to fail.



###  REST 

You can enable CMEK by calling the `Update CMEK config` method. The Cloud Tasks API provides the `Update CMEK config` method in both the REST and RPC APIs:

  * **REST** : Use the [`updateCmekConfig`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations/updateCmekConfig) method.
  * **RPC:** Use the [`UpdateCmekConfigRequest`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#google.cloud.tasks.v2.UpdateCmekConfigRequest) method.



To verify that the key was enabled successfully, follow the instructions in the section Identify the key in use.

### Enable for pre-existing tasks

CMEK does not protect tasks that were created prior to enabling CMEK for Cloud Tasks. To protect pre-existing tasks with CMEK:

  1. Enable CMEK (see the section on enabling CMEK).
  2. Replace the pre-existing tasks. There are two primary ways to do this. The best way to do it depends on what is important to you:

     * **Continuous execution:** To ensure continuous execution ("at _least_ once" delivery), you can first recreate the task and then delete the pre-existing task after verifying that the new task works as expected. This can result in duplicate executions, because both the old and new task may execute before you delete the old task.

     * **Duplicate prevention:** To prevent duplicate executions ("at _most_ once" delivery), you can first delete the old task and then recreate it. This can result in lost executions, because of the time elapsed between deleting the old task and creating the new one.




## Identify the key in use

To identify the CMEK key in use for your Cloud Tasks resources, run the following gcloud CLI command:
    
    
    gcloud tasks cmek-config describe --location=LOCATION

Replace `LOCATION` with the [region](https://docs.cloud.google.com/tasks/docs/locations) of your Cloud Tasks resources.

If there is no output, then CMEK is not configured for the location specified.

## Apply a CMEK organization policy

Cloud Tasks is integrated with two [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to help ensure CMEK usage across an organization:

  * `constraints/gcp.restrictNonCmekServices` is used to require CMEK protection.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` is used to limit which Cloud KMS keys are used for CMEK protection.

**Note:** CMEK organization policies only apply to newly created resources within supported Google Cloud services. For more information, see [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

This integration lets you specify the following encryption compliance requirements for Cloud Tasks resources in your organization:

  * Require CMEKs for all new Cloud Tasks resources
  * Restrict Cloud KMS keys for a Cloud Tasks project



### Considerations when applying organization policies

Before applying any CMEK organization policies, you should be aware of the following.

#### Prepare for a propagation delay

After you set or update an organization policy, it can take up to 15 minutes for the new policy to take effect.

#### Consider existing resources

Existing resources are not subject to newly created organization policies. For example, an organization policy does not retroactively apply to existing tasks. Those resources are still accessible without a CMEK and, if applicable, are still encrypted with existing keys. If you want to apply the policy to existing tasks, you must enable CMEK for pre-existing tasks.

#### Verify required permissions to set an organization policy

The permission to set or update the organization policy might be difficult to acquire for testing purposes. You must be granted the [Organization Policy Administrator role](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles), which can only be granted at the organization level (rather than the project or folder level).

Although the role must be granted at the organization level, it is still possible to specify a policy that only applies to a specific project or folder.

### Require CMEKs for all new Cloud Tasks resources

You can use the `constraints/gcp.restrictNonCmekServices` constraint to require that CMEKs be used to protect all new Cloud Tasks resources in an organization.

If set, this organization policy causes all resource creation requests without a specified Cloud KMS key to fail.

After you set this policy, it applies only to new resources in the project. Any existing resources without Cloud KMS keys applied continue to exist and are accessible without issue.

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Using the **Filter** , search for the following constraint:
         
         constraints/gcp.restrictNonCmekServices
         

  3. In the Name column, click **Restrict which services may create resources without CMEK**.

  4. Click edit **Manage Policy**.

  5. On the **Edit policy** page, under **Policy source** , select **Override parent's policy**.

  6. Under **Rules** , click **Add a rule**.

  7. In the **Policy values** list, select **Custom**.

  8. In the **Policy type** list, select **Deny**.

  9. In the **Custom values** field, enter the following:
         
         is:cloudtasks.googleapis.com
         

  10. Click **Done** , and then click **Set policy**.




###  gcloud 

  1. Create a temporary file `/tmp/policy.yaml` to store the policy:
         
         name: projects/PROJECT_ID/policies/gcp.restrictNonCmekServices
           spec:
             rules:
             - values:
                 deniedValues:
                 - is:cloudtasks.googleapis.com

Replace `PROJECT_ID` with the ID of the project where you are applying this constraint.

  2. Run the [`org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command:
         
         gcloud org-policies set-policy /tmp/policy.yaml




To verify that the policy is successfully applied, you can try to create a queue in the project. The process fails unless you specify a Cloud KMS key.

### Restrict Cloud KMS keys for a Cloud Tasks project

You can use the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint to restrict the Cloud KMS keys that you can use to protect a resource in a Cloud Tasks project.

For example, you can specify a rule similar to the following: "For all Cloud Tasks resources in `projects/my-company-data-project`, Cloud KMS keys used in this project must come from `projects/my-company-central-keys` OR `projects/team-specific-keys`."

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Using the **Filter** , search for the following constraint:
         
         constraints/gcp.restrictCmekCryptoKeyProjects
         

  3. In the Name column, click **Restrict which projects may supply KMS CryptoKeys for CMEK**.

  4. Click edit **Manage Policy**.

  5. On the **Edit policy** page, under **Policy source** , select **Override parent's policy**.

  6. Under **Rules** , click **Add a rule**.

  7. In the **Policy values** list, select **Custom**.

  8. In the **Policy type** list, select **Allow**.

  9. In the **Custom values** field, enter the following:
         
         under:projects/KMS_PROJECT_ID
         

Replace `KMS_PROJECT_ID` with the ID of the project where the Cloud KMS keys you want to use are located.

For example, `under:projects/my-kms-project`.

  10. Click **Done** , and then click **Set policy**.




###  gcloud 

  1. Create a temporary file `/tmp/policy.yaml` to store the policy:
         
         name: projects/PROJECT_ID/policies/gcp.restrictCmekCryptoKeyProjects
           spec:
             rules:
             - values:
                 allowedValues:
                 - under:projects/KMS_PROJECT_ID

Replace the following

     * `PROJECT_ID`: the ID of the project where you are applying this constraint.
     * `KMS_PROJECT_ID`: the ID of the project where the Cloud KMS keys you want to use are located.
  2. Run the [`org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command:
         
         gcloud org-policies set-policy /tmp/policy.yaml




To verify that the policy is successfully applied, you can try to create a queue using a Cloud KMS key from a different project. The process will fail.

## Disable CMEK for Cloud Tasks

You can disable CMEK using the API or the gcloud CLI. For Cloud Tasks, CMEK is disabled by region. It is not disabled by individual tasks. When CMEK is disabled for a given region in Cloud Tasks, tasks in that region are not protected by CMEK.

Disabling CMEK affects tasks created in the future, not tasks created in the past:

  * **New tasks:** are not protected by CMEK
  * **Pre-existing tasks:** tasks that were created while CMEK was enabled remain encrypted and continue to execute as long as the Cloud KMS key remains active.




###  gcloud 

To disable CMEK using the Google Cloud CLI, use the following command:
    
    
    gcloud tasks cmek-config update --location=LOCATION --clear-kms-key

Replace the following:

  * `LOCATION`: the region of your Cloud Tasks resource.



###  REST 

You can disable CMEK by calling the `Update CMEK config` method and clearing the Cloud KMS key by replacing it with an empty string. The Cloud Tasks API provides the `Update CMEK config` method in both the REST and RPC APIs:

  * **REST** : Use the [`updateCmekConfig`](https://docs.cloud.google.com/tasks/docs/reference/rest/v2/projects.locations/updateCmekConfig) method.
  * **RPC:** Use the [`UpdateCmekConfigRequest`](https://docs.cloud.google.com/tasks/docs/reference/rpc/google.cloud.tasks.v2#google.cloud.tasks.v2.UpdateCmekConfigRequest) method.



## Remove Cloud KMS

If you want to revoke data access to your tasks, you can remove Cloud KMS. There are three ways to do this:

  * [Disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable) the customer-managed encryption key. Disabling a CMEK key suspends access to all data protected by that key version while the key is disabled. You can't access or create tasks with a key that is disabled. Attempting to execute a CMEK-protected task while the key is disabled results in an `UNKNOWN` error in Cloud Logging. You can [re-enable](https://docs.cloud.google.com/kms/docs/enable-disable#enable) the key later if you want. When you disable a customer-managed encryption key, it can take up to 5 minutes for the change to apply.

  * [Destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy) the customer-managed encryption key. Destroying a CMEK key permanently suspends access to all data protected by that key version. You can't access or create tasks with a key that has been destroyed. If a task was created while CMEK was enabled, and the key is later destroyed, the task is encrypted with your key but cannot be executed. If the task attempts to execute, Cloud Logging logs an `UNKNOWN` error. When you destroy a customer-managed encryption key, it can take up to 5 minutes for the change to apply.

  * [Revoke](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) the `cloudkms.cryptoKeyEncrypterDecrypter`IAM role from the Cloud Tasks service agent. This affects all tasks in the Google Cloud project that support encryption using CMEK. You can't create new CMEK-integrated tasks, or view any CMEK-encrypted resources.




Although none of these operations guarantees instantaneous access revocation, IAM changes generally take effect faster. For more information, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Pricing

This integration does not incur additional costs beyond the key operations, which are billed to your Google Cloud project. For current pricing information, see [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
