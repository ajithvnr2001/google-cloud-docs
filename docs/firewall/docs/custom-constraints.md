---
url: https://docs.cloud.google.com/firewall/docs/custom-constraints/
title: Manage VPC firewall rule resources by using custom constraints \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:08.139159+00:00
---

# Manage VPC firewall rule resources by using custom constraints  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage VPC firewall rule resources by using custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Organization Policy gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin), you can define an organization policy, which is a set of restrictions called constraints that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides [predefined constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and enforce those custom constraints in a custom organization policy.

## Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, see [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#hierarchy_evaluation_rules).

## Cloud NGFW supported resources

For [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls), you can set custom constraints on the following resources and fields.

  * [Firewall](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls): `compute.googleapis.com/Firewall`
    * Name: `resource.name`
    * Description: `resource.description`
    * Network: `resource.network`
    * Priority: `resource.priority`
    * Source ranges: `resource.sourceRanges[]`
    * Destination ranges: `resource.destinationRanges[]`
    * Source tags: `resource.sourceTags[]`
    * Target tags: `resource.targetTags[]`
    * Allow rules: `resource.allowed[]`
      * Protocol: `resource.allowed[].IPProtocol`
      * Ports: `resource.allowed[].ports[]`
    * Deny rules: `resource.denied[]`
      * Protocol: `resource.denied[].IPProtocol`
      * Ports: `resource.denied[].ports[]`
    * Direction: `resource.direction`
    * Is disabled: `resource.disabled`

**Note:** To create custom constraints based on protocols or ports, we recommend that you use the custom CEL function `containsFirewallPort`. For more information, see Defining custom constraints.

## Defining custom constraints

A custom constraint is defined by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).

In addition to the standard CEL functions, you can use the custom CEL function `containsFirewallPort` to create custom constraints for firewall rules. You can use this function to create a constraint that refers to a particular protocol, or a protocol and port combination.

  * Protocol only: `resource.allowed.containsFirewallPort('PROTOCOL')`
  * Protocol and port: `resource.allowed.containsFirewallPort('PROTOCOL', 'PORT_NUMBER')`



For information about allowed protocols, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewalls#protocols_and_ports).

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

### Required roles

To get the permissions that you need to manage organization policies for Cloud Next Generation Firewall (Cloud NGFW) resources, ask your administrator to grant you the following IAM roles: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization resource
  * To test the constraints: 
    * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on the project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policies for Cloud Next Generation Firewall (Cloud NGFW) resources. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies for Cloud Next Generation Firewall (Cloud NGFW) resources:

  * `orgpolicy.constraints.list`
  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.list`
  * `orgpolicy.policies.update`
  * `orgpolicy.policy.get`
  * `orgpolicy.policy.set`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up a custom constraint

You can create a custom constraint and set it up for use in organization policies by using the Google Cloud console or Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. Select the **Project picker** at the top of the page.

  3. From the **Project picker** , select the resource for which you want to set the organization policy.

  4. Click add **Custom constraint**.

  5. In the **Display name** box, enter a human-friendly name for the constraint. This field has a maximum length of 200 characters. Don't use PII or sensitive data in constraint names, because they could be exposed in error messages.

  6. In the **Constraint ID** box, enter the name you want for your new custom constraint. A custom constraint must start with `custom.`, and can only include uppercase letters, lowercase letters, or numbers, for example, custom.httpFirewallRule. The maximum length of this field is 70 characters, not counting the prefix, for example, `organizations/123456789/customConstraints/custom.`.

  7. In the **Description** box, enter a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2,000 characters.

  8. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field you want to restrict. For example, `compute.googleapis.com/Firewall`.

  9. Under **Enforcement method** , select whether to enforce the constraint on the REST `CREATE` method only or on both the REST `CREATE` and `UPDATE` methods.

  10. To define a condition, click edit **Edit condition**.

     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource. This field has a maximum length of 1,000 characters.

     2. Click **Save**.

  11. Under **Action** , select whether to allow or deny the evaluated method if the previous condition is met.

  12. Click **Create constraint**.




When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right.

###  gcloud 

To create a custom constraint using the Google Cloud CLI, create a YAML file.
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resource_types: compute.googleapis.com/RESOURCE_NAME
    method_types:
    – METHOD1
    – METHOD2
    condition: "CONDITION"
    action_type: ACTION
    display_name: DISPLAY_NAME
    description: DESCRIPTION

Replace the following:

  * `ORGANIZATION_ID`: the organization ID, such as `123456789`.

  * `CONSTRAINT_NAME`: the name for the custom constraint to create. A custom constraint ID must start with `custom.` and can contain only uppercase letters, lowercase letters, and numbers. For example, custom.httpFirewallRule.

The maximum length of this field is 70 characters, not counting the prefix. For example, `organizations/123456789/customConstraints/custom`.

  * `RESOURCE_NAME`: the name (not the URI) of the Compute Engine API REST resource containing the object and field to restrict. For example, compute.googleapis.com/Firewall.

  * `METHOD1`, `METHOD2`, ...: a list of RESTful _methods_ for which to enforce the constraint. Can be `CREATE` or `CREATE` and `UPDATE`.

  * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field has a maximum length of 1,000 characters. See Supported resources for more information about the resources available to write conditions against.

  * `ACTION`: the action to take if the `condition` is met. This can be either `ALLOW` or `DENY`.

  * `DISPLAY_NAME`: a human-friendly name for the constraint. This field has a maximum length of 200 characters.

  * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2,000 characters.




For more information about how to create a custom constraint, see [Defining custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#defining_custom_constraints).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.httpFirewallRule`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. This constraint can only be enforced on the REST `CREATE` method. 

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
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.httpFirewallRule`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `compute.googleapis.com/Firewall`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.allowed.containsFirewallPort('tcp', '80')"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Can only be `ALLOW`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

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




## Enforce a custom constraint

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.httpFirewallRule`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Example: Create a constraint that restricts creating firewall rules that allow SSH connections

This constraint prevents the creation of ingress firewall rules that allow SSH connections from any IP address range other than the following ranges:

  * `10.0.0.0/8`: an internal IP address range used in the VPC network.
  * `192.168.0.0/16`: an internal IP address range used in the VPC network.
  * `35.235.240.0/20`: the IP address range used by [Identity-Aware Proxy (IAP) for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).



All IP address ranges that include TCP port 22 are also blocked.

###  gcloud 

  1. Create a `restrictSshRanges.yaml` constraint file with the following information.
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictSshRanges
         resource_types: compute.googleapis.com/Firewall
         condition: "resource.direction.matches('INGRESS') && resource.allowed.containsFirewallPort('tcp', '22') && !resource.sourceRanges.all(range, range == '35.235.240.0/20' || range.startsWith('10.') || range.startsWith('192.168.'))"
         action_type: DENY
         method_types: CREATE
         display_name: Limit firewall rules that allow ingress SSH traffic
         description: Firewall rules that allow ingress SSH traffic can only be created with allowed source ranges.

Replace `ORGANIZATION_ID` with the ID of the organization.

  2. Set the custom constraint by using the [`gcloud org-policies set-custom-constraint` command](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint):
         
         gcloud org-policies set-custom-constraint restrictSshRanges.yaml
         

  3. Create a `restrictSshRanges-policy.yaml` policy file with the information provided in the following example and enforce the constraint at the project level. You can also set this constraint at the organization or folder level.
         
         name: projects/PROJECT_ID/policies/custom.restrictSshRanges
             spec:
               rules:
               – enforce: true

Replace `PROJECT_ID` with the ID of the project.

  4. Enforce the policy by using the [`gcloud org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy).
         
         gcloud org-policies set-policy restrictSshRanges-policy.yaml
         

  5. To test the constraint, create an auto mode VPC network by using the [`gcloud compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
         
         gcloud compute firewall-rules create ssh-firewall-rule \
             --action=ALLOW \
             --direction=INGRESS \
             --network=NETWORK \
             --priority=1000 \
             --rules=tcp:22 \
             --source-ranges=0.0.0.0/0
         

Replace `NETWORK` with the name of the network. The output is similar to the following: 
         
         ERROR: (gcloud.compute.firewall-rules.create) Could not fetch resource:
         - Operation denied by custom org policy: [customConstraints/custom.restrictSshRanges] : Firewall rules that allow ingress SSH traffic can only be created with allowed source ranges.




## Example: Restrict ingress traffic to only standard web ports

This constraint blocks the creation of ingress firewall rules that allow traffic from `0.0.0.0/0` on TCP ports other than `80` or `443`.

###  gcloud 

  1. Create a `restrictWebPorts.yaml` constraint file with the following information.
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.restrictWebPorts
         resource_types: compute.googleapis.com/Firewall
         condition: "resource.direction.matches('INGRESS') && resource.sourceRanges.all(range, range == '0.0.0.0/0') && resource.allowed.exists(allowed, allowed.IPProtocol != 'tcp' || allowed.ports.exists(port, port != '80' && port != '443'))"
         action_type: DENY
         method_types: CREATE
         display_name: Limit firewall rules that allow ingress traffic from 0.0.0.0/0
         description: Firewall rules that allow ingress traffic from 0.0.0.0/0 on TCP ports other than 80 or 443.

Replace `ORGANIZATION_ID` with the ID of the organization.

  2. Set the custom constraint by using the [`gcloud org-policies set-custom-constraint` command](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint):
         
         gcloud org-policies set-custom-constraint restrictWebPorts.yaml
         

  3. Create a `restrictWebPorts-policy.yaml` policy file with the information provided in the following example and enforce the constraint at the project level. You can also set this constraint at the organization or folder level.
         
         name: projects/PROJECT_ID/policies/custom.restrictWebPorts
             spec:
               rules:
               – enforce: true

Replace `PROJECT_ID` with the ID of the project.

  4. Enforce the policy by using the [`gcloud org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy):
         
         gcloud org-policies set-policy restrictWebPorts-policy.yaml
         

  5. To test the constraint, create an auto mode VPC network by using the [`gcloud compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).
         
         gcloud compute firewall-rules create ssh-firewall-rule \
             --action=ALLOW \
             --direction=INGRESS \
             --network=NETWORK \
             --priority=1000 \
             --rules=tcp:22 \
             --source-ranges=0.0.0.0/0
         

Replace `NETWORK` with the name of the network. The output is similar to the following: 
         
         ERROR: (gcloud.compute.firewall-rules.create) Could not fetch resource:
         - Operation denied by custom org policy: [customConstraints/custom.restrictWebPorts] : Firewall rules that allow ingress traffic from 0.0.0.0/0 on TCP ports other than 80 or 443.




## What's next

  * [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)
  * [Create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)
  * [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
