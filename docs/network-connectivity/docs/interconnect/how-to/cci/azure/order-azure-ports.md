---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports/
title: Order Microsoft Azure ports \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:43.641630+00:00
---

# Order Microsoft Azure ports  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Order Microsoft Azure ports Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides sample guidance. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For detailed instructions, see the [Azure documentation](https://learn.microsoft.com/azure/?product=networking) . 

After you order your Cross-Cloud Interconnect connections, order your Microsoft Azure ports.

## Before you begin

If you haven't already done so, register the ExpressRoute Direct feature.

###  Azure portal 

**Note:** For the most up-to-date information about how to register the ExpressRoute feature, see the [Azure documentation](https://learn.microsoft.com/azure/expressroute/how-to-expressroute-direct-portal).

  1. Sign in to the Azure portal and select the appropriate subscription.
  2. In the navigation, find the **Settings** menu, and then click **Preview features**.
  3. In the search box, enter **ExpressRoute**.
  4. Select the **Allow ExpressRoute Direct** checkbox.
  5. At the top of the page, click the **+Register** button.
  6. In the table, locate **Allow ExpressRoute Direct** again. Make sure that the corresponding value in the **State** column is **Registered**.



###  Azure PowerShell 

**Note:** For the most up-to-date information about how to register the ExpressRoute feature, see the [Azure documentation](https://learn.microsoft.com/azure/expressroute/expressroute-howto-erdirect).

Use the [`Register-AzProviderFeature` command](https://learn.microsoft.com/powershell/module/az.resources/register-azproviderfeature?view=azps-8.2.0):
    
    
    Register-AzProviderFeature -FeatureName `
    AllowExpressRoutePorts -ProviderNamespace Microsoft.Network

## Create ExpressRoute Direct resources

For each of your Cross-Cloud Interconnect connections, you need an Azure port. To order a pair of Azure ports, create an ExpressRoute Direct resource.

When you create an ExpressRoute Direct resource, Azure automatically reserves a primary and secondary redundant port for you. This behavior differs from the Cross-Cloud Interconnect ordering process, which requires you to explicitly order two connections.

###  Azure portal 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Create ExpressRoute Direct](https://learn.microsoft.com/azure/expressroute/how-to-expressroute-direct-portal#create-erdir) in the Azure documentation.

  1. Go to the **ExpressRoute Direct** page.

  2. Click **Create**.

  3. Fill out the **Basics** tab of the **Create ExpressRoute Direct** page:

     * Select the **Subscription** where you want to create the resource. Later, when you create an ExpressRoute circuit, you must create it in the same subscription as the ExpressRoute Direct resource.
     * Select the **Resource group** where you want to place the ExpressRoute Direct resource.
     * Identify the **Region** where you want to locate the resource.
     * Enter a **Name** for the resource.

For the most up-to-date information about these fields, see [Azure documentation](https://learn.microsoft.com/azure/expressroute/how-to-expressroute-direct-portal#create-erdir).

  4. Click **Next : Configuration**.

  5. On the **Configuration** tab, enter values for the following fields:

     * In the **Peering location** field, enter the Azure location. If you need help with choosing a value for this field, see [Choose your locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/choose-locations).
     * Choose the appropriate **Bandwidth**. To view the list of valid capacities, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#port-capacity).
     * For **Encapsulation** , select **Dot1Q**.
**Important:** Google Cloud is incompatible with QinQ encapsulation, and you can't change this setting later.
  6. Click **Next : Tags**.

  7. Optional: Set up tags for this port.

  8. Click **Next : Review + create**.

  9. Review the summary of your choices. If you want to make changes, click **Previous** and update the form as needed. When the summary looks correct, click **Create**.

Azure displays a **Deployment is in progress** message. After some time, the message should update to say **Your deployment is complete**.

  10. Click the name of your new ExpressRoute Direct resource. You should see a **Links** table that lists **Link1** and **Link2**. These links represent your primary and secondary ports.




Do not enable the ports yet. Billing begins when you enable the ports.

###  Azure PowerShell 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Create the resource](https://learn.microsoft.com/azure/expressroute/expressroute-howto-erdirect#resources) in the Azure documentation.

Use the [`New-AzExpressRoutePort` command](https://learn.microsoft.com/powershell/module/az.network/new-azexpressrouteport?view=azps-8.2.0):
    
    
    New-AzExpressRoutePort -Name NAME `
       -ResourceGroupName RESOURCE_GROUP `
       -PeeringLocation PEERING_LOCATION `
       -BandwidthInGbps BANDWIDTH `
       -Encapsulation Dot1Q `
       -Location LOCATION

Replace the following:

  * `NAME`: the name of the new connection
  * `RESOURCE_GROUP`: the appropriate resource group
  * `PEERING_LOCATION`: the name of the location as it is represented in Azure—for example, `Interxion-Frankfurt-FRA11`
  * `BANDWIDTH`: the bandwidth in Gbps. To view the list of valid capacities, see [Port capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#port-capacity).
  * `LOCATION`: the name of the region



## Generate an LOA

For Google to provision your connection, it must have a letter of authorization (LOA) for your Azure port.

###  Azure portal 

**Note:** For the most up-to-date information about how to retrieve the LOA, see [Generate the letter of authorization](https://learn.microsoft.com/azure/expressroute/how-to-expressroute-direct-portal#authorization) in the Azure documentation.

  1. Go to the page that lists ExpressRoute Direct resources.
  2. Click the name of the connection that you created.
  3. For **Company Name** , enter **Google**.
  4. Click **Generate Letter of Authorization**.



###  Azure PowerShell 

**Note:** For the most up-to-date information about how to retrieve the LOA, see [Generate the letter of authorization](https://learn.microsoft.com/azure/expressroute/expressroute-howto-erdirect#authorization) in the Azure documentation.

Use the [`Get-AzExpressRoutePort` command](https://learn.microsoft.com/powershell/module/az.network/get-azexpressrouteport?view=azps-8.2.0) and the [`New-AzExpressRoutePortLOA` command](https://learn.microsoft.com/powershell/module/az.network/new-azexpressrouteportloa?view=azps-8.2.0):
    
    
    $port = Get-AzExpressRoutePort -Name CONNECTION_NAME; `
       New-AzExpressRoutePortLOA -ExpressRoutePort `
       $port -CustomerName "GoogleCloud" -Destination "PATH"

Replace the following:

  * `CONNECTION_NAME`: the name of the ExpressRoute Direct resource that you created in the previous step

  * `PATH`: the location where you want to download the LOA




## Send the LOA to Google

After you order your Cross-Cloud Interconnect connections, you should receive confirmation email messages from Google. Each of these messages includes instructions for how to send your Azure LOA to Google. Now that you have the LOA, follow the instructions to provide the document.

To summarize, you must provide both of the following:

  * The LOA document

  * Instructions for how you want your ports connected. For example, specify whether you want your primary Cross-Cloud Interconnect port connected to your primary or secondary ExpressRoute Direct port.




Make a note of the instructions that you provide to Google. You need this information later in the process when you configure your ExpressRoute circuits.

## Look for an email from Google

After you provide your LOA, Google can provision your Cross-Cloud Interconnect connections. When your connections are _provisioned_ , Google has physically connected the two ports.

After the connections are provisioned, you receive an email that does the following:

  * Lets you know that your ports are ready to use.
  * Instructs you to enable your Azure ports and then confirm that you have done so.



After you get the email, complete the steps described in the following sections.

## Check for a signal from Google

Check to see whether both Azure ports are receiving a signal from Google Cloud. If either of your ports is not receiving light, report the issue to Google before proceeding.

###  Azure PowerShell 

**Note:** For the most up-to-date information about how to check light levels, see [ExpressRoute Direct Metrics](https://learn.microsoft.com/azure/expressroute/expressroute-monitoring-metrics-alerts#expressroute-direct-metrics) in the Azure documentation.

Use the [`Get-AzExpressRoutePort` command](https://learn.microsoft.com/powershell/module/az.network/get-azexpressrouteport?view=azps-9.5.0) and the [`Get-AzMetric` command](https://learn.microsoft.com/powershell/module/az.monitor/get-azmetric?view=azps-9.5.0):
    
    
    $port = Get-AzExpressRoutePort -Name EXPRESS_ROUTE_DIRECT_NAME -ResourceGroupName RESOURCE_GROUP
    $metricLink1 = Get-AzMetric -ResourceId $port.id -DetailedOutput -MetricName "RxLightLevel" -MetricFilter "Link eq 'link1'"
    $metricLink2 = Get-AzMetric -ResourceId $port.id -DetailedOutput -MetricName "RxLightLevel" -MetricFilter "Link eq 'link2'"
    $metricLink1.Data[-1], $metricLink2.Data[-1]

Replace the following:

  * `EXPRESS_ROUTE_DIRECT_NAME`: the name of your ExpressRoute Direct resource
  * `RESOURCE_GROUP`: the appropriate resource group



You should see output similar to the following. Ideally, the value in the `Average` field is between `-10` and `0`.
    
    
    TimeStamp : 3/22/2023 8:54:00 PM
    Average   : -3.54
    Minimum   :
    Maximum   :
    Total     :
    Count     :
    
    TimeStamp : 3/22/2023 8:54:00 PM
    Average   : -4.17
    Minimum   :
    Maximum   :
    Total     :
    Count     : 

## Enable the Azure ports

To permit connectivity, enable your primary and secondary ExpressRoute Direct connections.

**Important:** After you enable your connections, billing begins. For more information, see the [ExpressRoute FAQ](https://learn.microsoft.com/azure/expressroute/expressroute-faqs#when-does-billing-start-and-stop-for-the-expressroute-direct-port-pairs).

###  Azure portal 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Change Admin State of links](https://learn.microsoft.com/azure/expressroute/how-to-expressroute-direct-portal#state) in the Azure documentation.

  1. Go to the **ExpressRoute Direct** page.

  2. Click the name of your ExpressRoute Direct resource. The page that is displayed lists two links: one for your primary connection and one for your secondary connection.

  3. Enable the primary connection:

     1. Click **Link 1**.
     2. Click the **Enabled** toggle.
     3. Click **Save**.
  4. Enable the secondary connection:

     1. Click **Link 2**.
     2. Click the **Enabled** toggle.
     3. Click **Save**.



###  Azure PowerShell 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Change Admin State of links](https://learn.microsoft.com/azure/expressroute/expressroute-howto-erdirect#state) in the Azure documentation.

  1. Fetch information about the ExpressRoute Direct port pair by using the [`Get-AzExpressRoutePort` command](https://learn.microsoft.com/powershell/module/az.network/get-azexpressrouteport?view=azps-8.2.0):
         
         Azure> $port = Get-AzExpressRoutePort -Name EXPRESS_ROUTE_DIRECT_CONNECTION

Replace `CONNECTION_NAME` with the name of your ExpressRoute Direct resource.

  2. Define an enabled state for the primary port:
         
         $port.Links[0].AdminState = "Enabled"

  3. Define an enabled state for the secondary port:
         
         $port.Links[1].AdminState = "Enabled"

  4. Update both ports by using the [`Set-AzExpressRoutePort` command](https://learn.microsoft.com/powershell/module/az.network/set-azexpressrouteport?view=azps-8.2.0):
         
         $port = Set-AzExpressRoutePort -ExpressRoutePort $port




## Respond to the Google email

After you enable your Azure ports, respond to the email that you received from Google and let us know that you enabled your ports.

After we receive your response, within 24 hours, you should be able to confirm that your Cross-Cloud Interconnect ports are [receiving a signal from Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources#check-for-a-signal-from-azure).

[ Previous arrow_back  Order Cross-Cloud Interconnect connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-google-connections)

[ Next Configure your Google Cloud resources  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
