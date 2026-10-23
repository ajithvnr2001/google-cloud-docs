---
url: https://docs.cloud.google.com/risk-manager/docs/managing-reports/
title: Managing reports \u00a0|\u00a0 Cyber Insurance Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:23.636262+00:00
---

# Managing reports  |  Cyber Insurance Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/risk-manager/docs/managing-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cyber Insurance Hub ](https://docs.cloud.google.com/risk-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/risk-manager/docs/quickstarts)



Send feedback 

#  Managing reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to manage reports using Cyber Insurance Hub on Google Cloud.

## Before you begin

  1. Complete the [onboarding steps](https://docs.cloud.google.com/risk-manager/docs/onboard) for your organization.
  2. [Configure Cyber Insurance Hub](https://docs.cloud.google.com/risk-manager/docs/configuring-risk-manager).



## Create a report

A report is an organization-level object that aggregates information from [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory) and [Security Command Center](https://docs.cloud.google.com/security-command-center) to build an aggregate view of risk across your organization. These reports are aligned to the [CIS Google Cloud Platform Foundation Benchmark v1.2.0](https://www.cisecurity.org/insights/blog/cis-benchmarks-may-2021-update). For more information on this framework, see [Vulnerabilties findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

You can enable [automatic report generation](https://docs.cloud.google.com/risk-manager/docs/automated-reports).

Alternatively, to create a manual report, follow these steps:

  1. In the Google Cloud console, go to the **Cyber Insurance Hub** page.

[Go to Cyber Insurance Hub](https://console.cloud.google.com/security/riskmanager)

  2. On the **Cyber Insurance Hub** page, click **Create manual report**.

When the report has finished, you see a green circle with a check mark. Click the date in the **Created on** column to view the report.




## Download a report

After you create a report, you can download it.

To download a report, follow these steps:

  1. In the Google Cloud console, go to the **Cyber Insurance Hub** page.

[Go to Cyber Insurance Hub](https://console.cloud.google.com/security/riskmanager)

  2. Click the date of the report that you want to download. 
  3. On the report view page, click **Download**. 



## Approve a report

To approve a Cyber Insurance Hub report, you must have one of the following IAM roles:

  * [Risk Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.admin) (`roles/riskmanager.admin`)
  * [Risk Manager Report Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/riskmanager#riskmanager.reviewer) (`roles/riskmanager.reviewer`)



For more information about roles in Cyber Insurance Hub, see [Cyber Insurance Hub roles](https://docs.cloud.google.com/risk-manager/docs/access-control#predefined-roles).

This responsibility often lies with the treasury team in larger organizations.

To approve a report, follow these steps:

  1. In the Google Cloud console, go to the **Cyber Insurance Hub** page.

[Go to Cyber Insurance Hub](https://console.cloud.google.com/security/riskmanager)

  2. On the **Cyber Insurance Hub** page, view an individual report by clicking the date in its **Created on** column. 
  3. In the page that opens, in the **Status** field, select whether the report is approved for sharing. 



To send the report to insurers, select **Approved to share**.

If the report is **Unreviewed** , then the system generates a warning when a user attempts to send that report to insurers.

If you select **Do not share** , then you can't send the report to insurers.

## Send a report to insurance carriers

Cyber Insurance Hub lets you send reports to our insurance partners: [Beazley](https://www.beazley.com/en-us/fullspectrumcyber/google-cloud/), [Chubb](https://www.chubb.com/risk-protection-program.html), and [Munich Re](https://www.munichre.com/en/solutions/for-industry-clients/cloud-protection-plus.html). Our partners can use Cyber Insurance Hub reports to potentially reduce the cost of cyber insurance and provide broad coverage designed exclusively for Google Cloud customers. Learn more about the [Risk Protection Program](https://cloud.google.com/security/products/risk-protection-program).

Once you create a report, and the report has been approved, you can send it to our insurance carrier partners.

### Reach out to your broker

You can use any broker to access the Risk Protection Program. If you don't have a broker, you can use one of the following insurance brokers who can advise you on the cyber insurance policies our partners provide. To learn more, reach out to your broker or to any of the following brokers:

Broker | Contact | Email template  
---|---|---  
Aon | `GCRiskManager@aon.com` | [Contact Aon](mailto:GCRiskManager@aon.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20Aon%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
Alliant | `AlliantCyber@Alliant.com` | [Contact Alliant](mailto:AlliantCyber@Alliant.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20Alliant%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
Epic | `cyberinsure@epicbrokers.com` | [Contact Epic](mailto:cyberinsure@epicbrokers.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20Epic%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
Lockton | `GoogleRPP@lockton.com` | [Contact Lockton](mailto:GoogleRPP@lockton.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20Lockton%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
Marsh | `CyberRPP@marsh.com` | [Contact Marsh](mailto:CyberRPP@marsh.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20Marsh%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
McGill and Partners | `cyber.it@mcgillpartners.com` | [Contact McGill and Partners](mailto:cyber.it@mcgillpartners.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20McGill%20and%20Partners%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
NFP | `nfpcyberpanel@nfp.com` | [Contact NFP](mailto:nfpcyberpanel@nfp.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20NFP%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
Willis Towers Watson | `CPP@wtwco.com` | [Contact Willis Towers Watson](mailto:CPP@wtwco.com?subject=Interested%20in%20Google%20Cloud%27s%20Risk%20Protection%20Program&body=Hi%20Willis%20Towers%20Watson%20team,%0A%0AMy%20name%20is%20%7BYOUR_NAME%7D%20and%20I%20am%20the%20%7BYOUR_ROLE%7D%20at%20%7BORGANIZATION_NAME%7D,%20located%20in%20%7BORGANIZATION_COUNTRY_NAME%7D.%0A%0AI%20am%20a%20%7BCURRENT%20/%20PROSPECTIVE%7D%20Google%20Cloud%20customer%20and%20am%20interested%20in%20engaging%20an%20insurance%20broker%20to%20learn%20more%20about%20Google%20Cloud%27s%20Risk%20Protection%20Program.%20This%20email%20was%20listed%20on%20the%20Google%20Cloud%20documentation%20as%20a%20broker%20partner%20that%20could%20assist%20me.%0A%0APlease%20let%20me%20know%20your%20next%20available%20time%20to%20discuss%20the%20program%20and%20potential%20next%20steps.%0A%0AThank%20you.)  
  
### Send the report

To send a Cyber Insurance Hub report, you must have the following IAM role:

  * Risk Manager Admin (`roles/riskmanager.admin`)



Once you have an approved report and you've contacted your broker, you can send that report using Cyber Insurance Hub. After the report is sent, your broker will coordinate next steps with you and the insurance carriers. Your broker is responsible for leading you through the rest of the insurance process.

To send a report to our insurance carrier partners, follow these steps:

  1. In the Google Cloud console, go to the **Cyber Insurance Hub** page.

[Go to Cyber Insurance Hub](https://console.cloud.google.com/security/riskmanager)

  2. On the **Cyber Insurance Hub** page, view an individual report by clicking the date in its **Created on** column. 
  3. On the report view page, make sure the report has a status of **Approved to share** in the top left corner. Then, click **Send report to insurance partners**. 
  4. On the **Send** page, do the following steps: 

     * Enter your email address. You receive a confirmation email once the report is sent.
     * Enter the requested details about your organization so that our partners can correctly route your application.
     * Select or enter your organization's insurance broker, if known.
     * Select the insurance partners that you want to share your report with.
     * Acknowledge that you have authority to send the report and agree to the consent and disclosure language.
     * Click **Agree**.
  5. In the **Confirmation** dialog, enter the name of your Google Cloud organization to confirm that you want to send the report to the selected insurance carrier partners.

After you send the report, the selected partners will have access to the report, your **Organization ID** , and the information you have provided. 

  6. Click **Send** to send the report to the selected insurance carrier partners. 



## What's next

  * Learn how to [remediate findings](https://docs.cloud.google.com/risk-manager/docs/remediate-findings).
  * Learn about [automatic report generation](https://docs.cloud.google.com/risk-manager/docs/automated-reports).
  * Learn about [audit logging](https://docs.cloud.google.com/risk-manager/docs/audit-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
