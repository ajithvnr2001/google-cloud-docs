---
url: https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm/
title: Create and manage a Single-tenant Cloud HSM instance \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:25.171988+00:00
---

# Create and manage a Single-tenant Cloud HSM instance  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Create and manage a Single-tenant Cloud HSM instance Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to create, provision, and manage a Single-tenant Cloud HSM instance using the Google Cloud CLI. After you create and provision your instance, you can create and use keys in the instance using the Google Cloud console, Cloud Key Management Service API, the gcloud CLI, and client libraries.

Creating and managing your instance requires [quorum authentication](https://docs.cloud.google.com/kms/docs/single-tenant-hsm#quorum). When you create your instance, you define the number of quorum member approvals that are required to run instance operations. Your quorum members must always have **at least this number** of control keys available to maintain administrative control of your instance.

**Caution:** Store the private keys in a secure location. If you lose a key but still have enough keys for quorum authentication, you can register a new key.**Warning:** If you lose too many keys and can't meet your required quorum size, you lose administrative control of the instance. Without administrative control of the instance, you can't register new keys or refresh the instance, and the instance is eventually disabled entirely. Cloud HSM created in the instance are lost if the instance is disabled and you don't have a quorum to re-enable it.

## Before you begin

  1. Review and apply the [Single-tenant Cloud HSM best practices](https://docs.cloud.google.com/kms/docs/single-tenant-hsm#best-practices) when creating and maintaining your instance. **Warning:** If you don't follow the best practices, your instance is more likely to be accidentally or maliciously lost or destroyed. Because you control your instance, Google can't stop you from creating a dangerous configuration that risks irrecoverable data loss.
  2. Decide how many quorum members you want to start with. Additional quorum members can be added later, if approved by the existing quorum members. The minimum number of quorum members is three.
  3. Decide how many quorum members are required to approve proposals. You **can't change** this number after the instance is created. Your quorum members must always have access to this many control keys to maintain the instance. The minimum quorum size is two. The required quorum size must be lower than the number of quorum members.
  4. Decide how you will make sure the instance is refreshed on time. You must monitor the `disableDate` of the instance and propose, approve, and execute an instance refresh operation **before** the deadline to avoid unwanted downtime.
  5. To get the permissions that you need to create, manage, and use Single-tenant Cloud HSM instances, ask your administrator to grant you the following IAM roles on the project or a parent resource: 

     * Create proposals: Cloud KMS single-tenant HSM Proposer (`cloudkms.hsmSingleTenantProposer`) 
     * Approve proposals: Cloud KMS single-tenant HSM Quorum Member (`cloudkms.hsmSingleTenantQuorumMember`) 
     * Execute proposals: Cloud KMS single-tenant HSM Executor (`cloudkms.hsmSingleTenantExecutor`) 
     * Create keys: [Cloud KMS single-tenant HSM Key Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.hsmSingleTenantKeyCreator) (`roles/cloudkms.hsmSingleTenantKeyCreator`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  6. For each quorum member, generate one RSA-2048 key pair for two-factor authentication (2FA). We recommend that you use physical tokens for your control keys. Follow your organization's standards for creating RSA-2048 key pairs on physical tokens.

For demonstration purposes, this guide uses OpenSSL to create three software-backed RSA-2048 keys:
         
         openssl genrsa -out rsaprivate1.pem
             openssl genrsa -out rsaprivate2.pem
             openssl genrsa -out rsaprivate3.pem
         
             openssl rsa -in rsaprivate1.pem  -out rsapub1.pem -pubout
             openssl rsa -in rsaprivate2.pem  -out rsapub2.pem -pubout
             openssl rsa -in rsaprivate3.pem  -out rsapub3.pem -pubout
             

Store the private keys securely; you need them to approve proposals. Keep the public keys handy; you need them to create the Single-tenant Cloud HSM instance.

  7. Choose a Cloud KMS location that supports Single-tenant Cloud HSM. To identify compatible locations, view the list of locations on the [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations) page. For the **HSM support** filter, select **Supports single-tenant HSM**.




## Create and provision an instance

To create and provision a Single-tenant Cloud HSM instance, you use the gcloud CLI to create the instance resource, create a proposal to register your authentication keys, and then approve and execute the proposal.

### Create the instance

This step must be completed by an instance administrator with the **Cloud KMS single-tenant HSM Proposer** role.

  1. Set your default project.
         
         gcloud config set project PROJECT_ID
         

Replace PROJECT_ID with the identifier of your project.

  2. Create the Single-tenant Cloud HSM instance.
         
         gcloud kms single-tenant-hsm create --location=LOCATION \
             --total-approver-count=QUORUM_MEMBER_COUNT \
             --single-tenant-hsm-instance-id=INSTANCE_ID
         

Replace the following:

     * `LOCATION`: the location where you want to create your instance—for example, `us-central1`.
     * `QUORUM_MEMBER_COUNT`: the total number of quorum members. This is also the number of control keys that you created previously. The minimum value is `3`. Additional keys can be added later with quorum approval. You must have at least one more quorum member than your required quorum size to recover after losing a control key.
     * `INSTANCE_ID`: the identifier that you want to use for the instance—for example, `example-sthsm-instance`. You can omit the `--single-tenant-hsm-instance-id` flag to have Cloud HSM assign a UUID.
  3. Check the status of the instance.
         
         gcloud kms single-tenant-hsm describe INSTANCE_ID \
             --location=LOCATION
         

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `LOCATION`: the location where you created your instance.

If the state is `PENDING_TWO_FACTOR_AUTH_REGISTRATION`, you can provision the instance. It usually takes between 5 and 30 minutes to reach this state.




### Provision the instance

  1. Create a proposal to register your two-factor authentication keys using the `register_2fa_keys` operation. This step requires the **Cloud KMS single-tenant HSM Proposer** role. Unlike most proposals, the register_2fa_keys proposal requires signed challenges from **all** quorum members.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
             --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
             --location LOCATION \
             --operation-type register_2fa_keys \
             --required-approver-count MEMBERS_REQUIRED_FOR_APPROVAL \
             --two-factor-public-key-pems=PUBLIC_KEY_LIST

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the unique identifier that you want to use for this proposal—for example, `set-up-2fa`.
     * `LOCATION`: the location where you created your instance.
     * `MEMBERS_REQUIRED_FOR_APPROVAL`: the number of quorum members who must approve a proposal before the operation can be executed. The minimum value is `2`. This value **can't be changed** after the instance is provisioned. Your quorum members must always have access to at least this many control keys to retain administrative control of the instance.
     * `PUBLIC_KEY_LIST`: a comma-separated list of paths to the public key portions of all of your control keys—for example, `rsapub1.pem,rsapub2.pem,rsapub3.pem`. The number of public keys in this list must match the value of `QUORUM_MEMBER_COUNT` that you used previously.
  2. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `set-up-2fa`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  3. Get the challenges from the proposal. Provisioning a new Single-tenant Cloud HSM instance requires signed challenges from all members of the quorum. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](quorumParameters.challenges)"
           

This command returns a JSON-formatted array of challenges.

  4. For each key, decode the challenge using `basenc --base64url -d` and sign it with the corresponding private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  5. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST"
           

Replace `SIGNED_QUORUM_CHALLENGE_LIST` with a JSON-formatted array of challenges, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  6. After the proposal has been approved, use the `execute` command to complete the `register_2fa_keys` operation. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.
         
         gcloud kms single-tenant-hsm proposal execute PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION

This is a long-running operation that provisions users and creates backups. The instance becomes `ACTIVE` after 20 to 30 minutes.

  7. After the instance is `ACTIVE`, view the instance details to view the `disableDate`:
         
         gcloud kms single-tenant-hsm describe INSTANCE_ID \
             --location=LOCATION
         

Note the `disableDate` of the instance. You must complete a `refresh_sthi` operation before this time, or your instance will be disabled.




## View instances

Users with any of the following roles can view a list of Single-tenant Cloud HSM instances and their states:

  * **Cloud KMS single-tenant HSM Proposer**
  * **Cloud KMS single-tenant HSM Quorum Member**
  * **Cloud KMS single-tenant HSM Executor**
  * **Cloud KMS Viewer**
  * **Cloud KMS Administrator**



Make sure to review the state of your instances regularly. Instances must be refreshed regularly to remain **Active**.

Instances in the **Active** state can be used. Developers who need to create or import keys in Single-tenant Cloud HSM instances need the resource identifier of the instance. The resource identifier uses the following format:
    
    
    projects/INSTANCE_PROJECT/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME
    

To view instances in your organization and find their resource identifiers, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **KMS infrastructure** page.

[Go to KMS infrastructure](https://console.cloud.google.com/security/kms/infrastructure)

  2. On the **Single-tenant HSM instance** card, click **View**. The **Single-tenant HSM instance** page displays a list of all Single-tenant Cloud HSM instances that you have permissions to view.

  3. To view details for an instance, click the name of the instance. The **Single-tenant HSM instance details** page displays details for the selected instance, including the full resource identifier of the instance and a list of proposals created for the instance.

  4. Optional: To view or download the public keys associated with your quorum members' current two-factor authorization (2FA) keys, click **Get public key**. You can compare the public keys with your private 2FA keys to verify which control keys are active.




###  gcloud 

View a list of existing instances using the `kms single-tenant-hsm list` method.
    
    
    gcloud kms single-tenant-hsm list --location=LOCATION

Replace `LOCATION` with the location where you want to view Single-tenant Cloud HSM instances.

View details of an existing instance using the `kms single-tenant-hsm describe` method.
    
    
    gcloud kms single-tenant-hsm describe INSTANCE_ID \
        --location=LOCATION
    

Replace the following:

  * `INSTANCE_ID`: the instance that you want to view details for.
  * `LOCATION`: the location where you want to view Single-tenant Cloud HSM instances.



## Use the instance

While your instance is `ACTIVE`, you can create and use keys. You can create single-tenant Cloud HSM keys on any key ring that exists in the same location as an active Single-tenant Cloud HSM instance.

Creating single-tenant Cloud HSM keys requires the **Cloud KMS single-tenant HSM Key Creator** role in addition to the **Cloud KMS Admin** role.

After they are created, using single-tenant Cloud HSM keys doesn't require special permissions.

### Create a key

When you create a single-tenant Cloud HSM key, you must specify the Single-tenant Cloud HSM instance where you want to create it. Otherwise, the process is similar to creating any other key. For detailed instructions, see [Create a key](https://docs.cloud.google.com/kms/docs/create-key).

### Import a key

When you import key material into a single-tenant Cloud HSM key, you must specify the Single-tenant Cloud HSM instance where you want to store it. Otherwise, the process is similar to importing any other key. For detailed instructions, see [Import a key version into Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/importing-a-key).

### Use a key

After the key is created, using a single-tenant Cloud HSM key is identical to using any other Cloud HSM key. You don't need to specify the Single-tenant Cloud HSM instance to use the key.

## Key portability

Key portability lets you manage your own wrapping keys on Single-tenant Cloud HSM instances. This capability lets you import and export other keys (referred to as _wrappable keys_) by wrapping them with your custom wrapping key. Key portability is useful for key interoperability between different cloud providers or between different Google Cloud regions.

All key portability operations require the keys to be created and stored on Single-tenant Cloud HSM instances. [RFC 5649](https://www.rfc-editor.org/info/rfc5649/) is the only supported algorithm for key wrapping.

To use key portability, you must complete the following steps:

  1. Set up a trusted wrapping key.
  2. Create or import a wrappable key.
  3. Use the trusted wrapping key to import pre-wrapped key material or export a wrappable key.



### Set up a trusted wrapping key

A _trusted wrapping key_ is an AES key used to wrap and unwrap other keys for export or import as defined in [RFC 5649](https://www.rfc-editor.org/info/rfc5649/). To set up a trusted wrapping key on a Single-tenant Cloud HSM instance, you must import the key as an import-only key with the `AES_WRAPPING` purpose, and then promote it to trusted.

Key promotion requires approval of a single quorum member.

  1. Create an import-only key resource with the `AES_WRAPPING` purpose:
         
         gcloud kms keys create KEY_NAME \
                 --location LOCATION \
                 --keyring KEY_RING \
                 --purpose AES_WRAPPING \
                 --protection-level HSM_SINGLE_TENANT \
                 --skip-initial-version-creation \
                 --import-only \
                 --crypto-key-backend "projects/INSTANCE_PROJECT/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME"
             

Replace the following:

     * `KEY_NAME`: the identifier for the trusted wrapping key.
     * `LOCATION`: the region where the key ring and Single-tenant Cloud HSM instance are located.
     * `KEY_RING`: the key ring where you want to create the key.
     * `INSTANCE_PROJECT`: the identifier of the project that contains the Single-tenant Cloud HSM instance.
     * `INSTANCE_NAME`: the identifier of the Single-tenant Cloud HSM instance.
  2. Create an import job for importing the key material:
         
         gcloud kms import-jobs create IMPORT_JOB_NAME \
                 --location LOCATION \
                 --keyring KEY_RING \
                 --import-method IMPORT_METHOD \
                 --protection-level HSM_SINGLE_TENANT
             

Replace the following:

     * `IMPORT_JOB_NAME`: the identifier for the import job.
     * `IMPORT_METHOD`: the import method for wrapping key material—for example, `rsa-oaep-4096-sha256-aes-256`.
  3. Import the raw AES key material.
         
         gcloud kms keys versions import \
                 --import-job IMPORT_JOB_NAME \
                 --location LOCATION \
                 --keyring KEY_RING \
                 --key KEY_NAME \
                 --algorithm aes-256-kwp \
                 --target-key-file TRUSTED_KEY_PATH
             

Replace `TRUSTED_KEY_PATH` with the path to the file containing the raw trusted wrapping key bytes.

**Important:** You can't use your imported wrapping key for trusted operations until you promote it. 
  4. Create a proposal to promote the wrapping key to trusted. The operation type is `upgrade_key_trust`. Promotion operations must be signed and approved by the same quorum member who initiated them.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_NAME \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type upgrade_key_trust \
                 --keyring KEY_RING \
                 --key KEY_NAME \
                 --two-factor-login-key PATH_TO_PUBLIC_KEY
             

Replace the following:

     * `PROPOSAL_ID`: a unique identifier for this proposal.
     * `PATH_TO_PUBLIC_KEY`: the path to the public key of the quorum member who initiates and signs the proposal.
  5. View the status of the proposal and wait until it changes to `PENDING`:
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
                 --single_tenant_hsm_instance INSTANCE_NAME \
                 --location LOCATION
             

When the status is `PENDING`, you can sign the challenge.

  6. Get the challenge from the proposal.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
                 --single_tenant_hsm_instance INSTANCE_NAME \
                 --location LOCATION \
                 --format="json[](requiredActionQuorumParameters.requiredChallenges)"
             

This command returns a JSON-formatted array that contains the challenge.

  7. Decode the challenge using `basenc --base64url -d`, and then sign it. The challenge must be signed by the private key that matches the public key that was provided when the proposal was created.
         
         echo CHALLENGE | basenc --base64url -d > decoded-challenge.txt
             openssl dgst -sign PRIVATE_KEY_PATH -out signed-challenge.txt decoded-challenge.txt
             

Replace the following:

     * `CHALLENGE`: the contents of the challenge from the output of the previous step.
     * `PRIVATE_KEY_PATH`: the path to the private key of the quorum member who created the proposal.
  8. Approve the proposal by uploading the signed challenge. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
                 --location LOCATION \
                 --single_tenant_hsm_instance INSTANCE_NAME \
                 --required-challenge-replies="[('signed-challenge.txt','PUBLIC_KEY_PATH')]"
             

Replace `PUBLIC_KEY_PATH` with the path to the public key of the quorum member who created the proposal.

After you upload the signed challenge, the proposal state updates to `APPROVED`.

  9. After the proposal is approved, execute it to complete the promotion:
         
         gcloud kms single-tenant-hsm proposal execute PROPOSAL_ID \
                 --single_tenant_hsm_instance INSTANCE_NAME \
                 --location LOCATION
             

After the proposal is executed, the key is promoted to a trusted wrapping key and can be used to import or export other keys on the Single-tenant Cloud HSM instance.




### Manage wrappable keys

A _wrappable key_ is a cryptographic key that is designated for secure import or export using a trusted wrapping key. You must configure a key to be wrappable when the key resource is created. You cannot modify this setting later.

#### Create a new wrappable key

To create a new wrappable key, use the `--hsm-trusted-wrapping` flag:
    
    
    gcloud kms keys create WRAPPABLE_KEY_NAME \
        --location LOCATION \
        --keyring KEY_RING \
        --purpose PURPOSE \
        --protection-level HSM_SINGLE_TENANT \
        --hsm-trusted-wrapping \
        --crypto-key-backend "projects/INSTANCE_PROJECT/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME"

Replace the following:

  * `WRAPPABLE_KEY_NAME`: the name for the new wrappable key.
  * `PURPOSE`: the purpose of the key—for example, `raw-encryption`. Imported keys can't use the `ENCRYPT_DECRYPT` key purpose.



#### Import a wrappable key

You can use an import job to import existing key material that you want to be able to export in the future. To do so, you must include the `hsm-trusted-wrapping` flag both when you create they key and when you import the key version.

  1. Create a key resource with the `--hsm-trusted-wrapping` flag:
         
         gcloud kms keys create WRAPPABLE_KEY_NAME \
             --location LOCATION \
             --keyring KEY_RING \
             --purpose PURPOSE \
             --protection-level HSM_SINGLE_TENANT \
             --hsm-trusted-wrapping \
             --skip-initial-version-creation \
             --crypto-key-backend "projects/INSTANCE_PROJECT/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME"
         

  2. Create an import job:
         
         gcloud kms import-jobs create IMPORT_JOB_NAME \
             --location LOCATION \
             --keyring KEY_RING \
             --import-method IMPORT_METHOD \
             --protection-level HSM_SINGLE_TENANT
         

  3. Import the key version, with the `--hsm-trusted-wrapping` flag:
         
         gcloud kms keys versions import \
             --import-job IMPORT_JOB_NAME \
             --location LOCATION \
             --keyring KEY_RING \
             --key WRAPPABLE_KEY_NAME \
             --algorithm ALGORITHM \
             --target-key-file UNWRAPPED_KEY_TO_IMPORT \
             --hsm-trusted-wrapping
         

Replace the following:

     * `KEY_ALGORITHM`: the algorithm of the key that you are importing.
     * `UNWRAPPED_KEY_TO_IMPORT`: the path to the raw (unwrapped) key material.



### Use trusted keys for import and export

After setting up a trusted wrapping key, you can use it to import pre-wrapped key material into a wrappable key, or export a wrappable key.

#### Import a key version pre-wrapped with a trusted key

You can import key material wrapped on-premises with your copy of a trusted wrapping key without using an import job.

  1. Ensure that you have created the target wrappable key resource with the `--hsm-trusted-wrapping` flag and `--import-only` option. See the Create a new wrappable key section.
  2. Import the pre-wrapped key version:
         
         gcloud kms keys versions import-trusted-key-wrapped \
             --location LOCATION \
             --target-keyring KEY_RING \
             --target-key TARGET_KEY_NAME \
             --trusted-keyring TRUSTED_KEY_RING \
             --trusted-key TRUSTED_KEY_NAME \
             --target-algorithm ALGORITHM \
             --wrapped-key-file PATH_TO_WRAPPED_KEY
         

Replace the following:

     * `TARGET_KEY_NAME`: the name of the wrappable key resource to import the key material into.
     * `TRUSTED_KEY_RING`: the key ring of the trusted wrapping key.
     * `TRUSTED_KEY_NAME`: the name of the promoted trusted wrapping key.
     * `ALGORITHM`: the algorithm of the target key. Supported values are all Cloud Key Management Service algorithms except `GOOGLE_SYMMETRIC_ENCRYPTION`.
     * `PATH_TO_WRAPPED_KEY`: the path to the file that contains the key material wrapped with the trusted wrapping key.



#### Export a wrappable key by wrapping it with a trusted key

You can wrap an existing wrappable key using a trusted wrapping key and save the resulting wrapped key material to a file.
    
    
    gcloud kms keys versions export-trusted-key-wrapped \
        --location LOCATION \
        --trusted-keyring TRUSTED_KEY_RING \
        --trusted-key TRUSTED_KEY_NAME \
        --target-keyring TARGET_KEY_RING \
        --target-key TARGET_KEY_NAME \
        --wrapped-key-file PATH_TO_OUTPUT_WRAPPED_KEY

Replace the following:

  * `TRUSTED_KEY_RING`: the key ring of the trusted wrapping key.
  * `TRUSTED_KEY_NAME`: the name of the promoted trusted wrapping key.
  * `TARGET_KEY_RING`: the key ring of the wrappable key being exported.
  * `TARGET_KEY_NAME`: the name of the wrappable key being exported.
  * `PATH_TO_OUTPUT_WRAPPED_KEY`: the path where the wrapped key material will be saved.



## Maintain an instance

After your instance is provisioned, you are responsible for maintaining the instance. You maintain the instance by creating proposals for maintenance operations, obtaining quorum approval, and then executing the approved operation. Only one proposal can be active at a time; if you choose not to move forward with a proposal, you can't propose a different operation until you either delete the active proposal or wait until the proposal expires.

You must refresh your instance before the `disableDate`. If you need to check the `disableDate` of an instance, you can view instance details.

### View instance proposals

To view proposals for an instance, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **KMS infrastructure** page.

[Go to KMS infrastructure](https://console.cloud.google.com/security/kms/infrastructure)

  2. On the **Single-tenant HSM instance** card, click **View**. The **Single-tenant HSM instance** page displays a list of all Single-tenant Cloud HSM instances that you have permissions to view.

  3. Locate the instance where you want to view proposals, and then click the name of the instance. The **Single-tenant HSM instance details** page displays details for the instance, including a list of proposals created for the instance.

  4. Optional: To filter the list of proposals, click the filter_alt **Filter** bar and enter your filter criteria. For example, you can filter the list to see only the proposal that is pending approval or only proposals that have been successfully completed.




###  gcloud 

  * View a list of existing proposals using the `kms single-tenant-hsm proposal list` method.
        
        gcloud kms single-tenant-hsm proposal list INSTANCE_ID \
            --location=LOCATION

Replace the following:

    * `INSTANCE_ID`: the identifier of the Single-tenant Cloud HSM instance that you want to view proposals for.
    * `LOCATION`: the location where you want to view Single-tenant Cloud HSM instances.



### Refresh an instance

You can refresh an instance to keep it updated and help prevent unplanned downtime. This operation requires quorum authentication. After the proposal is approved, the operation takes approximately 15 to 30 minutes to complete.

When you refresh an instance, the `disableDate` is set to 730 days from the time of the refresh.

  1. Create a proposal to refresh the instance using the `refresh_sthi` operation type. This step requires the **Cloud KMS single-tenant HSM Proposer** role.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type refresh_sthi
             

Replace the following:

     * `INSTANCE_ID`: the identifier of the instance.
     * `LOCATION`: the location where you created the instance.
     * `PROPOSAL_ID`: the unique identifier that you want to use for this proposal—for example, `refresh_instance`.
  2. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `refresh_instance`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  3. Get the challenges from the proposal. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](quorumParameters.challenges)"
           

This command returns a JSON-formatted array of challenges.

  4. For each challenge returned in the previous step, decode the challenge using `basenc --base64url -d` and sign it with a private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  5. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST"
           

Replace `SIGNED_QUORUM_CHALLENGE_LIST` with a JSON-formatted array of challenges, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  6. Execute the proposal. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.
         
         gcloud kms single-tenant-hsm proposal execute  PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION
             

After the operation is complete, the instance remains in the `ACTIVE` state and the `disableDate` is set to 730 days from the time of the refresh.




### Add a quorum member

You can add a quorum member to an instance. This operation requires quorum authentication. After the proposal is approved, the operation takes approximately 15 to 30 minutes to complete.

  1. Generate a new RSA-2048 key pair for the new quorum member. Follow your organization's standards for creating RSA-2048 key pairs on physical tokens.

Store the private key securely; you need it to approve proposals. Keep the public key handy; you need it to add the new quorum member to the Single-tenant Cloud HSM instance.

  2. Create a proposal to add a quorum member to the instance using the `add_quorum_member` operation. This step requires the **Cloud KMS single-tenant HSM Proposer** role.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type add_quorum_member \
                 --two_factor_public_key_pem PATH_TO_PUBLIC_KEY
             

Replace the following:

     * `INSTANCE_ID`: the identifier of the instance.
     * `LOCATION`: the location where you created the instance.
     * `PROPOSAL_ID`: the unique identifier that you want to use for this proposal—for example, `add_quorum_member`.
     * `PATH_TO_PUBLIC_KEY`: the path to the new public key—for example, `rsapub4.pem`.
  3. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `add_quorum_member`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  4. Get the challenges from the proposal. Adding a new quorum member requires signed challenges from a quorum of existing members plus a signed challenge from the new member using the new key. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](requiredActionQuorumParameters.requiredChallenges,requiredActionQuorumParameters.quorumChallenges)"
           

This command returns a JSON-formatted array of challenges. The `requiredActionQuorumParameters.requiredChallenges` field contains a challenge for the new key that you are registering. The `requiredActionQuorumParameters.quorumChallenges` field contains challenges for a quorum of the existing keys. You must sign all of the challenges in the `requiredActionQuorumParameters` object.

  5. For each challenge returned in the previous step, decode the challenge using `basenc --base64url -d` and sign it with a private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  6. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST" \
               --required-challenge-replies="SIGNED_REQUIRED_CHALLENGE_LIST"
           

Replace the following:

     * `SIGNED_QUORUM_CHALLENGE_LIST`: a JSON-formatted array of challenges signed using private keys that are already registered, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.
     * `SIGNED_REQUIRED_CHALLENGE_LIST`: a JSON-formatted array containing the challenge signed using the new private key, where the only list item isofthe a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-newkey.txt','rsapub-newkey.pem')]`.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  7. Execute the proposal. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.
         
         gcloud kms single-tenant-hsm proposal execute  PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION
             

After the operation is complete, the new quorum member can participate in challenges to approve proposals. The public key that you added is now included in the list of public keys in the instance details.




### Remove a quorum member

If you have more quorum members than your required quorum size, you can remove a quorum member from an instance. This operation requires quorum authentication. After the proposal is approved, the operation takes approximately 15 to 30 minutes to complete.

**Caution:** Removing a quorum member reduces the number of approved control keys for your instance. You must maintain more quorum members than the required quorum size of the instance. If you are rotating control keys, we recommend completing the `add_quorum_member` operation before approving the `remove_quorum_member` proposal.

  1. Create a proposal to remove a quorum member to the instance using the `remove_quorum_member` operation. This step requires the **Cloud KMS single-tenant HSM Proposer** role.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type remove_quorum_member \
                 --two_factor_public_key_pem PATH_TO_PUBLIC_KEY
             

Replace the following:

     * `INSTANCE_ID`: the identifier of the instance.
     * `LOCATION`: the location where you created the instance.
     * `PROPOSAL_ID`: the unique identifier that you want to use for this proposal—for example, `remove_quorum_member`.
     * `PATH_TO_PUBLIC_KEY`: the path to the public key that you want to remove from the instance—for example, `rsapub3.pem`. After the operation completes, the corresponding private key can't be used to approve proposals.
  2. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `remove_quorum_member`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  3. Get the challenges from the proposal. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](quorumParameters.challenges)"
           

This command returns a JSON-formatted array of challenges.

  4. For each challenge returned in the previous step, decode the challenge using `basenc --base64url -d` and sign it with a private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  5. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST"
           

Replace `SIGNED_QUORUM_CHALLENGE_LIST` with a JSON-formatted array of challenges, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  6. Execute the proposal. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.
         
         gcloud kms single-tenant-hsm proposal execute  PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION
             

After the operation is complete, the removed quorum member can no longer participate in challenges to approve proposals. The public key that you removed is no longer included in the list of public keys in the instance details.




### Disable an instance

You can disable an instance to temporarily block access to all of its keys. This operation requires quorum authentication. After the proposal is approved, the operation takes approximately 15 to 30 minutes to complete.

While an instance is disabled, keys stored in that instance still appear as `ACTIVE`, but are unusable. Trying to perform cryptographic operations with a key in a disabled instance results in an error.

  1. Create a proposal to disable the instance using the `disable_sthi` operation type. This step requires the **Cloud KMS single-tenant HSM Proposer** role.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type disable_sthi
             

Replace the following:

     * `INSTANCE_ID`: the identifier of the instance.
     * `LOCATION`: the location where you created the instance.
     * `PROPOSAL_ID`: the unique identifier that you want to use for this proposal—for example, `disable_instance`.
  2. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `disable_instance`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  3. Get the challenges from the proposal. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](quorumParameters.challenges)"
           

This command returns a JSON-formatted array of challenges.

  4. For each challenge returned in the previous step, decode the challenge using `basenc --base64url -d` and sign it with a private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  5. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST"
           

Replace `SIGNED_QUORUM_CHALLENGE_LIST` with a JSON-formatted array of challenges, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  6. Execute the proposal. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.
         
         gcloud kms single-tenant-hsm proposal execute  PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION
             

After the operation is complete, the instance remains in the `DISABLED` state and can't be used until it is re-enabled.




### Enable an instance

You can re-enable a `DISABLED` instance to restore access to it and its keys. This operation requires quorum authentication. After the proposal is approved, the operation takes approximately 15 to 30 minutes to complete.

  1. Create a proposal to enable the instance using the `enable_sthi` operation type. This step requires the **Cloud KMS single-tenant HSM Proposer** role.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type enable_sthi
             

Replace the following:

     * `INSTANCE_ID`: the identifier of the instance.
     * `LOCATION`: the location where you created the instance.
     * `PROPOSAL_ID`: the unique identifier that you want to use for this proposal—for example, `enable_instance`.
  2. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `enable_instance`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  3. Get the challenges from the proposal. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](quorumParameters.challenges)"
           

This command returns a JSON-formatted array of challenges.

  4. For each challenge returned in the previous step, decode the challenge using `basenc --base64url -d` and sign it with a private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  5. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST"
           

Replace `SIGNED_QUORUM_CHALLENGE_LIST` with a JSON-formatted array of challenges, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  6. Execute the proposal. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.
         
         gcloud kms single-tenant-hsm proposal execute  PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION
             

After the operation is complete, the instance returns to the `ACTIVE` state and the `disableDate` is set to 730 days from the time of the refresh.




### Delete an instance

You can delete an instance to permanently destroy it and its keys. This operation requires quorum authentication. After the proposal is approved, the operation takes approximately 15 to 30 minutes to complete.

After an instance is deleted, keys stored in that instance still appear as `ACTIVE`, but are unusable. Trying to perform cryptographic operations with a key in a deleted instance results in an error.

**Warning:** After the proposed operation is approved and executed, this operation is irreversible. All resources encrypted with keys created in this instance become unrecoverable when the instance is deleted. Don't delete an instance unless you want to permanently crypto-shred all data protected by keys in this instance.

  1. Create a proposal to delete the instance using the `delete_sthi` operation type. This step requires the **Cloud KMS single-tenant HSM Proposer** role.
         
         gcloud kms single-tenant-hsm proposal create INSTANCE_ID \
                 --location LOCATION \
                 --single-tenant-hsm-instance-proposal-id PROPOSAL_ID \
                 --operation-type delete_sthi
             

Replace the following:

     * `INSTANCE_ID`: the identifier of the instance that you want to delete.
     * `LOCATION`: the location where you created the instance.
     * `PROPOSAL_ID`: the unique identifier that you want to use for this proposal—for example, `delete_instance`.
  2. View the status of the proposal and wait for its state to become `PENDING`.
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION
           

Replace the following:

     * `INSTANCE_ID`: the identifier of your instance.
     * `PROPOSAL_ID` the identifier of the proposal—for example, `delete_instance`.
     * `LOCATION`: the location where you created your instance.

When the status is `PENDING`, you can sign the challenges.

  3. Get the challenges from the proposal. 
         
         gcloud kms single-tenant-hsm proposal describe PROPOSAL_ID \
               --single_tenant_hsm_instance INSTANCE_ID \
               --location LOCATION \
               --format="json[](quorumParameters.challenges)"
           

This command returns a JSON-formatted array of challenges.

  4. For each challenge returned in the previous step, decode the challenge using `basenc --base64url -d` and sign it with a private key. 
         
         echo CHALLENGE_N | basenc --base64url -d > decoded-challenge-N.txt
           openssl dgst -sign PRIVATE_KEY_N -out signed-challenge-N.txt decoded-challenge-N.txt
           

Replace the following:

     * `N`: the number of the challenge—for example, `1` for the first challenge, `2` for the second challenge, and so on.
     * `CHALLENGE_N`: the contents of challenge number `N` from the output of the previous step.
     * `PRIVATE_KEY_N`: the path to private key number `N`—for example, `rsaprivate1.pem` for the first challenge.
  5. Approve the proposal by uploading the signed challenges. You can upload them in one command or in multiple commands. This step requires the **Cloud KMS single-tenant HSM Quorum Member** role.
         
         gcloud kms single-tenant-hsm proposal approve PROPOSAL_ID \
               --location LOCATION \
               --single_tenant_hsm_instance INSTANCE_ID \
               --quorum-challenge-replies="SIGNED_QUORUM_CHALLENGE_LIST"
           

Replace `SIGNED_QUORUM_CHALLENGE_LIST` with a JSON-formatted array of challenges, where each list item is a tuple that contains the path to the signed challenge and the path to the corresponding the public key—for example, `[('signed-challenge-1.txt','rsapub1.pem'), ('signed-challenge-2.txt','rsapub2.pem')]` to submit the first two signed challenges in one command.

After you upload the required number of signed challenges, the proposal state updates to `APPROVED`.

  6. Make sure that you want to proceed to delete the instance and crypto-shred all data encrypted using keys created in this instance, and then execute the proposal. This step requires the **Cloud KMS single-tenant HSM Executor** role, and must be completed within 24 hours after the proposal was created.

Warning: The following command is irreversible. Permanent data loss can occur. Google can't help you recover keys in a deleted instance. 
         
         gcloud kms single-tenant-hsm proposal execute  PROPOSAL_ID \
             --single_tenant_hsm_instance INSTANCE_ID --location LOCATION
             

After the operation is complete, the instance is deleted.




### Delete a proposal

If you decide not to approve or execute a proposal, you can delete the proposal before it expires. Deleting a pending proposal prevents you from approving it, and lets you create a new proposal. Deleting an approved proposal prevents you from executing the operation.

  * Delete a proposal using the `proposal delete` command. This requires the **Cloud KMS single-tenant HSM Proposer** role.
        
        gcloud kms single-tenant-hsm proposal delete PROPOSAL_ID \
                --location LOCATION \
                --single_tenant_hsm_instance INSTANCE_ID
            

Replace the following:

    * `INSTANCE_ID`: the identifier of the instance.
    * `LOCATION`: the location where you created the instance.
    * `PROPOSAL_ID`: the unique identifier of the proposal that you want to delete—for example, `proposal_to_delete`.



## What's next

  * Learn more about [Single-tenant Cloud HSM](https://docs.cloud.google.com/kms/docs/single-tenant-hsm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
