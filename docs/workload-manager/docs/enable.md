---
url: https://docs.cloud.google.com/workload-manager/docs/enable/
title: Enable the Workload Manager API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:51.011800+00:00
---

# Enable the Workload Manager API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Enable the Workload Manager API Stay organized with collections  Save and categorize content based on your preferences. 

Enable the Workload Manager API to use its rule-based validation, guided deployment automation, and observability services for your workloads running on Google Cloud. Workload Manager lets you automate workload deployment, detect deviations from best practices, and monitor system health to help you improve system quality, reliability, and performance.

This document describes how to enable the Workload Manager API.

For information about Workload Manager and its features, see [About Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview).

## Before you begin

Before you enable the Workload Manager API, do the following:

  * Ensure that you have the `serviceusage.services.enable` IAM permission. If you don't have this permission, ask your administrator to grant you the Service Usage Admin (`roles/serviceusage.serviceUsageAdmin`) role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Ensure that billing is enabled for your Google Cloud project. [Verify billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).



## Enable the API

You can enable the Workload Manager API by using the Google Cloud console or the gcloud CLI.

###  Console 

  1. In the Google Cloud console, on the project selector page, select the project in which you want to enable Workload Manager.

  2. Enable the Workload Manager API.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workloadmanager)




###  gcloud 

To enable the API, use the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
    
    
      gcloud services enable workloadmanager.googleapis.com \
      --project=PROJECT_ID
    

Replace `PROJECT_ID` with the project ID of the _consumer_ project in which you create and run Workload Manager evaluations or the project in which you deploy workloads by using Workload Manager.

## What's next

  * Learn about [Workload Manager evaluations](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).
  * Learn about [Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment).
  * Learn about [Workload Manager's observability service for SAP](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
