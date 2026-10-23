---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-azure/
title: Configure your Microsoft Azure resources \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:47.627765+00:00
---

# Configure your Microsoft Azure resources  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure your Microsoft Azure resources Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides sample guidance. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For detailed instructions, see the [Azure documentation](https://learn.microsoft.com/azure/?product=networking) . 

To finalize your direct physical connection between Google Cloud and Microsoft Azure, configure your Azure resources.

Before you proceed, make sure you've already configured your [Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources).

## Before you begin

This section describes required setup and resources.

### Provisioned Cross-Cloud Interconnect connections

Before you configure your Azure resources, make sure that Google has provisioned your Cross-Cloud Interconnect connections. After this work is complete, you receive a confirmation email. You can also use the Google Cloud console to verify that the Cross-Cloud Interconnect ports are active, which indicates that the connections have been provisioned. For more information, see [Verify that your port is active](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources#provisioned-connections).

### Required Azure resources

Make sure that you have an Azure virtual network (VNet) that includes a subnet. The subnet must be located in an [Azure region that is supported for your location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/choose-locations#supported-locations). For help, see [Quickstart: Use the Azure portal to create a virtual network](https://learn.microsoft.com/azure/virtual-network/quick-create-portal).

## Create an ExpressRoute circuit

An Azure ExpressRoute circuit is similar to a Google Cloud VLAN attachment. The circuit represents a logical connection between your network in Azure and your peer network (in this case, Google Cloud).

When you create an ExpressRoute circuit, Azure automatically creates two circuits: a primary circuit and a redundant one. Azure creates one circuit on your primary ExpressRoute Direct resource and another on your secondary ExpressRoute Direct resource. This behavior differs from Google Cloud, where you had to explicitly create two VLAN attachments.

###  Azure portal 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Create a circuit](https://learn.microsoft.com/azure/expressroute/how-to-expressroute-direct-portal#circuit) in the Azure documentation.

  1. Go the **ExpressRoute Circuits** page.

  2. Click **Create**.

  3. Complete the form displayed on the **Basics** tab:

     * Select a **Subscription** and **Resource group**.
     * Select the **Region** where you [created your ExpressRoute Direct resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports#order-connections).
     * Enter a **Name** for the circuit.
  4. Click **Next : Configuration**.

  5. Complete the form displayed on the **Configuration** tab:

     * In the **Peering type** field, select **Direct**.
     * Select the **ExpressRoute Direct** resource that you created in [Order Azure connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports#order-connections). If you can't find the name of your connection in the drop-down list, go back to the previous page and make sure that you selected the correct region.
     * Use the **Circuit bandwidth** field to select the appropriate capacity.
     * Use the **SKU** field to select the appropriate level of service.
**Important:** The value that you select for **SKU** affects the price of the circuit. For help with making a choice, see [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/).
  6. Click **Next : Tags**.

  7. Optional: Set up tags for this port.

  8. Click **Next : Review + create**.

  9. Review the summary of your choices. If you want to make changes, click **Previous** and update the form as needed. When the summary looks correct, click **Create**.

Azure displays a **Deployment is in progress** message. After some time, the message should update to say **Your deployment is complete**.




###  Azure PowerShell 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Create a circuit](https://learn.microsoft.com/azure/expressroute/expressroute-howto-erdirect#circuit) in the Azure documentation.

Use the [`New-AzExpressRouteCircuit` command](https://learn.microsoft.com/powershell/module/az.network/new-azexpressroutecircuit?view=azps-8.2.0):
    
    
    $port = Get-AzExpressRoutePort -Name EXPRESS_ROUTE_DIRECT_CONNECTION `
    $circuit = New-AzExpressRouteCircuit `
       -Name NAME `
       -ResourceGroupName RESOURCE_GROUP_NAME `
       -Location LOCATION `
       -SkuTier SKU_TIER `
       -SkuFamily SKU_FAMILY `
       -ExpressRoutePort $port `
       -BandwidthInGbps CAPACITY

Replace the following:

  * `EXPRESS_ROUTE_DIRECT_CONNECTION`: the name of the ExpressRoute Direct connection that you created in [Order Azure ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports)
  * `NAME`: the name of the new circuit
  * `RESOURCE_GROUP_NAME`: the name of the appropriate resource group
  * `LOCATION`: the region where you created the ExpressRoute Direct connection, as described in [Order Azure ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports)
  * `SKU_TIER`: the SKU tier; possible values are `Standard`, `Premium`, and `Local`

**Important:** The value that you select for **SKU** affects the price of the circuit. For help making a choice, see [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/).
  * `SKU_FAMILY`: if you're using `LOCAL` for `SKU`, choose `UnlimitedData`; if you're using `STANDARD` or `PREMIUM`, choose `MeteredData`

  * `CAPACITY`: the capacity of each circuit




## Set up a private peering

Cross-Cloud Interconnect uses Border Gateway Protocol (BGP) to exchange routes between your Virtual Private Cloud (VPC) network and your Azure network. To that end, configure a private BGP peering between your ExpressRoute circuits and your Google Cloud VLAN attachments.

### Calculate the IPv4 subnet values

When you create the peering, you provide an **IPv4 primary subnet** value and an **IPv4 secondary subnet** value. These values represent the Google Cloud VLAN attachments that you want to connect with.

#### Check the instructions that you provided

When you provided your Azure LOA to Google, you also provided instructions about how you wanted your ports connected. You need that information to configure the **IPv4 Primary subnet** and **IPv4 Secondary subnet** fields.

For example, if your _primary_ ExpressRoute Direct port is connected to the _primary_ Cross-Cloud Interconnect port, do the following:

  * To calculate the **IPv4 Primary subnet** value, use details about the primary VLAN attachment.

  * To calculate the **IPv4 Secondary subnet** value, use details about the redundant VLAN attachment.




If your primary ExpressRoute Direct port is connected to the _redundant_ Cross-Cloud Interconnect port, do the reverse. That is, to calculate the **IPv4 Secondary subnet** value, use details about the primary VLAN attachment. To calculate the **IPv4 Primary subnet** value, use details about the redundant VLAN attachment.

#### Calculate the subnet values

To calculate the subnet value, start with the `customerRouterIpAddress` value of the appropriate VLAN attachment. Subtract 2 from the rightmost segment of the address (the fourth octet). The resulting value is the address that you enter in the **IPv4 Primary subnet** field or in the **IPv4 Secondary subnet** field.

For example, suppose the `customerRouterIpAddress` is `169.254.188.18/30`. In this case, the subnet value would be `169.254.188.16/30`.

### Create the private peering

###  Azure portal 

**Note:** For the most up-to-date information about how to create a private peering, see [Tutorial: Create and modify peering for an ExpressRoute circuit using the Azure portal](https://learn.microsoft.com/azure/expressroute/expressroute-howto-routing-portal-resource-manager) in the Azure documentation.

  1. Go the **ExpressRoute Circuits** page.

  2. Click the name of the circuit that you created in Create an ExpressRoute circuit.

  3. Click **Azure private peering**.

  4. Complete the form:

     * Enter the **ASN** of the Google Cloud Router—for example, `16550`.
     * In the **Subnets** section, enter **IPv4**.
     * Enter the **IPv4 Primary subnet** and **IPv4 Secondary subnet** values that you calculated in Calculate the IPv4 primary subnet value.
     * Enter the same **VLAN ID** that you entered when creating your VLAN attachments.
     * If you want to use MD5 authentication, enter your MD5 key in the **Shared key** field. Make sure that you enter the same key that you used when creating BGP sessions in Google Cloud.
  5. Click **Save**.




###  Azure PowerShell 

**Note:** For the most up-to-date information about how to create a private peering, see [Tutorial: Create and modify peering for an ExpressRoute circuit using PowerShell](https://learn.microsoft.com/azure/expressroute/expressroute-howto-routing-arm) in the Azure documentation.

Use the following commands:

  * [`Get-AzExpressRouteCircuit`](https://learn.microsoft.com/powershell/module/az.network/new-azexpressroutecircuitpeeringconfig?view=azps-8.2.0)
  * [`New-AzExpressRouteCircuitPeeringConfig`](https://learn.microsoft.com/powershell/module/az.network/new-azexpressroutecircuitpeeringconfig?view=azps-8.2.0)
  * [`Set-AzExpressRouteCircuit`](https://learn.microsoft.com/powershell/module/az.network/new-azexpressroutecircuitpeeringconfig?view=azps-8.2.0)



For example:
    
    
    $circuit = Get-AzExpressRouteCircuit -Name CIRCUIT_NAME `
       $circuit.Peerings = New-AzExpressRouteCircuitPeeringConfig `
       -Name 'AzurePrivatePeering' `
       -PeeringType 'AzurePrivatePeering' `
       -PeerASN ASN `
       -PrimaryPeerAddressPrefix PRIMARY_SUBNET  `
       -SecondaryPeerAddressPrefix SECONDARY_SUBNET `
       -VlanId VLAN_ID `
       -SharedKey MD5_KEY `
       Set-AzExpressRouteCircuit -ExpressRouteCircuit $circuit

Replace the following:

  * `CIRCUIT_NAME`: the name of your ExpressRoute circuit
  * `ASN`: the ASN of the Google Cloud Router
  * `PRIMARY_SUBNET` and `SECONDARY_SUBNET`: the values that you arrived at in Calculate the IPv4 primary subnet value
  * `VLAN_ID`: the VLAN ID that you specified when creating your VLAN attachments
  * `MD5_KEY`: the key to use for MD5 authentication (optional)



## Create a virtual network gateway

An ExpressRoute virtual network gateway connects your Azure network with a peer network—in this case, your Google Cloud VPC network.

###  Azure portal 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Tutorial: Configure a virtual network gateway for ExpressRoute using the Azure portal](https://learn.microsoft.com/azure/expressroute/expressroute-howto-add-gateway-portal-resource-manager) in the Azure documentation.

  1. Go the **Virtual network gateway** page.

  2. Click **Create**.

  3. Select the appropriate **Subscription**.

  4. Complete the **Instance Details** section of the form:

     * Enter a **Name** for the gateway.
     * Select the **Region** where your connection is located.
     * Select a **Gateway type** of **ExpressRoute**.
     * Use the **SKU** field to select the appropriate level of service.
**Important:** The value that you select for **SKU** affects the price of the circuit. For help with making a choice, see [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/).
     * Select a **Virtual network** that has a subnet in the same region as your ExpressRoute Direct connection.
     * Select a **Subnet**.
  5. Complete the **Public IP address** section of the form:

     * For **Public IP address** , do one of the following:

       * Select **Create new** , and then enter a **Public IP address name** for the new address and a **SKU**.

       * Select **Use existing** , and select an address that you previously created.

     * Select an **Availability zone**.

  6. Click **Next : Tags**.

  7. Optional: Set up tags for the gateway.

  8. Click **Next : Review + create**.

  9. Click **Create**.

Azure displays a **Deployment is in progress** message. After a few minutes, the message should update to say **Your deployment is complete**.




###  Azure PowerShell 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Tutorial: Configure a virtual network gateway for ExpressRoute using PowerShell](https://learn.microsoft.com/azure/expressroute/expressroute-howto-add-gateway-resource-manager) in the Azure documentation.

Use the following commands:

  * [`Get-AzVirtualNetwork`](https://learn.microsoft.com/powershell/module/az.network/get-azvirtualnetwork?view=azps-8.3.0)
  * [`Get-AzVirtualNetworkSubnetConfig`](https://learn.microsoft.com/powershell/module/az.network/get-azvirtualnetworksubnetconfig?view=azps-8.3.0)
  * [`New-AzPublicIpAddress`](https://learn.microsoft.com/powershell/module/az.network/new-azpublicipaddress?view=azps-8.3.0)
  * [`New-AzVirtualNetworkGatewayIpConfig`](https://learn.microsoft.com/powershell/module/az.network/new-azvirtualnetworkgatewayipconfig?view=azps-8.3.0)
  * [`New-AzVirtualNetworkGateway`](https://learn.microsoft.com/powershell/module/az.network/new-azvirtualnetworkgateway?view=azps-8.3.0)



Complete the following steps:

  1. Create an object that represents your Azure virtual network:
         
         $vnet = Get-AzVirtualNetwork -Name NETWORK_NAME `
            -ResourceGroupName RESOURCE_GROUP

Replace the following:

     * `NETWORK_NAME`: the name of your Azure virtual network
     * `RESOURCE_GROUP`: the name of the appropriate resource group
  2. Create an object that represents the subnet that you want to use for your circuit:
         
         $subnet = Get-AzVirtualNetworkSubnetConfig -Name NAME `
            -VirtualNetwork $vnet

Replace `NAME` with the name of your subnet.

  3. Allocate a public IP address for the virtual network:
         
         $pip = New-AzPublicIpAddress -Name NAME `
            -ResourceGroupName RESOURCE_GROUP `
            -Location REGION `
            -AllocationMethod Dynamic

Replace the following:

     * `NAME`: the name of your IP address
     * `RESOURCE_GROUP`: the name of the appropriate resource group
     * `REGION`: the region where your subnet is located
  4. Create a configuration object:
         
         $ipconf = New-AzVirtualNetworkGatewayIpConfig `
         -Name NAME `
         -Subnet $subnet `
         -PublicIpAddress $pip

Replace `NAME` with a name for your configuration.

  5. Create the gateway:
         
         $gateway = New-AzVirtualNetworkGateway NAME  `
            -ResourceGroupName RESOURCE_GROUP `
            -Location REGION `
            -IpConfigurations $ipconf `
            -GatewayType Expressroute `
            -GatewaySku SKU

Replace the following:

     * `NAME`: the name of the new gateway
     * `RESOURCE_GROUP`: the name of the appropriate resource group
     * `REGION`: the region where your subnet is located
     * `SKU`: the gateway SKU



## Create a connection

Create a connection between the following resources:

  * The ExpressRoute circuit private peering, which you created in Set up a private peering

  * The ExpressRoute virtual network gateway, which you created in Create a virtual network gateway




###  Azure portal 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Tutorial: Configure a virtual network gateway for ExpressRoute using the Azure portal](https://learn.microsoft.com/azure/expressroute/expressroute-howto-add-gateway-portal-resource-manager) in the Azure documentation.

  1. Go to the **Connections** page.

  2. Click **Create**.

  3. Select a **Subscription** and **Resource group**.

  4. Complete the **Instance Details** section of the form:

     * Set **Connection type** to **ExpressRoute**.
     * Enter a **Name** for the connection.
     * Select the **Region** where your ExpressRoute Direct connection is located.
  5. Click **Next : Settings** :

     * Select the appropriate **Virtual network gateway**.
     * Select your **ExpressRoute circuit**.
     * If appropriate, select **Enable Custom BGP Addresses**.
     * If appropriate, select **Redeem authorization**.
     * Enter the appropriate **Routing weight** value.
  6. Click **Next : Tags**.

  7. Optional: Set up tags for this port.

  8. Click **Next : Review + create**.

  9. Review the summary of your choices. If the summary looks correct, click **Create**. If not, click **Previous** and make corrections.

Azure displays a **Deployment is in progress** message. After a few minutes, the message should update to say **Your deployment is complete**.




###  Azure PowerShell 

**Note:** For the most up-to-date information about how to order an ExpressRoute Direct connection, see [Tutorial: Configure a virtual network gateway for ExpressRoute using PowerShell](https://learn.microsoft.com/azure/expressroute/expressroute-howto-add-gateway-resource-manager) in the Azure documentation.

Use the [`New-AzVirtualNetworkGatewayConnection` command](https://learn.microsoft.com/powershell/module/az.network/new-azvirtualnetworkgatewayconnection?view=azps-8.2.0):
    
    
    New-AzVirtualNetworkGatewayConnection `
       -Name CONNECTION_NAME `
       -ResourceGroupName RESOURCE_GROUP `
       -VirtualNetworkGateway1 GATEWAY `
       -Location LOCATION `
       -ConnectionType ExpressRoute `
       -PeerId PEER_ID
    

Replace the following:

  * `CONNECTION_NAME`: the name of the new connection
  * `RESOURCE_GROUP`: the name of the appropriate resource group
  * `GATEWAY`: the gateway that you created in Create a virtual network gateway
  * `LOCATION`: the region where you [created your ExpressRoute Direct resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/order-azure-ports#order-connections)
  * `PEER_ID`: the ID of the private peering that you created



[ Previous arrow_back  Configure your Google Cloud resources  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/configure-google-resources)

[ Next Verify your connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/test-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
