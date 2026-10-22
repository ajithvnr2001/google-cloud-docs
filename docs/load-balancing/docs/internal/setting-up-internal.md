---
url: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal/
title: Set up an internal passthrough Network Load Balancer with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:11.977603+00:00
---

# Set up an internal passthrough Network Load Balancer with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up an internal passthrough Network Load Balancer with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

This guide uses an example to teach the fundamentals of Google Cloud internal passthrough Network Load Balancers. Before following this guide, familiarize yourself with the following:

  * [Internal passthrough Network Load Balancer concepts](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [How internal passthrough Network Load Balancers work](https://docs.cloud.google.com/load-balancing/docs/internal#how_ilb_works)
  * [Firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls)
  * [Health check concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts)



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/welcome?walkthrough_id=load-balancing--internal-tcp-udp-load-balancer-vm-backends)

* * *

## Permissions

To follow this guide, you need to create instances and modify a network in a project. You need to be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you need to have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required role  
---|---  
Create networks, subnets, and load balancer components | [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
(`roles/compute.networkAdmin`)   
Add and remove firewall rules | [Compute Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
(`roles/compute.securityAdmin`)   
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
(`roles/compute.instanceAdmin`)   
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Set up load balancer with IPv4-only subnets and backends

This guide shows you how to configure and test an internal passthrough Network Load Balancer. The steps in this section describe how to configure the following:

  1. An example that uses a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network`.
  2. A _single-stack_ subnet (`stack-type` set to `IPv4`), which is required for IPv4 traffic. When you create a single stack subnet on a custom mode VPC network, you choose an [IPv4 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) for the subnet.
  3. Firewall rules that allow incoming connections to backend virtual machine (VM) instances.
  4. The backend instance group, which is located in the following region and subnet for this example: 
     * Region: `us-west1`
     * Subnet: `lb-subnet`, with primary IPv4 address range `10.1.2.0/24`.
  5. Four backend VMs: two VMs in an unmanaged instance group in zone `us-west1-a` and two VMs in an unmanaged instance group in zone `us-west1-c`. To demonstrate [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access), this example creates a second test client VM in a different region and subnet: 
     * Region: `europe-west1`
     * Subnet: `europe-subnet`, with primary IP address range `10.3.4.0/24`
  6. One client VM to test connections.
  7. The following internal passthrough Network Load Balancer components: 
     * A health check for the backend service.
     * An internal backend service in the `us-west1` region to manage connection distribution to the two zonal instance groups.
     * An internal forwarding rule and internal IP address for the frontend of the load balancer.

**Note:** You can change the name of the network, the region, and the parameters for the subnet; however, subsequent steps in this guide use the network, region, and subnet parameters as outlined in the previous steps.

The architecture for this example looks like this:

[ ![Internal passthrough Network Load Balancer example configuration.](https://docs.cloud.google.com/static/load-balancing/images/ilb-example.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-example.svg) Internal passthrough Network Load Balancer example configuration (click to enlarge).**Note:** For simplicity, this example uses unmanaged instance groups. In production, consider using a managed instance group, as illustrated in Managed instance groups.

### Configure a network, region, and subnet

To create the example network and subnet, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network`.

  4. In the **Subnets** section, do the following:

     1. Set the **Subnet creation mode** to **Custom**.
     2. In the **New subnet** section, enter the following information: 
        * **Name** : `lb-subnet`
        * **Region** : `us-west1`
        * **IP stack type** : **IPv4 (single-stack)**
        * **IP address range** : `10.1.2.0/24`
     3. Click **Done**.
     4. Click **Add subnet** and enter the following information: 
        * **Name** : `europe-subnet`
        * **Region** : `europe-west1`
        * **IP stack type** : **IPv4 (single-stack)**
        * **IP address range** : `10.3.4.0/24`
     5. Click **Done**.
  5. Click **Create**.




###  gcloud 

  1. Create the custom VPC network:
         
         gcloud compute networks create lb-network --subnet-mode=custom
         

  2. In the `lb-network` network, create a subnet for backends in the `us-west1` region:
         
         gcloud compute networks subnets create lb-subnet \
             --network=lb-network \
             --range=10.1.2.0/24 \
             --region=us-west1
         

  3. In the `lb-network` network, create another subnet for testing global access in the `europe-west1` region:
         
         gcloud compute networks subnets create europe-subnet \
             --network=lb-network \
             --range=10.3.4.0/24 \
             --region=europe-west1
         




###  API 

Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    
    {
     "routingConfig": {
       "routingMode": "REGIONAL"
     },
     "name": "lb-network",
     "autoCreateSubnetworks": false
    }
    

Make two `POST` requests to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks
    
    {
     "name": "lb-subnet",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
     "ipCidrRange": "10.1.2.0/24",
     "privateIpGoogleAccess": false
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/europe-west1/subnetworks
    
    {
     "name": "europe-subnet",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
      "ipCidrRange": "10.3.4.0/24",
      "privateIpGoogleAccess": false
    }
    

### Configure firewall rules

This example uses the following firewall rules:

  * `fw-allow-lb-access`: An ingress rule, applicable to all targets in the VPC network, allowing traffic from sources in the `10.1.2.0/24` and `10.3.4.0/24` ranges. This rule allows incoming traffic from any client located in either of the two subnets. It later lets you to configure and test global access.

  * `fw-allow-ssh`: An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port 22 from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the system from which you will be initiating SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it should apply.

  * `fw-allow-health-check`: An ingress rule, applicable to the instances being load balanced, that allows traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the instances to which it should apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

**Note:** You must create a firewall rule to allow health checks from the IP ranges of Google Cloud probe systems. For more information, see [probe IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow subnet traffic, click **Create firewall rule** and enter the following information:

     * **Name** : `fw-allow-lb-access`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **All instances in the network**
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.1.2.0/24`
     * **Protocols and ports** : **Allow all**
  3. Click **Create**.

  4. To allow incoming SSH connections, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : Select **Specified protocols and ports** , select the **TCP** checkbox, and then enter `22` in **Ports**.
  5. Click **Create**.

  6. To allow Google Cloud health checks, click **Create firewall rule** a third time and enter the following information:

     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : **Allow all**
  7. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-lb-access` firewall rule to allow communication from within the subnet:
         
         gcloud compute firewall-rules create fw-allow-lb-access \
             --network=lb-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.1.2.0/24,10.3.4.0/24 \
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
         




###  API 

Create the `fw-allow-lb-access` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    {
     "name": "fw-allow-lb-access",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
     "priority": 1000,
     "sourceRanges": [
       "10.1.2.0/24", "10.3.4.0/24"
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
    

Create the `fw-allow-ssh` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
    
    
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
    

Create the `fw-allow-health-check` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
    
    {
     "name": "fw-allow-health-check",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
     "priority": 1000,
     "sourceRanges": [HEALTH_CHECK_RANGES],
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
    

Replace the following:

  * PROJECT_ID: the project ID

  * HEALTH_CHECK_RANGES: the comma-separated list of [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges), formatted as quoted strings (for example, "192.0.2.0/24", "198.51.100.0/24")




### Create backend VMs and instance groups

This example uses two _unmanaged_ instance groups each having two backend (server) VMs. To demonstrate the regional nature of internal passthrough Network Load Balancers, the two instance groups are placed in separate zones, `us-west1-a` and `us-west1-c`.

  * Instance group `ig-a` contains these two VMs: 
    * `vm-a1`
    * `vm-a2`
  * Instance group `ig-c` contains these two VMs: 
    * `vm-c1`
    * `vm-c2`



Traffic to all four of the backend VMs is load balanced.

To support this example and the additional configuration options, each of the four VMs runs an Apache web server that listens on the following TCP ports: 80, 8008, 8080, 8088, 443, and 8443.

Each VM is assigned an internal IP address in the `lb-subnet` and an ephemeral external (public) IP address. You can remove the external IP addresses later.

External IP address for the backend VMs are not required; however, they are useful for this example because they permit the backend VMs to download Apache from the internet, and they can [connect using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#connect_to_vms).

By default, Apache is configured to bind to any IP address. Internal passthrough Network Load Balancers deliver packets by preserving the destination IP. Ensure that server software running on your backend VMs is listening on the IP address of the load balancer's internal forwarding rule. If you configure [multiple internal forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal#multiple_forwarding_rule), ensure that your software listens to the internal IP address associated with each one. The destination IP address of a packet delivered to a backend VM by an internal passthrough Network Load Balancer is the internal IP address of the forwarding rule.

For instructional simplicity, these backend VMs run Debian GNU/Linux 12.

###  Console 

**Create backend VMs**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat steps 3 to 8 for each VM, using the following name and zone combinations.

     * Name: `vm-a1`, zone: `us-west1-a`
     * Name: `vm-a2`, zone: `us-west1-a`
     * Name: `vm-c1`, zone: `us-west1-c`
     * Name: `vm-c2`, zone: `us-west1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated in step 2.

  5. For **Region** , select **`us-west1`** , and choose a **Zone** as indicated in step 2.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Change** to change the image.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh` and `allow-health-check`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `lb-subnet`
        * **IP stack type** : **IPv4 (single-stack)**
        * **Primary internal IPv4 address** : **Ephemeral (automatic)**
        * **External IPv4 address** : **Ephemeral**
  9. Click **Management** , and then in the **Startup script** field, enter the following script. The script contents are identical for all four VMs.
         
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
         

  10. Click **Create**.




**Create instance groups**

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Repeat the following steps to create two unmanaged instance groups each with two VMs in them, using these combinations.

     * Instance group name: `ig-a`, zone: `us-west1-a`, VMs: `vm-a1` and `vm-a2`
     * Instance group name: `ig-c`, zone: `us-west1-c`, VMs: `vm-c1` and `vm-c2`
  3. Click **Create instance group**.

  4. Click **New unmanaged instance group**.

  5. Set **Name** as indicated in step 2.

  6. In the **Location** section, select **`us-west1`** for **Region** , and then choose a **Zone** as indicated in step 2.

  7. For **Network** , select **`lb-network`**.

  8. For **Subnetwork** , select **`lb-subnet`**.

  9. In the **VM instances** section, add the VMs as indicated in step 2.

  10. Click **Create**.




###  gcloud 

  1. Create the four VMs by running the following command four times, using these four combinations for `[VM-NAME]` and `[ZONE]`. The script contents are identical for all four VMs.

     * `VM-NAME`: `vm-a1`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-a2`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-c1`, `ZONE`: `us-west1-c`
     * `VM-NAME`: `vm-c2`, `ZONE`: `us-west1-c`
    
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
    

  2. Create the two unmanaged instance groups in each zone:
         
         gcloud compute instance-groups unmanaged create ig-a \
             --zone=us-west1-a
         gcloud compute instance-groups unmanaged create ig-c \
             --zone=us-west1-c
         

  3. Add the VMs to the appropriate instance groups:
         
         gcloud compute instance-groups unmanaged add-instances ig-a \
             --zone=us-west1-a \
             --instances=vm-a1,vm-a2
         gcloud compute instance-groups unmanaged add-instances ig-c \
             --zone=us-west1-c \
             --instances=vm-c1,vm-c2
         




###  API 

For the four VMs, use the following VM names and zones:

  * `VM-NAME`: `vm-a1`, `ZONE`: `us-west1-a`
  * `VM-NAME`: `vm-a2`, `ZONE`: `us-west1-a`
  * `VM-NAME`: `vm-c1`, `ZONE`: `us-west1-c`
  * `VM-NAME`: `vm-c2`, `ZONE`: `us-west1-c`



You can get the current `DEBIAN_IMAGE_NAME` by running the following `gcloud` command:
    
    
    gcloud compute images list \
     --filter="family=debian-12"
    

Create four backend VMs by making four `POST` requests to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
     "name": "VM-NAME",
     "tags": {
       "items": [
         "allow-health-check",
         "allow-ssh"
       ]
     },
     "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/[ZONE]/machineTypes/e2-standard-2",
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
         "deviceName": "VM-NAME",
         "initializeParams": {
           "sourceImage": "projects/debian-cloud/global/images/debian-image-name",
           "diskType": "projects/PROJECT_ID/zones/zone/diskTypes/pd-standard",
           "diskSizeGb": "10"
         }
       }
     ],
     "metadata": {
       "items": [
         {
           "key": "startup-script",
           "value": "#! /bin/bash\napt-get update\napt-get install apache2 -y\na2ensite default-ssl\na2enmod ssl\nfile_ports=\"/etc/apache2/ports.conf\"\nfile_http_site=\"/etc/apache2/sites-available/000-default.conf\"\nfile_https_site=\"/etc/apache2/sites-available/default-ssl.conf\"\nhttp_listen_prts=\"Listen 80\\nListen 8008\\nListen 8080\\nListen 8088\"\nhttp_vh_prts=\"*:80 *:8008 *:8080 *:8088\"\nhttps_listen_prts=\"Listen 443\\nListen 8443\"\nhttps_vh_prts=\"*:443 *:8443\"\nvm_hostname=\"$(curl -H \"Metadata-Flavor:Google\" \\\nhttp://metadata.google.internal/computeMetadata/v1/instance/name)\"\necho \"Page served from: $vm_hostname\" | \\\ntee /var/www/html/index.html\nprt_conf=\"$(cat \"$file_ports\")\"\nprt_conf_2=\"$(echo \"$prt_conf\" | sed \"s|Listen 80|${http_listen_prts}|\")\"\nprt_conf=\"$(echo \"$prt_conf_2\" | sed \"s|Listen 443|${https_listen_prts}|\")\"\necho \"$prt_conf\" | tee \"$file_ports\"\nhttp_site_conf=\"$(cat \"$file_http_site\")\"\nhttp_site_conf_2=\"$(echo \"$http_site_conf\" | sed \"s|*:80|${http_vh_prts}|\")\"\necho \"$http_site_conf_2\" | tee \"$file_http_site\"\nhttps_site_conf=\"$(cat \"$file_https_site\")\"\nhttps_site_conf_2=\"$(echo \"$https_site_conf\" | sed \"s|_default_:443|${https_vh_prts}|\")\"\necho \"$https_site_conf_2\" | tee \"$file_https_site\"\nsystemctl restart apache2"
         }
       ]
     },
     "scheduling": {
       "preemptible": false
     },
     "deletionProtection": false
    }
    

Create two instance groups by making a `POST` request to the [`instanceGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups
    
    {
     "name": "ig-a",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
     "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet"
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instanceGroups
    
    {
     "name": "ig-c",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
     "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet"
    }
    

Add instances to each instance group by making a `POST` request to the [`instanceGroups.addInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/addInstances).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a/addInstances
    
    {
     "instances": [
       {
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/vm-a1",
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/vm-a2"
       }
     ]
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instanceGroups/ig-c/addInstances
    
    {
     "instances": [
       {
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instances/vm-c1",
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instances/vm-c2"
       }
     ]
    }
    

### Configure load balancer components

These steps configure all of the [internal passthrough Network Load Balancer components](https://docs.cloud.google.com/load-balancing/docs/internal#components) starting with the health check and backend service, and then the frontend components:

  * **Health check**. In this example, you use an HTTP health check that checks for an HTTP `200 OK` status code. For more information, see the [Health check section](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking).

  * **Backend service**. Because you need to pass HTTP traffic through the internal load balancer, you need to use TCP, not UDP.

  * **Forwarding rule**. This example creates a single internal forwarding rule.

  * **Internal IP address**. In this example, you specify an internal IP address, `10.1.2.99`, when you create the forwarding rule.




###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

On the **Create internal passthrough Network Load Balancer** page, enter the following information:

  * **Load balancer name** : `be-ilb`
  * **Region** : **`us-west1`**
  * **Network** : **`lb-network`**



#### Configure the backends

  1. Click **Backend configuration**.
  2. In the **Health check** list, click **Create a health check** , and enter the following information.

     * **Name:** `hc-http-80`
     * **Protocol:** **HTTP**
     * **Port:** `80`
     * **Proxy protocol:** **None**
     * **Request:** `/`

Note that when you use the Google Cloud console to create your load balancer, the health check is global. If you want to create a regional health check, use `gcloud` or the API.

  3. Click **Create**.

  4. To handle only IPv4 traffic, in the **New Backend** section, for **IP stack type** , select the **IPv4 (single-stack)** option.

  5. In the **Instance group** list, select the `ig-c` instance group and click **Done**.

  6. Click **Add a backend** and repeat the step to add the `ig-a` instance group.

  7. Verify that there is a blue check mark next to **Backend configuration** before continuing.




#### Configure the frontend

  1. Click **Frontend configuration**.
  2. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter `fr-ilb`.
     2. For **Subnetwork** , select `lb-subnet`.
     3. In the **Internal IP purpose** section, in the **IP address** list, select **Create IP address** , enter the following information, and then click **Reserve**. 
        * **Name:** `ip-ilb`
        * **IP version:** **IPv4**
        * **Static IP address:** **Let me choose**
        * **Custom IP address:** `10.1.2.99`
     4. For **Ports** , select **Multiple** and then in **Port numbers** , enter `80`,`8008`,`8080`, and `8088`.
     5. Verify that there is a blue check mark next to **Frontend configuration** before continuing.



#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to the VMs on port 80.
         
         gcloud compute health-checks create http hc-http-80 \
             --region=us-west1 \
             --port=80
         

  2. Create the backend service for HTTP traffic:
         
         gcloud compute backend-services create be-ilb \
             --load-balancing-scheme=internal \
             --protocol=tcp \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  3. Add the two instance groups to the backend service:
         
         gcloud compute backend-services add-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         gcloud compute backend-services add-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-c \
             --instance-group-zone=us-west1-c
         

  4. Create a forwarding rule for the backend service. When you create the forwarding rule, specify `10.1.2.99` for the internal IP address in the subnet.
         
         gcloud compute forwarding-rules create fr-ilb \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --network=lb-network \
             --subnet=lb-subnet \
             --address=10.1.2.99 \
             --ip-protocol=TCP \
             --ports=80,8008,8080,8088 \
             --backend-service=be-ilb \
             --backend-service-region=us-west1
         




###  API 

Create the health check by making a `POST` request to the [`regionHealthChecks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/regionHealthChecks
    
    {
    "name": "hc-http-80",
    "type": "HTTP",
    "httpHealthCheck": {
      "port": 80
    }
    }
    

Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices
    
    {
    "name": "be-ilb",
    "backends": [
      {
        "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a",
        "balancingMode": "CONNECTION"
      },
      {
        "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instanceGroups/ig-c",
        "balancingMode": "CONNECTION"
      }
    ],
    "healthChecks": [
      "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/healthChecks/hc-http-80"
    ],
    "loadBalancingScheme": "INTERNAL",
    "connectionDraining": {
      "drainingTimeoutSec": 0
     }
    }
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "ports": [
      "80", "8008", "8080", "8088"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "networkTier": "PREMIUM"
    }
    

### Test your load balancer

These tests show how to validate your load balancer configuration and learn about its expected behavior.

#### Create a client VM

This example creates a client VM (`vm-client`) in the same region as the backend (server) VMs. The client is used to validate the load balancer's configuration and demonstrate expected behavior as described in the testing section.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `vm-client`.

  4. For **Region** , select **`us-west1`**.

  5. For **Zone** , select **`us-west1-a`**.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : **`lb-network`**
        * **Subnet** : **`lb-subnet`**
  8. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client \
        --zone=us-west1-a \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=lb-subnet
    

###  API 

Make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
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
    

#### Test connection from client VM

This test contacts the load balancer from a separate client VM; that is, not from a backend VM of the load balancer. The expected behavior is for traffic to be distributed among the four backend VMs [because no session affinity has been configured](https://docs.cloud.google.com/load-balancing/docs/internal#traffic_distribution).

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Make a web request to the load balancer using `curl` to contact its IP address. Repeat the request so you can see that responses come from different backend VMs. The name of the VM generating the response is displayed in the text in the HTML response, by virtue of the contents of `/var/www/html/index.html` on each backend VM. For example, expected responses look like `Page served from: vm-a1` and `Page served from: vm-a2`.
         
         curl http://10.1.2.99
         

The forwarding rule is configured to serve ports `80`, `8008`, `8080`, and `8088`. To send traffic to those other ports, append a colon (`:`) and the port number after the IP address, like this:
         
         curl http://10.1.2.99:8008
         

If you [add a service label](https://docs.cloud.google.com/load-balancing/docs/dns-names) to the internal forwarding rule, you can use [internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns) to contact the load balancer using its service name.
         
         curl http://web-test.fr-ilb.il4.us-west1.lb.PROJECT_ID.internal
         




#### Ping the load balancer's IP address

This test demonstrates an expected behavior: You cannot ping the IP address of the load balancer. This is because internal passthrough Network Load Balancers are implemented in virtual network programming — they are not separate devices.

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Attempt to ping the IP address of the load balancer. Notice that you don't get a response and that the `ping` command times out after 10 seconds in this example.
         
         timeout 10 ping 10.1.2.99
         




#### Send requests from load-balanced VMs

This test demonstrates that when a backend VM sends packets to the IP address of its load balancer's forwarding rule, those requests are routed back to itself. This is the case regardless of the backend VM's health check state.

Internal passthrough Network Load Balancers are implemented by using virtual network programming and VM configuration in the guest OS. On Linux VMs, the [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) creates a route for the load balancer's IP address in the operating system's local routing table.

Because this local route is within the VM itself (not a route in the VPC network), packets sent to the load balancer's IP address are not processed by the VPC network. Instead, packets sent to the load balancer's IP address remain within the operating system of the VM.

  1. Connect to a backend VM, such as `vm-a1`:
         
         gcloud compute ssh vm-a1 --zone=us-west1-a
         

**Important:** You won't be able to connect to a backend VM in this way if you have removed its external IP address. For connection options if your backend VMs don't have external IP addresses, see [Choose a connection option for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip).
  2. Make a web request to the load balancer (by IP address or service name) using `curl`. The response comes from the same backend VM that makes the request. Repeated requests are answered in the same way. The expected response when testing from `vm-a1` is always `Page served from: vm-a1`.
         
         curl http://10.1.2.99
         

  3. Inspect the local routing table, looking for a destination that matches the IP address of the load balancer itself, `10.1.2.99`. This route is a necessary part of an internal passthrough Network Load Balancer, but it also demonstrates why a request from a VM behind the load balancer is always responded to by the same VM.
         
         ip route show table local | grep 10.1.2.99
         




When a backend VM for an internal passthrough Network Load Balancer sends packets to the load balancer's forwarding rule IP address, the packets are _always_ routed back to the VM that makes the request. This is because an internal passthrough Network Load Balancer is a pass-through load balancer and is implemented by creating a local route for the load balancer's IP address within the VM's guest OS, as indicated in this section. If you have a use case where load-balanced backends need to send TCP traffic to the load balancer's IP address, and you need the traffic to be distributed as if it originated from a non-load-balanced backend, consider using a [regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy) instead.

For more information, see [Internal passthrough Network Load Balancers as next hops](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview).

## Set up load balancer with dual-stack subnets and backends

This document shows you how to configure and test an internal passthrough Network Load Balancer that supports both IPv4 and IPv6 traffic. The steps in this section describe how to configure the following:

  1. The example on this page uses a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network-dual-stack`. IPv6 traffic [requires a custom mode subnet](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications).
  2. A _dual-stack_ subnet (`stack-type` set to `IPV4_IPV6`), which is required for IPv6 traffic. When you create a dual stack subnet on a custom mode VPC network, you choose an [IPv6 access type](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) for the subnet. For this example, we set the subnet's `ipv6-access-type` parameter to `INTERNAL`. This means new VMs on this subnet can be assigned both internal IPv4 addresses and internal IPv6 addresses. For instructions, see VPC documentation about [Adding a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).
  3. Firewall rules that allow incoming connections to backend VMs.
  4. The backend instance group, which is located in the following region and subnet for this example: 
     * Region: `us-west1`
     * Subnet: `lb-subnet`, with primary IPv4 address range `10.1.2.0/24`. Although you choose which IPv4 address range to configure on the subnet, the IPv6 address range is assigned automatically. Google provides a fixed size (`/64`) IPv6 CIDR block.
  5. Four backend [dual-stack](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6) VMs: two VMs in an unmanaged instance group in zone `us-west1-a` and two VMs in an unmanaged instance group in zone `us-west1-c`. To demonstrate [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access), this example creates a second test client VM in a different region and subnet: 
     * Region: `europe-west1`
     * Subnet: `europe-subnet`, with primary IP address range `10.3.4.0/24`
  6. One client VM to test connections.
  7. The following internal passthrough Network Load Balancer components: 
     * A health check for the backend service.
     * An internal backend service in the `us-west1` region to manage connection distribution to the two zonal instance groups.
     * Two internal forwarding rules for the frontend of the load balancer.



The following diagram shows the architecture for this example:

[ ![A dual-stack VPC network with a backend service to manage connection
    distribution to two zonal instance groups.](https://docs.cloud.google.com/static/load-balancing/images/ilb-example-ipv6.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-example-ipv6.svg) Internal passthrough Network Load Balancer example configuration (click to enlarge).**Note:** For simplicity, this example uses unmanaged instance groups. In production, consider using a managed instance group, as illustrated in Managed instance groups.

### Configure a network, region, and subnet

The example internal passthrough Network Load Balancer described on this page is created in a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network-dual-stack`.

To configure subnets with internal IPv6 ranges, enable a VPC network ULA internal IPv6 range. Internal IPv6 subnet ranges are allocated from this range.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click add_box**Create VPC network**.

  3. For **Name** , enter `lb-network-dual-stack`.

  4. If you want to configure internal IPv6 address ranges on subnets in this network, complete these steps:

     1. For **Private IPv6 address settings** , select **Configure a ULA internal IPv6 range for this VPC Network**.
     2. For **Allocate internal IPv6 range** , select **Automatically** or **Manually**. If you select **Manually** , enter a `/48` range from within the `fd20::/20` range. If the range is in use, you are prompted to provide a different range.
  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : `lb-subnet`
     * **Region** : `us-west1`
     * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
     * **IPv4 range** : `10.1.2.0/24`.
     * **IPv6 access type** : **Internal**
  7. Click **Done**.

  8. Click **Add subnet** and enter the following information:

     * **Name** : `europe-subnet`
     * **Region** : `europe-west1`
     * **IP stack type** : **IPv4 (single-stack)**
     * **IP address range** : `10.3.4.0/24`
  9. Click **Done**.

  10. Click **Create**.




###  gcloud 

  1. To create a new custom mode VPC network, run the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).

To configure _internal_ IPv6 ranges on any subnets in this network, use the `--enable-ula-internal-ipv6` flag. This option assigns a `/48` ULA prefix from within the `fd20::/20` range used by Google Cloud for internal IPv6 subnet ranges. If you want to select the `/48` IPv6 range that is assigned, use the `--internal-ipv6-range` flag to specify a range.
         
         gcloud compute networks create lb-network-dual-stack \
            --subnet-mode=custom \
            --enable-ula-internal-ipv6 \
            --internal-ipv6-range=ULA_IPV6_RANGE \
            --bgp-routing-mode=regional
         

Replace `ULA_IPV6_RANGE` with a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't use the `--internal-ipv6-range` flag, Google selects a `/48` prefix for the network, such as `fd20:bc7:9a1c::/48`.

  2. Within the `NETWORK` network, create a subnet for backends in the `us-west1` region and another subnet for testing global access in the `europe-west1` region.

To create the subnets, run the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create lb-subnet \
            --network=lb-network-dual-stack \
            --range=10.1.2.0/24 \
            --region=us-west1 \
            --stack-type=IPV4_IPV6 \
            --ipv6-access-type=INTERNAL
         
         
         gcloud compute networks subnets create europe-subnet \
            --network=lb-network-dual-stack \
            --range=10.3.4.0/24 \
            --region=europe-west1 \
            --stack-type=IPV4_IPV6 \
            --ipv6-access-type=INTERNAL
         




###  API 

Create a new custom mode VPC network.

To configure _internal_ IPv6 ranges on any subnets in this network, set `enableUlaInternalIpv6` to true. This option assigns a `/48` range from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select which `/48` IPv6 range that is assigned, also use the `internalIpv6Range` field to specify a range.
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
     {
       "autoCreateSubnetworks": false,
       "name": "lb-network-dual-stack",
       "mtu": MTU,
       "enableUlaInternalIpv6": true,
       "internalIpv6Range": "ULA_IPV6_RANGE",
       "routingConfig": {
       "routingMode": "DYNAMIC_ROUTING_MODE"
      }
     }
     

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `MTU`: the maximum transmission unit of the network. MTU can either be `1460` (default) or `1500`. Review the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu) before setting the MTU to `1500`.
  * `ULA_IPV6_RANGE`: a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix for the network.
  * `DYNAMIC_ROUTING_MODE`: either `global` or `regional` to control the route advertisement behavior of Cloud Routers in the network. For more information, refer to [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).

For more information, refer to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert).




Make two `POST` requests to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
     {
       "ipCidrRange": "10.1.2.0/24",
       "network": "lb-network-dual-stack",
       "name": "lb-subnet"
       "stackType": IPV4_IPV6,
       "ipv6AccessType": Internal
     }
     
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
     {
       "ipCidrRange": "10.3.4.0/24",
       "network": "lb-network-dual-stack",
       "name": "europe-subnet"
       "stackType": IPV4_IPV6,
       "ipv6AccessType": Internal
     }
     

### Configure firewall rules

This example uses the following firewall rules:

  * `fw-allow-lb-access`: An ingress rule, applicable to all targets in the VPC network, that allows traffic from sources in the `10.1.2.0/24` and `10.3.4.0/24` ranges. This rule allows incoming traffic from any client located in either of the two subnets. Later, you can configure and test global access.

  * `fw-allow-lb-access-ipv6`: An ingress rule, applicable to all targets in the VPC network, that allows traffic from sources in the IPv6 range configured in the subnet. This rule allows incoming IPv6 traffic from any client located in either of the two subnets. Later, you can configure and test global access.

  * `fw-allow-ssh`: An ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port 22 from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it should apply.

  * `fw-allow-health-check`: An ingress rule, applicable to the instances being load balanced, that allows traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check` to identify the instances to which it should apply.

  * `fw-allow-health-check-ipv6`: An ingress rule, applicable to the instances being load balanced, that allows traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check-ipv6` to identify the instances to which it should apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

**Note:** You must create a firewall rule to allow health checks from the IP ranges of Google Cloud probe systems. See [probe IP ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) for more information.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To create the rule to allow subnet traffic, click **Create firewall rule** and enter the following information:

     * **Name** : `fw-allow-lb-access`
     * **Network** : `lb-network-dual-stack`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **All instances in the network**
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `10.1.2.0/24` and `10.3.4.0/24`
     * **Protocols and ports** : **Allow all**
  3. Click **Create**.

  4. To allow IPv6 subnet traffic, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-lb-access-ipv6`
     * **Network** : `lb-network-dual-stack`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **All instances in the network**
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : IPV6_ADDRESS assigned in the `lb-subnet`
     * **Protocols and ports** : **Allow all**
  5. Click **Create**.

  6. To allow incoming SSH connections, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network-dual-stack`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : Select **Specified protocols and ports** , select the **TCP** checkbox, and then enter `22` in **Ports**.
  7. Click **Create**.

  8. To allow Google Cloud IPv6 health checks, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-health-check-ipv6`
     * **Network** : `lb-network-dual-stack`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check-ipv6`
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `2600:2d00:1:b029::/64`
     * **Protocols and ports** : **Allow all**
  9. Click **Create**.

  10. To allow Google Cloud health checks, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-health-check`
     * **Network** : `lb-network-dual-stack`
     * **Priority** : `1000`
     * **Direction of traffic** : **ingress**
     * **Action on match** : **allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `35.191.0.0/16`
     * **Protocols and ports** : **Allow all**
  11. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-lb-access` firewall rule to allow communication with the subnet:
         
         gcloud compute firewall-rules create fw-allow-lb-access \
             --network=lb-network-dual-stack \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.1.2.0/24,10.3.4.0/24 \
             --rules=all
         

  2. Create the `fw-allow-lb-access-ipv6` firewall rule to allow communication with the subnet:
         
         gcloud compute firewall-rules create fw-allow-lb-access-ipv6 \
             --network=lb-network-dual-stack \
             --action=allow \
             --direction=ingress \
             --source-ranges=IPV6_ADDRESS \
             --rules=all
         

Replace `IPV6_ADDRESS` with the IPv6 address assigned in the `lb-subnet`.

  3. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network-dual-stack \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  4. Create the `fw-allow-health-check-ipv6` rule to allow Google Cloud IPv6 health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check-ipv6 \
             --network=lb-network-dual-stack \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check-ipv6 \
             --source-ranges=2600:2d00:1:b029::/64 \
             --rules=tcp,udp
         

  5. Create the `fw-allow-health-check` rule to allow Google Cloud IPv4 health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check \
             --network=lb-network-dual-stack \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check \
             --source-ranges=35.191.0.0/16 \
             --rules=tcp,udp,icmp
         




###  API 

  1. Create the `fw-allow-lb-access` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         
         {
         "name": "fw-allow-lb-access",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
         "priority": 1000,
         "sourceRanges": [
           "10.1.2.0/24", "10.3.4.0/24"
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
         

  2. Create the `fw-allow-lb-access-ipv6` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         
         {
          "name": "fw-allow-lb-access-ipv6",
          "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
          "priority": 1000,
          "sourceRanges": [
            "IPV6_ADDRESS"
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
         

Replace `IPV6_ADDRESS` with the IPv6 address assigned in the `lb-subnet`.

  3. Create the `fw-allow-ssh` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         
         {
         "name": "fw-allow-ssh",
              "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
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
         

  4. Create the `fw-allow-health-check-ipv6` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         
         {
         "name": "fw-allow-health-check-ipv6",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
         "priority": 1000,
         "sourceRanges": [HEALTH_CHECK_RANGES],
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
         

Replace the following:

     * PROJECT_ID: the project ID

     * HEALTH_CHECK_RANGES: the comma-separated list of [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges), formatted as quoted strings (for example, "2001:db8::/32")

  5. Create the `fw-allow-health-check` firewall rule by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
         
         {
         "name": "fw-allow-health-check",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
         "priority": 1000,
         "sourceRanges": [HEALTH_CHECK_RANGES],
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
         

Replace the following:

     * PROJECT_ID: the project ID

     * HEALTH_CHECK_RANGES: the comma-separated list of [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges), formatted as quoted strings (for example, "192.0.2.0/24", "198.51.100.0/24")




### Create backend VMs and instance groups

This example uses two _unmanaged_ instance groups each having two backend (server) VMs. To demonstrate the regional nature of internal passthrough Network Load Balancers, the two instance groups are placed in separate zones, `us-west1-a` and `us-west1-c`.

  * Instance group `ig-a` contains these two VMs: 
    * `vm-a1`
    * `vm-a2`
  * Instance group `ig-c` contains these two VMs: 
    * `vm-c1`
    * `vm-c2`



Traffic to all four of the backend VMs is load balanced.

To support this example and the additional configuration options, each of the four VMs runs an Apache web server that listens on the following TCP ports: `80`,`8008`, `8080`, `8088`, `443`, and `8443`.

Each VM is assigned an internal IP address in the `lb-subnet` and an ephemeral external (public) IP address. You can remove the external IP addresses later.

External IP address for the backend VMs are not required; however, they are useful for this example because they permit the backend VMs to download Apache from the internet, and they can [connect using SSH](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcetools).

By default, Apache is configured to bind to any IP address. Internal passthrough Network Load Balancers deliver packets by preserving the destination IP.

Ensure that server software running on your backend VMs is listening on the IP address of the load balancer's internal forwarding rule. If you configure [multiple internal forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal#multiple_forwarding_rule), ensure that your software listens to the internal IP address associated with each one. The destination IP address of a packet delivered to a backend VM by an internal passthrough Network Load Balancer is the internal IP address of the forwarding rule.

If you're using managed instance groups, ensure that the subnetwork stack type matches the stack type of instance templates used by the managed instance groups. The subnetwork must be dual-stack if the managed instance group is using a dual-stack instance template.

For instructional simplicity, these backend VMs run Debian GNU/Linux 12.

###  Console 

#### Create backend VMs

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat steps 3 to 8 for each VM, using the following name and zone combinations.

     * Name: `vm-a1`, zone: `us-west1-a`
     * Name: `vm-a2`, zone: `us-west1-a`
     * Name: `vm-c1`, zone: `us-west1-c`
     * Name: `vm-c2`, zone: `us-west1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated in step 2.

  5. For **Region** , select `us-west1`, and choose a **Zone** as indicated in step 2.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Change** to change the image.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh` and `allow-health-check-ipv6`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network-dual-stack`
        * **Subnet** : `lb-subnet`
        * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
        * **Primary internal IPv4 address** : **Ephemeral (automatic)**
        * **External IPv4 address** : **Ephemeral**
     3. Click **Management** , and then in the **Startup script** field, enter the following script. The script contents are identical for all four VMs.
            
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
            

  9. Click **Create**.




#### Create instance groups

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Repeat the following steps to create two unmanaged instance groups each with two VMs in them, using these combinations.

     * Instance group name: `ig-a`, zone: `us-west1-a`, VMs: `vm-a1` and `vm-a2`
     * Instance group name: `ig-c`, zone: `us-west1-c`, VMs: `vm-c1` and `vm-c2`
  3. Click **Create instance group**.

  4. Click **New unmanaged instance group**.

  5. Set **Name** as indicated in step 2.

  6. In the **Location** section, select `us-west1` for the **Region** , and then choose a **Zone** as indicated in step 2.

  7. For **Network** , select `lb-network-dual-stack`.

  8. For **Subnetwork** , select `lb-subnet`.

  9. In the **VM instances** section, add the VMs as indicated in step 2.

  10. Click **Create**.




###  gcloud 

  1. To create the four VMs, run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) four times, using these four combinations for `[VM-NAME]` and `[ZONE]`. The script contents are identical for all four VMs.

     * `VM-NAME`: `vm-a1`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-a2`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-c1`, `ZONE`: `us-west1-c`
     * `VM-NAME`: `vm-c2`, `ZONE`: `us-west1-c`
           
           gcloud compute instances create VM-NAME \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh,allow-health-check-ipv6 \
             --subnet=lb-subnet \
             --stack-type=IPV4_IPV6 \
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
           

  2. Create the two unmanaged instance groups in each zone:
         
         gcloud compute instance-groups unmanaged create ig-a \
             --zone=us-west1-a
         gcloud compute instance-groups unmanaged create ig-c \
             --zone=us-west1-c
         

  3. Add the VMs to the appropriate instance groups:
         
         gcloud compute instance-groups unmanaged add-instances ig-a \
             --zone=us-west1-a \
             --instances=vm-a1,vm-a2
         gcloud compute instance-groups unmanaged add-instances ig-c \
             --zone=us-west1-c \
             --instances=vm-c1,vm-c2
         




###  api 

For the four VMs, use the following VM names and zones:

  * `VM-NAME`: `vm-a1`, `ZONE`: `us-west1-a`
  * `VM-NAME`: `vm-a2`, `ZONE`: `us-west1-a`
  * `VM-NAME`: `vm-c1`, `ZONE`: `us-west1-c`
  * `VM-NAME`: `vm-c2`, `ZONE`: `us-west1-c`



You can get the current `DEBIAN_IMAGE_NAME` by running the following `gcloud` command:
    
    
    gcloud compute images list \
     --filter="family=debian-12"
    

Create four backend VMs by making four `POST` requests to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
     "name": "VM-NAME",
     "tags": {
       "items": [
         "allow-health-check-ipv6",
         "allow-ssh"
       ]
     },
     "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/[ZONE]/machineTypes/e2-standard-2",
     "canIpForward": false,
     "networkInterfaces": [
       {
         "stackType": "IPV4_IPV6",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
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
         "deviceName": "VM-NAME",
         "initializeParams": {
           "sourceImage": "projects/debian-cloud/global/images/debian-image-name",
           "diskType": "projects/PROJECT_ID/zones/zone/diskTypes/pd-standard",
           "diskSizeGb": "10"
         }
       }
     ],
     "metadata": {
       "items": [
         {
           "key": "startup-script",
           "value": "#! /bin/bash\napt-get update\napt-get install apache2 -y\na2ensite default-ssl\na2enmod ssl\nfile_ports=\"/etc/apache2/ports.conf\"\nfile_http_site=\"/etc/apache2/sites-available/000-default.conf\"\nfile_https_site=\"/etc/apache2/sites-available/default-ssl.conf\"\nhttp_listen_prts=\"Listen 80\\nListen 8008\\nListen 8080\\nListen 8088\"\nhttp_vh_prts=\"*:80 *:8008 *:8080 *:8088\"\nhttps_listen_prts=\"Listen 443\\nListen 8443\"\nhttps_vh_prts=\"*:443 *:8443\"\nvm_hostname=\"$(curl -H \"Metadata-Flavor:Google\" \\\nhttp://169.254.169.254/computeMetadata/v1/instance/name)\"\necho \"Page served from: $vm_hostname\" | \\\ntee /var/www/html/index.html\nprt_conf=\"$(cat \"$file_ports\")\"\nprt_conf_2=\"$(echo \"$prt_conf\" | sed \"s|Listen 80|${http_listen_prts}|\")\"\nprt_conf=\"$(echo \"$prt_conf_2\" | sed \"s|Listen 443|${https_listen_prts}|\")\"\necho \"$prt_conf\" | tee \"$file_ports\"\nhttp_site_conf=\"$(cat \"$file_http_site\")\"\nhttp_site_conf_2=\"$(echo \"$http_site_conf\" | sed \"s|*:80|${http_vh_prts}|\")\"\necho \"$http_site_conf_2\" | tee \"$file_http_site\"\nhttps_site_conf=\"$(cat \"$file_https_site\")\"\nhttps_site_conf_2=\"$(echo \"$https_site_conf\" | sed \"s|_default_:443|${https_vh_prts}|\")\"\necho \"$https_site_conf_2\" | tee \"$file_https_site\"\nsystemctl restart apache2"
         }
       ]
     },
     "scheduling": {
       "preemptible": false
     },
     "deletionProtection": false
    }
    

Create two instance groups by making a `POST` request to the [`instanceGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups
    
    {
     "name": "ig-a",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
     "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet"
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instanceGroups
    
    {
     "name": "ig-c",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
     "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet"
    }
    

Add instances to each instance group by making a `POST` request to the [`instanceGroups.addInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroups/addInstances).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a/addInstances
    
    {
     "instances": [
       {
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/vm-a1",
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/vm-a2"
       }
     ]
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instanceGroups/ig-c/addInstances
    
    {
     "instances": [
       {
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instances/vm-c1",
         "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instances/vm-c2"
       }
     ]
    }
    

### Configure load balancer components

These steps configure all of the [internal passthrough Network Load Balancer components](https://docs.cloud.google.com/load-balancing/docs/internal#components) starting with the health check and backend service, and then the frontend components:

  * **Health check.** In this example, you use an HTTP health check that checks for an HTTP `200 OK` status code. For more information, see [health checks section of the internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking).

  * **Backend service.** Because you need to pass HTTP traffic through the internal load balancer, you need to use TCP, not UDP.

  * **Forwarding rule.** This example creates two internal forwarding rules for IPv4 and IPv6 traffic.

  * **Internal IP address.** In this example, you specify an internal IP address, `10.1.2.99`, when you create the IPv4 forwarding rule. For more information, see [Internal IP address](https://docs.cloud.google.com/load-balancing/docs/internal#load_balancing_ip_address). Although you choose which IPv4 address is configured, the IPv6 address is assigned automatically.




###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

On the **Create internal passthrough Network Load Balancer** page, enter the following information:

  * **Load balancer name** : `be-ilb`
  * **Region** : **`us-west1`**
  * **Network** : **`lb-network-dual-stack`**



#### Backend configuration

  1. Click **Backend configuration**.
  2. In the **Health check** list, click **Create a health check** , and enter the following information: 
     * **Name** : `hc-http-80`
     * **Scope** : **Regional**
     * **Protocol** : **HTTP**
     * **Port** : `80`
     * **Proxy protocol** : `NONE`
     * **Request** : `/`
  3. Click **Create**.
  4. In the **New Backend** section, for **IP stack type** , select the **IPv4 and IPv6 (dual-stack)** option.
  5. In **Instance group** , select the `ig-a` instance group and click **Done**.
  6. Click **Add a backend** and repeat the step to add the `ig-c` instance group.
  7. Verify that a blue check mark appears next to **Backend configuration**.



#### Frontend configuration

  1. Click **Frontend configuration**. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter `fr-ilb-ipv6`.
     2. To handle IPv6 traffic, do the following: 
        1. For **IP version** , select **IPv6**.
        2. For **Subnetwork** , select`lb-subnet`. The IPv6 address range in the forwarding rule is always ephemeral.
        3. For **Ports** , select **Multiple** , and then in the **Port number** field, enter `80`,`8008`,`8080`,`8088`.
        4. Click **Done**.
     3. To handle IPv4 traffic, do the following: 
        1. Click **Add frontend IP and port**.
        2. For **Name** , enter `fr-ilb`.
        3. For **Subnetwork** , select `lb-subnet`.
        4. In the **Internal IP purpose** section, from the **IP address** list, select **Create IP address** , enter the following information, and then click **Reserve**. 
           * **Name:** `ip-ilb`
           * **IP version:** **IPv4**
           * **Static IP address:** **Let me choose**
           * **Custom IP address:** `10.1.2.99`
        5. For **Ports** , select **Multiple** , and then in **Port numbers** , enter `80`,`8008`,`8080`, and `8088`.
        6. Click **Done**.
        7. Verify that there is a blue check mark next to **Frontend configuration** before continuing.



#### Review the configuration

  1. Click **Review and finalize**. Check all your settings.
  2. If the settings are correct, click **Create**. It takes a few minutes for the internal passthrough Network Load Balancer to be created.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to the VMs on port 80.
         
         gcloud compute health-checks create http hc-http-80 \
             --region=us-west1 \
             --port=80
         

  2. Create the backend service for HTTP traffic:
         
         gcloud compute backend-services create be-ilb \
             --load-balancing-scheme=internal \
             --protocol=tcp \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  3. Add the two instance groups to the backend service:
         
         gcloud compute backend-services add-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         gcloud compute backend-services add-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-c \
             --instance-group-zone=us-west1-c
         

  4. Create two forwarding rules for the backend service. When you create the IPv4 forwarding rule, specify `10.1.2.99` for the internal IP address in the subnet for IPv4 addresses.
         
         gcloud compute forwarding-rules create fr-ilb \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --subnet=lb-subnet \
             --address=10.1.2.99 \
             --ip-protocol=TCP \
             --ports=80,8008,8080,8088 \
             --backend-service=be-ilb \
             --backend-service-region=us-west1
         
         
         gcloud compute forwarding-rules create fr-ilb-ipv6 \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --subnet=lb-subnet \
             --ip-protocol=TCP \
             --ports=80,8008,8080,8088 \
             --backend-service=be-ilb \
             --backend-service-region=us-west1 \
             --ip-version=IPV6
         




###  api 

Create the health check by making a `POST` request to the [`regionHealthChecks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/regionHealthChecks
    
    {
    "name": "hc-http-80",
    "type": "HTTP",
    "httpHealthCheck": {
      "port": 80
    }
    }
    

Create the regional backend service by making a `POST` request to the [`regionBackendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices
    
    {
    "name": "be-ilb",
    "backends": [
      {
        "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instanceGroups/ig-a",
        "balancingMode": "CONNECTION"
      },
      {
        "group": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-c/instanceGroups/ig-c",
        "balancingMode": "CONNECTION"
      }
    ],
    "healthChecks": [
      "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/healthChecks/hc-http-80"
    ],
    "loadBalancingScheme": "INTERNAL",
    "connectionDraining": {
      "drainingTimeoutSec": 0
     }
    }
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb-ipv6",
    "IPProtocol": "TCP",
    "ports": [
      "80", "8008", "8080", "8088"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "ipVersion": "IPV6",
    "networkTier": "PREMIUM"
    }
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "ports": [
      "80", "8008", "8080", "8088"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "networkTier": "PREMIUM"
    }
    

### Test your load balancer

To test the load balancer, create a client VM in the same region as the load balancer, and then send traffic from the client to the load balancer.

#### Create a client VM

This example creates a client VM (`vm-client`) in the same region as the backend (server) VMs. The client is used to validate the load balancer's configuration and demonstrate expected behavior as described in the testing section.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `vm-client`.

  4. For **Region** , select **`us-west1`**.

  5. For **Zone** , select **`us-west1-a`**.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : **`lb-network-dual-stack`**
        * **Subnet** : **`lb-subnet`**
        * **IP stack type** : **IPv4 and IPv6 (dual-stack)**
        * **Primary internal IP** : **Ephemeral (automatic)**
        * **External IP** : **Ephemeral**
     3. Click **Done**.
  8. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client \
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
         "stackType": "IPV4_IPV6",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network-dual-stack",
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
    

#### Test the connection

This test contacts the load balancer from a separate client VM; that is, not from a backend VM of the load balancer. The expected behavior is for traffic to be distributed among the four backend VMs.

  1. Connect to the client VM instance.
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Describe the IPv6 forwarding rule `fr-ilb-ipv6`. Note the `IPV6_ADDRESS` in the description.
         
         gcloud compute forwarding-rules describe fr-ilb-ipv6 --region=us-west1
         

  3. Describe the IPv4 forwarding rule `fr-ilb`.
         
         gcloud compute forwarding-rules describe fr-ilb --region=us-west1
         

  4. From clients with IPv6 connectivity, run the following command:
         
         curl -m 10 -s http://IPV6_ADDRESS:80
         

For example, if the assigned IPv6 address is `[fd20:1db0:b882:802:0:46:0:0/96]:80`, the command should look like:
         
         curl -m 10 -s http://[fd20:1db0:b882:802:0:46:0:0]:80
         

  5. From clients with IPv4 connectivity, run the following command:
         
         curl -m 10 -s http://10.1.2.99:80
         

Replace the placeholders with valid values:

     * `IPV6_ADDRESS` is the ephemeral IPv6 address in the `fr-ilb-ipv6` forwarding rule.



## Set up load balancer with IPv6-only subnets and backends

This document shows you how to configure and test an internal passthrough Network Load Balancer that supports only IPv6 traffic. The steps in this section describe how to configure the following:

  1. A [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network-ipv6-only`. IPv6 traffic [requires a custom mode subnet](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications).
  2. An internal _IPv6-only_ subnet called `lb-subnet-ipv6-only` (`stack-type` set to `IPV6_ONLY`), which is required for IPv6-only traffic.
  3. Firewall rules that allow incoming connections to backend VMs.
  4. The backend instance group, which is located in the following region and subnet for this example: 
     * Region: `us-west1`
     * Subnet: `lb-subnet-ipv6-only`. The IPv6 address range for the subnet is assigned automatically. Google provides a fixed size (`/64`) IPv6 CIDR block.
  5. Four backend [IPv6-only](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#create-vm-ipv6) VMs—two VMs in an unmanaged instance group in zone `us-west1-a` and two VMs in an unmanaged instance group in zone `us-west1-c`.
  6. An IPv6 TCP server on the backend VMs. The server listens for incoming connections on the specified VIP of the load balancer's forwarding rule and the specified network interface. The server accepts incoming client connections, sends a response, and then closes the connection.
  7. One client VM to test connections.
  8. The following internal passthrough Network Load Balancer components: 
     * A health check for the backend service
     * An internal backend service in the `us-west1` region to manage connection distribution to the two zonal instance groups
     * An IPv6 forwarding rule



You can also set up an internal passthrough Network Load Balancer with internal IPv6-only backends by using a VM instance that serves as a NAT gateway. To learn more about this configuration, see [Set up an internal passthrough Network Load Balancer with internal IPv6-only backends](https://docs.cloud.google.com/load-balancing/docs/internal/setup-load-balancer-ipv6-backends-subnets-nat-table).

### Configure a network, region, and subnet

The example internal passthrough Network Load Balancer described on this page is created in a [custom mode VPC network](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) named `lb-network-ipv6-only`.

To configure subnets with internal IPv6 ranges, enable a VPC network ULA internal IPv6 range. Internal IPv6 subnet ranges are allocated from this range.

Later, in the Install an IPv6 TCP server on the backend VMs using a startup Bash script section of this document, the internal IPv6 subnet range is used to create a routing rule to route traffic from the VPC subnet through the specified gateway and network interface.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `lb-network-ipv6-only`.

  4. If you want to configure internal IPv6 address ranges on subnets in this network, complete these steps:

     1. For **Private IPv6 address settings** , select **Configure a ULA internal IPv6 range for this VPC Network**.
     2. For **Allocate internal IPv6 range** , select **Automatically** or **Manually**. If you select **Manually** , enter a `/48` range from within the `fd20::/20` range. If the range is already in use, you are prompted to provide a different range.
  5. For **Subnet creation mode** , select **Custom**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     * **Name** : `lb-subnet-ipv6-only`
     * **Region** : `us-west1`
     * **IP stack type** : **IPv6 (single-stack)**
     * **IPv6 access type** : **Internal**
  7. Click **Done**.

  8. Click **Create**.




###  gcloud 

  1. To create a new custom mode VPC network, run the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).

To configure [internal IPv6 ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#enable-internal-ipv6-network) on any subnets in this network, use the `--enable-ula-internal-ipv6` flag.
         
         gcloud compute networks create lb-network-ipv6-only \
           --subnet-mode=custom \
           --enable-ula-internal-ipv6 \
           --bgp-routing-mode=regional
         

  2. Configure a subnet with the `ipv6-access-type` set to `INTERNAL`. This indicates that the VMs in this subnet can only have internal IPv6 addresses.To create the subnet, run the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create lb-subnet-ipv6-only \
           --network=lb-network-ipv6-only \
           --region=us-west1 \
           --stack-type=IPV6_ONLY \
           --ipv6-access-type=INTERNAL
         




### Configure firewall rules

This example uses the following firewall rules:

  * `fw-allow-lb-access-ipv6-only`: an ingress rule, applicable to all targets in the VPC network, that allows traffic from all IPv6 sources.

  * `fw-allow-ssh`: an ingress rule, applicable to the instances being load balanced, that allows incoming SSH connectivity on TCP port `22` from any address. You can choose a more restrictive source IP range for this rule; for example, you can specify just the IP ranges of the system from which you initiate SSH sessions. This example uses the target tag `allow-ssh` to identify the VMs to which it must apply.

  * `fw-allow-health-check-ipv6-only`: an ingress rule, applicable to the instances being load balanced, that allows traffic from the [Google Cloud health check probe ranges](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges). This example uses the target tag `allow-health-check-ipv6` to identify the instances to which it must apply.




Without these firewall rules, the [default deny ingress](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) rule blocks incoming traffic to the backend instances.

**Note:** You must create a firewall rule to allow health checks from the IP ranges of Google Cloud probe systems. For more information, see [Probe IP ranges and firewall rules](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges).

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow IPv6 subnet traffic, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-lb-access-ipv6-only`
     * **Network** : `lb-network-ipv6-only`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **All instances in the network**
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `::/0`
     * **Protocols and ports** : **Allow all**
  3. Click **Create**.

  4. To allow incoming SSH connections, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-ssh`
     * **Network** : `lb-network-ipv6-only`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-ssh`
     * **Source filter** : **IPv4 ranges**
     * **Source IPv4 ranges** : `0.0.0.0/0`
     * **Protocols and ports** : Select **Specified protocols and ports** , select the **TCP** checkbox, and then enter `22` in **Ports**.
  5. Click **Create**.

  6. To allow Google Cloud IPv6 health checks, click **Create firewall rule** again and enter the following information:

     * **Name** : `fw-allow-health-check-ipv6-only`
     * **Network** : `lb-network-ipv6-only`
     * **Priority** : `1000`
     * **Direction of traffic** : **Ingress**
     * **Action on match** : **Allow**
     * **Targets** : **Specified target tags**
     * **Target tags** : `allow-health-check-ipv6`
     * **Source filter** : **IPv6 ranges**
     * **Source IPv6 ranges** : `2600:2d00:1:b029::/64`
     * **Protocols and ports** : **Allow all**
  7. Click **Create**.




###  gcloud 

  1. Create the `fw-allow-lb-access-ipv6-only` firewall rule to allow IPv6 traffic to all VM instances in the VPC network.
         
         gcloud compute firewall-rules create fw-allow-lb-access-ipv6-only \
             --network=lb-network-ipv6-only \
             --action=allow \
             --direction=ingress \
             --source-ranges=::/0 \
             --rules=all
         

  2. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`. When you omit `source-ranges`, Google Cloud [interprets the rule to mean any source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule).
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=lb-network-ipv6-only \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-ssh \
             --rules=tcp:22
         

  3. Create the `fw-allow-health-check-ipv6` rule to allow Google Cloud IPv6 health checks.
         
         gcloud compute firewall-rules create fw-allow-health-check-ipv6-only \
             --network=lb-network-ipv6-only \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-health-check-ipv6 \
             --source-ranges=2600:2d00:1:b029::/64 \
             --rules=tcp,udp
         




### Create backend VMs and instance groups

This example uses two _unmanaged_ instance groups, each having two backend VMs. To demonstrate the regional nature of internal passthrough Network Load Balancers, the two instance groups are placed in separate zones, `us-west1-a` and `us-west1-c`.

  * Instance group `ig-a` contains these two VMs: 
    * `vm-a1`
    * `vm-a2`
  * Instance group `ig-c` contains these two VMs: 
    * `vm-c1`
    * `vm-c2`



Traffic to all four of the backend VMs is load balanced.

###  Console 

#### Create backend VMs

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat these steps for each VM, using the following name and zone combinations.

     * Name: `vm-a1`, zone: `us-west1-a`
     * Name: `vm-a2`, zone: `us-west1-a`
     * Name: `vm-c1`, zone: `us-west1-c`
     * Name: `vm-c2`, zone: `us-west1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated in step 2.

  5. For **Region** , select `us-west1`, and choose a **Zone** as indicated in step 2.

  6. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Change** to change the image.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh` and `allow-health-check-ipv6`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network-ipv6-only`
        * **Subnet** : `lb-subnet-ipv6-only`
        * **IP stack type** : **IPv6 (single-stack)**
        * **Primary internal IPv6 address** : **Ephemeral (Automatic)**
  9. Click **Create**.




The backend VM needs to run an IPv6 TCP server that listens for incoming connections. You install this server on the backend VMs after you have configured the load balancer. This is because the server script creates a socket that binds to the forwarding rule of the load balancer. 

#### Create instance groups

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Repeat the following steps to create two unmanaged instance groups each with two VMs in them, using these combinations.

     * Instance group name: `ig-a`, zone: `us-west1-a`, VMs: `vm-a1` and `vm-a2`
     * Instance group name: `ig-c`, zone: `us-west1-c`, VMs: `vm-c1` and `vm-c2`
  3. Click **Create instance group**.

  4. Click **New unmanaged instance group**.

  5. Set **Name** as indicated in step 2.

  6. In the **Location** section, select `us-west1` for the **Region** , and then choose a **Zone** as indicated in step 2.

  7. For **Network** , select `lb-network-ipv6-only`.

  8. For **Subnetwork** , select `lb-subnet-ipv6-only`.

  9. In the **VM instances** section, add the VMs as indicated in step 2.

  10. Click **Create**.




###  gcloud 

  1. To create the four VMs, run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) four times, using these four combinations for `[VM-NAME]` and `[ZONE]`.

     * `VM-NAME`: `vm-a1`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-a2`, `ZONE`: `us-west1-a`
     * `VM-NAME`: `vm-c1`, `ZONE`: `us-west1-c`
     * `VM-NAME`: `vm-c2`, `ZONE`: `us-west1-c`
    
    gcloud beta compute instances create VM-NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh,allow-health-check-ipv6 \
        --subnet=lb-subnet-ipv6-only \
        --stack-type=IPV6_ONLY
    

The backend VM needs to run an IPv6 TCP server that listens for incoming connections. You install this server on the backend VMs after you have configured the load balancer. This is because the server script creates a socket that binds to the forwarding rule of the load balancer. 

  2. Create the two unmanaged instance groups in each zone:
         
         gcloud beta compute instance-groups unmanaged create ig-a \
             --zone=us-west1-a
         gcloud beta compute instance-groups unmanaged create ig-c \
             --zone=us-west1-c
         

  3. Add the VMs to the appropriate instance groups:
         
         gcloud beta compute instance-groups unmanaged add-instances ig-a \
           --zone=us-west1-a \
           --instances=vm-a1,vm-a2
         gcloud beta compute instance-groups unmanaged add-instances ig-c \
           --zone=us-west1-c \
           --instances=vm-c1,vm-c2
         




### Configure load balancer components

These steps configure all of the [internal passthrough Network Load Balancer components](https://docs.cloud.google.com/load-balancing/docs/internal#components) starting with the health check and backend service, and then the frontend components:

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

On the **Create internal passthrough Network Load Balancer** page, enter the following information:

  * **Load balancer name** : `ilb-ipv6-only`
  * **Region** : **`us-west1`**
  * **Network** : **`lb-network-ipv6-only`**



#### Backend configuration

  1. Click **Backend configuration**.
  2. In the **Health check** list, click **Create a health check** , and then enter the following information: 
     * **Name** : `hc-http-80`
     * **Scope** : **Regional**
     * **Protocol** : **HTTP**
     * **Port** : `80`
     * **Proxy protocol** : **None**
     * **Request** : `/`
  3. Click **Create**.
  4. In the **New Backend** section, for **IP stack type** , select the **IPv6 (single-stack)** option.
  5. In **Instance group** , select the `ig-a` instance group and click **Done**.
  6. Click **Add a backend** and repeat the step to add the `ig-c` instance group.
  7. Verify that a blue check mark appears next to **Backend configuration**.



#### Frontend configuration

  1. Click **Frontend configuration**. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter `fr-ilb-ipv6-only`.
     2. To handle IPv6 traffic, do the following: 
        1. For **IP version** , select **IPv6**. The IPv6 TCP server that you are going to create in the following section binds to the VIP of the forwarding rule.
        2. For **Subnetwork** , select`lb-subnet-ipv6-only`. The IPv6 address range in the forwarding rule is always ephemeral.
        3. For **Ports** , select **Multiple** , and then in the **Port number** field, enter `80`,`8008`,`8080`,`8088`.
        4. Click **Done**.
     3. Verify that there is a blue check mark next to **Frontend configuration** before continuing.



#### Review the configuration

  1. Click **Review and finalize**. Check all your settings.
  2. If the settings are correct, click **Create**. It takes a few minutes for the internal passthrough Network Load Balancer to be created.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to the VMs on port 80.
         
         gcloud beta compute health-checks create http hc-http-80 \
             --region=us-west1 \
             --port=80
         

  2. Create the backend service:
         
         gcloud beta compute backend-services create ilb-ipv6-only \
             --load-balancing-scheme=INTERNAL \
             --protocol=tcp \
             --region=us-west1 \
             --health-checks=hc-http-80 \
             --health-checks-region=us-west1
         

  3. Add the two instance groups to the backend service:
         
         gcloud beta compute backend-services add-backend ilb-ipv6-only \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         
         
         gcloud beta compute backend-services add-backend ilb-ipv6-only \
             --region=us-west1 \
             --instance-group=ig-c \
             --instance-group-zone=us-west1-c
         

  4. Create the IPv6 forwarding rule with an ephemeral IPv6 address.
         
         gcloud beta compute forwarding-rules create fr-ilb-ipv6-only \
             --region=us-west1 \
             --load-balancing-scheme=INTERNAL \
             --subnet=lb-subnet-ipv6-only \
             --ip-protocol=TCP \
             --ports=80,8008,8080,8088 \
             --backend-service=ilb-ipv6-only \
             --backend-service-region=us-west1 \
             --ip-version=IPV6
         

The IPv6 TCP server that you are going to create in the following section binds to the VIP of the forwarding rule.




### Install an IPv6 TCP server on the backend VMs using a startup Bash script

In this example, the Bash startup script for backend VMs contains the following:

  * Networking commands to route all outgoing packets originating from a subnet through a specified gateway and network interface.
  * Python server script (`server.py`), which is an IPv6 TCP server, that listens for incoming connections on the specified VIP and network interface. It accepts incoming client connections, sends a response, and then closes the connection.



You need to add the following details in the Bash script:

  * Gateway address
  * Subnet range
  * VIP of the forwarding rule
  * Network interface



You can identify the gateway address and the subnet range by running the `ip -6 route show table all` command in the backend VM. To learn more about the commands that are used in the startup Bash script, see the Appendix section.

To add a startup script to the VM instance, do the following:

**Note:** You need to run these steps for each backend VM that you created earlier.

###  Console 

  1. In the list of VM instances that you created earlier, click the VM instance that you need to update.

  2. Click **Edit**.

  3. In the **Metadata** section, enter the following script in the **Startup script** field.

**Note:** The server script `server.py` referenced in the Bash script is stored in the root folder of your backend VM.
         
         #!/bin/bash
         
         # Replace these with your actual values. Run the 'ip -6 route show table all' command to find the correct values.
         GATEWAY_ADDRESS=fe80::57:2ff:fe36:ffbe
         SUBNET_RANGE=fd20:307:120c:2000::/64
         
         # Add a custom default route to routing table 1.
         # The following command sends packets to the gateway using the network interface named 'ens4'.
         sudo ip route add default via $GATEWAY_ADDRESS dev ens4 table 1
         
         # Add a source-based policy routing rule.
         # The following command adds a rule to route all outgoing packets originating
         # from a specified subnet. If the source address matches the subnet,
         # the system uses the default route defined in table 1 to forward the traffic.
         sudo ip -6 rule add from $SUBNET_RANGE table 1
         
         # Allow the server to bind to a non-local IPv6 address--the VIP of the load balancer.
         sudo sysctl -w net.ipv6.ip_nonlocal_bind=1
         
         # Overview:
         # This script sets up a simple IPv6 TCP server using Python's socket library.
         # The server binds to a specific network interface and listens on a specified Virtual IP (VIP) address and port (default: 80).
         # It accepts incoming client connections, sends a simple response ("Thank you for connecting"), and then closes the connection.
         # Key features:
         # - Uses IPv6 (AF_INET6) for networking.
         # - Binds to a specific network interface using SO_BINDTODEVICE.
         # - Handles multiple client connections in a loop.
         # - Demonstrates basic socket programming concepts like binding, listening, accepting, and sending data.
         # Note: Replace placeholders like 'FORWARDING_RULE_VIP' and 'ens4' with actual values for your setup.
         
         # Write the Python file locally.
         cat << 'EOF' > server.py
         
         # Import the socket library to work with network connections
         import socket
         import urllib.request
         
         # Fetch the VM hostname from Google Cloud metadata server
         def get_vm_hostname():
             url = "http://metadata.google.internal/computeMetadata/v1/instance/name"
             req = urllib.request.Request(url, headers={"Metadata-Flavor": "Google"})
             with urllib.request.urlopen(req) as response:
                 return response.read().decode()
         
         vm_hostname = get_vm_hostname()
         
         # Create a socket object for IPv6 and TCP connections
         # AF_INET6 specifies IPv6, SOCK_STREAM specifies TCP
         server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
         
         # Set the SO_REUSEADDR option to allow reusing the address
         # This is useful to avoid "address already in use" errors when restarting the server
         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         
         # Specify the network interface to bind the server to
         # Replace "ens4" with the name of your network interface
         interface_name = "ens4"
         # Get the index of the network interface
         interface_index = socket.if_nametoindex(interface_name)
         # Bind the socket to the specified network interface
         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface_name.encode())
         
         # Bind the socket to an address and port
         # Replace 'FORWARDING_RULE_VIP' with the actual VIP (Virtual IP) address
         server_address = ('FORWARDING_RULE_VIP', 80, 0, 0)
         server_socket.bind(server_address)
         
         # Start listening for incoming connections
         # The argument '5' specifies the maximum number of queued connections
         server_socket.listen(5)
         
         # Print a message indicating that the server is ready to accept connections
         print(f"Server listening on {server_address}, bound to {interface_name}")
         
         # Serve incoming connections
         while True:
             client_socket, client_address = server_socket.accept()
             print(f"Accepted connection from {client_address}")
         
             # Generate response body
             body = f"Thank you for connecting to {vm_hostname}\n"
         
             # Construct a proper HTTP/1.1 response
             response = (
                 "HTTP/1.1 200 OK\r\n"
                 f"Content-Length: {len(body)}\r\n"
                 "Content-Type: text/plain\r\n"
                 "Connection: close\r\n"
                 "\r\n"
                 f"{body}"
             )
         
             # Send the response and close the connection
             client_socket.sendall(response.encode())
             client_socket.close()
         EOF
         
         # Make the Python script executable
         chmod +x server.py
         
         # Run the server
         sudo python3 server.py
         
         

  4. Click **Save**.

  5. [Reboot the instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance).




###  gcloud 

  1. Create a startup script.
         
         nano startup.sh
         

  2. Add the following script and save the file.

**Note:** The server script `server.py` referenced in the Bash script is stored in the root folder of your backend VM.
         
         #!/bin/bash
         
         # Replace these with your actual values. Run the 'ip -6 route show table all' command to find the correct values.
         GATEWAY_ADDRESS=fe80::57:2ff:fe36:ffbe
         SUBNET_RANGE=fd20:307:120c:2000::/64
         
         # Add a custom default route to routing table 1.
         # The following command sends packets to the gateway using the network interface named 'ens4'.
         sudo ip route add default via $GATEWAY_ADDRESS dev ens4 table 1
         
         # Add a source-based policy routing rule.
         # The following command adds a rule to route all outgoing packets originating
         # from a specified subnet. If the source address matches the subnet,
         # the system uses the default route defined in table 1 to forward the traffic.
         sudo ip -6 rule add from $SUBNET_RANGE table 1
         
         # Allow the server to bind to a non-local IPv6 address--the VIP of the load balancer.
         sudo sysctl -w net.ipv6.ip_nonlocal_bind=1
         
         # Overview:
         # This script sets up a simple IPv6 TCP server using Python's socket library.
         # The server binds to a specific network interface and listens on a specified Virtual IP (VIP) address and port (default: 80).
         # It accepts incoming client connections, sends a simple response ("Thank you for connecting"), and then closes the connection.
         # Key features:
         # - Uses IPv6 (AF_INET6) for networking.
         # - Binds to a specific network interface using SO_BINDTODEVICE.
         # - Handles multiple client connections in a loop.
         # - Demonstrates basic socket programming concepts like binding, listening, accepting, and sending data.
         # Note: Replace placeholders like 'FORWARDING_RULE_VIP' and 'ens4' with actual values for your setup.
         
         # Write the Python file locally.
         cat << 'EOF' > server.py
         
         # Import the socket library to work with network connections
         import socket
         import urllib.request
         
         # Fetch the VM hostname from Google Cloud metadata server
         def get_vm_hostname():
             url = "http://metadata.google.internal/computeMetadata/v1/instance/name"
             req = urllib.request.Request(url, headers={"Metadata-Flavor": "Google"})
             with urllib.request.urlopen(req) as response:
                 return response.read().decode()
         
         vm_hostname = get_vm_hostname()
         
         # Create a socket object for IPv6 and TCP connections
         # AF_INET6 specifies IPv6, SOCK_STREAM specifies TCP
         server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
         
         # Set the SO_REUSEADDR option to allow reusing the address
         # This is useful to avoid "address already in use" errors when restarting the server
         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
         
         # Specify the network interface to bind the server to
         # Replace "ens4" with the name of your network interface
         interface_name = "ens4"
         # Get the index of the network interface
         interface_index = socket.if_nametoindex(interface_name)
         # Bind the socket to the specified network interface
         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface_name.encode())
         
         # Bind the socket to an address and port
         # Replace 'FORWARDING_RULE_VIP' with the actual VIP (Virtual IP) address
         server_address = ('FORWARDING_RULE_VIP', 80, 0, 0)
         server_socket.bind(server_address)
         
         # Start listening for incoming connections
         # The argument '5' specifies the maximum number of queued connections
         server_socket.listen(5)
         
         # Print a message indicating that the server is ready to accept connections
         print(f"Server listening on {server_address}, bound to {interface_name}")
         
         # Serve incoming connections
         while True:
             client_socket, client_address = server_socket.accept()
             print(f"Accepted connection from {client_address}")
         
             # Generate response body
             body = f"Thank you for connecting to {vm_hostname}\n"
         
             # Construct a proper HTTP/1.1 response
             response = (
                 "HTTP/1.1 200 OK\r\n"
                 f"Content-Length: {len(body)}\r\n"
                 "Content-Type: text/plain\r\n"
                 "Connection: close\r\n"
                 "\r\n"
                 f"{body}"
             )
         
             # Send the response and close the connection
             client_socket.sendall(response.encode())
             client_socket.close()
         EOF
         
         # Make the Python script executable
         chmod +x server.py
         
         # Run the server
         sudo python3 server.py
         
         

  3. Add the metadata file to the VM instance.
         
         gcloud compute instances add-metadata VM-NAME \
           --metadata-from-file=startup-script=startup.sh
         

  4. [Reboot the instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance).




### Test your load balancer

To test the load balancer, create a client VM in the same region as the load balancer, and then send traffic from the client to the load balancer.

#### Create a client VM

This example creates a client VM (`vm-client`) in the same region as the backend (server) VMs. The client is used to validate the load balancer's configuration and demonstrate expected behavior as described in the testing section.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `vm-client`.

  4. For **Region** , select **`us-west1`**.

  5. For **Zone** , select **`us-west1-a`**.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : **`lb-network-ipv6-only`**
        * **Subnet** : **`lb-subnet-ipv6-only`**
        * **IP stack type** : **IPv6 (single-stack)**
     3. Click **Done**.
  8. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `us-west1-a` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud beta compute instances create vm-client \
        --zone=us-west1-a \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --stack-type=IPV6_ONLY \
        --tags=allow-ssh \
        --subnet=lb-subnet-ipv6-only
    

#### Test the connection

This test contacts the load balancer from a separate client VM; that is, not from a backend VM of the load balancer. The expected behavior is for traffic to be distributed among the four backend VMs.

  1. Connect to the client VM instance [by using SSH](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Describe the IPv6 forwarding rule `fr-ilb-ipv6-only`. Note the `IPV6_ADDRESS` in the description.
         
         gcloud beta compute forwarding-rules describe fr-ilb-ipv6-only \
             --region=us-west1
         

  3. From clients with IPv6 connectivity, run the following command:
         
         curl http://IPV6_ADDRESS:80
         

For example, if the assigned IPv6 address is `[fd20:307:120c:2000:0:1:0:0/96]:80`, the command should look like:
         
         curl http://[fd20:307:120c:2000:0:1:0:0]:80
         




## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### Enable global access

You can enable [global access](https://docs.cloud.google.com/load-balancing/docs/internal#client-access) for your example internal passthrough Network Load Balancer to make it accessible to clients in all regions. The backends of your example load balancer must still be located in one region (`us-west1`).

[ ![Internal passthrough Network Load Balancer with global access.](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-global-access-arch.svg)](https://docs.cloud.google.com/static/load-balancing/images/l4ilb-global-access-arch.svg) Internal passthrough Network Load Balancer with global access (click to enlarge).

To configure global access, make the following configuration changes.

###  Console 

**Edit the load balancer's forwarding rule**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. In the **Name** column, click your internal passthrough Network Load Balancer. The example load balancer is named `be-ilb`.

  3. Click **Frontend configuration**.

  4. Click **Edit** edit.

  5. Under **Global access** , select **Enable**.

  6. Click **Done**.

  7. Click **Update**.




On the **Load balancer details** page, verify that the frontend configuration says **Regional (` REGION`) with global access**.

###  gcloud 

  1. Update the example load balancer's forwarding rule, `fr-ilb` to include the `--allow-global-access` flag.
         
         gcloud compute forwarding-rules update fr-ilb \
              --region=us-west1 \
              --allow-global-access
         

  2. You can use the `forwarding-rules describe` command to determine whether a forwarding rule has global access enabled. For example:
         
         gcloud compute forwarding-rules describe fr-ilb \
              --region=us-west1 \
              --format="get(name,region,allowGlobalAccess)"
         

The word `True` appears in the output, after the name and region of the forwarding rule, when global access is enabled.




###  API 

Make a `PATCH` request to the [`forwardingRules/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/fr-ilb
    
    {
    "allowGlobalAccess": true
    }
    

#### Create a VM client to test global access

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set the **Name** to `vm-client2`.

  4. Set the **Region** to **`europe-west1`**.

  5. Set the **Zone** to **`europe-west1-b`**.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * **Network** : **`lb-network`**
        * **Subnet** : **`europe-subnet`**
  8. Click **Create**.




###  gcloud 

The client VM can be in any zone in the same region as the load balancer, and it can use any subnet in that region. In this example, the client is in the `europe-west1-b` zone, and it uses the same subnet as the backend VMs.
    
    
    gcloud compute instances create vm-client2 \
        --zone=europe-west1-b \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=europe-subnet
    

###  API 

Make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/europe-west1-b/instances
    
    {
    "name": "vm-client2",
    "tags": {
      "items": [
        "allow-ssh"
      ]
    },
    "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/europe-west1-b/machineTypes/e2-standard-2",
    "canIpForward": false,
    "networkInterfaces": [
      {
        "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
        "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/europe-west1/subnetworks/europe-subnet",
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
        "deviceName": "vm-client2",
        "initializeParams": {
          "sourceImage": "projects/debian-cloud/global/images/debian-image-name",
          "diskType": "projects/PROJECT_ID/zones/europe-west1-b/diskTypes/pd-standard",
          "diskSizeGb": "10"
        }
      }
    ],
    "scheduling": {
      "preemptible": false
    },
    "deletionProtection": false
    }
    

#### Connect to the VM client and test connectivity

To test the connectivity, run the following command:
    
    
      gcloud compute ssh vm-client2 --zone=europe-west1-b
      

Test connecting to the load balancer on all configured ports, as you did from the `vm-client` in the `us-west1` region. Test HTTP connectivity on the four ports configured on the forwarding rule:
    
    
      curl http://10.1.2.99
      curl http://10.1.2.99:8008
      curl http://10.1.2.99:8080
      curl http://10.1.2.99:8088
      

### Configure managed instance groups

The example configuration created two unmanaged instance groups. You can instead use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#types_of_managed_instance_groups), including zonal and regional managed instance groups, as backends for internal passthrough Network Load Balancers.

Managed instance groups require that you create an instance template. This procedure demonstrates how to replace the two zonal unmanaged instance groups from the example with a single, regional managed instance group. A regional managed instance group automatically creates VMs in multiple zones of the region, making it simpler to distribute production traffic among zones.

Managed instance groups also support [autoscaling](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) and [autohealing](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update). If you use autoscaling with internal passthrough Network Load Balancers, you cannot scale based on load balancing.

This procedure shows you how to modify the backend service for the example internal passthrough Network Load Balancer so that it uses a regional managed instance group.

###  Console 

**Instance template**

  1. In the Google Cloud console, go to the **VM instance templates** page.

[Go to VM instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. Set the **Name** to `template-vm-ilb`.

  4. Choose a [machine type](https://docs.cloud.google.com/compute/docs/machine-types).

  5. In the **Boot disk** section, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk options. If necessary, click **Change** to change the image.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh` and `allow-health-check`.
     2. For **Network interfaces** , select the following: 
        * **Network** : `lb-network`
        * **Subnet** : `lb-subnet`
  8. Click **Management** , and then in the **Startup script** field, enter the following script:
         
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
         

  9. Click **Create**.




**Managed instance group**

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**.

  3. Set the **Name** to `ig-ilb`.

  4. For **Location** , choose **Multi-zone** , and set the **Region** to `us-west1`.

  5. Set the **Instance template** to `template-vm-ilb`.

  6. Optional: Configure [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler). You cannot autoscale the instance group based on HTTP load balancing usage because the instance group is a backend for the internal passthrough Network Load Balancer.

  7. Set the **Minimum number of instances** to `1` and the **Maximum number of instances** to `6`.

  8. Optional: Configure [**autohealing**](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs). If you configure autohealing, use the same health check used by the backend service for the internal passthrough Network Load Balancer. In this example, use `hc-http-80`.

  9. Click **Create**.




###  gcloud 

  1. Create the instance template. Optionally, you can [set other parameters](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create), such as [machine type](https://docs.cloud.google.com/compute/docs/machine-types), for the image template to use.
         
         gcloud compute instance-templates create template-vm-ilb \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh,allow-health-check \
             --subnet=lb-subnet \
             --region=us-west1 \
             --network=lb-network \
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
         

  2. Create one regional managed instance group using the template:
         
         gcloud compute instance-groups managed create ig-ilb \
             --template=template-vm-ilb \
             --region=us-west1 \
             --size=6
         

  3. Add the regional managed instance group as a backend to the backend service that you already created:
         
         gcloud compute backend-services add-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-ilb \
             --instance-group-region=us-west1
         

  4. Disconnect the two unmanaged (zonal) instance groups from the backend service:
         
         gcloud compute backend-services remove-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-a \
             --instance-group-zone=us-west1-a
         gcloud compute backend-services remove-backend be-ilb \
             --region=us-west1 \
             --instance-group=ig-c \
             --instance-group-zone=us-west1-c
         




### Remove external IP addresses from backend VMs

When you created the backend VMs, each was assigned an ephemeral external IP address so it could download Apache using a startup script. Because the backend VMs are only used by an internal passthrough Network Load Balancer, you can remove their external IP addresses. Removing external IP addresses prevents the backend VMs from accessing the internet directly.

**Important:** Removing the external IP address from a VM limits how you can connect to it. For details, see [Choose a connection option for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip). It's useful to leave external IP addresses on backend VMs if you need to demonstrate how requests from a backend VM to the IP address of the load balancer are handled.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat the following steps for each backend VM.

  3. Click the name of the backend VM, for example, `vm-a1`.

  4. Click edit**Edit**.

  5. In the **Network interfaces** section, click the network.

  6. From the **External IP** list, select **None** , and click **Done**.

  7. Click **Save**.




###  gcloud 

  1. To look up the zone for an instance – for example, if you're using a regional managed instance group – run the following command for each instance to determine its zone. Replace `[SERVER-VM]` with the name of the VM to look up.
         
         gcloud compute instances list --filter="name=[SERVER-VM]"
         

  2. Repeat the following step for each backend VM. Replace `[SERVER-VM]` with the name of the VM, and replace and `[ZONE]` with the VM's zone.
         
         gcloud compute instances delete-access-config [SERVER-VM] \
             --zone=[ZONE] \
             --access-config-name=external-nat
         




###  API 

Make a `POST` request to the [`instances.deleteAccessConfig` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/deleteAccessConfig) for each backend VM, replacing`vm-a1` with the name of the VM, and replacing and `us-west1-a` with the VM's zone.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/vm-a1/deleteAccessConfig?accessConfig=external-nat&networkInterface=None
    

### Use a reserved internal IP address

When you create backend VMs and instance groups, the VM instance uses an ephemeral internal IPv4 or IPv6 address.

The following steps show you how to promote an internal IPv4 or IPv6 address to a static internal IPv4 or IPv6 address and then update the VM instance to use the static internal IP address:

  1. [Promote an in-use ephemeral internal IPv4 or IPv6 address to a static address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#promote-in-use-internal-address).
  2. [Change or assign an internal IPv6 address to an existing instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address#change_assign_intipv6).



Alternatively, the following steps show you how to reserve a new static internal IPv4 or IPv6 address and then update the VM instance to use the static internal IP address:

  1. [Reserve a new static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).

Unlike internal IPv4 reservation, internal IPv6 reservation doesn't support reserving a specific IP address from the subnetwork. Instead, a `/96` internal IPv6 address range is automatically allocated from the subnet's `/64` internal IPv6 address range.

  2. [Change or assign an internal IPv6 address to an existing instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address#change_assign_intipv6).




For more information, see [How to reserve a static internal IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address#how_to_reserve_a_static_internal_ip_address).

### Accept traffic on all ports

The load balancer's forwarding rule, not its backend service, determines the port or ports on which the load balancer accepts traffic. For information about the purpose of each component, see [Components](https://docs.cloud.google.com/load-balancing/docs/internal#components).

When you created this example load balancer's forwarding rule, you configured ports `80`, `8008`, `8080`, and `8088`. The startup script that installs Apache also configures it to accept HTTPS connections on ports `443` and `8443`.

To support these six ports, you can configure the forwarding rule to accept traffic on all ports. With this strategy, you can also configure the firewall rule or rules that allow incoming connections to backend VMs so that they only permit certain ports.

This procedure shows you how to delete the load balancer's current forwarding rule and create a new one that accepts traffic on all ports.

**Note:** If you try to edit the existing forwarding rule by adding a new port, you might encounter the following error: `Forwarding rule's port range is conflicting with forwarding rule: resource_type: FORWARDING_RULE resource_name: "<EXISTING_FORWARDING_RULE_NAME>"`

For more information about when to use this setup, see [Internal passthrough Network Load Balancers and forwarding rules with a common IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip).

###  Console 

**Delete your forwarding rule and create a new one**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the `be-ilb` load balancer and click **Edit**.

  3. Click **Frontend configuration**.

  4. Hold the pointer over the `10.1.2.9` forwarding rule and click delete**Delete**.

  5. Click **Add frontend IP and port**.

  6. In the **New Frontend IP and port** section, enter the following information and click **Done** :

     * **Name** : `fr-ilb`
     * **Subnetwork** : **`lb-subnet`**
     * **Internal IP** : **`ip-ilb`**
     * **Ports** : **All**.
  7. Verify that there is a blue check mark next to **Frontend configuration** before continuing.

  8. Click **Review and finalize** and review your load balancer configuration settings.

  9. Click **Create**.




###  gcloud 

  1. Delete your existing forwarding rule, `fr-ilb`.
         
         gcloud compute forwarding-rules delete fr-ilb \
             --region=us-west1
         

  2. Create a replacement forwarding rule, with the same name, whose port configuration uses the keyword `ALL`. The other parameters for the forwarding rule remain the same.
         
         gcloud compute forwarding-rules create fr-ilb \
             --region=us-west1 \
             --load-balancing-scheme=internal \
             --network=lb-network \
             --subnet=lb-subnet \
             --address=10.1.2.99 \
             --ip-protocol=TCP \
             --ports=ALL \
             --backend-service=be-ilb \
             --backend-service-region=us-west1
         




###  API 

Delete the forwarding rule by making a `DELETE` request to the [`forwardingRules.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/fr-ilb
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "allPorts": true,
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "networkTier": "PREMIUM"
    }
    

#### Test the traffic on all ports setup

Connect to the client VM instance and test HTTP and HTTPS connections.

  * Connect to the client VM:
        
        gcloud compute ssh vm-client --zone=us-west1-a
        

  * Test HTTP connectivity on all four ports:
        
        curl http://10.1.2.99
        curl http://10.1.2.99:8008
        curl http://10.1.2.99:8080
        curl http://10.1.2.99:8088
        

  * Test HTTPS connectivity on ports `443` and `8443`. The `--insecure` flag is required because each Apache server in the example setup uses a self-signed certificate. 
        
        curl https://10.1.2.99 --insecure
        curl https://10.1.2.99:8443 --insecure
        

  * Observe that HTTP requests (on all four ports) and HTTPS requests (on both ports) are distributed among all of the backend VMs.




### Accept traffic on multiple ports using two forwarding rules

When you created this example load balancer's forwarding rule, you configured ports `80`, `8008`, `8080`, and `8088`. The startup script that installs Apache also configures it to accept HTTPS connections on ports `443` and `8443`.

An alternative strategy to configuring a single forwarding rule to accept traffic on all ports is to create multiple forwarding rules, each supporting five or fewer ports.

This procedure shows you how to replace the example load balancer's forwarding rule with two forwarding rules, one handling traffic on ports `80`, `8008`, `8080`, and `8088`, and the other handling traffic on ports `443` and `8443`.

For more information about when to use this setup, see [Internal passthrough Network Load Balancers and forwarding rules with a common IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip).

###  Console 

  1. In the Google Cloud console, go to the **Forwarding rules** page.

[Go to Forwarding rules](https://console.cloud.google.com/net-services/loadbalancing/advanced/forwardingRules/list)

  2. In the **Name** column, click **`fr-ilb`** , and then click **Delete**.

  3. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  4. In the **Name** column, click **`be-ilb`**.

  5. Click **Edit**.

  6. Click **Frontend configuration**.

  7. Click **Add frontend IP and port**.

  8. In the **New Frontend IP and port** section, do the following:

     1. For **Name** , enter `fr-ilb-http`.
     2. For **Subnetwork** , select **`lb-subnet`**.
     3. For **Internal IP purpose** , select **Shared**.
     4. From the **IP address** list, select **Create IP address** , enter the following information, and click **Reserve** : 
        * **Name** : `internal-10-1-2-99`
        * **Static IP address** : **Let me choose**
        * **Custom IP address** : `10.1.2.99`
     5. For **Ports** , select **Multiple** , and then in **Port numbers** , enter `80`,`8008`,`8080`, and `8088`.
     6. Click **Done**.
  9. Click **Add frontend IP and port**.

  10. In the **New Frontend IP and port** section, do the following:

     1. For **Name** , enter `fr-ilb-https`.
     2. For **Subnetwork** , select **`lb-subnet`**.
     3. For **Internal IP purpose** , select **Shared**.
     4. From the **IP address** list, select **`internal-10-1-2-99`**.
     5. For **Ports** , select **Multiple** , and then in **Port numbers** , enter `443` and `8443`.
     6. Click **Done**.
  11. Click **Review and finalize** , and review your load balancer configuration settings.

  12. Click **Update**.




###  gcloud 

  1. Delete your existing forwarding rule, `fr-ilb`.
         
         gcloud compute forwarding-rules delete fr-ilb \
             --region=us-west1
         

  2. Create a static (reserved) internal IP address for `10.1.2.99` and set its `--purpose` flag to `SHARED_LOADBALANCER_VIP`. The `--purpose` flag is required so that two internal forwarding rules can use the same internal IP address.
         
         gcloud compute addresses create internal-10-1-2-99 \
             --region=us-west1 \
             --subnet=lb-subnet \
             --addresses=10.1.2.99 \
             --purpose=SHARED_LOADBALANCER_VIP
         

     1. Create two replacement forwarding rules with the following parameters:
    
    gcloud compute forwarding-rules create fr-ilb-http \
        --region=us-west1 \
        --load-balancing-scheme=internal \
        --network=lb-network \
        --subnet=lb-subnet \
        --address=10.1.2.99 \
        --ip-protocol=TCP \
        --ports=80,8008,8080,8088 \
        --backend-service=be-ilb \
        --backend-service-region=us-west1
    
    
    gcloud compute forwarding-rules create fr-ilb-https \
        --region=us-west1 \
        --load-balancing-scheme=internal \
        --network=lb-network \
        --subnet=lb-subnet \
        --address=10.1.2.99 \
        --ip-protocol=TCP \
        --ports=443,8443 \
        --backend-service=be-ilb \
        --backend-service-region=us-west1
    




###  API 

Delete the forwarding rule by making a `DELETE` request to the [`forwardingRules.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/fr-ilb
    

Create a static (reserved) internal IP address for `10.1.2.99` and set its purpose to `SHARED_LOADBALANCER_VIP` by making a `POST` request to the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/addresses
    
    {
    "name": "internal-10-1-2-99",
    "address": "10.1.2.99",
    "prefixLength": 32,
    "addressType": INTERNAL,
    "purpose": SHARED_LOADBALANCER_VIP,
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet"
    }
    

Create two forwarding rules by making two `POST` requests to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb-http",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "ports": [
      "80", "8008", "8080",  "8088"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "networkTier": "PREMIUM"
    }
    
    
    
    {
    "name": "fr-ilb-https",
    "IPAddress": "10.1.2.99",
    "IPProtocol": "TCP",
    "ports": [
      "443", "8443"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "networkTier": "PREMIUM"
    }
    

#### Test the traffic on multiple ports setup

Connect to the client VM instance and test HTTP and HTTPS connections.

  * Connect to the client VM:
        
        gcloud compute ssh vm-client --zone=us-west1-a
        

  * Test HTTP connectivity on all four ports:
        
        curl http://10.1.2.99
        curl http://10.1.2.99:8008
        curl http://10.1.2.99:8080
        curl http://10.1.2.99:8088
        

  * Test HTTPS connectivity on ports `443` and `8443`. The `--insecure` flag is required because each Apache server in the example setup uses a self-signed certificate.
        
        curl https://10.1.2.99 --insecure
        curl https://10.1.2.99:8443 --insecure
        

  * Observe that HTTP requests (on all four ports) and HTTPS requests (on both ports) are distributed among all of the backend VMs.




### Use session affinity

The example configuration creates a backend service without session affinity.

This procedure shows you how to update the backend service for the example internal passthrough Network Load Balancer so that it uses session affinity based on a hash created from the client's IP addresses and the IP address of the load balancer's internal forwarding rule.

For supported session affinity types, see [Session affinity options](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#session_affinity).

**Note:** For internal _UDP_ load balancers, setting session affinity is supported in the gcloud CLI and the API. You can't set session affinity for UDP traffic by using the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click **be-ilb** (the name of the backend service that you created for this example) and click **Edit**.

  3. On the **Edit internal passthrough Network Load Balancer** page, click **Backend configuration**.

  4. From the **Session affinity** list, select **Client IP**.

  5. Click **Update**.




###  gcloud 

Use the following `gcloud` command to update the `be-ilb` backend service, specifying client IP session affinity:
    
    
    gcloud compute backend-services update be-ilb \
        --region=us-west1 \
        --session-affinity CLIENT_IP
    

###  API 

Make a `PATCH` request to the [`regionBackendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb
    
    {
    "sessionAffinity": "CLIENT_IP"
    }
    

### Configure a connection tracking policy

This section shows you how to update the backend service to change the load balancer's default connection tracking policy.

A connection tracking policy includes the following settings:

  * [Tracking mode](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#tracking-mode)
  * [Connection persistence on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#connection-persistence)
  * [Idle timeout](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#idle-timeout)

**Note:** You cannot use the Google Cloud console to configure a connection tracking policy. Use the Google Cloud CLI or the [REST API](/compute/docs/reference/rest/v1/regionBackendServices) instead. 

###  gcloud 

Use the following [`gcloud compute backend-services` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services) to update the connection tracking policy for the backend service:
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --region=REGION \
        --tracking-mode=TRACKING_MODE \
        --connection-persistence-on-unhealthy-backends=CONNECTION_PERSISTENCE_BEHAVIOR \
        --idle-timeout-sec=IDLE_TIMEOUT_VALUE
    

Replace the placeholders with valid values:

  * `BACKEND_SERVICE`: the backend service that you're updating
  * `REGION`: the region of the backend service that you're updating
  * `TRACKING_MODE`: the connection tracking mode to be used for incoming packets; for the list of supported values, see [Tracking mode](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#tracking-mode)
  * `CONNECTION_PERSISTENCE_BEHAVIOR`: the connection persistence behavior when backends are unhealthy; for the list of supported values, see [Connection persistence on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#connection-persistence)
  * `IDLE_TIMEOUT_VALUE`: the number of seconds that a connection tracking table entry must be maintained after the load balancer processes the last packet that matched the entry



### Use zonal affinity

This section shows you how to configure an internal passthrough Network Load Balancer to [enable zonal affinity on the backend service](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update#--zonal-affinity-spillover) of the load balancer. By default, zonal affinity is disabled. For more information, see [Zonal affinity for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity).

  * Use the following command to configure the `ZONAL_AFFINITY_STAY_WITHIN_ZONE` zonal affinity option. For more information about how this option works, see [How `ZONAL_AFFINITY_STAY_WITHIN_ZONE` works](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-stay-in-zone).
        
        gcloud compute backend-services update be-ilb \
            --zonal-affinity-spillover=ZONAL_AFFINITY_STAY_WITHIN_ZONE \
            --region=us-west1
        

  * Use the following command to configure `ZONAL_AFFINITY_SPILL_CROSS_ZONE` zonal affinity with the default `0.0` spillover ratio. For more information about how this option works, see the [How `ZONAL_AFFINITY_SPILL_CROSS_ZONE` and spillover ratio work](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-spillover-ratio) and [Zero spillover ratio](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-spillover-ratio-zero) sections.
        
        gcloud compute backend-services update be-ilb \
            --zonal-affinity-spillover=ZONAL_AFFINITY_SPILL_CROSS_ZONE \
            --region=us-west1
        

  * Use the following command to configure `ZONAL_AFFINITY_SPILL_CROSS_ZONE` zonal affinity with a 30% spillover ratio. For more information about how this option works, see [How `ZONAL_AFFINITY_SPILL_CROSS_ZONE` and spillover ratio work](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-spillover-ratio) and [Nonzero spillover ratio](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity#zonal-affinity-spillover-ratio-non-zero) sections.
        
        gcloud compute backend-services update be-ilb \
            --zonal-affinity-spillover=ZONAL_AFFINITY_SPILL_CROSS_ZONE \
            --zonal-affinity-spillover-ratio=0.3 \
            --region=us-west1
        




### Create a forwarding rule in another subnet

This procedure creates a second IP address and forwarding rule in a different subnet to demonstrate that you can [create multiple forwarding rules](https://docs.cloud.google.com/load-balancing/docs/internal#multiple_forwarding_rule) for one internal passthrough Network Load Balancer. The region for the forwarding rule must match the region of the backend service.

Subject to firewall rules, clients in any subnet in the region can contact either internal passthrough Network Load Balancer IP address.

###  Console 

**Add the second subnet**

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Click `lb-network`.

  4. In the **Subnets** section, do the following:

     1. Click **Add subnet**.
     2. In the **New subnet** section, enter the following information: 
        * **Name** : `second-subnet`
        * **Region** : `us-west1`
        * **IP address range** : `10.5.6.0/24`
     3. Click **Add**.



**Add the second forwarding rule**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the `be-ilb` load balancer and click **Edit**.

  3. Click **Frontend configuration**.

  4. Click **Add frontend IP and port**.

  5. In the **New Frontend IP and port** section, set the following fields and click **Done** :

     * **Name** : `fr-ilb-2`
     * **IP version** : **IPv4**
     * **Subnetwork** : **`second-subnet`**
     * **Internal IP** : **`ip-ilb`**
     * **Ports** : `80` and `443`
  6. Verify that there is a blue check mark next to **Frontend configuration** before continuing.

  7. Click **Review and finalize** , and review your load balancer configuration settings.

  8. Click **Create**.




###  gcloud 

  1. Create a second subnet in the `lb-network` network in the `us-west1` region:
         
         gcloud compute networks subnets create second-subnet \
              --network=lb-network \
              --range=10.5.6.0/24 \
              --region=us-west1
         

  2. Create a second forwarding rule for ports 80 and 443. The other parameters for this rule, including IP address and backend service, are the same as for the primary forwarding rule, `fr-ilb`.
         
         gcloud compute forwarding-rules create fr-ilb-2 \
              --region=us-west1 \
              --load-balancing-scheme=internal \
              --network=lb-network \
              --subnet=second-subnet \
              --address=10.5.6.99 \
              --ip-protocol=TCP \
              --ports=80,443 \
              --backend-service=be-ilb \
              --backend-service-region=us-west1
         




###  API 

Make a `POST` requests to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks
    
    {
     "name": "second-subnet",
     "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
     "ipCidrRange": "10.5.6.0/24",
     "privateIpGoogleAccess": false
    }
    

Create the forwarding rule by making a `POST` request to the [`forwardingRules.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules
    
    {
    "name": "fr-ilb-2",
    "IPAddress": "10.5.6.99",
    "IPProtocol": "TCP",
    "ports": [
      "80", "443"
    ],
    "loadBalancingScheme": "INTERNAL",
    "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/subnetworks/lb-subnet",
    "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/lb-network",
    "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb",
    "networkTier": "PREMIUM"
    }
    

#### Test the new forwarding rule

Connect to the client VM instance and test HTTP and HTTPS connections to the IP addresses.

  1. Connect to the client VM:
         
         gcloud compute ssh vm-client --zone=us-west1-a
         

  2. Test HTTP connectivity to the IP addresses:
         
         curl http://10.1.2.99
         curl http://10.5.6.99
         

  3. Test HTTPS connectivity. Use of `--insecure` is required because the Apache server configuration in the example setup uses self-signed certificates.
         
         curl https://10.1.2.99 --insecure
         curl https://10.5.6.99 --insecure
         

  4. Observe that requests are handled by all of the backend VMs, regardless of the protocol (HTTP or HTTPS) or IP address used.




### Use backend subsetting

The example configuration creates a backend service without subsetting.

This procedure shows you how to enable subsetting on the backend service for the example internal passthrough Network Load Balancer so that the deployment can scale to a larger number of backend instances.

**Caution:** Enabling backend subsetting might be temporarily disruptive and might break existing TCP connections.

You should only enable subsetting if you need to support more than 250 backend VMs on a single load balancer.

**Note:** This feature does not support IPv6 addresses.

For more information about this use case, see [backend subsetting](https://docs.cloud.google.com/load-balancing/docs/backend-service#tcp-subsetting).

###  gcloud 

Use the following `gcloud` command to update the `be-ilb` backend service, specifying subsetting policy:
    
    
    gcloud compute backend-services update be-ilb \
        --subsetting-policy=CONSISTENT_HASH_SUBSETTING
    

###  API 

Make a `PATCH` request to the [`regionBackendServices/patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/be-ilb
    
    {
    "subsetting":
      {
        "policy": CONSISTENT_HASH_SUBSETTING
      }
    }
    

### Create a load balancer for Packet Mirroring

[Packet Mirroring](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview) lets you copy and collect packet data from specific instances in a VPC. The collected data can help you detect security threats and monitor application performance.

Packet Mirroring requires an internal passthrough Network Load Balancer in order to balance traffic to an instance group of collector destinations. To create an internal passthrough Network Load Balancer for Packet Mirroring, follow these steps.

###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Internal** and click **Next**.
  6. Click **Configure**.



#### Basic configuration

  1. For **Load balancer name** , enter a name.
  2. For **Region** , select the region of the VM instances where you want to mirror packets.
  3. For **Network** , select the network where you want to mirror packets.
  4. Click **Backend configuration**.
  5. In the **New Backend** section, for **Instance group** , select the instance group to forward packets to.
  6. In the **Health check** list, click **Create a health check** , and then enter the following information: 
     * In the **Name** field, enter a name for the health check.
     * In the **Protocol** list, select **HTTP**.
     * In the **Port** field, enter `80`.
  7. Click **Create**.
  8. Click **Frontend configuration**.
  9. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter a name.
     2. For **Subnetwork** , select a subnetwork in the same region as the instances to mirror.
     3. For **Ports** , select **All**.
     4. Click **Advanced configurations** and select the **Enable this load balancer for packet mirroring** checkbox.
     5. Click **Done**.
  10. Click **Create**.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to an instance group on port 80:
         
         gcloud compute health-checks create http HEALTH_CHECK_NAME \
             --region=REGION \
             --port=80
         

Replace the following:

     * `HEALTH_CHECK_NAME`: the name of the health check.
     * `REGION`: the region of the VM instances that you want to mirror packets for.
  2. Create a backend service for HTTP traffic:
         
         gcloud compute backend-services create COLLECTOR_BACKEND_SERVICE \
             --region=REGION \
             --health-checks-region=REGION \
             --health-checks=HEALTH_CHECK_NAME \
             --load-balancing-scheme=internal \
             --protocol=tcp
         

Replace the following:

     * `COLLECTOR_BACKEND_SERVICE`: the name of the backend service.
     * `REGION`: the region of the VM instances where you want to mirror packets.
     * `HEALTH_CHECK_NAME`: the name of the health check.
  3. Add an instance group to the backend service:
         
         gcloud compute backend-services add-backend COLLECTOR_BACKEND_SERVICE \
             --region=REGION \
             --instance-group=INSTANCE_GROUP \
             --instance-group-zone=ZONE
         

Replace the following:

     * `COLLECTOR_BACKEND_SERVICE`: the name of the backend service.
     * `REGION`: the region of the instance group.
     * `INSTANCE_GROUP`: the name of the instance group.
     * `ZONE`: the zone of the instance group.
  4. Create a forwarding rule for the backend service:
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
             --region=REGION \
             --network=NETWORK \
             --subnet=SUBNET \
             --backend-service=COLLECTOR_BACKEND_SERVICE \
             --load-balancing-scheme=internal \
             --ip-protocol=TCP \
             --ports=all \
             --is-mirroring-collector
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule.
     * `REGION`: the region for the forwarding rule.
     * `NETWORK`: the network for the forwarding rule.
     * `SUBNET`: a subnetwork in the region of the VMs where you want to mirror packets.
     * `COLLECTOR_BACKEND_SERVICE`: the backend service for this load balancer.



**Note:** You cannot use the `L3_DEFAULT` protocol in your forwarding rule to configure packet mirroring. 

## What's next

  * See [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal) for important fundamentals.
  * See [Failover concepts for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) for important information about failover.
  * See [Internal load balancing and DNS names](https://docs.cloud.google.com/load-balancing/docs/dns-names) for available DNS name options that your load balancer can use.
  * See [Configuring failover for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-failover) for configuration steps and an example internal passthrough Network Load Balancer failover configuration.
  * See [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring) for information about configuring Logging and Monitoring for internal passthrough Network Load Balancers.
  * See [Internal passthrough Network Load Balancers and connected networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks) for information about accessing internal passthrough Network Load Balancers from peer networks connected to your VPC network.
  * See [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb) for information about how to troubleshoot issues with your internal passthrough Network Load Balancer.
  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



## Appendix: IPv6 Bash script primer

This section provides a brief description of the different networking commands that are related to the Bash startup script that is used to install an IPv6 TCP server on the backend VMs. You don't need to run these steps again. They are only outlined here to provide context and aid understanding.

  1. Show all IPv6 routes.
         
         ip -6 route show table all
         

The output is as follows:
         
         fd20:307:120c:2000::/64 via fe80::57:2ff:fe36:ffbe dev ens4 proto ra metric 100 expires 62sec pref medium
         fe80::/64 dev ens4 proto kernel metric 256 pref medium
         default via fe80::57:2ff:fe36:ffbe dev ens4 proto ra metric 100 expires 62sec mtu 1460 pref medium
         local ::1 dev lo table local proto kernel metric 0 pref medium
         local fd20:307:120c:2000:0:b:: dev ens4 table local proto kernel metric 0 pref medium
         local fe80::56:24ff:feb1:59b3 dev ens4 table local proto kernel metric 0 pref medium
         multicast ff00::/8 dev ens4 table local proto kernel metric 256 pref medium
         

From the output of the previous step, identify the following:

     * Link-local IPv6 address (starting with fe80::/10): in the example output, the link local address is fe80::57:2ff:fe36:ffbe. This link-local address is used in the default route that is defined in routing table 1. This default route is created in step 2.
     * /64 subnet: this subnet is referenced in the source-based policy routing rule in step 3
  2. Add a custom default route in routing table 1.

The following command sends packets to the gateway using the network interface named `ens4`.
         
         sudo ip route add default via GATEWAY_ADDRESS dev ens4 table 1
         

After you run this command, a default route is added to a custom routing table (table 1), pointing to the gateway `fe80::57:2ff:fe36:ffbe` through the ens4 interface.

If you were to run the `ip -6 route show table all` command again, the output is as follows:
         
         default via fe80::57:2ff:fe36:ffbe dev ens4 table 1 metric 1024 pref medium
         fd20:307:120c:2000::/64 via fe80::57:2ff:fe36:ffbe dev ens4 proto ra metric 100 expires 89sec pref medium
         fe80::/64 dev ens4 proto kernel metric 256 pref medium
         default via fe80::57:2ff:fe36:ffbe dev ens4 proto ra metric 100 expires 89sec mtu 1460 pref medium
         local ::1 dev lo table local proto kernel metric 0 pref medium
         local fd20:307:120c:2000:0:1::/96 dev ens4 table local proto 66 metric 1024 pref medium
         local fd20:307:120c:2000:0:b:: dev ens4 table local proto kernel metric 0 pref medium
         local fe80::56:24ff:feb1:59b3 dev ens4 table local proto kernel metric 0 pref medium
         multicast ff00::/8 dev ens4 table local proto kernel metric 256 pref medium
         

  3. Add a source-based policy routing rule.

The following command adds a rule to route all outgoing packets originating from a specified subnet. If the source address matches the subnet, the system uses the default route defined in table 1 to forward the traffic.
         
         sudo ip -6 rule add from SUBNET_RANGE table 1
         

  4. To view the policy routing rules list, run the following command.
         
         ip -6 rule show
         

The output is as follows:
         
         0:      from all lookup local
         32765:  from fd20:307:120c:2000::/64 lookup 1
         32766:  from all lookup main
         

The line with `from fd20:... lookup 1` is the rule that you added—telling the kernel to use routing table 1 for traffic originating from that subnet.

  5. Allow the server to bind to a non-local IPv6 address—the VIP of the load balancer.
         
         sudo sysctl -w net.ipv6.ip_nonlocal_bind=1
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
