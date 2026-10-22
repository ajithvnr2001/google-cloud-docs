---
url: https://docs.cloud.google.com/dataflow/docs/resources/shared-responsibility/
title: Dataflow shared responsibility \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:44.948251+00:00
---

# Dataflow shared responsibility  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/resources/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dataflow/docs/resources)



Send feedback 

#  Dataflow shared responsibility Stay organized with collections  Save and categorize content based on your preferences. 

Security is a shared responsibility. Dataflow secures the scalable infrastructure that you use to run your Dataflow pipelines and provides you tools and security controls to protect your data, code, and models. While not an exhaustive list, this document lists the responsibilities for both Google and the customer.

## Google's responsibilities

  * **Protect the infrastructure** : Google is responsible for providing secure infrastructure for its services, including physical security of data centers, network security, and application security.

  * **Secure the platform** : Google is responsible for securing its platform, including managing access controls, monitoring for security incidents, and responding to security events. Google also provides customers with tools to manage their own security settings and configurations.

  * **Maintain compliance** : Google maintains compliance with relevant data protection laws and regulations. Learn more about [Google Cloud compliance](https://cloud.google.com/compliance).

  * **Harden and patch images** : Google hardens and patches the operating system of [base images](https://docs.cloud.google.com/software-supply-chain-security/docs/base-images) used by the Dataflow-owned images. Google promptly makes any patches to these images available. [Security bulletins](https://docs.cloud.google.com/dataflow/docs/security-bulletins) are provided for known vulnerabilities.

For open source dependencies like Apache Beam, Dataflow provides base images and updates the Apache Beam SDK on a best-effort basis as a convenience. Because Dataflow relies on the open source community for these fixes, Google doesn't have full control over fix prioritization or timing. Fixes for Common Vulnerabilities and Exposures (CVEs) are typically included in upcoming Apache Beam releases.




## Customer's responsibilities

  * **Use and update your environment to the latest versions of Dataflow containers, VM images, and SDKs** : Dataflow provides prebuilt containers and VM images to simplify the use of its services. Google creates new versions of these images when vulnerabilities are identified.

Your responsibilities include:

    * **Monitoring for[security bulletins](https://docs.cloud.google.com/dataflow/docs/security-bulletins)** and updating your environment promptly when new versions are available.
    * **Restarting long-running streaming jobs** to pick up the latest VM image patches or container updates. This only applies to streaming jobs, as batch jobs automatically use the latest image version each time they start.

To apply updated VM images or container images to streaming jobs, launch a replacement job with the [`--update` flag](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline) or drain and restart the pipeline. Streaming Engine in-flight option updates (`gcloud dataflow jobs update-options`) only adjust autoscaling parameters and don't recreate worker VMs or pull updated container images.

Dataflow worker VMs run a read-only, stateless Container-Optimized OS image without a package manager (such as `apt` or `yum`). Consequently, you can't modify worker VMs in place, run OS Patch Manager on worker VMs, or install host endpoint agents directly on the host OS.

For more information, see [Upgrade and patch Dataflow VMs](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#upgrade-patch). To manage security issues responsively, we recommend that you use [custom container](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) images. If you have strict security Service Level Agreement (SLA) requirements, such as those for FedRAMP compliance, using custom containers lets you manage your own Apache Beam versions and patch cycles, rather than relying on the Apache Beam open source release schedule.

    * **Regularly updating your Apache Beam SDK versions** to ensure you have the latest security fixes and features.

    * **Scanning and patching custom images** to mitigate vulnerabilities if you are using a [custom container](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) or a [custom template](https://docs.cloud.google.com/dataflow/docs/guides/templates/creating-templates).

    * **Using Distroless base images** when possible if you are using a [Flex Template base image](https://docs.cloud.google.com/dataflow/docs/reference/flex-templates-base-images) to ensure security and reduce vulnerability risks.

  * **Manage access controls** : You are responsible for managing access controls to your own data and services. This includes managing user access, authentication, and authorization controls, and securing your own applications and data. Learn more about [Dataflow security and permissions](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions).

  * **Secure applications** : You are responsible for securing your own applications running on Dataflow, including implementing secure coding practices and regularly testing for vulnerabilities.

Learn more about [Customer-managed encryption keys](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys), [networks and VPC Service Controls](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks), and [permissions best practices](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#best-practices).

  * **Monitor for security incidents** : You are responsible for monitoring your own applications for security incidents, and reporting any incidents to Google as necessary.

    * Subscribe to the [Dataflow security bulletins](https://docs.cloud.google.com/dataflow/docs/security-bulletins).
    * Follow the [Dataflow release notes](https://docs.cloud.google.com/dataflow/docs/release-notes).
    * Follow the [Apache Beam release notes](https://docs.cloud.google.com/dataflow/docs/resources/release-notes-apache-beam).
    * Learn more about [Monitoring](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring) and [Audit logging](https://docs.cloud.google.com/dataflow/docs/audit-logging).
**Note:** When using the Monitoring agent, the `--experiments=enable_stackdriver_agent_metrics` option uses a deprecated container image that isn't maintained and might have unpatched vulnerabilities. We recommend that you don't use this option.



## What's next

  * Learn more about [shared responsibilities on Google Cloud](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate).
  * Learn about how to [protect your software supply chain](https://docs.cloud.google.com/software-supply-chain-security/docs/practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
