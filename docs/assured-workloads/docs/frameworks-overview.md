---
url: https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview/
title: Overview of Assured Workloads frameworks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:28.168414+00:00
---

# Overview of Assured Workloads frameworks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/frameworks-overview/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of Assured Workloads frameworks

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Frameworks for Assured Workloads provide new and equivalent cloud controls for data residency, access, and personnel, similar to those in [Assured Workloads folders](https://docs.cloud.google.com/assured-workloads/docs/overview#folders).

You can use Assured Workloads frameworks to meet the security and regulatory requirements of your folders and projects in the following ways:

  * Choose a predefined [data boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages) to enforce and monitor your Google Cloud environment's compliance
  * Define your own compliant and secure configuration for your Google Cloud environment
  * View dashboards that show your environment's alignment with your compliance and security requirements
  * Audit your cloud environments, including collecting evidence and generating reports



Assured Workloads frameworks use software-defined controls that let you assess support for multiple compliance programs and security requirements within a Google Cloud folder or project.

**Note:** Deploying frameworks in Assured Workloads is a Preview feature, and you must be added to an allowlist. Request access to the allowlist by filling out [the sign-up form](https://forms.gle/JsX7kziFjEGsDhcQ8).

## Assured Workloads frameworks components

The following table describes the components of Assured Workloads frameworks:

Rule | A technical item within a cloud control that lets you meet a compliance, security, or privacy requirement. Rules can be organization policies, IAM policies, cloud settings, and detection logic based on [Common Expression Language (CEL)](https://docs.cloud.google.com/assured-workloads/docs/write-rules-cloud-controls).   
---|---  
Cloud control | A set of rules and associated metadata that you can use to define the security or compliance intent for your folder or project. Assured Workloads frameworks include a library of built-in cloud controls and lets you create your own. The metadata in a cloud control includes the remediation instructions and finding severity. Cloud controls have the following modes:

  * **Detective:** Assured Workloads frameworks apply the cloud control to the defined resources for monitoring purposes. Any violations are detected and findings are generated. No preventive actions are taken automatically.
  * **Preventive:** Assured Workloads frameworks apply the cloud control to the defined resources and actively enforces the rules. Any resource activity that violates the cloud control is blocked. Some cloud controls require that you provide additional information to work. For example, if you want to use a cloud control that checks whether your workloads and resources are running in particular regions, you must specify the permitted regions when you create the cloud control.

  
Framework | A collection of cloud controls and regulatory controls that represent security best practices or industry-defined standards. A framework can include a mapping between cloud controls and the regulatory controls, such as data boundaries like FedRAMP Moderate or IL2. Assured Workloads includes a library of built-in frameworks. You can customize these frameworks or create your own. **Note:** The [Assured Workloads Frameworks page](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks#view-frameworks) in the Google Cloud console displays a list of all available frameworks that can be either deployed in Assured Workloads or—depending on your [Audit Manager subscription tier](https://cloud.google.com/products/audit-manager/pricing)—can be [audited](https://docs.cloud.google.com/audit-manager/docs/run-audit).   
Framework deployment | The binding between a particular framework and a folder or project when you deploy the framework.  
  
## Supported frameworks

Assured Workloads supports built-in frameworks for Google Cloud, such as Assured Workloads data boundaries. You can deploy these frameworks as is or customize them for your needs.

### Supported Assured Workloads data boundaries

The following Assured Workloads data boundary frameworks are available:

  * [Data Boundary for FedRAMP High (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-high)
  * [Data Boundary for FedRAMP Moderate (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages#fedramp-moderate)
  * [Data Boundary for Impact Level 2 (IL2) (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il2)
  * [Data Boundary for Impact Level 4 (IL4) (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il4)
  * [Data Boundary for Impact Level 5 (IL5) (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/il5)
  * [Data Boundary for International Traffic in Arms (ITAR) (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/itar)
  * [Data Boundary for Criminal Justice Information Systems (CJIS) (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/cjis)
  * [EU Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary)
  * [EU Data Boundary and Support (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/eu-data-boundary-support)
  * [Switzerland Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/switzerland-data-boundary)
  * [UK Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/uk-data-boundary)
  * [US Data Boundary](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary)
  * [US Data Boundary and Support (Preview)](https://docs.cloud.google.com/assured-workloads/docs/control-packages/us-data-boundary-support)



## What's next

  * Learn how to [manage frameworks](https://docs.cloud.google.com/assured-workloads/docs/manage-frameworks).
  * Learn how to [manage cloud controls](https://docs.cloud.google.com/assured-workloads/docs/manage-cloud-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
