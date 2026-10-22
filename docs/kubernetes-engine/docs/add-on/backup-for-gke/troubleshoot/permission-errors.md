---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors/
title: Troubleshoot permission errors in Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:56.228502+00:00
---

# Troubleshoot permission errors in Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permission-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Troubleshoot permission errors in Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes permission errors you might encounter when using Backup for GKE, things to consider when performing the action, and how to resolve the error.

## Error 100010101: Failed to backup PersistentVolumeClaim - Missing IAM binding for tenant project

Error `100010101` occurs when an attempt to back up a `PersistentVolumeClaim` fails due to a missing Identity and Access Management binding for your tenant project, resulting in an error message stating `Failed to backup PersistentVolumeClaim - Missing IAM binding for tenant project`.

Backup for GKE creates snapshots of your GKE cluster's Persistent Disk. The snapshots reside in your Google Cloud project, also known as the consumer project, and Google Cloud creates them within a tenant project that it manages. The tenant project exists within the `google.com` organization, separate from your own organization.

The service agent within the tenant project requires specific permissions to use the customer-managed encryption key (CMEK) that encrypts the Persistent Disk that is referenced by your cluster's `PersistentVolumeClaim`. This permission encrypts and decrypts the snapshot data. If the `service-TENANT_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com` service agent lacks the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on your disk's CMEK, the backup operation fails.

To resolve this error, use the following instructions:

  1. Verify that you have sufficient IAM permissions to modify IAM policies on the Cloud Key Management Service key in the Google Cloud console, such as `roles/cloudkms.admin` or `roles/owner`.

  2. Locate the tenant project's Compute Engine service agent by using the `TENANT_PROJECT_NUMBER` value that's in the `status reason` message of your failed backup operation. For example, `service-TENANT_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`.

  3. Locate the following CMEK information used for your encrypted Persistent Disk:

     * **Key name** : the name of your encryption key.

     * **Key ring** : the name of the key ring where your key resides.

     * **Location** : the Google Cloud location where your key is located. For example, `global` or `us-central1`.

  4. To grant the tenant project's Compute Engine service agent the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on your CMEK, run the `gcloud kms keys add-iam-policy-binding` command using Google Cloud CLI:
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
             --keyring KEY_RING \
             --location LOCATION \
             --member "serviceAccount:service-TENANT_PROJECT_NUMBER@compute-system.iam.gserviceaccount.com" \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

     * `KEY_NAME`: the name of your encryption key.

     * `KEY_RING`: the name of the key ring.

     * `LOCATION`: the Google Cloud location of your key. For example, `global` or `us-central1`.

     * `TENANT_PROJECT_NUMBER`: the tenant project number that you obtained from the `status reason` message of your failed backup operation.

If the command is successful, the output looks like the following:
    
    - members:
    - serviceAccount:service-987654321098@compute-system.iam.gserviceaccount.com
    role: roles/cloudkms.cryptoKeyEncrypterDecrypter
    

  5. Retest the backup operation. If the operation is still unsuccessful, contact Cloud Customer Care for further assistance.




## Error 100010104: Failed to backup PersistentVolumeClaim - Org policy constraint violation while creating snapshot

Error `100010104` occurs when an attempt to back up a `PersistentVolumeClaim` fails due to an organization policy constraint violation during snapshot creation, resulting in an error message stating `Failed to backup PersistentVolumeClaim - Org policy constraint violation while creating snapshot`.

Backup for GKE creates snapshots of your GKE cluster's Persistent Disk. The snapshots reside in your Google Cloud project, also known as the consumer project, and are created within a tenant project that is managed by Google Cloud. The tenant project exists within the `google.com` organization, separate from your own organization.

Your organization policy dictates where you can create storage resources. The `Constraint constraints/compute.storageResourceUseRestrictions violated` error means that a resource or snapshot is violating the policy by being created in a tenant project that isn't part of your allowed organizational structure. Because the tenant project is within Google's organization, it falls outside of your defined policy, which leads to the backup failure.

To resolve this error, use the following instructions:

  1. Locate the organization policy that implements the `constraints/compute.storageResourceUseRestrictions` constraint. For more information about how to view organization policies using the Google Cloud console, see [Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies).

  2. Modify the `constraints/compute.storageResourceUseRestrictions` policy to include the `folders/77620796932` tenant project folder used by Backup for GKE in its allowlist.

**Note:** Make sure the specified folder ID is added to the list of allowed locations to permit Backup for GKE to create snapshots within its tenant projects, even though they are outside your organizational hierarchy.
  3. Save the policy changes after you add the folder to the allowlist.

  4. Retest the backup operation after the organization policy updates and propagates, which usually takes a few minutes. The backup should proceed without violating the storage resource use restrictions. If the operation is still unsuccessful, contact Cloud Customer Care for further assistance.




## Error 100010106: Failed to backup PersistentVolumeClaim - Missing IAM binding for Backup for GKE service agent

Error `100010106` occurs when an attempt to back up a `PersistentVolumeClaim` fails due to a missing Identity and Access Management binding for your Backup for GKE service agent, resulting in an error message stating `Failed to backup PVC - Missing IAM binding for Backup for GKE service agent`.

Backup for GKE requires permissions to use your `BackupPlan`'s customer-managed encryption key (CMEK) for encrypting and decrypting volumes Persistent Disks. When the Backup for GKE service agent lacks the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on your `BackupPlan` CMEK, backup operations fail.

To resolve this error, use the following instructions:

  1. Identify the Google-managed Backup for GKE service agent specific to your project. For example, `service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com`. You can find your project number by using the following methods:

     * Use the Google Cloud project dashboard in the Google Cloud console.

     * Run the `gcloud projects describe` command using Google Cloud CLI:
           
           gcloud projects describe PROJECT_ID –format="value(projectNumber)"
           

Replace `PROJECT_ID` with the unique name of your project.

  2. Identify the following CMEK details:

     * **Key name** : the name of your encryption key.

     * **Key ring** : the name of the key ring where your key resides.

     * **Location** : the Google Cloud location where your `BackupPlan` CMEK is located. For example, `global` or `us-central1`.

  3. To grant the Backup for GKE service agent the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on your CMEK, use Google Cloud CLI to run the `gcloud kms keys add-iam-policy-binding` command:
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
             --keyring KEY_RING \
             --location LOCATION \
             --member "serviceAccount:service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com" \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

     * `KEY_NAME`: the name of your encryption key.

     * `KEY_RING`: the name of the key ring.

     * `LOCATION`: the Google Cloud location of your key. For example, `global` or `us-central1`.

     * `PROJECT_NUMBER`: your Google Cloud project number.

  4. Verify that you have the required Identity and Access Management permissions on the Cloud Key Management Service key. For example, `roles/cloudkms.admin` or `roles/owner`.

  5. Verify that you have the granted permissions. In the output of the previous `gcloud kms keys add-iam-policy-binding` command, look for an entry similar to the following:
         
         -members:
         -serviceAccount:service-123456789012@gcp-sa-gkebackup.iam.gserviceaccount.com
         role: roles/cloudkms.cryptoKeyEncrypterDecrypter
         

  6. Retest the backup operation after you grant the necessary permissions. If the operation doesn't complete successfully, contact Cloud Customer Care for further assistance.




## Error 100010107: Failed to backup PersistentVolumeClaim - Missing IAM binding - agent service account (KCP)

Error `100010107` occurs when you try to perform a Backup for GKE backup operation and the Google Kubernetes Engine cluster service agent doesn't have access to your customer-managed encryption key (CMEK), resulting in a message stating `Failed to backup PVC - Missing IAM binding - agent service account (KCP)`.

The Google Kubernetes Engine cluster service agent, typically in the format of `service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`, is essential for your GKE cluster to interact with Google Cloud services. When your backup plan uses a customer-managed encryption key (CMEK). This service agent needs permissions to encrypt and decrypt your backup data using your CMEK. If the backup plan is missing the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on your CMEK, backup operations initiated from the cluster fail with a `permission denied` error.

To resolve this error, use the following troubleshooting instructions:

  1. Verify that you have the correct permissions to modify IAM policies on the Cloud Key Management Service key. For example, `cloudkms.admin` or `roles/owner`.

  2. Identify the Google Kubernetes Engine cluster service agent. This service agent is automatically created and managed by Google Cloud for your GKE clusters. For example, `service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com`. You need the project number to put together the full service account. You can find your project number by using one of the following methods:

     * Use the Google Cloud project dashboard in the Google Cloud console.

     * Run the `gcloud projects describe` command using Google Cloud CLI:
           
           gcloud projects describe PROJECT_ID –-format="value(projectNumber)"
           

Replace `PROJECT_ID` with your project ID.

  3. Locate the following CMEK information:

     * **Key name** : the name of your encryption key.

     * **Key ring** : the name of the key ring where your key resides.

     * **Location** : the Google Cloud location where your key is located. For example, `global` or `us-central1`.

  4. Grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role at the CMEK level. The Google Kubernetes Engine service agent needs permissions on your encryption key. To grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on your CMEK, use Google Cloud CLI to run the `gcloud kms key add-iam-policy-binding` command:
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
             --keyring KEY_RING \
             --location LOCATION \
             --member "serviceAccount:service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter
         

Replace the following:

     * `KEY_NAME`: the name of your encryption key.

     * `KEY_RING`: the name of the key ring.

     * `LOCATION`: the Google Cloud location of your key. For example, `global` or `us-central1`.

     * `PROJECT_NUMBER`: the name of the project.

The output is similar to the following:
    
    - members:
     - serviceAccount:service-123456789012@container-engine-robot.iam.gserviceaccount.com
     role: roles/cloudkms.cryptoKeyEncrypterDecrypter
     ```
    

  5. Re-attempt the Backup for GKE operation. If the operation continues to fail, contact Cloud Customer Care for further assistance.




## Error 100010109: Failed to backup PersistentVolumeClaim - Target backup region not permitted by DiskSettings policy

Error `100010109` occurs when the target backup region isn't permitted by your `DiskSettings` access location policy.

### Understanding the Error

This error occurs when the customer has a `DiskSettings` access location policy set to `SPECIFIC_REGIONS` for some disk locations referenced in the cluster that are being backed up. Because this access location policy only allows specific regions to be valid snapshot creation locations, the backup is rejected if the target storage location falls outside of this list. When this happens, snapshot creation fails with a message similar to the following:
    
    
    No permission to read source disk in us-central1 from target snapshot in us-east1.
    

### Troubleshooting Steps

  1. **Identify the source and target regions** : Review the error message to find the source disk location (for example, `us-central1`) and the target snapshot region (for example, `us-east1`) that was denied.
  2. **Update the DiskSettings policy** : To fix the issue, you must update the `DiskSettings` to allow the target storage location for the disk locations referenced in your cluster. You can achieve this by adding the target region to the access locations allowlist using the Google Cloud CLI.

     * For a zonal disk (for example, adding `us-east1` as allowed for disks in `us-central1-a`):
           
           gcloud beta compute disk-settings update --access-location-policy=specific-regions --add-access-locations=us-east1 --zone=us-central1-a
           

     * For a regional disk (for example, adding `us-east1` as allowed for disks in `us-central1`):
           
           gcloud beta compute disk-settings update --access-location-policy=specific-regions --add-access-locations=us-east1 --region=us-central1
           

  3. **Retest the Backup Operation** : After updating the `DiskSettings` to permit the target backup region, reattempt the backup operation.




## Error 100020101: Failure to backup PersistentVolumeClaim - PersistentVolumeClaim bound to an unsupported PersistentVolume type

Error `100020101` occurs when an attempt to back up a `PersistentVolumeClaim` fails because the `PersistentVolumeClaim` is bound to an unsupported `PersistentVolume` type. The error results in the following error message: `PersistentVolumeClaims are bound to PersistentVolumes of unsupported types and cannot be backed up.`

This error occurs when your Backup for GKE operation encounters a `PersistentVolumeClaim` that is bound to a `PersistentVolume` that uses volume type that isn't supported for data backup by Backup for GKE. Backup for GKE primarily supports backing up data from Persistent Disk volumes. If a `PersistentVolumeClaim` is bound to a `PersistentVolume` that isn't a Persistent Disk, the backup operation fails for the `PersistentVolumeClaim`'s data.

To resolve this error, use the following troubleshooting instructions:

  1. List all of the `PersistentVolumeClaims` and the `PersistentVolumes` that are bound to them by running the `kubectl get pvc` command. Review this list to identify the `PersistentVolumes` that are backed by unsupported volume types.
         
         kubectl get pvc --all-namespaces -o wide
         

  2. Determine the volume type of the `PersistentVolume` that is backed by a volume type not supported by Backup for GKE by running the `kubectl describe pv` command:
         
         kubectl describe pv PERSISTENT_VOLUME_NAME
         

Replace the following:

`PERSISTENT_VOLUME_NAME`: the name of `PersistentVolume` that has an unsupported volume type listed as column `VOLUME` in the output from the previous step.

In the output, use the `Source` and `Driver` fields to get volume provisioner details:

     * **For supported Persistent Disks** : the output looks similar to `Source.Driver: pd.csi.storage.gke.io` or `Source.Type:GCEPersistentDisk`.

     * **For unsupported types that are causing the error** : the output would be a non-Persistent Disk driver, for example, `Source.Driver:filestore.csi.storage.gke.io`.

  3. Use one of the following methods to resolve the error:

     * **Migrate to a Persistent Disk volume** : we recommend this method for full data backups. If you need to back up the actual volume data, you must use a Persistent Disk, which involves migrating your data from the unsupported volume type to a new Persistent Disk CSI volume. For assistance with migrating a Persistent Disk volume, contact Cloud Customer Care.

     * **Enable permissive mode in Backup for GKE** : we recommend this method if data backup isn't required for unsupported volumes. If migrating data isn't feasible or necessary—for example, if the volume is backed by an external service and you plan to reattach it during the restore operation—you can configure your Backup for GKE backup plan to allow the backup to proceed in permissive mode. For more information about how to enable permissive mode, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).

  4. Re-attempt the Backup for GKE operation. Based on the method you chose to resolve the error, the Backup for GKE operation behaves in the following ways:

     * If you migrated to a Persistent Disk volume, the backup should succeed for the volume, including its data.

     * If you enabled permissive mode, the backup operation should succeed, but the data for unsupported volumes isn't backed up.




If the operation continues to fail, contact Cloud Customer Care for further assistance.

## Error 100020104: Failure to backup PersistentVolumeClaim - PersistentVolumeClaim not bound to a PersistentVolume

Error `100020104` occurs when an attempt to back up a `PersistentVolumeClaim` fails because the `PersistentVolumeClaim` isn't bound to a `PersistentVolume`. The error results in the following error message: `Failed to backup PVC - PVC Not Bound to a Persistent Volume`.

This error occurs when your Backup for GKE operation attempts to back up a `PersistentVolumeClaim` that isn't successfully bound to a `PersistentVolume`. A `PersistentVolumeClaim` must be bound to a `PersistentVolume` before it can be used by a consuming workload, such as a Pod, and subsequently backed up by Backup for GKE. If the `PersistentVolumeClaim` remains in a `Pending` state, it signifies that a suitable `PersistentVolume` isn't available or can't be provisioned or bound, which leads to the backup operation's failure. A common reason for a `PersistentVolumeClaim` to remain unbound is when its associated `StorageClass` uses a `WaitForFirstConsumer` binding mode, but no Pod or other workload is yet trying to consume the `PersistentVolumeClaim`.

To resolve this error, use the following troubleshooting instructions:

  1. To check the status of all `PersistentVolumeClaims` in the cluster and identify the unbound `PersistentVolumeClaim`, run the `kubectl get pvc` command:
         
         kubectl get pvc --all-namespaces | grep `Pending`
         

  2. After you identify the `PersistentVolumeClaim` that isn't bound to a `PersistentVolume`, retrieve information about the unbound `PersistentVolumeClaim` by running the `kubectl describe pvc` command:
         
         kubectl describe pvc PVC_NAME -n NAMESPACE_NAME
         

Replace the following:

     * `PVC_NAME`: the name of the `PersistentVolumeClaim` that failed to back up.

     * `NAMESPACE_NAME`: the name of your namespace where the `PersistentVolumeClaim` resides.

After the description appears, use the `Status` and `Events` fields to determine if the `PersistentVolumeClaim` is bound to a `PersistentVolume`. If you're still unable to determine why the `PersistentVolumeClaim` isn't bound to a `PersistentVolume` or you're unable to resolve the identified issue, you can enable permissive mode on your backup plan. For more information about how to enable permissive mode, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).




## What's next

  * [Read the Backup for GKE error codes overview page](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
