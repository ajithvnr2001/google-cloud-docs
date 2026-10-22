---
url: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal-next-hop-tags/
title: Set up an internal passthrough Network Load Balancer as next hop (with tags) \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:29.466670+00:00
---

# Set up an internal passthrough Network Load Balancer as next hop (with tags)  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal-next-hop-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up an internal passthrough Network Load Balancer as next hop (with tags) Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial uses an example to show you how to deploy an [internal passthrough Network Load Balancer as the next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview) to which packets are forwarded along the path to their final destination. You use network tags to configure the specific client instances to which the route applies.

This guide assumes that you are familiar with the workings of an internal passthrough Network Load Balancer, its related components such as firewall rules and health checks, and how internal passthrough Network Load Balancers are used as next hops to forward packets on a route.

With the internal passthrough Network Load Balancer as next hop feature, you can integrate third-party appliances in a highly available, scaled-out manner. To do this, you need to configure a custom static route and set the next hop to the load balancer, which will distributes traffic for the destination prefix to the pool of health-checked third-party VM appliances. You have several options when selecting your next hops to support high availability of these third-party appliances:

  * **Specify an IP address as next hop:** Use the [internal IP address associated with the forwarding rule as the next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#ilb-next-hop-specify). This load balancer's virtual IP address can be learned across peers without having to export the custom route through its peers.
  * **Use network tags:** You can specify a network tag so that the internal passthrough Network Load Balancer as next hop route only applies to client instances that have been configured with the tag. This lets you select which client instances get populated with which tagged internal passthrough Network Load Balancer as next hop route and which set of appliances to route your traffic to. You don't need to segregate the different client instances into separate VPCs, each pointing to their preferred internal passthrough Network Load Balancer front-ending a set of appliances. Tagged routes are not exported or imported through VPC Network Peering.
  * **Configure multiple routes to the same destination prefix:** With tags you can specify multiple routes to the same destination with different internal load balancers as next hops. Although ECMP isn't supported (same destination prefix, same tags, different next hops), you can use different tags or different priorities for these same destination routes.



## Setup overview

Managed instance groups using VMs with a single NIC are defined in different regions, with Linux instances configured to SNAT-translate all outbound traffic to the internet (North-South outbound traffic flow). Regional failover is triggered manually. This tutorial also demonstrates East-West connectivity with symmetric hashing using an internal passthrough Network Load Balancer as next hop.

The steps in this section describe how to configure the following:

  1. Sample VPC networks with custom subnets
  2. Firewall rules that allow incoming connections to backend VMs
  3. Backend managed instance groups that deploy NAT gateways
  4. Client VMs to test connections
  5. The following internal passthrough Network Load Balancer components: 
     * A health check for the backend service
     * An internal backend service
     * An internal forwarding rule and IP address for the frontend of the load balancer



The architecture for this example looks like this:

[ ![Internal passthrough Network Load Balancer as next hop configuration](https://docs.cloud.google.com/static/load-balancing/images/ilb-next-hop-tags-tutorial.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-next-hop-tags-tutorial.svg) Internal passthrough Network Load Balancer as next hop configuration (click to enlarge)

As you follow the steps in this tutorial, replace REGION_A and REGION_B with the respective regions that you want to use for this example.

## Create the VPC networks and subnets

  1. Create a VPC network called `hub-vpc`.
         
         gcloud compute networks create hub-vpc --subnet-mode custom
         

  2. Create a subnet in `hub-vpc` in REGION_A.
         
         gcloud compute networks subnets create hub-subnet-a \
             --network hub-vpc \
             --range 10.0.0.0/24 \
             --region REGION_A
         

  3. Create a subnet in `hub-vpc` in region B.
         
         gcloud compute networks subnets create hub-subnet-b \
             --network hub-vpc \
             --range 10.0.1.0/24 \
             --region REGION_B
         

  4. Create a VPC network called `spoke1-vpc`.
         
         gcloud compute networks create spoke1-vpc --subnet-mode custom
         

  5. Create a subnet in `spoke1-vpc`.
         
         gcloud compute networks subnets create spoke1-subnet1 \
             --network spoke1-vpc \
             --range 192.168.0.0/24 \
             --region REGION_A
         

  6. Create a VPC network called `spoke2-vpc`.
         
         gcloud compute networks create spoke2-vpc --subnet-mode custom
         

  7. Create a subnet in `spoke2-vpc`.
         
         gcloud compute networks subnets create spoke2-subnet1 \
             --network spoke2-vpc \
             --range 192.168.1.0/24 \
             --region REGION_A
         




## Configure firewall rules

  1. Configure the following firewall rules to allow TCP, UDP, and ICMP traffic to reach instances from the specified source ranges.
         
         gcloud compute firewall-rules create hub-vpc-web-ping-dns \
             --network hub-vpc \
             --allow tcp:80,tcp:443,icmp,udp:53 \
             --source-ranges 10.0.0.0/24,10.0.1.0/24,192.168.0.0/24,192.168.1.0/24
         
         
         gcloud compute firewall-rules create spoke1-vpc-web-ping-dns \
             --network spoke1-vpc \
             --allow tcp:80,tcp:443,icmp,udp:53 \
             --source-ranges 10.0.0.0/24,10.0.1.0/24,192.168.0.0/24,192.168.1.0/24
         
         
         gcloud compute firewall-rules create spoke2-vpc-web-ping-dns \
             --network spoke2-vpc \
             --allow tcp:80,tcp:443,icmp,udp:53 \
             --source-ranges 10.0.0.0/24,10.0.1.0/24,192.168.0.0/24,192.168.1.0/24
         

  2. Create a firewall rule to allow health check probers to access instances on `hub-vpc`.
         
         gcloud compute firewall-rules create hub-vpc-health-checks \
             --network hub-vpc \
             --allow tcp:80 \
             --target-tags natgw \
             --source-ranges 35.191.0.0/16
         

  3. Create firewall rules to allow SSH access for instances on all subnets. If you prefer to use Identity-Aware Proxy for TCP forwarding (recommended), [follow these steps to enable SSH](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).
         
         gcloud compute firewall-rules create hub-vpc-allow-ssh \
             --network hub-vpc \
             --allow tcp:22
         
         
         gcloud compute firewall-rules create spoke1-vpc-allow-ssh \
             --network spoke1-vpc \
             --allow tcp:22
         
         
         gcloud compute firewall-rules create spoke2-vpc-allow-ssh \
             --network spoke2-vpc \
             --allow tcp:22
         




## Configure VPC Network Peering

  1. Create a peering from `hub-vpc` to `spoke1-vpc`.
         
         gcloud compute networks peerings create hub-to-spoke1 \
             --network hub-vpc \
             --peer-network spoke1-vpc \
             --peer-project PROJECT_ID \
             --export-custom-routes
             

  2. Create a peering from `spoke1-vpc` to `hub-vpc`.
         
         gcloud compute networks peerings create spoke1-to-hub \
             --network spoke1-vpc \
             --peer-network hub-vpc \
             --peer-project PROJECT_ID \
             --import-custom-routes
         

  3. Create a peering from `hub-vpc` to `spoke2-vpc`.
         
         gcloud compute networks peerings create hub-to-spoke2 \
             --network hub-vpc \
             --peer-network spoke2-vpc \
             --peer-project PROJECT_ID \
             --export-custom-routes
         

  4. Create a peering from `spoke2-vpc` to `hub-vpc`.
         
         gcloud compute networks peerings create spoke2-to-hub \
             --network spoke2-vpc \
             --peer-network hub-vpc \
             --peer-project PROJECT_ID \
             --import-custom-routes
         




## Create NAT gateway VMs and load balancing resources in region A

Create the managed instance group backend in REGION_A. Then create the load balancing resources and next hop routes.

### Create a managed instance group

  1. Create an instance template to deploy a NAT gateway in region A.
         
         gcloud compute instance-templates create hub-natgw-region-a-template \
             --network hub-vpc \
             --subnet hub-subnet-a \
             --region REGION_A \
             --machine-type n1-standard-2 \
             --can-ip-forward \
             --tags natgw \
             --metadata startup-script='#! /bin/bash
         # Enable IP forwarding:
         echo 1 > /proc/sys/net/ipv4/ip_forward
         echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/20-iptables.conf
         # iptables configuration
         iptables -t nat -F
         sudo iptables -t nat -A POSTROUTING ! -d 192.168.0.0/16 -j MASQUERADE
         iptables-save
         # Use a web server to pass the health check for this example.
         # You should use a more complete test in production.
         apt-get update
         apt-get install apache2 tcpdump -y
         a2ensite default-ssl
         a2enmod ssl
         echo "Example web page to pass health check" | \
         tee /var/www/html/index.html \
         systemctl restart apache2'
         

  2. Create the instance group in REGION_A.
         
         gcloud compute instance-groups managed create hub-natgw-region-a-mig \
             --region REGION_A \
             --size=2 \
             --template=hub-natgw-region-a-template
         




### Create the load balancer

Perform the following steps to create a load balancer in REGION_A.

  1. Create a health check.
         
         gcloud compute health-checks create http natgw-ilbnhop-health-check \
             --port=80
         

  2. Create the backend service.
         
         gcloud compute backend-services create hub-natgw-region-a-be \
             --load-balancing-scheme=internal \
             --protocol tcp \
             --region REGION_A\
             --health-checks=natgw-ilbnhop-health-check
         

  3. Add the managed instance group as a backend.
         
         gcloud compute backend-services add-backend hub-natgw-region-a-be \
             --instance-group=hub-natgw-region-a-mig \
             --instance-group-region=REGION_A
         

  4. Create the forwarding rule.
         
         gcloud compute forwarding-rules create hub-natgw-region-a \
             --load-balancing-scheme=internal \
             --network=hub-vpc \
             --subnet=hub-subnet-a \
             --address=10.0.0.10 \
             --ip-protocol=TCP \
             --ports=all \
             --allow-global-access \
             --backend-service=hub-natgw-region-a-be \
             --backend-service-region=REGION_A
         




### Create the next hop routes

Create the internal passthrough Network Load Balancer as next hop routes with the pre-defined network tag `ilbanh-region-a`.
    
    
    gcloud compute routes create spoke1-natgw-region-a \
        --network=spoke1-vpc \
        --destination-range=0.0.0.0/0 \
        --next-hop-ilb=10.0.0.10 \
        --tags=ilbanh-region-a \
        --priority 800
    
    
    
    gcloud compute routes create spoke2-natgw-region-a \
        --network=spoke2-vpc \
        --destination-range=0.0.0.0/0 \
        --next-hop-ilb=10.0.0.10 \
        --tags=ilbanh-region-a \
        --priority 800
    

### Test connectivity

Create client instances to test connectivity.

  1. Create a test client instance in `spoke1-vpc`.
         
         gcloud compute instances create spoke1-client \
             --subnet=spoke1-subnet1 --no-address --zone ZONE_A \
             --tags=ilbanh-region-a \
             --metadata startup-script='#! /bin/bash
         apt-get update
         apt-get install tcpdump -y'
         

  2. Create a test client instance in `spoke2-vpc`.
         
         gcloud compute instances create spoke2-client \
             --subnet=spoke2-subnet1 --no-address --zone ZONE_A \
             --tags=ilbanh-region-a \
             --metadata startup-script='#! /bin/bash
         apt-get update
         apt-get install tcpdump -y'
         




## Validate North-South and East-West traffic flows

  1. Make sure that the NAT gateway VMs are running, and _write down_ the assigned external IP addresses:
         
         gcloud compute instances list --filter="status:RUNNING AND name~natgw"
         

  2. Confirm that the load balancer is healthy and the routes were created as expected:
         
         gcloud compute backend-services get-health hub-natgw-region-a-be --region REGION_A
         
         
         backend: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/regions/us-central1/instanceGroups/hub-natgw-region-a-mig
         status:
           healthStatus:
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/regions/us-central1/forwardingRules/hub-natgw-region-a
             forwardingRuleIp: 10.0.0.10
             healthState: HEALTHY
             instance: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/zones/us-central1-b/instances/<INSTANCE_NAME>
             ipAddress: 10.0.0.5
             port: 80
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/regions/us-central1/forwardingRules/hub-natgw-region-a
             forwardingRuleIp: 10.0.0.10
             healthState: HEALTHY
             instance: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/zones/us-central1-f/instances/<INSTANCE_NAME>
             ipAddress: 10.0.0.6
             port: 80
           kind: compute#backendServiceGroupHealth
         

  3. Verify that the internal passthrough Network Load Balancer as next hop routes are added to the spoke VPCs with the expected priority and targeting the internal passthrough Network Load Balancer's IP address:
         
         gcloud compute routes list --filter="name~natgw"
         

  4. Go to the Google Cloud console and establish SSH connections to the NAT gateway VMs in different tabs.

  5. Start `tcpdump` in each of those SSH sessions by using the following command:
         
         sudo tcpdump -n net 192.168.0.0/16
         

  6. Go to the Google Cloud console and establish a new SSH connection to the `spoke1-client` VM. Then use the following command to ping the `spoke2-client` [internal IP address](https://docs.cloud.google.com/compute/docs/instances/view-network-properties#view_ip_addresses).
         
         ping SPOKE2_CLIENT_INTERNAL_IP
         

  7. Switch to the NAT gateway SSH windows and verify that you can see the ICMP packets as follows:
         
         16:51:28.411260 IP 192.168.0.2 > 192.168.1.2: ICMP echo request, id 1684, seq 492, length 64
         16:51:28.411676 IP 192.168.1.2 > 192.168.0.2: ICMP echo reply, id 1684, seq 492, length 64
         

You should be able to successfully ping the client VM, which demonstrates the following:

     * East-West traffic is enabled through the NAT gateways. Note that [transitive peering is not supported](https://docs.cloud.google.com/vpc/docs/vpc-peering#restrictions) between spoke VPCs.
     * [Symmetric hashing](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#symmetric-hashing) is enabled and working as expected, since the clients can communicate using their source IP addresses, without requiring SNAT translation.
     * [All protocols are supported with internal passthrough Network Load Balancer as next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#all-traffic).
  8. Stop the tcpdump outputs on the NAT gateway VMs and watch the `iptables` statistics:
         
         watch sudo iptables -t nat -nvL
         

  9. Switch back to the `spoke1-client` VM and run the following command multiple times. The output displays the public source IP address being used to connect to the website.
         
         curl ifconfig.io
         

You should see the IP addresses of both NAT gateway VMs displayed as source IP addresses. This demonstrates that the internal passthrough Network Load Balancer is distributing the traffic based on the [default affinity](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity) (5-tuple hashing).

  10. Switch back to the NAT gateway VM to confirm that the packet counters increased.
         
         Chain PREROUTING (policy ACCEPT 0 packets, 0 bytes)
          pkts bytes target     prot opt in     out     source               destination
         
         Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
          pkts bytes target     prot opt in     out     source               destination
         
         Chain POSTROUTING (policy ACCEPT 0 packets, 0 bytes)
          pkts bytes target     prot opt in     out     source               destination
           105 11442 MASQUERADE  all  --  *      *       0.0.0.0/0           !192.168.0.0/16
         
         Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
          pkts bytes target     prot opt in     out     source               destination
         




## Create NAT gateway VMs and load balancing resources in region B

Create the managed instance group backend in region B. Then create the load balancing resources and next hop routes.

### Create a managed instance group

  1. Create an instance template to deploy a NAT gateway in region B.
         
         gcloud compute instance-templates create hub-natgw-region-b-template \
             --network hub-vpc \
             --subnet hub-subnet-b --region REGION_B \
             --machine-type n1-standard-2 --can-ip-forward \
             --tags natgw \
             --metadata startup-script='#! /bin/bash
         # Enable IP forwarding:
         echo 1 > /proc/sys/net/ipv4/ip_forward
         echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/20-iptables.conf
         # iptables configuration
         iptables -t nat -F
         sudo iptables -t nat -A POSTROUTING ! -d 192.168.0.0/16 -j MASQUERADE
         iptables-save
         # Use a web server to pass the health check for this example.
         # You should use a more complete test in production.
         apt-get update
         apt-get install apache2 tcpdump -y
         a2ensite default-ssl
         a2enmod ssl
         echo "Example web page to pass health check" | \
         tee /var/www/html/index.html \
         systemctl restart apache2'
         

  2. Create the instance group in region B.
         
         gcloud compute instance-groups managed create hub-natgw-region-b-mig \
             --region REGION_B \
             --size=2 \
             --template=hub-natgw-region-b-template
         




### Create the load balancer

Perform the following steps to create a load balancer in region B.

  1. Create the backend service.
         
         gcloud compute backend-services create hub-natgw-region-b-be \
             --load-balancing-scheme=internal \
             --protocol tcp \
             --region REGION_B\
             --health-checks=natgw-ilbnhop-health-check
         

  2. Add the managed instance group as a backend.
         
         gcloud compute backend-services add-backend hub-natgw-region-b-be \
             --instance-group=hub-natgw-region-b-mig \
             --instance-group-region=REGION_B
         

  3. Create the forwarding rule.
         
         gcloud compute forwarding-rules create hub-natgw-region-b \
             --load-balancing-scheme=internal \
             --network=hub-vpc \
             --subnet=hub-subnet-b \
             --address=10.0.1.10 \
             --ip-protocol=TCP \
             --ports=all \
             --allow-global-access \
             --backend-service=hub-natgw-region-b-be \
             --backend-service-region=REGION_B
         




### Create the next hop routes

Create the internal passthrough Network Load Balancer as next hop routes with the pre-defined network tag `ilbanh-region-a`.
    
    
    gcloud compute routes create spoke1-natgw-region-b \
        --network=spoke1-vpc \
        --destination-range=0.0.0.0/0 \
        --next-hop-ilb=10.0.1.10 \
        --tags=ilbanh-region-a \
        --priority 900
    
    
    
    gcloud compute routes create spoke2-natgw-region-b \
        --network=spoke2-vpc \
        --destination-range=0.0.0.0/0 \
        --next-hop-ilb=10.0.1.10 \
        --tags=ilbanh-region-a \
        --priority 900
    

## Validate regional failover

  1. Make sure that the NAT gateway VMs are running, and _write down_ the assigned external IPs:
         
         gcloud compute instances list --filter="status:RUNNING AND name~natgw"
         

  2. Confirm that the load balancer is healthy and that the routes are created as expected:
         
         gcloud compute backend-services get-health hub-natgw-region-b-be --region REGION_B
         
         
         backend: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/regions/us-west2/instanceGroups/hub-natgw-region-b-mig
         status:
           healthStatus:
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/regions/us-west2/forwardingRules/hub-natgw-region-b
             forwardingRuleIp: 10.0.1.10
             healthState: HEALTHY
             instance: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/zones/us-west2-a/instances/<INSTANCE_NAME>
             ipAddress: 10.0.1.3
             port: 80
           - forwardingRule: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/regions/us-west2/forwardingRules/hub-natgw-region-b
             forwardingRuleIp: 10.0.1.10
             healthState: HEALTHY
             instance: https://www.googleapis.com/compute/v1/projects/<PROJECT_ID>/zones/us-west2-b/instances/<INSTANCE_NAME>
             ipAddress: 10.0.1.2
             port: 80
           kind: compute#backendServiceGroupHealth
         

  3. Verify that the internal passthrough Network Load Balancer as next hop routes are added to the spoke VPCs with the expected priority and targeting the internal passthrough Network Load Balancer's IP address:
         
         gcloud compute routes list --filter="name~natgw"
         

  4. You can now validate regional failover by deleting the high-priority routes and making note of what happens. Switch to the `spoke1-client` VM and run the following command to send a curl request every second. This command also reports the external IP address being used:
         
         while true; do echo -n `date` && echo -n ' - ' && curl ifconfig.io --connect-timeout 1; done
         

Only the external IP addresses assigned to the NAT gateways in region A should be displayed, because it is the high-priority route. Leave the `curl` command running and switch to Cloud Shell to delete the route to the internal passthrough Network Load Balancer in region A to verify the result:
         
         gcloud -q compute routes delete spoke1-natgw-region-a
         

In region B, the external IP addresses that are assigned to the NAT gateway VMs appear, likely with minimal downtime, which demonstrates that the regional failover was successful.


**Note:** A route is _not_ removed automatically even if all backends are unhealthy. Consider using [Cloud Run functions](https://docs.cloud.google.com/functions) to automate this process.

## Clean up resources

  1. Remove the internal passthrough Network Load Balancer as next hop routes:
         
         gcloud -q compute routes delete spoke1-natgw-region-b
         
         gcloud -q compute routes delete spoke2-natgw-region-a
         
         gcloud -q compute routes delete spoke2-natgw-region-b
         

  2. Remove the internal passthrough Network Load Balancer resources and backends:
         
         gcloud -q compute forwarding-rules delete hub-natgw-region-a \
           --region REGION_A
         
         gcloud -q compute backend-services delete hub-natgw-region-a-be \
           --region REGION_A
         
         gcloud -q compute instance-groups managed delete hub-natgw-region-a-mig \
           --region REGION_A
         
         gcloud -q compute instance-templates delete hub-natgw-region-a-template
         
         gcloud -q compute forwarding-rules delete hub-natgw-region-b \
           --region REGION_B
         
         gcloud -q compute backend-services delete hub-natgw-region-b-be \
           --region REGION_B
         
         gcloud -q compute instance-groups managed delete hub-natgw-region-b-mig \
           --region REGION_B
         
         gcloud -q compute instance-templates delete hub-natgw-region-b-template
         
         gcloud -q compute health-checks delete natgw-ilbnhop-health-check
         

  3. Delete the client VMs:
         
         gcloud -q compute instances delete spoke1-client \
           --zone=ZONE_A
         
         gcloud -q compute instances delete spoke2-client \
           --zone=ZONE_A
         

  4. Delete the VPC Network Peerings, firewall rules, subnets, and VPCs:
         
         gcloud -q compute networks peerings delete spoke2-to-hub \
           --network spoke2-vpc
         
         gcloud -q compute networks peerings delete spoke1-to-hub \
           --network spoke1-vpc
         
         gcloud -q compute networks peerings delete hub-to-spoke1 \
           --network hub-vpc
         
         gcloud -q compute networks peerings delete hub-to-spoke2 \
           --network hub-vpc
         
         gcloud -q compute firewall-rules delete spoke2-vpc-web-ping-dns
         
         gcloud -q compute firewall-rules delete spoke1-vpc-web-ping-dns
         
         gcloud -q compute firewall-rules delete hub-vpc-web-ping-dns
         
         gcloud -q compute firewall-rules delete hub-vpc-health-checks
         
         gcloud -q compute firewall-rules delete hub-vpc-allow-ssh
         
         gcloud -q compute firewall-rules delete spoke1-vpc-allow-ssh
         
         gcloud -q compute firewall-rules delete spoke2-vpc-allow-ssh
         
         gcloud -q compute networks subnets delete spoke1-subnet1 \
           --region REGION_A
         
         gcloud -q compute networks subnets delete spoke2-subnet1 \
           --region REGION_A
         
         gcloud -q compute networks subnets delete hub-subnet-a \
           --region REGION_A
         
         gcloud -q compute networks subnets delete hub-subnet-b \
           --region REGION_B
         
         gcloud -q compute networks delete spoke1-vpc
         
         gcloud -q compute networks delete spoke2-vpc
         
         gcloud -q compute networks delete hub-vpc
         




## What's next

  * See [Failover concepts for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) for important information about failover.
  * See [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring) for information on configuring Logging and Monitoring for internal passthrough Network Load Balancer.
  * See [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks) for information about accessing internal passthrough Network Load Balancers from peer networks connected to your VPC network.
  * See [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb) for information on how to troubleshoot issues with your internal passthrough Network Load Balancer.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
