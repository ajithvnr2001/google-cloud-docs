---
url: https://docs.cloud.google.com/nat/docs/set-up-private-nat/
title: Set up and manage network address translation with Private NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:12.467069+00:00
---

# Set up and manage network address translation with Private NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/set-up-private-nat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up and manage network address translation with Private NAT

This page describes how to configure private-to-private network address translation (NAT) in Cloud NAT.

## Before you begin

Complete the following tasks before setting up Private NAT.

### Prepare your environment

Depending on whether you want to use the Google Cloud console or gcloud CLI to set up Private NAT, configure the following resources in Google Cloud.

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)




###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com




### Get IAM permissions

The [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) gives you permissions to create a NAT gateway, reserve and assign NAT IP addresses, and specify subnets whose traffic must use network address translation by the NAT gateway.

### Create a NAT subnet

Before you configure Private NAT, you create a NAT subnet of purpose `PRIVATE_NAT`. The NAT subnet must be in the same region where you plan to create your Private NAT gateway. The Private NAT gateway uses IP address ranges from this subnet to perform NAT. Ensure that this subnet doesn't overlap with an existing subnet in any of the connected networks. You cannot create any resource in this subnet. This subnet is used only for Private NAT.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To show the VPC network details page, click the name of a VPC network.

  3. Click the **Subnets** tab.

  4. Click **Add subnet**. In the **Add a subnet** dialog, do the following:

     1. Provide a name for the subnet.
     2. Select a region.
     3. For **Purpose** , select **Private NAT**.
     4. Enter an **IP address range** , which is the primary IPv4 range for the subnet.

If you select a range that isn't an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information about valid IPv4 subnet ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).

**Note:** IP address ranges that have privately used public IPv4 addresses aren't supported. For more information, see [VPC spokes and VPC Network Peering](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#vpc-peering).
  5. Click **Add**.




###  gcloud 

Use the [`gcloud compute networks subnet create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create) to create the subnet.
    
    
      gcloud compute networks subnets create NAT_SUBNET \
          --network=NETWORK \
          --region=REGION \
          --range=IP_RANGE \
          --purpose=PRIVATE_NAT
    

Replace the following:

  * `NAT_SUBNET`: the name of the Private NAT subnet range to create.
  * `NETWORK`: the network to which the subnetwork belongs.
  * `REGION`: the region of the subnetwork to create. If not specified, you might be prompted to select a region (interactive mode only).
  * `IP_RANGE`: the IP space allocated to this subnet in CIDR format. Ensure that `IP_RANGE` takes into account using twice the size of ports required per VM.



### Configure DNS64

To use translation from IPv6 to IPv4 ([NAT64](https://docs.cloud.google.com/nat/docs/private-nat#nat64)), destination addresses must match the `64:ff9b::/96` prefix. You can [configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64) to automatically synthesize IPv4-embedded IPv6 addresses by prepending this prefix to your destination IPv4 addresses.

Skip this step if you want to use Cloud NAT only for IPv4 traffic.

## Configure Private NAT

You configure Private NAT by creating a Cloud NAT gateway in the source VPC network. Each gateway is associated with a single VPC network, region, and Cloud Router.

When creating a Cloud NAT gateway for Private NAT, you can configure the following options.

Configuration | Supported options | Description  
---|---|---  
Source IP version | 

  * **IPv4 subnet ranges**
  * **IPv6 subnet ranges**

| Private NAT supports translation from IPv4 to IPv4 (NAT44) and from IPv6 to IPv4 (NAT64). You can configure the gateway to perform NAT44 or NAT64, but not both.

  * If you configure IPv4 subnet ranges, IPv4-only VM instances (in IPv4-only or dual-stack subnets) or dual-stack VM instances (in dual-stack subnets, using their IPv4 addresses) can communicate with IPv4 destinations.
  * If you configure IPv6 subnet ranges, IPv6-only VM instances in IPv6-only subnets or dual-stack subnets can communicate with IPv4 destinations.

  
Source subnets | For IPv4 traffic:

  * **Primary and secondary ranges for all subnets**
  * **Custom**

For IPv6 traffic:

  * **All subnets**
  * **Custom**

| Private NAT supports the following subnet ranges in the region for the VPC network that you specify:

  * For IPv4 traffic: primary and secondary ranges
  * For IPv6 traffic: internal and external ranges

You can restrict which subnets can use NAT.  
Connectivity type | 

  * **Network Connectivity Center hub**
  * **Hybrid connectivity routes**
  * **Source IPv6 traffic (for NAT64)**

| Private NAT supports the following options for NAT44:

  * [Private NAT for NCC spokes](https://docs.cloud.google.com/nat/docs/about-private-nat-for-ncc)
  * [Hybrid NAT](https://docs.cloud.google.com/nat/docs/about-hybrid-nat)

You can enable one or both of these options. For NAT64, the **Source IPv6 traffic (for NAT64)** option configures Private NAT for [all supported destinations](https://docs.cloud.google.com/nat/docs/private-nat#nat64).  
Advanced configurations | 

  * Dynamic or static port allocation
  * Logging
  * NAT timeouts

| By default, Private NAT uses dynamic port allocation, which lets the Cloud NAT gateway dynamically allocate ports to each VM based on usage. [Logging](https://docs.cloud.google.com/nat/docs/monitoring#logging) is disabled by default. For information about NAT timeouts and their default values, see [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).  
  
### Create a Cloud NAT gateway

Create a Cloud NAT gateway in the VPC network and region where you want to configure Private NAT. You can configure the gateway to apply NAT to IPv4 subnet ranges (NAT44) or IPv6 subnet ranges (NAT64), but not both.

#### Create a gateway for IPv4 ranges (NAT44)

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page. 

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or, if you have existing gateways, **Create Cloud NAT gateway**.
  3. Enter a gateway name.
  4. For **NAT type** , select **Private**.
  5. Select the VPC network and region where you want to create the gateway.
  6. Select or create a Cloud Router in the region.
  7. In the **Cloud NAT mapping** section, for **Source endpoint type** , make sure the **VM instances, GKE nodes, Serverless** option is selected.
  8. In the **Source IP version** field, select **IPv4 subnet ranges**.
  9. In the **Source subnets** field, select **Custom**.
  10. In the **Subnets** section, select a subnet for which you want to configure NAT. If you want to specify additional ranges, click **Add subnet and IP range** and add another subnet.
  11. Add at least one NAT rule. All NAT rules must be configured with the same next hop. 
     1. Click **Add a rule**.
     2. In the **Rule priority** field, enter a value from `0` (highest priority) to `65000` (lowest priority).

If you intend to configure more than one rule, choose a value that places this rule in the correct evaluation order compared to your other rules.

     3. For **Match** , select the Private NAT type that you want to enable. 
        * **Hybrid connectivity routes** : enables Hybrid NAT.
        * **Network Connectivity Center hub** : enables Private NAT for NCC spokes.
        * To enable both types of Private NAT, select **Hybrid connectivity routes** and **Network Connectivity Center hub**.
     4. Optional: Apply the rule to one or more source subnet ranges or individual IP addresses ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). For more information about source-based NAT rules, see [NAT rules for Private NAT](https://docs.cloud.google.com/nat/docs/nat-rules-overview#private-nat-rules). 
        * Select **Source IP ranges**.
        * Enter one or more source subnet ranges or IP addresses.
     5. Select or create a private NAT subnet range.
     6. Click **Done**.
  12. Optional: Configure additional NAT rules to match traffic based on both its source IP address and the next hop ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). For more information about source-based NAT rules, see [NAT rules for Private NAT](https://docs.cloud.google.com/nat/docs/nat-rules-overview#private-nat-rules). 
     1. Click **Add a rule**.
     2. In the **Rule priority** field, enter a value from `0` (highest priority) to `65000` (lowest priority).
     3. For **Match** , configure the exact same next hop options that you configured for your first rule. Then, apply the rule to one or more source subnet ranges or individual IP addresses: 
        * Select **Source IP ranges**.
        * Enter one or more source subnet ranges or IP addresses.
     4. Select or create a private NAT subnet range.
     5. Click **Done**.
  13. Optional: Adjust any of the following settings in the **Advanced configurations** section: 
     * Whether to configure logging. By default, **No logging** is selected.
     * Whether to change how Cloud NAT allocates ports. By default, **Enable Dynamic Port Allocation** is selected. To configure static port allocation, clear **Enable Dynamic Port Allocation** and specify **Minimum ports per VM instance**. The default value is `64`.
     * Whether to update NAT timeouts for protocol connections. For information about these timeouts and their default values, see [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts). 
  14. Click **Create**.



###  gcloud 

  1. Create a Cloud Router in the region of the VPC network where you want to configure Private NAT. You need this Cloud Router to create your gateway.

Use the [`gcloud compute routers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create).
         
         gcloud compute routers create ROUTER_NAME \
           --network=NETWORK --region=REGION
         

Replace the following:

     * `ROUTER_NAME`: a name for the Cloud Router
     * `NETWORK`: the VPC network in which to create the Cloud Router
     * `REGION`: the region in which to create the Cloud Router
  2. Create the gateway and specify one or more subnets of the VPC network where you want to configure NAT. By default, Private NAT uses dynamic port allocation.

Use the [`gcloud compute routers nats create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create) with the `--type=PRIVATE` flag.
         
         gcloud compute routers nats create NAT_CONFIG \
           --router=ROUTER_NAME \
           --region=REGION \
           --type=PRIVATE \
           --nat-custom-subnet-ip-ranges=SUBNETWORK:ALL,[SUBNETWORK_1:ALL,...]
         

Replace the following:

     * `NAT_CONFIG`: a name for your NAT configuration
     * `ROUTER_NAME`: the name of the Cloud Router that you created in the previous step
     * `REGION`: the region of the Cloud Router
     * `SUBNETWORK`: the name of the subnet or subnets (comma-separated) for which you want to use NAT

If you want to create a gateway with static port allocation, run the preceding command with the `--no-enable-dynamic-port-allocation` and `--min-ports-per-vm=VALUE` flags, replacing `VALUE` with the minimum number of ports. If the `--min-ports-per-vm` flag isn't specified, the default value is `64`.

  3. Create at least one NAT rule to match traffic based on the type of Private NAT that you are configuring. This rule must include the next hop.

You can optionally configure NAT rules, including the required rule, to match traffic based on both its source IP address and the next hop ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). All NAT rules that are added to the gateway must be configured with the same next hop. For more information about source-based NAT rules, see [NAT rules for Private NAT](https://docs.cloud.google.com/nat/docs/nat-rules-overview#private-nat-rules).

Use the [`gcloud compute routers nats rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/create) with the `--match` flag set to one of the following options:

Option | Description  
---|---  
`nexthop.hub == "HUB_RESOURCE_NAME"` | Enables Private NAT for NCC spokes.  
`nexthop.is_hybrid` | Enables Hybrid NAT.  
`nexthop.hub == "HUB_RESOURCE_NAME" || nexthop.is_hybrid` | Enables both types of Private NAT.  
`SOURCE_MATCH && NEXT_HOP` | Enables the Cloud NAT gateway to match traffic based on both its source IP address and the next hop ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).  
  
Where:

     * HUB_RESOURCE_NAME is the full resource name of the NCC hub.
     * SOURCE_MATCH is the expression that specifies which source IP addresses or ranges the NAT rule applies to.
     * NEXT_HOP is the expression that specifies the next hop.

To create a NAT rule for Private NAT for NCC spokes, run the following command:
    
    gcloud compute routers nats rules create NAT_RULE_PRIORITY \
      --router=ROUTER_NAME --region=REGION \
      --nat=NAT_CONFIG \
      --match='nexthop.hub == "//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/hubs/HUB"' \
      --source-nat-active-ranges=NAT_SUBNET
    

Replace the following:

     * `NAT_RULE_PRIORITY`: the rule number that uniquely identifies the NAT rule, from `0` (highest priority) to `65000` (lowest priority). If you intend to configure more than one rule, specify a value that places this rule in the correct evaluation order compared to your other rules.
     * `ROUTER_NAME`: the name of the Cloud Router that you created earlier.
     * `REGION`: the region of the Cloud Router.
     * `NAT_CONFIG`: the name of the NAT configuration that you created earlier.
     * `PROJECT_ID`: the Google Cloud project of the NCC hub.
     * `HUB`: the name of the NCC hub.
     * `NAT_SUBNET`: the name of the Private NAT subnet or subnets (comma-separated) that you created earlier.

To create a NAT rule for Hybrid NAT, run the following command:
    
    gcloud compute routers nats rules create NAT_RULE_PRIORITY \
      --router=ROUTER_NAME \
      --region=REGION \
      --nat=NAT_CONFIG \
      --match='nexthop.is_hybrid' \
      --source-nat-active-ranges=NAT_SUBNET
    

Replace the following:

     * `NAT_RULE_PRIORITY`: the rule number that uniquely identifies the NAT rule, from `0` (highest priority) to `65000` (lowest priority). If you intend to configure more than one rule, specify a value that places this rule in the correct evaluation order compared to your other rules.
     * `ROUTER_NAME`: the name of the Cloud Router that you created earlier.
     * `REGION`: the region of the Cloud Router.
     * `NAT_CONFIG`: the name of the NAT configuration that you created earlier.
     * `NAT_SUBNET`: the name of the Private NAT subnet or subnets (comma-separated) that you created earlier.

To create a NAT rule for both Private NAT for NCC spokes and Hybrid NAT, run the following command:
    
    gcloud compute routers nats rules create NAT_RULE_PRIORITY \
      --router=ROUTER_NAME \
      --region=REGION \
      --nat=NAT_CONFIG \
      --match='nexthop.hub == "//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/hubs/HUB" || nexthop.is_hybrid' \
      --source-nat-active-ranges=NAT_SUBNET
    

Replace the following:

     * `NAT_RULE_PRIORITY`: the rule number that uniquely identifies the NAT rule, from `0` (highest priority) to `65000` (lowest priority). If you intend to configure more than one rule, specify a value that places this rule in the correct evaluation order compared to your other rules.
     * `ROUTER_NAME`: the name of the Cloud Router that you created earlier.
     * `REGION`: the region of the Cloud Router.
     * `NAT_CONFIG`: the name of the NAT configuration that you created earlier.
     * `PROJECT_ID`: the Google Cloud project of the NCC hub.
     * `HUB`: the name of the NCC hub.
     * `NAT_SUBNET`: the name of the Private NAT subnet or subnets (comma-separated) that you created earlier.

To create a NAT rule to match traffic based on both the source IP address or range and the next hop ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), run the following command:
    
    gcloud beta compute routers nats rules create NAT_RULE_PRIORITY \
      --router=ROUTER_NAME \
      --region=REGION \
      --nat=NAT_CONFIG \
      --match='SOURCE_MATCH && NEXT_HOP' \
      --source-nat-active-ranges=NAT_SUBNET
    

Replace the following:

     * `NAT_RULE_PRIORITY`: the rule number that uniquely identifies the NAT rule, from `0` (highest priority) to `65000` (lowest priority). If you intend to configure more than one rule, specify a value that places this rule in the correct evaluation order compared to your other rules.
     * `ROUTER_NAME`: the name of the Cloud Router that you created earlier.
     * `REGION`: the region of the Cloud Router.
     * `NAT_CONFIG`: the name of the NAT configuration that you created earlier.
     * `SOURCE_MATCH`: the source match expression in the format `(SOURCE_1 || SOURCE_2 || ...)`, where each source is one of the following:

       * `source.ip == "IP_ADDRESS"`: matches a specific source IP address (for example, `source.ip == "10.10.10.1"`).
       * `inIpRange(source.ip, "IP_RANGE")`: matches a source IP address range (for example, `inIpRange(source.ip, "10.10.10.0/24")`).

For examples of match expressions that you can use, see [Examples for Private NAT](https://docs.cloud.google.com/nat/docs/nat-rules-overview#private-examples).

     * `NEXT_HOP`: the next hop, which can include one or both of the following options:

       * `nexthop.hub == "HUB_RESOURCE_NAME"`, where `HUB_RESOURCE_NAME` is the full resource name of the NCC hub.
       * `nexthop.is_hybrid`
     * `NAT_SUBNET`: the name of the Private NAT subnet or subnets (comma-separated) that you created earlier.




#### Create a gateway for IPv6 ranges (NAT64)

**Note:** Select IPv6 subnet ranges only if you are configuring NAT64 for Compute Engine VM instances. For GKE nodes, serverless endpoints, and regional internet NEGs, Private NAT translates only IPv4 addresses.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page. 

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or, if you have existing gateways, **Create Cloud NAT gateway**.
  3. Enter a gateway name.
  4. For **NAT type** , select **Private**.
  5. Select the VPC network and region where you want to create the gateway.
  6. Select or create a Cloud Router in the region.
  7. In the **Cloud NAT mapping** section, for **Source endpoint type** , make sure the **VM instances, GKE nodes, Serverless** option is selected.
  8. In the **Source IP version** field, select **IPv6 subnet ranges**. 
  9. In the **Source subnets** field, do one of the following: 
     * To use Cloud NAT for all IPv6 subnets in the region, select **All subnets**.
     * To restrict which subnets can use Cloud NAT, select **Custom** and then select a subnet. If you want to specify additional subnets, click **Add subnet** and add another subnet.
  10. Add a NAT rule to configure a private subnet range that you want to use for NAT: 
     1. Click **Add a rule**.
     2. In the **Rule priority** field, enter any value from `0` to `65000`.
     3. Select or create a private NAT subnet range. 
     4. Click **Done**.
  11. Optional: Adjust any of the following settings in the **Advanced configurations** section: 
     * Whether to configure logging. By default, **No logging** is selected.
     * Whether to change how Cloud NAT allocates ports. By default, **Enable Dynamic Port Allocation** is selected. To configure static port allocation, clear **Enable Dynamic Port Allocation** and specify **Minimum ports per VM instance**. The default value is `64`.
     * Whether to update NAT timeouts for protocol connections. For information about these timeouts and their default values, see [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).
  12. Click **Create**.



###  gcloud 

  1. Create a Cloud Router in the region of the VPC network where you want to configure Private NAT. You need this Cloud Router to create your gateway.

Use the [`gcloud compute routers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create).
         
         gcloud compute routers create ROUTER_NAME \
           --network=NETWORK --region=REGION
         

Replace the following:

     * `ROUTER_NAME`: a name for the Cloud Router
     * `NETWORK`: the VPC network in which to create the Cloud Router
     * `REGION`: the region in which to create the Cloud Router
  2. Create the Cloud NAT gateway.

Use the [`gcloud compute routers nats create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create) with the `--type=PRIVATE` flag.

     * To configure Private NAT for all IPv6 subnet ranges, run the following command:
           
           gcloud compute routers nats create NAT_CONFIG \
             --router=ROUTER_NAME \
             --region=REGION \
             --type=PRIVATE \
             --nat64-all-v6-subnet-ip-ranges
           

     * To configure Private NAT for custom IPv6 subnet ranges, run the following command:
           
           gcloud compute routers nats create NAT_CONFIG \
             --router=ROUTER_NAME \
             --region=REGION \
             --type=PRIVATE \
             --nat64-custom-v6-subnet-ip-ranges=SUBNETWORK,[SUBNETWORK_1,…]
           

Replace the following:

     * `NAT_CONFIG`: a name for your NAT configuration
     * `ROUTER_NAME`: the name of the Cloud Router that you created in the previous step
     * `REGION`: the region of the Cloud Router
     * `SUBNETWORK`: the name of the subnet or subnets (comma-separated) for which you want to use NAT
  3. Create a NAT rule for NAT64. Use the [`gcloud compute routers nats rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/create) with the `--match` flag.
         
         gcloud compute routers nats rules create NAT_RULE_PRIORITY \
           --router=ROUTER_NAME \
           --region=REGION \
           --nat=NAT_CONFIG \
           --match='isIPv6(source.ip)' \
           --source-nat-active-ranges=NAT_SUBNET
         

Replace the following:

     * `NAT_RULE_PRIORITY`: the rule number that uniquely identifies the NAT rule; specify any number from `0` to `65000`
     * `ROUTER_NAME`: the name of the Cloud Router that you created earlier
     * `REGION`: the region of the Cloud Router
     * `NAT_CONFIG`: the name of the NAT configuration that you created earlier
     * `NAT_SUBNET`: the name of the Private NAT subnet or subnets (comma-separated) that you created earlier



## View Private NAT configuration

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. To view NAT gateway details, mapping information, or configuration details, click the name of your NAT gateway.

  3. To view NAT status, see the **Status** column for your NAT gateway.




###  gcloud 

You can view the NAT configuration details by running the following commands:

  * View the Private NAT gateway configuration.
        
        gcloud compute routers nats describe NAT_CONFIG \
            --router=ROUTER_NAME \
            --region=REGION
        

Replace the following:

    * `NAT_CONFIG`: the name of your NAT configuration
    * `ROUTER_NAME`: the name of your Cloud Router
    * `REGION`: the region of the NAT to describe; if not specified, you might be prompted to select a region (interactive mode only)
  * View the mapping of the IP:port-ranges allocated to each VM's interface.
        
        gcloud compute routers get-nat-mapping-info ROUTER_NAME \
            --region=REGION
        

  * View the status of the Private NAT gateway.
        
        gcloud compute routers get-status ROUTER_NAME \
            --region=REGION
        




## Update a Private NAT configuration

The following sections describe how to update an existing Cloud NAT gateway.

### Update subnets in the NAT configuration

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your NAT gateway.

  3. Click edit**Edit**.

  4. If **Custom** is selected for **Source subnets** , select a subnet. To specify additional ranges, click **Add subnet and IP range**.

  5. IPv6 subnet ranges only: In the **Customized rule** section, select **Source IPv6 traffic (for NAT64)**.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

To update the source subnet ranges for an existing Cloud NAT gateway, run one of the following commands, depending on the IP version of the subnet ranges that you want to update:

  * Update IPv4 subnet ranges:
        
        gcloud compute routers nats update NAT_CONFIG \
            --router=NAT_ROUTER \
            --region=REGION \
            --nat-custom-subnet-ip-ranges=IPV4_SUBNET_RANGES
        

  * Update IPv6 subnet ranges:
        
        gcloud compute routers nats update NAT_CONFIG \
            --router=NAT_ROUTER \
            --region=REGION \
            --nat64-custom-v6-subnet-ip-ranges=IPV6_SUBNET_RANGES
        




Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration
  * `NAT_ROUTER`: the name of your Cloud Router
  * `REGION`: the region of the NAT gateway
  * `IPV4_SUBNET_RANGES`: a subnet or subnets in the following format: `SUBNET_NAME_1:ALL,SUBNET_NAME_2:ALL`.
  * `IPV6_SUBNET_RANGES`: a subnet or subnets in the following format: `SUBNET_NAME_1,SUBNET_NAME_2`.



### Remove subnets from the NAT configuration

You can remove subnets from your NAT gateway configuration.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your NAT gateway.

  3. Click edit**Edit**.

  4. Delete the subnet that you want to remove from NAT mapping.

**Note:** If the subnet that you deleted is the only subnet that is mapped to the Private NAT gateway, then the system prompts you to add a subnet.
  5. Click **Save**.




### Add NAT subnets to the configuration

To perform NAT on traffic, a Private NAT configuration uses NAT IP addresses from a subnet that has a purpose of `PRIVATE_NAT`. If your Private NAT configuration requires more than the available number of NAT IP addresses, you can add more subnets of purpose `PRIVATE_NAT` to the configuration.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your NAT gateway.

  3. Click edit**Edit**.

  4. Expand the existing rule.

  5. Click **Add subnet ranges**.

  6. Select or create a new NAT subnet range, and then click **Done**.

**Note:** To add more NAT subnets, repeat the step.
  7. Click **Save**.




###  gcloud 
    
    
    gcloud compute routers nats rules update NAT_RULE_PRIORITY \
        --nat=NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION \
        --source-nat-active-ranges=NAT_SUBNET_1, NAT_SUBNET_2 ...
    

Replace the following:

  * `NAT_RULE_PRIORITY`: the number that uniquely identifies the rule to update, from `0` to `65000`.
  * `NAT_CONFIG`: the name of your Private NAT configuration for the rule to update.
  * `ROUTER_NAME`: the name of the router to use with this gateway.
  * `NAT_SUBNET`: the names of the Private NAT subnets to be added to your existing NAT configuration.



## Delete NAT configuration

Deleting a gateway configuration removes the NAT configuration from a Cloud Router. Deleting a gateway configuration doesn't delete the router itself.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Select the checkbox next to the gateway configuration that you want to delete.

  3. On the more_vert**Menu** , click **Delete**.




###  gcloud 
    
    
    gcloud compute routers nats delete NAT_CONFIG \
        --router=ROUTER_NAME \
        --region=REGION
    

Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration
  * `ROUTER_NAME`: the name of your Cloud Router
  * `REGION`: the region of the NAT to delete; if not specified, you might be prompted to select a region (interactive mode only).



## What's next

  * [Logs and metrics](https://docs.cloud.google.com/nat/docs/monitoring)
  * [Troubleshoot configuration](https://docs.cloud.google.com/nat/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
