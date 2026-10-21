---
url: https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation/
title: Migrate to Google Cloud: Plan and build your foundation \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:02.076929+00:00
---

# Migrate to Google Cloud: Plan and build your foundation  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Plan and build your foundation Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-31 UTC

This document helps you create the basic cloud infrastructure for your workloads. It can also help you plan how this infrastructure supports your applications. This planning includes identity management, organization and project structure, and networking.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads)
  * Migrate to Google Cloud: Plan and build your foundation (this document)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)
  * [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment)
  * [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
  * [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs)



The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

This document is useful if you're planning a migration from an on-premises environment, from a private hosting environment, from another cloud provider to Google Cloud, or if you're evaluating the opportunity to migrate and want to explore what it might look like. This document helps you understand the available products and decisions you'll make building a foundation focused on a migration use case.

For premade implementable options, see:

  * [Google Cloud setup checklist](https://docs.cloud.google.com/docs/enterprise/onboarding-checklist)
  * [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations)



For additional best practice guidance designing your foundation, see:

  * [Landing Zone design](https://docs.cloud.google.com/architecture/landing-zones) for designing a foundation broadly.
  * [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) for best practice guidance on system design.



When planning your migration to Google Cloud, you need to understand an array of topics and concepts related to cloud architecture. A poorly planned foundation can cause your business to face delays, confusion, and downtime, and can put the success of your cloud migration at risk. This guide provides an overview of Google Cloud foundation concepts and decision points.

Each section of this document poses questions that you need to ask and answer for your organization before building your foundation on Google Cloud. These questions are not exhaustive; they are meant to facilitate a conversation between your architecture teams and business leadership about what is right for your organization. Your plans for infrastructure, tooling, security, and account management are unique for your business and need deep consideration. When you finish this document and answer the questions for your organization, you're ready to begin the formal planning of your cloud infrastructure and services that support your migration to Google Cloud.

## Enterprise considerations

Consider the following questions for your organization:

  * Which IT responsibilities might change between you and your infrastructure provider when you move to Google Cloud?
  * How can you support or meet your regulatory compliance needs—for example, HIPAA or GDPR—during and after your migration to Google Cloud?
  * How can you control where your data is stored and processed in accordance with your data residency requirements?



### Shared responsibility model

The shared responsibilities between you and Google Cloud might be different than those you are used to, and you need to understand their implications for your business. The processes you previously implemented to provision, configure, and consume resources might change.

Review the [Terms of Service](https://cloud.google.com/terms/) and the [Google security model](https://cloud.google.com/security) for an overview of the contractual relationship between your organization and Google, and the implications of using a public cloud provider.

### Compliance, security, and privacy

Many organizations have compliance requirements around industry and government standards, regulations, and certifications. Many enterprise workloads are subject to regulatory scrutiny, and can require attestations of compliance by you and your cloud provider. If your business is regulated under [HIPAA or HITECH](https://cloud.google.com/security/compliance/hipaa/), make sure you understand [your responsibilities](https://cloud.google.com/security/compliance/hipaa/#customer_responsibilities) and which Google Cloud services are regulated. For information about Google Cloud certifications and compliance standards, see the [Compliance resource center](https://cloud.google.com/compliance). For more information about region-specific or sector-specific regulations, see [Google Cloud and the General Data Protection Regulation (GDPR)](https://cloud.google.com/privacy/gdpr).

[Trust and security](https://cloud.google.com/security) are important to every organization. Google Cloud implements a shared security model for many services.

The [Google Cloud trust principles](https://cloud.google.com/privacy) can help you understand our commitment to protecting the privacy of your data and your customers' data. For more information about Google's design approach for security and privacy, read the [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).

For more information about implementing a secure baseline on Google Cloud, see [Google Cloud minimum viable secure platform](https://docs.cloud.google.com/docs/security/gcmvsp).

### Data residency considerations

Geography can also be an important consideration for compliance. Make sure that you understand your data residency requirements and implement policies for deploying workloads into new regions to [control where your data is stored and processed](https://cloud.google.com/terms/data-processing-addendum). Understand how to use [resource location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to help ensure that your workloads can only be deployed in pre-approved [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). You need to account for the [regionality of different Google Cloud services](https://docs.cloud.google.com/docs/geography-and-regions#multiregional_resources) when choosing the deployment target for your workloads. Make sure that you understand your regulatory compliance requirements and how to implement a governance strategy that helps you ensure compliance.

## Resource hierarchy

Consider the following questions for your organization:

  * How do your existing business and organizational structures map to Google Cloud?
  * How often do you expect changes to your resource hierarchy?
  * How do project quotas impact your ability to create resources in the cloud?
  * How can you incorporate your existing cloud deployments with your migrated workloads?
  * What are best practices for managing multiple teams working simultaneously on multiple Google Cloud projects?



Your current business processes, lines of communication, and reporting structure are reflected in the design of your Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). The resource hierarchy provides the necessary structure to your cloud environment, determines the way you are billed for resource consumption, and establishes a security model for granting roles and permissions. You need to understand how these facets are implemented in your business today, and plan how to migrate these processes to Google Cloud.

### Understand Google Cloud resources

Resources are the fundamental components that make up all of Google Cloud services. The [Organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) is the apex of the Google Cloud resource hierarchy. All resources that belong to an organization are grouped under the organization node. This structure provides central visibility and control over every resource that belongs to an organization.

An Organization can contain one or more [folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders), and each folder can contain one or more projects. You can use folders to group related projects.

[Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) contain service resources such as [Compute Engine](https://docs.cloud.google.com/compute) virtual machines (VMs), [Pub/Sub](https://docs.cloud.google.com/pubsub) topics, [Cloud Storage](https://docs.cloud.google.com/storage) buckets, [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) endpoints, and other Google Cloud services. You can create resources by using the Google Cloud console, Cloud Shell, or the Cloud APIs. If you expect frequent changes to your environment, consider adopting an infrastructure as a code (IaC) approach to streamline resource management.

### Manage your Google Cloud projects

For more information about planning and managing your Google Cloud resource hierarchy, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy). If you're already working in Google Cloud and have created independent projects as tests or proofs-of-concept, you can [migrate existing Google Cloud projects into your organization](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing).

## Identity and Access Management

Consider the following questions for your organization:

  * Who will control, administer, and audit access to Google Cloud resources?
  * How will your existing security and access policies change when you move to Google Cloud?
  * How will you securely enable your users and apps to interact with Google Cloud services?



[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) lets you grant granular access to Google Cloud resources. [Cloud Identity](https://docs.cloud.google.com/identity) is a separate but related service that can help you migrate and manage your identities. At a high level, understanding how you want to manage access to your Google Cloud resources forms the basis for how you provision, configure, and maintain IAM.

### Understand identities

Google Cloud uses [identities](https://docs.cloud.google.com/identity/docs/concepts/overview) for authentication and access management. To access any Google Cloud resources, a member of your organization must have an identity that Google Cloud can understand. Cloud Identity is an identity as a service (IDaaS) platform that lets you centrally manage users and groups who can access Google Cloud resources. By setting up your users in Cloud Identity, you can set up [single sign-on](https://docs.cloud.google.com/identity) (SSO) with thousands of third-party software as a service (SaaS) applications. The way you set up Cloud Identity depends on how you manage identities.

For more information about identity provisioning options for Google Cloud, see [Decide how to onboard identities to Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities).

### Understand access management

The model for managing access consists of four core concepts:

  * _Principal_ : Can be a Google Account (for end users), a [service account](https://docs.cloud.google.com/iam/docs/understanding-service-accounts) (for Google Cloud products), a [Google Group](https://groups.google.com), or a Google Workspace or Cloud Identity account that can access a resource. Principals cannot perform any action that they aren't permitted to do.
  * [_Role_](https://docs.cloud.google.com/iam/docs/understanding-roles): A collection of permissions.
  * [_Permission_](https://docs.cloud.google.com/iam/docs/overview#permissions): Determines what operations are allowed on a resource. When you grant a role to a principal, you grant all the permissions that the role contains.
  * [_IAM allow policy_](https://docs.cloud.google.com/iam/docs/overview#iam_policy): Binds a set of principals to a role. When you want to define which principals have access to a resource, you create a policy and attach it to the resource.



Proper setup and effective management of principals, roles, and permissions forms the backbone of your security posture in Google Cloud. Access management helps protect you from internal misuse, and helps protect you from external attempts at unauthorized access to your resources.

### Understand application access

In addition to users and groups, there is another kind of identity known as a [service account](https://docs.cloud.google.com/iam/docs/service-accounts). A service account is an identity that your programs and services can use to authenticate and gain access to Google Cloud resources.

[User-managed service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts#user-managed_service_accounts) include service accounts that you explicitly create and manage using IAM, and the Compute Engine default service account that comes built into all Google Cloud projects. [Service agents](https://docs.cloud.google.com/compute/docs/access/service-accounts#google-managed_service_accounts) are automatically created, and run internal Google processes on your behalf.

When using service accounts, it's important to understand [application default credentials](https://docs.cloud.google.com/docs/authentication/production), and follow our recommended [best practices for service accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts#best_practices) to avoid exposing your resources to undue risk. The most common risks involve privilege escalation or accidental deletion of a service account that a critical application relies on.

### Follow best practices

For more information about best practices to manage identity and access effectively, see [Verify every access attempt explicitly](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust#verify_every_access_attempt_explicitly).

## Billing

How you pay for Google Cloud resources that you consume is an important consideration for your business, and an important part of your relationship with Google Cloud. You can manage billing in the Google Cloud console with [Cloud Billing](https://docs.cloud.google.com/billing/docs) alongside the rest of your cloud environment.

The concepts of resource hierarchy and [billing](https://docs.cloud.google.com/billing/docs/concepts) are closely related, so it's critical that you and your business stakeholders understand these concepts.

For more information about best practices, tools and techniques to help you track and control costs, see [Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).

## Connectivity and networking

For more information about designing your network on Google Cloud, see:

  * [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design).
  * [Implement your Google Cloud landing zone network design](https://docs.cloud.google.com/architecture/landing-zones/implement-network-design).



If your source environment is in another cloud service provider, you might need to connect it with your Google Cloud environment. For more information, see [Patterns for connecting other cloud service providers with Google Cloud](https://docs.cloud.google.com/architecture/patterns-for-connecting-other-csps-with-gcp).

When migrating production data and workloads to Google Cloud, we recommend that you consider how the availability of the connectivity solution can affect the success of your migration. For example, [Cloud Interconnect provides supports production-level SLA if you provision it according to specific topologies](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/production-level-overview).

When migrating data from your source environment to your Google Cloud environment, you should adjust the maximum transmission unit (MTU) to take protocol overhead into account. Doing so helps ensure that the data is transferred efficiently and accurately. This adjustment can also help prevent delays caused by data fragmentation and network performance issues. For example, if you're using Cloud VPN to connect your source environment to your Google Cloud environment, you might need to configure the MTU to a lower value to accommodate the VPN protocol overhead in each transmission unit.

To help you avoid connectivity issues during your migration to Google Cloud, we recommend that you:

  * Ensure that DNS records resolve across the source environment and your Google Cloud environment.
  * Ensure that network routes between the source environment and your Google Cloud environment correctly propagate across environments.



If you need to provision and use your own public IPv4 addresses in your VPCs, see [Bring your own IP address](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).

### Understand DNS options

[Cloud DNS](https://docs.cloud.google.com/dns) can serve as your public domain name system (DNS) server. For more information about how you can implement Cloud DNS, see [Cloud DNS best practices](https://docs.cloud.google.com/dns/docs/best-practices-dns).

If you need to customize how Cloud DNS responds to queries according to their source or destination, see [DNS policies overview](https://docs.cloud.google.com/dns/docs/policies-overview). For example, you can configure Cloud DNS to forward queries to your existing DNS servers, or you can override private DNS responses based on the query name.

A separate but similar service, called internal DNS, is included with your VPC. Instead of manually migrating and configuring your own DNS servers, you can use the internal DNS service for your private network. For more information, see [Overview of internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns).

### Understand data transfer

On-premises networking is managed and priced in a fundamentally different way than cloud networking. When managing your own data center or colocation facility, installing routers, switches, and cabling requires a fixed, upfront capital expenditure. In the cloud, you are billed for data transfer rather than the fixed cost of installing hardware, plus the ongoing cost of maintenance. Plan and manage data transfer costs accurately in the cloud by understanding data transfer costs.

When planning for traffic management, there are three ways you are charged:

  * _Ingress traffic_ : Network traffic that enters your Google Cloud environment from outside locations. These locations can be from the public internet, on-premises locations, or other cloud environments. Ingress is free for most services on Google Cloud. Some services that deal with internet-facing traffic management, such as [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing), [Cloud CDN](https://docs.cloud.google.com/cdn), and [Google Cloud Armor](https://docs.cloud.google.com/armor) charge based on how much ingress traffic they handle.
  * _Egress traffic_ : Network traffic that leaves your Google Cloud environment in any way. Egress charges apply to many Google Cloud services, including Compute Engine, Cloud Storage, [Cloud SQL](https://docs.cloud.google.com/sql), and [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * _Regional and zonal traffic_ : Network traffic that crosses regional or zonal boundaries in Google Cloud can also be subject to bandwidth charges. These charges can impact how you choose to design your apps for disaster recovery and high availability. Similar to egress charges, cross-regional and cross-zonal traffic charges apply to many Google Cloud services and are important to consider when planning for high availability and disaster recovery. For example, sending traffic to a database replica in another zone is subject to cross-zonal traffic charges



### Automate and control your network setup

In Google Cloud, the physical network layer is virtualized, and you deploy and configure your network using [software-defined networking](https://wikipedia.org/wiki/Software-defined_networking) (SDN). To ensure that your network is configured in a consistent and repeatable way, you need to understand how to automatically deploy and tear down your environments. You can use IaC tools, such as [Terraform](https://www.terraform.io/).

## Security

The way you manage and maintain the security of your systems in Google Cloud, and the tools you use, are different than when managing an on-premises infrastructure. Your approach will change and evolve over time to adapt to new threats, new products, and improved security models.

The responsibilities that you share with Google might be different than the responsibilities of your current provider, and understanding these changes is critical to ensuring the continued security and compliance of your workloads. Strong, verifiable security and regulatory compliance are often intertwined, and begin with strong management and oversight practices, consistent implementation of Google Cloud best practices, and active threat detection and monitoring.

For more information about designing a secure environment on Google Cloud, see [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security).

## Monitoring, alerting, and logging

For more information about setting up monitoring, alerting, and logging, see:

  * [Centrally aggregate audit logs](https://docs.cloud.google.com/architecture/security-log-analytics)
  * [Review best practices for protecting access to your sensitive logs](https://docs.cloud.google.com/logging/docs/audit/best-practices)



## Governance

Consider the following questions for your organization:

  * How can you ensure your users support and meet their compliance needs and align them with your business policies?
  * What strategies are available to maintain and organize your Google Cloud users and resources?



Effective governance is critical for helping to ensure reliability, security, and maintainability of your assets in Google Cloud. As in any system, entropy naturally increases over time and left unchecked, it can result in cloud sprawl and other maintainability challenges. Without effective governance, the accumulation of these challenges can impact your ability to achieve your business objectives and to reduce risk. Disciplined planning and enforcement of standards around naming conventions, labeling strategies, access controls, cost controls, and service levels is an important component of your cloud migration strategy. More broadly, the exercise of developing a governance strategy creates alignment among stakeholders and business leadership.

### Support continuous compliance

To help support organization-wide compliance of your Google Cloud resources, consider establishing a consistent resource [naming and grouping strategy](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#common-uses). Google Cloud provides several methods for annotating and enforcing policies on resources:

  * [Security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-asset-inventory#using_security_marks) let you classify resources to provide security insights from [Security Command Center](https://docs.cloud.google.com/security-command-center), and to enforce policies on groups of resources.
  * [Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) can track your resource spend in Cloud Billing, and provide extra insights in Cloud Logging.
  * [Tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) let you define sources and targets in global network firewall policies and regional network firewall policies.



For more information, see [Risk and compliance as code](https://docs.cloud.google.com/solutions/risk-and-compliance-as-code).

## What's next

  * Learn how to implement a [secure foundation in Google Cloud](https://docs.cloud.google.com/architecture/blueprints/security-foundations).
  * Continue your cloud migration and explore [transferring your data to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Travis Webb](https://www.linkedin.com/in/-traviswebb/) | Solution Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-31 UTC."],[],[]] 
