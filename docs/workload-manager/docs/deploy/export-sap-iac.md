---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/export-sap-iac/
title: Export and deploy \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:51.776171+00:00
---

# Export and deploy  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/export-sap-iac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Export and deploy Stay organized with collections  Save and categorize content based on your preferences. 

The Guided Deployment Automation tool in Workload Manager helps you deploy workloads on Google Cloud. The export option in the tool lets you review and customize the generated infrastructure as code (IaC) before deploying the workload.

This document describes how to download the Terraform and Ansible configuration files and deploy your workload on Google Cloud.

## Export Terraform and Ansible IaC

During the configuration, after you specify the deployment details for your system, the Guided Deployment Automation tool provides you with an option to download the Terraform and Ansible infrastructure as code (IaC), instead of Workload Manager deploying the system automatically.

![Download Terraform for deployment](https://docs.cloud.google.com/static/workload-manager/images/download-tf.png)

The downloaded Terraform file contains variables based on the configuration of your deployment. The following variables download the Terraform and Ansible files from a Google-owned repository, when required:

  * `source`: downloads the remaining Terraform files.
  * `package_location`: downloads the Ansible scripts.



You can customize the Terraform files and modify the deployment configuration. For more information about managing and deploying Terraform files in Google Cloud, see [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform).

Any modifications to the Terraform or Ansible IaC might cause issues during the deployment process or cause your configuration to no longer follow the best practices and recommendations.

**Note** : 

  * Workload Manager does not register any workloads deployed on your own using Terraform and it does not list these deployments on the Deployments dashboard. For these reasons, we recommend that only advanced users use the Download feature.
  * When you use the downloaded Terraform file to deploy the SAP workload, Workload Manager does not use the service account you attached to the deployment. Workload Manager uses the credentials of the user to authenticate and to run the Terraform file. For more information about service account attachment, see [Service accounts](https://docs.cloud.google.com/workload-manager/docs/deploy/prerequisites#service-accounts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
