---
url: https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client/
title: Troubleshoot issues with discovery client \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:26.756507+00:00
---

# Troubleshoot issues with discovery client  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Troubleshoot issues with discovery client Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to resolve issues with the discovery client.

## Use logs to identify issues

The discovery client generates log files that you can use for debugging. Logs are stored locally on the machine where you installed the discovery client in the `C:\ProgramData\Google\mcdc\logs` folder.

**Note:** The logs files are limited in size, therefore the discovery client periodically deletes the content of old logs.

## Troubleshoot permissions and service accounts

If you experience issues with the authorization in connected mode, you might not have the permissions required to create a service account in your organization, or might lack the required roles to authorize the discovery client.

To resolve the issue, ask your organization administrator to create a service account for you, and to assign the `roles/migrationcenter.discoveryClient` role. Also, make sure that the **Cloud Resource Manager API** is enabled in the project.

If you have a newly created organization on Google Cloud, by default service account key creation is disabled. To enable service account key creation, make sure you have the `Organization Policy Administrator` role assigned, then follow these steps:

  1. In the Google Cloud console, go to **IAM > Organization Policies**.
  2. Click the policy named **Disable service account key creation**.
  3. Click **Manage Policy**.
  4. On the **Edit policy** page, in the **Applies to** section, select **Customize**.
  5. In the **Rules** section, expand **Edit rule** , then set **Enforcement** to **Off**.
  6. To finish, click **Set Policy**.



## Troubleshoot installation issues

If you install or upgrade the discovery client, but you're not logged in as a local administrator, the MSI execution likely fails with the following error message:
    
    
    Google Cloud Migration Center discovery client Setup Wizard ended prematurely
    because of an error. Your system has not been modified. To install this program
    at a later time, run Setup Wizard again. Click the Finish button to exit the
    Setup Wizard.
    

To resolve the issue, right-click the MSI file and run it as an administrator.

In some cases, due to specific Windows versions or domain policies, the "Run as Administrator" option might be hidden. To resolve the issue, try the following workarounds:

  * **Preferred method:** Open PowerShell as an administrator, and run `msiexec.exe /i mcdc.msi /L*V "C:\installer.log"`.

**Tip:** if you have issues installing with PowerShell, check if you're using relative paths or long paths.
  * **Alternative method:** [Edit the registry](https://learn.microsoft.com/en-us/answers/questions/1090352/windows-11-msi-and-uac-rights) to show this option in the UI.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
