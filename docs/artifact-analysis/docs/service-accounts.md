---
url: https://docs.cloud.google.com/artifact-analysis/docs/service-accounts/
title: Artifact Analysis service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:38.869817+00:00
---

# Artifact Analysis service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)



Send feedback 

#  Artifact Analysis service accounts Stay organized with collections  Save and categorize content based on your preferences. 

The Container Analysis API analyzes your container images and stores metadata using a service account, a special Google Account that collects information about your images on your behalf.

The email for the Container Analysis service account is:

`service-[PROJECT_NUMBER]@artifact-analysis.iam.gserviceaccount.com`

PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Artifact Analysis is enabled.

This account has the **[Container Analysis Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.ServiceAgent)** role.

If you enable vulnerability scanning, the Container Scanning API used by this feature also creates a special Google Account.

The email for the Container Scanning service account is:

`service-[PROJECT_NUMBER]@gcp-sa-containerscanning.iam.gserviceaccount.com`. The account uses the **Container Scanner Service Agent** role.

PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Artifact Analysis is enabled.

You can view your project's service accounts in the [IAM menu of the Google Cloud console](https://console.cloud.google.com/iam-admin).

## What's next

Learn about [Artifact Analysis roles and configuring access](https://docs.cloud.google.com/artifact-analysis/docs/access-control).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
