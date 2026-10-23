---
url: https://docs.cloud.google.com/vpc/docs/using-packet-mirroring/
title: Use Packet Mirroring \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:53.325817+00:00
---

# Use Packet Mirroring  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/using-packet-mirroring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Packet Mirroring

You can use Packet Mirroring to mirror traffic to and from particular virtual machine (VM) instances. The collected traffic can help you detect security threats and monitor application performance. For details about Packet Mirroring, see [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring).

Mirrored traffic is sent to VMs where you have installed appropriate software. For a list of vendors who supply software, see [Packet Mirroring partner providers](https://docs.cloud.google.com/vpc/docs/packet-mirroring-partners).

The following sections describe how to create and manage packet mirroring policies.

## Limitations

  * Packet Mirroring can't mirror packets for [Private Service Connect published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) traffic.

  * For security reasons, Packet Mirroring doesn't mirror packets that are sent to the link-local IP address range `169.254.0.0/16`. This range includes [metadata requests](https://docs.cloud.google.com/compute/docs/metadata/overview) from a VM to its metadata server.

  * Using a Google Kubernetes Engine (GKE) LoadBalancer Service as a packet mirroring collector is not supported.

  * If a packet mirroring policy might apply to collector instances, Packet Mirroring ignores them and doesn't mirror their traffic.

  * When packets are mirrored, Google Cloud processes both the original and the mirrored packets, which slows the packet processing rate. The packet processing rate for the combined traffic is similar to the [egress rates outside of a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-e), and depends on factors including the following:

    * The machine type and CPU utilization of the mirrored VM.
    * The packet size of the mirrored traffic.
  * When network packets match any mirroring policy, Packet Mirroring processes both the original and mirrored packets at a slower rate. The combined rate of packet processing depends on the machine type, packet size, and CPU utilization, and is approximately similar to the [egress rates outside of a VPC network](https://docs.cloud.google.com/compute/docs/network-bandwidth#vm-out-dest-e).




## Before you begin

Before you create a packet mirroring policy, you must have the appropriate permissions. You must also create an internal passthrough Network Load Balancer to act as a collector destination. This internal passthrough Network Load Balancer requires an instance group so that its backend service can use the VMs as collector destinations.

### Permissions

To create and manage packet mirroring policies, Google Cloud provides two roles that are related to Packet Mirroring:

  * [`compute.packetMirroringUser`](https://docs.cloud.google.com/compute/docs/access/iam#compute.packetMirroringUser) grants users permission to create, update, and delete packet mirroring policies. To use Packet Mirroring, users must have this role in projects where they create packet mirroring policies.

  * [`compute.packetMirroringAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.packetMirroringAdmin) grants users permission to mirror particular resources. Even if users have permission to create a packet mirroring policy, they still require permission to mirror related sources. Use this role in projects where the owner of a policy might not have any other permissions, for example, in Shared VPC scenarios.




For more information about using IAM roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the IAM documentation.

### Create collector instances

Packet Mirroring requires an instance group of collector instances. For details about instance groups, see the following documentation: [Create a new instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template) and [Create a MIG in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).

### Create an internal load balancer for Packet Mirroring

To enable Packet Mirroring, you must have an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) that can serve as a packet mirroring collector. The internal passthrough Network Load Balancer must meet the following requirements:

  * The internal passthrough Network Load Balancer's forwarding rule must have Packet Mirroring enabled when the rule is created. This status cannot be changed after the rule is created. You can use this forwarding rule to collect both IPv4 and IPv6 traffic.
  * The internal passthrough Network Load Balancer is in the same region as the instances that you're mirroring.
  * The internal passthrough Network Load Balancer's backend service must use a [session affinity](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity) of `NONE` (5-tuple hash).
  * The internal passthrough Network Load Balancer's backend service must have [backend subsetting](https://docs.cloud.google.com/load-balancing/docs/internal#backend_subsetting) disabled.



If your collector instances are not set up to respond to the health check that you've configured with your backend service, the health check can fail. Packets can still be mirrored in this case.

For more information about how to create an internal passthrough Network Load Balancer for Packet Mirroring, see [Creating a load balancer for Packet Mirroring](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#lb-packet-mirroring).

### Configure firewall rules

To prepare your VPC network for Packet Mirroring traffic, do the following:

  * Ensure that collector instances in the load balancer's instance group can receive traffic from mirrored instances or from the IPv4 and IPv6 address ranges of mirrored instances. For example, to let collector instances receive IPv4 traffic from any VM, create a firewall rule with a source IPv4 address range of `0.0.0.0/0`. To let collector instances receive IPv6 traffic from any VM, create a firewall rule with a source IPv6 address range of `::/0`. To prevent internet traffic from reaching the collector instances, assign only internal IPv4 and IPv6 addresses to them.

  * Ensure that collector instances can receive traffic from the Google Cloud health checking systems. For example, for IPv4 traffic, create a firewall rule that allows traffic to the collector instances from the IPv4 address ranges of `130.211.0.0/22` and `35.191.0.0/16`. For IPv6 traffic, create a firewall rule that allows traffic to the collector instances from the IPv6 address range of `2600:2d00:1:b029::/64`.

  * If you want to test Packet Mirroring by manually sending egress traffic from one or more mirrored instances, create a firewall rule that allows SSH traffic to those instances. For example, to allow SSH connections to your mirrored instances from all IPv4 and IPv6 addresses, allow ingress `TCP` traffic to port `22` from any source IPv4 and IPv6 address. If you want to only allow SSH connections that are initiated from a certain IPv4 or IPv6 address range, specify that IPv4 or IPv6 address range as a source range for the firewall rule. For more information about testing your internal passthrough Network Load Balancer, see [Test load balancing](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#test_load_balancing).




If you don't have existing rules that allow this traffic, see [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to create them. For more information about creating firewall rules for an internal passthrough Network Load Balancer, see [Configuring firewall rules](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure_firewall_rules) in the Cloud Load Balancing documentation.

## Create a packet mirroring policy

To start mirroring traffic to and from particular instances, create a packet mirroring policy. Google Cloud mirrors any instance that matches at least one of your specified sources.

###  Console 

  1. In the Google Cloud console, go to the **Packet Mirroring** page.

[Go to Packet Mirroring](https://console.cloud.google.com/networking/packetmirroring)

  2. Click **Create policy**.

  3. Enter the following information about the policy, and then click **Continue**.

     1. Enter a name for the policy.
     2. Select the region that includes the mirrored sources and collector destination. The packet mirroring policy must be in the same region as the source and destination.
     3. Ignore the **Priority** field. It cannot be adjusted at present.
     4. Select **Enabled** to activate the policy when you create it.
  4. Select the VPC networks where the mirrored source and collector destination are located, and then click **Continue**.

The source and destination can be in the same or different VPC networks.

     * If they are in the same VPC network, select **Mirrored sources and destination are in the same VPC network** , and then select the network.
     * If they are in different networks, select **Mirrored source and collector destination are in separate, peered VPC networks** , and then select the mirrored source network and then the collector destination network.
  5. Select mirrored sources, and then click **Continue**. You can select one or more sources. Google Cloud mirrors any instance that matches at least one of your selected sources.

     * **Subnets** : select one or more subnetworks. Google Cloud mirrors existing and future instances in selected subnets.
     * **Network tag** : specify one or more network tags. Google Cloud mirrors instances that have at least one of the specified tags.
     * **Instance name** : select specific instances to mirror.
  6. Select an internal passthrough Network Load Balancer that has been configured for Packet Mirroring, and then click **Continue**. Google Cloud sends mirrored traffic to instances that are behind the internal passthrough Network Load Balancer.

For Shared VPC, if the collector destination and mirrored sources are in the same Shared VPC network, you must select the project where the collector destination is located, and then you select a load balancer.

  7. To select the traffic to mirror, do the following:

     * To mirror all IPv4 traffic, select **Mirror all IPv4 traffic (default)**.
     * To mirror all IPv4 and IPv6 traffic, select **Mirror filtered traffic** , and then do the following: 
       * Select **Allow all protocols**.
       * Select **Allow all IPv4 ranges (0.0.0.0/0)**.
       * Select **Allow all IPv6 ranges (::/0)**.
       * Select **Allow both ingress and egress traffic**.
     * To limit the traffic that's mirrored, select **Mirror filtered traffic** , and then do the following:

       * To limit mirrored traffic by protocol, select **Allow specific protocols** , and then select the protocols. If you don't see a protocol that you want to mirror traffic for, select **Other protocols** , and then enter the protocol in the **Other protocols** field. Valid values are `tcp`, `udp`, `esp`, `ah`, `ipip`, `sctp`, or an [IANA protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). To specify ICMP for IPv6, enter `58`.

       * For **IPv4 range filters** , do the following:

         * To mirror all IPv4 traffic, select **Allow all IPv4 ranges (0.0.0.0/0)**.
         * To mirror traffic for specific IPv4 address ranges, select **Allow specific IPv4 ranges**. In the **IPv4 ranges** field, type a single IPv4 address range, and then press **Enter**. You can add multiple IPv4 ranges by pressing **Enter** after each range that you type.
       * For **IPv6 range filters** , do the following:

         * To filter out all IPv6 traffic, select **None**.
         * To mirror all IPv6 traffic, select **Allow all IPv6 ranges (::/0)**.
         * To mirror traffic for specific IPv6 address ranges, select **Allow specific IPv6 ranges**. In the **IPv6 ranges** field, type a single IPv6 address range, and then press **Enter**. You can add multiple IPv6 ranges by pressing **Enter** after each range that you type.
  8. Select the **Traffic direction** of the traffic that you want to mirror.

  9. To create the packet mirroring policy, click **Submit**.




###  gcloud 

To create a packet mirroring policy, use the [`packet-mirrorings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/create).
    
    
    gcloud compute packet-mirrorings create POLICY_NAME \
        --region=REGION \
        --network=NETWORK_NAME \
        --collector-ilb=FORWARDING_RULE_NAME \
        [--mirrored-subnets=SUBNET,[SUBNET,...]] \
        [--mirrored-tags=TAG,[TAG,...]] \
        [--mirrored-instances=INSTANCE,[INSTANCE,...]] \
        [--filter-cidr-ranges=CIDR_RANGE,[CIDR_RANGE,...]] \
        [--filter-protocols=PROTOCOL,[PROTOCOL,...]] \
        [--filter-direction=DIRECTION]
    

Replace the following:

  * `POLICY_NAME`: the name of the packet mirroring policy.
  * `REGION`: the region where the mirrored sources and collector destination are located.
  * `NETWORK_NAME`: the network where the mirrored sources are located.
  * `FORWARDING_RULE_NAME`: the name of the forwarding rule that is configured as a mirroring collector. Google Cloud sends all mirrored traffic to the associated internal passthrough Network Load Balancer.
  * `SUBNET`: the name of one or more subnets to mirror. You can provide multiple subnets by using a comma-separated list. Google Cloud mirrors existing and future instances in the subnet.
  * `TAG`: one or more network tags. Google Cloud mirrors instances that have the network tag. You can provide multiple tags by using a comma-separated list.
  * `INSTANCE`: the fully qualified ID of one or more instances to mirror. You can provide multiple instances by using a comma-separated list.
  * `CIDR_RANGE`: one or more IPv4 or IPv6 CIDR ranges to mirror. If no CIDR ranges are specified, all IPv4 traffic that matches the specified protocols is mirrored. If neither CIDR ranges nor protocols are specified, all IPv4 traffic is mirrored. To mirror all IPv4 and IPv6 traffic, use `0.0.0.0/0,::/0`. You can include both IPv4 and IPv6 CIDR ranges. You can provide multiple ranges by using a comma-separated list.
  * `PROTOCOL`: one or more protocols to mirror. Valid values are `tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`, or an [IANA protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). If no protocols are specified, all traffic that matches the specified CIDR ranges is mirrored. If neither protocols nor CIDR ranges are specified, all IPv4 traffic is mirrored. To specify ICMP for IPv6, use `58`. You can provide multiple protocols by using a comma-separated list.
  * `DIRECTION`: the direction of the traffic to mirror relative to the VM. By default, this is set to `both`, which means that both ingress and egress traffic is mirrored. You can restrict which packets are captured by specifying `ingress` to capture only ingress packets or `egress` to capture only egress packets.



### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_packet_mirroring) to create a packet mirroring policy.
    
    
    resource "google_compute_packet_mirroring" "default" {
      region      = "europe-west1"
      name        = "my-mirroring"
      description = "My packet mirror"
      network {
        url = google_compute_network.ilb_network.id
      }
      collector_ilb {
        url = google_compute_forwarding_rule.default.id
      }
      mirrored_resources {
        tags = ["foo"]
        instances {
          url = google_compute_instance.vm_test.id
        }
      }
      filter {
        ip_protocols = ["tcp"]
        cidr_ranges  = ["0.0.0.0/0"]
        direction    = "BOTH"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

To create a packet mirroring policy, make a `POST` request to the [`packetMirrorings.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/packetMirrorings
    {
      "name": "POLICY_NAME",
      "enable": "ENABLED",
      "network": {
        "url": "NETWORK_URL"
      },
      "priority": PRIORITY,
      "mirroredResources": {
        "subnetworks": [
          {
            "url": "SUBNET_URL"
          }
        ],
        "tags": [
          "TAG"
        ],
        "instances": [
          {
            "url": "INSTANCE"
          }
        ]
      },
      "collectorIlb": {
        "url": "FORWARDING_RULE_URL"
      },
      "filter": {
        "IPProtocols": [
          "PROTOCOL"
        ],
        "cidrRanges": [
          "CIDR_RANGE"
        ],
        "direction": "DIRECTION"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project to create the policy in.
  * `REGION`: the region where the mirrored sources and collector destination are located.
  * `POLICY_NAME`: the name of the packet mirroring policy.
  * `ENABLED`: whether or not this policy takes effect. Options are `TRUE` and `FALSE`. `TRUE` is the default.
  * `NETWORK_URL`: the URL of the network where the mirrored sources are located.
  * `PRIORITY`: the priority of the forwarding rule, which is used to break ties when there is more than one matching rule. The valid range is 0 to 65,535, and the default is 1,000.
  * `SUBNET_URL`: the URL of a subnet to mirror. Google Cloud mirrors existing and future instances in the subnet. You can provide multiple subnets by using a comma-separated list.
  * `TAG`: a network tag. Google Cloud mirrors instances that have the network tag. You can provide multiple tags by using a comma-separated list.
  * `INSTANCE`: the fully qualified ID of an instance to mirror. You can provide multiple instances by using a comma-separated list.
  * `FORWARDING_RULE_URL`: the URL of a forwarding rule that is configured as a mirroring collector. Google Cloud sends all mirrored traffic to the associated internal passthrough Network Load Balancer.
  * `PROTOCOL`: one or more protocols. Options are `tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`, or an [IANA protocol number](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). If no protocols are specified, all traffic that matches the specified CIDR ranges is mirrored. If neither CIDR ranges nor protocols are specified, all IPv4 traffic is mirrored. To specify ICMP for IPv6, enter `58`. You can provide multiple protocols by using the following form: `"icmp", "udp"`.
  * `CIDR_RANGE`: one or more IPv4 or IPv6 CIDR ranges to mirror. If no CIDR ranges are specified, all IPv4 traffic that matches the specified protocols is mirrored. If neither CIDR ranges nor protocols are specified, all IPv4 traffic is mirrored. To mirror all IPv4 and IPv6 traffic, use `"0.0.0.0/0", "::/0"`. You can include both IPv4 and IPv6 CIDR ranges. You can provide multiple CIDR ranges by using the following form: `"192.0.2.0/24", "2001:0DB8::/32"`.
  * `PROTOCOL`: one or more protocols to mirror.
  * `DIRECTION`: the direction of traffic to mirror. Options are `INGRESS`, `EGRESS`, or `BOTH`. The default is `BOTH`.



## Verify packet mirroring

To verify that your collector instances are correctly receiving mirrored traffic, you can use [`tcpdump`](https://www.tcpdump.org/).

  1. [Connect to a collector instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).

  2. If the `tcpdump` command is not available, install it.

  3. Identify your network interface:
         
         ip address
         

In the list of network interfaces, find the name that is associated with your collector instance's primary internal IPv4 address—for example, `ens4`.

  4. Start analyzing packets:
         
         sudo tcpdump -i INTERFACE_NAME -f "host IP_ADDRESS"
         

Replace the following:

     * `INTERFACE_NAME`: the interface name that you identified in step 3.
     * `IP_ADDRESS`: the IPv4 address of a mirrored source VM.
  5. To run the test, send traffic from the mirrored source VM—for example, by sending an `ICMP` ping. In the output of `tcpdump`, verify that you can see the expected traffic.




## Modify a packet mirroring policy

You can update an existing policy to change details such as mirrored sources or collector destinations.

###  Console 

  1. In the Google Cloud console, go to the **Packet Mirroring** page.

[Go to Packet Mirroring](https://console.cloud.google.com/networking/packetmirroring)

  2. From the list of packet mirroring policies, click the one that you want to edit.

  3. On the policy details page, click **Edit**.

  4. Edit the fields that you want to update. The console follows the same flow as the steps for when you create a policy. For information about each field, see Create a packet mirroring policy.




###  gcloud 

To update an existing packet mirroring policy, use the [`packet-mirrorings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update).
    
    
    gcloud compute packet-mirrorings update POLICY_NAME [--async] \
      [--collector-ilb=FORWARDING_RULE_NAME] [--description=DESCRIPTION] [--enable] \
      [--filter-direction=DIRECTION] [--region=REGION] \
      [--add-filter-cidr-ranges=[CIDR_RANGE,...] | --clear-filter-cidr-ranges \
        | --remove-filter-cidr-ranges=[CIDR_RANGE,...] \
        | --set-filter-cidr-ranges=[CIDR_RANGE,...]] \
      [--add-filter-protocols=[PROTOCOL,...] | --clear-filter-protocols \
        | --remove-filter-protocols=[PROTOCOL,...] \
        | --set-filter-protocols=[PROTOCOL,...]] \
      [--add-mirrored-instances=[INSTANCE,...] | --clear-mirrored-instances \
        | --remove-mirrored-instances=[INSTANCE,...] \
        | --set-mirrored-instances=[INSTANCE,...]] \
      [--add-mirrored-subnets=[SUBNET,...] | --clear-mirrored-subnets \
        | --remove-mirrored-subnets=[SUBNET,...] \
        | --set-mirrored-subnets=[SUBNET,...]] \
      [--add-mirrored-tags=[TAG,...] | --clear-mirrored-tags \
        | --remove-mirrored-tags=[TAG,...] | --set-mirrored-tags=[TAG,...]]
    

Replace the following:

  * `POLICY_NAME`: the name of the packet mirroring policy to modify.
  * `FORWARDING_RULE_NAME`: the name of the forwarding rule that is configured as a collector. Google Cloud sends all mirrored traffic to the associated internal passthrough Network Load Balancer.
  * `DESCRIPTION`: a description of the packet mirroring policy.
  * `DIRECTION`: the direction of traffic to apply the packet mirroring policy to. Options are `egress`, `ingress`, or `both`.
  * `REGION`: the region where the policy is located.
  * `CIDR_RANGE`: one or more IPv4 or IPv6 CIDR ranges to mirror. If no CIDR ranges are specified, all IPv4 traffic that matches the specified protocols is mirrored. If neither CIDR ranges nor protocols are specified, all IPv4 traffic is mirrored. To mirror all IPv4 and IPv6 traffic, use `0.0.0.0/0,::/0`. You can include both IPv4 and IPv6 CIDR ranges. You can provide multiple ranges by using a comma-separated list.
  * `PROTOCOL`: one or more protocols to mirror. Valid values are `tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`, or an [IANA protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). If no protocols are specified, traffic that matches the specified CIDR ranges is mirrored. If neither protocols nor CIDR ranges are specified, all IPv4 traffic is mirrored. To specify ICMP for IPv6, use `58`. You can provide multiple protocols by using a comma-separated list.
  * `INSTANCE`: the fully qualified ID of one or more VM instances to mirror. You can provide multiple instances by using a comma-separated list.
  * `SUBNET`: one or more subnetworks. You can provide multiple subnetworks by using a comma-separated list. Google Cloud mirrors existing and future instances in the subnet.
  * `TAG`: one or more network tags. You can provide multiple tags by using a comma-separated list.



###  API 

To update a packet mirroring policy, make a `POST` request to the [`packetMirrorings.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/packetMirrorings/POLICY_NAME
    {
      "name": "POLICY_NAME",
      "description": "DESCRIPTION",
      "priority": "PRIORITY",
      "collectorIlb": {
        "url": "FORWARDING_RULE_URL"
      },
      "mirroredResources": {
        "subnetworks": [
          {
            "url": "SUBNET_URL"
          }
        ],
        "instances": [
          {
            "url": "INSTANCE_URL"
          }
        ],
        "tags": [
          "NETWORK_TAGS"
        ]
      },
      "filter": {
        "cidrRanges": [
          "CIDR_RANGE"
        ],
        "IPProtocols": [
          "PROTOCOL"
        ],
        "direction": "DIRECTION"
      },
      "enable": "ENABLED"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the policy is located.
  * `REGION`: the region of the packet mirroring policy.
  * `POLICY_NAME`: the name of the packet mirroring policy to modify.
  * `DESCRIPTION`: an optional description of the policy.
  * `PRIORITY`: the policy's priority, which is used to break ties when there are multiple matching policies. The default value is 1,000. The valid range is 0 through 65,535.
  * `FORWARDING_RULE_URL`: the URL of a forwarding rule with Packet Mirroring enabled. Google Cloud sends all mirrored traffic to the associated internal passthrough Network Load Balancer.
  * `SUBNET_URL`: the URL of a subnetwork. Google Cloud mirrors existing and future instances in the subnet. You can provide multiple subnetworks by using a comma-separated list.
  * `INSTANCE_URL`: the URL of a VM instance to mirror. You can provide multiple instances by using a comma-separated list.
  * `NETWORK_TAGS`: a network tag. Google Cloud mirrors instances that have one or more network tags. You can provide multiple tags by using a comma-separated list.
  * `CIDR_RANGE`: one or more IPv4 or IPv6 CIDR ranges to mirror. If no CIDR ranges are specified, all IPv4 traffic that matches the specified protocols is mirrored. If neither CIDR ranges nor protocols are specified, all IPv4 traffic is mirrored. To mirror all IPv4 and IPv6 traffic, use `"0.0.0.0/0", "::/0"`. You can include both IPv4 and IPv6 CIDR ranges. You can provide multiple CIDR ranges by using the following form: `"192.0.2.0/24", "2001:DB8::/32"`.
  * `IP_PROTOCOL`: one or more protocols. Options are `tcp`, `udp`, `icmp`, `esp`, `ah`, `ipip`, `sctp`, or an [IANA protocol number](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). If no protocols are specified, all traffic that matches the specified CIDR ranges is mirrored. If neither CIDR ranges nor protocols are specified, all IPv4 traffic is mirrored. To specify ICMP for IPv6, use `58`. You can provide multiple protocols by using the following form: `"icmp", "udp"`.
  * `DIRECTION`: the direction of traffic to mirror. Options are `INGRESS`, `EGRESS`, or `BOTH`. The default is `BOTH`.
  * `ENABLED`: indicates whether the policy is enabled or not. Options are `TRUE` or `FALSE`.



## List packet mirroring policies

You can list packet mirroring policies to view existing policies.

###  Console 

  * In the Google Cloud console, go to the **Packet Mirroring** page.

[Go to Packet Mirroring](https://console.cloud.google.com/networking/packetmirroring)

The Google Cloud console lists all of the policies in your project.




###  gcloud 

To list packet mirroring policies that are in your project or for a particular region, use the [`packet-mirrorings list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/list).
    
    
    gcloud compute packet-mirrorings list \
      [--filter="region:(REGION...)"]
    

Replace `REGION` with the name of the region that contains the policies to list.

###  API 

To list existing packet mirroring policies in your project, make a `GET` request to the [`packetMirrorings.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/packetMirrorings
    

Replace `PROJECT_ID` with the ID of your project.

To list existing packet mirroring policies for a particular region, make a `GET` request to the [`packetMirrorings.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/packetMirrorings
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the policies to list.
  * `REGION`: the region that contains the policies to list.



## Describe a packet mirroring policy

You can describe a packet mirroring policy to view details such as the policy's filters.

###  Console 

  1. In the Google Cloud console, go to the **Packet Mirroring** page.

[Go to Packet Mirroring](https://console.cloud.google.com/networking/packetmirroring)

  2. From the list of packet mirroring policies, select the policy that you want to view. The Google Cloud console shows the details of the policy that you selected.




###  gcloud 

To describe a packet mirroring policy, use the [`packet-mirrorings describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/describe).
    
    
    gcloud compute packet-mirrorings describe POLICY_NAME \
      --region=REGION \
    

Replace the following:

  * `POLICY_NAME`: the name of the packet mirroring policy to describe.
  * `REGION`: the region where the policy is located.



###  API 

To describe a packet mirroring policy, make a `GET` request to the [`packetMirrorings.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/packetMirrorings/POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the policy is located.
  * `REGION`: the region where the policy is located.
  * `POLICY_NAME`: the name of the packet mirroring policy to describe.



## Disable or enable a packet mirroring policy

You can disable or enable a packet mirroring policy to stop or start collecting mirrored traffic.

###  Console 

  1. In the Google Cloud console, go to the **Packet Mirroring** page.

[Go to Packet Mirroring](https://console.cloud.google.com/networking/packetmirroring)

  2. From the list of packet mirroring policies, select the one to disable or enable.

  3. Click **Disable** or **Enable**.

  4. Confirm by clicking **Disable** or **Enable**.




###  gcloud 

To disable a packet mirroring policy, use the [`packet-mirrorings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update).
    
    
    gcloud compute packet-mirrorings update POLICY_NAME \
      --region=REGION \
      --no-enable
    

Replace the following:

  * `POLICY_NAME`: the name of the packet mirroring policy to disable or enable.
  * `REGION`: the region where the policy is located.



To enable a packet mirroring policy, use the [`packet-mirrorings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/update).
    
    
    gcloud compute packet-mirrorings update POLICY_NAME \
      --region=REGION \
      --enable
    

Replace the following:

  * `POLICY_NAME`: the name of the packet mirroring policy to disable or enable.
  * `REGION`: the region where the policy is located.



###  API 

To disable or enable an existing packet mirroring policy, make a `PATCH` request to the [`packetMirrorings.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/packetMirrorings/POLICY_NAME
    {
      "enable": "FALSE|TRUE"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the policy is located.
  * `REGION`: the region where the policy is located.
  * `POLICY_NAME`: the name of the packet mirroring policy to disable.



## Delete a packet mirroring policy

You can delete a packet mirroring policy to remove it from your project. After you delete a policy, Google Cloud stops mirroring all traffic that is related to the policy.

###  Console 

  1. In the Google Cloud console, go to the **Packet Mirroring** page.

[Go to Packet Mirroring](https://console.cloud.google.com/networking/packetmirroring)

  2. From the list of packet mirroring policies, select the one that you want to delete.

  3. Click **Delete**.

  4. Confirm by clicking **Delete**.




###  gcloud 

To delete a packet mirroring policy, use the [`packet-mirrorings delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/delete).
    
    
    gcloud compute packet-mirrorings delete POLICY_NAME \
      --region=REGION \
    

Replace the following:

  * `POLICY_NAME`: the name of the packet mirroring policy to delete.
  * `REGION`: the region where the policy is located.



###  API 

To delete a packet mirroring policy, make a `DELETE` request to the [`packetMirrorings.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/packetMirrorings/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/packetMirrorings/POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the policy is located.
  * `POLICY_NAME`: the name of the packet mirroring policy to delete.
  * `REGION`: the region where the policy is located.



## Troubleshooting

If your packet mirroring policy isn't collecting the intended mirrored traffic, check the following configurations:

  * Check that you have firewall rules that allow traffic from mirrored instances to the collector instances.

  * Check that your mirrored sources include or exclude the instances to mirror. For example, if you specify a subnet as a mirrored source, all existing and future instances in the subnet are mirrored. If you specify tags, only instances that have matching tags are mirrored.

  * Check that the packet mirroring filters aren't too broad or too narrow. You might have unintentionally configured filters to include or exclude certain traffic.

  * If you have configured a packet mirroring policy to collect IPv6 traffic, ensure that the sources of mirrored traffic are [VMs with IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address) that are connected to [subnets with IPv6 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
