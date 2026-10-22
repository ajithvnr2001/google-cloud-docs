---
url: https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview/
title: Policy Analyzer for allow policies \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:44.100519+00:00
---

# Policy Analyzer for allow policies  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Policy Analyzer for allow policies Stay organized with collections  Save and categorize content based on your preferences. 

Policy Analyzer for allow policies lets you find out which principals (for example, users, service accounts, groups, and domains) have what access to which Google Cloud resources based on your [IAM allow policies](https://docs.cloud.google.com/iam/docs/policies).

Policy Analyzer for allow policies can help you answer questions like these:

  * Who can access this IAM service account?
  * Who can read data in this BigQuery dataset that contains personally identifiable information (PII)?
  * What roles and permissions does the `dev-testers` group have on any resource in this project?
  * What Compute Engine virtual machine (VM) instances can Tal delete in project A?
  * Who can access this Cloud Storage bucket at 7 PM?



## How Policy Analyzer for allow policies works

To use Policy Analyzer for allow policies, you create an analysis query, specify a scope for the analysis, and then run the query.

### Analysis queries

To use Policy Analyzer, you create an _analysis query_ specifying one or more of the following fields:

  * Principals: The identities (for example, users, service accounts, groups, and domains) whose access you want to check
  * Access: The permissions and roles that you want to check for
  * Resources: The resources that you want to check for access to
  * (API only) Condition context: The context—for example, time of day—under which you want to check for access



Typically, you specify one or two of these fields in the analysis query, then use the query results to get more information about the fields that you didn't specify. For example, if you wanted to know who has a certain permission on a certain resource, you would specify the access and resource in the analysis query, but you would not specify the principal.

For more examples of the kinds of queries you can create, see Common query types.

### Analysis scope

To run an analysis query, you need to specify a _scope_ to analyze. The scope is an organization, a folder, or a project that you want to restrict your analysis to. Only IAM allow policies attached to the resource used as the scope and to its descendants will be analyzed.

In the REST API and gcloud CLI, you specify the scope manually. In the Google Cloud console, the scope is automatically determined based on the project, folder, or organization that you're managing.

After you create an analysis query and specify the scope, you can [run the query](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies) to analyze policies in that scope.

### Query results

When you run an analysis query, Policy Analyzer reports any [role bindings](https://docs.cloud.google.com/iam/docs/policies#structure) that contain the principals, access, and resources that you specified in the query. For each role binding, it reports the principals in the binding, the access (role and permissions) that the binding grants, and the resource that the binding grants access to.

You can review these results to better understand access in your project, folder, or organization. For example, if you ran a query to find out which principals have access to a specific resource, you would review the principals in the query results.

You can adjust the information in your query results by enabling query options.

### Supported policy types

Policy Analyzer for allow policies only supports [IAM allow policies](https://docs.cloud.google.com/iam/docs/policies).

Policy Analyzer for allow policies doesn't support the following forms of access control:

  * [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview)
  * [IAM Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)
  * [Google Kubernetes Engine role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)
  * [Cloud Storage access control lists](https://docs.cloud.google.com/storage/docs/access-control/lists)
  * [Cloud Storage public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)



Policy Analyzer query results don't account for unsupported policy types. For example, imagine that a user has the `iam.roles.get` permission on a project because of an allow policy, but a deny policy prevents them from using the permission. Policy Analyzer will report that they have the `iam.roles.get` permission, despite the deny policy.

### Policy inheritance

To account for [policy inheritance](https://docs.cloud.google.com/iam/docs/policies#inheritance), Policy Analyzer automatically analyzes all relevant allow policies within the specified scope, regardless of where they are in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

For example, imagine you're trying to find out who can access an IAM service account:

  * If you scope the query to a project, Policy Analyzer analyzes the allow policy of the service account and the allow policy of the project.
  * If you scope the query to an organization, Policy Analyzer analyzes the allow policy of the service account, the allow policy of the project that owns the service account, the allow policies of any folders containing the project, and the allow policy of the organization.



### Conditional access

If a role binding has a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview), it only grants a principal access when that condition is met. Policy Analyzer always reports conditions that are attached to relevant role bindings. Relevant role bindings are role bindings that contain the principals, access, and resources that you specified in the analysis query.

In some cases, Policy Analyzer can also analyze the condition, meaning that it can report whether the condition would be met. Policy Analyzer can analyze the following types of conditions:

  * Conditions based on [resource attributes](https://docs.cloud.google.com/iam/docs/conditions-overview#resource_attributes), for resource types that provide a [resource name](https://docs.cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).
  * [Date/time conditions](https://docs.cloud.google.com/iam/docs/conditions-overview#example-date-time) (API and gcloud CLI only). For Policy Analyzer to analyze these conditions, you need to provide the time of the access (`accessTime`) in your analysis query. To learn how to provide this context, see [Determine access at a specific time](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#conditional-access).



If a relevant role binding contains a condition, Policy Analyzer does one of the following:

  * If Policy Analyzer can analyze the condition, it does one of the following:

    * If the condition evaluates to true, Policy Analyzer includes the role binding in the query results and marks the condition evaluation as `TRUE`.
    * If the condition evaluates to false, Policy Analyzer does not include the role in the query results.
  * If Policy Analyzer can't analyze a condition for a relevant role binding, it includes the role in the query results and marks the condition evaluation as `CONDITIONAL`.




### Data freshness

Policy Analyzer uses the Cloud Asset API, which offers best-effort data freshness. While almost all policy updates appear in Policy Analyzer in minutes, it's possible that Policy Analyzer won't include the most recent policy updates. 

## Common query types

This section describes how to use analysis queries to answer common access-related questions.

### Which principals can access this resource?

To determine which principals can access a resource, create an analysis query that specifies the resource and, optionally, the roles and permissions that you want to check for.

These queries can help you answer questions like the following:

  * Who has access to this IAM service account?
  * Who has permission to impersonate this IAM service account?
  * Who are the billing administrators on project A?
  * (API and gcloud CLI only): Who can update project A by impersonating a service account?



To learn how to create and send these queries, see [Determine which principals can access a resource](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#principal-query-resource).

### Which principals have these roles and permissions?

To determine which principals have certain roles and permissions, create an analysis query that specifies a principal and a set of roles and permissions that you want to check for.

These queries can help you answer questions like the following:

  * Who has permission to impersonate service accounts in my organization?
  * Who are the billing administrators in my organization?
  * Who can read data in this BigQuery dataset that contains personally identifiable information (PII)?
  * (API and gcloud CLI only): Who in my organization can read a BigQuery dataset by impersonating a service account?



To learn how to create and send these queries, see [Determine which principals have certain roles or permissions](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#principal-query-all).

### What roles and permissions does this principal have on this resource?

To determine what roles and permissions a principal has on a specific resource, create an analysis query that specifies a principal and a resource that you want to check for permissions on.

These queries can help you answer questions like the following:

  * What roles and permissions does user Sasha have on this BigQuery dataset?
  * What roles and permissions does the `dev-testers` group have on any resource in this project?
  * (API and gcloud CLI only): What roles and permissions does the user Dana have on this BigQuery dataset if Dana impersonates a service account?



To learn how to create and send these queries, see [Determine what access a principal has on a resource](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#access-query).

### Which resources can this principal access?

To determine what resources a specific principal can access, create an analysis query that specifies a principal and the roles and permissions that you want to check for.

These queries can help you answer questions like the following:

  * Which BigQuery datasets does the user Mahan have permission to read?
  * Which BigQuery datasets is the `dev-testers` group the data owner of?
  * What VMs can Tal delete in project A?
  * (API and gcloud CLI only): What VMs can the user John delete by impersonating a service account?



To learn how to create and send these queries, see [Determine which resources a principal can access](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#resource-query).

## Saved analysis queries

If you're using the REST API, you can save analysis queries to reuse or share with others. You can run a saved query just like you would run any other query.

To learn more about saving queries, see [Manage saved queries](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-saved-queries).

## Export query results

You can run queries asynchronously and export query results to BigQuery or Cloud Storage by using `analyzeIamPolicyLongrunning`.

To learn how to export query results to BigQuery, see [Write policy analysis to BigQuery](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-write-to-bigquery).

To learn how to export query results to Cloud Storage, see [Write policy analysis to Cloud Storage](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-write-to-gcs).

## Query options

Policy Analyzer offers several options that add more details to your query results.

To learn how to enable these options, see [Enable options](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#options).

### Group expansion

If you enable group expansion, any groups in the query results are expanded into individual members. This expansion is capped at 1,000 members per group. If you have sufficient group permissions, nested groups will also be expanded. This option is only effective if you don't specify a principal in your query.

For example, imagine you enable group expansion for the query "Who has the `storage.buckets.delete` permission for `project-1`?" If Policy Analyzer finds any groups that have the `storage.buckets.delete` permission, the query results will list not only the group identifier, but also all individual members in the group.

This option lets you understand individual users' access, even if that access is a result of their membership in a group.

### Role expansion

If you enable role expansion, the query results list all permissions inside each role in addition to the role itself. This option is only available if you don't specify any permissions or roles in your query.

For example, imagine you enable role expansion for the query "What access does `my-user@example.com` have on the bucket `bucket-1`?" If Policy Analyzer finds any roles that give `my-user@example.com` access to `bucket-1`, the query results will list not only the role name, but also all permissions included in the role.

This option lets you see exactly what permissions your principals have.

### Resource expansion

If you enable resource expansion for a Policy Analyzer query, the query results list all relevant [descendant resources](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) for any parent resources (projects, folders, and organizations) in the query results. This expansion is capped at 1,000 resources per parent resource for Policy Analyzer queries and 100,000 resources per parent resource for longrunning Policy Analyzer queries.

For example, consider how resource expansion would affect the following queries:

  * Who has the `storage.buckets.delete` permission for `project-1`?

If you enable resource expansion for this query, the resources section of the query results will list not only the project, but also all storage buckets inside the project.

  * Which resources does `my-user@example.com` have the `compute.instances.setIamPolicy` permission on?

If you enable resource expansion for this query and Policy Analyzer finds that `my-user@example.com` has a project-level role that contains that permission, the resources section of the query results will list not only the project, but also all Compute Engine instances inside the project.




This option lets you get a detailed understanding of the resources that your principals can access.

### Service account impersonation

If you are using the REST API or gcloud CLI you can enable analysis of [service account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

If this option is enabled, Policy Analyzer runs additional analysis queries to determine who can impersonate the service accounts that have the specified access to the specified resources. Policy Analyzer runs one query for each service account in query results. These queries analyze who has any of the following permissions on the service account:

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.getOpenIdToken`
  * `iam.serviceAccounts.implicitDelegation`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`



## Quotas and limits

Cloud Asset Inventory enforces the rate of incoming requests, including policy analysis requests, based on the consumer project. Cloud Asset Inventory also limits group expansion within the group memberships and resource expansion within the resource hierarchy.

To see the default quotas and limits for Policy Analyzer, see [Quotas and limits](https://docs.cloud.google.com/asset-inventory/docs/quota#policy_analyzer_expansion_limits) in the Cloud Asset Inventory documentation.

## Pricing

Each organization can execute up to 20 analysis queries per day for no charge. This limit includes both allow policy analysis and organization policy analysis.

If you want to execute more than 20 analysis queries per day, you must have an [organization-level activation of the Premium or Enterprise tier of Security Command Center](https://docs.cloud.google.com/security-command-center/pricing#security-command-center-pricing). For more information, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

## What's next

  * Learn how to use Policy Analyzer to [analyze an allow policy](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies).
  * See how you can use the REST API to [save Policy Analysis queries](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-saved-queries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
