---
url: https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation/
title: Quickstart: Set up and manage network address translation with Public NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:20.981755+00:00
---

# Quickstart: Set up and manage network address translation with Public NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up and manage network address translation with Public NAT

This page describes how to set up and manage network address translation (NAT) by using Public NAT. Before setting up Public NAT, see the [Public NAT overview](https://docs.cloud.google.com/nat/docs/public-nat).

## Limitations

  * If you change the network tier of the automatically allocated IP addresses for a Cloud NAT gateway, all connections on the previously allocated IP addresses immediately close.

  * If you use manual NAT IP address allocation and you change the IP addresses that are used for Cloud NAT, all connections on the previously allocated IP addresses immediately close. To avoid this, see Drain external IP addresses associated with NAT.

  * If you configure a Cloud NAT gateway with static port allocation and you reduce the minimum ports per virtual machine (VM) instance, established NAT connections might be broken. For more information, see [Reducing ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-reducing).

  * If you configure a Cloud NAT gateway with dynamic port allocation and you make any further configuration changes, established NAT connections might be broken. When the configuration changes, the number of ports allocated to each VM might be temporarily reset to the minimum number configured. For more information, see [Reduce ports per VM](https://docs.cloud.google.com/nat/docs/ports-and-addresses#specs-reducing).

  * If you configure a Cloud NAT gateway with dynamic port allocation and then turn off dynamic port allocation, all VM connections that use the NAT gateway are closed. For more information, see [Switch port allocation method](https://docs.cloud.google.com/nat/docs/ports-and-addresses#switch-port-allocation).

  * If endpoint-independent mapping (EIM) is enabled, you can't configure dynamic port allocation or [NAT rules](https://docs.cloud.google.com/nat/docs/using-nat-rules).

  * Cloud NAT doesn't support IP fragments.

  * A Cloud NAT configuration is tied to a Virtual Private Cloud (VPC) network. So, the configuration applies to all the resources that belong to the subnets of that network. You can't choose specific VMs to be served by a Cloud NAT gateway.

  * [NAT64](https://docs.cloud.google.com/nat/docs/public-nat#nat64) is available only for IPv6-only Compute Engine VM instances, for the following machine series:

    * All second generation or earlier series
    * M3 series

For more information, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology).

For Google Kubernetes Engine (GKE) nodes, serverless endpoints, and regional internet network endpoint groups (NEGs), Public NAT translates only IPv4 addresses. For more information about which services in Google Cloud include IPv6-only support, see [IPv6 support in Google Cloud](https://docs.cloud.google.com/vpc/docs/ipv6-support).




## Before you begin

Complete the following tasks before setting up Public NAT.

### Get IAM permissions

The [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) includes the permissions that you need to configure Public NAT.

### Prepare your environment

Depending on whether you want to use the Google Cloud console or gcloud CLI to set up Public NAT, configure the following resources in Google Cloud.

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




### Configure DNS64

To use translation from IPv6 to IPv4 ([NAT64](https://docs.cloud.google.com/nat/docs/public-nat#nat64)), destination addresses must match the `64:ff9b::/96` prefix. You can [configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64) to automatically synthesize IPv4-embedded IPv6 addresses by prepending this prefix to your destination IPv4 addresses.

Skip this step if you want to use Cloud NAT only for IPv4 traffic.

## Configure Public NAT

You configure Public NAT by creating a Cloud NAT gateway in the source VPC network. Each gateway is associated with a single VPC network, region, and Cloud Router. Cloud NAT uses Cloud Router only to group NAT configuration information and doesn't direct Cloud Router to use Border Gateway Protocol or add routes. NAT traffic doesn't pass through Cloud Router.

When creating a Cloud NAT gateway, you can configure the following options.

Configuration | Supported options | Description  
---|---|---  
Source endpoint type | 

  * **VM instances, GKE nodes, Serverless**
  * **Managed proxy load balancers**

| By default, Public NAT provides NAT services to VM instances, GKE nodes, and serverless endpoints. To create a Cloud NAT gateway for these resources, complete the steps in the following section. To create a Cloud NAT gateway for a regional internet NEG, see "Set up a Cloud NAT gateway" for the following:

  * [Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend#nat-setup)
  * [Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-int-https-external-backend#nat-setup)
  * [Regional external proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-internet#nat-setup)
  * [Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-internet#nat-setup)

For a full list of Google Cloud resources that Cloud NAT supports, see [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview).  
Source IP version | 

  * **IPv4 subnet ranges**
  * **IPv6 subnet ranges**
  * **IPv4 and IPv6 subnet ranges**

| Public NAT supports translation from IPv4 to IPv4 and from IPv6 to IPv4.

  * If you configure IPv4 subnet ranges, IPv4-only VM instances and dual-stack VM instances (using their IPv4 addresses) in IPv4-only and dual-stack subnets can communicate with IPv4 destinations on the internet.
  * If you configure IPv6 subnet ranges, IPv6-only VM instances in IPv6-only and dual-stack subnets can communicate with IPv4 destinations on the internet.
  * If you configure IPv4 and IPv6 subnet ranges, the following applies: 
    * IPv4-only VM instances and dual-stack VM instances (using their IPv4 addresses) can communicate with IPv4 destinations on the internet.
    * Dual-stack VM instances can't use their IPv6 addresses to communicate with IPv4 destinations on the internet.
    * IPv6-only VM instances can communicate with IPv4 destinations on the internet.

  
Source subnets | For IPv4 traffic:

  * **Primary and secondary ranges for all subnets**
  * **Primary ranges for all subnets**
  * **Custom**

For IPv6 traffic:

  * **All subnets**
  * **Custom**

| Public NAT supports the following subnet ranges in the region for the VPC network that you specify:

  * For IPv4 traffic: primary and secondary ranges. You can restrict which subnets and subnet ranges can use NAT.
  * For IPv6 traffic: internal and external ranges. You can restrict which subnets can use NAT.

  
IP address allocation | 

  * **Automatic (recommended)**
  * **Manual**

| By default, Public NAT uses automatic NAT IP address allocation. This configuration automatically allocates the necessary external IP addresses to provide NAT services to a region. VM instances without external IP addresses in any subnet of the region are provided internet access through NAT. When you use automatic NAT IP address allocation, Google Cloud reserves IP addresses in your project. These addresses count against your [in-use regional external IPv4 address quotas](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_in_use_addresses) in the project. You can manually allocate NAT IP addresses for a Cloud NAT gateway. These addresses count against the following quotas:

  * [Static regional external IPv4 addresses](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_static_addresses)
  * [In-use regional external IPv4 addresses](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_in_use_addresses)

If you choose manual allocation, make sure to allocate enough IP addresses to avoid dropped packets. For more information, see [Public NAT IP addresses](https://docs.cloud.google.com/nat/docs/ports-and-addresses#addresses).  
Network tier | 

  * **Premium**
  * **Standard**

| Public NAT lets you specify the [Network Service Tiers](https://docs.cloud.google.com/network-tiers/docs/overview) from which the Cloud NAT gateway allocates external IP addresses. By default, the network tier is set to the current project-level tier. 

  * When creating a Cloud NAT gateway with automatic NAT IP address allocation, you can assign NAT IP addresses from either Premium Tier or Standard Tier.
  * When creating a Cloud NAT gateway with manual NAT IP address allocation, you can choose to manually assign NAT IP addresses from either Premium Tier or Standard Tier or both, subject to certain [conditions](https://docs.cloud.google.com/nat/docs/ports-and-addresses#assign-mixed-tier-ip).

  
Advanced configurations | 

  * Dynamic port allocation
  * Endpoint-independent mapping
  * Logging
  * NAT timeouts

| By default, Public NAT uses static port allocation, which means that each VM is allocated the same number of ports. You can configure dynamic port allocation with either automatic or manual NAT IP address allocation. Using dynamic port allocation lets the Cloud NAT gateway dynamically allocate ports to each VM based on usage. You can't enable [endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/public-nat#specs-rfcs) if your Cloud NAT gateway uses NAT rules or dynamic port allocation. [Logging](https://docs.cloud.google.com/nat/docs/monitoring#logging) is disabled by default. For information about NAT timeouts and their default values, see [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).  
  
### Create a Cloud NAT gateway

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** for the first Cloud NAT gateway or **Create Cloud NAT gateway** for subsequent gateways.

  3. In the **Gateway name** field, enter a name for the gateway.

  4. For **NAT type** , select **Public**.

  5. In the **Select Cloud Router** section, configure the following:

     1. In the **Network** field, select the VPC network in which you want to create the gateway.
     2. In the **Region** field, set the region for the gateway.
     3. In the **Cloud Router** field, select or create a Cloud Router in the region.
  6. In the **Cloud NAT mapping** section, for **Source endpoint type** , make sure the **VM instances, GKE nodes, Serverless** option is selected.

  7. In the **Source IP version** field, select the source IP version and then configure the source subnet ranges for which you want to use Cloud NAT.

**Note:** Select and configure IPv6 subnet ranges only if you are configuring NAT64 for Compute Engine VM instances. For GKE nodes, serverless endpoints, and regional internet NEGs, Public NAT translates only IPv4 addresses.
     * For IPv4 subnet ranges, in the **Source subnets** field, select one of the following: 
       * To use Cloud NAT for primary and secondary IP ranges for all subnets in the region, select **Primary and secondary IP ranges for all subnets**.
       * To use Cloud NAT only for primary IP ranges, select **Primary IP ranges for all subnets**.
       * To restrict which subnet IP ranges can use Cloud NAT, select **Custom** and do the following: 
         1. In the **Subnets** section, select a subnet.
         2. In the **IP ranges** list, select the subnet IP ranges to include and click **OK**.
         3. Optional: If you want to specify additional ranges, click **Add subnet and IP range** and add another subnet.
     * For IPv6 subnet ranges, in the **Source subnets** field, select one of the following: 
       * To use Cloud NAT for internal and external IP ranges for all subnets in the region, select **All subnets**.
       * To restrict which subnets can use Cloud NAT, select **Custom** and do the following: 
         1. In the **Subnets** section, select a subnet.
         2. Optional: If you want to specify additional subnets, click **Add subnet** and add another subnet.
  8. Configure the NAT IP address allocation type and network tier by selecting one of the following:

     * To use automatic NAT IP address allocation, do the following: 
       1. In the **Cloud NAT IP addresses** list, select **Automatic (recommended)**.
       2. For **Network service tier** , choose either **Premium** or **Standard**.
     * To use manual NAT IP address allocation, do the following: 
       1. In the **Cloud NAT IP addresses** list, select **Manual**.
       2. For **Network service tier** , choose either **Premium** or **Standard**.
       3. Select or create a static reserved external IP address to use for NAT.
       4. Optional: If you want to specify additional IP addresses, click **Add IP address** and then select or create an additional static reserved external IP address.
       5. Optional: If you want to create custom NAT rules, configure the **Cloud NAT rules** section. For an example configuration, see [Create NAT rules](https://docs.cloud.google.com/nat/docs/using-nat-rules#create_nat_rules).
  9. Optional: Adjust any of the following settings in the **Advanced configurations** section:

     * Whether to configure logging. By default, **No logging** is selected.
     * Whether to change how Cloud NAT allocates ports. By default, **Enable Dynamic Port Allocation** is deselected. For static port allocation, the **Minimum ports per VM instance** field is set to `64`. 
       * To update the minimum number of ports per VM instance for static port allocation, specify a value in the **Minimum ports per VM instance** field. This value can be set from `2` to `57344`.
       * To configure dynamic port allocation, select **Enable Dynamic Port Allocation** and select a value for the **Minimum ports per VM instance** field (default is `32`) and the **Maximum ports per VM instance** field (default is `65536`).
     * Whether to update NAT timeouts for protocol connections. For information about these timeouts and their default values, see [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).
  10. Click **Create**.




###  gcloud 

To create a Cloud NAT gateway, use the [`gcloud compute routers nats create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create). You can create a Cloud NAT gateway with all of its configuration options set to their default values, or you can customize your gateway configuration.

  * Create a Cloud NAT gateway with default settings
  * Customize configuration settings for a Cloud NAT gateway



#### Create a Cloud NAT gateway with default settings

  1. [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network#gcloud) in the region of the VPC network where you want to use the Cloud NAT gateway. You need this Cloud Router to create your Cloud NAT gateway.

  2. Create the Cloud NAT gateway by running one of the following commands, depending on the IP version of the source subnet ranges for which you are configuring NAT.

**Note:** Configure NAT for IPv6 subnet ranges only if you are configuring NAT64 for Compute Engine VM instances. For GKE nodes, serverless endpoints, and regional internet NEGs, Public NAT translates only IPv4 addresses.
     * Configure Cloud NAT for IPv4 subnet ranges:
           
           gcloud compute routers nats create NAT_CONFIG \
               --router=NAT_ROUTER \
               --region=REGION \
               --nat-all-subnet-ip-ranges \
               --auto-allocate-nat-external-ips
           

This configuration enables NAT for all IPv4 subnet ranges in IPv4-only and dual-stack subnets in the region.

     * Configure Cloud NAT for IPv6 subnet ranges:
           
           gcloud compute routers nats create NAT_CONFIG \
               --router=NAT_ROUTER \
               --region=REGION \
               --nat64-all-v6-subnet-ip-ranges \
               --auto-allocate-nat-external-ips
           

This configuration enables NAT for all IPv6 subnet ranges in IPv6-only and dual-stack subnets in the region.

     * Configure Cloud NAT for both IPv4 and IPv6 subnet ranges:
           
           gcloud compute routers nats create NAT_CONFIG \
               --router=NAT_ROUTER \
               --region=REGION \
               --nat-all-subnet-ip-ranges \
               --nat64-all-v6-subnet-ip-ranges \
               --auto-allocate-nat-external-ips
           

This configuration enables NAT for all IPv4 and IPv6 subnet ranges in IPv4-only, dual-stack, and IPv6-only subnets in the region.

Replace the following:

     * `NAT_CONFIG`: a name for your NAT configuration
     * `NAT_ROUTER`: the name of the Cloud Router that you created in the previous step
     * `REGION`: the region where you want to use the Cloud NAT gateway



#### Customize configuration settings for a Cloud NAT gateway

When creating a Cloud NAT gateway, you can customize its default configuration. For a full list of flags that you can use, see the [`gcloud compute routers nats create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create).

Create a Cloud NAT gateway for IPv6 subnet ranges only if you are configuring NAT64 for Compute Engine VM instances. For GKE nodes, serverless endpoints, and regional internet NEGs, Public NAT translates only IPv4 addresses.

Create a Cloud NAT gateway:

  1. [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network#gcloud) in the region the VPC network where you want to use the Cloud NAT gateway. You need this Cloud Router to create your Cloud NAT gateway.

  2. Create the Cloud NAT gateway, specifying each parameter that you want to customize.

The following examples show how to customize the source subnets, NAT IP address allocation type, network tier, and the port allocation type.

The command that you run in each of these examples depends on the IP version of the source subnet ranges for which you are configuring NAT.

     * **Restrict which source subnets can use NAT**. To create a Cloud NAT gateway that restricts which subnets and subnet ranges can use NAT, run one of the following commands:

       * Restrict which IPv4 subnet ranges can use NAT:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat-custom-subnet-ip-ranges=IPV4_SUBNET_RANGES \
                 --auto-allocate-nat-external-ips
             

       * Restrict which IPv6 subnet ranges can use NAT:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat64-custom-v6-subnet-ip-ranges=IPV6_SUBNET_RANGES \
                 --auto-allocate-nat-external-ips
             

       * Restrict both IPv4 and IPv6 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat-custom-subnet-ip-ranges=IPV4_SUBNET_RANGES \
                 --nat64-custom-v6-subnet-ip-ranges=IPV6_SUBNET_RANGES \
                 --auto-allocate-nat-external-ips
             

Replace the following:

       * `NAT_CONFIG`: a name for your NAT configuration
       * `NAT_ROUTER`: the name of the Cloud Router that you created in the previous step
       * `REGION`: the region where you want to use the Cloud NAT gateway
       * `IPV4_SUBNET_RANGES`: a comma-separated list of subnet names—for example: 
         * `SUBNET_NAME_1:ALL,SUBNET_NAME_2:ALL`: includes both the primary and all secondary ranges of subnets `SUBNET_NAME_1` and `SUBNET_NAME_2`.
         * `SUBNET_NAME_1,SUBNET_NAME_2`: includes only the primary ranges of subnets `SUBNET_NAME_1` and `SUBNET_NAME_2`.
         * `SUBNET_NAME:SECONDARY_RANGE_NAME`: includes the specified secondary range of subnet `SUBNET_NAME` and doesn't include the primary range
         * `SUBNET_NAME_1,SUBNET_NAME_2:SECONDARY_RANGE_NAME`: includes the primary range of subnet `SUBNET_NAME_1` and the specified secondary range of subnet `SUBNET_NAME_2`
       * `IPV6_SUBNET_RANGES`: a comma-separated list of subnet names—for example, `SUBNET_NAME_1,SUBNET_NAME_2`
     * **Configure manual NAT IP address allocation**. To create a Cloud NAT gateway with manual NAT IP address allocation, run one of the following commands:

       * For IPv4 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat-all-subnet-ip-ranges \
                 --nat-external-ip-pool=IP_ADDRESS_1,IP_ADDRESS_2
             

       * For IPv6 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat64-all-v6-subnet-ip-ranges \
                 --nat-external-ip-pool=IP_ADDRESS_1,IP_ADDRESS_2
             

If you are creating the gateway for IPv4 and IPv6 subnet ranges, specify both the `--nat-all-subnet-ip-ranges` and `--nat64-all-v6-subnet-ip-ranges` flags in this command.

Replace the following:

       * `NAT_CONFIG`: a name for your NAT configuration
       * `NAT_ROUTER`: the name of the Cloud Router that you created in the previous step
       * `REGION`: the region where you want to use the Cloud NAT gateway
       * `IP_ADDRESS_1` and `IP_ADDRESS_2`: the static reserved external IP addresses that you want to use for NAT

You can specify one or more IP addresses when using the `--nat-external-ip-pool` flag.

     * **Specify the network tier**. To specify the network tier from which the Cloud NAT gateway allocates external IP addresses, run one of the following commands:

       * For IPv4 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat-all-subnet-ip-ranges \
                 --auto-allocate-nat-external-ips \
                 --auto-network-tier=AUTO_NETWORK_TIER
             

       * For IPv6 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat64-all-v6-subnet-ip-ranges \
                 --auto-allocate-nat-external-ips \
                 --auto-network-tier=AUTO_NETWORK_TIER
             

If you are creating the gateway for IPv4 and IPv6 subnet ranges, specify both the `--nat-all-subnet-ip-ranges` and `--nat64-all-v6-subnet-ip-ranges` flags in this command.

Replace the following:

       * `NAT_CONFIG`: a name for your NAT configuration
       * `NAT_ROUTER`: the name of the Cloud Router that you created in the previous step
       * `REGION`: the region where you want to use the Cloud NAT gateway
       * `AUTO_NETWORK_TIER`: the network tier to use when automatically allocating IP addresses for the Cloud NAT gateway. The allowed values are `PREMIUM` and `STANDARD`. If not specified, then the current [project-level default](https://docs.cloud.google.com/network-tiers/docs/set-network-tier#setting_the_tier_for_all_resources_in_a_project) tier is associated with the Cloud NAT gateway.

You can also specify the network tier with manual NAT IP addresses allocation. If you assign multiple IP addresses to the gateway, all the IP addresses that you assign must be from the same network tier.

     * **Configure dynamic port allocation**. To create a Cloud NAT gateway with dynamic port allocation, run one the following commands:

       * For IPv4 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat-all-subnet-ip-ranges \
                 --auto-allocate-nat-external-ips \
                 --enable-dynamic-port-allocation \
                 [--min-ports-per-vm=MIN_PORTS ] \
                 [--max-ports-per-vm=MAX_PORTS ]
             

       * For IPv6 subnet ranges:
             
             gcloud compute routers nats create NAT_CONFIG \
                 --router=NAT_ROUTER \
                 --region=REGION \
                 --nat64-all-v6-subnet-ip-ranges \
                 --auto-allocate-nat-external-ips \
                 --enable-dynamic-port-allocation \
                 [--min-ports-per-vm=MIN_PORTS ] \
                 [--max-ports-per-vm=MAX_PORTS ]
             

If you are creating the gateway for IPv4 and IPv6 subnet ranges, specify both the `--nat-all-subnet-ip-ranges` and `--nat64-all-v6-subnet-ip-ranges` flags in this command.

Replace the following:

       * `NAT_CONFIG`: a name for your NAT configuration
       * `NAT_ROUTER`: the name of the Cloud Router that you created in the previous step
       * `REGION`: the region where you want to use the Cloud NAT gateway
       * Optional: `MIN_PORTS`: the minimum number of ports to allocate for each VM. If dynamic port allocation is enabled, `MIN_PORTS` must be a power of `2` and can be between `32` and `32768`. The default is `32`.
       * Optional: `MAX_PORTS`: the maximum number of ports to allocate for each VM. `MAX_PORTS` must be a power of `2` and can be between `64` and `65536`. `MAX_PORTS` must be greater than `MIN_PORTS`. The default is `65536`.



### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-cloud-router) to create a Cloud Router with a NAT gateway for IPv4 traffic.
    
    
    module "cloud_router" {
      source = "../.."
    
      name       = "my-cloud-router"
      project_id = var.project_id
      network    = module.vpc.network_name
      region     = "us-central1"
    
      nats = [{
        name                               = "my-nat-gateway"
        source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
        subnetworks = [
          {
            name                     = module.vpc.subnets["us-central1/test-subnet-01-1"].id
            source_ip_ranges_to_nat  = ["PRIMARY_IP_RANGE", "LIST_OF_SECONDARY_IP_RANGES"]
            secondary_ip_range_names = module.vpc.subnets["us-central1/test-subnet-01-1"].secondary_ip_range[*].range_name
          }
        ]
      }]
    }

The resulting NAT gateway uses the following default values:
    
    
    enable_endpoint_independent_mapping = true
    icmp_idle_timeout_sec               = 30
    min_ports_per_vm                    = 0
    nat_ip_allocate_option              = "AUTO_ONLY"
    source_subnetwork_ip_ranges_to_nat  = "ALL_SUBNETWORKS_ALL_IP_RANGES"
    tcp_established_idle_timeout_sec    = 1200
    tcp_transitory_idle_timeout_sec     = 30
    udp_idle_timeout_sec                = 30
    log_config {
        enable = true
        filter = "ALL"
    }
    

## View a Public NAT configuration

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. To view NAT gateway details, mapping information, or configuration details, click the name of your NAT gateway.

  3. To view NAT status, see the **Status** column for your NAT gateway.




###  gcloud 

You can view the NAT configuration details by running the following commands:

  * View the Public NAT gateway configuration.
        
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
        

  * View the status of the Public NAT gateway.
        
        gcloud compute routers get-status ROUTER_NAME \
            --region=REGION
        




### View external IP addresses assigned to a Cloud NAT gateway

By default, Cloud NAT gateways for Public NAT use automatic IP address allocation. To view the external IP addresses that are assigned to a Cloud NAT gateway, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click the name of your Cloud NAT gateway.

  3. On the **Cloud NAT gateway details** page, view **Allocated external IP addresses**.




###  gcloud 

To list all allocated NAT IP addresses, use the following command:
    
    
    gcloud compute routers get-nat-ip-info NAT_ROUTER \
        --region=REGION
    

For more examples, see the [`gcloud compute routers get-nat-ip-info` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info).

## Update a Public NAT configuration

The following sections describe how to update an existing Cloud NAT gateway.

### Update subnets in the NAT configuration

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. If **Custom** is selected for **Source subnets** , do the following:

     * IPv4 subnet ranges: select a subnet and the **IP ranges** to include.
     * IPv6 subnet ranges: select a subnet.
  5. Optional: If you want to specify additional ranges, click **Add subnet and IP range**.

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
        

  * Update both IPv4 and IPv6 subnet ranges:
        
        gcloud compute routers nats update NAT_CONFIG \
            --router=NAT_ROUTER \
            --region=REGION \
            --nat-custom-subnet-ip-ranges=IPV4_SUBNET_RANGES \
            --nat64-custom-v6-subnet-ip-ranges=IPV6_SUBNET_RANGES
        




Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration
  * `NAT_ROUTER`: the name of your Cloud Router
  * `REGION`: the region of the NAT gateway
  * `IPV4_SUBNET_RANGES`: a subnet or comma-separated list of subnets—for example: 
    * `SUBNET_NAME_1:ALL,SUBNET_NAME_2:ALL`: includes both the primary and all secondary ranges of subnets `SUBNET_NAME_1` and `SUBNET_NAME_2`.
    * `SUBNET_NAME_1,SUBNET_NAME_2`: includes only the primary ranges of subnets `SUBNET_NAME_1` and `SUBNET_NAME_2`.
    * `SUBNET_NAME:SECONDARY_RANGE_NAME`: includes the specified secondary range of subnet `SUBNET_NAME` and doesn't include the primary range
    * `SUBNET_NAME_1,SUBNET_NAME_2:SECONDARY_RANGE_NAME`: includes the primary range of subnet `SUBNET_NAME_1` and the specified secondary range of subnet `SUBNET_NAME_2`
  * `IPV6_SUBNET_RANGES`: a comma-separated list of subnet names—for example, `SUBNET_NAME_1,SUBNET_NAME_2`



### Remove subnets from the NAT configuration

You can remove subnets from the Cloud NAT gateway that are no longer in use.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Delete the subnet that you want to remove from NAT mapping.

**Note:** If the subnet that you deleted is the only subnet that is mapped to the Public NAT gateway, then the system prompts you to add a subnet.
  5. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

You can remove only IPv4 subnet ranges or IPv6 subnet ranges, but not both.

The following example disables NAT for IPv6 subnet ranges:
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=NAT_ROUTER \
        --region=REGION \
        --clear-nat64-subnet-ip-ranges
    

Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration
  * `NAT_ROUTER`: the name of your Cloud Router
  * `REGION`: the region of the NAT gateway



### Update external IP addresses assigned to NAT

You can change the list of external IP addresses for a given gateway or switch from manual to automatic IP allocation. When you do, Google Cloud removes the previously allocated IP addresses and adds the new ones. Any existing connections on the previously allocated IP addresses immediately close. To let existing connections continue while preventing new connections on those IP addresses, see the Drain external IP addresses associated with NAT section of this document.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click the **NAT IP addresses** list, and then select **Automatic** or **Manual**.

  5. If you select **Manual** , specify an external **IP address**.

  6. For high availability, click **Add IP address** , and then add a second address.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=NAT_ROUTER \
        --region=REGION \
        --nat-external-ip-pool=IP_ADDRESS_1,IP_ADDRESS_2
    

Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration.
  * `NAT_ROUTER`: the name of your Cloud Router.
  * `REGION`: the region of the NAT to update. If not specified, you might be prompted to select a region (interactive mode only).
  * `IP_ADDRESS_1`: a manual external IP address.
  * `IP_ADDRESS_2`: another manual external IP address.

**Important:** To update multiple gateway IP addresses at the same time, you can use the `nat-external-ip-pool` flag. However, all the new IP addresses that you assign must be from the same network tier.

### Update NAT by using external IP addresses from a different network tier

You can update an existing Cloud NAT gateway by changing the network tier of the external IP addresses associated with the gateway.

#### Update NAT by changing the network tier of automatically allocated external IP addresses

When you change the network tier of automatically allocated external IP addresses associated with an existing Cloud NAT gateway, Google Cloud removes the previously allocated IP addresses and replaces them with IP addresses from the specified network tier. Any existing connections on the previously allocated IP addresses immediately close.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway name that has automatically allocated IP addresses.

  3. Click edit**Edit**.

  4. For **Network service tier** , choose either **Premium** or **Standard**.

  5. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=NAT_ROUTER \
        --region=REGION \
        --auto-allocate-nat-external-ips
        --auto-network-tier=AUTO_NETWORK_TIER
    

Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration

  * `NAT_ROUTER`: the name of your Cloud Router

  * `REGION`: the region of the NAT to create; if not specified, you might be prompted to select a region (interactive mode only)

  * `AUTO_NETWORK_TIER`: the network tier to use when automatically allocating IP addresses for the Cloud NAT gateway. The allowed values are `PREMIUM` and `STANDARD`. If not specified, then the current [project-level default](https://docs.cloud.google.com/network-tiers/docs/set-network-tier#setting_the_tier_for_all_resources_in_a_project) tier is associated with the Cloud NAT gateway.




#### Update NAT by changing the network tier of manually assigned IP addresses

You can update an existing NAT by manually specifying external IP addresses from a different tier. You can assign external IP addresses from either Standard Tier or Premium Tier or both, subject to [certain conditions](https://docs.cloud.google.com/nat/docs/ports-and-addresses#assign-mixed-tier-ip). Before you specify external IP addresses from a different tier, first drain the existing IP addresses to let existing connections continue and prevent new connections on the existing IP addresses.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway name that has manually assigned IP addresses.

  3. Click edit**Edit**.

  4. To specify IP addresses from a tier that is different from the selected tier, either delete all the existing IP addresses or enable draining for all the existing IP addresses.

You can't change the network tier if draining is disabled for an existing IP address.

  5. For **Network service tier** , choose either **Premium** or **Standard**.

  6. Select an external IP address from the list of active, available IP addresses.

**Note:** Draining is always disabled for a newly selected IP address.
  7. Optional: To add more IP addresses, click **Add IP addresses**.

  8. Click **Save**.




###  gcloud 

To update an existing gateway by manually changing the existing external IP addresses with new ones from a different network tier, use the `--nat-external-ip-pool` flag of the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

For more information about manually changing the existing external IP addresses, see Update external IP addresses associated with NAT.

### Drain external IP addresses assigned to NAT

Before you remove a manually configured IP address, you can _drain_ it so that existing connections aren't disrupted. When an IP address is drained, all existing connections continue until they expire naturally. You can [view the logs](https://docs.cloud.google.com/nat/docs/monitoring) to check the status of existing connections.

No new connections are accepted on the drained IP addresses. However, the IP address stays associated with the NAT configuration.

You must have at least one active address in a NAT configuration, which means that you can't drain all IP addresses in a configuration.

To see the state of your NAT IP addresses, view Public NAT configuration.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. For **NAT IP addresses** , set the **IP draining** value next to the IP address to **On**.

  5. Click **Save**.


**Note:** If you want to make an existing draining IP address active, you can set the **IP draining** value next to the IP address to **Off**. However, if the selected network tier isn't the same as the tier of the draining IP address, you can't disable draining.

###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).

To drain an address, you must move it from the active pool to the drain pool in the same command. If you remove it from the active pool without adding it to the drain pool in a single command, the IP address is deleted from service and existing connections are terminated immediately.

If you move an IP address from the drain pool to the active pool, you undrain the IP address. If you remove a NAT IP address from both pools, you disconnect it from the NAT configuration.

This command leaves the other fields in the NAT configuration unchanged.
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=NAT_ROUTER \
        --region=REGION \
        --nat-external-ip-pool=IP_ADDRESS_2 \
        --nat-external-drain-ip-pool=IP_ADDRESS_1
    

Where:

  * `--nat-external-ip-pool=IP_ADDRESS_2`: updates the active pool to omit `IP_ADDRESS_1`
  * `--nat-external-drain-ip-pool=IP_ADDRESS_1`: adds `IP_ADDRESS_1` to the drain pool



Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration.
  * `NAT_ROUTER`: the name of your Cloud Router.
  * `REGION`: the region of the NAT to update. If not specified, you might be prompted to select a region (interactive mode only).
  * `IP_ADDRESS_2`: an IP address.
  * `IP_ADDRESS_1`: another IP address.



### Update endpoint mapping

You can enable or disable [endpoint-independent mapping](https://docs.cloud.google.com/nat/docs/ports-and-addresses#ports-reuse-endpoints) for your gateway. By default, this option is disabled. Switching endpoint-independent mapping from enabled to disabled (or from disabled to enabled) doesn't interrupt existing connections.

You can't enable endpoint-independent mapping if your Cloud NAT gateway uses NAT rules or dynamic port allocation.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click your Cloud NAT gateway.

  3. Click edit**Edit**.

  4. Click **Advanced configurations**.

  5. To enable endpoint-independent mapping, select the **Enable Endpoint-Independent Mapping** checkbox. To disable endpoint-independent mapping, clear the checkbox.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute routers nats update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update).
    
    
    gcloud compute routers nats update NAT_CONFIG \
        --router=NAT_ROUTER \
        --region=REGION \
        [--enable-endpoint-independent-mapping | --no-enable-endpoint-independent-mapping]
    

Replace the following:

  * `NAT_CONFIG`: the name of your NAT configuration
  * `NAT_ROUTER`: the name of your Cloud Router
  * `REGION`: the region of the NAT to update; if not specified, you might be prompted to select a region (interactive mode only)



### Update logging

To add, modify, or remove logging for an existing Cloud NAT gateway, see [Configuring logging](https://docs.cloud.google.com/nat/docs/monitoring#configuring_logging).

## Delete a Public NAT configuration

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



## Quotas and limits

For quota and limit information, see [Quotas and limits](https://docs.cloud.google.com/nat/quota).

## Example setups

  * [Use Public NAT with Compute Engine](https://docs.cloud.google.com/nat/docs/gce-example)
  * [Use Public NAT with GKE](https://docs.cloud.google.com/nat/docs/gke-example)
  * [Configure IPv6-only subnets and instances with DNS64 and NAT64](https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4)



## What's next

  * [Logs and metrics](https://docs.cloud.google.com/nat/docs/monitoring)
  * [Troubleshoot configuration](https://docs.cloud.google.com/nat/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
