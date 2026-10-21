---
url: https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions/
title: Prepare IAM permissions and storage \u00a0|\u00a0 Transfer Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:44.957233+00:00
---

# Prepare IAM permissions and storage  |  Transfer Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transfer-appliance/docs/4.0/prepare-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Transfer Appliance ](https://docs.cloud.google.com/transfer-appliance/docs)



Send feedback 

#  Prepare IAM permissions and storage Stay organized with collections  Save and categorize content based on your preferences. 

To prepare Google Cloud permissions and storage, choose one of the following options:

  * Recommended: [Appliance Cloud Setup Application](https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-application). Within the Google Cloud Console, you activate Google Cloud Shell and download a small application. The application prompts you for values and configures Google Cloud permissions and storage. Then you send relevant data to the Transfer Appliance Team.

  * [Step-by-step configuration](https://docs.cloud.google.com/transfer-appliance/docs/4.0/permissions-step-by-step). You use either the Google Cloud console or a command line prompt to configure your Google Cloud permissions and storage. You apply all necessary changes and send relevant data to the Transfer Appliance Team.




## Service account quick reference

The following service accounts and roles are required. They are configured during the setup process.

Service Account | Roles Required in Customer Project | Role Required in Bucket | Comment  
---|---|---|---  
`SESSION_ID@transfer-appliance-zimbru.iam.gserviceaccount.com` | N/A | Storage Admin | For offline transfer  
`project-TENANT_IDENTIFIER@storage-transfer-service.iam.gserviceaccount.com` The project identifier belongs to the tenant project. | N/A | Storage Admin | A Google-managed service agent for offline transfer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
