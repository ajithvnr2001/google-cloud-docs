---
url: https://docs.cloud.google.com/chronicle/docs/detection/applied-threat-intel-overview/
title: Applied Threat Intelligence overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:16.472297+00:00
---

# Applied Threat Intelligence overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/applied-threat-intel-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Applied Threat Intelligence overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Applied Threat Intelligence (ATI) helps you identify and respond to threats. It continually analyzes and evaluates your security telemetry against Indicators of Compromise (IoCs) curated by Google Threat Intelligence.

When ATI is enabled, Google SecOps ingests IoCs curated by Google Threat Intelligence that are classified as malicious by the Google Threat Indicator (GTI) verdict. When a match is found, an alert is generated. You can then investigate the IoC on the **IoC matches** page, which displays possible IoC matches for domains, IP addresses, file hashes, and URLs. Information about the IoC is displayed, including the following:

  * GCTI priority
  * GTI verdict
  * Associations
  * Campaigns



You can also view detailed information about the events that triggered the IoC match, information from the threat intelligence source, and the rationale for the GTI score. For more information about IoCs, see [View IoCs using Applied Threat Intelligence](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page). For more information about Google Threat Intelligence verdicts, see [What is a verdict](https://gtidocs.virustotal.com/docs/google-threat-intelligence-indicator-score#what-is-a-verdict-confidence-of-maliciousness).

**Important:** Applied Threat Intelligence in Google SecOps is available with a Google SecOps Enterprise Plus license.

Google SecOps curated detections evaluate your event data against Google Threat Intelligence data, and generate an alert when one or more rules identify a match to an IoC with an active breach or high priority. In addition, ATI includes [composite rules](https://docs.cloud.google.com/chronicle/docs/detection/composite-rules-category#ati_composite_rules) that correlate multiple ATI alerts into a single, high-fidelity alert when a campaign, malware, or threat actor is identified.

For Google SecOps Enterprise Plus instances, Applied Threat Intelligence curated detection rule sets are enabled by default. To use and manage this feature:

  1. **Verify settings** : You can review or customize the Status and Alerting configuration for these [curated detection rule sets](https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections) on the Curated Detections page.
  2. **Investigate alerts** : Use the [IOC matches](https://docs.cloud.google.com/chronicle/docs/detection/ati-view-ioc-page) page to prioritize and respond to threats.



You can also learn more about how the IC-Score is assigned in the [IC-Score overview](https://docs.cloud.google.com/chronicle/docs/detection/understand-ic-score).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
