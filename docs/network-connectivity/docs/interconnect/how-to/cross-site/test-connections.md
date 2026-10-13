---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections/
title: Test connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:02.477151+00:00
---

# Test connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Test connections Stay organized with collections  Save and categorize content based on your preferences. 

Before you can use your Cross-Site Interconnect connections, Google must verify that your connections to Google's edge network are working. To do this, Google sends you an IP address configuration that you must apply to your on-premises routers.

The test described on this page helps you ensure that your connection is successfully installed and connects the Cross-Site Interconnect port to your on-premises router port.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

## Test a connection

  1. Google polls its edge device every 24 hours, checking for light on the port to your on-premises router. Receiving light indicates that your connection is installed. After detecting this light, Google sends you an email containing a link-local IP address that Google uses to ping your on-premises router to test the circuit.
  2. Configure the interface of your on-premises router with the correct link-local IP address.

The following example shows an IP address configuration similar to the one that Google sends you for the test. Replace these values with the values that Google sends you for your network.

Google's link-local IP address | Your router's link-local IP address | Subnet size  
---|---|---  
169.254.0.1 | 169.254.0.2 | /30  
  3. Apply the test IP address that Google sends you to the interface of your on-premises router that connects to Google. For testing, you must configure this interface in _access mode_ with no VLAN tagging.

  4. Google tests your connection by pinging the link-local IP address. Google tests once, 30 minutes after detecting light, and then every 1 hour thereafter.

     * After a successful test, Google sends you an email notifying you that your connection is ready to use.
     * If a test fails, Google automatically retests the connection once an hour for 30 days.



## Use your Cross-Site Interconnect connection

After all tests have passed, your Cross-Site Interconnect connection is ready to use, and Google starts billing for it. To view the status of your connection, see [View connection details](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/view-connections).

At this stage, remove the test IP addresses from the interface or interfaces on your on-premises routers. To reconfigure your router for production, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/configure-onprem-routers).

Your connection can now carry traffic, and you can create your cross-site networks.

[ Previous arrow_back  Retrieve LOA-CFAs  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/retrieve-loas)

[ Next Create a cross-site network  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/create-network)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
