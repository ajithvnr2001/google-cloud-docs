---
url: https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-best-practices/
title: Role recommendations best practices \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:49.498804+00:00
---

# Role recommendations best practices  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Role recommendations best practices Stay organized with collections  Save and categorize content based on your preferences. 

We recommend the following best practices for managing role recommendations.

For more information about role recommendations, see the [role recommendation overview](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).

## Getting started with recommendations

The following best practices can help you get started with role recommendations.

  * **Begin with an initial cleanup of over-granted permissions.** Initially, you might see a very large number of recommendations, especially if many principals have highly permissive roles like Editor. Take the time to address all recommendations in your project or organization to ensure that all of your principals have the appropriate roles.

When doing this initial cleanup, prioritize the following types of recommendations:

    * **Recommendations that reduce permissions for service accounts.** By default, all [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default) are granted the highly permissive Editor role on projects. Other service accounts that you manage might also have been granted highly permissive roles. All over-granted permissions increase your security risk, including overly privileged service accounts, so we recommend prioritizing overly privileged service accounts during your initial cleanup.

    * **Recommendations that help prevent privilege escalation.** Roles that let principals act as a service account (`iam.serviceAccounts.actAs`) or get or set the allow policy for a resource can potentially let a principal escalate their own privilege. Prioritize recommendations relating to these roles.

    * **Recommendations that reduce lateral movement.** Lateral movement is when a service account in one project has permission to impersonate a service account in another project. This permission can result in a chain of impersonations across projects that gives principals unintended access to resources. To mitigate this unintended access, prioritize recommendations that are associated with [lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights).

    * **Recommendations with a high priority level.** IAM recommendations are automatically assigned priority levels based on the role bindings they're associated with. Prioritize recommendations with a high priority level to quickly reduce over-granted permissions.

To learn how a recommendation's priority is determined, see [Recommendation priority](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#priority).

    * **When you find an over-privileged principal in one project, check other projects for recommendations involving that principal.** If a principal has been granted an overly permissive role in one project, it is possible that they have been granted overly permissive roles in other projects as well. Review recommendations for the principal across multiple projects to globally reduce the principal's access to the appropriate level.

  * After the initial cleanup, **check your recommendations regularly.** We recommend that you check your recommendations at least once a week. This check will usually take much less time than the initial cleanup, because you will only need to address recommendations for changes that have occurred since the last cleanup or check.

Regularly checking permissions reduces the work required for each check, and can help you proactively identify and remove inactive users, as well as continue to downscope permissions for active users.




## Best practices for working with recommendations

If you use the [Recommender API](https://docs.cloud.google.com/recommender/docs/reference/rest) or the [`recommender` commands for the gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/recommender) to manage recommendations, make sure to update the state of recommendations that you apply. This allows you to keep track of your recommendations and ensures that the changes you make appear in your [recommendations logs](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations#logs).

Before you apply a recommendation, review it carefully and make sure you understand when it was last refreshed and how it will change the principal's access to Google Cloud resources.

## Best practices for applying recommendations automatically

To manage your recommendations more efficiently, you might want to automate the process of applying recommendations. If you decide to use automation, keep the following points in mind.

Recommender tries to provide recommendations that will not cause breaking changes in access. For example, we will never recommend a role that excludes permissions that a principal has used, [passively or actively](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#permissions-used), in the last 90 days. We also use [machine learning](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#ml) to identify other permissions that the user is likely to need.

However, we cannot guarantee that our recommendations will never cause breaking changes in access—it is possible that applying a recommendation will result in a principal being unable to access a resource that they need. We recommend reviewing [How the IAM recommender works](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-recommender-works) and deciding how much automation you are comfortable with. For example, you might decide to apply most recommendations automatically, but require a manual review for recommendations that add or remove a certain number of permissions, or that involve granting or revoking a specific role.

When automating recommendations, you might want to identify which resource a recommendation is for. To identify the resource, use the `operation.resource` field. Other fields, such as the `name` field, will not always represent the resource that the recommendation is for.

## What's next

  * Understand [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview).
  * Learn the steps for [reviewing and applying recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations).
  * Find out how to [export data for IAM recommendations](https://docs.cloud.google.com/policy-intelligence/docs/export-role-recommendations-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
