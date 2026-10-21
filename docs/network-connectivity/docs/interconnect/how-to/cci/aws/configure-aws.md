---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-aws/
title: Configure your AWS resources \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:06.669405+00:00
---

# Configure your AWS resources  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure your AWS resources Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides sample guidance. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For detailed instructions, see the [AWS documentation](https://docs.aws.amazon.com/) . 

To finalize your dedicated physical connection between Google Cloud and Amazon Web Services (AWS), configure your AWS resources. You must configure your AWS resources after you configure your [Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources).

## Before you begin

Before starting, you must already have an AWS VPC. For more information, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html#Create-VPC).

## Create a Direct Connect gateway

A [Direct Connect gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html) connects your AWS port to your AWS VPC.

###  AWS console 

To create a Direct Connect gateway, complete the following steps:

  1. Go to the **Direct Connect gateway** page.

  2. Click **Create Direct Connect gateway**.

  3. On the **Create Direct Connect gateway** page, enter the required information:

     1. Enter a **Name** for the gateway.

     2. Enter an **Amazon-side ASN**. This value must match the **Peer ASN** value that you used when you [configured a Border Gateway Protocol (BGP) session in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp).

  4. Click **Create Direct Connect gateway**.




###  AWS CLI 

To create a Direct Connect gateway, use the [`create-direct-connect-gateway` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway.html). For example:
    
    
    aws directconnect create-direct-connect-gateway \
      --direct-connect-gateway-name GATEWAY_NAME \
      --amazon-side-asn AMAZON_ASN
    

Replace the following:

  * `GATEWAY_NAME`: the name of the gateway
  * `AMAZON_ASN`: the ASN that you're using to represent Amazon; this value must match the `peer-asn` value when you [created the Border Gateway Protocol (BGP) session on the Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp)



## Create a virtual private interface

Before you can begin using your Direct Connect gateway, you must create a [private virtual interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/WorkingWithVirtualInterfaces.html) for each of your LAGs. A private virtual interface lets you access an Amazon VPC by using private IP addresses.

The function of a private virtual interface is similar to the function of a Google Cloud VLAN attachment. However, one difference is that you configure a BGP peering session as part of the process of creating the interface, rather than doing it later.

**Note:** To complete this procedure, you need values from your VLAN attachments in Google Cloud. Specifically, you need the IP addresses that represent the Google Cloud and AWS sides of the peering. For help finding these values, see [Get details about your VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#describe-attachments).

###  AWS console 

To create a private virtual interface, complete the following steps:

  1. Go to the **Virtual interfaces** page.

  2. Click **Create virtual interface**.

  3. On the **Create virtual interface** page, enter the required information:

     * Leave **Type** set to **Private**.

     * Enter a **Virtual interface name**.

     * Select the appropriate **Connection**.

     * Set **Virtual interface owner** to the appropriate value.

     * Leave **Gateway type** set to **Direct Connect Gateway --_Recommended_**.

     * Set **Direct Connect gateway** to the gateway that you just created.

     * In the **Virtual Local Area Network (VLAN)** field, enter the value that you used for **VLAN ID** when you [created your VLAN attachments in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#create-attachments).

     * Set **BGP ASN** to the value of the ASN used by your Google Cloud Router.

     * Expand **Additional settings**. In the form that is displayed, some values are labeled as optional, but they are required by Cross-Cloud Interconnect. Do the following:

       * Leave **Address family -_optional_** set to **IPv4**.

       * In the **Your router peer ip -_optional_** field, enter the address on your [VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#describe-attachments) that represents Google Cloud; that is, the **Cloud Router BGP IP** value.

       * In the **Amazon router peer IP -_optional_** field, enter the address on your VLAN attachment on your [VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#describe-attachments) AWS; that is, the **BGP IP Peer** value.

       * In the **BGP authentication key -_optional_** field, enter the same MD5 authentication key that you used when you [configured a BGP peering session in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp).

  4. Click **Create virtual interface**.

  5. Repeat steps 1 through 4 for your second LAG.




###  AWS CLI 

To create virtual interfaces, you use the [`aws directconnect create-private-virtual-interface` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-private-virtual-interface.html). Complete the following steps:

  1. Create the virtual interface for your first LAG:
         
         aws directconnect create-private-virtual-interface \
            --connection-id DXLAG_ID \
            --region REGION \
            --new-private-virtual-interface `echo '{
                "virtualInterfaceName": "INTERFACE_NAME",
                "vlan": VLAN_ID,
                "asn": GOOGLE_SIDE_ASN,
                "authKey": "YOUR_KEY",
                "amazonAddress": "AMAZON_ADDRESS",
                "customerAddress": "GOOGLE_ADDRESS",
                "directConnectGatewayId": "GATEWAY_ID"
            }' | jq -r tostring`
         

Replace the following:

     * `DXLAG_ID`: the ID of the LAG; if you don't have this value, retrieve it by using the [`aws directconnect describe-lags` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-lags.html)
     * `REGION`: the region where the LAG is located
     * `INTERFACE_NAME`: a name for the new private virtual interface
     * `VLAN_ID`: the same ID that you used when [creating your VLAN attachments in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#create-attachments)
     * `GOOGLE_SIDE_ASN`: the Google Cloud Router ASN
     * `YOUR_KEY`: the same MD5 authentication key you used when you [configured a BGP peering session in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp)
     * `AMAZON_ADDRESS`: the address that represents AWS on your [VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#describe-attachments); that is, the `customerRouterIpAddress` value
     * `GOOGLE_CLOUD_ADDRESS`: the address that represents Google Cloud on your VLAN attachment; that is, the `cloudRouterIpAddress` value
     * `GATEWAY_ID`: the ID of your Direct Connect gateway
  2. Create the virtual interface for your second LAG:
         
         aws directconnect create-private-virtual-interface \
            --connection-id DXLAG_ID_2 \
            --region REGION_2 \
            --new-private-virtual-interface `echo '{
                "virtualInterfaceName": "INTERFACE_NAME_2",
                "vlan": VLAN_ID_2,
                "asn": GOOGLE_SIDE_ASN,
                "authKey": "YOUR_KEY",
                "amazonAddress": "AMAZON_ADDRESS_2",
                "customerAddress": "GOOGLE_ADDRESS_2",
                "directConnectGatewayId": "GATEWAY_ID"
            }' | jq -r tostring`
         

Replace the following:

     * `DXLAG_ID_2`: the connection ID of your second LAG; if you don't have this value, retrieve it by using the [`aws directconnect describe-lags` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-lags.html)
     * `REGION_2`: the region where the LAG is located
     * `INTERFACE_NAME_2`: a name for the new private virtual interface
     * `VLAN_ID_2`: the same ID that you used when [creating your VLAN attachments in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#create-attachments)
     * `GOOGLE_SIDE_ASN`: the Google Cloud Router ASN
     * `YOUR_KEY`: the same MD5 authentication key you used when you [configured a BGP peering session in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp)
     * `AMAZON_ADDRESS_2`: the address that represents AWS on your [VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#describe-attachments); that is, the `customerRouterIpAddress` value
     * `GOOGLE_ADDRESS_2`: the address that represents Google Cloud on your VLAN attachment; that is, the `cloudRouterIpAddress` value
     * `GATEWAY_ID`: the ID of your Direct Connect gateway



## Create a virtual private gateway

A virtual private gateway provides access to an AWS VPC.

###  AWS console 

To create a virtual private gateway, do the following:

  1. Go to the **Virtual private gateways** page.

  2. Click **Create virtual private gateway**.

  3. On the **Create virtual private gateway** page, enter the required information:

     * Optional: enter a **Name tag** for the gateway.

     * For **Autonomous System Number (ASN)** , select an ASN to represent AWS. Make sure you match the value that you entered for **Peer ASN** when you [configured a BGP peering session in Google Cloud](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp). Do one of the following:

       * If you used `64512`, select **Amazon default ASN**.
       * If you used something else, select **Custom ASN** and enter the appropriate value.
  4. Click **Create virtual private gateway**.




###  AWS CLI 

To create a virtual private gateway, use the [`create-vpn-gateway` command](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpn-gateway.html). For example:
    
    
    aws directconnect create-vpn-gateway \
    --type ipsec.1 \
    --region REGION \
    --amazon-side-asn ASN

Replace the following:

  * `REGION`: the name of your region
  * `AMAZON_ASN`: the ASN that you're using to represent Amazon; it must be the same value that you used when you [created the BGP peer on the Google Cloud Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources#configure-bgp)



## Attach the virtual private gateway to your AWS VPC

For the virtual private gateway to work, you must attach it to your AWS VPC.

###  AWS console 

To attach a private virtual interface to your AWS VPC, complete the following steps:

  1. Go to the **Virtual private gateways** page.

  2. Click the name of the virtual private gateway that you just created.

  3. Click the **Actions** menu, and select **Attach to VPC**.

  4. On the **Attach to VPC** page, select the appropriate VPC.

  5. Click **Attach to VPC**.




###  AWS CLI 

To attach the gateway to your VPC, use the [`aws ec2 create-private-virtual-interface` command](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-vpn-gateway.html). For example:
    
    
      aws ec2 attach-vpn-gateway \
        --vpn-gateway-id VIRTUAL_PRIVATE_GATEWAY_ID \
        --vpc-id VPC_ID \
        --region REGION
    

Replace the following:

  * `VIRTUAL_PRIVATE_GATEWAY_ID`: the ID of your virtual private gateway
  * `VPC_ID`: the ID of your AWS VPC
  * `REGION`: the region where your virtual private gateway is located



## Associate the virtual private gateway with the Direct Connect gateway

To connect your Direct Connect gateway to your AWS VPC, associate the virtual private gateway with the Direct Connect gateway.

###  AWS console 

To attach a private virtual interface to your AWS VPC, complete the following steps:

  1. Go to the **Direct Connect gateway** page.

  2. Click the name of your gateway.

  3. Click **Gateway associations**.

  4. Click **Associate gateway**.

  5. On the **Associate gateway** page, set **Gateways** to the name of your virtual private gateway.

  6. Click **Associate gateways**.




###  AWS CLI 

To associate your virtual private gateway to your Direct Connect, you use the [`aws directconnect create-direct-connect-gateway-association` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/create-direct-connect-gateway-association.html). For example:
    
    
     aws directconnect create-direct-connect-gateway-association \
       --direct-connect-gateway-id GATEWAY_ID \
       --virtual-gateway-id VIRTUAL_PRIVATE_GATEWAY_ID \
       --region REGION
    

Replace the following:

  * `GATEWAY_ID`: the ID of your Direct Connect gateway
  * `VIRTUAL_PRIVATE_GATEWAY_ID`: the ID of your virtual private gateway
  * `REGION`: the region where your Direct Connect gateway is located



[ Previous arrow_back  Configure Google Cloud resources  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources)

[ Next Verify your connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/test-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
