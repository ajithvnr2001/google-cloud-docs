---
url: https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints/
title: Manage NetApp Volumes resources using custom constraints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:47:00.918057+00:00
---

# Manage NetApp Volumes resources using custom constraints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage NetApp Volumes resources using custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `netapp.googleapis.com/ActiveDirectory`
  * `netapp.googleapis.com/Backup`
  * `netapp.googleapis.com/BackupPolicy`
  * `netapp.googleapis.com/BackupVault`
  * `netapp.googleapis.com/HostGroup`
  * `netapp.googleapis.com/KmsConfig`
  * `netapp.googleapis.com/QuotaRule`
  * `netapp.googleapis.com/Replication`
  * `netapp.googleapis.com/Snapshot`
  * `netapp.googleapis.com/StoragePool`
  * `netapp.googleapis.com/Volume`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Google Cloud NetApp Volumes supported resources

The following table lists the Google Cloud NetApp Volumes resources that you can reference in custom constraints. 

Resource | Field  
---|---  
netapp.googleapis.com/ActiveDirectory |  `resource.aesEncryption`  
`resource.description`  
`resource.dns`  
`resource.domain`  
`resource.encryptDcConnections`  
`resource.kdcHostname`  
`resource.kdcIp`  
`resource.ldapSigning`  
`resource.name`  
`resource.netBiosPrefix`  
`resource.nfsUsersWithLdap`  
`resource.organizationalUnit`  
`resource.site`  
netapp.googleapis.com/Backup |  `resource.description`  
`resource.name`  
`resource.ontapSource.snapshotUuid`  
`resource.ontapSource.storagePool`  
`resource.ontapSource.volumeUuid`  
`resource.sourceSnapshot`  
`resource.sourceVolume`  
netapp.googleapis.com/BackupPolicy |  `resource.dailyBackupLimit`  
`resource.description`  
`resource.enabled`  
`resource.monthlyBackupLimit`  
`resource.name`  
`resource.weeklyBackupLimit`  
netapp.googleapis.com/BackupVault |  `resource.backupRegion`  
`resource.backupRetentionPolicy.backupMinimumEnforcedRetentionDays`  
`resource.backupRetentionPolicy.dailyBackupImmutable`  
`resource.backupRetentionPolicy.manualBackupImmutable`  
`resource.backupRetentionPolicy.monthlyBackupImmutable`  
`resource.backupRetentionPolicy.weeklyBackupImmutable`  
`resource.backupVaultType`  
`resource.description`  
`resource.kmsConfig`  
`resource.name`  
`resource.sourceRegion`  
netapp.googleapis.com/HostGroup |  `resource.description`  
`resource.hosts`  
`resource.name`  
`resource.osType`  
`resource.type`  
netapp.googleapis.com/KmsConfig |  `resource.cryptoKeyName`  
`resource.description`  
`resource.name`  
netapp.googleapis.com/QuotaRule |  `resource.description`  
`resource.diskLimitMib`  
`resource.name`  
`resource.type`  
netapp.googleapis.com/Replication |  `resource.clusterLocation`  
`resource.description`  
`resource.destinationVolumeParameters.description`  
`resource.destinationVolumeParameters.shareName`  
`resource.destinationVolumeParameters.storagePool`  
`resource.destinationVolumeParameters.tieringPolicy.coolingThresholdDays`  
`resource.destinationVolumeParameters.tieringPolicy.hotTierBypassModeEnabled`  
`resource.destinationVolumeParameters.tieringPolicy.tierAction`  
`resource.destinationVolumeParameters.volumeId`  
`resource.name`  
`resource.replicationSchedule`  
netapp.googleapis.com/Snapshot |  `resource.description`  
`resource.name`  
netapp.googleapis.com/StoragePool |  `resource.activeDirectory`  
`resource.allowAutoTiering`  
`resource.capacityGib`  
`resource.customPerformanceEnabled`  
`resource.description`  
`resource.enableHotTierAutoResize`  
`resource.hotTierSizeGib`  
`resource.kmsConfig`  
`resource.ldapEnabled`  
`resource.mode`  
`resource.name`  
`resource.network`  
`resource.psaRange`  
`resource.qosType`  
`resource.replicaZone`  
`resource.scaleType`  
`resource.serviceLevel`  
`resource.totalIops`  
`resource.totalThroughputMibps`  
`resource.type`  
`resource.zone`  
netapp.googleapis.com/Volume |  `resource.backupConfig.backupPolicies`  
`resource.backupConfig.backupVault`  
`resource.backupConfig.scheduledBackupEnabled`  
`resource.blockDevices.hostGroups`  
`resource.blockDevices.name`  
`resource.blockDevices.osType`  
`resource.blockDevices.sizeGib`  
`resource.cacheParameters.cacheConfig.cachePrePopulate.excludePathList`  
`resource.cacheParameters.cacheConfig.cachePrePopulate.pathList`  
`resource.cacheParameters.cacheConfig.cachePrePopulate.recursion`  
`resource.cacheParameters.cacheConfig.cifsChangeNotifyEnabled`  
`resource.cacheParameters.cacheConfig.writebackEnabled`  
`resource.cacheParameters.enableGlobalFileLock`  
`resource.cacheParameters.peerClusterName`  
`resource.cacheParameters.peeringCommandExpiryTime`  
`resource.cacheParameters.peerIpAddresses`  
`resource.cacheParameters.peerSvmName`  
`resource.cacheParameters.peerVolumeName`  
`resource.capacityGib`  
`resource.description`  
`resource.exportPolicy.rules.accessType`  
`resource.exportPolicy.rules.allowedClients`  
`resource.exportPolicy.rules.anonUid`  
`resource.exportPolicy.rules.hasRootAccess`  
`resource.exportPolicy.rules.kerberos5iReadOnly`  
`resource.exportPolicy.rules.kerberos5iReadWrite`  
`resource.exportPolicy.rules.kerberos5pReadOnly`  
`resource.exportPolicy.rules.kerberos5pReadWrite`  
`resource.exportPolicy.rules.kerberos5ReadOnly`  
`resource.exportPolicy.rules.kerberos5ReadWrite`  
`resource.exportPolicy.rules.nfsv3`  
`resource.exportPolicy.rules.nfsv4`  
`resource.exportPolicy.rules.squashMode`  
`resource.hybridReplicationParameters.clusterLocation`  
`resource.hybridReplicationParameters.description`  
`resource.hybridReplicationParameters.hybridReplicationType`  
`resource.hybridReplicationParameters.largeVolumeConstituentCount`  
`resource.hybridReplicationParameters.peerClusterName`  
`resource.hybridReplicationParameters.peerIpAddresses`  
`resource.hybridReplicationParameters.peerSvmName`  
`resource.hybridReplicationParameters.peerVolumeName`  
`resource.hybridReplicationParameters.replication`  
`resource.hybridReplicationParameters.replicationSchedule`  
`resource.kerberosEnabled`  
`resource.largeCapacity`  
`resource.largeCapacityConfig.constituentCount`  
`resource.multipleEndpoints`  
`resource.name`  
`resource.protocols`  
`resource.restoreParameters.sourceBackup`  
`resource.restoreParameters.sourceSnapshot`  
`resource.restrictedActions`  
`resource.securityStyle`  
`resource.shareName`  
`resource.smbSettings`  
`resource.snapReserve`  
`resource.snapshotDirectory`  
`resource.snapshotPolicy.dailySchedule.hour`  
`resource.snapshotPolicy.dailySchedule.minute`  
`resource.snapshotPolicy.dailySchedule.snapshotsToKeep`  
`resource.snapshotPolicy.enabled`  
`resource.snapshotPolicy.hourlySchedule.minute`  
`resource.snapshotPolicy.hourlySchedule.snapshotsToKeep`  
`resource.snapshotPolicy.monthlySchedule.daysOfMonth`  
`resource.snapshotPolicy.monthlySchedule.hour`  
`resource.snapshotPolicy.monthlySchedule.minute`  
`resource.snapshotPolicy.monthlySchedule.snapshotsToKeep`  
`resource.snapshotPolicy.weeklySchedule.day`  
`resource.snapshotPolicy.weeklySchedule.hour`  
`resource.snapshotPolicy.weeklySchedule.minute`  
`resource.snapshotPolicy.weeklySchedule.snapshotsToKeep`  
`resource.storagePool`  
`resource.throughputMibps`  
`resource.tieringPolicy.coolingThresholdDays`  
`resource.tieringPolicy.hotTierBypassModeEnabled`  
`resource.tieringPolicy.tierAction`  
`resource.unixPermissions`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.restrictStoragePoolCapacity`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.restrictStoragePoolCapacity`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `netapp.googleapis.com/StoragePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.capacityGib <= 10240"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.restrictStoragePoolCapacity`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint and policy that lets users create a NetApp Volumes storage pool if the `capacityGib` field is less than or equal to `10240`.

### Create the constraint

  1. Save the following file as `constraint-storage-pool-capacity.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictStoragePoolCapacity
         resourceTypes: netapp.googleapis.com/StoragePool
         methodTypes:
         - CREATE
         condition: "resource.capacityGib <= 10240"
         actionType: ALLOW
         displayName: Restrict storage pool capacity
         description: Restrict storage pool capacity to 10,240 GiB.
         

Replace `ORGANIZATION_ID` with your organization ID.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint constraint-storage-pool-capacity.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT                   ACTION_TYPE  METHOD_TYPES   RESOURCE_TYPES                     DISPLAY_NAME
         custom.restrictStoragePoolCapacity  ALLOW        CREATE         netapp.googleapis.com/StoragePool  Restrict storage pool capacity
         
         ...
         




### Create the policy

  1. Save the following file as `policy-storage-pool-capacity.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.restrictStoragePoolCapacity
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy policy-storage-pool-capacity.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT                          LIST_POLICY  BOOLEAN_POLICY  ETAG
         custom.restrictStoragePoolCapacity  -            SET             CKrb785HFNjBzHF=-
         




After you apply the policy, wait for about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

  * Try creating a storage pool with the `capacityGib` field set greater than `10240`:
        
        gcloud netapp storage-pools create test-pool --location=us-central1 --service-level=standard --capacity=10241 --network=name=default --description="example description"
        

The request fails with an error similar to the following:
        
        ERROR: (gcloud.netapp.storage-pools.create) FAILED_PRECONDITION: Operation denied by custom org policy on resource 'projects/test-project/locations/us-central1/storagePools/test-pool': ["customConstraints/custom.restrictStoragePoolCapacity": "Restrict storage pool capacity to less than or equal to 10,240 GiB"].
        




## Example custom organization policies for common use cases

The following table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Deny storage pool creation or update if capacity exceeds 10,000 GiB | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictStoragePoolCapacity
        resourceTypes: netapp.googleapis.com/StoragePool
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.capacityGib > 10000"
        actionType: DENY
        displayName: Restrict storage pool capacity
        description: Prevent creation or update of storage pools with capacity greater than 10,000 GiB.  
  
Require Premium or Extreme service level for storage pools | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.enforcePremiumServiceLevel
        resourceTypes: netapp.googleapis.com/StoragePool
        methodTypes:
        - CREATE
        - UPDATE
        condition: "!(resource.serviceLevel in ['PREMIUM', 'EXTREME'])"
        actionType: DENY
        displayName: Enforce Premium or Extreme service level
        description: Make sure that the storage pools are created only for the Premium or Extreme service level.  
  
Deny volume creation or update if capacity exceeds 5,000 GiB | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictVolumeCapacity
        resourceTypes: netapp.googleapis.com/Volume
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.capacityGib > 5000"
        actionType: DENY
        displayName: Restrict volume capacity
        description: Prevent creation or update of volumes with capacity greater than 5,000 GiB.  
  
Require description for backups | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.requireBackupDescription
        resourceTypes: netapp.googleapis.com/Backup
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.description.size() == 0"
        actionType: DENY
        displayName: Require backup description
        description: Prevent creation or update of backups without a description.  
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
