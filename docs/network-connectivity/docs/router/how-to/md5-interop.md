---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/md5-interop/
title: Set up MD5 authentication on third-party routers \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:19.702595+00:00
---

# Set up MD5 authentication on third-party routers  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/md5-interop/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up MD5 authentication on third-party routers

If you configure MD5 authentication when establishing a Border Gateway Protocol (BGP) session by using Cloud Router, you must also configure MD5 authentication on the peer router. The following sections include guidance specific to several third-party routers.

MD5 is a method of BGP peer authentication that uses the MD5 message-digest algorithm. When you use this approach, BGP peers must use the same authentication key, or a connection cannot be established between them. Later, every segment routed between the peers is verified. For more information about MD5 authentication, see [RFC 2385](https://datatracker.ietf.org/doc/html/rfc2385). For more information about using MD5 authentication with Cloud Router, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

## Arista EOS

The following sections describe how to use MD5 authentication with Arista Extensible Operating System (EOS) devices.

For more information, see the [Arista documentation](https://www.arista.com/en/um-eos/eos-border-gateway-protocol-bgp#xx1117278).

### Configure MD5 authentication

To configure MD5 authentication, log in to the Arista router and associate the BGP peer with your secret key:
    
    
    router bgp ASN
    neighbor CLOUD_ROUTER_IP_ADDRESS password SECRET_KEY
    

Replace the following values:

  * `ASN`: the ASN for the Arista side of the BGP session
  * `CLOUD_ROUTER_IP_ADDRESS`: the IP address of the Cloud Router that you are peering with
  * `SECRET_KEY`: your secret MD5 authentication key; make sure you use the same key that you used to configure the corresponding BGP session on the Cloud Router



### Verify the configuration

After committing the configuration, verify it:
    
    
    show running-config
    

In the output, look for the following details.
    
    
    ..
    router bgp ASN
       ...
       neighbor CLOUD_ROUTER_IP_ADDRESS password ENCRYPTED_KEY_STRING
       ...
    

In this output, `ENCRYPTED_KEY_STRING` is an encrypted string that represents your secret key.

### Verify routes

To verify routes, run the following command.
    
    
    show ip route bgp
    

### Verify status

To view the status of a BGP neighbor, run the following command.
    
    
    show ip bgp neighbors CLOUD_ROUTER_IP_ADDRESS
    

Replace `CLOUD_ROUTER_IP_ADDRESS` with the IP address of the neighbor.

## Cisco IOS and IOS-XE

The following sections describe how to use MD5 authentication with Cisco IOS and IOS-XE devices.

For more information, see [MD5 Authentication Between BGP Peers Configuration Example](https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/112188-configure-md5-bgp-00.html#configs) in the Cisco documentation.

### Configure MD5 authentication

To configure MD5, log in to the Cisco router and associate the BGP peer with your secret key:
    
    
    router bgp ASN
     neighbor CLOUD_ROUTER_IP_ADDRESS password SECRET_KEY
     !
    

Replace the following values:

  * `ASN`: the ASN for the Cisco side of the BGP session
  * `CLOUD_ROUTER_IP_ADDRESS`: the IP address of the Cloud Router that you are peering with
  * `SECRET_KEY`: your secret MD5 authentication key; make sure you use the same key that you used to configure the corresponding BGP session on the Cloud Router



### Verify the configuration

After committing the configuration, verify it:
    
    
    show running-config
    

In the output, look for the following details:
    
    
    ..
    router bgp ASN
     ...
     neighbor CLOUD_ROUTER_IP_ADDRESS  password  ... 
     ...
    

### Verify routes

To verify routes, run the following command.
    
    
    show ip route bgp
    

### Verify status

To view the status of a BGP neighbor, run the following command.
    
    
    show ip bgp neighbors CLOUD_ROUTER_IP_ADDRESS
    

Replace `CLOUD_ROUTER_IP_ADDRESS` with the IP address of the neighbor.

## Juniper JunOS

The following sections describe how to use MD5 authentication with Juniper JunOS devices.

For additional information, see the [Juniper documentation](https://www.juniper.net/documentation/us/en/software/junos/bgp/topics/ref/statement/authentication-key-edit-protocols-bgp.html).

### Configure MD5 authentication

To configure MD5, log in to the Juniper router and associate the BGP peer with your secret key:
    
    
    set protocols bgp group YOUR_PEER_GROUP neighbor CLOUD_ROUTER_IP_ADDRESS SECRET_KEY
    

Replace the following values:

  * `YOUR_PEER_GROUP`: the BGP peer group
  * `CLOUD_ROUTER_IP_ADDRESS`: the IP address of the Cloud Router that you are peering with
  * `SECRET_KEY`: your secret MD5 authentication key; make sure you use the same key that you used to configure the corresponding BGP session on the Cloud Router



### Verify the configuration

After committing the configuration, verify it:
    
    
    show configuration
    

In the output, look for the following details.
    
    
    bgp {
        group YOUR_PEER_GROUP {
            ...
            neighbor CLOUD_ROUTER_IP_ADDRESS {
                authentication-key ENCRYPTED_KEY_STRING; ## SECRET-DATA
                ...
            }
        }
    }
    

In this output, `ENCRYPTED_KEY_STRING` is an encrypted string that represents your secret key.

### Verify routes

To verify routes, run the following command.
    
    
    show ip route bgp
    

### Verify status

To view the status of a BGP neighbor, run the following command.
    
    
    show ip bgp neighbors CLOUD_ROUTER_IP_ADDRESS
    

Replace `CLOUD_ROUTER_IP_ADDRESS` with the IP address of the neighbor.

## Palo Alto Networks VM-Series

The following sections describe how to use MD5 authentication with Palo Alto Networks VM-Series devices.

For more information, see the [Palo Alto Networks documentation](https://docs.paloaltonetworks.com/pan-os/10-0/pan-os-admin/networking/bgp/configure-bgp).

### Configure MD5 authentication

In the PAN-OS Web Interface, complete the following steps:

  1. Select **Network** > **Virtual Routers** > ROUTER_NAME > **BGP** > **Create a new Auth Profile**.

  2. In the **Auth Profile** window, enter values for each of the following:

     * **Profile Name**
     * **Secret/Confirm Secret**

Make sure you use the same secret key that you used to configure the BGP session on the Cloud Router.

  3. Apply your new authentication profile to the BGP session:

     1. Go to **Network** > **Virtual Routers** > ROUTER_NAME > **BGP** > **Peer Group** > YOUR PEER GROUP > YOUR BGP PEER > **Connection Options**.

     2. In the **Auth Profile** field, select the authentication profile that you just created.

  4. Click **OK**.




### Verify the configuration

After you have configured MD5 authentication, verify it by using the PAN-OS Web Interface. To view details about the configuration, go to **Network** > **Virtual Routers** > **More Runtime Stats** > **BGP** > **Peer**.

### Verify routes

To verify routes by using the PAN-OS Web Interface, complete the following steps:

  1. Select **Network** > **Virtual Routers**.

  2. In the row that corresponds with the virtual router that you are interested in, click **More Runtime Stats**.

  3. Select **Routing** > **Route Table**.




### Verify status

To verify BGP peer status by using the PAN-OS Web Interface, complete the following steps:

  1. Select **Network** > **Virtual Routers**.

  2. In the row that corresponds with the virtual router that you are interested in, click **More Runtime Stats**.

  3. Select **BGP** > **Peer**.




## Quagga

The following sections describe how to use MD5 authentication with Quagga devices.

For more information, see the [Quagga documentation](https://quagga.net/docs/quagga.html#BGP).

### Configure MD5 authentication

To configure MD5, log in to the Quagga router and associate the BGP peer with your secret key:
    
    
    router bgp ASN
     neighbor CLOUD_ROUTER_IP_ADDRESS password SECRET_KEY
     !
    

Replace the following values:

  * `ASN`: the ASN for the Quagga side of the BGP session
  * `CLOUD_ROUTER_IP_ADDRESS`: the IP address of the Cloud Router that you are peering with
  * `SECRET_KEY`: your secret MD5 authentication key; make sure you use the same key that you used to configure the corresponding BGP session on the Cloud Router



### Verify the configuration

After committing the configuration, verify it:
    
    
    show running-config
    

In the output, look for the following details.
    
    
    ..
    router bgp ASN
     ...
     neighbor CLOUD_ROUTER_IP_ADDRESS  password ENCRYPTED_KEY_STRING
     ...
    

In this output, `ENCRYPTED_KEY_STRING` is an encrypted string that represents your secret key.

### Verify routes

To view the route table, run the following command.
    
    
    show ip bgp
    

For more information, see the [Quagga documentation for this command](https://www.quagga.net/docs/docs-multi/Show-IP-BGP.html#Show-IP-BGP).

### Verify status

To verify BGP status, use the following command.
    
    
    show ip bgp neighbor CLOUD_ROUTER_IP_ADDRESS
    

Replace `CLOUD_ROUTER_IP_ADDRESS` with the IP address of the neighbor.

## What's next

  * [Update the base advertised route priority](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/updating-priority)

  * [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp)

  * [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details)

  * [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
