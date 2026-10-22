---
url: https://docs.cloud.google.com/organization-policy/restrict-services/
title: Restrict service usage \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:10.466749+00:00
---

# Restrict service usage  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/restrict-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Restrict service usage Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the **Restrict Resource Service Usage** [organization policy constraint](https://docs.cloud.google.com/organization-policy/overview#constraints), which allows enterprise administrators to control which Google Cloud services can be used within their Google Cloud resource hierarchy. This constraint can only be enforced on services with resources that are the direct descendants of an organization, folder, or project resource. For example, Compute Engine and Cloud Storage.

The **Restrict Resource Service Usage** constraint excludes and won't work with certain services that are essential dependencies for Google Cloud products, such as Identity and Access Management (IAM), Cloud Logging, and Cloud Monitoring. For the list of cloud resource services that are supported by this constraint, see [Services that support restricting service usage](https://docs.cloud.google.com/organization-policy/reference/restrict-services-supported-services).

Administrators can use this constraint to define hierarchical restrictions on allowed Google Cloud resource services within a **resource container** , such as an organization, a folder, or a project. For example, allow `storage.googleapis.com` within project X, or deny `compute.googleapis.com` within folder Y. This constraint also determines Google Cloud console availability.

The **Restrict Resource Service Usage** constraint can be used in two mutually exclusive ways:

  * Denylist - resources of any service that isn't denied are allowed.

  * Allowlist - resources of any service that isn't allowed are denied.




The **Restrict Resource Service Usage** constraint controls the runtime access to all in-scope resources. When the organization policy containing this constraint is updated, it immediately applies to all access to all resources within the scope of the policy, with eventual consistency.

We recommend administrators carefully manage updates to organization policies containing this constraint. You can more safely rollout this policy change by using tags to conditionally enforce the constraint. For more information, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

When a service is restricted by this policy, some Google Cloud services that have a direct dependency on the restricted service will be restricted as well. This only applies to services that manage the same customer resources. For example, Google Kubernetes Engine (GKE) has a dependency on Compute Engine. When Compute Engine is restricted, GKE is also restricted.

**Note:** Organization policy [audit logging](https://docs.cloud.google.com/organization-policy/audit-logging) violations are logged in the [Policy Denied](https://docs.cloud.google.com/logging/docs/audit#policy_denied) category of Cloud Audit Logs. This is a billable category.

### Google Cloud console availability

Restricted services in the Google Cloud console behave in the following way:

  * You can't navigate to a product using the menu menu.
  * Restricted services don't appear in Google Cloud console search results.
  * When you navigate to a restricted service's Google Cloud console page—such as from a link or bookmark—an error message appears.



## Using the Restrict Resource Service Usage constraint

Organization policy constraints can be set at the organization, folder, and project level. Each policy applies to all resources within its corresponding resource hierarchy, but can be overridden at lower levels in the resource hierarchy.

For more information about policy evaluation, see [Hierarchy evaluation](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).

## Setting the organization policy

To set, change, or delete an organization policy, you must have the [Organization Policy Administrator](https://docs.cloud.google.com/organization-policy/create-organization-policies#add-org-policy-admin) role.

### Console

To set an organization policy that includes a **Restrict Resource Service Usage** constraint, do the following:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the resource on which you want to set the organization policy.

  3. In the table of organization policies, select **Restrict Resource Service Usage**.

  4. Click **Manage policy**.

  5. Under **Applies to** , select **Override parent's policy**.

  6. Under **Policy enforcement** , choose how to apply inheritance to this policy.

     1. If you want to inherit the organization policy of the parent resource and merge it with this one, select **Merge with parent**.

     2. If you want to override any existing organization policies, select **Replace**.

  7. Click **Add a rule**.

  8. Under **Policy values** , select **Custom**.

  9. Under **Policy type** , select **Deny** for denylist or **Allow** for allowlist.

  10. Under **Custom values** , add the service you want to block or allow to the list.

     1. For example, to block Cloud Storage, you could enter `storage.googleapis.com`.

     2. To add more services, click **Add value**.

  11. To enforce the policy, click **Set policy**.




### gcloud

Organization policies can be set through the Google Cloud CLI. To enforce an organization policy that includes the **Restrict Resource Service Usage** constraint, first create a YAML file with the policy to be updated:
    
    
    name: organizations/ORGANIZATION_ID/policies/gcp.restrictServiceUsage
    spec:
      rules:
      - values:
          deniedValues:
          - file.googleapis.com
          - bigquery.googleapis.com
          - storage.googleapis.com
    

Replace ORGANIZATION_ID with the ID of your organization resource. To set this policy on that organization, run the following command:
    
    
    gcloud org-policies set-policy /tmp/policy.yaml
    

To learn about using constraints in organization policies, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint).

## Restricting untagged resources

You can use tags and conditional organization policies to restrict any resources that are not using a particular tag. If you set an organization policy on a resource that restricts services and make it conditional on the presence of a tag, no child resources descended from that resource can be used unless they have been tagged. In this way, resources must be set up in accordance with your governance plan before they can be used.

To restrict untagged organization, folder, or project resources, you can use the `!` logical operator in a conditional query when creating your organization policy.

For example, to allow the usage of `sqladmin.googleapis.com` only in projects that have the tag `sqladmin=enabled`, you can create an organization policy that denies `sqladmin.googleapis.com` on projects that do not have the tag `sqladmin=enabled`.

  1. [Create a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) that identifies whether the resources have had proper governance applied. For example, you could create a tag with the key `sqlAdmin` and the value `enabled`, to designate that this resource should allow the usage of the Cloud SQL Admin API. For example:

![Creating a tag key and value](https://docs.cloud.google.com/static/organization-policy/images/sqladmin_tag.png)

  2. Click on the name of the newly created tag. You need the namespaced name of the tag key, listed under **Tag key path** , in the next steps to create a condition.

  3. Create a **Restrict Resource Service Usage** organization policy at the level of your organization resource to deny access to the Cloud SQL Admin API. For example:

![Creating an organization policy for restricting resources](https://docs.cloud.google.com/static/organization-policy/images/sqladmin_policy.png)

  4. Add a condition to the above organization policy, specifying that the policy is enforced if the governance tag is not present. The logical NOT operator is not supported by the condition builder, so this condition must be built in the condition editor. For example:

![Building a conditional organization policy](https://docs.cloud.google.com/static/organization-policy/images/sqladmin_condition.png)

`!resource.matchTag("012345678901/sqlAdmin", "enabled")`




Now, the `sqlAdmin=enabled` tag must be attached to or inherited by a project, before your developers can use the Cloud SQL Admin API with that project.

For more information about creating conditional organization policies, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

## Create an organization policy in dry-run mode

An organization policy in dry-run mode is a type of organization policy where violations of the policy are audit logged, but the violating actions aren't denied. You can create an organization policy in dry-run mode using the **Restrict Resource Service Usage** constraint to monitor how it would affect your organization before you enforce the live policy. For more information, see [Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies#create_dry_run_list_policy).

## Error message

If you set an organization policy to deny service A within resource hierarchy B, when a client tries to use service A within resource hierarchy B, the operation fails. An error is returned that describes the reason for this failure. Also, an AuditLog entry is generated for further monitoring, alerting, or debugging.

### Example error message
    
    
    Request is disallowed by organization's constraints/gcp.restrictServiceUsage
    constraint for projects/PROJECT_ID attempting to use service
    storage.googleapis.com.
    

### Example Cloud Audit Logs

![Screenshot of example Audit Log entry](https://docs.cloud.google.com/static/organization-policy/images/sur-error.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
