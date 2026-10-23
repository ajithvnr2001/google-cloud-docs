---
url: https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy/
title: Add custom organization policies \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:56.855382+00:00
---

# Add custom organization policies  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/org-policy/custom-org-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Add custom organization policies Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/org-policy/custom-org-policy "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/org-policy/custom-org-policy "View this page for the SQL Server database engine")

This page describes how to create, set up, and manage custom constraints in Cloud SQL instances. For an overview of custom organization policies, see [custom organization policies](https://docs.cloud.google.com/sql/docs/mysql/org-policy/org-policy#custom_constraints).

## Cloud SQL supported resources

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `sqladmin.googleapis.com/Instance`
  * `sqladmin.googleapis.com/BackupRun`



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

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

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

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Cloud SQL for MySQL supported resources

The following table lists the Cloud SQL for MySQL resources that you can reference in custom constraints. 

Resource | Field  
---|---  
sqladmin.googleapis.com/BackupRun |  `resource.description`  
`resource.location`  
sqladmin.googleapis.com/Instance |  `resource.databaseVersion`  
`resource.diskEncryptionConfiguration.kmsKeyName`  
`resource.diskEncryptionStatus.kmsKeyVersionName`  
`resource.failoverReplica.name`  
`resource.masterInstanceName`  
`resource.name`  
`resource.nodeCount`  
`resource.project`  
`resource.region`  
`resource.replicaConfiguration.cascadableReplica`  
`resource.replicaConfiguration.failoverTarget`  
`resource.settings.activationPolicy`  
`resource.settings.activeDirectoryConfig.domain`  
`resource.settings.advancedMachineFeatures.threadsPerCore`  
`resource.settings.availabilityType`  
`resource.settings.backupConfiguration.backupRetentionSettings.retainedBackups`  
`resource.settings.backupConfiguration.backupRetentionSettings.retentionUnit`  
`resource.settings.backupConfiguration.binaryLogEnabled`  
`resource.settings.backupConfiguration.enabled`  
`resource.settings.backupConfiguration.location`  
`resource.settings.backupConfiguration.pointInTimeRecoveryEnabled`  
`resource.settings.backupConfiguration.startTime`  
`resource.settings.backupConfiguration.transactionLogRetentionDays`  
`resource.settings.collation`  
`resource.settings.connectionPoolConfig.connectionPoolingEnabled`  
`resource.settings.connectionPoolConfig.flags.name`  
`resource.settings.connectionPoolConfig.flags.value`  
`resource.settings.connectorEnforcement`  
`resource.settings.databaseFlags.name`  
`resource.settings.databaseFlags.value`  
`resource.settings.dataCacheConfig.dataCacheEnabled`  
`resource.settings.dataDiskProvisionedIops`  
`resource.settings.dataDiskProvisionedThroughput`  
`resource.settings.dataDiskSizeGb`  
`resource.settings.dataDiskType`  
`resource.settings.deletionProtectionEnabled`  
`resource.settings.denyMaintenancePeriods.endDate`  
`resource.settings.denyMaintenancePeriods.startDate`  
`resource.settings.denyMaintenancePeriods.time`  
`resource.settings.edition`  
`resource.settings.enableDataplexIntegration`  
`resource.settings.enableGoogleMlIntegration`  
`resource.settings.insightsConfig.queryInsightsEnabled`  
`resource.settings.insightsConfig.queryPlansPerMinute`  
`resource.settings.insightsConfig.queryStringLength`  
`resource.settings.insightsConfig.recordApplicationTags`  
`resource.settings.insightsConfig.recordClientAddress`  
`resource.settings.ipConfiguration.authorizedNetworks.name`  
`resource.settings.ipConfiguration.authorizedNetworks.value`  
`resource.settings.ipConfiguration.customSubjectAlternativeNames`  
`resource.settings.ipConfiguration.enablePrivatePathForGoogleCloudServices`  
`resource.settings.ipConfiguration.ipv4Enabled`  
`resource.settings.ipConfiguration.privateNetwork`  
`resource.settings.ipConfiguration.pscConfig.allowedConsumerProjects`  
`resource.settings.ipConfiguration.pscConfig.pscAutoConnections.consumerNetwork`  
`resource.settings.ipConfiguration.pscConfig.pscAutoConnections.consumerProject`  
`resource.settings.ipConfiguration.pscConfig.pscEnabled`  
`resource.settings.ipConfiguration.serverCaMode`  
`resource.settings.ipConfiguration.serverCaPool`  
`resource.settings.ipConfiguration.sslMode`  
`resource.settings.locationPreference.secondaryZone`  
`resource.settings.locationPreference.zone`  
`resource.settings.maintenanceWindow.day`  
`resource.settings.maintenanceWindow.hour`  
`resource.settings.maintenanceWindow.updateTrack`  
`resource.settings.passwordValidationPolicy.complexity`  
`resource.settings.passwordValidationPolicy.disallowUsernameSubstring`  
`resource.settings.passwordValidationPolicy.enablePasswordPolicy`  
`resource.settings.passwordValidationPolicy.minLength`  
`resource.settings.passwordValidationPolicy.passwordChangeInterval`  
`resource.settings.passwordValidationPolicy.reuseInterval`  
`resource.settings.replicationLagMaxSeconds`  
`resource.settings.retainBackupsOnDelete`  
`resource.settings.sqlServerAuditConfig.bucket`  
`resource.settings.sqlServerAuditConfig.retentionInterval`  
`resource.settings.sqlServerAuditConfig.uploadInterval`  
`resource.settings.storageAutoResize`  
`resource.settings.tier`  
`resource.settings.timeZone`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.region`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.region`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `sqladmin.googleapis.com/Instance`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.region == "us-central1""`. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.region`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Ensure that instances are Enterprise Plus | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.edition
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.edition == 'ENTERPRISE_PLUS'"
        actionType: ALLOW
        displayName: Instances must be Enterprise Plus.
        description: Cloud SQL instances must be Enterprise Plus.
          
  
Ensure instances are highly available | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.availability
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.availabilityType == 'REGIONAL'"
        actionType: ALLOW
        displayName: Instances must be regional.
        description: Cloud SQL instances must be highly available. To do this, make them regional.
          
  
Ensure that instances have a password policy. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.enforcePassword
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.passwordValidationPolicy.enablePasswordPolicy == true"
        actionType: ALLOW
        displayName: The password policy must be enabled for Cloud SQL instances.
        description: Cloud SQL instances must have a password policy.
          
  
Ensure that the password policy for instances has a minimum length | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.passwordMinLength
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.passwordValidationPolicy.minLength >= 6"
        actionType: ALLOW
        displayName: The password policy must have a minimum length of six characters.
        description: Cloud SQL instances must have a password policy that has a minimum length of six characters.
          
  
Ensure that instances have password policy complexity enabled. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.passwordComplexity
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.passwordValidationPolicy.complexity == 'COMPLEXITY_DEFAULT'"
        actionType: ALLOW
        displayName: The password policy complexity must be enabled.
        description: Cloud SQL instances must have a password policy with complex passwords.
          
  
Require the SSL Mode to be enabled with encrypted connections only. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.sslMode
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.ipConfiguration.sslMode == 'ENCRYPTED_ONLY'"
        actionType: ALLOW
        displayName: Only allow connections that are encrypted with SSL/TLS.
        description: Cloud SQL instances must only allow connections that are encrypted with SSL/TLS.
          
  
Block database access from anywhere in the public internet. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.authorizedNetworks
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.ipConfiguration.authorizedNetworks.exists(network, network.value == '0.0.0.0/0')"
        actionType: DENY
        displayName: The list of authorized networks can't contain 0.0.0.0/0
        description: Authorized networks for Cloud SQL instances can't contain 0.0.0.0/0. This allows users to access the database from any IP address.
          
  
Ensure that instances aren't created with an external IP address. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.ipv4Enabled
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.ipConfiguration.ipv4Enabled == false"
        actionType: ALLOW
        displayName: ipv4Enabled must be set to false.
        description: Cloud SQL instances can't have an external IP address.
          
  
Ensure that instances are encrypted with a KMS key. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.encrypted
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.diskEncryptionConfiguration.kmsKeyName.size() > 0"
        actionType: ALLOW
        displayName: Instances must be encrypted with a KMS key.
        description: Cloud SQL instances must be disk-encrypted with a KMS key.
          
  
Ensure Instances are in the us-central1 | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.region
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.region == 'us-central1'"
        actionType: ALLOW
        displayName: Instances must be in the us-central1 region.
        description: Cloud SQL instances must be in the us-central1 region.
          
  
Ensure that instances have data cache enabled. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.dataCache
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.dataCacheConfig.dataCacheEnabled == true"
        actionType: ALLOW
        displayName: Instances must have data cache enabled.
        description: Cloud SQL instances must have data cache enabled.
          
  
Enforce automated backups. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.enableBackups
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.backupConfiguration.enabled == true"
        actionType: ALLOW
        displayName: Automated backups must be enabled.
        description: Cloud SQL instances must have automated backups enabled.
          
  
Restrict the location of automated backups. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.automatedBackupLocation
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.settings.backupConfiguration.location == 'us-central1'"
        actionType: ALLOW
        displayName: The location of automated backups must be in the us-central1 region.
        description: The location of automated backups for Cloud SQL instances must be in the us-central1 region.
          
  
Restrict the location of on-demand backups to us-central1 | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.onDemandBackupLocation
        resourceTypes:
        - sqladmin.googleapis.com/BackupRun
        methodTypes:
        - CREATE
        - UPDATE
        condition: "condition: resource.location == 'us-central1'"
        actionType: ALLOW
        displayName: The location of on-demand backups must be in the us-central1 region.
        description: On-demand backups are restricted to the us-central1.
          
  
Enforce a final backup at instance deletion | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.retainBackupsOnDelete
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "condition: resource.settings.finalBackupConfig.enabled == true"
        actionType: ALLOW
        displayName: Final backup is enabled and must be taken at instance deletion.
        description: Final backups are enabled for instance.
          
  
Enforce a final backup at instance deletion retention period | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.retainBackupsOnDelete
        resourceTypes:
        - sqladmin.googleapis.com/Instance
        methodTypes:
        - CREATE
        - UPDATE
        condition: "condition: resource.settings.finalBackupConfig.enabled == true && resource.settings.finalBackupConfig.retentionDays == 20"
        actionType: ALLOW
        displayName: Final backup is enabled and must be retained for 20 days after
        instance deletion.
        description: Final backups is retained for 20 days after instance deletion.
          
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
