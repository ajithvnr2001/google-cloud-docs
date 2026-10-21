---
url: https://docs.cloud.google.com/workstations/docs/shared-responsibility/
title: Shared security responsibilities \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:07.172370+00:00
---

# Shared security responsibilities  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Shared security responsibilities Stay organized with collections  Save and categorize content based on your preferences. 

Security for Cloud Workstations is a shared responsibility between Google and you, the customer. Google manages the security of the infrastructure for Cloud Workstations, and provides tools and controls to help you secure your workloads in the cloud.

This document details the key security responsibilities for Google and for you within this shared model.

## Google's responsibilities

Our responsibilities include:

  * **Protect the infrastructure.** Google is responsible for providing secure infrastructure for its services, including physical security of data centers, network security, and application security. This includes compliance with applicable industry standards and regulations.

  * **Harden and patch default images.**

    * Google hardens and maintains the operating system of container images used by the Cloud Workstations preconfigured images. This includes applying security patches and updates from upstream open source maintainers.
    * Google automatically hardens, patches, and updates the operating system of the virtual machines that run underneath Cloud Workstations containers. These virtual machines run [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/concepts/security).
  * **Maintain platform security.** Google is responsible for maintaining the security of the Cloud Workstations platform. This responsibility includes managing platform-level access controls, monitoring for security incidents, and responding to security events. Google also provides tools and controls for you to manage your specific security settings and configurations.

  * **Maintain compliance.** Google maintains compliance with relevant data protection laws and regulations.

  * **Provide security integrations.**

    * Google provides integrations for Identity and Access Management (IAM), Cloud Audit Logs, Google Cloud Observability, Cloud Key Management Service, Security Command Center, and others.
    * Restrict and log Google administrative access to customer clusters for contractual support purposes with [Access Transparency and Access Approval](https://cloud.google.com/security/products/access-transparency).



## Your responsibilities

Your responsibilities as a customer include:

  * **Comply with applicable laws and regulations for your use cases.** You are responsible for understanding the security and regulatory requirements specific to your business and ensuring your use of Cloud Workstations meets them.

  * **Select appropriate workstation images.** Cloud Workstations offers preconfigured images for various use cases. You are responsible for verifying that all software in your chosen image, beyond the base OS and editor, meets your security and regulatory requirements.

For more information, see [Customize container images](https://docs.cloud.google.com/workstations/docs/customize-container-images).

  * **Use the latest versions of Cloud Workstations base images.** Cloud Workstations provides [prebuilt container images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) to simplify the use of its services. Google creates new versions of the base images to address identified security vulnerabilities. You are responsible for ensuring your workstation configurations use the latest image version, either by updating your configuration to pull the latest version automatically or by manually upgrading.

For more information, see [Automate container image rebuilds](https://docs.cloud.google.com/workstations/docs/tutorial-automate-container-image-rebuild).

  * **Manage access controls.** You are responsible for managing access controls to your own data, services, and workstations instances. This includes managing user access, authentication, and authorization controls, and securing your own applications and data.

You are also responsible for managing access controls to the resources stored in your projects that are used to back workstation instances, such as Compute Engine instances and Persistent Disks.

For more information about user-managed resources, see the [Cloud Workstations architecture](https://docs.cloud.google.com/workstations/docs/architecture).

  * **Secure applications and source code.** You are responsible for securing your own applications and source code accessed on the Cloud Workstations platform, including implementing secure coding practices and regularly testing for vulnerabilities.

For more information, see [Set up security best practices](https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices), [Encrypt workstation resources using CMEK](https://docs.cloud.google.com/workstations/docs/encrypt-workstation-resources-using-cmek), and [Configure VPC Service Controls and private clusters](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters).

  * **Monitor for security incidents.** You are responsible for monitoring your own applications for security incidents, and reporting any incidents to Google as necessary.

For more information, see [Cloud Workstations resource monitoring](https://docs.cloud.google.com/workstations/docs/resource-monitoring) and [Cloud Workstations audit logging](https://docs.cloud.google.com/workstations/docs/audit-logging).




## What's next

  * Learn more about [shared responsibilities and shared fate on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate).
  * Learn about how to [protect your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
