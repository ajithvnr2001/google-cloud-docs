---
url: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/recommended-iam-groups/
title: Recommended user groups and Identity and Access Management roles \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:39.581985+00:00
---

# Recommended user groups and Identity and Access Management roles  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/security-best-practices-catalog/recommended-iam-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Recommended user groups and Identity and Access Management roles Stay organized with collections  Save and categorize content based on your preferences. 

The following table describes the Identity and Access Management (IAM) roles that we recommend as a starting point for running workloads on Google Cloud. Configure your IAM roles to implement separation of duties within your environment and to align with your risk appetite and organizational structure.

As you assign these roles to the user groups in your organization, consider where you need to apply more fine-grained roles to address specific use cases and data access requirements. For environments where highly sensitive data is used (for example, you're using sensitive data to train models), see the [Import data into a secured BigQuery data warehouse](https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint) for more information about the roles that you can use to permit access to stored data.

The following table describes the role recommendations. Apply foundational recommendations and use-case specific recommendations as appropriate.

Service | Group | Description | IAM roles  
---|---|---|---  
Foundational | `grp-gcp-org-admin` | This group administers the resources that belong to the organization. Assign this role sparingly. Organization administrators have access to all of your Google Cloud resources. Alternatively, because this function is highly privileged, consider using individual accounts instead of creating a group. | 

  * Organization administrator (`roles/resourcemanager.organizationAdmin`)
  * Folder Admin (`roles/resourcemanager.folderAdmin`)
  * Project Creator (`roles/resourcemanager.projectCreator`)
  * Billing Account User (`roles/billing.user`)
  * Organization Role Administrator (`roles/iam.organizationRoleAdmin`)
  * Organization Policy Administrator (`roles/orgpolicy.policyAdmin`)
  * Security Center Admin (`roles/securitycenter.admin`)
  * Support Account Administrator (`roles/cloudsupport.admin`)

  
Foundational | `grp-gcp-network-admins` | This group can create networks, subnets, firewall rules, and network devices such as Cloud Router, Cloud VPN, and cloud load balancers. | 

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Shared VPC Admin (`roles/compute.xpnAdmin`)
  * Compute Security Admin (`roles/compute.securityAdmin`)
  * Folder Viewer (`roles/resourcemanager.folderViewer`)

  
Foundational | `grp-gcp-billing-admin` | This group sets up billing accounts and monitors their usage. | 

  * Billing Account Administrator (`roles/billing.admin`)
  * Billing Account Creator (`roles/billing.creator`)
  * Organization Viewer (`roles/resourcemanager.organizationViewer`)

  
Foundational | `grp-gcp-security-admins` | This group establishes and manages security policies for the entire organization, including access management and organization constraint policies. To plan your Google Cloud security infrastructure, see the [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). | 

  * BigQuery Data Viewer (`roles/bigquery.dataViewer`)
  * Compute Viewer (`roles/compute.viewer`)
  * Folder IAM Admin (`roles/resourcemanager.folderIamAdmin`)
  * Kubernetes Engine Viewer (`roles/container.viewer`)
  * Logs Configuration Writer (`roles/logging.configWriter`)
  * Organization Role Viewer (`roles/iam.organizationRoleViewer`)
  * Organization Policy Administrator (`roles/orgpolicy.policyAdmin`)
  * Organization Policy Viewer (`roles/orgpolicy.policyViewer`)
  * Private Logs Viewer (`roles/logging.privateLogViewer`)
  * Security Center Admin (`roles/securitycenter.admin`)
  * Security Reviewer (`roles/iam.securityReviewer`)

  
Foundational | `grp-gcp-billing-viewer` | This group monitors the spend on projects. Typically group members are part of the finance team. | 

  * Billing Account Viewer (`roles/billing.viewer`)

  
Foundational | `grp-gcp-platform-viewer` | This group reviews resource information across the Google Cloud organization. | 

  * Viewer (`roles/viewer`)

  
Foundational | `grp-gcp-security-reviewer` | This group reviews cloud security. | 

  * Security Reviewer (`roles/iam.securityReviewer`)

  
Foundational | `grp-gcp-network-viewer` | This group reviews network configurations. | 

  * Compute Network Viewer (`roles/compute.networkViewer`)

  
Foundational | `grp-gcp-audit-viewer` | This group views audit logs. | 

  * Private Logs Viewer (`roles/logging.privateLogViewer`)
  * Viewer (`roles/viewer`)

  
Foundational | `grp-gcp-scc-admin` | This group administers Security Command Center. | 

  * Security Center Admin (`roles/securitycenter.admin`)

  
Foundational | `grp-gcp-secrets-admin` | This group manages secrets in Secret Manager. | 

  * Secret Manager Admin (`roles/secretmanager.admin`)

  
Agent Platform administrators | `grp-gcp-vertex-ai-admin` | This group has full access to all resources in Agent Platform. | 

  * Vertex AI Administrator (`roles/aiplatform.admin`)

  
Agent Platform viewers | `grp-gcp-vertex-ai-viewer` | This group views all resources in Agent Platform. | 

  * Vertex AI Viewer (`roles/aiplatform.viewer`)

  
Agent Platform users | `grp-gcp-vertex-ai-user` | This group uses all resources in Agent Platform. | 

  * Vertex AI User (`roles/aiplatform.user`)

  
Agent Platform Workbench administrators | `grp-gcp-vertex-ai-notebook-admin` | This group has full access to all runtime templates and runtimes in Agent Platform Workbench. | 

  * Notebook Runtime Admin (`roles/aiplatform.notebookRuntimeAdmin`)

  
Agent Platform Workbench users | `grp-gcp-vertex-ai-notebook-user` | This group creates runtime resources using a runtime template and manages the runtime resources that they created. | 

  * Notebook Runtime User (`roles/aiplatform.notebookRuntimeUser`)

  
  
## What's next

  * Review [role recommendations](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization#groups_for_access_control) in the enterprise foundations blueprint.

  * Review [secure enterprise foundation controls](https://docs.cloud.google.com/docs/security/security-best-practices-catalog/secure-enterprise-foundations).

  * See more [Google Cloud security best practices and guidelines](https://docs.cloud.google.com/docs/security/security-best-practices-catalog).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
