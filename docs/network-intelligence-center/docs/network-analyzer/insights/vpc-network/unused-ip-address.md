---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/unused-ip-address/
title: Unused IP address insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:17.300487+00:00
---

# Unused IP address insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/unused-ip-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Unused IP address insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for unused IP addresses. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

## View insights in the Recommender API

To view these insights in the gcloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.vpcnetwork.ipAddressInsight`



You need the following permissions:

  * `recommender.networkAnalyzerIpAddressInsights.list`
  * `recommender.networkAnalyzerIpAddressInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## Unassigned external IP addresses

This insight shows the external IP addresses of your project that have not been assigned for at least 24 hours.

This insight includes the following information:

  * **Reserved:** The total number of reserved external IP addresses.
  * **Unassigned:** The number of external IP addresses that are not assigned.
  * **Unassigned ratio:** The percentage of external IP addresses that are not assigned.



The insight also includes a table that lists the number of unassigned external IP addresses for each region.

### Recommendations

To find all unassigned external IP addresses, go to the [external IP addresses](https://console.cloud.google.com/networking/addresses/list) page in the Google Cloud console and use the **In use by:""** filter.

For more information about releasing the unused static external IP addresses, see [Release a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
