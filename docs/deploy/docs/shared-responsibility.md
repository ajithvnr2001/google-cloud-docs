---
url: https://docs.cloud.google.com/deploy/docs/shared-responsibility/
title: Statement of shared responsibility for security \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:04.772386+00:00
---

# Statement of shared responsibility for security  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Statement of shared responsibility for security Stay organized with collections  Save and categorize content based on your preferences. 

Running business-critical workloads on Cloud Deploy requires that multiple parties assume different responsibilities. The shared responsibility model described in this document clarifies that Google Cloud is accountable for the security of the Cloud Deploy service itself and its underlying infrastructure, while you, the customer, are responsible for security in how Cloud Deploy is used, including your specific delivery pipelines, configurations, data, and the applications you deploy using Cloud Deploy.

While not an exhaustive list, this page lists the respective responsibilities of Google Cloud and the customer.

## Google Cloud Responsibilities

  * Protecting the underlying infrastructure, including hardware, firmware, kernel, operating system, storage, and network.

This includes the following:

    * Protecting the physical security of data centers, default encryption of data at rest and in transit, and secure network components.
    * Providing network protection using VPC Service Controls.
    * Following secure software development practices.
    * Managing and securing the Cloud Deploy service control plane (API, backend, schedulers, etc.), including patching and hardening.
    * Providing ephemeral, isolated [execution environments](https://docs.cloud.google.com/deploy/docs/execution-environment) for running Cloud Deploy operations.
  * Providing Google Cloud integrations for [Identity and Access Management](https://docs.cloud.google.com/iam) (IAM), [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), and others.

  * Restricting Google Cloud administrative access to customer resources for contractual support purposes, with [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs) and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview), and logging all such access.

  * Ensuring that versions of [embedded tools](https://docs.cloud.google.com/deploy/docs/select-tool-version) are compatible on the Cloud Deploy image.




## The Customer's Responsibilities

  * Securing your application source code, configuration files, and all container images you deploy.

This includes evaluating image suitability for your security standards, leveraging the latest supported image versions, and following best practices for open source components and overall build configuration.

  * Ensuring any 3rd-party integration tokens are appropriately safeguarded.

  * Configuring IAM for all users, groups, and service accounts interacting with Cloud Deploy, in accordance with the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely).

We recommend you use dedicated, user-specified service accounts to run deploy pipelines and other operations, instead of default service accounts.

  * Enabling and acting on vulnerability scanning for build artifacts (for example, using Artifact Analysis), generating build provenance data, and implementing deployment policies (for example, using Binary Authorization) to ensure only authorized and verified images are deployed.

  * Ensuring that versions of [embedded tools](https://docs.cloud.google.com/deploy/docs/select-tool-version) are compatible on the Cloud Deploy image, when [replacing tool versions](https://docs.cloud.google.com/deploy/docs/select-tool-version#how_select).

  * Providing Google with environmental details when requested for troubleshooting purposes.




## What's next

  * [Read more](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) about the Google Cloud shared responsibility model.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
