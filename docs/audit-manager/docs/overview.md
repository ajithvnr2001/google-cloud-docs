---
url: https://docs.cloud.google.com/audit-manager/docs/overview/
title: Audit Manager overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:40.169903+00:00
---

# Audit Manager overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Audit Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

Audit Manager is a compliance audit solution that helps you to simplify your compliance audit process on Google Cloud. Audit Manager lets you run audits against built-in frameworks and custom frameworks that you define using Compliance Manager or Assured Workloads frameworks ([Preview](https://cloud.google.com/products/#product-launch-stages)).

Audit Manager has the following capabilities:

  * A [shared responsibilities](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) matrix that shows separation of duties and recommendations to manage your responsibilities.
  * [Compliance documents for Google Cloud](https://docs.cloud.google.com/audit-manager/docs/download_compliance_documents).
  * Automated compliance assessments to evaluate compliance controls on workloads to understand their state of compliance.
  * Evidence collection for compliance audits.
  * Gap identification to help remediate the generated violations.
  * Ability to schedule audits to run at regular intervals.



Audit Manager can provide assessments for any Google Cloud organization, folder, or project.

## Supported frameworks

Audit Manager can evaluate your resources against the cloud controls and controls for the following built-in frameworks:

  * [Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#security-essentials) [1]
  * [SOC2 2017](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#soc2-2017)



If you purchase [Security Command Center Premium or Enterprise](https://docs.cloud.google.com/security-command-center/docs/service-tiers) subscriptions or enable Assured Workloads, the following:

  * Any custom framework that you create using [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#create-framework) or [Assured Workloads frameworks (](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks#create-framework)[Preview](https://cloud.google.com/products/#product-launch-stages)).

  * The following built-in frameworks:

    * [Google Recommended AI Essentials - Gemini Enterprise Agent Platform](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#aipp) [1]
    * [CIS GCP Foundations Benchmark v3.0](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#cis-gcp-v3-0)
    * [CIS GKE 1.7](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#cis-gke-1-7) [1]
    * [CIS Critical Security Controls v8](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#cis-v8)
    * [CSA Cloud Controls Matrix v4.0.11](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#csa-ccm-4-0-11)
    * [Compute Engine Security Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#gce-security-essentials) [1]
    * [GKE Essentials](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#gke-essentials) [1]
    * [ISO 27001:2022](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#iso-27001-2022)
    * [Qatar National Information Assurance Standard v2.1](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#nias-v2-1)
    * [NIST 800-53 Revision 5](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#nist-800-53-revision5)
    * [NIST Cybersecurity Framework 1.1](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#nist-csf-v1-1)
    * [PCI DSS v4.0.1](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#pci-dss-v4-0-1)
  * The following built-in Assured Workloads frameworks:

    * [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/framework-reference#eu-data-boundary)
    * [Switzerland Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/framework-reference#switzerland-data-boundary)
    * [UK Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/framework-reference#uk-data-boundary)
    * [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/framework-reference#us-data-boundary)



1 If you run an audit at the organization level, these frameworks are available in [General Availability](https://docs.cloud.google.com/products#product-launch-stages). All other frameworks are available in Preview.

### Migrating from older frameworks

If you ran an audit before June 30, 2026, you used different frameworks. These frameworks are no longer available for running audits. The following table maps the older frameworks to the frameworks that you can deploy using Compliance Manager or Assured Workloads frameworks ([Preview](https://cloud.google.com/products/#product-launch-stages)).

Older framework | Equivalent Audit Manager framework | Equivalent Compliance Manager framework | ([Preview](https://cloud.google.com/products/#product-launch-stages)) Equivalent Assured Workloads frameworks  
---|---|---|---  
NIST 800-53 Revision 4 | — | NIST 800-53 Revision 5 | NIST 800-53 Revision 5  
Google-recommended AI controls | — | —[2] | —[2]  
SOC2 2017 | SOC2 2017 | SOC2 2017 | SOC2 2017  
CIS Controls v8 | — | CIS Critical Security Controls v8 | CIS Critical Security Controls v8  
PCI DSS 4.0 | — | PCI DSS v4.0.1 | PCI DSS v4.0.1  
Cloud Controls Matrix 4.0 | — | CSA Cloud Controls Matrix v4.0.11 | CSA Cloud Controls Matrix v4.0.11  
NIST CSF v1 | — | NIST Cybersecurity Framework 1.1 | NIST Cybersecurity Framework 1.1  
CIS Google Cloud Foundation Benchmark 2.0 | — | CIS GCP Foundations Benchmark v3.0 | CIS GCP Foundations Benchmark v3.0  
ISO 27001 2022 | — | ISO 27001:2022 | ISO 27001:2022  
  
If you ran audits using the older frameworks, you can continue to view the audit reports on the **View assessments** page and in the Cloud Storage buckets where you stored the reports.

2 Both Compliance Manager and Assured Workloads frameworks ([Preview](https://cloud.google.com/products/#product-launch-stages)) include the [Google Recommended AI Essentials - Gemini Enterprise Agent Platform](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-frameworks#aipp) built-in framework. You can use this framework instead of the older Google-recommended AI controls framework, though it uses different controls to evaluate your environment.

### Custom frameworks

Before June 30, 2026, Audit Manager included a preview feature that let you create custom frameworks. If you created a custom framework using that preview feature, you can continue to run audits against the custom framework and view the reports that you created. However, you can't view or edit your custom framework.

If none of the built-in frameworks in Audit Manager apply to your environment, you can use the following options:

  * [Create a custom framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework#create-framework) in Compliance Manager. Compliance Manager includes a [library of built-in cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls), and you can [create custom cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control), if required. After you create this framework, you can use Audit Manager or Compliance Manager to run audits in your environment.

  * [Create a custom framework](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks#create-framework) in Assured Workloads frameworks ([Preview](https://cloud.google.com/products/#product-launch-stages)). The [built-in cloud controls for Assured Workloads frameworks](https://docs.cloud.google.com/assured-workloads/docs/cloud-control-reference) include the Compliance Manager library of cloud controls and a library of preventive cloud controls that are specific to regulatory workloads. You can also use Assured Workloads frameworks to [create custom cloud controls](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls#create-custom-cloud-control), if required. If you create a framework that includes preventive controls, you can only use Audit Manager to run audits in your environment.




## Controls and cloud controls

Audit Manager includes controls and cloud controls within its frameworks. Consider the following:

  * _Controls_ are general objectives that let you assess asset protection, risk mitigation, and business regulatory objectives. Controls can be composed of technical and non-technical cloud controls.

  * _Cloud controls_ are software-defined controls that check for particular configurations in your Google Cloud environment. Most cloud controls are technical. For example, a control is a regulatory requirement to audit your environment, and a cloud control is the specific mechanism to ensure that Cloud Audit Logs is enabled for various APIs.

  * _Frameworks_ are collections of controls and cloud controls that help you meet a particular regulatory standard. For example, Audit Manager includes a framework for ISO 27001 2022. Cloud controls and controls that are technical include one or more rules that Audit Manager can check during an audit and collect evidence for.




## How controls and cloud controls are audited

How Audit Manager audits a control or cloud control depends on whether Audit Manager can technically evaluate the control or cloud control. Consider the following:

  * Some controls or cloud controls require _manual reviews_ because there are no API calls that Audit Manager can make to validate them. For example, a control might require you to review access systems that aren't in Google Cloud. If a control or cloud control requires a manual review, Audit Manager creates an _observation_ that tells you that you must complete the review yourself. Technical evidence might be generated. The state of the control or cloud control is _Optional: Manual Review Needed_.

  * Some controls or cloud controls apply directly to a particular value in Google Cloud. For example, a cloud control can require that you turn on CMEK for Cloud Storage buckets. In this scenario, Audit Manager can make an API call to check a particular setting. The value that's returned is the _evidence_. Audit Manager can then evaluate whether the evidence meets or fails the expected rules. Audit Manager creates an _observation_ that includes the evidence and the evaluation. The state of a control or cloud control can be any of the following:

    * If Audit Manager evaluates the evidence as meeting the rule, the state of the control or cloud control is _Compliance_.

    * If Audit Manager evaluates the evidence as failing the rule, the state of the control or cloud control is _Violation_. For controls or cloud controls that include multiple rules, if any rule fails, the state is _failed_.

    * If Audit Manager encounters any type of error during this process (for example, an API call timed out), the state of the control or cloud control is _Skipped_.




## Audit Manager workflow

The high-level workflow of Audit Manager involves setting up Audit Manager access and managing audits.

  1. To set up Audit Manager access, you must be an Audit Manager Admin (`roles/auditmanager.admin`) and enroll resources for audit.
  2. To manage audits, you can be an administrator or an auditor and do the following: 
     1. Schedule audits and run on-demand audits.
     2. Get audit status.
     3. View detailed Audit Manager reports.



## What's next

  * [Enroll resources for audit](https://docs.cloud.google.com/audit-manager/docs/enroll-resource).
  * [Schedule and run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
