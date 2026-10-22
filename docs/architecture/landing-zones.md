---
url: https://docs.cloud.google.com/architecture/landing-zones/
title: Landing zone design in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:51.051815+00:00
---

# Landing zone design in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/landing-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Landing zone design in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-02 UTC

This document provides an overview on how to design landing zones in Google Cloud. A landing zone, also called a _cloud foundation_ , is a modular and scalable configuration that enables organizations to adopt Google Cloud for their business needs. A landing zone is often a prerequisite to deploying enterprise workloads in a cloud environment.

A _landing zone_ is not a [zone](https://cloud.google.com/docs/geography-and-regions#regions_and_zones) or [zonal resources](https://cloud.google.com/docs/geography-and-regions#zonal_resources).

This document is aimed at solutions architects, technical practitioners, and executive stakeholders who want an overview of the following:

  * Typical elements of landing zones in Google Cloud
  * Where to find detailed information on landing zone design
  * How to deploy a landing zone for your enterprise, including options to deploy pre-built solutions



This document is part of a series that helps you understand how to design and build a landing zone. The other documents in this series help guide you through the high-level decisions that you need to make when you design your organization's landing zone. In this series, you learn about the following:

  * Landing zone design in Google Cloud (this document)
  * [Decide how to onboard identities to Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities)
  * [Decide the resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy)
  * [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)
  * [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security)



This series does not specifically address compliance requirements from regulated industries such as financial services or healthcare.

## What is a Google Cloud landing zone?

Landing zones help your enterprise deploy, use, and scale Google Cloud services more securely. Landing zones are dynamic and grow as your enterprise adopts more cloud-based workloads over time.

To deploy a landing zone, you must first [create an organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) and [create a billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account), either online or invoiced.

A landing zone spans multiple areas and includes different elements, such as identities, resource management, security, and networking. Many other elements can also be part of a landing zone, as described in Elements of a landing zone.

The following diagram shows a sample implementation of a landing zone. It shows an Infrastructure as a Service (IaaS) use case with hybrid cloud and on-premises connectivity in Google Cloud:

![Example architecture for a landing zone.](https://docs.cloud.google.com/static/architecture/landing-zones/images/landing-zone-design-overview.svg)

The example architecture in the preceding diagram shows a Google Cloud landing zone that includes the following Google Cloud services and features:

  * Resource Manager defines a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) with [organizational policies.](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)

  * A [Cloud Identity](https://docs.cloud.google.com/identity/docs/overview) account synchronizes with an on-premises identity provider and [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) providing granular access to Google Cloud resources.

  * A network deployment that includes the following:

    * A [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) network for each environment (production, development, and testing) connects resources from multiple projects to the VPC network.
    * [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) control connectivity to and from workloads in the [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) networks.
    * A [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway allows outbound connections to the internet from resources in these networks without external IP addresses.
    * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) connects on-premises applications and users. (You can choose between different Cloud Interconnect options, including [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).)
    * [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) (or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn)) connects to other cloud service providers.
    * A [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) private zone hosts DNS records for your deployments in Google Cloud.
  * Multiple service projects are configured to use the [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) networks. These service projects host your application resources.

  * [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) includes [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) for monitoring and [Cloud Logging](https://docs.cloud.google.com/logging/docs) for logging. [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) and [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) help ensure all necessary data is logged and available for analysis.

  * A [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter isolates service and resources, which helps to mitigate the risk of data egress to Google Cloud services outside the perimeter. Traffic from hybrid environments is configured with authorized private access to communicate with services inside the perimeter.




The diagram above is only an example, because there is no single or standard implementation of a landing zone. Your business must make many design choices, depending on different factors, including the following:

  * Your industry
  * Your organizational structure and processes
  * Your security and compliance requirements
  * The workloads that you want to move to Google Cloud
  * Your existing IT infrastructure and other cloud environments
  * The location of your business and customers



## When to build a landing zone

We recommend that you build a landing zone before you deploy your first enterprise workload on Google Cloud, because a landing zone provides the following:

  * A foundation that's designed to be secure
  * The network for enterprise workloads
  * The tools that you require to govern your internal cost distribution



However, because a landing zone is modular, your first iteration of a landing zone is often not your final version. Therefore, we recommend that you design a landing zone with scalability and growth in mind. For example, if your first workload does not require access to on-premises network resources, you could build connectivity to your on-premises environment later.

Depending on your organization and the type of workloads that you plan to run on Google Cloud, some workloads might have very different requirements. For example, some workloads might have unique scalability or compliance requirements. In these cases, you might require more than one landing zone for your organization: one landing zone to host most of the workloads and a separate landing zone to host the unique workloads. You can share some elements such as identities, billing, and the organization resource across your landing zones. However, other elements, such as the network setup, deployment mechanisms, and folder-level policies, might vary.

## Elements of a landing zone

A landing zone requires you to design the following core elements on Google Cloud:

  * [Identity provisioning ](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities)
  * [Resource hierarchy ](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy)

  * [Network](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)

  * [Security controls](https://docs.cloud.google.com/architecture/landing-zones/decide-security)




In addition to these core elements, your business might have additional requirements. The following table describes these elements and where you can find more information about them.

Landing zone element |  Description  
---|---  
Monitoring and logging |  Design a monitoring and logging strategy that helps ensure all relevant data is logged and that you have dashboards that visualize the data and alerts that notify you of any actionable exceptions.   
For more information, see the [Monitoring, logging, and alerting](https://docs.cloud.google.com/docs/security/gcmvsp/monitoring-logging-alerting) section of the Google Cloud minimum viable secure platform.   
Backup and disaster recovery |  Design a strategy for backups and disaster recovery.   
For more information, see the following: 

  * [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)
  * [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)

  
Compliance |  Follow the compliance frameworks that are relevant to your organization.  
For more information, see the [Compliance resource center](https://cloud.google.com/compliance).  
Cost efficiency and control |  Design capabilities to monitor and optimize cost for workloads in your landing zone.   
For more information, see the following: 

  * [Overview of cloud billing concepts](https://docs.cloud.google.com/billing/docs/concepts)
  * [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management](https://cloud.google.com/cost-management)

  
API management |  Design a scalable solution for APIs that you develop. For more information, see [Apigee API Management](https://docs.cloud.google.com/apigee).  
Cluster management |  Design Google Kubernetes Engine (GKE) clusters that follow best practices to build scalable, resilient, and observable services. For more information, see the following:

  * [GKE best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices)
  * [GKE Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
  * [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services)
  * [About Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)

  
  
## Best practices for designing and deploying a landing zone

Designing and deploying a landing zone requires planning. You must have the right team to perform the tasks, and use a project management process. We also recommend that you follow the technical best practices that are described in this series.

### Build a team

Bring together a team that includes people from multiple technical functions across the organization. The team must include people who can build all landing zone elements, including security, identity, networks, and operations. Identify a cloud practitioner who understands Google Cloud to lead the team. Your team should include members who manage the project and track achievements, and members who collaborate with application or business owners.

Make sure that all stakeholders are involved early in the process. Your stakeholders must come to a common understanding of the scope of the process and make high-level decisions when the project gets kicked off.

### Apply project management to your landing zone deployment

Designing and deploying your landing zone can take multiple weeks, so project management is essential. Ensure that project goals are clearly defined and communicated to all stakeholders and that all parties receive updates on any project changes. Define regular checkpoints and agree on milestones with realistic timelines that take operational processes and unexpected delays into account.

To best align with business requirements, plan the initial landing zone deployment around the use cases that you want to deploy first in Google Cloud. We recommend that you first deploy workloads that can most easily run on Google Cloud, such as horizontally scaling multi-tier web applications. These workloads might be new or existing workloads. To assess existing workloads for migration readiness, see [Migration to Google Cloud: Getting started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).

Because landing zones are modular, center the initial design around the elements that are required to migrate your first workloads and plan to add other elements later.

### Follow technical best practices

Consider using [Infrastructure as Code (IaC)](https://en.wikipedia.org/wiki/Infrastructure_as_code), with, for example, [Terraform](https://docs.cloud.google.com/docs/terraform). IaC helps you make your deployment repeatable and modular. Having a [CI/CD pipeline that deploys cloud infrastructure changes](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code) using GitOps helps you ensure that you follow internal guidelines and put the right controls in place.

When you design your landing zone, ensure that you and your team take technical best practices into consideration. For more information on decisions to make in your landing zone, see the other guides in this series.

In addition to this series, the following table describes frameworks, guides, and blueprints that can also help you follow best practices, depending on your use cases.

Related documentation | Description  
---|---  
[Google Cloud Setup](https://docs.cloud.google.com/docs/enterprise/cloud-setup) |  A high-level guided flow to help you set up Google Cloud for scalable, production-ready, enterprise workloads.  
[Enterprise foundation blueprint](https://docs.cloud.google.com/architecture/security-foundations) |  An opinionated view of Google Cloud security best practices, aimed at CISO, security practitioners, risk managers, or compliance officers.  
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) |  Recommendations and best practices to help architects, developers, administrators, and other cloud practitioners design and operate a cloud topology that's secure, efficient, resilient, high-performing, and cost-effective.  
[Terraform blueprints](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) |  A list of blueprints and modules that are packaged as Terraform modules and that you can use to create resources for Google Cloud.  
  
## Identify resources to help implement your landing zone

Google Cloud offers the following options to help you set up your landing zone:

  * Design and deploy a landing zone that is customized to your requirements with [Google Cloud partners](https://cloud.google.com/partners) or Google Cloud [professional services](https://cloud.google.com/consulting).
  * Onboard a workload with the [Google Cloud Customer Onboarding program](http://cloud.google.com/onboarding).
  * Deploy a generic landing zone with the [setup guide in the Google Cloud console](https://console.cloud.google.com/cloud-setup/overview).
  * Deploy a highly opinionated landing zone by using the [Terraform example foundation](https://github.com/terraform-google-modules/terraform-example-foundation).



All these offerings have approaches that are designed specifically to meet the needs of different industries and business sizes, across the globe. To help you make the best selection for your use case, we recommend that you work with your Google Cloud account team to make the selection and help to ensure a successful project.

## What's next

  * [Decide how to onboard identities to Google Cloud](https://docs.cloud.google.com/architecture/landing-zones/decide-how-to-onboard-identities) (next document in this series).
  * [Decide the resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).
  * [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design).
  * [Decide the security for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-02 UTC."],[],[]] 
