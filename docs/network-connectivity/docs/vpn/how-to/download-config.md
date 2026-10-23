---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/download-config/
title: Download a peer VPN configuration template \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:46.937423+00:00
---

# Download a peer VPN configuration template  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/download-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Download a peer VPN configuration template Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to download a configuration template for your third-party peer VPN device. You configure the device when you connect your on-premises network to Google Cloud by using HA VPN.

You can download the configuration template as the final step of creating the HA VPN connection to a peer VPN gateway. Another option is to download the configuration template for an existing peer VPN gateway that already has established HA VPN tunnels.

## Available vendor templates

You can download configuration templates for the following third-party VPN devices:

  * Cisco Firepower, running ASA 9.13(1)2 or later
  * Fortinet FortiGate 200E, running FortiOS 6.2.3 or later
  * Juniper vSRX, running JunOS 18.4R3-S2 or later



These configuration templates apply only to HA VPN and not to Classic VPN.

## Considerations for using the templates

When using the configuration templates, keep the following in mind:

  * You can only download configuration templates for your peer VPN device from the Google Cloud console. The configuration templates are not accessible through the Cloud VPN API or the Google Cloud CLI.

  * You can only download configuration templates for VPN tunnels that are configured with a Border Gateway Protocol (BGP) session.

  * The configuration templates might not include any configuration values for the following Google Cloud features:

    * Dual stack (IPv4 and IPv6) or IPv6 only HA VPN gateways
    * IPv4 BGP session multiprotocol BGP (MP-BGP) configuration
    * MD5 for BGP authentication
    * IPv6 BGP session configuration
    * External IPv6 addresses for HA VPN gateways

If you enable these features in HA VPN, you must add their configuration after you download the configuration template.

  * The configuration templates might require additional customization before you apply the configuration to your VPN device. For example, customization might be required for your network or the specific operating system version installed on your VPN device. Before you apply the configuration, review the contents of the downloaded configuration file, and make any necessary adjustments.

  * Some templates include defaults that have been preselected by Google. For example, some templates specify `aes256-sha1` algorithms for IKE Phase 1 and Phase 2. You can modify these defaults as needed for your network or security requirements. The selected defaults might differ across vendor devices. For additional details on selected defaults, review the comments at the top of your configuration template.

  * The configuration templates don't address advanced configurations, such as virtual port assignments or virtual interface definitions.




## Required permissions

To create HA VPN gateways and tunnels, you need the permissions listed in [Create an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#creating-ha-gw-peer-tunnel).

To download a peer VPN configuration template, you must have the following project permissions.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.routers.get`
  * `compute.routers.list`



**Roles**

  * `roles/compute.networkUser`



## Download a configuration template for new peer VPN tunnels

To download a configuration template that contains tunnel configurations for a new peer VPN device, perform the following steps:

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. Create the VPN tunnels and BGP sessions:



  * If you want to create a new HA VPN gateway, click **VPN setup wizard**. Then follow the wizard to configure an HA VPN gateway, peer VPN gateway resource, VPN tunnels, and BGP sessions. For detailed instructions, see [Create an HA VPN to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn). 
    * If you want to create tunnels for an existing HA VPN gateway, complete the following steps:

      1. Click **Create VPN tunnel**.
      2. In the **VPN gateway** list, select an HA VPN gateway, and click **Continue**.
      3. Select a peer VPN gateway. Then, create the VPN tunnels and configure the BGP sessions. For detailed instructions, see [Add a tunnel from an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel#add-tunnel-from-ha-vpn-to-peer).


  1. On the **Summary and reminder** page, click **Download configuration**. The **Download configuration** dialog appears.

  2. In the **Vendor** list, select the vendor for your peer VPN device.

  3. If the vendor of your peer VPN device does not appear in the list, select **Other** and perform the following steps:

     1. Record the configuration values listed in the dialog. You use these values to configure your peer VPN device.
     2. Click **Cancel** to exit the dialog.
     3. Complete the instructions in the [Use third-party VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides) and [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway) pages to configure your peer VPN device.
  4. If you've selected one of the vendors, continue by selecting the platform of your VPN device from the **Platform** list.

  5. In the **Software** list, select the software version of your VPN device. The software version reflects the minimum required software version of the VPN device.

  6. After you make all the selections for your peer VPN device, the contents of the template appear in plain text. To download the configuration file, complete one of the following options:

     * Click content_copy**Copy** to put the contents of the template into your buffer.
     * Click **Download** to save the text file locally.
  7. Open the file or paste the contents in a text editor of your choice.

  8. Replace all `_SNAKE_CASE_` variables in the file with the appropriate values for your VPN gateways and networks.

Because you haven't yet created the VPN tunnels, the IKE pre-shared keys that you configured for each tunnel are stored within the configuration template. Don't replace the `_IKE_SHARED_SECRET_PLACEHOLDER_` variables because the variables are already replaced for you.

  9. Complete the configuration by using the commands in the updated configuration file. You might be able to load the entire configuration file on your device, or you might enter the commands through an interactive prompt. For more information, see your peer VPN vendor documentation.




## Download a configuration template for existing tunnels

To download a configuration template for your existing peer VPN device and tunnels, perform the following steps:

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. Click **Peer VPN Gateways**.

  3. Next to the peer VPN gateway and VPN tunnels that have configurations you want to download, click more_vert**Actions** , then select **Download configuration**.

  4. In the **Download configuration** dialog, select the VPN tunnels that have configurations you want download. You can only select the VPN tunnels that are configured with a BGP session.

  5. In the **Vendor** list, select the vendor for your peer VPN device.

  6. If the vendor of your peer VPN device does not appear in the list, select **Other** and perform the following steps:

     1. Record the configuration values listed in the dialog. You use these values to configure your peer VPN device.
     2. Click **Cancel** to exit the dialog.
     3. Complete the instructions in the [Use third-party VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides) and [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway) pages to configure your peer VPN device.
  7. If you've selected one of the vendors, continue by selecting the platform of your VPN device from the **Platform** list.

  8. In the **Software** list, select the software version of your VPN device. The software version reflects the minimum required software version of the VPN device.

  9. After you make all the selections for your peer VPN device, the contents of the template appear in plain text. To download the configuration file, complete one of the following options:

     * Click content_copy **Copy** to put the contents of the template into your buffer.
     * Click **Download** to save the text file locally.
  10. Open the file or paste the contents in a text editor of your choice.

  11. Replace all `_SNAKE_CASE_` variables in the file with the appropriate values for your VPN gateways and networks.

Because these VPN tunnels are already created, you must replace each `_IKE_SHARED_SECRET_PLACEHOLDER_` with the IKE pre-shared key configured for each tunnel.

  12. Complete the configuration by using the commands in the updated configuration file. You might be able to load the entire configuration file on your device, or you might enter the commands through an interactive prompt. For more information, see your peer VPN vendor documentation.




## What's next

  * To check the status of your VPN tunnels, see [Check VPN status](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status).
  * To view Cloud Logging and Monitoring information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
