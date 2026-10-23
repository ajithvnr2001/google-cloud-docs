---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-overview/
title: Security posture overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:16.558015+00:00
---

# Security posture overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security posture overview Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

A security posture lets you define and manage the security status of your cloud assets, including your cloud network and cloud services. You can use a security posture to evaluate your current cloud security against defined benchmarks, which helps you maintain the level of security that your organization requires. A security posture helps you detect and mitigate any drift from your defined benchmark. By defining and maintaining a security posture that matches your business's security needs, you can reduce cybersecurity risks to your organization and help prevent attacks from occurring.

In Google Cloud, you can use the security posture service in Security Command Center to define and deploy a security posture, monitor the security status of your Google Cloud resources, and address any drift (or unauthorized change) from your defined posture.

## Benefits and applications

The security posture service is a built-in service for the Security Command Center that lets you define, assess, and monitor the overall status of your security in Google Cloud. The security posture service is only available to you if you purchase a subscription of the Security Command Center Premium tier or the Enterprise tier and activate Security Command Center at the organization level.

You can use the security posture service to achieve the following goals:

  * Ensure that your workloads conform to security standards, compliance regulations, and your organization's custom security requirements.

  * Apply your security controls to Google Cloud projects, folders, or organizations before you deploy any workloads.

  * Continuously monitor for and resolve any drift from your defined security controls.




The security posture service is automatically enabled when you activate Security Command Center at the organization level.

## Service components

The security posture service includes the following components:

### Posture

One or more policy sets that enforce the preventative and detective controls that your organization requires to meet its security standard. You can deploy postures at the organization level, folder level, or project level. For a list of posture templates, see Predefined posture templates.

### Policy sets

A set of security requirements and associated controls in Google Cloud. Typically, a policy set consists of all the policies that let you meet the requirements of a particular security standard or compliance regulation.

### Policy

A particular constraint or restriction that controls or monitors the behavior of resources in Google Cloud. Policies can be preventative (for example, [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints)) or detective (for example, Security Health Analytics detectors). Supported policies are the following:

  * Organization Policy constraints, including [custom constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints)

  * Security Health Analytics detectors, including [custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview)




### Posture deployment

After you create a posture, you deploy it so that you can apply the posture to the organization, folders, or projects that you want to manage using the posture.

The following diagram shows the components of an example security posture.

![Components in the security posture service.](https://docs.cloud.google.com/static/security-command-center/images/security-posture-components.svg)

## Predefined posture templates

The security posture service includes predefined posture templates that adhere to a compliance standard or to a Google-recommended standard like the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/security-foundations) recommendations. You can use these templates to create security postures that apply to your business. The following table describes the posture templates.

Posture template | Template name | Description  
---|---|---  
[ Secure by default, essentials](https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-secure-default-template) | `secure_by_default_essential` |  This template implements the policies that help prevent common misconfigurations and common security issues caused by default settings. You can deploy this template without making any changes to it.   
[ Secure by default, extended](https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-secure-default-template) | `secure_by_default_extended` |  This template implements the policies that help prevent common misconfigurations and common security issues caused by default settings. Before you deploy this template, you must customize it to match your environment.   
[ Secure AI recommendations, essentials](https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-secure-ai-template) | `secure_ai_essential` |  This template implements policies that help you secure Gemini and Gemini Enterprise Agent Platform workloads. You can deploy this template without making any changes to it.   
[ Secure AI recommendations, extended](https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-secure-ai-template) | `secure_ai_extended` |  This template implements policies that help you secure Gemini and Gemini Enterprise Agent Platform workloads. Before you deploy this template, you must customize it to match your environment.   
[ BigQuery recommendations, essentials](https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-bigquery-template) | `big_query_essential` |  This template implements policies that help you secure BigQuery. You can deploy this template without making any changes to it.   
[ Cloud Storage recommendations, essentials](https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-storage-template) | `cloud_storage_essential` |  This template implements policies that help you secure Cloud Storage. You can deploy this template without making any changes to it.   
[ Cloud Storage recommendations, extended](https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-storage-template) | `cloud_storage_extended` |  This template implements policies that help you secure Cloud Storage. Before you deploy this template, you must customize it to match your environment.   
[ VPC recommendations, essentials](https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-vpc-template) | `vpc_networking_essential` |  This template implements policies that help you secure Virtual Private Cloud (VPC). You can deploy this template without making any changes to it.   
[ VPC recommendations, extended](https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-vpc-template) | `vpc_networking_extended` |  This template implements policies that help you secure VPC. Before you deploy this template, you must customize it to match your environment.   
[ Center for Internet Security (CIS) Google Cloud Computing Platform Benchmark v2.0.0 recommendations](https://docs.cloud.google.com/security-command-center/docs/security-posture-cis-20-template) | `cis_2_0` |  This template implements policies that help you detect when your Google Cloud environment doesn't align with the CIS Google Cloud Computing Platform Benchmark v2.0.0. You can deploy this template without making any changes to it.   
[ NIST SP 800-53 standard recommendations](https://docs.cloud.google.com/security-command-center/docs/security-posture-nist-800-53-template) | `nist_800_53` |  This template implements policies that help you detect when your Google Cloud environment doesn't align with the National Institute of Standards and Technology (NIST) SP 800-53 standard. You can deploy this template without making any changes to it.  
[ ISO 27001 standard recommendations](https://docs.cloud.google.com/security-command-center/docs/security-posture-iso-27001-template) | `iso_27001` |  This template implements policies that help you detect when your Google Cloud environment doesn't align with the International Organization for Standards (ISO) 27001 standard. You can deploy this template without making any changes to it.   
[ PCI DSS standard recommendations](https://docs.cloud.google.com/security-command-center/docs/security-posture-pci-dss-template) | `pci_dss_v_3_2_1` |  This template implements policies that help you detect when your Google Cloud environment doesn't align with the Payment Card Industry Data Security Standard (PCI DSS) version 3.2.1 and version 1.0. You can deploy this template without making any changes to it.   
  
## Posture deployment and drift monitoring

To enforce a posture with all its policies on a Google Cloud resource, you deploy the posture. You can specify which level of the resource hierarchy (organization, folder, or project) that the posture applies to. You can only deploy one posture to each organization, folder, or project.

Postures are inherited by child folders and projects. Therefore, if you deploy postures at the organization level and at the project level, all the policies within both postures apply to the resources in the project. If there are any differences in policy definitions (for example, a policy is set to Allow at the organization level and to Deny at the project level), the lower-level posture is used by the resources in that project.

As a best practice, we recommend that you deploy a posture at the organization level that includes policies that can apply to your entire business. You can then apply more stringent policies to folders or projects that require them. For example, if you use the enterprise foundations blueprint to set up your infrastructure, you create certain projects (for example, `prj-c-kms`) that are specifically created to contain the encryption keys for all the projects in a folder. You can use a security posture to set the [`constraints/gcp.restrictCmekCryptoKeyProjects`](https://docs.cloud.google.com/kms/docs/cmek-org-policy#example-require-cmek-project) organization policy constraint on the `common` folder and environment folders (`development`, `nonproduction`, and `production`) so that all projects only use keys from the key projects.

After you deploy your posture, you can monitor your environment for any drift from your defined posture. Security Command Center reports instances of drift as findings that you can review, filter, and resolve. In addition, you can export these findings in the same way that you export any other findings from Security Command Center. For more information, see [Exporting Security Command Center data](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data).

## Integration with Gemini Enterprise Agent Platform and Gemini

You can use security postures to help you maintain the security for your AI workloads. The security posture service includes the following:

  * Predefined posture templates that are specific to AI workloads.

  * A [pane on the **Overview** page](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture#monitor-posture) that lets you monitor for vulnerabilities that were found by the Security Health Analytics custom modules that apply to AI, and lets you view any drift from the Gemini Enterprise Agent Platform organization policies that are defined in a posture.




## AWS integration

If you connect Security Command Center Enterprise to AWS for [configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws), the Security Health Analytics service includes built-in detectors that can monitor your AWS environment and create [findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#aws-findings).

When you create or modify a posture file, you can include Security Health Analytics detectors that are specific to AWS. You must deploy this posture file at the organization level.

## Service limits

The security posture service includes the following limits:

  * A maximum of 100 postures in an organization.
  * A maximum of 400 policies in a posture.
  * A maximum of 1000 posture deployments in an organization.



## What's next

  * [Create and deploy a posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
