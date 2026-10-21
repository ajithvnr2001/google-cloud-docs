---
url: https://docs.cloud.google.com/compute/docs/access/custom-constraints/
title: Custom constraints \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:53.952840+00:00
---

# Custom constraints  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `compute.googleapis.com/Disk`
  * `compute.googleapis.com/Image`
  * `compute.googleapis.com/Instance`
  * `compute.googleapis.com/InstanceGroup`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

### Benefits

  * **_Cost management_** : use custom organization policies to restrict the virtual machine (VM) instance and disk sizes and types that can be used in your organization. You can also restrict the machine family that is used for the VM instance
  * **_Security, compliance, and governance_** : you can use custom organization policies to enforce policies as follows: 
    * To enforce security requirements, you can require specific firewall port rules on VMs.
    * To support hardware isolation or licensing compliance, you can require all VMs within a specific project or folder to run on [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
    * To govern automation scripts, you can use custom organization policies to verify that labels match specified expressions.



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

To get the permissions that you need to manage organization policies for Compute Engine resources, ask your administrator to grant you the following IAM roles: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization resource
  * To test the constraints: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policies for Compute Engine resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies for Compute Engine resources:

  * `orgpolicy.constraints.list`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`
  * To test the constraints: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Compute Engine supported resources

For Compute Engine, you can set custom constraints on the following resources and fields.

Resource | Field  
---|---  
compute.googleapis.com/Disk |  `resource.enableConfidentialCompute`  
`resource.licenseCodes`  
`resource.licenses`  
`resource.sizeGb`  
`resource.sourceImage`  
`resource.type`  
compute.googleapis.com/Image |  `resource.rawDisk.source`  
compute.googleapis.com/Instance |  `resource.advancedMachineFeatures.enableNestedVirtualization`  
`resource.advancedMachineFeatures.performanceMonitoringUnit`  
`resource.advancedMachineFeatures.threadsPerCore`  
`resource.canIpForward`  
`resource.confidentialInstanceConfig.confidentialInstanceType`  
`resource.confidentialInstanceConfig.enableConfidentialCompute`  
`resource.deletionProtection`  
`resource.guestAccelerators.acceleratorCount`  
`resource.guestAccelerators.acceleratorType`  
`resource.labels`  
`resource.machineType`  
`resource.minCpuPlatform`  
`resource.networkInterfaces.accessConfigs.name`  
`resource.networkInterfaces.accessConfigs.natIP`  
`resource.networkInterfaces.network`  
`resource.networkInterfaces.networkAttachment`  
`resource.networkInterfaces.subnetwork`  
`resource.privateIpv6GoogleAccess`  
`resource.resourceStatus.effectiveInstanceMetadata.blockProjectSshKeysMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.enableGuestAttributesMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.enableOsconfigMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.enableOsInventoryMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.enableOsloginMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.serialPortEnableMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.serialPortLoggingEnableMetadataValue`  
`resource.resourceStatus.effectiveInstanceMetadata.vmDnsSettingMetadataValue`  
`resource.scheduling.nodeAffinities.key`  
`resource.scheduling.nodeAffinities.operator`  
`resource.scheduling.nodeAffinities.values`  
`resource.selfLink`  
`resource.shieldedInstanceConfig.enableIntegrityMonitoring`  
`resource.shieldedInstanceConfig.enableSecureBoot`  
`resource.shieldedInstanceConfig.enableVtpm`  
`resource.zone`  
compute.googleapis.com/InstanceGroup |  `resource.description`  
`resource.name`  
`resource.namedPorts.name`  
`resource.namedPorts.port`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.createOnlyN2DVMs`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.createOnlyN2DVMs`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `compute.googleapis.com/Instance`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.machineType.contains('/machineTypes/n2d')"`. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.createOnlyN2DVMs`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint that restricts VMs to use the N2D machine type.

### Create the custom constraint

  1. To define a custom constraint, create a file named `onlyN2DVMs.yaml`.
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.createOnlyN2DVMs
         resourceTypes: compute.googleapis.com/Instance
         condition: "resource.machineType.contains('/machineTypes/n2d')"
         actionType: ALLOW
         methodTypes: CREATE
         displayName: Only N2D VMs allowed
         description: Restrict all VMs created to only use N2D machine types.

Replace ORGANIZATION_ID with your organization ID.

  2. Apply the custom constraint.
         
         gcloud org-policies set-custom-constraint onlyN2DVMs.yaml
         




### Create the organization policy

  1. To define an organization policy, create a file named `onlyN2DVMs-policy.yaml`. In this example we enforce this constraint at the project level but you might also set this at the organization or folder level.
         
         name: projects/PROJECT_ID/policies/custom.createOnlyN2DVMs
         spec:
           rules:
           – enforce: true

Replace `PROJECT_ID` with your project ID.

  2. Enforce the organization policy.
         
         gcloud org-policies set-policy onlyN2DVMs-policy.yaml
         




### Test the policy

  1. Test the constraint by trying to create a VM that uses a machine type that isn't an N2D machine.
         
         gcloud compute instances create my-test-instance \
             --project=PROJECT_ID \
             --zone=us-central1-c \
             --machine-type=e2-medium
         

The operation is disallowed and the output is similar to the following:
         
         ERROR: (gcloud.compute.instances.create) Could not fetch resource:
         – Operation denied by custom org policies: [customConstraints/custom.createOnlyN2DVMs]: Restrict all VMs created to only use N2D machine types.
         




## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
  
Persistent Disk type must be "Extreme persistent disk (`pd-extreme`)" | 
    
    
      name: organizations/ORGANIZATION_ID/customConstraints/custom.createDisksPDExtremeOnly
      resourceTypes: compute.googleapis.com/Disk
      condition: "resource.type.contains('pd-extreme')"
      actionType: ALLOW
      methodTypes: CREATE
      displayName: Create pd-extreme disks only
      description: Only the extreme persistent disk type is allowed to be created.  
  
Disk size must be less than or equal to 250 GB | 
    
    
      name: organizations/ORGANIZATION_ID/customConstraints/custom.createDisksLessThan250GB
      resourceTypes: compute.googleapis.com/Disk
      condition: "resource.sizeGb <= 250"
      actionType: ALLOW
      methodTypes: CREATE
      displayName: Disks size maximum is 250 GB
      description: Restrict the boot disk size to 250 GB or less for all VMs.  
  
Source images must be from Cloud Storage `test_bucket` only | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.createDisksfromStoragebucket
    resourceTypes: compute.googleapis.com/Image
    condition: "resource.rawDisk.source.contains('storage.googleapis.com/test_bucket/')"
    actionType: ALLOW
    methodTypes: CREATE
    displayName: Source image must be from Cloud Storage test_bucket only
    description: Source images used in this project must be imported from the
    Cloud Storage test_bucket.  
  
VM must have a label with the key set to `cost center` | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.createVMWithLabel
    resourceTypes: compute.googleapis.com/Instance
    condition: "'cost_center' in resource.labels"
    actionType: ALLOW
    methodTypes: CREATE
    displayName: 'cost_center' label required
    description: Requires that all VMs created must have a 'cost_center' label
    that can be used for tracking and billing purposes.  
  
VM must have a label with the key set to `cost center` and the value set to `eCommerce` | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.createECommerceVMOnly
    resourceTypes: compute.googleapis.com/Instance
    condition: "'cost_center' in resource.labels and resource.labels['cost_center'] == 'eCommerce'"
    actionType: ALLOW
    methodTypes: CREATE
    displayName:  Label (cost_center/eCommerce) required
    description: Label required and Key/value must be cost_center/eCommerce.  
  
VM must use machine type N2D | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.createOnlyN2DVMs
    resourceTypes: compute.googleapis.com/Instance
    condition: "resource.machineType.contains('/machineTypes/n2d')"
    actionType: ALLOW
    methodTypes: CREATE
    displayName: Only N2D VMs allowed
    description: Restrict all VMs created to only use N2D machine types.  
  
VM must use machine type `e2-highmem-8` | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.createOnlyE2highmem8
    resourceTypes: compute.googleapis.com/Instance
    condition: "resource.machineType.endsWith('-e2-highmem-8')"
    actionType: ALLOW
    methodTypes: CREATE
    displayName: Only "e2-highmem-8" VMs allowed
    description: Restrict all VMs created to only use the E2 high-memory
    machine types that have 8 vCPUs.  
  
Ensures that VMs are scheduled on the node group "foo" | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.createOnlySTVM
    resourceTypes: compute.googleapis.com/Instance
    condition: "resource.scheduling.nodeAffinities.exists(n, n.key == 'foo')"
    actionType: ALLOW
    methodTypes: CREATE
    displayName: Only VMs scheduled on node group "foo" allowed
    description: Restrict all VMs created to use the node group "foo".  
  
Deny exposure of host IDs on VMs | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.disableHostIdExposure
    resourceTypes: compute.googleapis.com/Instance
    condition: "resource.scheduling.exposeHostTopology == true"
    actionType: DENY
    methodTypes:
    - CREATE
    - UPDATE
    displayName: Disable host ID exposure
    description: Prevents enabling the exposure of the host IDs on which your VMs
    run.  
  
## Enforcing Mandatory Resource Manager Tags

Some Compute Engine resources also support the `GOVERN_TAGS` type constraint to enforce mandatory Resource Manager tags on the Compute Engine resource. For more information, see [Enforcement of mandatory tags using organization policies](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#enforce_tags).

## Pricing

The Organization Policy Service, including predefined and custom organization policies, is offered at no charge.

## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
