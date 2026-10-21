---
url: https://docs.cloud.google.com/sap/docs/getting-support-diag-info-tf-config/
title: Terraform configurations for SAP diagnostic information \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:30.457145+00:00
---

# Terraform configurations for SAP diagnostic information  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/getting-support-diag-info-tf-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Terraform configurations for SAP diagnostic information Stay organized with collections  Save and categorize content based on your preferences. 

For problems that are related to the Terraform configurations that Google Cloud provides for deploying SAP systems, gather the following information before you contact Cloud Customer Care for support:

  * A complete and detailed description of the problem or error, including:

    * The current application or system state.
  * The URL of the Google Cloud deployment guide that corresponds to the Terraform configuration that you are using. You can find all of the guides at [Supported SAP solutions](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).

  * After removing any plain text passwords, the Terraform configuration that you used for your deployment.

  * If you experienced errors running `terraform apply`, then share the complete output.

Alternatively, you can enable the Terraform debug mode as follows, retry the deployment and then share the output log file with Customer Care. To do this, follow these steps:

    1. In your terminal, go to the working directory of your Terraform configuration.

    2. Destroy your Terraform configuration:
           
           terraform destroy
           

    3. Set the following environment variables:
           
           export TF_LOG=INFO
           export TF_LOG_PATH=tf_debug.log
           

    4. Run `terraform apply` to reproduce the issue.

    5. Share the `tf_debug.log` from the working directory.

  * If the deployed VM is available, then provide the `/var/log/messages` file.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
