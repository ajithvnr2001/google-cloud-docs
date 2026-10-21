---
url: https://docs.cloud.google.com/architecture/gke-pci-dss-blueprint/
title: Security blueprint: PCI on GKE \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:36:01.012447+00:00
---

# Security blueprint: PCI on GKE  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/gke-pci-dss-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Security blueprint: PCI on GKE Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-03-12 UTC

The PCI on Google Kubernetes Engine blueprint contains a set of [Terraform](https://www.terraform.io/) configurations and scripts that demonstrate how to bootstrap a PCI environment in Google Cloud. The core of this blueprint is the [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) application, where users can browse items, add them to the cart, and purchase them.

This blueprint was developed for [Payment Card Industry Data Security Standard (PCI DSS)](https://www.pcisecuritystandards.org/pci_security/maintaining_payment_security) version 3.2.1. The blueprint lets you deploy workloads on GKE that align with the PCI DSS in a repeatable, supported, and secure way.

  * **Architecture**
  * **Compliance mapping**
  * **Deployable assets**
  * **Frequently asked questions**
  * **Resources**



## Architecture

### Project overview

In this blueprint, you bootstrap a cardholder data environment (CDE) in Google Cloud that contains the following resource hierarchy:

  * An [Organizational](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) resource.
  * A [Folder](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) resource. Folder resources provide a grouping mechanism and isolation boundaries between projects.
  * [Project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) resources. You deploy the following Google Cloud projects:

    * Network: The host project for the Shared VPC.
    * Management: A project that will hold the logging and monitoring infrastructure, such as Cloud Logging.
    * In-scope: A project that contains the in-scope resources. In this solution, the project consists of a GKE cluster that's designed to run the in-scope applications. In the example, this includes the Frontend, Payment, and Checkout services.
    * Out-of-scope: A project that contains the out-of-scope resources. In the solution, that's a GKE cluster that's designed to run the rest of the services.



![Project overview.](https://docs.cloud.google.com/static/architecture/images/pci-gke-dss-architecture-project-overview.svg)

### Application and projects

The following diagram illustrates the CDE boundary on Google Cloud and which projects are in the scope of your PCI assessment of the Microservices Demo application. As you build your environment, you use an illustration like this to communicate Google Cloud about resources into and out of your PCI boundary.

The path labeled `1` shows log data from Kubernetes clusters going to Cloud Logging.

![Application deployment.](https://docs.cloud.google.com/static/architecture/images/pci-gke-dss-architecture-application-deployment.svg)

### Network layout

This diagram illustrates the network and subnet details within each project. It documents the data flows between projects and into and out of the CDE boundary.

![Network layout.](https://docs.cloud.google.com/static/architecture/images/pci-gke-dss-architecture-network-layout.svg)

### Encrypted traffic

This diagram illustrates the encrypted traffic going into and out of the PCI boundary:

  1. TLS-encrypted (HTTPS) traffic from outside the VPC goes to the in-scope public load balancer.
  2. TLS-encrypted traffic between in-scope Kubernetes cluster nodes to the out-of-scope cluster goes to internal load balancers.
  3. Traffic from the internal load balancers to the out-of-scope cluster is encrypted with mTLS using Istio.
  4. Communication within each cluster is encrypted with mTLS using Istio.



![Encrypted traffic.](https://docs.cloud.google.com/static/architecture/images/pci-gke-dss-architecture-encrypted-traffic.svg)

## Compliance mapping

The blueprint described in this document addresses a range of PCI DSS compliance requirements. The table in this section highlights some of those requirements.

**Note:** The [PCI on GKE Blueprint Review for PCI Compliance](https://docs.cloud.google.com/static/architecture/google-cloud-pci-gke-review.pdf) whitepaper (PDF) provides an independent, third-party assessment of the blueprint performed by [Coalfire](https://www.coalfire.com/), Google's PCI-DSS auditor. It also provides guidance on elements that you should address when you adopt the blueprint.

The items in the following table don't address all requirements; compliance with some requirements is met by the Google Cloud infrastructure as part of the shared responsibility between you and Google. Compliance with other requirements needs to be implemented by you. For a detailed explanation of the shared responsibility model, see [Exploring container security: the shared responsibility model in GKE](https://cloud.google.com/blog/products/containers-kubernetes/exploring-container-security-the-shared-responsibility-model-in-gke-container-security-shared-responsibility-model-gke) on the Google Cloud blog.

**Note:** The compliance mapping describes how controls implemented in this blueprint help you comply with a PCI requirement; however, the blueprint does not guarantee PCI compliance for the requirements specified later in this document. It's important to note that the description of the implementation details in this blueprint must be reviewed, evaluated, assessed, and approved by you and your Qualified Security Assessor (QSA), and layered with other security features that address all of the in-scope systems and applications for a holistic solution to meet the PCI requirements.

The numbers in parentheses refer to sections of the Payment Card Industry (PCI) Data Security Standard document. You can download the document from the PCI Security Standards Council website's [document library](https://www.pcisecuritystandards.org/document_library?category=pcidss&document=pci_dss).

Requirement | Section | Description  
---|---|---  
**Implement segmentation and boundary protection** | 1.3.2, 1.3.4 |  This blueprint helps you implement a logical segmentation by using Google Cloud projects; the segmentation lets you create a boundary for your PCI assessment. This blueprint runs [ Istio on Google Kubernetes Engine](https://cloud.google.com/istio) as an add-on that lets you create a service mesh around the GKE cluster that includes all of the components you need. The blueprint also creates a security perimeter using [ VPC](https://docs.cloud.google.com/vpc-service-controls/docs) around all of the Google Cloud projects that are in scope for PCI.   
**Configure least-privilege access to Google Cloud resources** | 7.1, 7.2 |  This blueprint helps you to implement role-based access control to manage who has access to Google Cloud resources. The blueprint also implements GKE-specific access controls like [ role-based access control (RBAC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control) and [ namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) to restrict access to cluster resources.   
**Establish Organization-level policies** |  |  With this blueprint, you establish policies that apply to your Google Cloud [ Organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) resource, such as the following: 

  * No external IP addresses
  * [Domain restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains)
  * [Trusted images](https://cloud.google.com/blog/products/identity-security/deploy-only-what-you-trust-introducing-binary-authorization-for-google-kubernetes-engine)

  
**Enforce separation of duties through Shared VPC** | 7.1.2, 7.1.3 | This blueprint uses [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) for connectivity and segregated network control to enforce [separation of duties](https://en.wikipedia.org/wiki/Separation_of_duties).   
**Harden your cluster's security** | 2.2, 2.2.5 | The GKE clusters in this blueprint are hardened as described in the [ GKE hardening guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).   
  
This list is just a subset of the security controls implemented in this blueprint that can meet PCI DSS requirements. You can find a full list of those requirements that are addressed in the [PCI DSS Requirements](https://github.com/GoogleCloudPlatform/pci-gke-blueprint/blob/master/docs/assets/pci-mapping.pdf) (PDF) document on GitHub.

## Deployable assets

The [PCI and GKE Blueprint](https://github.com/GoogleCloudPlatform/pci-gke-blueprint) repository on GitHub contains a set of Terraform configurations and scripts that show how to bootstrap a PCI environment in Google Cloud. The PCI on GKE project also showcases Google Cloud services, tools, and projects that are useful to start your own Google Cloud PCI environment.

## Frequently asked questions

###  How do I use this blueprint? 

The PCI on GKE blueprint provides you with prescriptive information and instructions for creating or migrating workloads on GKE that align with PCI compliance requirements. 

The blueprint is made up of the following elements: 

  * [An implementation guide](https://github.com/GoogleCloudPlatform/pci-gke-blueprint)
  * [Reference architectures](https://github.com/GoogleCloudPlatform/pci-gke-blueprint/blob/master/docs/diagrams.md)
  * [Terraform](http://terraform.io) scripts that implement infrastructure as code (IaC) 
  * [A demo application](https://github.com/GoogleCloudPlatform/pci-gke-blueprint/blob/master/docs/deploy-application.md)
  * [PCI compliance mappings](https://github.com/GoogleCloudPlatform/pci-gke-blueprint/blob/master/docs/assets/pci-mapping.pdf)



We recommend that you read through the implementation guide and review the reference architectures before deploying the PCI environment using Terraform. We've provided a demo ecommerce application that you can deploy to test the PCI blueprint environment. 

###  Is this the only way to run PCI-compliant workloads on Google Cloud? 

No. PCI DSS is a set of security standards and there are many ways to interpret and implement the controls to satisfy the standards. This blueprint is designed as a set of best practices and recommendations to support your own PCI DSS compliance. 

###  Does this blueprint include best practices for PCI compliance for Google Distributed Cloud? 

While some of the guidance in this blueprint is applicable to Google Distributed Cloud, the focus is on Google Kubernetes Engine (GKE) running on Google Cloud. 

###  Do you have a list of PCI requirements that this blueprint can help satisfy? 

This blueprint addresses a range of PCI DSS compliance requirements. You can find a full list of those requirements in the [PCI DSS Requirements](https://github.com/GoogleCloudPlatform/pci-gke-blueprint/blob/master/docs/assets/pci-mapping.pdf) document (PDF) on GitHub. This list addresses only the PCI compliance requirements that are supported by the Google Cloud infrastructure as part of the shared responsibility between you and Google. Note that the implementation of any PCI compliance controls is the sole responsibility of the customer and you should conduct your own evaluation of your organization's PCI compliance. For more information about the shared responsibility model, see [Exploring container security: the shared responsibility model in GKE](https://cloud.google.com/blog/products/containers-kubernetes/exploring-container-security-the-shared-responsibility-model-in-gke-container-security-shared-responsibility-model-gke) on the Google Cloud blog. 

###  What services are supported by the guidance in this blueprint? 

For a full list of supported services, see the top of the [README](https://github.com/GoogleCloudPlatform/pci-gke-blueprint) file in the PCI on GKE repository on GitHub. 

###  Do you accept contributions to the PCI on GKE repository on GitHub? 

Yes. You can submit a [ pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests) or fork the repository. 

## Resources

  * [PCI DSS compliance on Google Cloud](https://docs.cloud.google.com/solutions/pci-dss-and-gke-guide). This guide helps you address concerns unique to Google Kubernetes Engine (GKE) applications when you are implementing customer responsibilities for PCI DSS requirements.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-12 UTC."],[],[]] 
