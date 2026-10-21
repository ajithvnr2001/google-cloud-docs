---
url: https://docs.cloud.google.com/organization-policy/release-notes/
title: Organization Policy Service release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:29:49.807900+00:00
---

# Organization Policy Service release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Resources ](https://docs.cloud.google.com/organization-policy/resources)



Send feedback 

#  Organization Policy Service release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Organization Policy Service. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/organization-policy-release-notes.xml) directly. 

## September 18, 2026

Feature

The [Organization Policy remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/organization-policy/use-organization-policy-mcp) helps you discover available constraints, evaluate effective inheritance hierarchies across organizations, folders, and projects, and safely author and update organization policies. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 17, 2026

Feature

Organization Policy Service custom constraints are [generally available](https://cloud.google.com/products#product-launch-stages) for Google Cloud NetApp Volumes. For more information, see [Use custom organization policies](https://docs.cloud.google.com/netapp/volumes/docs/secure-control-access/custom-constraints).

## September 10, 2026

Feature

The [Organization Policy remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/organization-policy/use-organization-policy-mcp) helps you discover available constraints, evaluate effective inheritance hierarchies across organizations, folders, and projects, and safely author and update organization policies. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 03, 2026

Feature

You can use the `vertexai.allowOnlyAllCompliantAPIs` legacy managed constraint to restrict Gemini Enterprise Agent Platform requests.

You can use the `container.managed.autopilotPrivilegedAdmission` to enable allowlist-based admission control for privileged Autopilot workloads when creating or updating GKE clusters.

These constraints are [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

Feature

You can use the `container.managed.restrictControlPlaneEgress` managed constraint to require that GKE Control Plane Egress is set to the secure 'NONE' mode. For more information, see [Restrict egress traffic from the API server](https://docs.cloud.google.com/kubernetes-engine/networking/docs/restrict-egress-control-plane).

You can use the `firestore.managed.disableEnhancedTextSearch` to prevent enabling query enhancements for Firestore full text search.

These constraints are [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

## August 14, 2026

Feature

Organization Policy Service custom constraints are [generally available](https://cloud.google.com/products#product-launch-stages) for Agent Identity Auth Manager. For more information, see [Use custom organization policies](https://docs.cloud.google.com/iam/docs/agent-identity-custom-constraints).

## August 03, 2026

Feature

Privileged Access Manager (PAM) custom constraints are available. You can use custom constraints to restrict how users create and modify entitlements and grants. For more information, see [Use custom organization policies for Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-custom-constraints). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 31, 2026

Feature

You can use [custom organization policies](https://docs.cloud.google.com/memorystore/docs/valkey/use-custom-org-policies) to improve the security, compliance, and governance of your Memorystore for Valkey instances by enforcing consistent configurations and restrictions for the instances. This ensures that your instances adhere to security best practices and regulatory requirements. This feature is [generally available](https://docs.cloud.google.com/products#product-launch-stages).

## July 07, 2026

Feature

Organization Policy Service custom constraints are [generally available](https://cloud.google.com/products#product-launch-stages) for VMware Engine. For more information, see [Use custom organization policies](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints).

## July 06, 2026

Feature

You can use Organization Policy Service custom constraints to manage specific operations on continuous materialized views. This feature is [generally available](https://cloud.google.com/products#product-launch-stages). For more information, see [Use custom organization policies](https://docs.cloud.google.com/bigtable/docs/custom-constraints).

## June 30, 2026

Feature

You can limit [authorization key](https://docs.cloud.google.com/docs/authentication/api-keys#api-keys-bound-sa) creation to specific services by using the (`constraints/iam.managed.disableServiceAccountApiKeyCreation`) organization policy constraint. When users create an authorization key, they must add an API restriction that matches a service allowed by the constraint.

For more information, see [Limit creation of authorization keys to specific services](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#disable_service_account_api_key_creation).

## June 22, 2026

Change

Custom constraints can be deleted, allowing the name to be reused. For more information, see [Delete a custom constraint](https://docs.cloud.google.com/organization-policy/create-custom-constraints#delete_custom_constraint).

## June 09, 2026

Feature

Organization Policy Service custom constraints are [generally available](https://cloud.google.com/products#product-launch-stages) for Cloud Domains. For more information, see [Use custom organization policies](https://docs.cloud.google.com/domains/docs/custom-constraints).

## April 24, 2026

Feature

Organization Policy Service custom constraints are [generally available](https://cloud.google.com/products#product-launch-stages) for some Service Networking resources. For more information, see [Restrict private connections with organization policies](https://docs.cloud.google.com/vpc/docs/private-services-access#org-policies).

## April 07, 2026

Feature

Managed workload identity and Workload Identity Federation custom constraints are available. For more information, see [Custom organization policy constraints for managed workload identity](https://docs.cloud.google.com/iam/docs/managed-workload-identity-custom-constraints) and [Custom organization policy constraints for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints).

## March 26, 2026

Feature

You can use Gemini Cloud Assist to create and test custom organization policy constraints. For more information, see [Test custom constraints with Gemini Cloud Assist](https://docs.cloud.google.com/organization-policy/test-constraints-gca). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 15, 2026

Deprecated

Control of MCP use with organization policies is deprecated. After March 17, 2026, organization policies that use the `gcp.managed.allowedMCPServices` constraint won't work, and you can control MCP use with Identity and Access Management deny policies. For more information about controlling MCP use, see [Control MCP use with IAM](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## February 09, 2026

Feature

Organization Policy Service custom constraints are available for some Network Connectivity resources. For more information, see [Manage VPC resources by using custom organization policies](https://docs.cloud.google.com/vpc/docs/custom-constraints).

## February 02, 2026

Feature

Organization Policy Service custom constraints are available for some Artifact Analysis resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/artifact-analysis/docs/custom-constraints).

Organization Policy Service custom constraints are available for some Storage Transfer Service resources. For more information, see [Custom organization policy constraints](https://docs.cloud.google.com/storage-transfer/docs/custom-constraints).

## November 13, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Dataform resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## November 11, 2025

Change

The list of organization policy constraints that are enforced when an organization resource is created has changed. The following Google Cloud security baseline constraints are enforced for all organizations created on or after May 3, 2024:

  * `constraints/iam.managed.disableServiceAccountKeyCreation`
  * `constraints/iam.managed.disableServiceAccountKeyUpload`
  * `constraints/iam.automaticIamGrantsForDefaultServiceAccounts`
  * `constraints/iam.allowedPolicyMemberDomains`
  * `constraints/essentialcontacts.managed.allowedContactDomains`
  * `constraints/compute.managed.restrictProtocolForwardingCreationForTypes`
  * `constraints/storage.uniformBucketLevelAccess`



For more information, see [Manage baseline constraints](https://docs.cloud.google.com/organization-policy/manage-baseline-constraints).

## November 05, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some BigQuery resources. For more information, see [Manage BigQuery resources using custom constraints](https://docs.cloud.google.com/bigquery/docs/custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 30, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Certificate Authority Service resources. For more information, see [Manage Certificate Authority Service resources using custom constraints](https://docs.cloud.google.com/certificate-authority-service/docs/custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for managed workload identities. For more information, see [Use custom organization policies for Managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some BigQuery sharing resources. For more information, see [Manage Sharing data exchanges and listings using custom constraints](https://docs.cloud.google.com/bigquery/docs/analytics-hub-custom-constraints). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## October 14, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Datastream resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/datastream/docs/custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 10, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Application Integration resources. For more information, see [Manage Application Integration resources using custom constraints](https://docs.cloud.google.com/application-integration/docs/custom-constraints). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 06, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Dataform resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dataform/docs/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 03, 2025

Feature

Select Workload Identity Federation resources let you use custom constraints to define your own restrictions on Google Cloud services. To learn which Workload Identity Federation resources support custom constraints and to view sample use cases, see [Use custom organization policies for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-custom-constraints).

This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## September 18, 2025

Feature

Select Cloud Load Balancing resources let you use custom constraints to define your own restrictions on Google Cloud services. To learn which Cloud Load Balancing resources support custom constraints and to view sample use cases, see [Manage Cloud Load Balancing resources using custom constraints](https://docs.cloud.google.com/load-balancing/docs/custom-constraints).

This feature is available in **General Availability**.

## September 11, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Live Stream API resources. For more information, see [Use custom constraints](https://docs.cloud.google.com/livestream/docs/custom-constraints).

## September 09, 2025

Feature

**Preview:** Eight new organization policy constraints are available to help you enforce security best practices for Compute Engine virtual machine (VM) instances.

These [managed constraints](https://docs.cloud.google.com/organization-policy/overview#managed-constraints) simplify governance for common security scenarios and integrate with safe rollout tools like [dry-run](https://docs.cloud.google.com/organization-policy/test-policies) and [simulation](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies), letting you test their impact before enforcement.

The new constraints are as follows:

  * `compute.managed.disableNestedVirtualization`
  * `compute.managed.disableSerialPortAccess`
  * `compute.managed.disableSerialPortLogging`
  * `compute.managed.disallowGlobalDns`
  * `compute.managed.requireOsConfig`
  * `compute.managed.requireOsLogin`
  * `compute.managed.vmCanIpForward`
  * `compute.managed.vmExternalIpAccess`



These constraints can evaluate metadata values at the [VM instance, project, or zonal level](https://cloud.google.com/compute/docs/metadata/overview#metadata-directories). For more information about these managed constraints, see the list of [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints#managed-constraints).

## September 08, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Cloud Deploy resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/deploy/docs/custom-org-policy).

## August 28, 2025

Fixed

Certain organization policy [managed constraints](https://docs.cloud.google.com/organization-policy/overview#managed-constraints) that were released on August 21, 2025 were not functioning as intended. The Organization Policy Service evaluated these constraints as if the `effectiveInstanceMetadata` field of the resources that they were enforced on was empty, causing them to always evaluate to either allow or deny access to the resource.

The following managed constraints were evaluated to always allow creation of resources where they were enforced:

  * `constraints/compute.managed.disableGuestAttributesAccess`
  * `constraints/compute.managed.disableSerialPortAccess`
  * `constraints/compute.managed.disableSerialPortLogging`



The following managed constraints were evaluated to always block creation of resources where they were enforced:

  * `constraints/compute.managed.disallowGlobalDns`
  * `constraints/compute.managed.requireOsConfig`
  * `constraints/compute.managed.requireOsLogin`



This issue has been corrected, and these constraints now properly evaluate the `effectiveInstanceMetadata` field to determine whether resource creation should be allowed or blocked.

## August 18, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Backup for GKE resources. For more information, see [Manage Backup for GKE resources using custom constraints](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints). This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

Feature

You can now use organization policy conditions to match a tag key. This lets you enable or disable enforcement against all resources with that tag key, regardless of what tag value is attached. For more information, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

## July 25, 2025

Issue

Organization policies in dry-run mode are reporting inconsistent results for the following [managed constraints](https://docs.cloud.google.com/organization-policy/overview#managed_constraints):

  * `constraints/compute.managed.restrictProtocolForwardingCreationForTypes`
  * `constraints/iam.managed.allowedPolicyMembers`
  * `constraints/essentialcontacts.managed.allowedContactDomains`
  * `constraints/compute.managed.blockPreviewFeatures`



If a resource inherited an organization policy in dry-run mode that uses any of these managed constraints, that dry-run policy was evaluated without using the parameters specified in the live policy. Normally, an organization policy in dry-run mode that's inherited on a resource is overridden by the live organization policy set directly on that same resource. Not evaluating the live organization policy parameters in the inherited organization policy in dry-run mode led to inconsistent results.

Our engineering team is working to resolve this issue.

## July 01, 2025

Feature

[Policy Simulator for Organization Policy](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies) is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## June 13, 2025

Feature

Custom organization policies are now generally available for some API keys. For more information, see [Creating and managing custom constraints](https://docs.cloud.google.com/api-keys/docs/custom-constraints).

## June 10, 2025

Change

You can use custom constraints with organization policies to provide more granular control over specific fields for indexes and index endpoints in Vector Search. For more information, see [Create custom constraints for Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/custom-constraints).

## May 15, 2025

Feature

Support for [creating custom organization policy constraints in Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/custom-constraints) and for [creating custom organization policy constraints in Eventarc Standard](https://docs.cloud.google.com/eventarc/standard/docs/custom-constraints) is generally available for some Eventarc resources.

## May 12, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Cloud Quotas resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/docs/quotas/custom-constraints). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 06, 2025

Feature

You can use custom constraints with organization policies to provide more granular control over specific fields for some Knowledge Catalog and data lineage resources. For more information, see [Manage Knowledge Catalog resources using custom constraints](https://docs.cloud.google.com/dataplex/docs/dataplex-custom-constraints) and [Manage data lineage resources using custom constraints](https://docs.cloud.google.com/dataplex/docs/lineage-custom-constraints). This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 17, 2025

Feature

Custom organization policies are now generally available for Filestore. For more information, see [Creating custom constraints for Filestore](https://docs.cloud.google.com/filestore/docs/create-custom-constraints).

## April 08, 2025

Feature

Custom organization policies are now generally available for Identity-Aware Proxy. For more information, see [Use custom organization policies](https://docs.cloud.google.com/iap/docs/custom-org-policies).

## March 26, 2025

Feature

Custom organization policies are now available in [Preview](https://cloud.google.com/products#product-launch-stages) for Resource Manager. For more information, see [Create custom constraints](https://docs.cloud.google.com/resource-manager/docs/custom-constraints).

## March 21, 2025

Feature

Custom organization policies are now generally available for Access Context Manager and VPC Service Controls. For more information, see [Manage Access Context Manager resources with custom constraints](https://docs.cloud.google.com/access-context-manager/docs/custom-constraints) and [Create custom constraints for VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/custom-constraints).

## March 18, 2025

Feature

Custom organization policies are now generally available for Cloud Service Mesh. For more information, see [Set up custom constraints](https://docs.cloud.google.com/service-mesh/docs/service-routing/custom-constraints).

## March 17, 2025

Feature

You can enforce mandatory tags on resources using custom organization policies. When a user attempts to create a resource, the system checks for the presence of the mandatory tags. If any mandatory tag is missing or does not have a value, the resource creation is blocked. By defining mandatory tags within an organization policy, you can ensure that all newly created resources adhere to your organization's tagging standards. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Enforcing mandatory tags on resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#enforcing_mandatory_tags).

## March 14, 2025

Feature

Custom organization policies are now generally available for Managed Service for Apache Airflow. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/composer/docs/composer-3/create-custom-constraints).

## February 27, 2025

Feature

Custom organization policies are now generally available for the Video Stitcher API. For more information, see [Create custom constraints for the Video Stitcher API](https://docs.cloud.google.com/video-stitcher/docs/how-to/create-custom-constraints).

Feature

Custom organization policies are now generally available for Service Management. For more information, see [Manage Service Management resources with custom constraints](https://docs.cloud.google.com/service-infrastructure/docs/service-management/custom-constraints).

## February 20, 2025

Feature

Custom organization policies are now generally available for Cloud Healthcare API. For more information, see [Use custom organization policies](https://docs.cloud.google.com/healthcare-api/docs/custom-org-policy).

## February 19, 2025

Feature

Custom organization policies are now generally available for Essential Contacts. For more information, see [Creating custom constraints for Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/essentialcontacts-custom-org-policies).

## February 14, 2025

Feature

Custom organization policies are now generally available for Cloud Logging. For more information, see [Use custom organization policies](https://docs.cloud.google.com/logging/docs/custom-constraints).

## February 13, 2025

Feature

Custom organization policies are now generally available for security posture resources. For more information, see [Add a custom organization policy](https://docs.cloud.google.com/security-command-center/docs/security-posture-custom-constraints).

## February 11, 2025

Feature

Custom organization policies are now generally available for Identity-Aware Proxy. For more information, see [Use custom organization policies](https://docs.cloud.google.com/iap/docs/custom-org-policies).

Feature

Custom organization policies are now generally available for Developer Connect. For more information, see [Create custom organization policies](https://docs.cloud.google.com/developer-connect/docs/custom-constraints).

Feature

Custom organization policies are now generally available for Cloud DNS. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/dns/docs/create-custom-constraints).

Feature

Custom organization policies are now generally available for Managed Service for Apache Spark. For more information, see [Use custom constraints](https://docs.cloud.google.com/dataproc-serverless/docs/guides/dataproc-serverless-custom-constraints).

Feature

Custom organization policies are now generally available for Spanner. For more information, see [Add a custom organization policy](https://docs.cloud.google.com/spanner/docs/spanner-custom-constraints).

## February 06, 2025

Feature

You can now create custom organization policies for Workflows. For more information, see [Create custom organization policy constraints for Workflows](https://docs.cloud.google.com/workflows/docs/custom-constraints).

## February 05, 2025

Feature

You can now create custom organization policies for Cloud Monitoring alerting policies, notification channels, and snoozes. For more information, see [Use custom organization policies](https://docs.cloud.google.com/monitoring/docs/custom-constraints).

## January 21, 2025

Feature

You can use custom constraints with Organization Policy Service to provide more granular control over specific fields for some Cloud Data Fusion resources. For more information, see [Create custom organization policy constraints](https://docs.cloud.google.com/data-fusion/docs/how-to/create-custom-constraints).

## January 15, 2025

Feature

You can use custom constraints with Organization Policy Service to provide more granular control over specific fields for some reCAPTCHA resources. For more information, see [Use custom organization policies for reCAPTCHA keys and firewall policies](https://docs.cloud.google.com/recaptcha/docs/custom-constraints).

## December 19, 2024

Feature

The [Organization Policy recommender](https://docs.cloud.google.com/policy-intelligence/docs/organization-policy-recommendations-overview) generates insights and organization policy recommendations to restrict the creation and upload of service account keys. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

You can use the `iam.managed.allowedPolicyMembers` managed organization policy constraint to implement domain restricted sharing. For more information, see [Domain restricted sharing](https://docs.cloud.google.com/organization-policy/domain-restricted-sharing).

Feature

You can use custom constraints with Organization Policy Service to provide more granular control over specific fields for some Secure Source Manager resources. For more information, see [Manage resources with custom constraints](https://docs.cloud.google.com/secure-source-manager/docs/custom-constraints).

## December 17, 2024

Feature

You can use Organization Policy Service custom constraints to manage specific operations on Bigtable resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/bigtable/docs/custom-constraints). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## December 16, 2024

Feature

Cloud Load Balancing resources now let you use custom constraints to define your own restrictions on Google Cloud services. To learn about which load balancing resources support custom constraints, and some sample use cases, see [Manage Cloud Load Balancing resources using custom constraints](https://docs.cloud.google.com/load-balancing/docs/custom-constraints).

This feature is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## December 09, 2024

Feature

You can use the `iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` managed organization policy constraint to prevent default service accounts from being granted the Editor (`roles/editor`) or Owner (`roles/owner`) roles. For more information, see [Prevent the Owner and Editor role from being granted to default service accounts](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#prevent-service-account-grants).

Change

Using Identity and Access Management attributes in custom organization policies is generally available. For more information, see [Use custom organization policies](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints).

## December 06, 2024

Feature

You can now [manage Firestore resources using Organization Policy Service custom constraints](https://docs.cloud.google.com/firestore/docs/custom-constraints).

## October 29, 2024

Feature

[Organization policy managed constraints](https://docs.cloud.google.com/organization-policy/overview#managed_constraints) are a set of constraints built on the [custom organization policy](https://docs.cloud.google.com/organization-policy/overview#custom-constraints) platform. You can use managed constraints in place of certain predefined constraints to perform dry-run tests and simulate changes to your policies using [Policy Intelligence tools](https://docs.cloud.google.com/organization-policy/overview#policy-intelligence). This feature is now in [General Availability](https://cloud.google.com/products#product-launch-stages).

## May 03, 2024

Announcement

Starting on June 16, 2024, if you don't set a value for the [`iam.serviceAccountKeyExposure` organization policy constraint](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#disable-exposed-keys), Google Cloud will default to the behavior described for `DISABLE_KEY`.

## February 12, 2024

Feature

[Policy Analyzer for Organization Policy](https://docs.cloud.google.com/policy-intelligence/docs/analyze-organization-policies) is now in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 06, 2024

Feature

You can use the Google Cloud console with Policy Simulator for Organization Policy to [test organization policies](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## December 20, 2023

Feature

The [dry-run feature for organization policy](https://docs.cloud.google.com/organization-policy/test-policies) is now in [General Availability](https://cloud.google.com/products#product-launch-stages).

## December 12, 2023

Feature

Organization policy custom constraints allow you to [configure customizable organization policies](https://docs.cloud.google.com/organization-policy/create-custom-constraints) to prevent the misconfiguration of resources and help you meet your security and compliance goals. This feature is now in [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 07, 2023

Feature

You can use the Google Cloud console to [analyze organization policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-organization-policies). This feature is available in Preview.

## July 27, 2023

Feature

Policy Simulator for Organization Policy allows you to [test organization policies](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies) before they are enforced. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

New organization policy constraints have launched into general availability to define service attachment controls for Private Service Connect consumers. For more information, see [Manage security for Private Service Connect consumers](https://docs.cloud.google.com/vpc/docs/manage-security-private-service-connect-consumers).

## July 26, 2023

Feature

Two automatically configured organization policy constraints have launched into general availability to provide advanced regulatory control for Assured Workloads. For more information, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

Feature

New organization policy constraints have launched into general availability to define access and creation controls for Vertex AI Workbench notebooks and instances. For more information, see [Organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).

## June 16, 2023

Feature

You can now monitor how [custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints) would impact your organization's workflows by setting custom constraints in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies).

## April 18, 2023

Feature

You can now [test organization policies](https://docs.cloud.google.com/organization-policy/test-policies) using the Google Cloud console.

## March 08, 2023

Feature

You can now [test organization policies](https://docs.cloud.google.com/organization-policy/test-policies) to monitor how policy changes would impact your workflows before they are enforced.

## November 18, 2022

Feature

Policy Analyzer now offers [organization policy analysis](https://docs.cloud.google.com/policy-intelligence/docs/analyze-organization-policies). Policy Analyzer helps you get more information about the resources affected by an organization policy constraint. This feature is available in Preview.

## August 24, 2022

Feature

Organization policy custom constraints have launched into public preview. Custom constraints can allow or restrict access to API calls in the same way that predefined constraints do, but allow administrators to configure conditions based on request parameters and other metadata. For more information, see [Create custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints).

## August 02, 2022

Feature

Two organization policy constraints have launched into general availability to help ensure CMEK usage across an organization. For more information, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## June 14, 2022

Feature

The following [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) to restrict resource creation of global security configuration have launched into general availability:

  * Disable Creation of Google Cloud Armor Security Policies
  * Disable Creation of global self-managed SSL Certificates
  * Disable Global Load Balancing
  * Disable Enabling Identity-Aware Proxy (IAP) on global resources
  * Disable Enabling IAP on regional resources



## May 04, 2022

Feature

The [resource usage restriction](https://docs.cloud.google.com/organization-policy/restrict-services) organization policy constraint has launched into general availability.

## September 20, 2021

Feature

The Organization Policy Service v2 API reference documentation is now available. For more information, see the [API reference documentation](https://docs.cloud.google.com/organization-policy/reference/rest).

## August 09, 2021

Feature

You can now use the Google Cloud console to manage your organization policies with tags. For more information, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

## July 27, 2021

Feature

The organization policy constraints [**Allowed ingress settings** and **Allowed VPC egress settings** for Cloud Run](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) have launched into general availability.

## March 16, 2021

Feature

The Organization Policy Service v2 API has launched into general availability.

  * You can now apply conditions for the enforcement of organization policies. For more information, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).
  * For more details about the v2 version of the API, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).



## September 24, 2020

Feature

The organization policy constraints for [Direct Path disablement](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) have launched into beta.

## August 26, 2020

Feature

The organization policy constraint for [Cloud NAT](https://docs.cloud.google.com/nat/docs/org-policy-constraints) has launched into beta.

## August 19, 2020

Feature

The organization policies for [restricting Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage) have launched into beta.

The organization policy for [restricting protocol forwarding creation](https://docs.cloud.google.com/compute/docs/protocol-forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization) has launched into general availability.

The organization policy for [restricting Cloud Load Balancing creation](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints) has launched into general availability.

## August 14, 2020

Feature

The organization policy for [extending the maximum lifetime for OAuth 2.0 access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) that you create for a service account has been launched into general availability.

## July 20, 2020

Feature

The organization policy for [enabling detailed Cloud Audit Logs](https://docs.cloud.google.com/storage/docs/org-policy-constraints#audit-logging) has launched into general availability.

## July 17, 2020

Feature

The organization policy for [restricting protocol forwarding creation](https://docs.cloud.google.com/compute/docs/protocol-forwarding#enforcing_protocol_forwarding_settings_across_a_project_folder_or_organization) has launched into public beta.

## July 01, 2020

Feature

The organization policy for [restricting automatic Identity and Access Management permission grants to new service accounts](https://docs.cloud.google.com/organization-policy/restrict-service-accounts#disable_service_account_default_grants) has launched into general availability.

## June 15, 2020

Feature

The organization policy for [restricting peer IP addresses through a Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#vpn-org-policy) has been launched into general availability.

## April 10, 2020

Feature

The Organization Policy Service resource locations constraint has launched for general availability. This constraint allows you to define the location where your resources are created, providing important data location compliance tools. For more information, see the [Restrict resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations).

## January 30, 2020

Feature

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) helps you to set up a secure perimeter to guard against data exfiltration. The [VPC Service Controls organization policies](https://docs.cloud.google.com/functions/docs/securing/using-vpc-service-controls) have been launched into public beta.

## January 10, 2020

Feature

The [domain-restricted sharing](https://docs.cloud.google.com/organization-policy/domain-restricted-sharing) organization policies have been launched into general availability.

## September 12, 2019

Feature

The organization policies for [service account management](https://docs.cloud.google.com/organization-policy/restrict-service-accounts) have been launched into general availability.

## June 26, 2019

Feature

Resource location restriction constraint beta release

The Organization Policy Service resource locations constraint allows you to define the location where your resources are created. For more information, see the [quickstart](https://docs.cloud.google.com/organization-policy/quickstart) or the [how-to guide](https://docs.cloud.google.com/organization-policy/restrict-locations).

## October 11, 2018

Feature

Organization policy administrative UI beta release

The Organization Policy Service administrative UI allows you to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies) in the Google Cloud console.

## July 12, 2018

Feature

[Service account restriction](https://docs.cloud.google.com/organization-policy/restrict-service-accounts) organization policy constraint beta release

The service account restriction constraint can be used to limit the usage of Identity and Access Management service accounts.

## July 09, 2018

Feature

Domain restriction organization policy constraint beta release

The [domain restriction](https://docs.cloud.google.com/organization-policy/restrict-domains) constraint can be used to restrict the set of identities that can be used in Identity and Access Management policies.

## July 27, 2017

Feature

Organization Policy Service General Availability

The [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview) gives you central, programmatic control over your organization's Google Cloud resources. It provides a simple mechanism for you to restrict allowed configurations across your entire cloud resource hierarchy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
