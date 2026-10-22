---
url: https://docs.cloud.google.com/compute/docs/access/managed-constraints/
title: Managed constraints \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:36.899179+00:00
---

# Managed constraints  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/managed-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Managed constraints Stay organized with collections  Save and categorize content based on your preferences. 

Managed constraints are predefined organization policies, built on a modern platform, that provide centralized, programmatic control over your Compute Engine resources. They include built-in support for safe rollout tools like Policy Simulator and dry run.

Managed constraints are identifiable by the `compute.managed.*` prefix and serve as a direct replacement for legacy `compute.*` constraints.

## Benefits

  * **Safe rollout and monitoring** : Implement policies with full tooling, faster change control, and deploy gradually using simulation and dry-run capabilities.
  * **Consistent logging** : Enforces uniformity in logging and error messages, simplifying centralized monitoring and streamlining audits.



## Policy inheritance

Organization policies that you set on a resource are inherited by that resource's descendants in the resource hierarchy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in that folder.

## Pricing

The Organization Policy Service, including predefined (legacy), managed, and custom organization policies, is offered at no charge.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 



  * Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * If you haven't already, [install](https://docs.cloud.google.com/sdk/docs/install) the gcloud CLI and initialize it by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init).
  * Set a default project for your testing.



### Required roles

To get the permissions that you need to manage organization policies with managed constraints, ask your administrator to grant you the following IAM roles: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization resource
  * To test the constraints: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policies with managed constraints. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies with managed constraints:

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

## Available managed constraints

The following managed organization policy constraints are available for Compute Engine:

Constraint | Description  
---|---  
Allowed VLAN Attachment encryption settings |  This list constraint defines the allowed encryption settings for new VLAN Attachments.   
By default, VLAN Attachments are allowed to use any encryption settings.   
Set IPSEC as the allowed value to enforce creating encrypted VLAN attachments only. `constraints/compute.managed.allowedVlanAttachmentEncryption`  
Block Compute Engine Preview Features |  This constraint blocks Compute Engine preview features by default. You can explicitly allow specific preview features by adding them to the allowedPreviewFeatures list. Alternatively, you can disable the constraint (set to not enforced) to allow all preview features. After a preview feature is allowed (either by using the allowed list or by disabling the constraint), it must also be enabled for the project before it can be used. Subsequently enforcing the constraint does not change the status of individual preview features already set. This constraint only applies to Compute Alpha API features. `constraints/compute.managed.blockPreviewFeatures`  
Block Project-wide SSH Keys |  Preview: This constraint prevents the block-project-ssh-keys metadata key from being set to false at the project, project-zonal, or instance level for Compute Engine VMs within the organization, project, or folder where this constraint is enforced. By default, [project-wide SSH keys](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys) are allowed and can be disabled at the project, project-zonal, or instance level using this metadata key. To allow project-wide SSH keys for specific VMs, you can exempt them from this policy using tags and conditional rules.  
Important: Enforcing this constraint does not affect existing VMs where block-project-ssh-keys is already set to false; they will retain access unless their metadata is updated. `constraints/compute.managed.blockProjectSshKeys`  
Disable Guest Attributes of Compute Engine metadata |  Preview: This constraint, when enforced, disables Compute Engine API access to the [Guest Attributes](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#guest_attributes) of Compute Engine VMs.   
By default, the Compute Engine API can be used to access Compute Engine VM guest attributes.  
You can allow specific VM instances to use guest attributes. First apply tags to mark the instances, and then use conditional rules based on tag values to properly scope those instances out of enforcement. `constraints/compute.managed.disableGuestAttributesAccess`  
Disable VM Nested Virtualization |  This boolean constraint disables hardware-accelerated nestedvirtualization for all Compute Engine VMs belonging to the organization, project, or folder where this constraint is set to `True`.  
By default, hardware-accelerated nested virtualization is allowed for all Compute Engine VMs running on Intel Haswell or newer CPU platforms.   
`constraints/compute.managed.disableNestedVirtualization`  
Disable Non-FIPS Compliant Machine Types |  Preview: This constraint, when enforced, prevents the creation or update of VM instances using machine types that are not FIPS compliant. By default, all machine types are allowed. You can exempt specific VMs using tags and conditional rules. `constraints/compute.managed.disableNonFIPSMachineTypes`  
Restrict enabling VM serial port access metadata |  This constraint prevents the serial-port-enable metadata key from being set to true for Compute Engine VMs within the organization, project, or folder where this constraint is enforced. By default, serial port access can be enabled on a per-VM, per-zone, or per-project basis using this metadata key. To allow serial port access for specific VMs, you can exempt them from this policy using tags and conditional rules.  
Important: Enforcing this constraint does not affect existing VMs where serial-port-enable is already set to true; they will retain access unless their metadata is updated. `constraints/compute.managed.disableSerialPortAccess`  
Disable VM serial port logging to Stackdriver |  This constraint, when enforced, disables serial port logging to Stackdriver from Compute Engine VMs.  
By default, serial port logging for Compute Engine VMs is disabled, and can be selectively enabled on a per-VM or per-project basis using [metadata attributes](https://cloud.google.com/compute/docs/instances/viewing-serial-port-output#enable-stackdriver). Disabling serial port logging can cause certain services that rely on it, such as Google Kubernetes Engine clusters, to not function correctly. Before you enforce this constraint, verify that the products in your project do not rely on serial port logging. You can allow specific VM instances to use serial port logging. First apply tags to mark the instances, and then use conditional rules based on tag values to properly scope those instances out of enforcement. `constraints/compute.managed.disableSerialPortLogging`  
Disable creation of Compute Engine instances that use the deprecated container startup agent (konlet). |  Preview: This boolean constraint prevents the creation of Compute Engine instances that use konlet, the deprecated container startup agent. When enabled, you can't create compute instances that have the `gce-container-declaration` metadata key.This constraint also prevents creation of compute instances from instance templates that contain the `gce-container-declaration` metadata key, which affects managed instance groups (MIGs) that use such instance templates. `constraints/compute.managed.disableVmsWithContainerStartupAgent`  
Restricts usage of Global Internal DNS (gDNS) for projects that have a ZonalOnly DNS setting. |  This constraint, when enforced, restricts gDNS usage. This restriction disables gDNS VM creation and updating VMs to use gDNS. You can revert a zDNS project to gDNS, but this results in policy violation enforcement during subsequent Instance API invocations. Note: This policy requires explicitly setting the 'vmDnsSetting=ZonalOnly' metadata at the project or instance level for the policy to function as expected, even if the project default is already zonal DNS. `constraints/compute.managed.disallowGlobalDns`  
Require OS Config |  This constraint, when enforced, requires enablement of VM Manager (OS Config) on all new projects. On new and existing projects, this constraint prevents metadata updates that disable VM Manager at the project, project-zonal, or instance level. You can allow specific VM instances to disable VM Manager. First apply tags to mark the instances, and then use conditional rules based on tag values to properly scope those instances out of enforcement. `constraints/compute.managed.requireOsConfig`  
Require OS Login |  This constraint, when enforced, requires enablement of OS Login on all newly created Projects. On new and existing projects, this constraint prevents metadata updates that disable OS Login at the project, project-zonal, or instance level. You can allow specific VM instances to disable OS Login. First apply tags to mark the instances, and then use conditional rules based on tag values to properly scope those instances out of enforcement. `constraints/compute.managed.requireOsLogin`  
Restrict Non-Confidential Computing |  Preview: Requires all new VMs to be created with Confidential Computing enabled. By default, new VMs are not required to use Confidential Computing. You can apply/exempt this constraint by using tags to mark VM Instances and then enforcing the constraint with conditional rules based on the applied tags. `constraints/compute.managed.restrictNonConfidentialComputing`  
Restricts the use of protocol forwarding |  This constraint lets you restrict the types of protocol forwarding deployments (internal or external) that can be created in your organization. To configure the constraint, you specify an allowlist of the type of protocol forwarding deployment to be allowed. The allowlist can only include the following values: 

  * INTERNAL
  * EXTERNAL

. For example, if the allowlist is set to INTERNAL, your users can only set up internal protocol forwarding. That is, any forwarding rules associated with target instances are restricted to the INTERNAL load balancing scheme and must use only internal IP addresses. `constraints/compute.managed.restrictProtocolForwardingCreationForTypes`  
Define trusted image projects for boot disks |  Preview: This constraint defines the set of projects that can be used for image storage and disk instantiation for Compute Engine. By default, instances can be created from images in any project that shares images publicly or explicitly with the user. Where this constraint is enforced, only images from trusted projects are allowed as the source for new boot disks. Note: If a project is specified in both allowedValues and deniedValues, it will be denied. **Note:** This constraint doesn't support simulation by Policy Simulator for Organization Policy. `constraints/compute.managed.trustedImageProjects`  
Restrict VM IP forwarding |  This constraint defines whether Compute Engine VM instances can enable IP forwarding. By default, if no policy is specified, any VM can enable IP forwarding in any virtual network. If enforced, this constraint will deny the creation or update of VM instances with IP forwarding enabled. You can allow specific VM instances to enable IP forwarding. First apply tags to mark the instances, and then use conditional rules based on tag values to properly scope those instances out of enforcement. `constraints/compute.managed.vmCanIpForward`  
Restrict External IPs For VM instances |  This constraint defines whether Compute Engine VM instances are allowed to use IPv4 external IP addresses. By default, all VM instances are allowed to use external IP addresses. If enforced, this constraint will deny the creation or update of VM instances with IPv4 external IP addresses. This constraint will not restrict the usage of IPv6 external IP addresses. You can allow specific VM instances to use external IPv4 IP addresses. First apply tags to mark the instances, and then use conditional rules based on tag values to properly scope those instances out of enforcement. `constraints/compute.managed.vmExternalIpAccess`  
  
## Hierarchical metadata evaluation

Managed constraints that rely on predefined metadata keys, such as OS Login or Serial Port Access, support hierarchical evaluation. When Compute Engine evaluates these constraints, it checks metadata values set at the VM instance, project, or zonal level.

Setting metadata values at the project or zonal level lets you manage VM instances at scale. However, constraint enforcement occurs only during VM instance creation or update API calls. Thus, changes to project or zonal metadata affect a VM instance's constraint compliance only when that instance is created or updated.

### Metadata-based constraints and levels

Constraint | Metadata key | Metadata hierarchy levels  
---|---|---  
`compute.managed.disableSerialPortAccess` | `serial-port-enable` | Project, Zonal, Instance  
`compute.managed.requireOsLogin` | `enable-oslogin` | Project, Zonal, Instance  
`compute.managed.disableGuestAttributesAccess` | `enable-guest-attributes` | Project, Zonal, Instance  
`compute.managed.requireOsConfig` | `enable-osconfig` | Project, Zonal, Instance  
`compute.managed.disallowGlobalDns` | `VmDnsSetting` | Project, Instance  
  
## Safe rollout: The policy lifecycle

To prevent service disruptions when you gradually implement new constraints, Google recommends that you implement managed constraints by following these steps:

### Analyze with Policy Simulator

Before enforcing a policy, use Policy Simulator to see which existing resources violate the policy. Follow these steps:

  1. In the Google Cloud console, go to the **Organization Policies** page.

[Go to Organization Policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. In the filter bar, search for your constraint, then click the constraint name to go to its **Policy details** page.

  3. Click **Test Changes** to generate a simulation report.

  4. Hierarchical metadata changes might take a few hours to reflect on the simulation report for constraints on VM metadata settings.

  5. Review the report to reconfigure non-compliant resources or request exemptions.




### Validate with dry run

Dry run mode logs violations to Cloud Logging but doesn't enforce restrictions.

To test a constraint, use the [`gcloud org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) as follows:

  1. Create a policy YAML file (for example, `dry-run-policy.yaml`) with a `dryRunSpec`:
         
         name: projects/PROJECT_ID/policies/compute.managed.requireOsLogin
         dryRunSpec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy dry-run-policy.yaml
         




### Full enforcement

After you simulate and test your policy, you can enforce it on a resource. Policy changes can take up to 15 minutes to propagate across all Google Cloud systems.

### Test constraint enforcement

After setting a policy, you can verify enforcement using the gcloud CLI. For example, to test the `compute.managed.requireOsLogin` constraint, follow these steps:

  1. List existing policies to confirm your configuration:
         
         gcloud org-policies list --project=PROJECT_ID
         

  2. Apply the enforcement policy using a YAML file:
         
         gcloud org-policies set-policy enforce_managed_constraint.yaml
         

  3. Verify enforcement by calling a mutation API. Attempting to create a VM instance with non-compliant metadata should fail:
         
         gcloud compute instances create VM_NAME \
             --machine-type=MACHINE_TYPE \
             --image-family=IMAGE_FAMILY \
             --image-project=IMAGE_PROJECT \
             --metadata=enable-oslogin=false
         

Replace the following:

     * `VM_NAME`: the name for the new VM instance.
     * `MACHINE_TYPE`: a valid machine type, for example, `e2-micro`.
     * `IMAGE_FAMILY`: a valid image family, for example, `debian-13`.
     * `IMAGE_PROJECT`: the project of the image family, for example, `debian-cloud`.
  4. Check the error message. You should see a denial indicating the specific constraint violated: `ERROR: (gcloud.compute.instances.create) Could not fetch resource: - Operation denied by org policy: [constraints/compute.managed.requireOsLogin]`




## Conditional exemptions with tags

You can use tags to grant exceptions to specific resources based on business needs. In this example, we use a tag named `osLoginOptional` to identify resources that are exempt from the OS Login requirement. When you bind this tag with a value of `true` to a resource, the organization policy permits that specific resource to exist without OS Login enabled, even while the policy remains strictly enforced for the rest of your environment.

To grant an exception using tags, follow these steps:

  1. Create a tag: Use the gcloud CLI to create a tag key and a tag value.

     1. Create the tag key:
            
            gcloud resource-manager tags keys create osLoginOptional \
                --parent=organizations/ORGANIZATION_ID
            

     2. Create the tag value:
            
            gcloud resource-manager tags values create true \
                --parent=organizations/ORGANIZATION_ID/tagKeys/osLoginOptional
            

Replace `ORGANIZATION_ID` with your organization ID.

  2. Bind the tag to a resource. To exempt a project from the `compute.managed.requireOsLogin` constraint, bind the `osLoginOptional=true` tag to the project using the [`gcloud resource-manager tags bindings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create):
         
         gcloud resource-manager tags bindings create \
             --tag-value=ORGANIZATION_ID/osLoginOptional/true \
             --parent=//cloudresourcemanager.googleapis.com/projects/PROJECT_ID \
             --location=global
         

Replace `ORGANIZATION_ID` with your organization ID, and `PROJECT_ID` with the ID of the project that you want to exempt.

To learn how to bind tags to other resources, see [Bind a tag to a resource](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#binding_tags).

  3. Update the policy: Create or update your policy YAML file (for example, `policy.yaml`) to include the conditional rule.
         
         name: projects/PROJECT_ID/policies/compute.managed.requireOsLogin
         spec:
           rules:
           - condition:
               expression: "resource.matchTag('ORGANIZATION_ID/osLoginOptional', 'true')"
             enforce: false
           - enforce: true
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `ORGANIZATION_ID`: your organization ID.
  4. Apply the policy: Use the following gcloud CLI command to activate the configuration:
         
         gcloud org-policies set-policy policy.yaml
         




## Migration from legacy constraints

When migrating, note that managed constraints improve upon, but don't exactly replicate, the behavior of legacy policies. Managed constraints offer greater predictability by checking for violations only during API requests that create or modify resources. If a request violates a constraint, the API call fails with a clear error. This differs from legacy policies, which could be enforced at various stages of an operation or used as resource attributes, making enforcement behavior less predictable.

When moving from a legacy `compute.*` constraint to a modern `compute.managed.*` equivalent, follow these steps to prevent unintended tightening of restrictions:

  1. Discover: Identify the new managed constraint alternative.
  2. Analyze and validate: Use Policy Simulator and dry run as described earlier.
  3. Enforce managed constraint: Apply the new managed constraint alongside the legacy one.
  4. Delete legacy policies: 
     * Navigate to Asset Inventory in the Google Cloud console and filter by `orgpolicy.Policy` and the legacy constraint name to identify all policies that use the legacy constraint.
     * Delete all policies that use the legacy constraint. Deleting a policy resets that policy to the Google-managed default behavior for that constraint.



## What's next

  * Learn more about the service's foundational concepts and benefits in [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).
  * For detailed instructions on creating and managing policies, see the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).
  * View the [full list of constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) available across all Google Cloud services.
  * Learn how to use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies) for advanced impact analysis of your organization policies.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
