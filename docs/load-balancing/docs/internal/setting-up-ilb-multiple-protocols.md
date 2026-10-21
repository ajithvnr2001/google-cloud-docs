---
url: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols/
title: Set up an internal passthrough Network Load Balancer with VM instance group backends for multiple protocols \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:33.690733+00:00
---

# Set up an internal passthrough Network Load Balancer with VM instance group backends for multiple protocols  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up an internal passthrough Network Load Balancer with VM instance group backends for multiple protocols Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for creating internal passthrough Network Load Balancers to load balance traffic for multiple protocols.

To configure a load balancer for multiple protocols, including TCP and UDP, you create a [forwarding rule with the protocol set to `L3_DEFAULT`](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding-rule-protocols). This forwarding rule points to a [backend service with the protocol set to `UNSPECIFIED`](https://docs.cloud.google.com/load-balancing/docs/internal#backend-service).

In this example, we use one internal passthrough Network Load Balancer to distribute traffic across a backend VM in the `us-west1` region. The load balancer has a forwarding rule with protocol `L3_DEFAULT` to handle TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE .

[ ![Load balancing IPv4 and IPv6 traffic based on the protocols, with
    backend services to manage connection distribution to a single zonal
    instance group.](https://docs.cloud.google.com/static/load-balancing/images/ilb-all-protocols-l3-default.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-all-protocols-l3-default.svg) Internal passthrough Network Load Balancer for multiple protocols (click to enlarge).

## Before you begin

  * Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [API and gcloud CLI references](https://docs.cloud.google.com/load-balancing/docs/apis). If you haven't run the gcloud CLI previously, first run the [`gcloud init` command](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.
  * Learn about [bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)).



## Permissions

To get the permissions that you need to complete this guide, ask your administrator to grant you the following IAM roles on the project: 

  * To create load balancer resources: [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) 
  * To create Compute Engine instances and instance groups: [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 
  * To create networking components: [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to complete this guide. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Set up load balancer for L3_DEFAULT traffic

The steps in this section describe the following configurations:

  * An example that uses a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`. You can use an auto mode network if you only want to handle IPv4 traffic. However, IPv6 traffic [requires a custom mode subnet](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications).
  * A _single-stack_ subnet (`stack-type` set to `IPv4`), which is required for IPv4 traffic. When you create a single-stack subnet on a custom mode VPC network, you choose an [IPv4 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) for the subnet. For IPv6 traffic, we require a _dual-stack_ subnet (`stack-type` set to `IPV4_IPV6`). When you create a dual stack subnet on a custom mode VPC network, you choose an [IPv6 access type](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) for the subnet. For this example, we set the subnet's `ipv6-access-type` parameter to `INTERNAL`. This means new VMs on this subnet can be assigned both internal IPv4 addresses and internal IPv6 addresses.
  * Firewall rules that allow incoming connections to backend VMs.
  * The backend instance group and the load balancer components used for this example are located in this region and subnet: 
    * Region: `us-west1`
    * Subnet: `lb-subnet`, with primary IPv4 address range `10.1.2.0/24`. Although you choose which IPv4 address range is configured on the subnet, the IPv6 address range is assigned automatically. Google provides a fixed size (/64) IPv6 CIDR block.
  * A backend VM in a managed instance group in zone `us-west1-a`.
  * A client VM to test connections to the backends.
  * An internal passthrough Network Load Balancer with the following components: 
    * A health check for the backend service.
    * A backend service in the `us-west1` region with the protocol set to `UNSPECIFIED` to manage connection distribution to the zonal instance group.
    * A forwarding rule with the protocol set to `L3_DEFAULT` and the port set to `ALL`.

**Note:** You can change the name of the network, the region, and the parameters for the subnet. However, subsequent steps in this guide use the network, region, and subnet parameters as outlined in the preceding list.

### Configure a network, region, and subnet

To configure subnets with internal IPv6 ranges, enable a Virtual Private Cloud (VPC) network ULA internal IPv6 range. Internal IPv6 subnet ranges are allocated from this range. To create the example network and subnet, follow these steps:

###  Console 

To support both **IPv4 and IPv6 traffic** , use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. If you want to configure internal IPv6 address ranges on subnets in this network, complete these steps:

     1. For **VPC network ULA internal IPv6 range** , select **Enabled**.
     2. For **Allocate internal IPv6 range** , select **Automatically** or **Manually**. 

**Pro Tip** : If you select **Manually** , enter a `/48` range from within the `fd20::/20` range. If the range is in use, you are prompted to provide a different range.

  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. For **Name** , enter `lb-subnet`.
     2. For **Region** , select `us-west1`.
     3. To create a dual-stack subnet, for **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.
     4. For **IPv4 range** , enter `10.1.2.0/24`.
     5. For **IPv6 access type** , select **Internal**.
  7. Click **Done**.

  8. Click **Create**.




To support **IPv4 traffic** , use the following steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section:

     * Set the **Subnet creation mode** to **Custom**.
     * In the **New subnet** section, enter the following information: 
       * **Name** : `lb-subnet`
       * **Region** : `us-west1`
       * **IP stack type** : **IPv4 (single-stack)**
       * **IP address range** : `10.1.2.0/24`
     * Click **Done**.
  5. Click **Create**.




###  gcloud 

For both **IPv4 and IPv6 traffic** , use the following commands:

  1. To create a new custom mode VPC network, run the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).

To configure _internal_ IPv6 ranges on any subnets in this network, use the `--enable-ula-internal-ipv6` flag. This option assigns a `/48` ULA prefix from within the `fd20::/20` range used by Google Cloud for internal IPv6 subnet ranges.
         
         gcloud compute networks create lb-network \
          --subnet-mode=custom \
          --enable-ula-internal-ipv6
         

  2. Within the `lb-network`, create a subnet for backends in the `us-west1` region.

To create the subnets, run the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create lb-subnet \
          --network=lb-network \
          --range=10.1.2.0/24 \
          --region=us-west1 \
          --stack-type=IPV4_IPV6 --ipv6-access-type=INTERNAL
         




For **IPv4 traffic only** , use the following commands:

  1. To create the custom VPC network, use the `gcloud compute networks create` command:
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. To create the subnet for backends in the `us-west1` region within the `lb-network` network, use the `gcloud compute networks subnets create` command.
         
         gcloud compute networks subnets create lb-subnet \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-west1
         




###  API 

For both **IPv4 and IPv6 traffic** , use the following commands:

  1. Create a new custom mode VPC network. Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert).

To configure _internal_ IPv6 ranges on any subnets in this network, set `enableUlaInternalIpv6` to `true`. This option assigns a `/48` range from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
         {
           "autoCreateSubnetworks": false,
           "name": "lb-network",
           "mtu": MTU,
           "enableUlaInternalIpv6": true,
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the VPC network is created.
     * `MTU`: the maximum transmission unit of the network. MTU can either be `1460` (default) or `1500`. Review the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu) before setting the MTU to `1500`.
  2. Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
         {
         "ipCidrRange": "10.1.2.0/24",
         "network": "lb-network",
         "name": "lb-subnet"
         "stackType": IPV4_IPV6,
         "ipv6AccessType": Internal
         }
         




For **IPv4 traffic only** , use the following steps:

  1. Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
         {
         "name": "lb-network",
         "autoCreateSubnetworks": false
         }
         

  2. Make two `POST` requests to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks
         {
         "name": "lb-subnet",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "ipCidrRange": "10.1.2.0/24",
         "privateIpGoogleAccess": false
         }
         




### Configure firewall rules

This example uses the following firewall rules:

  * `fw-allow-lb-access`: An ingress rule, applicable to all targets in the VPC network, that allows traffic from sources in the `10.1.2.0/24` ranges. This rule allows incoming traffic from any client located in the subnet.

  * `fw-allow-lb-access-ipv6`: An ingress rule, applicable to all targets in the VPC network, that allows traffic from sources in the IPv6 range configured in the subnet. This rule allows incoming IPv6 traffic from any client located in the subnet.

  * `fw-allow-ssh`: An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port 22 from any address. You can choose a more restrictive source IP range for this rule—for example, you can specify only the IP ranges of the system from which you are initiating SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it should apply.

  * `fw-allow-health-check`: An ingress rule, applicable to the instances being load balanced, that allows traffic from [Google Cloud health check ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the instances to which it should apply.

  * `fw-allow-health-check-ipv6`: An ingress rule, applicable to the instances being load balanced, that allows traffic from [Google Cloud health check ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check-ipv6` to identify the instances to which it should apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

**Note:** You must create a firewall rule to allow health checks from the IP ranges of Google Cloud probe systems. For more information, see [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow **IPv4 TCP, UDP, and ICMP traffic** to reach backend instance group `ig-a`:

     * Click **Create firewall rule**.
     * **Name** : `fw-allow-lb-access`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : Ingress
     * **Action on match** : Allow
     * **Targets** : All instances in the network
     * **Source filter** : IPv4 ranges
     * **Source IPv4 ranges** : `10.1.2.0/24`
     * **Protocols and ports** : select **Specified protocols and ports**. 
       * Select **TCP** and enter `ALL`.
       * Select **UDP**.
       * Select **Other** and enter `ICMP`.
  3. Click **Create**.

  4. To allow incoming SSH connections:

     * Click **Create firewall rule**.
     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : Ingress
     * **Action on match** : Allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-ssh`
     * **Source filter** : IPv4 ranges
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : choose **Specified protocols and ports** , and then type `tcp:22`.
  5. Click **Create**.

  6. To allow **IPv6 TCP, UDP, and ICMP traffic** to reach backend instance group `ig-a`:

     * Click **Create firewall rule**.
     * **Name** : `fw-allow-lb-access-ipv6`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : Ingress
     * **Action on match** : Allow
     * **Targets** : All instances in the network
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : IPV6_ADDRESS assigned in the `lb-subnet`
     * **Protocols and ports** : select **Specified protocols and ports**. 
       * Select **TCP** and enter `0-65535`.
       * Select **UDP**.
       * Select **Other** and for ICMPv6 protocol enter `58`.
  7. Click **Create**.

  8. To allow Google Cloud IPv6 health checks:

     * Click **Create firewall rule**.
     * **Name** : `fw-allow-health-check-ipv6`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : Ingress
     * **Action on match** : Allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-health-check-ipv6`
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `2600:2d00:1:b029::/64`
     * **Protocols and ports** : Allow all
  9. Click **Create**.

  10. To allow Google Cloud IPv4 health checks:

     * Click **Create firewall rule**
     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : Ingress
     * **Action on match** : Allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-health-check`
     * **Source filter** : IPv4 ranges
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : Allow all
  11. Click **Create**.




###  gcloud 

  1. To allow **IPv4 TCP traffic** to reach backend instance group `ig-a`, create the following rule:
         
         gcloud compute firewall-rules create fw-allow-lb-access \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.1.2.0/24 \
             --rules=tcp,udp,icmp
         

  2. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs by using the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  3. To allow **IPv6 traffic** to reach backend instance group `ig-a`, create the following rule:
         
         gcloud compute firewall-rules create fw-allow-lb-access-ipv6 \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=IPV6_ADDRESS \
             --rules=all
         

Replace `IPV6_ADDRESS` with the IPv6 address assigned in the `lb-subnet`.

  4. Create the `fw-allow-health-check` firewall rule to allow Google Cloud IPv4 health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check \
             --source-ranges=35.191.0.0/16 \
             --rules=tcp,udp,icmp
         

  5. Create the `fw-allow-health-check-ipv6` rule to allow Google Cloud IPv6 health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check-ipv6 \
            --network=lb-network \
            --action=allow \
            --direction=ingress \
            --target-tags=allow-health-check-ipv6 \
            --source-ranges=2600:2d00:1:b029::/64 \
            --rules=tcp,udp,icmp
         




###  API 

  1. To create the `fw-allow-lb-access` firewall rule, make a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         {
         "name": "fw-allow-lb-access",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "priority": 1000,
         "sourceRanges": [
           "10.1.2.0/24"
         ],
         "allPorts": true,
         "allowed": [
           {
             "IPProtocol": "tcp"
           },
           {
             "IPProtocol": "udp"
           },
           {
             "IPProtocol": "icmp"
           }
         ],
         "direction": "INGRESS",
         "logConfig": {
           "enable": false
         },
         "disabled": false
         }
         

  2. Create the `fw-allow-lb-access-ipv6` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         {
          "name": "fw-allow-lb-access-ipv6",
          "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
          "priority": 1000,
          "sourceRanges": [
            "IPV6_ADDRESS"
          ],
          "allPorts": true,
          "allowed": [
            {
               "IPProtocol": "tcp"
             },
             {
               "IPProtocol": "udp"
             },
             {
               "IPProtocol": "58"
             }
          ],
          "direction": "INGRESS",
          "logConfig": {
             "enable": false
          },
          "disabled": false
         }
         

Replace IPV6_ADDRESS with the IPv6 address assigned in the `lb-subnet`.

  3. To create the `fw-allow-ssh` firewall rule, make a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         {
         "name": "fw-allow-ssh",
              "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "priority": 1000,
         "sourceRanges": [
           "0.0.0.0/0"
         ],
         "targetTags": [
           "allow-ssh"
         ],
         "allowed": [
          {
            "IPProtocol": "tcp",
            "ports": [
              "22"
            ]
          }
         ],
         "direction": "INGRESS",
         "logConfig": {
          "enable": false
         },
         "disabled": false
         }
         

  4. To create the `fw-allow-health-check` firewall rule, make a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         {
         "name": "fw-allow-health-check",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "priority": 1000,
         "sourceRanges": [35.191.0.0/16],
         "targetTags": [
           "allow-health-check"
         ],
         "allowed": [
           {
             "IPProtocol": "tcp"
           },
           {
             "IPProtocol": "udp"
           },
           {
             "IPProtocol": "icmp"
           }
         ],
         "direction": "INGRESS",
         "logConfig": {
           "enable": false
         },
         "disabled": false
         }
         

  5. Create the `fw-allow-health-check-ipv6` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         {
         "name": "fw-allow-health-check-ipv6",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "priority": 1000,
         "sourceRanges": [2600:2d00:1:b029::/64],
         "targetTags": [
           "allow-health-check-ipv6"
         ],
         "allowed": [
           {
             "IPProtocol": "tcp"
           },
           {
             "IPProtocol": "udp"
           }
         ],
         "direction": "INGRESS",
         "logConfig": {
           "enable": false
         },
         "disabled": false
         }
         




### Create backend VMs and instance groups

For this load balancing scenario, you create a Compute Engine zonal managed instance group and install an Apache web server.

To handle both IPv4 and IPv6 traffic, configure the backend VMs to be dual-stack. Set the VM's `stack-type` to `IPV4_IPV6`. The VMs also inherit the `ipv6-access-type` setting (in this example, `INTERNAL`) from the subnet. For more details about IPv6 requirements, see the [Internal passthrough Network Load Balancer overview: Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal#forwarding_rule).

If you want to use existing VMs as backends, update the VMs to be dual-stack by using the [`gcloud compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

Instances that participate as backend VMs for internal passthrough Network Load Balancers must be running the appropriate [Linux Guest Environment](https://docs.cloud.google.com/compute/docs/instances/linux-guest-environment), [Windows Guest Environment](https://github.com/GoogleCloudPlatform/compute-image-windows), or other processes that provide equivalent functionality.

For instructional simplicity, the backend VMs run Debian GNU/Linux 12.

#### Create the instance group

###  Console 

To support both **IPv4 and IPv6 traffic** , use the following steps:

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

     1. Click **Create instance template**.
     2. For the **Name** , enter `vm-a1`.
     3. Ensure that the Boot disk is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     4. Expand the **Advanced options** section.
     5. Expand the **Management** section, and then copy the following script into the **Startup script** field. The startup script also configures the Apache server to listen on port `8080` instead of port `80`.
            
            #! /bin/bash
            apt-get update
            apt-get install apache2 -y
            a2ensite default-ssl
            a2enmod ssl
            vm_hostname="$(curl -H "Metadata-Flavor:Google" \
            http://metadata.google.internal/computeMetadata/v1/instance/name)"
            echo "Page served from: $vm_hostname" | \
            tee /var/www/html/index.html
            sed -ire 's/^Listen 80$/Listen 8080/g' /etc/apache2/ports.conf
            systemctl restart apache2
            

     6. Expand the **Networking** section, and then specify the following:

        1. For **Network tags** , add `allow-ssh` and `allow-health-check-ipv6`.
        2. For **Network interfaces** , click the **default** interface and configure the following fields: 
           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
     7. Click **Create**.




To support **IPv4 traffic** , use the following steps:

  1. Create an instance template. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.

     1. For the **Name** , enter `vm-a1`.
     2. Ensure that the Boot disk is set to a Debian image, such as **Debian GNU/Linux 12 (bookworm)**. These instructions use commands that are only available on Debian, such as `apt-get`.
     3. Expand the **Advanced options** section.
     4. Expand the **Management** section, and then copy the following script into the **Startup script** field. The startup script also configures the Apache server to listen on port `8080` instead of port `80`.
            
            #! /bin/bash
            apt-get update
            apt-get install apache2 -y
            a2ensite default-ssl
            a2enmod ssl
            vm_hostname="$(curl -H "Metadata-Flavor:Google" \
            http://metadata.google.internal/computeMetadata/v1/instance/name)"
            echo "Page served from: $vm_hostname" | \
            tee /var/www/html/index.html
            sed -ire 's/^Listen 80$/Listen 8080/g' /etc/apache2/ports.conf
            systemctl restart apache2
            

     5. Expand the **Networking** section, and then specify the following:

        1. For **Network tags** , add `allow-ssh` and `allow-health-check`.
        2. For **Network interfaces** , click the **default** interface and configure the following fields: 
           * **Network** : `lb-network`
           * **Subnetwork** : `lb-subnet`
           * **IP stack type** : **IPv4 (single-stack)**
     6. Click **Create**.

  3. Create a managed instance group. Go to the **Instance groups** page in the Google Cloud console.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     1. Click **Create instance group**.
     2. Choose **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
     3. For the **Name** , enter `ig-a`.
     4. For **Location** , select **Single zone**.
     5. For the **Region** , select `us-west1`.
     6. For the **Zone** , select `us-west1-a`.
     7. For **Instance template** , select `vm-a1`.
     8. Specify the number of instances that you want to create in the group.

For this example, specify the following options under **Autoscaling** :

        * For **Autoscaling mode** , select `Off:do not autoscale`.
        * For **Maximum number of instances** , enter `2`.
     9. Click **Create**.




###  gcloud 

The `gcloud` instructions in this guide assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.

  1. Create a VM instance template with HTTP server with the [`gcloud compute instance-templates create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) command.

The startup script also configures the Apache server to listen on port `8080` instead of port `80`.

To handle both **IPv4 and IPv6 traffic** , use the following command.
         
         gcloud compute instance-templates create vm-a1 \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet \
             **--ipv6-network-tier=PREMIUM \**
             **--stack-type=IPV4_IPV6 \**
             --tags=allow-ssh \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
               http://metadata.google.internal/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               sed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf
               systemctl restart apache2'
         

Or, if you want to handle **IPv4 traffic only** , use the following command.
         
         gcloud compute instance-templates create vm-a1 \
             --region=us-west1 \
             --network=lb-network \
             --subnet=lb-subnet \
             --tags=allow-ssh \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --metadata=startup-script='#! /bin/bash
               apt-get update
               apt-get install apache2 -y
               a2ensite default-ssl
               a2enmod ssl
               vm_hostname="$(curl -H "Metadata-Flavor:Google" \
               http://metadata.google.internal/computeMetadata/v1/instance/name)"
               echo "Page served from: $vm_hostname" | \
               tee /var/www/html/index.html
               sed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf
               systemctl restart apache2'
         

  2. Create a managed instance group in the zone with the [`gcloud compute instance-groups managed create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) command.
         
         gcloud compute instance-groups managed create ig-a \
             --zone us-west1-a \
             --size 2 \
             --template vm-a1
         




###  api 

To handle both **IPv4 and IPv6 traffic** , use the following steps:.

  1. Create a VM by making `POST` requests to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
         {
         "name": "vm-a1",
         "tags": {
          "items": [
            "allow-health-check-ipv6",
            "allow-ssh"
          ]
         },
         "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/e2-standard-2",
         "canIpForward": false,
         "networkInterfaces": [
          {
            "stackType": "IPV4_IPV6",
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
            "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
            "accessConfigs": [
              {
                "type": "ONE_TO_ONE_NAT",
                "name": "external-nat",
                "networkTier": "PREMIUM"
              }
            ]
          }
         ],
         "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "autoDelete": true,
            "deviceName": "vm-a1",
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/DEBIAN_IMAGE_NAME",
              "diskType": "projects/PROJECT_ID/zones/ZONE/diskTypes/pd-standard",
              "diskSizeGb": "10"
            }
          }
         ],
         "metadata": {
          "items": [
            {
              "key": "startup-script",
              "value": "#! /bin/bash\napt-get update\napt-get install apache2 -y\na2ensite default-ssl\na2enmod ssl\nvm_hostname="$(curl -H "Metadata-Flavor:Google" \\\nhttp://metadata.google.internal/computeMetadata/v1/instance/name)"\necho "Page served from: $vm_hostname" | \\\ntee /var/www/html/index.html\nsed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf\nsystemctl restart apache2"
            }
          ]
         },
         "scheduling": {
          "preemptible": false
         },
         "deletionProtection": false
         }
         




To handle **IPv4 traffic** , use the following steps.

  1. Create a VM by making `POST` requests to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
         {
         "name": "vm-a1",
         "tags": {
          "items": [
            "allow-health-check",
            "allow-ssh"
          ]
         },
         "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/e2-standard-2",
         "canIpForward": false,
         "networkInterfaces": [
          {
            "stackType": "IPV4",
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
            "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
            "accessConfigs": [
              {
                "type": "ONE_TO_ONE_NAT",
                "name": "external-nat",
                "networkTier": "PREMIUM"
              }
            ]
          }
         ],
         "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "autoDelete": true,
            "deviceName": "vm-a1",
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/DEBIAN_IMAGE_NAME",
              "diskType": "projects/PROJECT_ID/zones/ZONE/diskTypes/pd-standard",
              "diskSizeGb": "10"
            }
          }
         ],
         "metadata": {
          "items": [
            {
              "key": "startup-script",
              "value": "#! /bin/bash\napt-get update\napt-get install apache2 -y\na2ensite default-ssl\na2enmod ssl\nvm_hostname="$(curl -H "Metadata-Flavor:Google" \\\nhttp://metadata.google.internal/computeMetadata/v1/instance/name)"\necho "Page served from: $vm_hostname" | \\\ntee /var/www/html/index.html\nsed -ire "s/^Listen 80$/Listen 8080/g" /etc/apache2/ports.conf\nsystemctl restart apache2"
            }
          ]
         },
         "scheduling": {
          "preemptible": false
         },
         "deletionProtection": false
         }
         

  2. Create an instance group by making a `POST` request to the [`instanceGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups
         
         {
         "name": "ig-a",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet"
         }
         

  3. Add instances to each instance group by making a `POST` request to the [`instanceGroups.addInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/addInstances).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a/addInstances
         
         {
         "instances": [
         {
          "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/vm-a1"
         }
         ]
         }
         




### Create a client VM

This example creates a client VM in the same region as the backend (server) VMs. The client is used to validate the load balancer's configuration and demonstrate expected behavior as described in the testing section.

For **IPv4 and IPv6 traffic** :

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set the **Name** to `vm-client-ipv6`.

  4. Set the **Zone** to `us-west1-a`.

  5. Expand the **Advanced options** section, and then make the following changes:

     * Expand **Networking** , and then add the `allow-ssh` to **Network tags**.
     * Under **Network interfaces** , click **Edit** , make the following changes, and then click **Done** : 
       * **Network** : `lb-network`
       * **Subnet** : `lb-subnet`
       * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
       * **Primary internal IP** : Ephemeral (automatic)
       * **External IP** : Ephemeral
  6. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client-ipv6 \
        --zone=us-west1-a \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --stack-type=IPV4_IPV6 \
        --tags=allow-ssh \
        --subnet=lb-subnet
    

###  api 

Make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances
    
    {
     "name": "vm-client-ipv6",
     "tags": {
       "items": [
         "allow-ssh"
       ]
     },
     "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/machineTypes/e2-standard-2",
     "canIpForward": false,
     "networkInterfaces": [
       {
         "stackType": "IPV4_IPV6",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
         "accessConfigs": [
           {
             "type": "ONE_TO_ONE_NAT",
             "name": "external-nat",
             "networkTier": "PREMIUM"
           }
         ]
       }
     ],
     "disks": [
       {
         "type": "PERSISTENT",
         "boot": true,
         "mode": "READ_WRITE",
         "autoDelete": true,
         "deviceName": "vm-client",
         "initializeParams": {
           "sourceImage": "projects/debian-cloud/global/images/debian-image-name",
           "diskType": "projects/PROJECT_ID/zones/us-west1-a/diskTypes/pd-standard",
           "diskSizeGb": "10"
         }
       }
     ],
     "scheduling": {
       "preemptible": false
     },
     "deletionProtection": false
    }
    

For **IPv4 traffic** :

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `vm-client`.

  4. For **Zone** , enter `us-west1-a`.

  5. Expand the **Advanced options** section.

  6. Expand **Networking** , and then configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `lb-subnet`
  7. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client \
        --zone=us-west1-a \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=lb-subnet
    

###  API 

Make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances
     {
        "name": "vm-client",
        "tags": {
          "items": [
            "allow-ssh"
          ]
      },
        "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/machineTypes/e2-standard-2",
        "canIpForward": false,
        "networkInterfaces": [
          {
            "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
            "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
            "accessConfigs": [
              {
                "type": "ONE_TO_ONE_NAT",
                "name": "external-nat",
                "networkTier": "PREMIUM"
              }
            ]
          }
        ],
        "disks": [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "autoDelete": true,
            "deviceName": "vm-client",
            "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/debian-image-name",
              "diskType": "projects/PROJECT_ID/zones/us-west1-a/diskTypes/pd-standard",
              "diskSizeGb": "10"
            }
          }
        ],
        "scheduling": {
          "preemptible": false
         },
        "deletionProtection": false
      }
      

### Configure load balancer components

Create a load balancer for multiple protocols.

###  gcloud 

  1. Create an HTTP health check for port 80. This health check is used to verify the health of backends in the `ig-a` instance group.
         
         gcloud compute health-checks create http hc-http-80 \
             --region=us-west1 \
             --port=80
         

  2. Create the backend service with the protocol set to `UNSPECIFIED`:
         
         gcloud compute backend-services create be-ilb-l3-default \
             --load-balancing-scheme=internal \
             --protocol=UNSPECIFIED \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  3. Add the instance group to the backend service:
         
         gcloud compute backend-services add-backend be-ilb-l3-default \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         

  4. **For IPv6 traffic** : Create a forwarding rule with the protocol set to `L3_DEFAULT` to handle all supported IPv6 protocol traffic. All ports must be configured with `L3_DEFAULT` forwarding rules.
         
         gcloud compute forwarding-rules create fr-ilb-ipv6 \
            --region=us-west1 \
            --load-balancing-scheme=internal \
            --subnet=lb-subnet \
            --ip-protocol=L3_DEFAULT \
            --ports=ALL \
            --backend-service=be-ilb-l3-default \
            --backend-service-region=us-west1 \
            --ip-version=IPV6
         

  5. **For IPv4 traffic** : Create a forwarding rule with the protocol set to `L3_DEFAULT` to handle all supported IPv4 protocol traffic. All ports must be configured with `L3_DEFAULT` forwarding rules. Use `10.1.2.99` as the internal IP address.
         
         gcloud compute forwarding-rules create fr-ilb-l3-default \
            --region=us-west1 \
            --load-balancing-scheme=internal \
            --network=lb-network \
            --subnet=lb-subnet \
            --address=10.1.2.99 \
            --ip-protocol=L3_DEFAULT \
            --ports=ALL \
            --backend-service=be-ilb-l3-default \
            --backend-service-region=us-west1
         




###  API 

  1. Create the health check by making a `POST` request to the [`regionHealthChecks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/regionHealthChecks
         
         {
         "name": "hc-http-80",
         "type": "HTTP",
         "httpHealthCheck": {
          "port": 80
         }
         }
         

  2. Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices
         
         {
         "name": "be-ilb-l3-default",
         "backends": [
          {
            "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a",
            "balancingMode": "CONNECTION"
          }
         ],
         "healthChecks": [
          "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/healthChecks/hc-http-80"
         ],
         "loadBalancingScheme": "INTERNAL",
         "protocol": "UNSPECIFIED",
         "connectionDraining": {
          "drainingTimeoutSec": 0
         }
         }
         

  3. **For IPv6 traffic** : Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
         
         {
         "name": "fr-ilb-ipv6",
         "IPProtocol": "L3_DEFAULT",
         "allPorts": true,
         "loadBalancingScheme": "INTERNAL",
         "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
         "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb-l3-default",
         "ipVersion": "IPV6",
         "networkTier": "PREMIUM"
         }
         

  4. **For IPv4 traffic** : Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
         
         {
         "name": "fr-ilb-l3-default",
         "IPAddress": "10.1.2.99",
         "IPProtocol": "L3_DEFAULT",
         "allPorts": true,
         "loadBalancingScheme": "INTERNAL",
         "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb-l3-default",
         "networkTier": "PREMIUM"
         }
         




### Test your load balancer

The following tests show how to validate your load balancer configuration and learn about its expected behavior.

#### Test connection from client VM

This test contacts the load balancer from a separate client VM; that is, not from a backend VM of the load balancer.

### gcloud:IPv6

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client-ipv6 --zone=us-west1-a
         

  2. Describe the IPv6 forwarding rule `fr-ilb-ipv6`. Note the `IPV6_ADDRESS` in the description.
         
         gcloud compute forwarding-rules describe fr-ilb-ipv6 --region=us-west1
         

  3. From clients with IPv6 connectivity, run the following command. Replace `IPV6_ADDRESS` with the ephemeral IPv6 address in the `fr-ilb-ipv6` forwarding rule.
         
         curl -m 10 -s http://IPV6_ADDRESS:80
         

For example, if the assigned IPv6 address is `[fd20:1db0:b882:802:0:46:0:0/96]:80`, the command should look like:
         
         curl -m 10 -s http://[fd20:1db0:b882:802:0:46:0:0]:80
         




### gcloud:IPv4

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Describe the IPv4 forwarding rule `fr-ilb`.
         
         gcloud compute forwarding-rules describe fr-ilb --region=us-west1
         

  3. Make a web request to the load balancer by using `curl` to contact its IP address. Repeat the request so that you can see that responses come from different backend VMs. The name of the VM that generates the response is displayed in the text in the HTML response by virtue of the contents of `/var/www/html/index.html` on each backend VM. Expected responses look like `Page served from: vm-a1`.
         
         curl http://10.1.2.99
         

The forwarding rule is configured to serve ports `80` and `53`. To send traffic to those ports, append a colon (`:`) and the port number after the IP address, like this:
         
         curl http://10.1.2.99:80
         




#### Ping the load balancer's IP address

This test demonstrates an expected behavior: you can ping the IP address of the load balancer.

### gcloud:IPv6

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client-ipv6 --zone=us-west1-a
         

  2. Attempt to ping the IPv6 address of the load balancer. Replace `IPV6_ADDRESS` with the ephemeral IPv6 address in the `fr-ilb-ipv6` forwarding rule.

Notice that you get a response and that the `ping` command works in this example.
         
         ping6 IPV6_ADDRESS
         

For example, if the assigned IPv6 address is `[2001:db8:1:1:1:1:1:1/96]`, the command is as follows:
         
         ping6 2001:db8:1:1:1:1:1:1
         

The output is similar to the following:
         
         @vm-client: ping IPV6_ADDRESS
         PING IPV6_ADDRESS (IPV6_ADDRESS) 56(84) bytes of data.
         64 bytes from IPV6_ADDRESS: icmp_seq=1 ttl=64 time=1.58 ms
         




### gcloud:IPv4

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Attempt to ping the IPv4 address of the load balancer. Notice that you get a response and that the `ping` command works in this example.
         
         ping 10.1.2.99
         

The output is the following:
         
         @vm-client: ping 10.1.2.99
         PING 10.1.2.99 (10.1.2.99) 56(84) bytes of data.
         64 bytes from 10.1.2.99: icmp_seq=1 ttl=64 time=1.58 ms
         64 bytes from 10.1.2.99: icmp_seq=2 ttl=64 time=0.242 ms
         64 bytes from 10.1.2.99: icmp_seq=3 ttl=64 time=0.295 ms
         




## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

You can reserve a static internal IP address for your example. This configuration allows multiple internal forwarding rules to use the same IP address with different protocols and different ports. The backends of your example load balancer must still be located in the region `us-west1`.

The following diagram shows the architecture for this example.

[ ![Load balancing traffic based on the protocols, with backend services to
    manage connection distribution to a single zonal instance group.](https://docs.cloud.google.com/static/load-balancing/images/ilb-all-protocols.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-all-protocols.svg) An internal passthrough Network Load Balancer for multiple protocols that uses a static internal IP address (click to enlarge).

You can also consider using the following forwarding rule configurations:

  * Forwarding rules with multiple ports:

    * Protocol `TCP` with ports `80,8080`
    * Protocol `L3_DEFAULT` with ports `ALL`
  * Forwarding rules with all ports:

    * Protocol `TCP` with ports `ALL`
    * Protocol `L3_DEFAULT` with ports `ALL`



### Reserve static internal IPv4 address

Reserve a static internal IP address for `10.1.2.99` and set its `--purpose` flag to `SHARED_LOADBALANCER_VIP`. The `--purpose` flag is required so that many forwarding rules can use the same internal IP address.

###  gcloud 

Use the `gcloud compute addresses create` command:
    
    
    gcloud compute addresses create internal-lb-ipv4 \
        --region us-west1 \
        --subnet lb-subnet \
        --purpose SHARED_LOADBALANCER_VIP \
        --addresses 10.1.2.99
    

###  API 

Call the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/addresses
    

The body of the request must include the `addressType`, which should be `INTERNAL`, the `name` of the address, and the `subnetwork` that the IP address belongs to. You must specify the `address` as `10.1.2.99`.
    
    
    {
      "addressType": "INTERNAL",
      "name": "internal-lb-ipv4",
      "subnetwork": "regions/us-west1/subnetworks/lb-subnet",
      "purpose": "SHARED_LOADBALANCER_VIP",
      "address": "10.1.2.99"
    }
    

### Configure load balancer components

Configure three load balancers with the following components:

  * The first load balancer has a forwarding rule with protocol `TCP` and port `80`. TCP traffic arriving at the internal IP address on port `80` is handled by the `TCP` forwarding rule.
  * The second load balancer has a forwarding rule with protocol `UDP` and port `53`. UDP traffic arriving at the internal IP address on port `53` is handled by the `UDP` forwarding rule.
  * The third load balancer has a forwarding rule with protocol `L3_DEFAULT` and port `ALL`. All other traffic that does not match the `TCP` or `UDP` forwarding rules is handled by the `L3_DEFAULT` forwarding rule.
  * All three load balancers share the same static internal IP address (`internal-lb-ipv4`) in their forwarding rules.



#### Create the first load balancer

Create the first load balancer for TCP traffic on port `80`.

###  gcloud 

  1. Create the backend service for TCP traffic:
         
         gcloud compute backend-services create be-ilb \
             --load-balancing-scheme=internal \
             --protocol=tcp \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  2. Add the instance group to the backend service:
         
         gcloud compute backend-services add-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         

  3. Create a forwarding rule for the backend service. Use the static reserved internal IP address (`internal-lb-ipv4`) for the internal IP address.
         
         gcloud compute forwarding-rules create fr-ilb \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --network=lb-network \
             --subnet=lb-subnet \
             --address=internal-lb-ipv4 \
             --ip-protocol=TCP \
             --ports=80 \
             --backend-service=be-ilb \
             --backend-service-region=us-west1
         




###  API 

  1. Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices
         {
         "name": "be-ilb",
         "backends": [
          {
            "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a",
            "balancingMode": "CONNECTION"
          }
         ],
         "healthChecks": [
          "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/healthChecks/hc-http-80"
         ],
         "loadBalancingScheme": "INTERNAL",
         "protocol": "TCP",
         "connectionDraining": {
          "drainingTimeoutSec": 0
         }
         }
         

  2. Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
         
         {
         "name": "fr-ilb",
         "IPAddress": "internal-lb-ipv4",
         "IPProtocol": "TCP",
         "ports": [
          "80"
         ],
         "loadBalancingScheme": "INTERNAL",
         "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
         "networkTier": "PREMIUM"
         }
         




#### Create the second load balancer

Create the second load balancer for UDP traffic on port `53`.

###  gcloud 

  1. Create the backend service with the protocol set to `UDP`:
         
         gcloud compute backend-services create be-ilb-udp \
             --load-balancing-scheme=internal \
             --protocol=UDP \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  2. Add the instance group to the backend service:
         
         gcloud compute backend-services add-backend be-ilb-udp \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         

  3. Create a forwarding rule for the backend service. Use the static reserved internal IP address (`internal-lb-ipv4`) for the internal IP address.
         
         gcloud compute forwarding-rules create fr-ilb-udp \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --network=lb-network \
             --subnet=lb-subnet \
             --address=internal-lb-ipv4 \
             --ip-protocol=UDP \
             --ports=53 \
             --backend-service=be-ilb-udp \
             --backend-service-region=us-west1
         




###  API 

  1. Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices
         {
         "name": "be-ilb-udp",
         "backends": [
          {
           "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a",
           "balancingMode": "CONNECTION"
          }
         ],
         "healthChecks": [
          "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/healthChecks/hc-http-80"
         ],
         "loadBalancingScheme": "INTERNAL",
         "protocol": "UDP",
         "connectionDraining": {
          "drainingTimeoutSec": 0
         }
         }
         

  2. Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
         
         {
         "name": "fr-ilb-udp",
         "IPAddress": "internal-lb-ipv4",
         "IPProtocol": "UDP",
         "ports": [
          "53"
         ],
         "loadBalancingScheme": "INTERNAL",
         "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
         "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb-udp",
         "networkTier": "PREMIUM"
         }
         




#### Create the third load balancer

Create the forwarding rule of the third load balancer to use the static reserved internal IP address.

###  gcloud 

Create the forwarding rule with the protocol set to `L3_DEFAULT` to handle all other supported IPv4 protocol traffic. Use the static reserved internal IP address (`internal-lb-ipv4`) as the internal IP address.
    
    
    gcloud compute forwarding-rules create fr-ilb-l3-default \
        --region=us-west1 \
        --load-balancing-scheme=internal \
        --network=lb-network \
        --subnet=lb-subnet \
        --address=internal-lb-ipv4 \
        --ip-protocol=L3_DEFAULT \
        --ports=ALL \
        --backend-service=be-ilb-l3-default \
        --backend-service-region=us-west1
    

###  API 

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert). Replace `PROJECT_ID` with the ID of your Google Cloud project.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb-l3-default",
    "IPAddress": "internal-lb-ipv4",
    "IPProtocol": "L3_DEFAULT",
    "ports": [
      "ALL"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb-l3-default",
    "networkTier": "PREMIUM"
    }
    

### Test your load balancer

To test your load balancer, follow the steps in the previous section.

## What's next

  * To learn about important concepts, see [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal).
  * To learn to configure failover, see [Configure failover for internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-failover).
  * To learn about configuring Logging and Monitoring for internal passthrough Network Load Balancers, see [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring).
  * To learn about troubleshooting, see [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb).
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
