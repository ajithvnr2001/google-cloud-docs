---
url: https://docs.cloud.google.com/vpc/docs/org-policy-flow-logs/
title: Configure organization policy constraints for VPC Flow Logs \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:37.714620+00:00
---

# Configure organization policy constraints for VPC Flow Logs  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/org-policy-flow-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure organization policy constraints for VPC Flow Logs

This page provides information about the [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) constraints that you can configure for subnets in VPC Flow Logs.

**Note:** The information on this page applies only to VPC Flow Logs configurations that are managed by the Compute Engine API. We recommend that you use the Network Management API to [configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs#before-you-begin). To enable VPC Flow Logs for an organization by using the Network Management API, see [Enable VPC Flow Logs for an organization](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-organization).

Administrators can enable or disable VPC Flow Logs. By default, no constraints are imposed on enabling or disabling VPC Flow Logs.

An Organization Policy Administrator can use the `constraints/compute.requireVpcFlowLogs` constraint to require that VPC Flow Logs is enabled for all subnets in the scope of the policy with a specified sampling rate. The policy is enforced when creating subnets or updating the VPC Flow Logs configuration on subnets. Pre-existing subnets are not affected if their VPC Flow Logs configurations are not updated.

## Before you begin

### IAM permissions

The principal creating the constraints must have the [Organization Policy Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy) (`roles/orgpolicy.policyAdmin`).

Principals viewing the constraints must have the `orgpolicy.policy.get` permission on the appropriate resource. For example, the [Organization Policy Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyViewer) (`roles/orgpolicy.policyViewer`) includes the `orgpolicy.policy.get` permission.

### Organization policy background

If you have not worked with organization policy constraints before, see the following pages:

  * [Understanding constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints)
  * [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy)



## Plan your constraints

You can create constraints at the following levels of the resource hierarchy:

  * Organization
  * Folder
  * Project



By default, a constraint created at a node is inherited by all child nodes. However, an Organization Policy Administrator for a given folder can decide if a given folder inherits from its parents, so inheritance is not automatic. For more information, see [Inheritance](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#inheritance) in _Understanding hierarchy evaluation_.

## Sampling rates for VPC Flow Logs

You can use the `constraints/compute.requireVpcFlowLogs` constraint to ensure that the following [sample rates](https://docs.cloud.google.com/vpc/docs/flow-logs#log-sampling) are configured on subnets.

Policy value | Sample rate  
---|---  
`ESSENTIAL` | Greater than or equal to 0.1 (10%) and less than 0.5 (50%) | `LIGHT` | Greater than or equal to 0.5 (50%) and less than 1.0 (100%) | `COMPREHENSIVE` | Equal to 1.0 (100%)  
  
These policy values can be combined. See the following table for examples.

Sample rate | Values to include in constraint  
---|---  
At least 0.1 (10%) | `ESSENTIAL`, `LIGHT`, and `COMPREHENSIVE` | At least 0.5 (50%) | `LIGHT` and `COMPREHENSIVE` | 1.0 (100%) | `COMPREHENSIVE`  
  
## Configure the VPC Flow Logs constraint

###  Console 

For more information about configuring a constraint using the Google Cloud console, see [Customizing policies for list constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints).

  1. Go to the **Require predefined policies for VPC flow logs** policy page in the Google Cloud console:

[Go to organization policy](https://console.cloud.google.com/iam-admin/orgpolicies/compute-requireVpcFlowLogs)

  2. Click **Edit**.

  3. On the **Edit** page, select a value for **Applies to** :

     * **Inherit parent's policy** : If you are configuring policies for a project or folder, the policy of the parent scope is inherited. If you are configuring policies for an organization, the policy is not activated.

     * **Google-managed default** : Disables the policy, even if it's enabled at the parent scope.

     * **Customize** : Lets you enable and configure the policy for all subnets in the current scope.

  4. For **Policy enforcement** , select **Replace**.

**Merge with parent** option is not allowed for VPC Flow Logs.

  5. In the **Rules** section, click **Add rule**.

  6. For **Policy values** , select **Custom**.

Other values are not allowed for VPC Flow Logs.

  7. For **Policy type** , select **Allow**.

  8. In the **Custom values** section, enter one of the values that represents the sampling rate that you want to configure.

If you need to specify more than one value to configure the sampling rate that you want, click **New policy value** and enter the next value. Repeat again if you need to specify a third value.

  9. Click **Save**.




###  gcloud 

For more information about configuring a constraint using the Google Cloud CLI, see [Set up enforcement on the organization resource](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#enforce_list_constraint).

  1. Get the current policy on the organization resource using the `describe` command. This command returns the policy directly applied to this resource. If a policy isn't set, the command returns a `NOT_FOUND` error.
         
         gcloud org-policies describe \
             compute.requireVpcFlowLogs \
             [ --organization=ID | --folder=ID | --project=ID ]
         

Replace the following:

     * `ID`: the ID of the organization, folder, or project that you want to apply the constraint to.
  2. Set the policy on the organization using the `set-policy` command. This command overwrites any policy currently attached to the resource.

     1. Create a temporary file `/tmp/policy.yaml` to store the policy:
            
            name: RESOURCE_TYPE/ID/policies/compute.requireVpcFlowLogs
             spec:
               rules:
               - values:
                   allowedValues:
                   - POLICY_VALUES
             

Replace the following:

        * `RESOURCE_TYPE`: the type of resource that you want to apply the policy to. Valid options are `organizations`, `folders`, or `projects`.

        * `ID`: the ID of the organization, folder, or project that you want to apply the constraint to.

        * `POLICY_VALUES`: the values that represent the sampling rate that you want to configure. You can combine multiple values. For more information, see Sampling rates for VPC Flow Logs.

This example constraint requires a sampling rate of at least 10% at the organizational level:
    
    name: organizations/ID/policies/compute.requireVpcFlowLogs
    spec:
     rules:
     - values:
         allowedValues:
         - ESSENTIAL
         - LIGHT
         - COMPREHENSIVE
    

This example constraint requires a sampling rate of at least 50% at the organizational level:
    
    name: organizations/ID/policies/compute.requireVpcFlowLogs
    spec:
     rules:
     - values:
         allowedValues:
         - LIGHT
         - COMPREHENSIVE
    
    

This example constraint requires a sampling rate of 100% at the organizational level:
    
    name: organizations/ID/policies/compute.requireVpcFlowLogs
    spec:
     rules:
     - values:
         allowedValues:
         - COMPREHENSIVE
    

     2. Run the `set-policy` command:
            
            gcloud org-policies set-policy /tmp/policy.yaml
             

  3. View the current effective policy using `describe --effective`. This command returns the organization policy as it is evaluated at this point in the resource hierarchy with inheritance included.
         
         gcloud org-policies describe \
             compute.requireVpcFlowLogs --effective \
             [ --organization=ID | --folder=ID | --project=ID ]
         




## Effects of setting a requirement for VPC Flow Logs

Configuring an organization policy with the `constraints/compute.requireVpcFlowLogs` constraint means that you might see errors if you create a subnet, or update the VPC Flow Logs configuration of an existing subnet, and the configuration does not meet the requirements of the policy.

If you see errors, you might need to know how the constraint is configured so that you can create a valid configuration. If you don't have sufficient IAM permissions to view the constraint, contact your organization administrator.

Subnets that are created before the policy is set are not affected by the policy, as long as their VPC Flow Logs configuration is not updated.

### Effects on subnet creation

When creating a new subnet in the policy's scope, the following applies:

  * If VPC Flow Logs is explicitly enabled with a sampling rate that meets the requirements of the policy, then the subnet is created with VPC Flow Logs enabled and the requested sampling rate.

  * If VPC Flow Logs is explicitly enabled with a sampling rate that does not meet the requirements of the policy, an error is returned and the subnet is not created.

  * If VPC Flow Logs is explicitly disabled, an error is returned and the subnet is not created.

  * If VPC Flow Logs is not set and the sampling rate is also not set, a subnet is created with VPC Flow Logs enabled and the minimum sampling rate required by the policy. For example, if the policy is configured with policy values of `LIGHT` and `COMPREHENSIVE`, the sampling rate is set to `0.5` (50%).


**Note:** When you create a subnet using the Google Cloud console, you must explicitly set VPC Flow Logs to be disabled or enabled. However, when you create a subnet using the Google Cloud CLI or the API, you can configure VPC Flow Logs to be disabled, enabled, or not set.

### Effects on subnet updates

When updating an existing subnet in the policy scope, the following applies:

  * If the update enables VPC Flow Logs or if VPC Flow Logs was already enabled, and the sampling rate is set to a value that meets the requirements of the policy, then the subnet is updated with VPC Flow Logs enabled with the requested sampling rate.

  * If the update enables VPC Flow Logs or if VPC Flow Logs was already enabled, and the sampling rate is set to a value that does not meet the requirements of the policy, an error is returned and the subnet is not updated.

  * If the update disables VPC Flow Logs, an error is returned and the subnet is not updated.

  * If the update does not enable or disable VPC Flow Logs and the sampling rate is also not set, the policy is ignored and the subnet is updated.




### Effects on auto mode VPC network creation

When an auto mode VPC network is created, a subnet is automatically created in each region. If the network is in the scope of a VPC Flow Logs policy, VPC Flow Logs is enabled on the subnets with the minimum sampling rate defined by the policy. For example, if the policy is configured with policy values of `LIGHT` and `COMPREHENSIVE`, the sampling rate is set to `0.5` (50%).

### Effects on VPC Flow Logs configuration

If a subnet is in the scope of the policy, [log filtering](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#filtering) isn't allowed, to ensure the VPC Flow Logs configuration meets the requirements of the policy.

## What's next

  * [Configure VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
