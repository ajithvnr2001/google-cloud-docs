---
url: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal-zonal-neg/
title: Set up an internal passthrough Network Load Balancer with zonal NEGs \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:12.325805+00:00
---

# Set up an internal passthrough Network Load Balancer with zonal NEGs  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal-zonal-neg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up an internal passthrough Network Load Balancer with zonal NEGs Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to deploy an internal passthrough Network Load Balancer with zonal network endpoint group (NEG) backends. Zonal NEGs are [zonal](https://docs.cloud.google.com/compute/docs/regions-zones) resources that represent collections of either IP addresses or IP address/port combinations for Google Cloud resources within a single [subnet](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets). NEGs allow you to create logical groupings of IP addresses or IP address/port combinations that represent _software services_ instead of entire VMs.

Before following this guide, familiarize yourself with the following:

  * [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Zonal NEG overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)



Internal passthrough Network Load Balancers only support zonal NEGs with [`GCE_VM_IP` endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip).

## Permissions

To follow this guide, you need to create instances and modify a network in a project. You should be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you should have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required Role  
---|---  
Create networks, subnets, and load balancer components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Setup overview

This guide shows you how to configure and test an internal passthrough Network Load Balancer with `GCE_VM_IP` zonal NEG backends. The steps in this section describe how to configure the following:

  1. A sample VPC network called `lb-network` with a custom subnet
  2. Firewall rules that allow incoming connections to backend VMs
  3. Four VMs: 
     * VMs `vm-a1` and `vm-a2` in zone `us-west1-a`
     * VMs `vm-c1` and `vm-c2` in zone `us-west1-c`
  4. Two backend zonal NEGs, `neg-a` in zone `us-west1-a`, and `neg-c` in zone `us-west1-c`. Each NEG will have the following endpoints: 
     * `neg-a` contains these two endpoints: 
       * Internal IP address of VM `vm-a1`
       * Internal IP address of VM `vm-a2`
     * `neg-c` contains these two endpoints: 
       * Internal IP address of VM `vm-c1`
       * Internal IP address of VM `vm-c2`
  5. One client VM (`vm-client`) in `us-west1-a` to test connections
  6. The following internal passthrough Network Load Balancer components: 
     * An internal backend service in the `us-west1` region to manage connection distribution to the two zonal NEGs
     * An internal forwarding rule and internal IP address for the frontend of the load balancer



The architecture for this example looks like this:

[ ![Internal passthrough Network Load Balancer configuration with zonal NEGs](https://docs.cloud.google.com/static/load-balancing/images/ilb-zonal-neg-example.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-zonal-neg-example.svg) Internal passthrough Network Load Balancer configuration with zonal NEGs

## Configure a network, region, and subnet

The example internal passthrough Network Load Balancer described on this page is created in a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.

This example's backend VMs, zonal NEGs and load balancer's components are located in this region and subnet:

  * Region: `us-west1`
  * Subnet: `lb-subnet`, with primary IP address range `10.1.2.0/24`

**Note:** You can change the name of the network, the region, and the parameters for the subnet; however, subsequent steps in this guide use the network, region, and subnet parameters as outlined here.

To create the example network and subnet, follow these steps.

###  Console 

  1. Go to the VPC networks page in the Google Cloud console.   
[Go to the VPC network page](https://console.cloud.google.com/networking/networks/list)
  2. Click **Create VPC network**.
  3. Enter a **Name** of `lb-network`.
  4. In the **Subnets** section: 
     * Set the **Subnet creation mode** to **Custom**.
     * In the **New subnet** section, enter the following information: 
       * **Name** : `lb-subnet`
       * **Region** : `us-west1`
       * **IP address range** : `10.1.2.0/24`
       * Click **Done**.
  5. Click **Create**.



###  gcloud 

  1. Create the custom VPC network:
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

     1. Within the `lb-network` network, create a subnet for backend VMs in the `us-west1` region:
    
    gcloud compute networks subnets create lb-subnet \
        --network=lb-network \
        --range=10.1.2.0/24 \
        --region=us-west1
    




## Configure firewall rules

This example uses the following firewall rules:

  * `fw-allow-lb-access`: An ingress rule, applicable to all targets in the VPC network, allowing traffic from sources in the `10.1.2.0/24` range. This rule allows incoming traffic from any client located in `lb-subnet`.

  * `fw-allow-ssh`: An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port 22 from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the system from which you will initiating SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it should apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.   
[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rule** and enter the following information to create the rule to allow subnet traffic: 
     * **Name** : `fw-allow-lb-access`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : All instances in the network
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.1.2.0/24`
     * **Protocols and ports** : Allow all
  3. Click **Create**.
  4. Click **Create firewall rule** again to create the rule to allow incoming SSH connections: 
     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : Choose _Specified protocols and ports_ then type: `tcp:22`
  5. Click **Create**.
  6. Click **Create firewall rule** a third time to create the rule to allow Google Cloud health checks: 
     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : ingress
     * **Action on match** : allow
     * **Targets** : Specified target tags
     * **Target tags** : `allow-health-check`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : Allow all
  7. Click **Create**.



###  gcloud 

  1. Create the `fw-allow-lb-access` firewall rule to allow communication from with the subnet:
         
         gcloud compute firewall-rules create fw-allow-lb-access \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.1.2.0/24 \
             --rules=tcp,udp,icmp
         

  2. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  3. Create the `fw-allow-health-check` rule to allow Google Cloud health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check \
             --source-ranges=35.191.0.0/16 \
             --rules=tcp,udp,icmp
         




## Create NEG backends

To demonstrate the regional nature of internal passthrough Network Load Balancers, this example uses two zonal NEG backends, `neg-a` and `neg-c`, in zones `us-west1-a` and `us- west1-c`. Traffic is load-balanced across both NEGs, and across endpoints within each NEG.

### Create VMs

To support this example, each of the four VMs runs an Apache web server that listens on the following TCP ports: 80, 8008, 8080, 8088, 443, and 8443.

Each VM is assigned an internal IP address in the `lb-subnet` and an ephemeral external (public) IP address. You can remove the external IP addresses later.

External IP addresses are not required for backend VMs; however, they are useful for this example because they permit the VMs to download Apache from the internet, and they let you [connect using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools). By default, Apache is configured to bind to any IP address. Internal passthrough Network Load Balancers deliver packets by preserving the destination IP.

Ensure that server software running on your VMs is listening on the IP address of the load balancer's internal forwarding rule.

For instructional simplicity, these backend VMs run Debian GNU Linux 10.

###  Console 

**Create VMs**

  1. Go to the VM instances page in the Google Cloud console.   
[Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Repeat the following steps to create four VMs, using the following name and zone combinations. 
     * Name: `vm-a1`, zone: `us-west1-a`
     * Name: `vm-a2`, zone: `us-west1-a`
     * Name: `vm-c1`, zone: `us-west1-c`
     * Name: `vm-c2`, zone: `us-west1-c`
  3. Click **Create instance**.
  4. Set the **Name** as indicated in step 2.
  5. For the **Region** , choose `us-west1`, and choose a **Zone** as indicated in step 2.
  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. Click **Choose** to change the image if necessary.
  7. Click **Advanced options** and make the following changes:

     * Click **Networking** and add the following **Network tags** : `allow-ssh` and `allow-health-check`
     * Click **Edit** edit under **Network interfaces** and make the following changes then click **Done** : 
       * **Network** : `lb-network`
       * **Subnet** : `lb-subnet`
       * **Primary internal IP** : Ephemeral (automatic)
       * **External IP** : Ephemeral
     * Click **Management**. In the **Startup script** field, copy and paste the following script contents. The script contents are identical for all four VMs:
           
           #! /bin/bash
           if [ -f /etc/startup_script_completed ]; then
           exit 0
           fi
           apt-get update
           apt-get install apache2 -y
           a2ensite default-ssl
           a2enmod ssl
           file_ports="/etc/apache2/ports.conf"
           file_http_site="/etc/apache2/sites-available/000-default.conf"
           file_https_site="/etc/apache2/sites-available/default-ssl.conf"
           http_listen_prts="Listen 80\nListen 8008\nListen 8080\nListen 8088"
           http_vh_prts="*:80 *:8008 *:8080 *:8088"
           https_listen_prts="Listen 443\nListen 8443"
           https_vh_prts="*:443 *:8443"
           vm_hostname="$(curl -H "Metadata-Flavor:Google" \
           http://metadata.google.internal/computeMetadata/v1/instance/name)"
           echo "Page served from: $vm_hostname" | \
           tee /var/www/html/index.html
           echo "Page served from: $vm_hostname" | \
           tee /var/www/html/index.html
           prt_conf="$(cat "$file_ports")"
           prt_conf_2="$(echo "$prt_conf" | sed "s|Listen 80|${http_listen_prts}|")"
           prt_conf="$(echo "$prt_conf_2" | sed "s|Listen 443|${https_listen_prts}|")"
           echo "$prt_conf" | tee "$file_ports"
           http_site_conf="$(cat "$file_http_site")"
           http_site_conf_2="$(echo "$http_site_conf" | sed "s|*:80|${http_vh_prts}|")"
           echo "$http_site_conf_2" | tee "$file_http_site"
           https_site_conf="$(cat "$file_https_site")"
           https_site_conf_2="$(echo "$https_site_conf" | sed "s|_default_:443|${https_vh_prts}|")"
           echo "$https_site_conf_2" | tee "$file_https_site"
           systemctl restart apache2
           touch /etc/startup_script_completed
           

  8. Click **Create**.




###  gcloud 

Create the four VMs by running the following command four times, using these four combinations for `[VM-NAME]` and `[ZONE]`. The script contents are identical for all four VMs.

  * `[VM-NAME]` of `vm-a1` and `[ZONE]` of `us-west1-a`
  * `[VM-NAME]` of `vm-a2` and `[ZONE]` of `us-west1-a`
  * `[VM-NAME]` of `vm-c1` and `[ZONE]` of `us-west1-c`
  * `[VM-NAME]` of `vm-c2` and `[ZONE]` of `us-west1-c`
        
        gcloud compute instances create VM-NAME \
            --zone=ZONE \
            --image-family=debian-12 \
            --image-project=debian-cloud \
            --tags=allow-ssh,allow-health-check \
            --subnet=lb-subnet \
            --metadata=startup-script='#! /bin/bash
        if [ -f /etc/startup_script_completed ]; then
        exit 0
        fi
        apt-get update
        apt-get install apache2 -y
        a2ensite default-ssl
        a2enmod ssl
        file_ports="/etc/apache2/ports.conf"
        file_http_site="/etc/apache2/sites-available/000-default.conf"
        file_https_site="/etc/apache2/sites-available/default-ssl.conf"
        http_listen_prts="Listen 80\nListen 8008\nListen 8080\nListen 8088"
        http_vh_prts="*:80 *:8008 *:8080 *:8088"
        https_listen_prts="Listen 443\nListen 8443"
        https_vh_prts="*:443 *:8443"
        vm_hostname="$(curl -H "Metadata-Flavor:Google" \
        http://metadata.google.internal/computeMetadata/v1/instance/name)"
        echo "Page served from: $vm_hostname" | \
        tee /var/www/html/index.html
        prt_conf="$(cat "$file_ports")"
        prt_conf_2="$(echo "$prt_conf" | sed "s|Listen 80|${http_listen_prts}|")"
        prt_conf="$(echo "$prt_conf_2" | sed "s|Listen 443|${https_listen_prts}|")"
        echo "$prt_conf" | tee "$file_ports"
        http_site_conf="$(cat "$file_http_site")"
        http_site_conf_2="$(echo "$http_site_conf" | sed "s|*:80|${http_vh_prts}|")"
        echo "$http_site_conf_2" | tee "$file_http_site"
        https_site_conf="$(cat "$file_https_site")"
        https_site_conf_2="$(echo "$https_site_conf" | sed "s|_default_:443|${https_vh_prts}|")"
        echo "$https_site_conf_2" | tee "$file_https_site"
        systemctl restart apache2
        touch /etc/startup_script_completed'
        




### Create `GCE_VM_IP` zonal NEGs

The NEGs (`neg-a` and `neg-c`) must be created in the same zones as the VMs created in the previous step.

###  Console 

To create a zonal network endpoint group:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click **Create network endpoint group**.
  3. Enter a **Name** for the zonal NEG: `neg-a`.
  4. Select the **Network endpoint group type** : **Network endpoint group (Zonal)**.
  5. Select the **Network** : **lb-network**
  6. Select the **Subnet** : **lb-subnet**
  7. Select the **Zone** : **us-west1-a**
  8. Click **Create**.
  9. Repeat these steps to create a second zonal NEG called `neg-c`, in the **us-west1-c** zone.



Add endpoints to the zonal NEG:

  1. Go to the Network Endpoint Groups page in the Google Cloud console.   
[Go to the Network endpoint groups](https://console.cloud.google.com/compute/networkendpointgroups/list)  

  2. Click the **Name** of the first network endpoint group created in the previous step (**neg-a**). You see the **Network endpoint group details** page.
  3. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.

     1. Click **VM instance** and select **vm-a1** to add its internal IP addresses as network endpoints.
     2. Click **Create**.
     3. Again click **Add network endpoint** and under **VM instance** select **vm-a2**.
     4. Click **Create**.
  4. Click the **Name** of the second network endpoint group created in the previous step (**neg-c**). You see the **Network endpoint group details** page.

  5. In the **Network endpoints in this group** section, click **Add network endpoint**. You see the **Add network endpoint** page.

     1. Click **VM instance** and select **vm-c1** to add its internal IP addresses as network endpoints.
     2. Click **Create**.
     3. Again click **Add network endpoint** and under **VM instance** select **vm-c2**.
     4. Click **Create**.



###  gcloud 

  1. Create a `GCE_VM_IP` zonal NEG called `neg-a` in `us-west1-a` using the [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-endpoint-groups/create) command:
         
         gcloud compute network-endpoint-groups create neg-a \
             --network-endpoint-type=gce-vm-ip \
             --zone=us-west1-a \
             --network=lb-network \
             --subnet=lb-subnet
         

  2. Add endpoints to `neg-a`:
         
         gcloud compute network-endpoint-groups update neg-a \
             --zone=us-west1-a \
             --add-endpoint='instance=vm-a1' \
             --add-endpoint='instance=vm-a2'
         

  3. Create a `GCE_VM_IP` zonal NEG called `neg-c` in `us-west1-c` using the [`gcloud compute network-endpoint-groups create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-endpoint-groups/create) command:
         
         gcloud compute network-endpoint-groups create neg-c \
             --network-endpoint-type=gce-vm-ip \
             --zone=us-west1-c \
             --network=lb-network \
             --subnet=lb-subnet
         

  4. Add endpoints to `neg-c`:
         
         gcloud compute network-endpoint-groups update neg-c \
             --zone=us-west1-c \
             --add-endpoint='instance=vm-c1' \
             --add-endpoint='instance=vm-c2'
         




## Configure load balancer components

These steps configure all of the [internal passthrough Network Load Balancer components](https://docs.cloud.google.com/load-balancing/docs/internal#components):

  * **Backend service** : For this example, you need to pass HTTP traffic through the load balancer. Therefore, you need to use TCP, not UDP.

  * **Forwarding rule** : This example creates a single internal forwarding rule.

  * **Internal IP address** : In this example, you specify an internal IP address, `10.1.2.99`, when you create the forwarding rule.




###  Console 

**Note:** You cannot use the Google Cloud console to create or manage an internal passthrough Network Load Balancer with `GCE_VM_IP` zonal NEGs. Use either [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-endpoint-groups/create) or the [REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups).

###  gcloud 

  1. Create a new regional HTTP health check.
         
         gcloud compute health-checks create http hc-http-80 \
             --region=us-west1 \
             --port=80
         

  2. Create the backend service:
         
         gcloud compute backend-services create bs-ilb \
             --load-balancing-scheme=internal \
             --protocol=tcp \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  3. Add the two zonal NEGs, `neg-a` and `neg-c`, to the backend service:
         
         gcloud compute backend-services add-backend bs-ilb \
             --region=us-west1 \
             --network-endpoint-group=neg-a \
             --network-endpoint-group-zone=us-west1-a
         
         
         gcloud compute backend-services add-backend bs-ilb \
             --region=us-west1 \
             --network-endpoint-group=neg-c \
             --network-endpoint-group-zone=us-west1-c
         

  4. Create a forwarding rule for the backend service. When you create the forwarding rule, specify `10.1.2.99` for the internal IP address in the subnet.
         
         gcloud compute forwarding-rules create fr-ilb \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --network=lb-network \
             --subnet=lb-subnet \
             --address=10.1.2.99 \
             --ip-protocol=TCP \
             --ports=80,8008,8080,8088 \
             --backend-service=bs-ilb \
             --backend-service-region=us-west1
         




## Test the load balancer

This test contacts the load balancer from a separate client VM; that is, not from a backend VM of the load balancer. The expected behavior is for traffic to be distributed among the four backend VMs [because no session affinity has been configured](https://docs.cloud.google.com/load-balancing/docs/internal#traffic_distribution).

### Create a test client VM

This example creates a client VM (`vm-client`) in the same region as the backend (server) VMs. The client is used to validate the load balancer's configuration and demonstrate expected behavior as described in the testing section.

###  Console 

  1. Go to the VM instances page in the Google Cloud console.   
[Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Click **Create instance**.
  3. Set the **Name** to `vm-client`.
  4. Set the **Zone** to `us-west1-a`.
  5. Click **Advanced options** and make the following changes: 
     * Click **Networking** and add the `allow-ssh` to **Network tags**.
     * Click the edit button under **Network interfaces** and make the following changes then click **Done** : 
       * **Network** : `lb-network`
       * **Subnet** : `lb-subnet`
       * **Primary internal IP** : Ephemeral (automatic)
       * **External IP** : Ephemeral
  6. Click **Create**.



###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client \
        --zone=us-west1-a \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=lb-subnet
    

### Send traffic to the load balancer

Perform the following steps to connect to the load balancer.

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Make a web request to the load balancer using `curl` to contact its IP address. Repeat the request so you can see that responses come from different backend VMs. The name of the VM generating the response is displayed in the text in the HTML response, by virtue of the contents of `/var/www/html/index.html` on each backend VM. Expected responses look like: `Page served from: vm-a1` and `Page served from: vm-a2`.
         
         curl http://10.1.2.99
         

The forwarding rule is configured to serve ports `80`, `8008`, `8080`, and `8088`. To send traffic to those other ports, append a colon (`:`) and the port number after the IP address, like this:
         
         curl http://10.1.2.99:8008
         




## What's next

  * To set up additional configuration options, such as enabling global access, accepting traffic on all ports, and accepting traffic on multiple ports using two forwarding rules, see [Additional configuration options for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#additional-configuration-options).
  * See [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal) for important fundamentals.
  * See [Failover concepts for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) for important information about failover.
  * See [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring) for information about configuring Logging and Monitoring for internal passthrough Network Load Balancers.
  * See [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks) for information about accessing internal passthrough Network Load Balancers from peer networks connected to your VPC network.
  * See [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb) for information about how to troubleshoot issues with your internal passthrough Network Load Balancer.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
