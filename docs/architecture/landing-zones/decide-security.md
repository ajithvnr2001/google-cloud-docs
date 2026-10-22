---
url: https://docs.cloud.google.com/architecture/landing-zones/decide-security/
title: Decide the security for your Google Cloud landing zone \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:26.011109+00:00
---

# Decide the security for your Google Cloud landing zone  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/landing-zones/decide-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Decide the security for your Google Cloud landing zone Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-02 UTC

This document introduces important security decisions and recommended options to consider when designing a Google Cloud landing zone. It's part of a series about [landing zones](https://docs.cloud.google.com/architecture/landing-zones), and is intended for security specialists, CISOs, and architects who want to understand the decisions that they need to make when designing a landing zone in Google Cloud.

In this document, it's assumed that a central team, such as the security team or the platform team, enforces these landing zone security controls. Because the focus of this document is the design of enterprise-scale environments, some strategies that it describes might be less relevant for small teams.

## Decision points for securing your Google Cloud landing zone

To choose the best security design for your organization, you must make the following decisions:

  * How to limit persistent credentials for service accounts

  * How to mitigate data exfiltration through Google APIs

  * How to continuously monitor for insecure configurations and threats

  * How to centrally aggregate necessary logs

  * How to meet compliance requirements for encryption at rest

  * How to meet compliance requirements for encryption in transit

  * Which additional controls are necessary for managing cloud service provider access




## Architecture diagram

The example architecture described in this document uses common security design patterns. Your specific controls might vary based on factors such as your organization's industry, target workloads, or additional compliance requirements. The following diagram shows the security controls architecture that you apply in your landing zone when you follow the recommendations in this document.

![Example security controls architecture.](https://docs.cloud.google.com/static/architecture/landing-zones/images/decide-security-architecture.svg)

The preceding diagram shows the following:

  * Service account key management helps mitigate risk from long-lived service account credentials.
  * VPC Service Controls defines a perimeter around sensitive resources that helps to restrict access from outside the perimeter.
  * Security Command Center monitors the environment for insecure configurations and threats.
  * A centralized log sink collects audit logs from all projects.
  * Google default encryption at rest encrypts all data that persists to disk.
  * Google default encryption in transit applies to layer 3 and layer 4 network paths.
  * Access Transparency gives you visibility and control over how Google can access your environment.



## Decide how to limit persistent credentials for service accounts

[Service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) are machine identities that you use to grant IAM roles to workloads and allow the workload to access Google Cloud APIs. A service account key is a persistent credential, and any persistent credentials are potentially high risk. We don't recommend that you let developers freely [create service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

For example, if a developer accidentally commits the service account key to a public Git repository, an external attacker can authenticate using those credentials. As another example, if the service account key is stored in an internal repository, a malicious insider who can read the key could use the credentials to escalate their own Google Cloud privileges.

To define a strategy to manage these persistent credentials, you must provide viable alternatives, limit the proliferation of persistent credentials, and manage how they are used. For information about alternatives to service account keys, see [Choose the right authentication method for your use case](https://docs.cloud.google.com/docs/authentication#auth-decision-tree).

The following sections describe the options to limit persistent credentials. We recommend option 1 for most use cases. The other options discussed in the following sections are alternatives that you can consider if option 1 doesn't apply to your specific organization.

All organizations created after May 23, 2024 have [Google Cloud security baseline constraints](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations#organization_policies_enforced_on_organization_resources) enforced when the organization resource is first created. This change makes option 1 the default option.

### Option 1: Restrict use of persistent service account keys

We recommend that you don't permit any users to download service account keys because exposed keys are a common attack vector. Restricting the use of persistent service account keys is an option that can help reduce the risk and overhead of manually managing service account keys.

To implement this option, consider the following:

  * To prevent developers from creating and downloading persistent credentials, configure the [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) `constraints/iam.disableServiceAccountKeyCreation`.
  * Educate your teams on [more secure alternatives to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree). For example, when users and applications that are outside of your Google Cloud environment need to use a service account, they can authenticate with [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation) or [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) instead of a service account key.
  * Design a process for teams to request an exception to this policy when downloading a service account key is the only viable option. For example, a third-party SaaS product might require a service account key to read logs from your Google Cloud environment.



Avoid this option when you already have tooling in place to generate short-lived API credentials for service accounts.

For more information, see the following:

  * [Organization policy constraints](https://docs.cloud.google.com/architecture/security-foundations/preventative-controls#organization-policy) in the Google Cloud enterprise foundations blueprint
  * [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)



### Option 2: Use additional access management tools to generate short-lived credentials

As an alternative to Restrict use of persistent service account keys, you can generate [short-lived credentials for service accounts](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials). Short-lived credentials create less risk than persistent credentials such as service account keys. You can develop your own tooling or use third-party solutions such as Hashicorp Vault to generate short-lived access credentials.

Use this option when you already have invested in a third-party tool for generating short-lived credentials for access control, or have sufficient budget and capacity to develop your own solution.

Avoid using this option when you don't have existing tooling to grant short-lived credentials, or don't have the capacity to build your own solution.

For more information, see [Create short-lived service account credentials](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials).

## Decide how to mitigate data exfiltration through Google APIs

Google APIs have public endpoints that are available to all customers. While every API resource in your Google Cloud environment is subject to IAM access controls, there is a risk that data could be accessed using stolen credentials, exfiltrated by malicious insiders or compromised code, or exposed through a misconfigured IAM policy.

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) is a solution that addresses these risks. However, VPC Service Controls also introduces complexity to your access model, so you must design VPC Service Controls to meet your unique environment and use case.

The following sections describe the options to mitigate data exfiltration through Google APIs. We recommend option 1 for most use cases. The other options discussed in the following sections are alternatives that you can consider if option 1 doesn't apply to your specific use case.

### Option 1: Configure VPC Service Controls broadly across your environment

We recommend that you design your environment within one or more VPC Service Controls perimeters that restrict all supported APIs. Configure exceptions to the perimeter with access levels or ingress policies so that developers can access the services that they require, including console access where needed.

Use this option when the following is true:

  * The services that you intend to use support VPC Service Controls, and your workloads don't require unrestricted internet access.
  * You store sensitive data on Google Cloud that could be a significant loss if exfiltrated.
  * You have consistent attributes for developer access that can be configured as exceptions to the perimeter, allowing users to access the data that they need.



Avoid this option when your workloads require unrestricted internet access or services that are not supported by VPC Service Controls.

For more information, see the following:

  * [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/enable)
  * [Supported products and limitations for VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products)
  * [Design and architect service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters)



### Option 2: Configure VPC Service Controls for a subset of your environment

Instead of configuring VPC Service Controls broadly across your environment, you can configure VPC Service Controls only on the subset of projects that contain sensitive data and internal-only workloads. This option lets you use a simpler design and operation for most projects, while still prioritizing data protection for projects with sensitive data.

For example, you might consider this alternative when a limited number of projects contain BigQuery datasets with sensitive data. You can define a service perimeter around just these projects, and define [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to allow narrow exceptions for the analysts who need to use these datasets.

For another example, in an application with three-tier architecture, some components might be outside of the perimeter. The presentation tier that allows ingress from user traffic might be a project outside of the perimeter, and the application tier and data tier that contain sensitive data might be separate projects inside the service perimeter. You define ingress and egress rules to the perimeter so that the tiers can communicate across the perimeter with granular access.

Use this option when the following is true:

  * Only limited and well-defined projects contain sensitive data. Other projects contain data of lower risk.
  * Some workloads are internal only, but some workloads require public internet access or have dependencies on services that are not supported by VPC Service Controls.
  * Configuring VPC Service Controls across all projects creates too much overhead or requires too many workarounds



Avoid this option when many projects could potentially contain sensitive data.

For more information, see [Best practices for enabling VPC Service Controls](https://docs.cloud.google.com/architecture/vpc-service-controls-enterprise-best-practices).

### Option 3: Don't configure VPC Service Controls

As another alternative to configuring VPC Service Controls broadly across your environment, you can choose not to use VPC Service Controls, particularly if the operational overhead outweighs the value of VPC Service Controls.

For example, your organization might not have a consistent pattern of developer access that could form the basis of an ingress policy. Perhaps your IT operations are outsourced to multiple third parties, so developers don't have managed devices or access from consistent IP addresses. In this scenario, you might not be able to define ingress rules to allow exceptions to the perimeter that developers need to complete their daily operations.

Use this option when:

  * You use services that don't support VPC Service Controls.
  * Workloads are internet facing and don't contain sensitive data.
  * You don't have consistent attributes of developer access like managed devices or known IP ranges.



Avoid this option when you have sensitive data in your Google Cloud environment.

## Decide how to continuously monitor for insecure configurations and threats

Adopting cloud services introduces new challenges and threats when compared to using services located on-premises. Your existing tools that monitor long-lived servers may not be appropriate for autoscaling or ephemeral services, and might not monitor serverless resources at all. Therefore, you should evaluate security tools that work with the full range of cloud services that you might adopt. You should also continuously monitor for cloud standards, like the [CIS Benchmark for Google Cloud](https://www.cisecurity.org/benchmark/google_cloud_computing_platform).

The following sections describe the options for continuous monitoring. We recommend option 1 for most use cases. The other options discussed in the following sections are alternatives that you can consider if option 1 doesn't apply to your specific use case.

### Option 1: Use Security Command Center

We recommend that you activate [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) at the organization level, which helps you strengthen your security posture by doing the following:

  * Evaluating your security and data attack surface
  * Providing asset inventory and discovery
  * Identifying misconfigurations, vulnerabilities, and threats
  * Helping you mitigate and remediate risks



When you enable Security Command Center at the beginning of your landing zone build, your organization's security team has near real-time visibility on insecure configurations, threats, and remediation options. This visibility helps your security team assess whether the landing zone meets their requirements and is ready for developers to start deploying applications.

Use this option when the following is true:

  * You want a security posture management and threat detection tool that is integrated with all Google Cloud services without additional integration effort.
  * You want to use the same threat intelligence, machine learning, and other advanced methods that Google uses to protect its own services.
  * Your existing security operations center (SOC) doesn't have the skills or capacity to generate threat insights from a large volume of cloud logs.



Avoid this option when your existing security tools can fully address ephemeral or serverless cloud resources, monitor for insecure configurations, and identify threats at scale in a cloud environment.

### Option 2: Use your existing security tools for cloud security posture management and threat detection

As an alternative option to Use Security Command Center, you might consider other cloud security posture management tools. Various third-party tools exist that have similar functions to Security Command Center, and you might already have invested in cloud-native tools that are focused on multi-cloud environments.

You can also use Security Command Center and third-party tools together. For example, you might ingest the [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) from Security Command Center to another tool, or you might [add a third-party security service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#third-party-source) to the Security Command Center dashboard. As another example, you might have a requirement to store logs on an existing SIEM system for the SOC team to analyze for threats. You could configure your existing SIEM to ingest only the [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) that Security Command Center produces, instead of ingesting a large volume of logs and expecting a SOC team to analyze the raw logs for insight.

Use this option when your existing security tools can fully address ephemeral or serverless cloud resources, monitor for insecure configurations, and identify threats at scale in a cloud environment.

Avoid this option when the following is true:

  * Your existing SOC doesn't have the skills or capacity to generate threat insights from the vast volume of cloud logs.
  * Integrating multiple third-party tools with multiple Google Cloud services introduces more complexity than value.



For more information, see the following:

  * [Enable finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)
  * [Managing security sources using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources)
  * [Add a third-party security service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#third-party-source)



## Decide how to centrally aggregate necessary logs

Most audit logs are stored in the Google Cloud project that produced them. As your environment grows, it can be untenable for an auditor to check logs in every individual project. Therefore, you need to make a decision on how logs will be centralized and aggregated to help your internal audit and security operations.

The following sections describe the options for aggregating logs. We recommend option 1 for most use cases. The other options discussed in the following sections are alternatives that you can consider if option 1 doesn't apply to your specific use case.

### Option 1: Retain logs in Google Cloud by using aggregated logs sinks

We recommend that you configure a centralized organization-wide log sink for audit logs and other logs that are required by your security team. You can reference the [logs scoping tool](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-security-and-access-analytics#log_scoping_tool) to identify the logs that your security team requires and whether these log types require explicit enablement.

For example, the security team expects a central record of any resources that your users create so that the security team can monitor and investigate suspicious changes. The security team also requires an immutable record of data access for certain highly sensitive workloads. Therefore, the security team configures one log sink to aggregate administrator activity audit logs from all projects into a [Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics#analytics) bucket in a central project that they can view for impromptu investigations. They then configure a second log sink for data access audit logs from projects with sensitive workloads into a Cloud Storage bucket for long-term retention.

Use this option when the following is true:

  * Your security team expects a central record of all audit logs or other specific log types.
  * Your security team needs to store logs in an environment with restricted access, outside the control of the workload or teams who produced the log.



Avoid this option when the following is true:

  * Your organization doesn't have a central requirement for consistent audit logs across workloads.
  * Individual project owners have full responsibility for managing their own audit logs.



For more information, see the following:

  * [Detective controls](https://docs.cloud.google.com/architecture/security-foundations/detective-controls) in the enterprise foundations blueprint
  * [Best practices for Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit/best-practices)
  * [Configure aggregated sinks](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks)
  * [Log scoping tool](https://docs.cloud.google.com/architecture/exporting-stackdriver-logging-for-security-and-access-analytics#log_scoping_tool)
  * [Retention policies and retention policy locks](https://docs.cloud.google.com/storage/docs/bucket-lock)



### Option 2: Retain audit logs in Google SecOps with direct ingestion

If you're using [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) as a SIEM solution, you can automatically ingest supported log types from Google Cloud to Google SecOps. You can send specific log types (including Cloud Logging, Cloud Asset Inventory metadata, and Security Command Center findings) to Google Security Operations in real-time by configuring [direct ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs#option_1_direct_ingestion).

Depending on your requirements, you might use a combination of Option 1 and Option 2. For example, you might have a platform team who needs to view centralized logs in your Google Cloud environment and doesn't have access to your Google SecOps environment, and a security operations team who needs to view logs from multiple cloud providers and only has access to your Google SecOps environment.

If you require logs from your Google Cloud environment beyond the set of [log types supported for export](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs#supported-logs-for-export), you can configure your own log feeds for other log types. See [feed management](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api) and [default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers) for more information.

Use this option when the following is true:

  * You're using Google SecOps.



Avoid this option when the following is true:

  * You're not using Google SecOps.
  * You require more granular control over log ingestion compared to the default settings provided by direct ingestion.



For more information, see the following:

  * [Ingest Google Cloud data to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs)



### Option 3: Export required audit logs to storage outside of Google Cloud

As an alternative to storing logs in Google Cloud only, consider exporting audit logs outside of Google Cloud. After you centralize necessary log types into an aggregate log sink in Google Cloud, ingest the contents of that sink to another platform outside of Google Cloud for storing and analyzing logs.

For example, you might use a third-party SIEM to aggregate and analyze audit logs across multiple cloud providers. This tool has sufficient capabilities to work with serverless cloud resources, and your SOC team has the skills and capacity to generate insight from this large volume of logs.

This option can potentially be very expensive because of the network egress cost in Google Cloud, as well as the storage cost and capacity in the other environment. Rather than exporting every available log, we recommend that you be selective about which logs are required in the external environment.

Use this option when you have a requirement to store logs from all environments and cloud providers in a single central location.

Avoid this option when the following is true:

  * Your existing systems don't have the capacity or budget to ingest a large volume of additional cloud logs.
  * Your existing systems require integration efforts for each log type and format.
  * You are collecting logs without a clear goal of how they will be used.



For more information, see [Detective controls](https://docs.cloud.google.com/architecture/security-foundations/detective-controls) in the enterprise foundations blueprint.

## Decide how to meet compliance requirements for encryption at rest

Google Cloud automatically encrypts all your content stored at rest, using one or more encryption mechanisms. Depending on your compliance requirements, you might have an obligation to manage the encryption keys yourself.

The following sections describe the options for encryption at rest. We recommend option 1 for most use cases. The other options discussed in the following sections are alternatives that you can consider if option 1 doesn't apply to your specific use case.

### Option 1: Accept use of default encryption at rest

Default encryption at rest is sufficient for many use cases that don't have particular compliance requirements regarding encryption key management.

For example, the security team at an online gaming company requires all customer data to be encrypted at rest. They don't have regulatory requirements about key management, and after reviewing Google's default encryption at rest, they are satisfied that it's a sufficient control for their needs.

Use this option when the following is true:

  * You don't have particular requirements around how to encrypt data or how encryption keys are managed.
  * You prefer a managed service over the cost and operational overhead of managing your own encryption keys.



Avoid this option when you have compliance requirements to manage your own encryption keys.

For more information, see [Encryption at rest in Google Cloud](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

### Option 2: Manage encryption keys using Cloud KMS

In addition to default encryption at rest, you might require more control over the keys used to encrypt data at rest within a Google Cloud project. Cloud Key Management Service (Cloud KMS) offers the ability to protect your data using customer-managed encryption keys (CMEK). For example, in the financial services industry, you might have a requirement to report to your external auditors how you manage your own encryption keys for sensitive data.

For additional layers of control, you can configure hardware security modules (HSM) or external key management (EKM) with CMEK. Customer-supplied encryption keys (CSEK) are not recommended; scenarios that historically were addressed by CSEK are now better addressed by Cloud External Key Manager (Cloud EKM) because Cloud EKM has support for more services and higher availability.

This option shifts some responsibility to application developers to follow the key management that your security team mandates. The security team can enforce the requirement by blocking the creation of non-compliant resources with [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

Use this option when one or more of the following is true:

  * You have a requirement to manage the lifecycle of your own keys.
  * You have a requirement to generate cryptographic key material with a [FIPS 140-2 Level 3](https://csrc.nist.gov/publications/detail/fips/140/2/final) certified HSM.
  * You have a requirement to store cryptographic key material outside of Google Cloud using Cloud EKM.



Avoid this option when the following is true:

  * You don't have particular requirements for how to encrypt data or how encryption keys are managed.
  * You prefer a managed service over the cost and operational overhead of managing your own encryption keys.



For more information, see the following:

  * [Recommended practices for using CMEKs](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices)
  * [Manage encryption keys with Cloud Key Management Service](https://docs.cloud.google.com/architecture/security-foundations/operation-best-practices#manage-encryption) in the enterprise foundations blueprint
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek)
  * [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm)
  * [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm)
  * [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy)



### Option 3: Tokenize data at the application layer before persisting in storage

In addition to the default encryption provided by Google, you can also develop your own solution to tokenize data before storing it in Google Cloud.

For example, a data scientist must analyze a dataset with PII information, but the data scientist shouldn't have access to read the raw data of some sensitive fields. To limit control access to raw data, you could develop an ingestion pipeline with [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) to ingest and tokenize sensitive data, and then persist the tokenized data to BigQuery.

Tokenizing data is not a control that you can centrally enforce in the landing zone. Instead, this option shifts the responsibility to application developers to configure their own encryption, or to a platform team who develops an encryption pipeline as a shared service for application developers to use.

Use this option when particular workloads have highly sensitive data that must not be used in its raw form.

Avoid this option when Cloud KMS is sufficient to meet your requirements, as described in Manage encryption keys using Cloud KMS. Moving data through additional encryption and decryption pipelines adds cost, latency, and complexity to applications.

For more information, see [Sensitive Data Protection overview](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview).

## Decide how to meet compliance requirements for encryption in transit

Google Cloud has several security measures to help ensure the authenticity, integrity, and privacy of data in transit. Depending on your security and compliance requirements, you might also configure application layer encryption.

The following sections describe the options for encryption in transit. We recommend option 1 for most use cases. The other options discussed in the following sections are additional features that you can consider if option 1 is insufficient for your specific use case.

### Option 1: Evaluate whether Google Cloud encryption in transit is sufficient

Many traffic patterns in your landing zone benefit from Google Cloud default encryption in transit.

  * VM-to-VM connections within VPC networks and peered VPC networks that are inside of Google's production network are integrity-protected and encrypted.
  * Traffic from the internet to Google services and traffic from your VPC network to Google services terminate at the Google Front End (GFE). GFE also does the following:

    * Provides DDoS attack countermeasures
    * Routes and load balances traffic to the Google Cloud services
  * Google's infrastructure uses ALTS for the authentication, integrity, and encryption of connections from the GFE to a Google Cloud service, and from one Google Cloud service to another Google Cloud service.




Use this option when Google Cloud default encryption in transit is sufficient for your internal workloads.

Add additional protection when the following is true:

  * You allow internet ingress traffic into your VPC network.
  * You're connecting to your on-premises environment.



In these cases, you should configure additional controls, as discussed in Option 2: Require applications to configure Layer 7 encryption in transit and Option 3: Configure additional encryption to your on-premises environment.

For more information about Google Cloud default encryption in transit, see [Encryption in transit in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).

### Option 2: Configure addition encryption for traffic to or from your customer applications

In addition to default encryption in transit, you can configure Layer 7 encryption for application traffic to your customer applications. Google Cloud provides managed services to support applications that need application-layer encryption in transit, including managed certificates and Cloud Service Mesh.

For example, a developer is building a new application that accepts ingress traffic from the internet. They use an external Application Load Balancer with Google-managed SSL certificates to run and scale services behind a single IP address.

Application layer encryption is not a control that you can enforce centrally in the landing zone. Instead, this option shifts some responsibility to application developers to configure encryption in transit.

Use this option when applications require HTTPS or SSL traffic between components.

Consider allowing a limited exception to this option when you are migrating compute workloads to the cloud that did not previously require encryption in transit for internal traffic when the applications were on-premises. During a large-scale migration, forcing legacy applications to modernize before migration might cause an unacceptable delay to the program.

For more information, see the following:

  * [Using Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)
  * [Using self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)



### Option 3: Configure additional encryption to your on-premises environment

If you require a connection from Google Cloud to your on-premises environment, you can configure Cloud Interconnect, which sets up a direct physical connection between Google Cloud and your data centers. When using Cloud Interconnect, traffic from your on-premises environment to Google Cloud isn't encrypted in transit by default. Therefore, if you're using Cloud Interconnect, we recommend that you enable [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview) as part of your landing zone.

If you use HA VPN to connect private traffic between Google Cloud and your data centers, traffic uses IPsec encryption by default.

For more information, see [Choosing a Network Connectivity Center product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

## Decide which additional controls are necessary for managing cloud service provider access

The need to audit cloud service provider (CSP) access can be a concern during cloud adoption. Google Cloud provides multiple layers of control that can enable verification of cloud provider access.

The following sections describe the options for managing CSP access. We recommend option 1 for most use cases. The other option discussed in the following sections is an additional feature that you can consider if option 1 is insufficient for your specific use case.

### Option 1: Enable Access Transparency logs

[Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) logs record the actions taken by Google Cloud personnel in your environment, such as when they troubleshoot a support case.

For example, your developer raises a troubleshooting issue to Cloud Customer Care, and asks the support agent to help troubleshoot their environment. An Access Transparency log is generated to show what actions the support staff took, including the support case number that justified it.

Use this option when the following is true:

  * You have a requirement to verify that Google Cloud personnel are accessing your content only for valid business reasons, such as fixing an outage or attending to your support requests.
  * You have a compliance requirement to track access to sensitive data.



### Option 2: Enable Access Transparency logs and provider access management

If your business has a compliance requirement to grant explicit approval before a CSP can access your environment, in addition to Option 1, you can use Access Transparency with other controls that let you explicitly approve or deny access to your data.

[Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) is a manual solution that ensures that Customer Care and Google engineering require your explicit approval (through email or through a webhook) whenever they need to access your content.

[Key Access Justifications](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) lets you set a policy on Cloud KMS keys to view, approve, and deny key access requests depending on the provided justification code.

Use this option when the following is true:

  * You want a central team to directly manage access to your content by Google personnel.
  * For Access Approval, you can accept the risk that the central capability to approve or deny each access request is more important than the operational trade-off, which could be a slower resolution of support cases.
  * For Key Access Justifications, your business is already using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) as part of your compliance strategy, and wants programmatic control over all types of access to encrypted data.



Avoid this option when the following is true:

  * The operational delay that can result when a central team with Access Approval authority must respond is an unacceptable risk to workloads that require high availability and a rapid response from Customer Care.



For more information, see the following:

  * [Cloud provider access management](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)

  * [Overview of Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)




## Security best practices for Google Cloud landing zones

In addition to the decisions introduced in this document, consider the following security best practices:

  * Provision the identities in your environment. For more information, see [Decide how to onboard identities to Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities).
  * Design a network that meets your organization's use cases. For more information, see [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design).
  * Implement the [organization policy constraints](https://docs.cloud.google.com/architecture/security-foundations/using-example-terraform#organization-policy-setup) that are defined in the enterprise foundations blueprint. These constraints help to prevent common security issues such as creating unnecessary external IP addresses, or granting the Editor role to all service accounts.
  * Review the full list of [organization policy constraints](https://docs.cloud.google.com/architecture/security-foundations/preventative-controls#organization-policy) to assess whether other controls are relevant for your requirements. All organizations created after May 23, 2024 have [Google Cloud security baseline constraints](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations#organization_policies_enforced_on_organization_resources) enforced when the organization resource is first created.



## What's next

  * Review the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations).
  * Read more security best practices in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-02 UTC."],[],[]] 
