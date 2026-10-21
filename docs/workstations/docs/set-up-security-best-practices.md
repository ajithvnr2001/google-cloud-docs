---
url: https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices/
title: Set up security best practices \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:23.210889+00:00
---

# Set up security best practices  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/set-up-security-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Set up security best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of security best practices recommended to increase the security and data protection posture around your Cloud Workstations. This list is _not_ a comprehensive checklist ensuring security guarantees, or a replacement to your existing security postures.

The goal is to provide you with a guide to the security best practices made possible by Cloud Workstations. Add these recommendations to your portfolio of security solutions when applicable, as part of the efforts to build a layered security approach. A layered security approach is one of the core [security principles](https://docs.cloud.google.com/architecture/framework/security#core_principles) for running secure and compliant services on Google Cloud.

## Background

The Cloud Workstations service provides [predefined base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images) for use with the service. The service rebuilds and republishes these images weekly to help ensure that the bundled software includes the latest security patches. In addition, the service uses a default _running timeout_ value on your [workstation configuration](https://docs.cloud.google.com/workstations/docs/customize-development-environment#resource:-workstationconfig) to help make sure that workstations are automatically updated and that unpatched images don't remain live.

However, Google Cloud does not own all the packages bundled into these images. Package managers might prioritize updates differently depending on how a bug or common vulnerabilities and exposures (CVE) impacts their product. If a product uses only a portion of a library, it might not be impacted by discoveries in other portions of the library. Because of this, although CVE findings from vulnerability scans of our images exist, Cloud Workstations is still able to provide a secure product.

Cloud Workstations can do this because it provides an authentication and authorization system that helps ensure that only the designated developer can access their workstation. As with any development environment, developers should apply best practices when using their workstation. To be as secure as possible, run only trusted code, operate only on trusted input, and access only trusted domains. Additionally, you are discouraged from using workstations to host production servers, or sharing a single workstation with multiple developers.

If you want to have more control over the security of your organization's workstation images, you can also create your own [customized container images](https://docs.cloud.google.com/workstations/docs/customize-container-images#use_your_own_container_image).

## Use Secure Web Proxy to control internet access for enhanced data loss prevention (DLP)

To block all access to the public internet–for example, for data loss prevention (DLP)–[disable public IP addresses](https://docs.cloud.google.com/workstations/docs/customize-development-environment#gceinstance) on your workstation configurations. If you disable public IP addresses, you must set up [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) or [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) on your network. If you use Private Google Access and you use `private.googleapis.com` or `restricted.googleapis.com` for Artifact Registry, make sure that you set up DNS records for [domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) `*.pkg.dev`. If, however, your developers require access to certain external websites from their workstations, use [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) to provide auditable access to those sites, which includes DLP protections. Secure Web Proxy helps organizations enforce granular internet access, controlling outbound traffic based on source, identity, destination, and request type. You can define these policies within a Google Cloud Identity and Access Management (IAM) context, using service accounts and secure tags to restrict traffic, for example, to a specific destination. Secure Web Proxy also offers a scalable TLS inspection service that lets you enforce policies on intercepted encrypted TLS traffic. Secure Web Proxy integrates with Cloud Logging to record metrics and transaction logs. To identify the source workstation for a given log entry, find the VM's IP address in the log entry, then use [workstation platform logs](https://docs.cloud.google.com/workstations/docs/platform-logging) to correlate that IP address with the corresponding workstation. You can use a [custom image](https://docs.cloud.google.com/workstations/docs/customize-container-images) to set the `https_proxy` and `http_proxy` to the Secure Web Proxy in your workstations. Restrict direct SSH access Make sure that you restrict direct SSH access to VMs in the project hosting your Cloud Workstations, so that access is only possible through the Cloud Workstations gateway, where [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview)) policies are enforced and [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) can be enabled. To disable direct SSH access to VM, run the following Google Cloud CLI command:
    
    
        gcloud workstations configs update CONFIG \
            --cluster=CLUSTER \
            --region=REGION \
            --project=PROJECT \
            --disable-ssh-to-vm
    

Limit access to sensitive resources Set up a [VPC Service Controls service perimeter](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters) to limit access to sensitive resources from your workstations, preventing source code and data exfiltration. Follow the principle of least privilege Follow the principle of least privilege for permissions and resource allocation. IAM permissions Use the [default Identity and Access Management configuration](https://docs.cloud.google.com/workstations/docs/access-control), limiting workstation access to a single developer. This helps ensure that each developer is using a unique workstation instance with a distinct underlying VM, increasing the environment isolation. Cloud Workstations code editors and applications run inside a container running in privileged mode and with root access, for increased developer flexibility. This provides a unique workstation per developer and helps ensure that even if a user escapes from this container, they'd still be inside their VM, unable to gain access to any additional external resources. Set up IAM permissions limiting non-admin access to modify [workstation configurations](https://docs.cloud.google.com/workstations/docs/access-control#workstations-admin) and container images on [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/access-control). Additionally, Google recommends that you set up IAM permissions limiting non-admin access to any of the underlying Compute Engine resources in the project hosting your Cloud Workstations. For more information, see [using IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely). Cloud KMS permissions To better support the principle of least privilege, we recommend that you keep Cloud KMS resources and Cloud Workstations resources in separate Google Cloud projects. Create your Cloud KMS key project without an `owner` at the project level, and designate an _Organization Admin_ [granted at the organization-level](https://docs.cloud.google.com/resource-manager/docs/quickstart#grant_iam_roles_at_the_organization_level). Unlike an `owner`, an _Organization Admin_ can't manage or use keys directly. They are restricted to setting IAM policies, which restrict who can manage and use keys. This is also referred to as _separation of duties,_ which is the concept of making sure that one individual does not have all necessary permissions to be able to complete a malicious action. For more information, see [separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties). Enforce automatic image updates and patches Make sure that your workstations are using the latest version of the Cloud Workstations [base images](https://docs.cloud.google.com/workstations/docs/preconfigured-base-images), which contains the latest security patches and fixes. The [running timeout](https://docs.cloud.google.com/workstations/docs/customize-development-environment#gceinstance) value on your workstation configuration helps ensure that workstations created with this configuration automatically update on the next session, to match the latest version of the container image defined in the workstation configuration.

  * If your organization uses one of the Cloud Workstations base images, the workstation automatically picks up any updates to the workstation configuration the next time the workstation is shutdown and restarted. Setting [`runningTimeout`](https://docs.cloud.google.com/workstations/docs/customize-development-environment#gceinstance), or using the default, helps ensure that these workstations are shutdown.
  * If your organization uses a custom image, be sure that you rebuild the image regularly.

Maintain custom images You're responsible for maintaining and updating custom packages and dependencies added on custom images. If you're creating custom images, we recommend the following:

  * Run a container scanning tool such as [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) to inspect any additional dependencies you added.
  * [Schedule builds](https://docs.cloud.google.com/build/docs/schedule-builds) to rebuild images weekly, or learn how to [automate container image rebuilds](https://docs.cloud.google.com/workstations/docs/tutorial-automate-container-image-rebuild).

Set up VPC Flow Logs When you create a workstation cluster, Cloud Workstations associates the cluster with a particular subnet and all workstations are placed in that subnet. To enable VPC Flow Logs, make sure that you turn on logging for that subnet. For more information, see [Enable VPC Flow Logs for an existing subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-logging-existing). Enable VM Threat detection in the Security Command Center The [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) is a cloud-based risk management solution that helps security professionals to prevent, detect, and respond to security issues. Because workstations run on a dedicated, per workstation VM, [Virtual Machine Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-vm-threat-detection-overview) can be used to detect potentially malicious applications, such as cryptocurrency mining software, kernel-mode rootkits, and malware running in the workstation. When evaluating the [findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) for VMs, you can find the workstation assigned to the VM by inspecting the [workstation labels](https://docs.cloud.google.com/workstations/docs/platform-logging) on the VM, or by using [workstations platform logs](https://docs.cloud.google.com/workstations/docs/platform-logging) to look up historical assignments.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
