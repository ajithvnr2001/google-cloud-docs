---
url: https://docs.cloud.google.com/security-command-center/docs/download-risk-reports/
title: Download risk reports \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:51.942637+00:00
---

# Download risk reports  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/download-risk-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Download risk reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document describes how to download risk reports that are generated for your Security Command Center organization.

Risk reports provide insights into potential attack paths and exposures within your Google Cloud environment. You can download reports to review findings and share information with security management and analysts.

## Required roles

Before you download a risk report, verify that you meet the following requirements:

To get the permissions that you need to download a risk report, ask your administrator to grant you the [Security Center Risk Reports Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.riskReportsViewer) (`roles/securitycenter.riskReportsViewer`) IAM role on your Security Command Center organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to download a risk report. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to download a risk report:

  * `securitycenter.riskReports.get`
  * `securitycenter.riskReports.list`
  * `securitycenter.userinterfacemetadata.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Download a risk report

Download a risk report as a PDF from the Google Cloud console.

  1. In the **Security** navigation menu in Security Command Center, click **Download Risk Report**.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/overview)

**Note:**
     * If you don't have the required role to download a report, the Google Cloud console displays a message indicating the necessary permissions.
     * If you have the required role but a risk report is not available, the system scan is still running. The report becomes available after the scan completes.
  2. From the **Download Risk Report** window, select the report that you want to download. You can select the latest report or a report from a specific date within the last 30 days.

The Google Cloud console provides quick links to download the **Most recent** report, the report from **1 week ago** , and the report from **30 days ago**. The quick links include the timestamp or date of the report. The first page of the downloaded report includes a timestamp that indicates when data for the report was collected.

  3. Optional. If you want to choose a report that the quick links didn't locate, choose an option in **Select a report date**.

  4. Choose your encryption option: **Add password encryption** (the default option) or **Do not password encrypt**.

If you want to encrypt the PDF file, you must provide a password between 12-16 characters, using any combination of ASCII letters, numbers, and symbols. Google Cloud does not store or provide password recovery if you lose the password.

  5. Click **Download**.




The report is downloaded as a PDF file to the system that you're using. Typically, the file is available in the browser downloads folder by default.

## What's next

To learn more, see [Risk reports overview](https://docs.cloud.google.com/security-command-center/docs/risk-reports-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
