---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/
title: Enterprise foundations blueprint \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:21.289038+00:00
---

# Enterprise foundations blueprint  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Enterprise foundations blueprint Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

This document describes the best practices that let you deploy a foundational set of resources in Google Cloud. A cloud foundation is the baseline of resources, configurations, and capabilities that enable companies to adopt Google Cloud for their business needs. A well-designed foundation enables consistent governance, security controls, scale, visibility, and access to shared services across all workloads in your Google Cloud environment. After you deploy the controls and governance that are described in this document, you can deploy workloads to Google Cloud.

The _enterprise foundations blueprint_ (formerly known as the _security foundations blueprint_) is intended for architects, security practitioners, and platform engineering teams who are responsible for designing an enterprise-ready environment on Google Cloud. This blueprint consists of the following:

  * A [terraform-example-foundation GitHub repository](https://github.com/terraform-google-modules/terraform-example-foundation) that contains the deployable Terraform assets.
  * A guide that describes the architecture, design, and controls that you implement with the blueprint (this document).



You can use this guide in one of two ways:

  * To create a complete foundation based on Google's best practices. You can deploy all the recommendations from this guide as a starting point, and then customize the environment to address your business' specific requirements.
  * To review an existing environment on Google Cloud. You can compare specific components of your design against Google-recommended best practices.



## Supported use cases

The enterprise foundation blueprint provides a baseline layer of resources and configurations that help enable all types of workloads on Google Cloud. Whether you're migrating existing compute workloads to Google Cloud, building containerized web applications, or creating big data and machine learning workloads, the enterprise foundation blueprint helps you build your environment to support enterprise workloads at scale.

After you deploy the enterprise foundation blueprint, you can deploy workloads directly or deploy additional blueprints to support complex workloads that require additional capabilities.

## A defense-in-depth security model

Google Cloud services benefit from the underlying [Google infrastructure security design](https://docs.cloud.google.com/docs/security/infrastructure/design). It is your responsibility to design security into the systems that you build on top of Google Cloud. The enterprise foundation blueprint helps you to implement a defense-in-depth security model for your Google Cloud services and workloads.

The following diagram shows a defense-in-depth security model for your Google Cloud organization that combines architecture controls, policy controls, and detective controls.

![The defense-in-depth security model.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-security-model.svg)

The diagram describes the following controls:

  * **Policy controls** are programmatic constraints that enforce acceptable resource configurations and prevent risky configurations. The blueprint uses a combination of policy controls including infrastructure-as-code (IaC) validation in your pipeline and organization policy constraints.
  * **Architecture controls** are the configuration of Google Cloud resources like networks and resource hierarchy. The blueprint architecture is based on security best practices.
  * **Detective controls** let you detect anomalous or malicious behavior within the organization. The blueprint uses platform features such as Security Command Center, integrates with your existing detective controls and workflows such as a security operations center (SOC), and provides capabilities to enforce custom detective controls.



## Key decisions

This section summarizes the high-level architectural decisions of the blueprint.

![Key Google Cloud services in the blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/efb-key-decisions.svg)

The diagram describes how Google Cloud services contribute to key architectural decisions:

  * **Cloud Build:** Infrastructure resources are managed using a GitOps model. Declarative IaC is written in Terraform and managed in a version control system for review and approval, and resources are deployed using Cloud Build as the continuous integration and continuous deployment (CI/CD) automation tool. The pipeline also enforces policy-as-code checks to validate that resources meet expected configurations before deployment.
  * **Cloud Identity:** Users and group membership are synchronized from your existing identity provider. Controls for user account lifecycle management and single sign-on (SSO) rely on the existing controls and processes of your identity provider.
  * **Identity and Access Management (IAM):** Allow policies (formerly known as IAM policies) allow access to resources and are applied to groups based on job function. Users are added to the appropriate groups to receive view-only access to foundation resources. All changes to foundation resources are deployed through the CI/CD pipeline which uses privileged service account identities.
  * **Resource Manager:** All resources are managed under a single organization, with a resource hierarchy of folders that organizes projects by environments. Projects are labeled with metadata for governance including cost attribution.
  * **Networking** : Network topologies use Shared VPC to provide network resources for workloads across multiple [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) and zones, separated by environment, and managed centrally. All network paths between on-premises hosts, Google Cloud resources in the VPC networks, and Google Cloud services are private. No outbound traffic to or inbound traffic from the public internet is permitted by default.
  * **Cloud Logging** : Aggregated log sinks are configured to collect logs relevant for security and auditing into a centralized project for long-term retention, analysis, and export to external systems.
  * **Organization Policy Service:** Organization policy constraints are configured to prevent various high-risk configurations.
  * **Secret Manager:** Centralized projects are created for a team responsible for managing and auditing the use of sensitive application secrets to help meet compliance requirements.
  * **Cloud Key Management Service (Cloud KMS):** Centralized projects are created for a team responsible for managing and auditing encryption keys to help meet compliance requirements.
  * **Security Command Center:** Threat detection and monitoring capabilities are provided using a combination of built-in security controls from Security Command Center and custom solutions that let you detect and respond to security events.



For alternatives to these key decisions, see [alternatives](https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary#alternatives).

## What's next

  * Read about [authentication and authorization](https://docs.cloud.google.com/architecture/blueprints/security-foundations/authentication-authorization) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
