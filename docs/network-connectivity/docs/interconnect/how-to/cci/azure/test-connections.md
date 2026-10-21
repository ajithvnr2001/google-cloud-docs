---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/test-connections/
title: Verify your connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:08.185452+00:00
---

# Verify your connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/test-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Verify your connections Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page includes instructions about Azure products. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For the most current information, refer to the [Azure documentation](https://learn.microsoft.com/azure/?product=networking).

To check connectivity between your Google Cloud and Azure networks, complete the following tasks. By verifying these connections, you confirm proper setup and can troubleshoot any connectivity issues, ensuring reliable hybrid cloud operations.

## Check for a signal from Azure

In Google Cloud, check to see whether your Cross-Cloud Interconnect port is receiving a signal from the ExpressRoute Direct port. 

### Console

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** page. 

[Go to **Physical connections**](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click the name of your primary Cross-Cloud Interconnect connection.
  3. On the **Interconnect details** page, locate the **Link circuit info** table. Check the **Receiving Optical Power** column. This column indicates whether the Cross-Cloud Interconnect connection is receiving input from the Azure port. The value in this column should be **OK**. 
  4. Repeat the preceding steps for your redundant Cross-Cloud Interconnect connection.



If the status of either connection is not receiving a signal, double-check that you enabled the corresponding Azure port, as described in [Enable the ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports#enable-ports).

## Check the route table

To verify that Azure has learned your Google Cloud routes, view the route table for your ExpressRoute circuit.

###  Azure PowerShell 

Use the [`Get-AzExpressRouteCircuitRouteTable` command](https://learn.microsoft.com/powershell/module/az.network/get-azexpressroutecircuitroutetable?view=azps-8.2.0):
    
    
    Get-AzExpressRouteCircuitRouteTable -DevicePath DEVICE_PATH `
       -ExpressRouteCircuitName CIRCUIT_NAME `
       -PeeringType AzurePrivatePeering `
       -ResourceGroupName RESOURCE_GROUP
    

Replace the following:

  * `DEVICE_PATH`: to check the primary circuit, use `primary`; to check the secondary circuit, use `secondary`
  * `CIRCUIT_NAME`: the name of your ExpressRoute circuit
  * `RESOURCE_GROUP`: the resource group associated with the circuit



If you don't see the results that you expect, review the [private peering you created](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-azure#set-up-private-peering) for your ExpressRoute circuit. Try reversing the values for **IPv4 Primary subnet** and **IPv4 Secondary subnet** , and then check the route table again.

## Review the Troubleshooting page

For additional guidance, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

[ Previous arrow_back  Configure your Azure resources  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-azure)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
