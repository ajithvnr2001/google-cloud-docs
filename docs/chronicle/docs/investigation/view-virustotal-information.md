---
url: https://docs.cloud.google.com/chronicle/docs/investigation/view-virustotal-information/
title: View VirusTotal information \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:08.226758+00:00
---

# View VirusTotal information  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/investigation/view-virustotal-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View VirusTotal information 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Use Google Security Operations's integration with [VirusTotal](https://www.virustotal.com/gui/) to pivot from finding domains linked to an asset in Google SecOps to viewing information about that domain from VirusTotal and launching VirusTotal Graph.

VirusTotal Graph is a visualization tool built on top of the VirusTotal dataset. It analyzes the relationship between files, URLs, domains, IP addresses, and other items encountered. VirusTotal Graph helps to illustrate the interconnections between potentially malicious domains and the assets within your enterprise.

**Note:** Some of the VirusTotal information is only available with a VirusTotal Enterprise account.

To view the VirusTotal Context for a domain, complete the following steps:

**Note:** The same steps apply for IP address and file or hash views.

  1. Search for a suspicious domain in Google SecOps. Select the domain in the search results to open Domain view.

  2. Click **VT CONTEXT** at the top of Domain view to open the VT Context window. The numbers next to **VT CONTEXT** indicate the number of security vendors that have flagged this domain as malicious.

**Domain view with VT CONTEXT option**

  3. The VT Context window opens to the **Detections** tab. This tab displays more information from VirusTotal with regards to what is known about this domain, for example, whether or not the domain is malicious.

![Detections tab](https://docs.cloud.google.com/chronicle/images/vt-context-detections.png)

**Detections tab**

  4. Click the **IoCs** tab to view any of the IoCs VirusTotal has in its database for this domain. To view the VirusTotal IoCs, you must be signed you must have a VirusTotal Enterprise account. Enter your VirusTotal login credentials when asked.

![IoCs tab](https://docs.cloud.google.com/chronicle/images/vt-context-iocs.png)

**IoCs tab**

  5. Click the **Graph** tab to open the control to launch VirusTotal Graph. To use VirusTotal Graph, you must have a VirusTotal Enterprise account. Enter your VirusTotal login credentials when asked.

![VirusTotal Graph](https://docs.cloud.google.com/chronicle/images/virustotal-graph.png)

**VirusTotal Graph**




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
