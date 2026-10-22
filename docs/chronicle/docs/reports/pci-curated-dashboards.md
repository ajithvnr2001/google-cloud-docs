---
url: https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards/
title: PCI curated dashboards overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:18.106621+00:00
---

# PCI curated dashboards overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PCI curated dashboards overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes Payment Card Industry (PCI) dashboards that provide a centralized view of key metrics and information on an organization's PCI compliance. These dashboards help you take immediate action in response to security threats. The PCI dashboards use reference lists. For more information about reference lists, see [Reference list](https://docs.cloud.google.com/chronicle/docs/reference/reference-lists).

**Note:** Google SecOps PCI dashboards help monitor compliance with PCI controls but don't guarantee compliance.

The following PCI dashboards are available as curated dashboards:

Curated dashboard | Description  
---|---  
[Anti-malware](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#anti-malware-dashboard) | Provides a summary of PCI assets and active threats for better visibility and control.  
[Network](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#network-dashboard) | Provides insights into network performance, activity, and traffic trends.  
[Alert overview](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#alert-overview-dashboard) | Lets you monitor, manage, and respond to security events.  
[Identity and access](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#identity-and-access-dashboard) | Provides a real-time overview of Identity and Access Management activity, including key metrics like user access permissions, password changes, and authentication events.  
[Monitoring and testing](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#monitoring-and-testing-dashboard) | Lets you monitor key activities and events, including critical incidents, failed events, and administrative access.  
[Vulnerability management](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#vulnerability-management-dashboard) | Lets you monitor and track vulnerabilities in network systems.  
[Patch management](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#patch-management-dashboard) | Provides a summary of the patch management lifecycle to monitor and manage system updates for security and efficiency.  
[Secure configurations](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#secure-configurations-dashboard) | Provides real-time monitoring and tracking of key metrics to identify and mitigate potential risks by maintaining critical configurations.  
[Data encryption](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#data-encryption-dashboard) | Provides a high-level summary of data encryption activity and key management practices, including a number of key operations, deletions, and decryption results.  
[EDR alert overview](https://docs.cloud.google.com/chronicle/docs/reports/pci-curated-dashboards#edr-alert-overview-dashboard) | Provides summary of overall EDR activity and the number of events and alerts.  
  
## Anti-malware dashboard

The Anti-malware dashboard provides an overview of PCI assets and active threat detections for enhanced visibility and control. This dashboard displays the number of active Endpoint Detection and Response (EDR) sensors for device compliance. It also categorizes alerts and events by severity, including allowed and blocked detections, using the `PCI_Assets` reference list.

## Network dashboard

The Network dashboard provides insights into network performance, activity, and traffic trends, helping you understand network behavior, maintain security, and monitor PCI Data Security Standards (DSS) compliance. It provides a comprehensive overview of network activity and events, with filtering options to refine data analysis by time period and data source. This dashboard uses the `PCI_Network_Ranges` reference list.

## Alert overview dashboard

The Alert overview dashboard lets you monitor, manage, and respond to security events, helping you monitor PCI DSS compliance for safeguarding cardholder data. It provides a real-time, consolidated view of alerts and insights into potential security breaches and PCI-related events. This dashboard uses the `PCI_Assets` reference list.

## Identity and access dashboard

The Identity and access dashboard protects cardholder data and simplifies compliance reporting. It provides a real-time overview of Identity and Access Management activity, including key metrics like user access permissions, password changes, and authentication events. This ensures access to sensitive data and network resources aligns with PCI DSS standards. This dashboard uses the `PCI_Assets` reference list.

## Monitoring and testing dashboard

The Monitoring and testing dashboard lets you monitor key activities and events, including critical incidents, failed events, and administrative access. The dashboard also helps monitor account activity and highlights metrics like audit policy changes and top access by source to manage threats, providing insights into failed events and audit policy changes. This dashboard uses the `PCI_Assets` reference list.

## Vulnerability management dashboard

The Vulnerability management dashboard helps you monitor and track vulnerabilities in network systems. It provides real-time monitoring, facilitates regular tracking, streamlines compliance reporting, and identifies, assesses, and manages vulnerabilities to maintain secure payment environments. This dashboard uses the `PCI_Assets` and `PCI_Network_Ranges` reference lists.

## Patch management dashboard

The Patch management dashboard provides an overview of the patch management lifecycle, helping you monitor and manage system updates for security and efficiency. It lets you track successful and failed installations, monitor download statuses, and identify systems with missed or available updates. This dashboard uses the `Patch_Updates` and `PCI_Assets` reference lists.

## Secure configurations dashboard

The Secure configurations dashboard displays real-time monitoring and tracking of key metrics, helping identify and mitigate potential risks by maintaining critical configurations. It provides insights into trends, patterns, and potential gaps, letting you manage configurations from initiation through enforcement. The dashboard proactively tracks policy changes, failed logins, and default account usage to identify weaknesses. It also sends real-time alerts for critical updates, policy changes, and failed logins, letting you take quick action on issues like failed updates or unauthorized login attempts. This dashboard uses the `PCI_Assets` and `Default_Users` reference lists.

## Data encryption dashboard

The Data encryption dashboard helps you secure sensitive data, identify vulnerabilities, and maintain PCI compliance through real-time and historical analysis of data encryption. It provides a high-level summary of data encryption activity and key management practices, including a number of key operations, deletions, and decryption results. The dashboard distinguishes between secure and potentially vulnerable encryption practices. This dashboard uses the `PCI_Network_Ranges` reference list.

## EDR alert overview dashboard

The EDR alert overview dashboard provides security teams with a complete picture of assets, events, and active threat detections, enabling them to quickly detect, investigate, and respond to potential threats. It summarizes overall EDR activity and the number of events and alerts. It prioritizes investigations by sorting alerts and events by severity and listing the top ten alerts, hosts, techniques, and tactics. It also helps evaluate the effectiveness of the EDR solution. This dashboard uses the `PCI_Assets` the reference list.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
