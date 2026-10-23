---
url: https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters/
title: Design and architect service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:04.257088+00:00
---

# Design and architect service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/architect-perimeters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Design and architect service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

This document describes recommended VPC Service Controls deployment architectures. This document is for network administrators, security architects, and cloud operations professionals who run and operate large, production scale deployments on Google Cloud and who want to mitigate the risk of sensitive data loss.

Because VPC Service Controls protection affects cloud services functionality, we recommend that you plan the enablement of VPC Service Controls in advance, and consider VPC Service Controls during architecture design. It's important to keep VPC Service Controls design as simple as possible. We recommend that you avoid perimeter designs that use multiple bridges, perimeter network projects or a [DMZ perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/share-across-perimeters), and complex access levels.

## Use a common unified perimeter

A single large perimeter, referred to as a _common unified perimeter_ , provides the most effective protection against data exfiltration compared to using multiple, segmented perimeters.

A common unified perimeter also provides the benefit of lower management overhead for the teams responsible for perimeter creation and maintenance. Since services and network resources within a perimeter can communicate freely with the necessary IAM and network controls permissions, the teams responsible for perimeter management will primarily be concerned with north-south access, which is access from the internet to resources inside the perimeter.

When an organization uses multiple smaller perimeters, perimeter management teams must devote resources to managing east-west traffic between an organization's perimeters in addition to north-south traffic from outside the organization. Depending on the size of the organization and the number of perimeters, this overhead can be considerable. We recommend that you layer your perimeter with additional security controls and best practices, such as ensuring that resources within the VPC network don't have direct internet egress.

Service perimeters aren't intended to replace or reduce the need for IAM controls. When you are defining access controls, we recommend that you ensure that the principle of least privilege is followed and [IAM best practices](https://docs.cloud.google.com/iam/docs/using-iam-securely) are applied.

For more information, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

### Use multiple perimeters in one organization

Certain use cases might require multiple perimeters for an organization. For example, an organization that handles healthcare data might want one perimeter for high-trust, non-obfuscated data and a separate perimeter for lower-tier, de-identified data to facilitate sharing with external entities while still protecting the high-trust data.

If your organization wants to comply with standards such as [PCI DSS](https://docs.cloud.google.com/security/compliance/pci-dss), you might want to have a separate perimeter around your regulated data.

When data sharing is a primary use case for your organization, consider using more than one perimeter. If you produce and share lower-tier data like de-identified patient health data, you can use a separate perimeter to facilitate sharing with outside entities. For more information, see reference patterns for [secure data exchange](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange#share-anonymized-data-with-partner-org).

Additionally, if you use your Google Cloud organization to host independent, third-party tenants such as partners or customers, consider defining a perimeter for each tenant. If you consider data movement from from one of these tenants to another to be exfiltration, we recommend that you implement a separate perimeter.

## Perimeter design

We recommend that you enable all protected services when you create a perimeter, which helps reduce operational complexity and minimize potential exfiltration vectors. Because leaving APIs unprotected increases possible exfiltration vectors, there should be reviews and justifications if your organization opts to protect one API and not another.

All new projects should go through the review and qualification process that is described in the following sections. Include in the perimeter all the projects that pass the qualification conditions.

Make sure that there isn't a path to the private VIP from any of the VPCs in the perimeter. If you allow a network route to `private.googleapis.com`, you negate VPC Service Controls protection from insider data exfiltration. If you must allow access to a non-supported service, try to isolate the use of unsupported services into a separate project, or move the entire workload outside the perimeter.

### Review and qualify projects

A typical enterprise has many projects that represent workloads and high-level constructs such as control planes, data lakes, business units, and lifecycle stages. In addition to organizing these projects and components into folders, we recommend that you qualify them to be inside or outside of a VPC Service Controls perimeter. To make the qualification, consider the following questions:

  * Is there a component that has a hard dependency on a [service that VPC Service Controls doesn't support](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products)?

VPC Service Controls enforcement is unambiguous, so this type of dependency might not function in a perimeter. We recommend that you modify the workload to isolate the requirement for unsupported services into a separate project, or move the workload out of the perimeter altogether.

  * Does the project contain only components that have no sensitive data and don't consume sensitive data from other projects?




If you answered yes to any of the preceding questions, we recommend that you don't put the project into a perimeter. You can work around this, as discussed in the [Allowlist design](https://docs.cloud.google.com/vpc-service-controls/docs/access-level-design) topic. However, we recommend that you minimize perimeter complexity.

## What's next

  * Learn how to [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).
  * Learn how to test the impact of a perimeter using the [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).
  * Learn about [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) that enable communication between service perimeters.
  * Watch a video to [learn more about designing service perimeter architectures](https://www.youtube.com/watch?v=5t43c-p5c9Y).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
