---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections/
title: Test connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:09.813797+00:00
---

# Test connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Test connections Stay organized with collections  Save and categorize content based on your preferences. 

Before you can use your Dedicated Interconnect connections, Google must verify that your connections to Google's edge network are working. To do this, Google sends you an IP address configuration that you must apply to your on-premises router. This configuration differs depending on whether you order one circuit or more than one circuit.

The following sections describe two different testing procedures. The first is for a single-circuit connection and the second is for a multi-circuit connection.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Dedicated Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

## Test a single-circuit connection

  1. Google polls its edge device every 24 hours, checking for light on the port to your on-premises router. Receiving light indicates that your connection has been installed. After detecting this light, Google sends you an email containing an IP address that Google uses to ping your on-premises router to test the circuit.
  2. Configure the interface of your on-premises router with the correct link-local IP address and configure LACP on that interface. Even though there is only one circuit in your Dedicated Interconnect connection, you must still use LACP.

The following example shows an IP address configuration similar to the one that Google sends you for the test. Replace these values with the values that Google sends you for your network.

Google's link-local IP address | Your router's link-local IP address | Subnet size  
---|---|---  
169.254.0.1 | 169.254.0.2 | /30  
  3. Apply the test IP address that Google sends you to the interface of your on-premises router that connects to Google. For testing, you must configure this interface in _access mode_ with no VLAN tagging. For a sample configuration, see [Configure on-premises routers for testing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#testing).

  4. Google tests your connection by pinging the link-local IP address with LACP enabled. Google tests once, 30 minutes after detecting light, and then every 1 hour thereafter.

     * After a successful test, Google sends you an email notifying you that your connection is ready to use.
     * If a test fails, Google automatically retests the connection once an hour for 30 days.



To fix issues, see the guidance for single-link bundles in the [Troubleshooting guide](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cant-ping-during-connection-provisioning).

## Test a multi-circuit connection

When you order a Dedicated Interconnect connection that has multiple circuits, Google performs ping tests on the final bundled connection with LACP enabled.

### Ping test

  1. Google polls its edge device every 24 hours, checking for light on the port to your on-premises router. Receiving light indicates that your connections have been installed. After detecting this light, Google sends you an email with instructions for the ping test.

  2. On your on-premises router, configure all the circuits into a bundle with LACP enabled and configure the IP address on the bundled interface.

The following example shows an IP address configuration similar to the one that Google sends you for the test. Replace these values with the values that Google sends you for your network.

Google's link-local IP address | Your router's link-local IP address | Subnet size  
---|---|---  
169.254.0.1 | 169.254.0.2 | /30  
  3. Apply the test IP address that Google sends you to the bundled interface of your on-premises router that connects to Google. For testing, you must configure this interface in _access mode_ with no VLAN tagging. For a sample configuration, see [Configure on-premises routers for testing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#testing).

  4. Google tests each connection once every 1 hour. After a successful test, Google notifies you that your connection is ready to use.




To fix issues, see the guidance for multiple-link bundles in the [Troubleshooting guide](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cant-ping-during-connection-provisioning).

## Use your Dedicated Interconnect connection

After all tests have passed, your Dedicated Interconnect connection is ready to use, and Google starts billing for it. To view the status of your connection, see [View connection details](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-interconnects).

At this stage, remove the test IP addresses from the interface or interfaces on your on-premises router. To reconfigure your router for production, see [Configure on-premises routers for production](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers#production).

Your connection can now carry traffic, but it isn't associated with any Google Virtual Private Cloud (VPC) networks.

**Note:** When you configure VLAN attachments on your on-premises router, the subnet size is different than when you configure a Dedicated Interconnect connection for a test. Make sure that you specify the correct subnet size, depending on what you're configuring. Google provides these values when you order a connection or create a VLAN attachment.

## Use the Cloud Interconnect diagnostics tool

To understand the status and health of your Dedicated Interconnect connection, we recommend that you use the Cloud Interconnect diagnostics tool. See [Get diagnostics](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/getting-diagnostics) for more information.

[ Previous arrow_back  Retrieve LOA-CFAs  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/retrieving-loas)

[ Next Create VLAN attachments  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
