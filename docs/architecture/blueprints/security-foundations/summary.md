---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary/
title: Deploy the blueprint \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:55.355440+00:00
---

# Deploy the blueprint  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy the blueprint Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

This section describes the process that you can use to deploy the blueprint, its naming conventions, and alternatives to blueprint recommendations.

## Bringing it all together

To deploy your own enterprise foundation in alignment with the best practices and recommendations from this blueprint, follow the high-level tasks summarized in this section. Deployment requires a combination of prerequisite setup steps, automated deployment through the [terraform-example-foundation](https://github.com/terraform-google-modules/terraform-example-foundation) on GitHub, and additional steps that must be configured manually after the initial foundation deployment is complete.

Process | Steps  
---|---  
Prerequisites before deploying the foundation pipeline resources | Complete the following steps before you deploy the foundation pipeline:

  * [Create a Cloud Identity account and verify domain ownership](https://docs.cloud.google.com/docs/enterprise/setup-checklist#checklist-section-1).
  * [Apply for an invoiced billing account](https://docs.cloud.google.com/billing/docs/how-to/invoiced-billing) with your Google Cloud sales team or create a [self-service billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).
  * Enforce [security best practices](https://support.google.com/a/answer/9011373) for administrator accounts.
  * Verify and reconcile [issues with consumer user accounts](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization#issues_with_consumer_user_accounts).
  * Configure your [external identity provider as source of truth](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization#external_identity_provider_as_the_source_of_truth) for synchronizing user accounts and SSO.
  * Provision the [groups for access control](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization#groups_for_access_control) that are required to run the blueprint.
  * Determine the [network topology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#network_topology) that you will use.
  * Decide your source code management tool. The instructions for terraform-example-foundation are written to a Git repository that is hosted in Cloud Source Repositories.
  * Decide your CI/CD automation tools. The terraform-example-foundation provides different sets of directions for different automation tools.

To connect to an an existing on-premises environment, prepare the following:

  * Plan your [IP address allocation](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#ip-address-allocation) based on the number and size of ranges that are required by the blueprint.
  * Order your [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) connections.

  
Steps to deploy the terraform-example-foundation from GitHub | Follow the README directions for each stage to deploy the [terraform-example-foundation](https://github.com/terraform-google-modules/terraform-example-foundation) from GitHub:

  * Stage [`0-bootstrap`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/0-bootstrap) to create a foundation pipeline. If using a self-service billing account, you must [request additional project quota](https://github.com/terraform-google-modules/terraform-example-foundation/blob/4d7e822b85d6c21c28389e82b3794b9e1554ebc6/docs/FAQ.md?plain=1#L9) before proceeding to the next stage.
  * Stage [`1-org`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/1-org) to configure organization-level resources.
  * Stage [`2-environments`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/2-environments) to create environments.
  * Stage either [`3-networks-dual-svpc`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/3-networks-dual-svpc) `or` [`3-networks-hub-and-spoke`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/3-networks-hub-and-spoke) to create networking resources in your preferred topology.
  * Stage [`4-projects`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/4-projects) to create an infrastructure pipeline.
  * Optionally, stage [`5-app-infra`](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/5-app-infra) for sample usage of the infrastructure pipeline.

  
Additional steps after IaC deployment | After you deploy the Terraform code, complete the following:

  * Complete the [on-premises configuration changes](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#on-premises_configuration_changes).
  * [Activate Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).
  * [Export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).
  * Sign up for a [Cloud Customer Care plan](https://docs.cloud.google.com/support).
  * [Enable Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable) logs.
  * [Share data from Cloud Identity with Google Cloud](https://support.google.com/a/answer/9320190).
  * Apply the [administrative controls for Cloud Identity](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization#administrative-controls-for-cloud-identity) which aren't automated by the IaC deployment.
  * Assess which of the [additional administrative controls for customers with sensitive workloads](https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary#additional_administrative_controls_for_customers_with_sensitive_workloads) are appropriate for your use case.
  * Review [operation best practices](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices) and plan how to connect your existing operations and capabilities to the foundation resources.

  
  
## Additional administrative controls for customers with sensitive workloads

Google Cloud provides additional administrative controls that can help your security and compliance requirements. However, some controls involve additional cost or operational trade-offs that might not be appropriate for every customer. These controls also require customized inputs for your specific requirements that can't be fully automated in the blueprint with a default value for all customers.

This section introduces security controls that you apply centrally to your foundation. This section isn't intended to be exhaustive of all the security controls that you can apply to specific workloads. For more information on Google's security products and solutions, see [Google Cloud security best practices center](https://cloud.google.com/security/best-practices).

Evaluate whether the following controls are appropriate for your foundation based on your compliance requirements, risk appetite, and sensitivity of data.

Control | Description  
---|---  
[Protect your resources with VPC Service Controls](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#protect-resources) | VPC Service Controls lets you define security policies that prevent access to Google-managed services outside of a trusted perimeter, block access to data from untrusted locations, and mitigate data exfiltration risks. However, VPC Service Controls can cause existing services to break until you define exceptions to allow intended access patterns.Evaluate whether the value of mitigating exfiltration risks justifies the increased complexity and operational overhead of adopting VPC Service Controls. The blueprint prepares prerequisite network controls and a dry-run VPC Service Controls perimeter, but the perimeter isn't enforced until you take additional steps.  
[Restrict resource locations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) | You might have regulatory requirements that cloud resources must only be deployed in approved geographical locations. This organization policy constraint enforces that resources can only be deployed in the list of locations you define.  
[Enable Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) | Assured Workloads provides additional compliance controls that help you meet specific regulatory regimes. The blueprint provides optional variables in the deployment pipeline for enablement.  
[Enable data access logs](https://docs.cloud.google.com/logging/docs/audit#data-access) | You might have a requirement to log all access to certain sensitive data or resources.Evaluate where your workloads handle sensitive data that requires data access logs, and enable the logs for each service and environment working with sensitive data.  
[Enable Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) | Access Approval ensures that Cloud Customer Care and engineering require your explicit approval whenever they need to access your customer content.Evaluate the operational process required to [review Access Approval requests](https://docs.cloud.google.com/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys#review) to mitigate possible delays in resolving support incidents.  
[Enable Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview#onboarding) | Key Access Justifications lets you programmatically control whether Google can access your encryption keys, including for automated operations and for Customer Care to access your customer content.Evaluate the cost and operational overhead associated with Key Access Justifications as well as its dependency on [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm#overview).  
[Disable Cloud Shell](https://docs.cloud.google.com/shell/docs/resetting-cloud-shell#disable_for_managed_user_accounts) | [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) is an online development environment. This shell is hosted on a Google-managed server outside of your environment, and thus it isn't subject to the controls that you might have implemented on your own developer workstations.If you want to strictly control which workstations a developer can use to access cloud resources, disable Cloud Shell. You might also evaluate [Cloud Workstations](https://docs.cloud.google.com/workstations/docs/overview) for a configurable workstation option in your own environment.  
[Restrict access to the Google Cloud console](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis) | Google Cloud lets you restrict access to the Google Cloud console based on [access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes) like group membership, trusted IP address ranges, and device verification. Some attributes require an additional subscription to [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview).Evaluate the access patterns that you trust for user access to web-based applications such as the console as part of a larger [zero trust deployment](https://cloud.google.com/blog/topics/developers-practitioners/zero-trust-and-beyondcorp-google-cloud).  
  
## Naming conventions

We recommend that you have a standardized naming convention for your Google Cloud resources. The following table describes recommended conventions for resource names in the blueprint.

Resource | Naming convention  
---|---  
Folder | `fldr-environment``environment` is a description of the folder-level resources within the Google Cloud organization. For example, `bootstrap`, `common`, `production`, `nonproduction`, `development`, or `network`.For example: `fldr-production`  
Project ID | `prj-environmentcode-description-randomid`

  * `environmentcode` is a short form of the environment field (one of `b`, `c`, `p`, `n`, `d`, or `net`). Shared VPC host projects use the `environmentcode` of the associated environment. Projects for networking resources that are shared across environments, like the `interconnect` project, use the `net` environment code.
  * `description` is additional information about the project. You can use short, human-readable abbreviations.
  * `randomid` is a randomized suffix to prevent collisions for resource names that must be globally unique and to mitigate against attackers guessing resource names. The blueprint automatically adds a random four-character alphanumeric identifier.

For example: `prj-c-logging-a1b2`  
VPC network | `vpc-environmentcode-vpctype`

  * `environmentcode` is a short form of the environment field (one of `b`, `c`, `p`, `n`, `d`, or `net`).
  * `vpctype` is one of `svpc`, `float`, or `peer`.

For example: `vpc-p-svpc`  
Subnet | `sn-environmentcode-vpctype-region{-description`}

  * `environmentcode` is a short form of the environment field (one of `b`, `c`, `p`, `n`, `d`, or `net`).
  * `vpctype` is one of `svpc`, `float`, or `peer`.
  * `region` is any valid [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) that the resource is located in. We recommend removing hyphens and using an abbreviated form of some regions and directions to avoid hitting character limits. For example, `au` (Australia), `na` (North America), `sa` (South America), `eu` (Europe), `se` (southeast), or `ne` (northeast).
  * `description` is additional information about the subnet. You can use short, human-readable abbreviations.

For example: `sn-p-svpc-uswest1`  
Firewall policies | `fw-firewalltype-scope-environmentcode{-description`}

  * `firewalltype` is `hierarchical` or `network`.
  * `scope` is `global` or the Google Cloud region that the resource is located in. We recommend removing hyphens and using an abbreviated form of some regions and directions to avoid reaching character limits. For example, `au` (Australia), `na` (North America), `sa` (South America), `eu` (Europe), `se` (southeast), or `ne` (northeast).
  * `environmentcode` is a short form of the environment field (one of `b`, `c`, `p`, `n`, `d`, or `net`) that owns the policy resource.
  * `description` is additional information about the hierarchical firewall policy. You can use short, human-readable abbreviations.

For example:`fw-hierarchical-global-c-01``fw-network-uswest1-p-svpc`  
Cloud Router | `cr-environmentcode-vpctype-region{-description`}

  * `environmentcode` is a short form of the environment field (one of `b`, `c`, `p`, `n`, `d`, or `net`).
  * `vpctype` is one of `svpc`, `float`, or `peer`.
  * `region` is any valid Google Cloud region that the resource is located in. We recommend removing hyphens and using an abbreviated form of some regions and directions to avoid reaching character limits. For example, `au` (Australia), `na` (North America), `sa` (South America), `eu` (Europe), `se` (southeast), or `ne` (northeast).
  * `description` is additional information about the Cloud Router. You can use short, human-readable abbreviations.

For example: `cr-p-svpc-useast1-cr1`  
Cloud Interconnect connection | `ic-dc-colo`

  * `dc` is the name of your data center to which a Cloud Interconnect is connected.
  * `colo` is the [colocation facility name](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities#locations-table) that the Cloud Interconnect from the on-premises data center is peered with.

For example: `ic-mydatacenter-lgazone1`  
Cloud Interconnect VLAN attachment | `vl-dc-colo-environmentcode-vpctype-region{-description}`

  * `dc` is the name of your data center to which a Cloud Interconnect is connected.
  * `colo` is the colocation facility name that the Cloud Interconnect from the on-premises data center is peered with.
  * `environmentcode` is a short form of the environment field (one of `b`, `c`, `p`, `n`, `d`, or `net`).
  * `vpctype` is one of `svpc`, `float`, or `peer`.
  * `region` is any valid Google Cloud region that the resource is located in. We recommend removing hyphens and using an abbreviated form of some regions and directions to avoid reaching character limits. For example, `au` (Australia), `na` (North America), `sa` (South America), `eu` (Europe), `se` (southeast), or `ne` (northeast).
  * `description` is additional information about the VLAN. You can use short, human-readable abbreviations.

For example: `vl-mydatacenter-lgazone1-p-svpc-useast1-cr1`  
Group | `grp-gcp-description@example.com` Where `description` is additional information about the group. You can use short, human-readable abbreviations.For example: `grp-gcp-billingadmin@example.com`  
Custom role | `rl-description`Where `description` is additional information about the role. You can use short, human-readable abbreviations.For example: `rl-customcomputeadmin`  
Service account | `sa-description@projectid.iam.gserviceaccount.com`Where:

  * `description` is additional information about the service account. You can use short, human-readable abbreviations.
  * `projectid` is the globally unique project identifier.

For example: `sa-terraform-net@prj-b-seed-a1b2.iam.gserviceaccount.com`  
Storage bucket | `bkt-projectid-description`Where:

  * `projectid` is the globally unique project identifier.
  * `description` is additional information about the storage bucket. You can use short, human-readable abbreviations.

For example: `bkt-prj-c-infra-pipeline-a1b2-app-artifacts`  
  
## Alternatives to default recommendations

The best practices that are recommended in the blueprint might not work for every customer. You can customize any of the recommendations to meet your specific requirements. The following table introduces some of the common variations that you might require based on your existing technology stack and ways of working.

Decision area | Possible alternatives  
---|---  
**Organization:** The blueprint uses a single organization as the root node for all resources. | [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy#single-org-node) introduces scenarios in which you might prefer multiple organizations, such as the following:

  * Your organization includes sub-companies that are likely to be sold in the future or that run as completely separate entities.
  * You want to experiment in a sandbox environment with no connectivity to your existing organization.

  
**Folder structure:** The blueprint has a folder structure that divides workloads into `production, non-production` and `development` folders at the top layer. | [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy#decision_points_for_resource_hierarchy_design) introduces other approaches for structuring folders based on how you want to manage resources and inherit policies, such as:

  * Folders based on application environments
  * Folders based on regional entities or subsidiaries
  * Folders based on accountability framework

  
**Organization policies:** The blueprint enforces all organization policy constraints at the organization node. | You might have different security policies or ways of working for different parts of the business. In this scenario, enforce organization policy constraints at a lower node in the resource hierarchy. Review the complete list of [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that help meet your requirements.  
**Deployment pipeline tooling:** The blueprint uses Cloud Build to run the automation pipeline. | You might prefer other products for your deployment pipeline, such as [Terraform Enterprise](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/0-bootstrap/README-Terraform-Cloud.md), [GitLab Runners](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/0-bootstrap/README-GitLab.md/), [GitHub Actions](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/0-bootstrap/README-GitHub.md), or [Jenkins](https://github.com/terraform-google-modules/terraform-example-foundation/blob/master/0-bootstrap/README-Jenkins.md). The blueprint includes alternative directions for each product.  
**Code repository for deployment:** The blueprint uses Cloud Source Repositories as the managed private Git repository. | Use your preferred version control system for managing code repositories, such as [GitLab](https://about.gitlab.com/), [GitHub](https://github.com/), or [Bitbucket](https://bitbucket.org/product).If you use a private repository that is hosted in your on-premises environment, configure a private network path from your repository to your Google Cloud environment.  
**Identity provider:** The blueprint assumes an on-premises Active Directory and federates identities to Cloud Identity using Google Cloud Directory Sync. | If you already use Google Workspace, you can use the Google identities that are already managed in Google Workspace.If you don't have an existing identity provider, you might create and manage user identities directly in Cloud Identity.If you have an existing identity provider, such as [Okta](https://www.okta.com/), [Ping](https://www.pingidentity.com/en/solutions/business-priority/zero-trust.html), or [Azure Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id), you might manage user accounts in your existing identity provider and synchronize to Cloud Identity.If you have data sovereignty or compliance requirements that prevent you from using Cloud Identity, and if you don't require managed Google user identities for other Google services such as Google Ads or Google Marketing Platform, then you might prefer [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). In this scenario, be aware of limitations with [supported services](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).  
**Multiple regions:** The blueprint deploys regional resources into two different Google Cloud regions to help enable workload design with high availability and disaster recovery requirements in mind. | If you have end users in more geographical locations, you might configure more Google Cloud regions to create resources closer to the end user with less latency.If you have data sovereignty constraints or your availability needs can be met in a single region, you might configure only one Google Cloud region.  
**IP address allocation:** The blueprint provides a set of IP address ranges. | You might need to change the specific IP address ranges that are used based on the IP address availability in your existing hybrid environment. If you modify the IP address ranges, use the blueprint as guidance for the number and size of ranges required, and review the [valid IP address ranges for Google Cloud](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).  
**Hybrid networking:** The blueprint uses Dedicated Interconnect across multiple physical sites and Google Cloud regions for maximum bandwidth and availability. | Depending on your requirements for cost, bandwidth, and reliability requirements, you might configure [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) instead.If you need to start deploying resources with private connectivity before a Dedicated Interconnect can be completed, you might start with Cloud VPN and change to using Dedicated Interconnect later.If you don't have an existing on-premises environment, you might not need hybrid networking at all.  
**VPC Service Controls perimeter:** The blueprint recommends a single perimeter which includes all service projects for your Shared VPC topology. | You might have a use case that requires [multiple perimeters for an organization](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters#multiple-perimeters) or you might decide not to use VPC Service Controls at all.For information, see [decide how to mitigate data exfiltration through Google APIs](https://docs.cloud.google.com/architecture/landing-zones/decide-security#data-exfiltration).  
**Secret Manager:** The blueprint deploys a project for using Secret Manager in the `common` folder for organization-wide secrets, and a project in each environment folder for environment-specific secrets. | If you have a single team who is responsible for managing and auditing sensitive secrets across the organization, you might prefer to use only a single project for managing access to secrets.If you let workload teams manage their own secrets, you might not use a centralized project for managing access to secrets, and instead let teams use their own instances of Secret Manager in workload projects.  
**Cloud KMS:** The blueprint deploys a project for using Cloud KMS in the `common` folder for organization-wide keys, and a project for each environment folder for keys in each environment. | If you have a single team who is responsible for managing and auditing encryption keys across the organization, you might prefer to use only a single project for managing access to keys. A centralized approach can help meet compliance requirements like PCI key custodians.If you let workload teams manage their own keys, you might not use a centralized project for managing access to keys, and instead let teams use their own instances of Cloud KMS in workload projects.  
**Aggregated log sinks:** The blueprint configures a set of log sinks at the organization node so that a central security team can review audit logs from across the entire organization. | You might have different teams who are responsible for auditing different parts of the business, and these teams might require different logs to do their jobs. In this scenario, design multiple aggregated sinks at the appropriate folders and projects and create filters so that each team receives only the necessary logs, or design [log views](https://docs.cloud.google.com/logging/docs/logs-views) for granular access control to a common log bucket.  
**Granularity of infrastructure pipelines:** The blueprint uses a model where each business unit has a separate infrastructure pipeline to manage their workload projects. | You might prefer a single infrastructure pipeline that is managed by a central team if you have a central team who is responsible for deploying all projects and infrastructure. This central team can accept pull requests from workload teams to review and approve before project creation, or the team can create the pull request themselves in response to a ticketed system.You might prefer more granular pipelines if individual workload teams have the ability to customize their own pipelines and you want to design more granular privileged service accounts for the pipelines.  
**SIEM exports:** The blueprint manages all security findings in Security Command Center. | Decide whether you will export security findings from Security Command Center to tools such as Google Security Operations or your existing SIEM, or whether teams will use the console to view and manage security findings. You might configure multiple exports with unique filters for different teams with different scopes and responsibilities.  
  
## What's next

  * Implement the blueprint using the [Terraform example foundation](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master) on GitHub.
  * Learn more about best practice design principles with the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
  * Review the [library of blueprints](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) to help you accelerate the design and build of common enterprise workloads, including the following:

    * [Import data from Google Cloud into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint)

    * [Import data from an external network into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/secured-data-warehouse-blueprint-onprem)

    * [Deploy a secured serverless architecture using Cloud Run functions](https://docs.cloud.google.com/architecture/blueprints/serverless-functions-blueprint)

    * [Deploy a secured serverless architecture using Cloud Run](https://docs.cloud.google.com/architecture/blueprints/serverless-blueprint)

  * See [related solutions](https://docs.cloud.google.com/solutions) to deploy on top of your foundation environment.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
