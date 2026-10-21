---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center/
title: Use Security Command Center in the Google Cloud console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:24.302209+00:00
---

# Use Security Command Center in the Google Cloud console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Security Command Center in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides an overview of Security Command Center in the Google Cloud console, describes the navigation, and gives an overview of top-level pages.

If you haven't set up Security Command Center, see one of the following for instructions about how to activate it:

  * To activate the Standard or Premium tier, see [Overview of activating Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).
  * To activate the Enterprise tier, see [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).



For a general overview of Security Command Center, see [Security Command Center overview](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

If Security Command Center was recently activated, it might take time for data to appear. For information about the scan frequency of Security Command Center services, see [When to expect findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview). 

## Required IAM permissions

To use Security Command Center with all service tiers, you must have an Identity and Access Management (IAM) role that includes appropriate permissions:

###  Standard-legacy 

  * **Security Center Admin Viewer** (`roles/securitycenter.adminViewer`) lets you view Security Command Center.
  * **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) lets you view Security Command Center and make changes.



### Standard

You must have one of the following:

  * **Security Center Admin** (`roles/securitycenter.admin`)
  * **Security Center Admin Editor** (`roles/securitycenter.adminEditor`)
  * **Security Center Viewer** (`roles/securitycenter.adminViewer`)



### Premium

  * **Security Center Admin Viewer** (`roles/securitycenter.adminViewer`) lets you view Security Command Center.
  * **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) lets you view Security Command Center and make changes.



### Enterprise

  * **Security Center Admin Viewer** (`roles/securitycenter.adminViewer`) lets you view Security Command Center.
  * **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) lets you view Security Command Center and make changes.
  * **Chronicle Service Viewer** (`roles/chroniclesm.viewer`) lets you view the associated Google SecOps instance.



You also need any of the following IAM roles:

  * **Chronicle SOAR Admin** (`roles/chronicle.soarAdmin`)
  * **Chronicle SOAR Threat Manager** (`roles/chronicle.soarThreatManager`)
  * **Chronicle SOAR Vulnerability Manager** (`roles/chronicle.soarVulnerabilityManager`)



To enable access to SOAR-related features, you must also map these Identity and Access Management roles to a **SOC role** , **Permission group** , and **Environment** on the **Settings > SOAR settings** page. For more information, see [Map and authorize users using IAM](https://docs.cloud.google.com/security-command-center/docs/map-users-in-secops).

If your organization policies are set to [restrict identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), you must be signed in to the console on an account that's in an allowed domain.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Options when working in the console

This section describes options that determine how you work with data and configuration settings in the Google Cloud console. Each option provides a filtered view of all data stored in Security Command Center.

### Use Security Command Center with data residency enabled

If data residency is enabled and you aren't using the jurisdictional console for the configured location, you see a message on the page to open the jurisdictional console for the configured location. For more information, see [About the jurisdictional console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console).

When you open the console for a specific jurisdiction, Security Command Center displays [data that's subject to data residency controls](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#create-view-data) from that location only.

The following Security Command Center pages don't require that you use the jurisdictional console:

  * **Assets** : When you select the organization scope, displays all assets in the organization or project regardless of jurisdiction.
  * **Settings** : Displays all configuration settings.



### Select a scope: organization, project, or folder

When you select a specific project or folder, some pages display only findings, data, and configuration options specific to the resources in the selected scope. The data doesn't show cross-project correlations, such as toxic combination or attack paths that depend on resource relationships across the organization.

Some features are available at the organization scope only and you're prompted to select an organization.

### Filter by application

Some pages let you filter data for a single application and displays data for resources [registered to the App Hub application](https://docs.cloud.google.com/app-hub/docs/register-resources). For more information, see [Application Design Center integration](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#application-security-assessments).

## Access Security Command Center

To access Security Command Center in the console, do the following:

  1. Go to Security Command Center:

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/overview)

  2. Select the project or organization that you want to view.

If Security Command Center is active in the organization or project you select, the **Risk overview** page appears.

If Security Command Center is not active, you are invited to activate it. For more information about activating Security Command Center, see one of the following:

     * Standard, Standard-legacy, or Premium: [Overview of activating Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview).
     * Enterprise: [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).



## Security Command Center navigation

The following describes the navigation in Security Command Center. The navigation differs depending on your [Security Command Center service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers). The tasks that you can perform also depend on [services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center) that are enabled and the IAM permissions that you are granted.

Click a link for an explanation of the page.

###  Standard-legacy 

The following describes the navigation in Security Command Center Standard-legacy service tier.

  * Risk overview
  * Issues page: Prompts you to upgrade to the Premium service tier.
  * Threats: Prompts you to upgrade to the Premium service tier.
  * Compliance: Prompts you to upgrade to the Premium service tier.
  * Assets
  * Findings
  * Sources
  * Posture Management: Prompts you to upgrade to the Premium service tier.
  * Settings



### Standard

The following describes the navigation in Security Command Center Standard.

  * Risk overview
  * Issues page: Prompts you to upgrade to the Premium service tier.
  * Threats: Prompts you to upgrade to the Premium service tier.
  * Compliance
  * Assets
  * Findings
  * Sources
  * Posture Management: Prompts you to upgrade to the Premium service tier.
  * Settings



### Premium

The following describes the navigation in Security Command Center Premium.

  * Risk overview
  * Graph Search
  * Issues page
  * Findings
  * Assets
  * Compliance
  * Posture Management
  * Sources
  * Settings



### Enterprise

In the Security Command Center Enterprise left navigation, **Cases** links to pages in the Google Security Operations tenant that was configured during Security Command Center Enterprise activation.

For information about the features available in Google Security Operations, see Security Command Center Enterprise links to the Security Operations console.

  * Risk overview
  * Graph Search
  * Issues page
  * Findings
  * Assets
  * Compliance
  * Posture Management
  * Sources
  * Settings
  * Setup Guide
  * Cases



### Risk overview

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **Risk overview** page serves as your first-contact security dashboard, highlighting high-priority risks in your cloud environments identified by all built-in and integrated services.

The views on the **Risk overview** page differ depending on your service tier.

###  Standard-legacy 

Learn more about each investigative view by selecting one of the following views:

  * [All risk](https://docs.cloud.google.com/security-command-center/docs/assess-risk#all-risk): shows misconfiguration findings. 
  * [Vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/assess-risk#vulnerabilities): displays vulnerabilities and related CVE information. 
  * [Identity](https://docs.cloud.google.com/security-command-center/docs/assess-risk#identity): shows a summary of identity and access findings by category. 
  * [Threats](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats): Prompts you to upgrade to the Premium service tier. 



###  Standard 

Learn more about each investigative view by selecting one of the following views:

  * [All risk](https://docs.cloud.google.com/security-command-center/docs/assess-risk#all-risk): shows misconfiguration findings. 
  * [Vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/assess-risk#vulnerabilities): displays vulnerabilities and related CVE information. 
  * [Identity](https://docs.cloud.google.com/security-command-center/docs/assess-risk#identity): shows a summary of identity and access findings by category. 
  * [Data](https://docs.cloud.google.com/security-command-center/docs/assess-risk#data): displays information about your data security posture. 
  * [Threats](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats): Prompts you to upgrade to the Premium service tier. 



###  Premium 

Learn more about each investigative view by selecting one of the following views:

  * [All risk](https://docs.cloud.google.com/security-command-center/docs/assess-risk#all-risk): shows all data. 
  * [Vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/assess-risk#vulnerabilities): displays vulnerabilities and related CVE information. 
  * [Identity](https://docs.cloud.google.com/security-command-center/docs/assess-risk#identity): shows a summary of identity and access findings by category. 
  * [Data](https://docs.cloud.google.com/security-command-center/docs/assess-risk#data): displays information about your data security posture. 
  * [AI Security](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection): shows AI-related findings and security posture data. 
  * [Threats](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats): shows threat-related findings. 



###  Enterprise 

Learn more about each investigative view by selecting one of the following views:

  * [All risk](https://docs.cloud.google.com/security-command-center/docs/assess-risk#all-risk): shows all data. 
  * [Vulnerabilities](https://docs.cloud.google.com/security-command-center/docs/assess-risk#vulnerabilities): displays vulnerabilities and related CVE information. 
  * [Identity](https://docs.cloud.google.com/security-command-center/docs/assess-risk#identity): shows a summary of identity and access findings by category. 
  * [Data](https://docs.cloud.google.com/security-command-center/docs/assess-risk#data): displays information about your data security posture. 
  * [AI Security](https://docs.cloud.google.com/security-command-center/docs/assess-risk#ai-protection): shows AI-related findings and security posture data. 
  * [Threats](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats): shows threat-related findings. 



### Assets

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

**Important:** On or after July 11, 2024, you will need a new Identity and Access Management (IAM) permission to view assets on the **Assets** page in the console.

If your business uses [custom IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#custom) for strict access control to Google Cloud resources, ask your security administrator to add the `cloudasset.assets.searchEnrichmentResourceOwners` permission to your custom role. 

If your business uses [predefined IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) to control access to the **Assets** page, such as the `roles/securitycenter.assetsViewer` role, you don't need to do anything. 

The **Assets** page provides a detailed display of all Google Cloud resources, also called _assets_ , in your project or organization.

For more information about how to work with assets on the **Assets** page, see [Work with resources in the console](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console).

### Compliance

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (some features require [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

By default, when you activate Security Command Center, you enable [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-overview). The **Compliance** page shows the following tabs: **Configure (New)** , **Monitor (New)** , and **Audit (New)**. These tabs let you create and apply cloud controls and frameworks, monitor your environment, and complete audits.

If you activated Security Command Center before Compliance Manager was generally available and you don't enable Compliance Manager, the **Compliance** page shows a **Monitor** tab only. This tab shows all industry benchmarks that Security Command Center supports using Security Health Analytics and the percentage of passing benchmark controls. For more information about how Security Command Center supports compliance management if Compliance Manager isn't enabled, see [Assess compliance without Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-management).

### Findings

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

On the **Findings** page, you can query, review, mute, and mark Security Command Center _findings_ , the records that Security Command Center services create when they detect a security issue in your environment. For more information about how to work with findings on the **Findings** page, see [Review and manage findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings).

### Graph Search

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Security graph in Security Command Center is a database that understands and maps the relationships between your cloud resources, their configurations, and associated security risks. These risks include vulnerabilities, access permissions, data sensitivity, and network exposure. This graph offers a comprehensive view of your cloud assets and their interdependencies.

On the **Graph Search** page, you can query the security graph to proactively identify and monitor potential security vulnerabilities within your environment.

For more information about querying the security graph, see [Exploring the security graph using queries](https://docs.cloud.google.com/security-command-center/docs/graph-search).

### Issues

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Issues are the most important security risks that Security Command Center finds in your cloud environments, giving you the opportunity to respond quickly to vulnerabilities and threats. Security Command Center discovers issues through virtual red teaming and rule-based detections. For information about investigating issues, see [Issues overview](https://docs.cloud.google.com/security-command-center/docs/issues-overview).

### Posture management

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

On the **Posture** page, you can view details about the [security postures](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture) that you created in your organization and apply the postures to an organization, folder, or project. You can also view the available predefined posture templates.

### Settings

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Open the **Settings** page from the **Settings** link in the navigation. The **Settings** page lets you configure Security Command Center, including the following:

  * [Additional Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center)
  * [AI Protection](https://docs.cloud.google.com/security-command-center/docs/configure-ai-protection)
  * Multi-cloud connectors for [AWS](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) and [Azure](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure)
  * [High-value resource sets](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set)
  * [Mute findings rules](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings)
  * [Continuous data exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data)



### SCC setup guide

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **Setup guide** page lets you activate Security Command Center Enterprise and configure additional services. For more information, see [Activate the Security Command Center Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier).

### Sources

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The **Sources** page contains cards that provide a summary of assets and findings from the security sources you have enabled. The card for each security source shows some of the findings from that source. You can click the finding category name to view all findings in that category.

#### Findings by source

The **Findings by source** card displays a count of each category of finding that your enabled security sources provide.

  * To view details about the findings from a specific source, click the source name.
  * To view details about all findings, click the **Findings** page, where you can group findings or view details about an individual finding.



#### Source summaries

Below the **Findings by source** card, separate cards appear for any built-in, integrated, and third-party sources you enabled. Each card provides counts of active findings for that source.

### Threats

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

Threats are potentially harmful events in your cloud resources. Security Command Center displays threats in different views, depending on your service tier.

###  Standard and Standard-legacy

The **Threats** page is not supported in Security Command Center Standard and Standard-legacy. You can view threat findings on the **Findings** page.

###  Premium 

In Security Command Center Premium, the **Threats** navigation link opens the **Risk Overview** > [Threats dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats).

###  Enterprise 

In Security Command Center Enterprise, you view threats in the **Risk Overview** > [Threats dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#threats).

### Legacy Vulnerabilities page

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The legacy **Vulnerabilities** page lists all of the misconfiguration and software vulnerability findings that the built-in detection services of Security Command Center run in your cloud environments. For each listed detector, the number of active findings is displayed.

To view the **Vulnerabilities** page in Security Command Center, do the following:

  1. In the Google Cloud console, go to the **Risk overview** page.

[Go to Risk overview](https://console.cloud.google.com/security/command-center/overview)

  2. On the **Risk Overview** page, click **Vulnerabilities**.

  3. On the **Vulnerabilities** dashboard, click **Go to legacy page**.




#### Vulnerability detection services

The **Vulnerabilities** page lists detectors for the following built-in detection services of Security Command Center:

  * [Notebook Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#notebook-security-scanner) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors)
  * [Vulnerability Assessment for Amazon Web Services (AWS)](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview)
  * [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview)



Other Google Cloud services that are integrated with Security Command Center also detect software vulnerabilities and misconfigurations. The findings from a selection of these services are also displayed on the **Vulnerabilities** page. For more information about the services that produce vulnerability findings in Security Command Center, see [Detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources).

#### Information about vulnerability detector categories

For each misconfiguration or software vulnerability detector, the **Vulnerabilities** page shows the following information:

  * **Status** : an icon indicates whether the detector is active and whether the detector found a finding that needs to be addressed. When you hold the pointer over the status icon, a tooltip displays the date and time the detector found the result or information about how to validate the recommendation.
  * **Last scanned** : the date and time of the last scan for the detector.
  * **Category** : the category or type of vulnerability. For a list of the categories that each Security Command Center service detects, see the following: 
    * [Notebook Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#nss-findings) ([Preview](https://cloud.google.com/products#product-launch-stages))
    * [Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#security-health-analytics-detectors)
    * [Vulnerability Assessment for AWS findings](https://docs.cloud.google.com/security-command-center/docs/vulnerability-assessment-aws-overview#findings)
    * [Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#web-security-scanner-findings)
  * **Recommendation** : a summary of how to remediate the finding. For more information, see the following:

    * [Remediating Security Health Analytics findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-security-health-analytics-findings).
    * [Remediating Web Security Scanner findings](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings)
    * [Review and resolve package vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/enable-notebook-security-scanner#review-findings)
  * **Active** : the total number of findings in the category.

  * **Standards** : the compliance benchmark that the finding category applies to, if any. For more information about benchmarks, see [Vulnerabilities findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings#detectors_and_compliance).




#### Filtering vulnerability findings

A large organization might have many vulnerability findings across their deployment to review, triage, and track. By using filters that are available on the Security Command Center **Vulnerabilities** and **Findings** pages in the Google Cloud console, you can focus on the highest severity vulnerabilities across your organization, and review vulnerabilities by asset type, project, and more.

For more information about filtering vulnerability findings, see [Filter vulnerability findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/filter-vulnerability-findings).

## Links to the Security Operations console

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

The Security Command Center Enterprise tier includes features available on both the Google Cloud console pages and on Security Operations console pages.

You sign in to the console and navigate to Security Operations console pages from the console navigation. This section describes the tasks that you can perform on each page and the navigation links that open Security Operations console pages.

For information about Google Security Operations features available with the Security Command Center Enterprise tier, see [Google SecOps features in Security Command Center Enterprise](https://docs.cloud.google.com/security-command-center/docs/secops-limits).

###  Google Cloud console pages

The Google Cloud console pages let you perform tasks such as the following:

  * Activate Security Command Center.
  * Set up Identity and Access Management (IAM) permissions for all Security Command Center users.
  * Connect to other cloud environments to collect resource and configuration data.
  * Work with and export findings.
  * Assess risks with attack exposure scores.
  * Work with issues, the most important security risks Security Command Center Enterprise has found in your cloud environments.
  * Identify high-sensitivity data with Sensitive Data Protection.
  * Investigate and remediate individual findings.
  * Configure Security Health Analytics, Web Security Scanner, and other Google Cloud integrated services.
  * Manage security postures.
  * Configure cloud controls and frameworks.
  * Manage a data security posture.
  * Assess and report on your compliance with common security standards or benchmarks.
  * View and search your Google Cloud assets.



**Note** : The **Findings** page doesn't show threat detections and alerts created by [curated detections](https://docs.cloud.google.com/security-command-center/docs/investigate-threat-findings). To view these detections and alerts in the Security Operations console, go to **SIEM Dashboards**. For more information about this console page, see [Security Operations console](https://docs.cloud.google.com/security-command-center/docs/scce-consoles-overview#secops-console). 

###  Security Operations console pages 

The Security Operations console page lets you perform tasks such as the following:

  * Connect to other cloud environments to collect log data for curated detections in security information and event management (SIEM).
  * Configure security orchestration, automation, and response (SOAR) settings.
  * Configure users and groups for incident and case management.
  * Work with cases, which includes grouping findings, assigning tickets, and working with alerts.
  * Use an automated sequence of steps known as playbooks to remediate problems.
  * Use Workdesk to manage actions and tasks waiting for you from open cases and playbooks.


    
    
    https://CUSTOMER_SUBDOMAIN.backstory.chronicle.security/cases
    

Where `CUSTOMER_SUBDOMAIN` is your customer-specific identifier.

### Cases

In the Security Operations console, you use cases to obtain details about findings, attach playbooks to finding alerts, apply automatic threat responses, and track the remediation of security issues.

For information, see [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview) in Google Security Operations documentation.

## What's next

  * Learn about [detection services](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources) that generate findings in Security Command Center.
  * Learn how to [annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings).
  * Learn how to [configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
