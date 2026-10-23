---
url: https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls/
title: Compliance and sovereign controls for SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:34.282898+00:00
---

# Compliance and sovereign controls for SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/compliance-and-sovereign-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Compliance and sovereign controls for SAP on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud enables you to run your SAP workloads in compliance with data residency, access control, support personnel, or regulatory requirements. This is delivered through [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview) \- a service that helps you run secure and compliant workloads.

This document provides an overview of how Assured Workloads works, and provides details on how to plan and implement Assured Workloads to meet the compliance and sovereignty requirements of your SAP workloads running on Google Cloud.

## Compliance made seamless with Assured Workloads

To run an SAP workload on Google Cloud that adheres to the requirements of a compliance program, you need to create an Assured Workloads folder for that program. The preconfigured controls of the Assured Workloads folder enable you to meet the data residency, access control, or support personnel requirements stipulated by your desired compliance program.

Once you create the required Assured Workloads folder, you deploy your SAP systems in a child Google Cloud project using the conventional deployment options provided by Google Cloud. The Google Cloud resources created under the folder automatically inherit the parent Assured Workloads folder's controls.

This way, Assured Workloads offers a seamless experience for deploying various SAP landscapes while satisfying a mix of compliance requirements. 

For example, by creating appropriate folders, you can facilitate a multinational operation that includes running a mix of SAP workloads like the following:

  * Workloads that are not required to adhere to a compliance program
  * Workloads that require EU, US, Canadian, Australian, or Israeli data residency
  * Workloads that require FedRAMP Moderate compliance
  * Workloads that require IL4 compliance



To run an SAP workload that is not required to adhere to a compliance program, you need to use a non-Assured Workloads folder. For information about creating such a folder, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).

The following image illustrates how folders and Google Cloud projects are organized in Google Cloud.

![Organization of folders and projects in Google Cloud](https://docs.cloud.google.com/static/sap/docs/images/assured-workloads-structure.svg)

### Example Assured Workloads setup for FedRAMP Moderate

The following image is an example architecture for an SAP workload that runs in compliance with US's [Federal Risk and Authorization Management Program (FedRAMP) Moderate](https://www.fedramp.gov/baselines/).

![SAP on Google Cloud: example Assured Workloads setup for FedRAMP Moderate compliance](https://docs.cloud.google.com/static/sap/docs/images/assured-workloads-eg-fedramp-moderate.svg)

## Plan for using Assured Workloads

To effectively deploy SAP workloads using Assured Workloads, the following are some high-level planning guidelines:

  1. Define the security, compliance, or sovereignty requirements for each SAP workload. In most organizations, this activity is done in consultation with their IT security teams.

For example, your SAP workload might be required to satisfy compliance requirements arising from the following:

     * Data residency and access control.
     * Regulatory compliance such as ITAR, FedRAMP Moderate and High, IL4, IL5, and Canada Protected B.
     * Sovereign controls for the European Union.
     * Data Residency controls for locations such as the European Union, Israel, US, Canada, or Australia.
  2. Design the architecture of your SAP workload. This activity identifies SAP systems and Google Cloud services that must be set up to run your SAP workload, and how they interact with each other.

  3. Contact Google Cloud Sales and review your SAP workload's architecture.

  4. In consultation with Google Cloud Sales, create a deployment plan that achieves the required compliance for your SAP workload.




## Run program-compliant SAP workloads using Assured Workloads

The following are the high-level steps that you need to complete to run program-compliant SAP workloads using Assured Workloads:

  1. Plan your deployment and review it with Google Cloud Sales.

  2. [Create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) for the required compliance program.

  3. In a Google Cloud project under your Assured Workloads folder, deploy your SAP system using the deployment guide for your scenario.




## Monitor Assured Workloads folders for violations

Once you create an Assured Workloads folder for a compliance program, Assured Workloads monitors the applied constraints, and highlights a violation if a change to a child resource is not in compliance with that program. You address the violations either by resolving them or by creating appropriate exceptions.

For more information, see [Monitor an Assured Workloads folder for violations](https://docs.cloud.google.com/assured-workloads/docs/monitor-folder).

## Get support

To get support from Cloud Customer Care for resolving problems with your SAP workloads that use Assured Workloads, you must purchase Assured Support. For more information, see the [Getting support](https://docs.cloud.google.com/assured-workloads/docs/getting-support).

When you contact Customer Care, make sure to collect and provide the required diagnostic information for the SAP products you use. For more information, see [Diagnostic information for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support-gather-diagnostic-info).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
