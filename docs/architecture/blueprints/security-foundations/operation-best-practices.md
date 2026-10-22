---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices/
title: Operations best practices \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:40.147927+00:00
---

# Operations best practices  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Operations best practices Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

This section introduces operations that you must consider as you deploy and operate additional workloads into your Google Cloud environment. This section isn't intended to be exhaustive of all operations in your cloud environment, but introduces decisions related to the architectural recommendations and resources deployed by the blueprint.

## Update foundation resources

Although the blueprint provides an opinionated starting point for your foundation environment, your foundation requirements might grow over time. After your initial deployment, you might adjust configuration settings or build new shared services to be consumed by all workloads.

To modify foundation resources, we recommend that you make all changes through the foundation pipeline. Review the [branching strategy](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#branching-strategy) for an introduction to the flow of writing code, merging it, and triggering the deployment pipelines.

## Decide attributes for new workload projects

When creating new projects through the project factory module of the automation pipeline, you must configure various attributes. Your process to design and create projects for new workloads should include decisions for the following:

  * Which Google Cloud APIs to enable
  * Which Shared VPC to use, or whether to create a new VPC network
  * Which IAM roles to create for the initial `project-service-account` that is created by the pipeline
  * Which project labels to apply
  * The folder that the project is deployed to
  * Which billing account to use
  * Whether to add the project to a VPC Service Controls perimeter
  * Whether to configure a budget and billing alert threshold for the project



For a complete reference of the configurable attributes for each project, see the [input variables for the project factory](https://github.com/terraform-google-modules/terraform-example-foundation/tree/master/4-projects/modules/single_project#inputs) in the automation pipeline.

## Manage permissions at scale

When you deploy workload projects on top of your foundation, you must consider how you will grant access to the intended developers and consumers of those projects. We recommend that you add users into a group that is managed by your existing identity provider, synchronize the groups with Cloud Identity, and then apply IAM roles to the groups. Always keep in mind the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

We also recommend that you use [IAM recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) to identify allow policies that grant over-privileged roles. Design a process to periodically review recommendations or automatically apply recommendations into your deployment pipelines.

## Coordinate changes between the networking team and the application team

The network topologies that are deployed by the blueprint assume that you have a team responsible for managing network resources, and separate teams responsible for deploying workload infrastructure resources. As the workload teams deploy infrastructure, they must create firewall rules to allow the intended access paths between components of their workload, but they don't have permission to modify the network firewall policies themselves.

Plan how teams will work together to coordinate the changes to the centralized networking resources that are needed to deploy applications. For example, you might design a process where a workload team requests [tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) for their applications. The networking team then creates the tags and adds rules to the network firewall policy that allows traffic to flow between resources with the tags, and delegates the [IAM roles to use the tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#iam) to the workload team.

## Optimize your environment with the Active Assist portfolio

In addition to IAM recommender, Google Cloud provides the [Active Assist](https://docs.cloud.google.com/solutions/active-assist) portfolio of services to make recommendations about how to optimize your environment. For example, [firewall insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights) or the [unattended project recommender](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender) provide actionable recommendations that can help tighten your security posture.

Design a process to periodically review recommendations or automatically apply recommendations into your deployment pipelines. Decide which recommendations should be managed by a central team and which should be the responsibility of workload owners, and apply IAM roles to access the recommendations accordingly.

## Grant exceptions to organization policies

The blueprint enforces a set of organization policy constraints that are recommended to most customers in most scenarios, but you might have legitimate use cases that require limited exceptions to the organization policies you enforce broadly.

For example, the blueprint enforces the [iam.disableServiceAccountKeyCreation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) constraint. This constraint is an important security control because a leaked service account key can have a significant negative impact, and most scenarios should use [more secure alternatives to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) to authenticate. However, there might be use cases that can only authenticate with a service account key, such as an on-premises server that requires access to Google Cloud services and cannot use Workload Identity Federation. In this scenario, you might decide to allow an exception to the policy, so long as additional compensating controls like [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) are enforced.

Therefore, you should design a process for workloads to request an exception to policies, and ensure that the decision makers who are responsible for granting exceptions have the technical knowledge to validate the use case and consult on whether additional controls must be in place to compensate. When you grant an exception to a workload, modify the organization policy constraint as narrowly as possible. You can also [conditionally add constraints to an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy#conditionally_add_constraints_to_organization_policy) by defining a tag that grants an exception or enforcement for policy, then applying the tag to projects and folders.

## Protect your resources with VPC Service Controls

The blueprint helps prepare your environment for VPC Service Controls by enforcing prerequisite configurations like the restricted VIP. However, the blueprint initially deploys VPC Service Controls only in dry-run mode because cutting over to enforced mode can be a disruptive process that requires planning unique to your organization.

A perimeter denies access to restricted Google Cloud services from traffic that originates outside the perimeter, which includes the console, developer workstations, and the foundation pipeline used to deploy resources. If you use VPC Service Controls, you must design exceptions to the perimeter that allow the access paths that you intend.

A VPC Service Controls perimeter is intended for exfiltration controls between your Google Cloud organization and external sources. The perimeter isn't intended to replace or duplicate allow policies for granular access control to individual projects or resources. When you [design and architect a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters), we recommend using a common unified perimeter for lower management overhead.

If you must design multiple perimeters to granularly control service traffic within your Google Cloud organization, we recommend that you clearly define the threats that are addressed by a more complex perimeter structure and the access paths between perimeters that are needed for intended operations.

To adopt VPC Service Controls, evaluate the following:

  * Which of your use cases require VPC Service Controls.
  * Whether the required Google Cloud services [support VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).
  * How to configure breakglass access to modify the perimeter in case it disrupts your automation pipelines.
  * How to use [best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable) to design and implement your perimeter.



After you change the perimeter from dry-run to enforced mode, we recommend that you design a process to consistently add new projects to the correct perimeter, and a process to design exceptions when developers have a new use case that is denied by your current perimeter configuration.

## Test organization-wide changes in a separate organization

We recommend that you never deploy changes to production without testing. For workload resources, this approach is facilitated by separate environments for development, non-production, and production. However, some resources at the organization don't have separate environments to facilitate testing.

For changes at the organization-level, or other changes that can affect production environments like the configuration between your identity provider and Cloud Identity, consider creating a separate organization for test purposes.

## Control remote access to virtual machines

Because we recommend that you deploy immutable infrastructure through the foundation pipeline, infrastructure pipeline, and application pipeline, we also recommend that you only grant developers direct access to a virtual machine through SSH or RDP for limited or exceptional use cases.

For scenarios that require remote access, we recommend that you manage user access using [OS Login](https://docs.cloud.google.com/compute/docs/oslogin) where possible. This approach uses managed Google Cloud services to enforce access control, account lifecycle management, two-step verification, and audit logging. Alternatively, if you must allow access through [SSH keys in metadata](https://docs.cloud.google.com/compute/docs/instances/access-overview#ssh-access) or [RDP credentials](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials), it is your responsibility to manage the credential lifecycle and store credentials securely outside of Google Cloud.

In any scenario, a user with SSH or RDP access to a VM can be a privilege escalation risk, so you should design your access model with this in mind. The user can run code on that VM with the privileges of the associated service account or [query the metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview#metadata_security_considerations) to view the access token that is used to authenticate API requests. This access can then be a privilege escalation if you didn't deliberately intend for the user to operate with the privileges of the service account.

## Mitigate overspending by planning budget alerts

The blueprint implements best practices introduced in the [Google Cloud Well-Architected Framework: Cost Optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization) for managing cost, including the following:

  * Use a single billing account across all projects in the enterprise foundation.

  * Assign each project a `billingcode` metadata label that is used to allocate cost between cost centers.

  * Set budgets and alert thresholds.




It's your responsibility to plan budgets and configure billing alerts. The blueprint [creates budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) for workload projects when the forecasted spending is on track to reach 120% of the budget. This approach lets a central team identify and mitigate incidents of significant overspending. Significant unexpected increases in spending without a clear cause can be an indicator of a security incident and should be investigated from the perspectives of both cost control and security.

**Note:** Budget alerts cover a different type of notification than the [Billing category of Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). Budget alerts are related to the consumption of budgets that you define for each project. Billing notifications from Essential Contacts are related to pricing updates, errors, and credits.

Depending on your use case, you might set a budget that is based on the cost of an entire environment folder, or all projects related to a certain cost center, instead of setting granular budgets for each project. We also recommend that you delegate budget and alert setting to workload owners who might set more granular alerting threshold for their day-to-day monitoring.

For guidance on cost optimization, see [Optimize costs with FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).

## Allocate costs between internal cost centers

The console lets you [view your billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) to view and forecast cost in multiple dimensions. In addition to the prebuilt reports, we recommend that you export billing data to a BigQuery dataset in the `prj-c-billing-export` project. The exported billing records allow you to allocate cost on custom dimensions, such as your internal cost centers, based on project label metadata like `billingcode`.

The following SQL query is a sample query to understand costs for all projects that are grouped by the `billingcode` project label.
    
    
    #standardSQL
    SELECT
       (SELECT value from UNNEST(labels) where key = 'billingcode') AS costcenter,
       service.description AS description,
       SUM(cost) AS charges,
       SUM((SELECT SUM(amount) FROM UNNEST(credits))) AS credits
    FROM PROJECT_ID.DATASET_ID.TABLE_NAME
    GROUP BY costcenter, description
    ORDER BY costcenter ASC, description ASC
    

To set up this export, see [export Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

If you require internal accounting or chargeback between cost centers, it's your responsibility to incorporate the data that is obtained from this query into your internal processes.

## Ingest findings from detective controls into your existing SIEM

Although the foundation resources help you configure aggregated destinations for audit logs and security findings, it is your responsibility to decide how to consume and use these signals.

If you have a requirement to aggregate logs across all cloud and on-premise environments into an existing SIEM, decide how to ingest logs from the `prj-c-logging` project and findings from Security Command Center into your existing tools and processes. You might create a single export for all logs and findings if a single team is responsible for monitoring security across your entire environment, or you might create multiple exports filtered to the set of logs and findings needed for multiple teams with different responsibilities.

Alternatively, if log volume and cost are prohibitive, you might avoid duplication by retaining Google Cloud logs and findings only in Google Cloud. In this scenario, ensure that your existing teams have the right access and training to work with logs and findings directly in Google Cloud.

  * For audit logs, design [log views](https://docs.cloud.google.com/logging/docs/logs-views#create_view) to grant access to a subset of logs in your centralized logs bucket to individual teams, instead of duplicating logs to multiple buckets which increases log storage cost.
  * For security findings, grant [folder-level and project-level roles](https://docs.cloud.google.com/security-command-center/docs/access-control-org#folder-level_and_project-level_roles) for Security Command Center to let teams view and manage security findings just for the projects for which they are responsible, directly in the console.



## Continuously develop your controls library

The blueprint starts with a baseline of controls to detect and prevent threats. We recommend that you review these controls and add additional controls based on your requirements. The following table summarizes the mechanisms to enforce governance policies and how to extend these for your additional requirements:

Policy controls enforced by the blueprint | Guidance to extend these controls  
---|---  
Security Command Center detects vulnerabilities and threats from multiple [security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources). | Define [custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview) and [custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview).  
The Organization Policy service enforces a recommended set of [organization policy constraints](https://docs.cloud.google.com/architecture/blueprints/security-foundations/preventative-controls#organization-policy) on Google Cloud services. | Enforce additional constraints from the premade list of [available constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) or [create custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints).  
Open Policy Agent (OPA) policy [validates code in the foundation pipeline](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#automating-pipeline) for acceptable configurations before deployment. | Develop additional constraints based on the guidance at [GoogleCloudPlatform/policy-library](https://github.com/GoogleCloudPlatform/policy-library#developing-a-constraint).  
[Alerting on log-based metrics and performance metrics](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#alerting-log-based) configures log-based metrics to alert on changes to IAM policies and configurations of some sensitive resources. | Design additional log-based metrics and alerting policies for log events that you expect shouldn't occur in your environment.  
A [custom solution for automated log analysis](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#custom-solution) regularly queries logs for suspicious activity and creates Security Command Center findings. | Write additional queries to create findings for security events that you want to monitor, using [security log analytics](https://docs.cloud.google.com/architecture/security-log-analytics#analyze_logs) as a reference.  
A [custom solution to respond to asset changes](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#custom-solution-asset) creates Security Command Center findings and can automate remediation actions. | Create additional Cloud Asset Inventory feeds to monitor changes for particular asset types and write additional Cloud Run functions with custom logic to respond to policy violations.  
  
These controls might evolve as your requirements and maturity on Google Cloud change.

## Manage encryption keys with Cloud Key Management Service

Google Cloud provides [default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) for all customer content, but also provides [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/key-management-service) to provide you additional control over your encryption keys for data at rest. We recommend that you evaluate whether the default encryption is sufficient, or whether you have a compliance requirement that you must use Cloud KMS to manage keys yourself. For more information, see [decide how to meet compliance requirements for encryption at rest](https://docs.cloud.google.com/architecture/landing-zones/decide-security#encrypt-rest).

The blueprint provides a `prj-c-kms` project in the common folder and a `prj-{env}-kms` project in each environment folder for managing encryption keys centrally. This approach lets a central team audit and manage encryption keys that are used by resources in workload projects, in order to meet regulatory and compliance requirements.

Depending on your operational model, you might prefer a single centralized project instance of Cloud KMS under the control of a single team, you might prefer to manage encryption keys separately in each environment, or you might prefer multiple distributed instances so that accountability for encryption keys can be delegated to the appropriate teams. Modify the Terraform code sample as needed to fit your operational model.

Optionally, you can enforce [customer-managed encryption keys (CMEK) organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) to enforce that certain resource types always require a CMEK key and that only CMEK keys from an allowlist of trusted projects can be used.

## Store and audit application credentials with Secret Manager

We recommend that you never commit sensitive secrets (such as API keys, passwords, and private certificates) to source code repositories. Instead, commit the secret to [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and grant the [Secret Manager Secret Accessor](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor) IAM role to the user or service account that needs to access the secret. We recommend that you grant the IAM role to an individual secret, not to all secrets in the project.

When possible, you should generate production secrets automatically within the CI/CD pipelines and keep them inaccessible to human users except in breakglass situations. In this scenario, ensure that you don't grant IAM roles to view these secrets to any users or groups.

The blueprint provides a single `prj-c-secrets` project in the common folder and a `prj-{env}-secrets` project in each environment folder for managing secrets centrally. This approach lets a central team audit and manage secrets used by applications in order to meet regulatory and compliance requirements.

Depending on your operational model, you might prefer a single centralized instance of Secret Manager under the control of a single team, or you might prefer to manage secrets separately in each environment, or you might prefer multiple distributed instances of Secret Manager so that each workload team can manage their own secrets. Modify the Terraform code sample as needed to fit your operational model.

## Plan breakglass access to highly privileged accounts

Although we recommend that changes to foundation resources are managed through version-controlled IaC that is deployed by the foundation pipeline, you might have exceptional or emergency scenarios that require privileged access to modify your environment directly. We recommend that you plan for breakglass accounts (sometimes called firecall or emergency accounts) that have highly privileged access to your environment in case of an emergency or when the automation processes break down.

The following table describes some example purposes of breakglass accounts.

Breakglass purpose | Description  
---|---  
Super admin | Emergency access to the [Super admin](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices) role used with Cloud Identity, to, for example, fix issues that are related to identity federation or multi-factor authentication (MFA).  
Organization administrator | Emergency access to the [Organization Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin:~:text=roles%2Fresourcemanager.organizationAdmin) role, which can then grant access to any other IAM role in the organization.  
Foundation pipeline administrator | Emergency access to modify the resources in your CICD project on Google Cloud and external Git repository in case the automation of the foundation pipeline breaks down.  
Operations or SRE | An operations or SRE team needs privileged access to respond to outages or incidents. This can include tasks like restarting VMs or restoring data.  
  
Your mechanism to permit breakglass access depends on the existing tools and procedures you have in place, but a few example mechanisms include the following:

  * Use your existing tools for privileged access management to temporarily add a user to a group that is predefined with highly-privileged IAM roles or use the credentials of a highly-privileged account.
  * Pre-provision accounts intended only for administrator usage. For example, developer Dana might have an identity dana@example.com for daily use and admin-dana@example.com for breakglass access.
  * Use an application like [just-in-time privileged access](https://docs.cloud.google.com/architecture/manage-just-in-time-privileged-access-to-project) that allows a developer to self-escalate to more privileged roles.



Regardless of the mechanism you use, consider how you operationally address the following questions:

  * How do you design the scope and granularity of breakglass access? For example, you might design a different breakglass mechanism for different business units to ensure that they cannot disrupt each other.
  * How does your mechanism prevent abuse? Do you require approvals? For example, you might have split operations where one person holds credentials and one person holds the MFA token.
  * How do you audit and alert on breakglass access? For example, you might configure a [custom Event Threat Detection module](https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview) to create a security finding when a predefined breakglass account is used.
  * How do you remove the breakglass access and resume normal operations after the incident is over?



For common privilege escalation tasks and rolling back changes, we recommend designing automated workflows where a user can perform the operation without requiring privilege escalation for their user identity. This approach can help reduce human error and improve security.

For systems that require regular intervention, automating the fix might be the best solution. Google encourages customers to adopt a zero-touch production approach to make all production changes using automation, [safe proxies](https://google.github.io/building-secure-and-reliable-systems/raw/ch03.html), or audited breakglass. Google provides the [SRE books](https://sre.google/books/) for customers who are looking to adopt Google's SRE approach.

## What's next

  * Read [Deploy the blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
