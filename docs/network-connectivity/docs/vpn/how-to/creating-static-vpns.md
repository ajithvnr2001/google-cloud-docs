---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns/
title: Create a Classic VPN gateway using static routing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:47.439210+00:00
---

# Create a Classic VPN gateway using static routing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-static-vpns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Create a Classic VPN gateway using static routing Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use static routing to create a Classic VPN gateway and one tunnel. This tunnel is either a policy-based or route-based tunnel.

With route-based VPN, you specify only the remote traffic selector. If you need to specify a local traffic selector, create a Cloud VPN tunnel that uses policy-based routing instead.

Classic VPN does not support IPv6.

**Note:** HA VPN _does not_ support static routing.**Caution:** If you convert an auto mode VPC network to a custom mode VPC network, you might have to delete and re-create VPN tunnels that use policy-based routing if the tunnel relied on default values for local IP ranges. Changing the mode of a VPC network with active VPN tunnels can lead to outages. For more information, see [considerations for auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations).

For more information about Cloud VPN, see the following resources:

  * For best practices to consider before setting up Cloud VPN, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices).

  * For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  * For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).




## Routing options

When you use the Google Cloud console to create a _policy-based_ tunnel, Classic VPN performs the following tasks:

  * Sets the tunnel's local traffic selector to the IP range that you specify.
  * Sets the tunnel's remote traffic selector to the IP ranges that you specify in the **Remote network IP ranges** field.
  * For each range in **Remote network IP ranges** , Google Cloud creates a custom static route whose destination (prefix) is the range's CIDR, and whose next hop is the tunnel.



After you create a _policy-based_ Classic VPN tunnel, the IP ranges you entered in the **Remote network IP ranges** field appear as **Advertised IP ranges** on the VPN tunnel details page.

When you use the Google Cloud console to create a _route-based_ tunnel, Classic VPN performs the following tasks:

  * Sets the tunnel's local and remote traffic selectors to any IP address (`0.0.0.0/0`).
  * For each range in **Remote network IP ranges** , Google Cloud creates a custom static route whose destination (prefix) is the range's CIDR and whose next hop is the tunnel.

**Important:** Traffic selectors cannot be changed after a tunnel has been created. If traffic selectors need to be changed in the future, you must delete and re-create the tunnel.

When you use the Google Cloud CLI to create either a policy-based tunnel or a route-based tunnel, traffic selectors for the tunnel are defined in the same way. However, because the creation of custom static routes is done with separate commands, you have more control over those routes.

The number of CIDRs that you can specify in a traffic selector depends on the IKE version.

For important background information, see the following:

  * [Routing options and traffic selectors](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing)
  * [Multiple CIDRs per traffic selector](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-ip-ranges)



## Before you begin

Set up the following items in Google Cloud to make it easier to configure Cloud VPN:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init



  1. If you are using the Google Cloud CLI, set your project ID with the following command. The `gcloud` instructions on this page assume that you have set your project ID before issuing commands.
         
         gcloud config set project PROJECT_ID
             



  1. You can also view a project ID that has already been set by running the following command:
         
         gcloud config list --format='text(core.project)'
             




#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.targetVpnGateways.get`
  * `compute.targetVpnGateways.list`
  * `compute.targetVpnGateways.create`
  * `compute.targetVpnGateways.delete`
  * `compute.targetVpnGateways.use`
  * `compute.targetVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`

**Important:** Creating a Classic VPN gateway requires external forwarding rules that you create in the Google Cloud CLI or in the Google Cloud console. Make sure that an Identity and Access Management (IAM) condition doesn't allow principals to create internal forwarding rules only. If such a condition exists, Classic VPN gateway creation fails with a permissions error. For more information, see [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions).

### Create a custom VPC network and subnet

Before creating a Classic VPN gateway and tunnel, create a Virtual Private Cloud (VPC) network and at least one subnet in the [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) where the Classic VPN gateway is located.

  * To create a custom mode VPC network (recommended), see [Create a custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).
  * To create subnets, see [Working with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).



## Create a gateway and tunnel

###  Console 

**Configure the gateway**

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. If you are creating a gateway for the first time, click **Create VPN connection**.

  3. Select the **VPN setup wizard**.

  4. Select the **Classic VPN** option button.

  5. Click **Continue**.

  6. On the **Create a VPN connection** page, specify the following gateway settings:

     * **Name** : The name of the VPN gateway. The name cannot be changed later.
     * **Description** : Optionally, add a description.
     * **Network** : Specify an existing VPC network in which to create the VPN gateway and tunnel.
     * **Region** : Cloud VPN gateways and tunnels are regional objects. Choose a [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) where the gateway will be located. Instances and other resources in _different regions_ can use the tunnel for egress traffic subject to the [order of routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes). For best performance, locate the gateway and tunnel in the same region as relevant Google Cloud resources.
     * **IP address** : Create or choose an existing regional [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress).



**Configure tunnels**

  1. For the new tunnel, in the **Tunnels** section, specify the following settings:

     * **Name** : The name of the VPN tunnel. The name cannot be changed later.
     * **Description** : Optionally, type a description.
     * **Remote peer IP address** : Specify the external IP address of the peer VPN gateway.
     * **IKE version** : Choose the appropriate IKE version supported by the peer VPN gateway. IKEv2 is preferred if it's supported by the peer device. **Known issue:** When configuring VPN tunnels to AWS, use the IKEv2 encryption protocol and select fewer transform sets on the AWS side; otherwise, the Cloud VPN tunnel can fail to rekey. For example, select a combination of single Phase 1 and Phase 2 encryption algorithms, integrity algorithms, and DH group numbers.  
  
This rekeying issue is caused by a large Security Association (SA) payload size for the default set of AWS transform sets. This large payload size results in IP fragmentation of IKE packets on the AWS side, which Cloud VPN does not support.
     * **IKE pre-shared key** : Provide a pre-shared key (shared secret) used for authentication. The pre-shared key for the Cloud VPN tunnel must match the one used when you configure the counterpart tunnel on the peer VPN gateway. To generate a cryptographically strong pre-shared key, follow the directions at [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key).

**For policy-based tunnels**

     1. Under **Routing options** , select **Policy-based**.
     2. Under **Remote network IP ranges** , provide a space-separated list of the IP ranges used by the peer network. This is the **remote traffic selector** , or the _right side_ from the perspective of Cloud VPN.

After you create a _policy-based_ Classic VPN tunnel, the IP ranges you entered in the **Remote network IP ranges** field appear as **Advertised IP ranges** on the VPN tunnel details page.

     3. Under **Local IP ranges** , select _one_ of the following methods:

        * To choose an existing local IP range, use the **Local subnetworks** menu.
        * To enter a list of space-separated IP ranges used in your VPC network, use the **Local IP ranges** field. For important considerations, see [Policy-based tunnels and traffic selectors](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#static-routing-networks).

**For route-based tunnels**

     1. Under **Routing options** , select **Route-based**.
     2. Under **Remote network IP ranges** , provide a space-separated list of the IP ranges used by the peer network. These ranges are used to create custom static routes whose next hop is this VPN tunnel.
  2. Optional: Select cipher configuration. Select **Default** for automatic, recommended security settings, or **Custom** to manually order and configure ciphers. For steps about how to configure ciphers, see Configure ciphers.

  3. If you need to create more tunnels on the same gateway, click **Add tunnel** and repeat the previous step. You can also [add more tunnels later](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel).

  4. Click **Create**.


**Note:** Google Cloud automatically creates one route for each remote IP range that you specify. The destination of the route is the remote IP range, its next hop is set to the Cloud VPN tunnel, and its priority is `1000`. You _cannot_ set the priority of this automatically created route, but you can delete and replace it. If you need greater control over the priority of VPN routes, follow the gcloud CLI steps instead.

**Configure ciphers**

You can configure ciphers when creating Cloud VPN tunnels. If you don't configure ciphers, the system uses the [default values](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#tables). To configure ciphers, do the following:

  1. Go to the **VPN cipher selection** section.
  2. Select **Custom**.
  3. Configure the ciphers for **IKE Phase 1**.

     1. In the **Encryption** row, click edit.
     2. In the **New Cipher** section, select the encryption cipher.
     3. Click **Done**.
     4. To add more ciphers, click **Add Cipher** and select the encryption cipher, and click **Done**.
**Note:** You can change the priority order of ciphers using the arrows.
  4. Click **Save**.

  5. Similarly, configure the following:

     * **Integrity** : in the **Integrity** row, click edit, select ciphers, and then click **Save**.
     * **PRF** : in the **PRF** row, click edit, select ciphers, and then click **Save**.
     * **Diffie-Hellman (DH)** : in the **Diffie-Hellman (DH)** row, click edit, select ciphers, and then click **Save**.
  6. Click **Save**.

  7. In the **IKE Phase 2** section, configure the following:

     * **Encryption** : Select one or more encryption algorithms.
     * **Integrity** : Select one or more integrity algorithms.
     * **PFS** : Select one or more PFS algorithms.
  8. Click **Save**.


**Note:** When selecting multiple ciphers, ensure that you order Authenticated Encryption with Associated Data (AEAD) ciphers before non-AEAD ciphers.

###  gcloud 

To create a Cloud VPN gateway, complete the following command sequence. In the commands, replace the following:

  * `PROJECT_ID`: the ID of your project
  * `NETWORK`: the name of your Google Cloud network
  * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
  * `GW_NAME`: the name of the gateway
  * `GW_IP_NAME`: a name for the external IP address used by the gateway
  * Optional: The `--target-vpn-gateway-region` is the region of the Classic VPN gateway to operate on. Its value should be the same as `--region`. If not specified, this option is automatically set. This option overrides the default compute/region property value for this command invocation.



**Configure the gateway resources**

  1. Create the target VPN gateway object:
         
         gcloud compute target-vpn-gateways create GW_NAME \
            --network=NETWORK \
            --region=REGION \
            --project=PROJECT_ID
         

  2. Reserve a regional external (static) IP address:
         
         gcloud compute addresses create GW_IP_NAME \
            --region=REGION \
            --project=PROJECT_ID
         

  3. Note the IP address (so you can use it when you configure your peer VPN gateway):
         
         gcloud compute addresses describe GW_IP_NAME \
            --region=REGION \
            --project=PROJECT_ID \
            --format='flattened(address)'
         

  4. Create three forwarding rules; these rules instruct Google Cloud to send ESP (IPsec), UDP 500, and UDP 4500 traffic to the gateway:
         
         gcloud compute forwarding-rules create fr-GW_NAME-esp \
            --load-balancing-scheme=EXTERNAL \
            --network-tier=PREMIUM \
            --ip-protocol=ESP \
            --address=GW_IP_NAME \
            --target-vpn-gateway=GW_NAME \
            --region=REGION \
            --project=PROJECT_ID
         
         
         gcloud compute forwarding-rules create fr-GW_NAME-udp500 \
            --load-balancing-scheme=EXTERNAL \
            --network-tier=PREMIUM \
            --ip-protocol=UDP \
            --ports=500 \
            --address=GW_IP_NAME \
            --target-vpn-gateway=GW_NAME \
            --region=REGION \
            --project=PROJECT_ID
         
         
         gcloud compute forwarding-rules create fr-GW_NAME-udp4500 \
            --load-balancing-scheme=EXTERNAL \
            --network-tier=PREMIUM \
            --ip-protocol=UDP \
            --ports=4500 \
            --address=GW_IP_NAME \
            --target-vpn-gateway=GW_NAME \
            --region=REGION \
            --project=PROJECT_ID
         




**Create the Cloud VPN tunnel**

  1. In the commands, replace the following:

     * `TUNNEL_NAME`: a name for the tunnel
     * `ON_PREM_IP`: the external IP address of the peer VPN gateway
     * `IKE_VERS`: `1` for IKEv1 or `2` for IKEv2  **Known issue:** When configuring VPN tunnels to AWS, use the IKEv2 encryption protocol and select fewer transform sets on the AWS side; otherwise, the Cloud VPN tunnel can fail to rekey. For example, select a combination of single Phase 1 and Phase 2 encryption algorithms, integrity algorithms, and DH group numbers.  
  
This rekeying issue is caused by a large SA payload size for the default set of AWS transform sets. This large payload size results in IP fragmentation of IKE packets on the AWS side, which Cloud VPN does not support.
     * `SHARED_SECRET`: your pre-shared key (shared secret). The pre-shared key for the Cloud VPN tunnel must match the one used when you configure the counterpart tunnel on the peer VPN gateway. To generate a cryptographically strong pre-shared key, follow the directions at [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key).
     * The following are optional parameters for configuring cipher algorithms. If not specified, the system uses the [default values](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#tables). 
       * `PH1_ENCRYPT_ALGRTHS`: a comma-separated list of encryption algorithms that are supported for IKE Phase 1 security association (SA) negotiations. You can list the algorithms in your order of preference.
       * `PH1_INTEGRITY_ALGRTHS`: a comma-separated list of integrity algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
       * `PH1_PRF_ALGRTHS`: a comma-separated list of Pseudo-Random Function (PRF) algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
       * `PH1_DH_GROUP`: a comma-separated list of Diffie-Hellman (DH) algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
       * `PH2_ENCRYPT_ALGRTHS`: a comma-separated list of encryption algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.
       * `PH2_INTEGRITY_ALGRTHS`: a comma-separated list of integrity algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.
       * `PH2_PFS_ALGRTHS`: a comma-separated list of PFS algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.

For policy-based VPN:

     * `LOCAL_IP_RANGES`: a comma-delimited list of the Google Cloud IP ranges. For example, you can supply the CIDR block for each subnet in a VPC network. This is the _left side_ from the perspective of Cloud VPN.
     * `REMOTE_IP_RANGES`: a comma-delimited list of the peer network IP ranges. This is the _right side_ from the perspective of Cloud VPN.

To configure a policy-based VPN tunnel, run the following command:
    
    gcloud compute vpn-tunnels create TUNNEL_NAME \
        --peer-address=ON_PREM_IP \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --local-traffic-selector=LOCAL_IP_RANGES \
        --remote-traffic-selector=REMOTE_IP_RANGES \
        --target-vpn-gateway=GW_NAME \
        --region=REGION \
        --project=PROJECT_ID
    

For route-based VPN, both the local and remote traffic selectors are `0.0.0.0/0` as defined in [routing options and traffic selectors](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#ts-tun-routing).

To configure a route-based VPN tunnel, run the following command:
    
    gcloud compute vpn-tunnels create TUNNEL_NAME \
        --peer-address=ON_PREM_IP \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --local-traffic-selector=0.0.0.0/0 \
        --remote-traffic-selector=0.0.0.0/0 \
        --target-vpn-gateway=GW_NAME \
        --region=REGION \
        --project=PROJECT_ID
    

You can also configure cipher algorithms for both policy-based and route-based tunnels. For example, to configure cipher algorithms for a policy-based tunnel, run the following command:
    
    gcloud compute vpn-tunnels create TUNNEL_NAME \
        --peer-address=ON_PREM_IP \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --local-traffic-selector=LOCAL_IP_RANGES \
        --remote-traffic-selector=REMOTE_IP_RANGES \
        --target-vpn-gateway=GW_NAME \
        --region=REGION \
        --project=PROJECT_ID \
        --phase1-encryption=PH1_ENCRYPT_ALGRTHS \
        --phase1-integrity=PH1_INTEGRITY_ALGRTHS \
        --phase1-prf=PH1_PRF_ALGRTHS \
        --phase1-dh=PH1_DH_GROUP \
        --phase2-encryption=PH2_ENCRYPT_ALGRTHS \
        --phase2-integrity=PH2_INTEGRITY_ALGRTHS \
        --phase2-pfs=PH2_PFS_ALGRTHS
    

To learn more about the cipher algorithms supported by Cloud VPN, see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).

  2. Create a static route for each remote IP range that you specified in the `--remote-traffic-selector` option in the previous step. Repeat this command for each remote IP range. Replace `ROUTE_NAME` with a unique name for the route, and replace `REMOTE_IP_RANGE` with the appropriate remote IP range.
         
         gcloud compute routes create ROUTE_NAME \
             --destination-range=REMOTE_IP_RANGE \
             --next-hop-vpn-tunnel=TUNNEL_NAME \
             --network=NETWORK \
             --next-hop-vpn-tunnel-region=REGION \
             --project=PROJECT_ID
         

**Note:** The `gcloud` command to create a route uses the default priority of `1000`. If you need to create a higher priority route, use the `--priority` flag with a _lower_ number _when you create the route_. You cannot change the priority of a route after the route has been created; however, you can delete and replace the custom static route without needing to re-create the VPN tunnel. For details about how routes work in your VPC network, see [Routes overview](https://docs.cloud.google.com/vpc/docs/routes) and [Order of routes](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes).



## Complete the configuration

Before you can use a new Cloud VPN gateway and its associated VPN tunnel, complete the following steps:

  1. Set up the peer VPN gateway and configure the corresponding tunnel there. For instructions, see the following: 
     * For specific configuration guidance for certain peer VPN devices, see [Use third-party VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides).
     * For general configuration parameters, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).
  2. [Configure firewall rules](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules) in Google Cloud and your peer network as required.
  3. [Check the status of your VPN tunnel and forwarding rules](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status).
  4. View your VPN routes by going to the project routing table and filtering for `Next hop type:VPN tunnel`:

[Go to Routes](https://console.cloud.google.com/networking/routes/list)




## What's next

  * To control which IP addresses are allowed for peer VPN gateways, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
