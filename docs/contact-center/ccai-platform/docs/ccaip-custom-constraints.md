---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints/
title: Manage Contact Center AI Platform (CCAI Platform) resources using custom constraints \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:36.282419+00:00
---

# Manage Contact Center AI Platform (CCAI Platform) resources using custom constraints  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Manage Contact Center AI Platform (CCAI Platform) resources using custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud [Organization Policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) gives you centralized, programmatic control over your organization's resources. As the organization policy administrator, you can define an organization policy, which is a set of restrictions called constraints that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides [predefined constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create custom constraints. Implementing a custom constraint for CCAI Platform requires you to configure your instances for private access. This restricts public internet access to those instances, which means that you need to set up Private Service Connect for your agents, managers, and CCAI Platform administrators to access them. For more information, see [Set up Private Service Connect](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc).

## Benefits

Organization policies for CCAI Platform let Google Cloud administrators enforce organization-wide constraints over network paths that are not covered by [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). In addition, these organization policies offer fine-grained control over ingress and egress paths by partitioning the network traffic into components. For more information, see Components.

## Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#disallow_inheritance).

## Pricing

The Organization Policy Service, including predefined and custom organization policies, is offered at no charge.

## Limitations

CCAI Platform is not integrated with [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) and therefore the [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview) feature of Policy Intelligence is not available for CCAI Platform Organization Policy.

## Before you begin

Before you begin, do the following:

  1. Follow the steps in [Set up your Google Cloud project for CCAI Platform](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started#set-up-project).
  2. To install and initialize the Google Cloud CLI, do the following: 
     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init



* Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

### Required roles

To get the permissions that you need to manage organization policies, ask your administrator to grant you the following IAM roles: 

  * [Organization policy administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization resource
  * For full access to CCAI Platform resources: [Contact Center AI Platform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenteraiplatform#contactcenteraiplatform.admin) (`roles/contactcenteraiplatform.admin`) on the project resource 
  * For the ability to enable, disable, and inspect service states, inspect operations, and consume quota and billing for a consumer project: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) on the project resource 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage organization policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage organization policies:

  * `orgpolicy.customConstraints.get`
  * `orgpolicy.customConstraints.list`
  * `orgpolicy.customConstraints.create`
  * `orgpolicy.customConstraints.update`
  * `orgpolicy.customConstraints.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Components

You use components when creating custom constraints on CCAI Platform instances. Components are abstractions of network paths associated with specific CCAI Platform functionalities. For example, the _agent_ component represents the group of all ingress network paths related to the tasks that an agent, manager, or CCAI Platform administrator does.

The following table shows the components used in CCAI Platform custom constraints:

Component | Description | Traffic direction | Example value  
---|---|---|---  
`AGENT` | The group of all ingress network paths related to the tasks that an agent, manager, or CCAI Platform administrator does. | Ingress | `AGENT`  
`CRM` | Egress traffic to a customer relationship management (CRM) app. | Egress | `CRM`  
`MEDIA` | Media egress traffic.  | Egress | `MEDIA`  
`DIRECT_ACCESS_POINT` | Egress traffic to a direct access endpoint (DAP). | Egress | `DIRECT_ACCESS_POINT`  
`EMAIL` | Email egress traffic. | Egress | `EMAIL`  
`COBROWSE` | Screen Share egress traffic. | Egress | `COBROWSE`  
  
## Create a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language).

To define a custom constraint in a YAML file for CCAI Platform, follow these steps:

  1. Create a text file that contains the following lines:
         
         name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
         resourceTypes:
         - contactcenteraiplatform.googleapis.com/ContactCenter
         methodTypes:
         - CREATE
         - UPDATE
         condition: "CONDITION"
         actionType: ACTION_TYPE
         displayName: "DISPLAY_NAME"
         description: "DESCRIPTION"
         

Replace the following:

     * `ORGANIZATION_ID`: your organization ID.

     * `CONSTRAINT_NAME`: the name of your custom constraint. A custom constraint must start with a `custom.` prefix, and can only include uppercase letters, lowercase letters, or numbers—for example, `custom.requirePrivateAccess`. This field has a maximum length of 70 characters, not counting the prefix.

     * `CONDITION`: a [CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource—for example, `resource.privateAccess.ingressSettings.exists(private_component, private_component.name == 'AGENT')`. This field has a maximum length of 1000 characters. For more information about the resources that are available to write conditions against, see CCAI Platform supported resources and operations. For more information about components, see Components.

     * `ACTION_TYPE`: the action to take if the `condition` is met. Specify `ALLOW`.

     * `DISPLAY_NAME`: a human-friendly name for the constraint. This field has a maximum length of 200 characters.

     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field has a maximum length of 2000 characters.

  2. Save the custom constraint as a YAML file—for example, `customconstraint.yaml`. Use the path to this file as the value of the `CONSTRAINT_PATH` variable in Set up a custom constraint.




For more information about custom organization policies and constraint syntax, see Example custom organization policies for common use cases.

## Set up a custom constraint

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.requirePrivateAccess`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
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
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.requirePrivateAccess`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `contactcenteraiplatform.googleapis.com/ContactCenter`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, ``resource.privateAccess.ingressSettings.exists(private_component, private_component.name == 'AGENT')``. 

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

You can enforce a boolean constraint by creating an organization policy that references it, and applying that organization policy to a Google Cloud resource.

To enforce a custom constraint, follow these steps:

  1. To create an organization policy that enforces a boolean constraint, create a policy YAML file that references the following constraint:
         
         name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
         spec:
           rules:
           - enforce: true
         

Replace the following:

     * `PROJECT_ID`: the project on which you want to enforce your constraint.
     * `CONSTRAINT_NAME`: the name that you defined for your custom constraint—for example, `custom.requirePrivateAccess`.
  2. To enforce the organization policy containing the constraint, run the following command:
         
         gcloud org-policies set-policy POLICY_PATH
         

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy will take up to 15 minutes to take effect.




## Test the custom constraint

A custom constraint, as defined in Create a custom constraint (with a component of type `AGENT`, as in the example in the `CONDITION` description), enforces the following behaviors:

  * Creating or updating an instance with a component of type `AGENT`succeeds. For more information, see Create and update a CCAI Platform instance with a component of type `AGENT`.

  * Creating or updating an instance without a component of type `AGENT`fails. For more information, see Create a CCAI Platform instance without a component of type `AGENT` and Update a CCAI Platform instance without a component of type `AGENT`.




### Create and update a CCAI Platform instance with a component of type `AGENT`

To test creating and updating a CCAI Platform instance with a component of type `AGENT`, follow these steps:

  1. Create, set up, and enforce a custom constraint as directed in this document.

  2. Create an instance as directed in [Create a CCAI Platform instance configured for private access](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc#create-an-instance-configured-for-private-access). The instance creation succeeds.

  3. To update the instance, do the following:

     1. In the Google Cloud console, in the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

The **CCAI Platform instances** page displays.

     2. Click the name of the instance that you created previously in this procedure.

     3. Click **Edit** , and then click **Configure deployments**.

     4. Change the deployment schedule, and then click **Save**. The update succeeds.




Because you created a private CCAI Platform instance, you need to [Set up a Private Service Connect connection ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc#set-up-a-private-service-connect-connection) to access it.

### Create a CCAI Platform instance without a component of type `AGENT`

To test creating and updating a CCAI Platform instance without a component of type `AGENT`, follow these steps:

  1. Create, set up, and enforce a custom constraint as directed in this document.

  2. Attempt to create an instance as directed in [Create a CCAI Platform instance](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started#create-ccaip-instance), without configuring private access. The instance creation fails.




### Update a CCAI Platform instance without a component of type `AGENT`

As demonstrated in Create a CCAI Platform instance without a component of type `AGENT`, you can't create an instance without a component of type `AGENT` after enforcing the custom constraint. If you already had such an instance before you enforced the custom constraint, after enforcing the constraint, updates to the instance fail (unless the updates include adding a component of type `AGENT`—see the following note).

**Note:** After enforcing the custom constraint, there is one type of update that you can make to a CCAI Platform instance without a component of type `AGENT`. You can configure the instance for private access and add a component of type `AGENT`. If you do this, you need to [Set up a Private Service Connect connection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc#set-up-a-private-service-connect-connection) to access the private instance.

## CCAI Platform supported resources and operations

The following table shows the supported resources and operations for Organization Policy custom constraints.

Resource | Action | Attribute | Operator | Example condition  
---|---|---|---|---  
ContactCenter | Create or update an instance. For more information, see [Create a CCAI Platform instance](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started#create-ccaip-instance). | name | contains | `resource.name.contains("us-central1/contactCenters/myContactCenter")`  
matches | `resource.name.matches("projects/my-project/locations/us-central1/contactCenters/myContactCenter")`  
startsWith | `resource.name.startsWith("projects/my-project")`  
endsWith | `resource.name.endsWith("myContactCenter")`  
privateAccess | exists |  `resource.privateAccess.ingressSettings.exists(private_component, private_component.name == 'AGENT')` Checks that the `AGENT` component is enabled.  
  
## Example custom organization policies for common use cases

The following table provides the syntax of some custom organization policies that you might find useful:

Description | Constraint syntax  
---|---  
All of the specified components are private—in other words, `AGENT)`. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.requirePrivateAccess
        resourceTypes:
        - contactcenteraiplatform.googleapis.com/ContactCenter
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.privateAccess.ingressSettings.exists(private_component, private_component.name == 'AGENT')"
        actionType: ALLOW
        displayName: Agents cannot connect over the internet.
        description: Internet access is disallowed for agents.  
  
All instances, except the single specified instance, must use the specified private `AGENT`. | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.requirePrivateAccess
        resourceTypes:
        - contactcenteraiplatform.googleapis.com/ContactCenter
        methodTypes:
        - CREATE
        - UPDATE
        condition: "resource.privateAccess.ingressSettings.exists(private_component, private_component.name == 'AGENT' ||
        resource.name.contains('myContactCenterId')"
        actionType: ALLOW
        displayName: Restrict Internet access to AGENT for all instances except a
        single instance.
        description: Internet access for agents is restricted except for myContactcenterId CCAI Platform instances.  
  
## What's next

  * [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)
  * [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints)
  * [Creating and managing custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints)
  * [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
