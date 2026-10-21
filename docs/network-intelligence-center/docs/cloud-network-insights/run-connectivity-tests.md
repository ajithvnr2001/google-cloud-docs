---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/run-connectivity-tests/
title: Run Connectivity Tests \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:23:24.901721+00:00
---

# Run Connectivity Tests  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/run-connectivity-tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Run Connectivity Tests Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to validate connectivity between endpoints of a dual-ended network path if the following conditions are met:

  * The source (host) or the destination (target) Monitoring Point is in Google Cloud.
  * The destination is an IP address.

**Note:** Connectivity Tests validates the Google Cloud configuration, which is static. However, network paths are dynamic and can change how they map the source to the destination. These changes can lead to situations where Connectivity Tests has a different result than the metrics reported in Cloud Network Insights, because the networking configuration in Google Cloud is correct but a setting on the destination endpoint is preventing the Cloud Network Insights tests from completing successfully.

When you run a test, the following attributes are used in the test definition:

  * Protocol
  * Source instance
  * Destination IP
  * Destination port



You can change the protocol and destination port for Connectivity Tests in Cloud Network Insights. These changes are not saved and must be re-entered when you run the test again.

## Before you begin

  * Verify that you have sufficient [permissions](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control#networkmanagement-permissions) to run Connectivity Tests.



## Run Connectivity Tests

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights** > **Monitoring Points**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights/monitoring-points)

  2. Click **Network Paths**.

  3. Find the network path with an endpoint in Google Cloud that you want to test. Click **Run** under the **Connectivity Test** column.

If this option is not available, the network path is not in Google Cloud.




The results of the connectivity test are displayed in the **Connectivity test result** panel.

Expand steps in the configuration analysis trace for more detailed information about the results.

For more information about Connectivity Tests, see [Connectivity Tests components](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/reachability#test-components).

You can run the test again or change the protocol or destination port.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
