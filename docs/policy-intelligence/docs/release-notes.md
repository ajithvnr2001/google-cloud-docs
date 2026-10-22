---
url: https://docs.cloud.google.com/policy-intelligence/docs/release-notes/
title: Policy Intelligence release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:48.995272+00:00
---

# Policy Intelligence release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Resources ](https://docs.cloud.google.com/policy-intelligence/docs/resources)



Send feedback 

#  Policy Intelligence release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Policy Intelligence. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## September 15, 2026

Feature

Policy Troubleshooter now supports troubleshooting access for [agent identities](https://docs.cloud.google.com/iam/docs/agent-identity-overview). You can troubleshoot IAM allow policies, deny policies, and principal access boundary policies for agents acting under their own authority by entering the agent's principal identifier or by troubleshooting with an error ID from an access denial event. To learn more, see [Troubleshooting access](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access#troubleshoot-access).

## September 09, 2026

Feature

The Policy Assist remote MCP server is available in [Preview](https://cloud.google.com/products#product-launch-stages). To learn about using the Policy Assist remote MCP server to let external AI agents and applications suggest IAM roles, see [Use the Policy Assist remote MCP server](https://docs.cloud.google.com/policy-intelligence/docs/use-policy-assist-mcp) and the [Policy Assist MCP reference](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyassist/mcp).

Feature

The Policy Assist REST API is available in [Preview](https://cloud.google.com/products#product-launch-stages). Policy Assist lets you get IAM role suggestions for individual principals with AI assistance.

To learn about using the Policy Assist API to get role suggestions programmatically, see the [Policy Assist REST reference](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyassist/rest).

## September 01, 2026

Feature

The Policy Analyzer MCP server is [generally available](https://cloud.google.com/products#product-launch-stages). To learn about using the Policy Analyzer MCP server to let agents and AI applications analyze and audit IAM configurations, see [Use the Policy Analyzer remote MCP server](https://docs.cloud.google.com/policy-intelligence/docs/use-policy-analyzer-mcp).

## August 06, 2026

Feature

The Policy Troubleshooter MCP server is [generally available](https://cloud.google.com/products?e=48754805#product-launch-stages). To learn about using the Policy Troubleshooter MCP server to let agents and AI applications troubleshoot IAM issues and errors, see [Use the Policy Troubleshooter remote MCP server](https://docs.cloud.google.com/policy-intelligence/docs/use-policy-troubleshooter-mcp).

## June 12, 2026

Feature

The ability to [remediate access issues](https://docs.cloud.google.com/policy-intelligence/docs/remediate-requests) with Policy Troubleshooter is [generally available](https://cloud.google.com/products#product-launch-stages).

## June 09, 2026

Feature

[Policy Simulator for deny policies](https://docs.cloud.google.com/policy-intelligence/docs/deny-simulator-overview) is [generally available](https://cloud.google.com/products#product-launch-stages).

## June 03, 2026

Feature

You can use Policy Analyzer to visualize allow policy queries. This can help you understand the relationship between identities, roles, permissions, and resources within your resource hierarchy.

Policy Analyzer supports queries about agent identities. You can see who can access an agent or what resources and agents a specific agent can reach.

These features are available in in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Analyze allow policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies).

## May 08, 2026

Feature

You can use the IAM recommender to remediate excessive permissions for Google groups by transitioning from permanent role bindings to temporary, on-demand entitlements in Privileged Access Manager (PAM). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

To learn how to remediate excessive permissions, see [Remediate excessive permissions with Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-remediate-iam-recommendations).

## November 24, 2025

Feature

IAM administrators can review and manage identity risks across their organization, folder, or project from the Google Cloud console by using the **Security Insights** dashboard. For more information, see [Review and manage identity risks](https://docs.cloud.google.com/policy-intelligence/docs/manage-identity-risks).

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## November 13, 2025

Change

[Policy Simulator](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_simulator) deny policy simulations on organization and folder resources are not protected by VPC Service Controls. For more information, see [Help secure Policy Intelligence APIs with VPC Service Controls](https://docs.cloud.google.com/policy-intelligence/docs/secure-apis-vpc-sc#simulator).

## November 04, 2025

Feature

You can use Policy Troubleshooter to troubleshoot policies that include bindings for [service account principal sets](https://docs.cloud.google.com/iam/docs/principal-identifiers#allow-service-account-principal-sets). This feature is available in [GA](https://cloud.google.com/products#product-launch-stages).

## October 22, 2025

Fixed

The issue that caused IAM recommender role recommendations to be inaccurate and out of date is fixed.

## October 16, 2025

Feature

You can use Policy Troubleshooter to [remediate access issues](https://docs.cloud.google.com/policy-intelligence/docs/remediate-requests). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 13, 2025

Issue

Due to an ongoing issue, IAM recommender role recommendations might be out of date and inaccurate. Removing roles or permissions can break existing processes. Therefore, please validate usage before applying any changes.

## July 01, 2025

Feature

[Policy Simulator for Organization Policy](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies) is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## December 19, 2024

Feature

The [Organization Policy recommender](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-recommendations-overview) generates insights and organization policy recommendations to restrict the creation and upload of service account keys. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 16, 2024

Feature

You can use [Policy Simulator for principal access boundary policies](https://docs.cloud.google.com/policy-intelligence/docs/pab-simulator-overview) to simulate changes to principal access boundary policies before you apply them. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 11, 2024

Feature

You can use [Policy Simulator for deny policies](https://docs.cloud.google.com/policy-intelligence/docs/deny-simulator-overview) to simulate changes to deny policies before you apply them. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 15, 2024

Feature

The IAM recommender generates policy insights and role recommendations for the following identities:

  * All identities in a workload identity pool
  * Single identity in a workload identity pool
  * All identities in a workforce identity pool
  * Single identity in a workforce identity pool
  * All Google Kubernetes Engine Pods that use a specific Kubernetes service account



To learn more, see [Availability](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#availability). This feature is generally available.

## July 03, 2024

Change

You can use Policy Troubleshooter to [troubleshoot principal access boundary policies](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 31, 2024

Change

[Activity Analyzer](https://docs.cloud.google.com/policy-intelligence/docs/activity-analyzer-service-account-authentication) checks service activation and quota for the project that you're using to analyze access (the client project) instead of the projects whose resources you're analyzing (the resource projects). As a result, you only need to enable the [Policy Analyzer API](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyanalyzer/rest) in your client project, not in your resource projects.

## May 17, 2024

Feature

The IAM recommender generates policy insights and role recommendations for identities in Workload Identity Federation pools. To learn more, see [Availability](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#availability). This feature is available in Preview.

During Preview, the actual [observation period](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#observation-period) might be shorter than the observation period listed in recommendations for these principals.

## May 03, 2024

Change

Some Policy Intelligence features are only available for customers with [organization-level activations of Security Command Center](https://cloud.google.com/security-command-center/pricing#organization-level-activations). For more information, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

## April 01, 2024

Issue

[Policy Troubleshooter for IAM](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access) currently doesn't fetch tags for regional resources, such as [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters). As a result, if you have IAM policies with [tag-based conditions](https://docs.cloud.google.com/iam/docs/tags-access-control) and you try to use Policy Troubleshooter to troubleshoot access to regional resources, you might get inaccurate results. Our engineering team is working to resolve this issue.

## February 26, 2024

Feature

The IAM recommender offers [role recommendations for BigQuery datasets](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-datasets). Role recommendations help you reduce excess permissions by suggesting role changes based on actual permission usage. This feature is available in Preview.

## January 12, 2024

Change

The requirement that customers have [organization-level activations of Security Command Center](https://cloud.google.com/security-command-center/pricing#organization-level-activations) to use certain Policy Intelligence features has been delayed until April 29, 2024. For more information about which features are affected by this change, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

## November 07, 2023

Feature

You can use the Google Cloud console to [analyze organization policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-organization-policies). This feature is available in Preview.

## September 28, 2023

Announcement

After January 15, 2024, some Policy Intelligence features will only be available for customers with [organization-level activations of Security Command Center](https://cloud.google.com/security-command-center/pricing#organization-level-activations). For more information, see [Billing questions](https://docs.cloud.google.com/policy-intelligence/docs/billing-questions).

Change

Using [Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access) to troubleshoot deny policies is generally available.

## July 05, 2023

Feature

You can use Policy Troubleshooter to [troubleshoot deny policies](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 24, 2023

Change

[Configurable IAM recommendations](https://docs.cloud.google.com/policy-intelligence/docs/configure-role-recommendations) are now generally available. With configurable IAM recommendations, you can set the [minimum observation period](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#observation-period) for the IAM recommender to 30 or 60 days instead of the default period of 90 days.

## December 12, 2022

Change

You can now use the Google Cloud console to [write IAM policy analysis results to BigQuery](https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-write-to-bigquery). This feature is generally available.

## December 05, 2022

Feature

You can now set the [minimum observation period](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#observation-period) for the IAM recommender to 30 or 60 days instead of the default period of 90 days. For more information, see [Configure role recommendation generation](https://docs.cloud.google.com/policy-intelligence/docs/configure-role-recommendations). This feature is available in Preview.

## November 18, 2022

Feature

Policy Analyzer now offers [organization policy analysis](https://docs.cloud.google.com/policy-intelligence/docs/analyze-organization-policies). Policy Analyzer helps you get more information about the resources affected by an organization policy constraint. This feature is available in Preview.

## November 10, 2022

Change

[Role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets) and [policy insights](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights-buckets) for Cloud Storage buckets are now generally available. Additionally, you can now use the Google Cloud console to review bucket-level role recommendations and policy insights.

## August 30, 2022

Change

The user interface for [Policy Troubleshooter](https://docs.cloud.google.com/policy-intelligence/docs/troubleshoot-access) in the Cloud console has been updated to improve usability. To view the new user interface, visit the [Policy Troubleshooter page in the Cloud console](https://console.cloud.google.com/iam-admin/troubleshooter).

## July 08, 2022

Feature

Recommender now offers [role recommendations for Cloud Storage buckets](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets). Role recommendations help you reduce excess permissions by suggesting role changes based on actual permission usage. This feature is available in Preview.

## July 01, 2022

Change

[Lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#lateral-movement-insights), which identify roles that allow a service account in one project to impersonate a service account in another project, are now generally available.

## June 27, 2022

Change

In the Cloud console, [Policy Troubleshooter for IAM allow policies](https://docs.cloud.google.com/policy-intelligence/docs/access-troubleshooters) now reports if there are deny policies that could affect a principal's access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
