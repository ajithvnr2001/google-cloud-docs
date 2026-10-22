---
url: https://docs.cloud.google.com/dataform/docs/cmek/
title: Use customer-managed encryption keys \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:46.733602+00:00
---

# Use customer-managed encryption keys  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes using CMEK for Dataform and walks you through how to enable CMEK encryption of Dataform repositories.

By default, Dataform encrypts customer content at rest. Dataform handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Dataform. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Dataform resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## CMEK encryption of repository data

When you apply CMEK encryption to a Dataform repository, all Dataform-managed customer data in that repository is encrypted at rest using the CMEK protection key set for the repository. This data includes the following:

  * Git repository content of the Dataform repository and its workspaces
  * Compiled SQL queries and compilation errors
  * Stored SQL queries of workflow actions
  * Error details of executed workflow actions



Dataform uses CMEK protection keys in the following scenarios:

  * During every operation that requires decryption of customer data stored at rest. These operations include, but are not limited to the following: 
    * Responses to a user query—for example, [`compilationResults.query`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/query).
    * Creation of Dataform resources that require previously created encrypted repository data—for example, [workflow invocations](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workflowInvocations/create).
    * Git operations to update the [remote repository](https://docs.cloud.google.com/dataform/docs/connect-repository), for example, [pushing a Git commit](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/push).
  * During every operation that requires storing customer data at rest. These operations include, but are not limited to, the following: 
    * Responses to a user query—for example, [`compilationResults.create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.compilationResults/create).
    * Git operations to a workspace—for example, [pulling a Git commit](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/pull).



Dataform manages the encryption of customer data associated only with Dataform resources. Dataform does not manage encryption of customer data that is created in BigQuery through execution of Dataform workflows. To encrypt data created and stored in BigQuery, [configure CMEK for BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption).

### Supported keys

Dataform supports the following types of CMEK keys:

  * [Cloud KMS software keys](https://docs.cloud.google.com/kms/docs/protection-levels#software)
  * [Cloud Hardware Security Module (HSM) keys](https://docs.cloud.google.com/kms/docs/hsm)
  * [Cloud External Key Manager (Cloud EKM) keys](https://docs.cloud.google.com/kms/docs/ekm)



Key availability varies by key type and region. For more information about the geographical availability of CMEK keys, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

### Restrictions

Dataform supports CMEK with the following restrictions:

  * The maximum size of a CMEK-encrypted repository is 512 MB.
  * The maximum size of a workspace in a CMEK-encrypted repository is 512 MB.
  * You can't apply a CMEK protection key to a repository after the repository has been created. You can apply CMEK encryption during repository creation only.
  * You can't remove a CMEK protection key from a repository.
  * You can't change a CMEK protection key for a repository.
  * If you set a default Dataform CMEK key for your Google Cloud project, all new repositories created in the Google Cloud project location must be encrypted with CMEK. When you create a new repository in the Google Cloud project location, you can apply the default Dataform CMEK key or a different CMEK key, but you cannot apply [default encryption at rest](https://cloud.google.com/docs/security/encryption/default-encryption).
  * If you change the value of a default Dataform CMEK key, the previous value applies to pre-existing repositories, and the updated value applies to repositories created after the change.
  * You can set only one default Dataform CMEK key per location of Google Cloud project repositories.
  * Using Cloud HSM and Cloud EKM keys is subject to availability. For more information about availability of keys across locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).



### Cloud KMS quotas and Dataform

You can use Cloud HSM and Cloud EKM keys with Dataform. When you use CMEK in Dataform, your projects can consume Cloud KMS cryptographic requests quotas. For example, CMEK-encrypted Dataform repositories can consume these quotas for each change to repository contents. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

### Managing keys

Use Cloud KMS for all key-management operations. Dataform cannot detect or act upon any key changes until they are propagated by Cloud KMS. Some operations, such as disabling or destroying a key, can take [up to three hours to propagate](https://docs.cloud.google.com/kms/docs/consistency). Changes to permissions usually propagate much faster.

After the repository is created, Dataform calls Cloud KMS to make sure that the key is still valid during each operation on encrypted repository data.

If Dataform detects that your Cloud KMS key has been disabled or destroyed, all data stored in the corresponding repository becomes inaccessible.

If calls by Dataform to Cloud KMS detect that a formerly disabled key has been re-enabled, Dataform restores access automatically.

### Use external keys with Cloud EKM

As an alternative to using keys that reside on Cloud KMS, you can use keys that reside with a [supported external key management partner](https://docs.cloud.google.com/kms/docs/ekm#supported_partners). To do this, use Cloud External Key Manager (Cloud EKM) to create and manage external keys, which are pointers to keys that reside outside of Google Cloud. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

After you create an external key with Cloud EKM, you can apply it to a new Dataform repository by providing the ID of that key when [creating the repository](https://docs.cloud.google.com/dataform/docs/create-repository). This procedure is the same as applying a Cloud KMS key to a new repository.

**Caution:** If an external key is deleted or cannot be recovered, any repository data encrypted with that key becomes permanently inaccessible. Google doesn't control the availability of keys in an external key management partner system.

### Use Dataform default CMEK keys

To encrypt multiple Dataform repositories with the same CMEK key, you can set a default Dataform CMEK key for your Google Cloud project. You must specify the location of the Google Cloud project for the default Dataform CMEK key. You can set only one default CMEK key per Google Cloud project.

After you set a default Dataform CMEK key, Dataform applies the key to all new repositories created in the Google Cloud project location by default. When you [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository#create-repository), you can use the default key, or select a different CMEK key.

**Caution:** After you set a default Dataform CMEK key for your Google Cloud project, all new repositories created in the Google Cloud project location must be encrypted with CMEK. When you create a new repository in the Google Cloud project location, you can apply the default Dataform CMEK key or a different CMEK key, but you cannot apply [default encryption at rest](https://cloud.google.com/docs/security/encryption/default-encryption).

### How an unavailable key status is handled

In rare scenarios, such as during periods when Cloud KMS is unavailable, Dataform might be unable to retrieve the status of your key from Cloud KMS.

If your Dataform repository is protected by a key that is enabled at the time at which Dataform is unable to communicate with Cloud KMS, the encrypted repository data becomes inaccessible.

The encrypted repository data remains inaccessible until Dataform can reconnect with Cloud KMS and Cloud KMS responds that the key is active.

Conversely, if your Dataform repository is protected by a key that is disabled at the time at which Dataform is first unable to communicate with Cloud KMS, the encrypted repository data remains inaccessible until it is able to reconnect to Cloud KMS and you have re-enabled your key.

### Logging

You can audit the requests that Dataform sends to Cloud KMS on your behalf in Cloud Logging, if you have [enabled audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API in your project. These [Cloud KMS log entries](https://docs.cloud.google.com/kms/docs/audit-logging) are visible in [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-explorer-summary). For more information, see [View logs](https://docs.cloud.google.com/kms/docs/audit-logging#viewing_logs).

## Before you begin

  * Decide whether you are going to run Dataform and Cloud KMS in different projects, or in the same project. We recommend using separate projects for greater control over permissions. For information about Google Cloud project IDs and project numbers, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).

  * For the Google Cloud project that runs Cloud KMS: 

    1. [Enable the Cloud Key Management Service API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/). 
    2. Create a key ring and a key as described in [Creating key rings and keys](https://docs.cloud.google.com/kms/docs/creating-keys). Create the key ring in a location that matches the location of your Dataform repository: 
       * Repositories must use matching regional keys. For example, a repository in region `asia-northeast3` must be protected with a key from a key ring located in `asia-northeast3`. 
       * The `global` region can't be used with Dataform. 
For more information about the supported locations for Dataform and Cloud KMS, see [Cloud locations](https://cloud.google.com/about/locations/). 



## Enable CMEK

Dataform can access the key on your behalf after you grant the Cloud KMS [CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) role to the default [Dataform service agent](https://docs.cloud.google.com/dataform/docs/access-control#grant-dataform-required-access).

Your default Dataform service agent ID is in the following format:
    
    
    service-YOUR_PROJECT_NUMBER@gcp-sa-dataform.iam.gserviceaccount.com
    

To grant the CryptoKey Encrypter/Decrypter role to the default Dataform service agent, follow these steps:

###  Console 

  1. Open the **Key Management** page in the Google Cloud console. 

[Open the **Key Management** page](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key.

  3. Click the checkbox for the encryption key to which you want to add the role. The **Permissions** tab opens.

  4. Click **Add member**.

  5. Enter the email address of the service agent.

     * If the service agent is already on the members list, it has existing roles. Click the current role drop-down list for the service agent.
  6. Click the drop-down list for **Select a role** , click **Cloud KMS** , and then click the **Cloud KMS CryptoKey Encrypter/Decrypter** role.

  7. Click **Save** to apply the role to the service account.




###  gcloud 

You can use the Google Cloud CLI to assign the role:
    
    
    gcloud kms keys add-iam-policy-binding \
        --project=KMS_PROJECT_ID \
        --member serviceAccount:SERVICE_AGENT \
        --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
        --location=KMS_KEY_LOCATION \
        --keyring=KMS_KEY_RING \
        KMS_KEY
    

Replace the following:

  * `KMS_PROJECT_ID`: the ID of your Google Cloud project that is running Cloud KMS
  * `SERVICE_AGENT`: the email address of your default Dataform service agent
  * `KMS_KEY_LOCATION`: the location name of your Cloud KMS key
  * `KMS_KEY_RING`: the key ring name of your Cloud KMS key
  * `KMS_KEY`: the key name of your Cloud KMS key



## Apply a CMEK organization policy

Dataform is integrated with two [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to help ensure CMEK usage across an organization:

  * `constraints/gcp.restrictNonCmekServices` is used to require CMEK protection.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` is used to limit which Cloud KMS keys are used for CMEK protection.

**Note:** CMEK organization policies only apply to newly created resources within supported Google Cloud services. For more information, see [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

This integration lets you specify the following encryption compliance requirements for Dataform repositories in your organization:

  * Require CMEKs for all new Dataform repositories
  * Restrict Cloud KMS keys for a Dataform project



### Considerations when applying organization policies

Before applying any CMEK organization policies, you should be aware of the following.

#### Prepare for a propagation delay

After you set or update an organization policy, it can take up to 15 minutes for the new policy to take effect.

#### Consider existing resources

Existing resources are not subject to newly created organization policies. For example, an organization policy does not retroactively apply to existing repositories. Those resources are still accessible without a CMEK and, if applicable, are still encrypted with existing keys.

#### Verify required permissions to set an organization policy

The permission to set or update the organization policy might be difficult to acquire for testing purposes. You must be granted the [Organization Policy Administrator role](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles), which can only be granted at the organization level (rather than the project or folder level).

Although the role must be granted at the organization level, it is still possible to specify a policy that only applies to a specific project or folder.

### Require CMEKs for all new Dataform repositories

You can use the `constraints/gcp.restrictNonCmekServices` constraint to require that CMEKs be used to protect all new Dataform repositories in an organization.

If set, this organization policy causes all resource creation requests without a specified Cloud KMS key to fail.

After you set this policy, it applies only to new repositories in the project. Any existing repositories without Cloud KMS keys applied continue to exist and are accessible without issue.

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
         
         is:dataform.googleapis.com
         

  10. Click **Done** , and then click **Set policy**.




###  gcloud 

  1. Create a temporary file `/tmp/policy.yaml` to store the policy:
         
         name: projects/PROJECT_ID/policies/gcp.restrictNonCmekServices
           spec:
             rules:
             - values:
                 deniedValues:
                 - is:dataform.googleapis.com

Replace `PROJECT_ID` with the ID of the project where you are applying this constraint.

  2. Run the [`org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command:
         
         gcloud org-policies set-policy /tmp/policy.yaml




To verify that the policy is successfully applied, you can try to create a Dataform repository in the project. The process fails unless you specify a Cloud KMS key.

### Restrict Cloud KMS keys for a Dataform project

You can use the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint to restrict the Cloud KMS keys that you can use to protect a repository in a Dataform project.

For example, you can specify a rule similar to the following: "For all Dataform repositories in `projects/my-company-data-project`, Cloud KMS keys used in this project must come from `projects/my-company-central-keys` OR `projects/team-specific-keys`."

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




To verify that the policy is successfully applied, you can try to create a Dataform repository using a Cloud KMS key from a different project. The process will fail.

## Set a default Dataform CMEK key

Setting a default Dataform CMEK key for your Google Cloud project lets you encrypt multiple repositories with the same CMEK key. For more information, see Use a default key for Dataform repositories.

**Caution:** After you set a default Dataform CMEK key for your Google Cloud project, all new repositories created in the Google Cloud project location must be encrypted with CMEK. When you create a new repository in the Google Cloud project location, you can apply the default Dataform CMEK key or a different CMEK key, but you cannot apply [default encryption at rest](https://cloud.google.com/docs/security/encryption/default-encryption).

To set or edit a default CMEK key, call the Dataform API in the following request:
    
    
    curl -X PATCH \
    -H "Content-Type: application/json" \
    -d '{"defaultKmsKeyName":"projects/PROJECT_ID/locations/PROJECT_LOCATION/keyRings/KMS_KEY_RING/cryptoKeys/KMS_KEY"}' \
    https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/PROJECT_LOCATION/config
    

Replace the following:

  * KMS_KEY_RING: the key ring name of your Cloud KMS key.
  * KMS_KEY: the name of your Cloud KMS key.
  * PROJECT_ID: the ID of your Google Cloud project.
  * PROJECT_LOCATION: the location name of your Google Cloud project.



## Remove a default Dataform CMEK key

To remove a default Dataform CMEK key from your Google Cloud project, call the Dataform API in the following request:
    
    
    curl -X PATCH \
    -H "Content-Type: application/json" \
    -d '{"defaultKmsKeyName":""}' \
    https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/PROJECT_LOCATION/config
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * PROJECT_LOCATION: the location name of your Google Cloud project where you want to unset default CMEK.



## Check if a default Dataform CMEK key is set

To check if a default Dataform CMEK key is set for your Google Cloud project, call the Dataform API in the following request:
    
    
    curl -X GET \
    -H "Content-Type: application/json" \
    https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/PROJECT_LOCATION/config
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * PROJECT_LOCATION: the location name of your Google Cloud project.



## Apply CMEK to a repository

You can apply CMEK protection to a Dataform repository during repository creation.

To apply CMEK encryption to a Dataform repository, select encryption with the default Dataform CMEK key or specify a unique Cloud KMS key when you create the repository. For instructions, see [Create a repository](https://docs.cloud.google.com/dataform/docs/create-repository#create-repository).

You can't change the encryption mechanism of a Dataform repository after the repository is created.

For more information, see Restrictions.

## What's next

  * To learn more about CMEK, see [CMEK overview](https://docs.cloud.google.com/kms/docs/cmek).
  * To learn more about Cloud KMS quotas, see [Cloud KMS Quotas](https://docs.cloud.google.com/kms/quotas).
  * To learn more about Cloud KMS pricing, see [Cloud KMS Pricing](https://cloud.google.com/kms/pricing).
  * To learn more about Dataform repositories, see [Create a repository](https://docs.cloud.google.com/dataform/docs/create-repository).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
