---
url: https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging/
title: Export logs to Cloud Logging \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:48.334872+00:00
---

# Export logs to Cloud Logging  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Export logs to Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center lets you export Event Threat Detection and Container Threat Detection findings to [Logging](https://docs.cloud.google.com/logging/docs/overview). This task helps you centralize security telemetry and configure log-based alerts.

Exporting findings requires [activating Security Command Center at the organization level](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#org-level-activation) using the Premium or Enterprise tier. Ingestion and storage costs depend on finding volume. To manage expenses, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

Depending on the quantity of information, Cloud Logging costs can be significant. To understand your usage of the service and its cost, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). 

To configure export, do the following:

  1. In the Google Cloud console, go to Security Command Center.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/config/services)

  2. Select your organization.

  3. Click **settings Settings**.

  4. Click the **Continuous Exports** tab.

  5. In **Export name** , click **Logging Export**.

  6. In **Sinks** , turn on ![](https://docs.cloud.google.com/static/security-command-center/images/toggle-on.png)**Log findings to Logging**.

  7. In **Logging project** , enter or search for the project where you want to log findings.

  8. Click **Save**.




When Event Threat Detection and Container Threat Detection write logs, each log entry includes the `threat_detector` resource type and contains the same information as findings. For instructions on reviewing logs, see [Using Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection#findings-logging) or [Using Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection#findings-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
