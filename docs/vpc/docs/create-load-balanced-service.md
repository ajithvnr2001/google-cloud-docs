---
url: https://docs.cloud.google.com/vpc/docs/create-load-balanced-service/
title: Create a load-balanced service \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:16.363020+00:00
---

# Create a load-balanced service  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-load-balanced-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback 

#  Create a load-balanced service Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how you, as a _service producer_ , can create a simple service that uses an internal passthrough Network Load Balancer. By default, an internal passthrough Network Load Balancer is available only from within the VPC network that hosts it.

This tutorial is intended for cloud architects, network architects, network administrators, and IT administrators.

## Objectives

  * Configure networking for the service producer resources
  * Create VM resources for the load balancer backend
  * Configure the load balancer components
  * Test accessing the load balancer



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing/pricing)
  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Create or select a project to use for the service producer resources. This project is referred to in the later tutorials as `PRODUCER_PROJECT`
     1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. Select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  3. Make sure that you have the following role or roles on the project: Compute Engine > Compute Network Admin, Compute Engine > Compute Security Admin, Compute Engine > Compute Instance Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Configure networking

The following sections explain how to create a network, a subnet, and firewall rules for the service.

### Configure a network and subnet

To create the service network and subnet for the load balancer, complete the steps in the following sections.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `service-network`.

  4. For **Subnet creation mode** , select **Custom**.

  5. In the **New subnet** section, enter the following information.

     1. For **Name** , enter `service-subnet`.
     2. For **Region** , select the region that you want to use.
     3. For **IP stack type** , select **IPv4 (single-stack)**.
     4. For **IPv4 range** , enter `10.10.10.0/24`.
     5. Click **Done**.
  6. Click **Create**.




###  gcloud 

  1. Create a custom mode VPC network:
         
         gcloud compute networks create service-network --subnet-mode=custom
         

  2. In the `service-network` network, create a subnet.
         
         gcloud compute networks subnets create service-subnet \
             --network=service-network \
             --range=10.10.10.0/24 \
             --region=REGION
         

Replace `REGION` with the region that you want to use.




### Configure firewall rules

Create firewall rules to allow the following traffic:

  * `fw-allow-subnet`: lets traffic from `10.10.10.0/24` reach other resources in `10.10.10.0/24`.
  * `fw-allow-ssh`: lets SSH traffic from `0.0.0.0/0` reach VMs that have the `allow-ssh` network tag.
  * `fw-allow-healthcheck`: lets traffic from the Google Cloud health checking systems reach VMs that have the `allow-healthcheck` network tag.




###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. To allow subnet traffic, click **Create firewall rule** and use the following settings:

     * For **Name** , enter `fw-allow-subnet`.
     * For **Network** , select `service-network`.
     * For **Priority** , enter `1000`.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Targets** , select **All instances in the network**.
     * For **Source filter** , select **IPv4 ranges**.
     * For **Source IPv4 ranges** , enter `10.10.10.0/24`.
     * For **Protocols and ports** , select **Allow all**.
  3. Click **Create**. 

  4. To allow incoming SSH connections, click **Create firewall rule** and use the following settings:

     * For **Name** , enter `fw-allow-ssh`.
     * For **Network** , select `service-network`.
     * For **Priority** , enter `1000`.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Targets** , select **Specified target tags**.
     * For **Target tags** , enter `allow-ssh`.
     * For **Source filter** , select **IPv4 ranges**.
     * For **Source IPv4 ranges** , enter `0.0.0.0/0`.
     * For **Protocols and ports** , select **Specified protocols and ports** , select the **TCP** checkbox. For **Ports** , enter `22`.
  5. Click **Create**. 

  6. To allow Google Cloud health checks, click **Create firewall rule** and use the following settings:

     * For **Name** , enter `fw-allow-healthcheck`.
     * For **Network** , select `service-network`.
     * For **Priority** , enter `1000`.
     * For **Direction of traffic** , select **Ingress**.
     * For **Action on match** , select **Allow**.
     * For **Targets** , select **Specified target tags**.
     * For **Target tags** , enter `allow-healthcheck`.
     * For **Source filter** , select **IPv4 ranges**.
     * For **Source IPv4 ranges** , enter `130.211.0.0/22` and `35.191.0.0/16`.
     * For **Protocols and ports** , select **Allow all**.
  7. Click **Create**. 




###  gcloud 

  1. Create the `fw-allow-subnet` firewall rule to allow communication from within the subnet:
         
         gcloud compute firewall-rules create fw-allow-subnet \
             --network=service-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=10.10.10.0/24 \
             --rules=tcp,udp,icmp
         




  1. Create the `fw-allow-ssh` firewall rule to allow SSH connectivity to VMs with the network tag `allow-ssh`.
         
         gcloud compute firewall-rules create fw-allow-ssh \
             --network=service-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=0.0.0.0/0 \
             --target-tags=allow-ssh \
             --rules=tcp:22
         




  1. Create the `fw-allow-healthcheck` rule to allow Google Cloud health checks.
         
         gcloud compute firewall-rules create fw-allow-healthcheck \
             --network=service-network \
             --action=allow \
             --direction=ingress \
             --target-tags=allow-healthcheck \
             --source-ranges=130.211.0.0/22,35.191.0.0/16 \
             --rules=tcp,udp,icmp
         




## Create VM resources for the load balancer backend

Create the VMs and the instance group to use with the load balancer.

### Create backend VMs

The service that you're creating runs on two VMs for higher availability: `vm-1` and `vm-2`. The VMs are in the same zone, but in a production environment, we recommend using multiple zones.

In addition to creating the VMs, following these steps accomplishes the following:

  * Configures the VMs to use the network tags that you configured as targets in the firewall rules and an additional network tag (`allow-nat`) that is used later.
  * Installs, configures, and starts the Apache service.




###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `vm-1`.

  4. For **Region** and **Zone** , select a region and a zone within that region.

  5. In the navigation menu, go to **OS and storage**.

  6. In the **Operating system and storage** pane, ensure that **Debian GNU/Linux 12 (bookworm)** is selected for the boot disk. If you need to select a different image, click **Change**.

  7. In the navigation menu, go to **Networking**.

  8. For **Network tags** , enter `allow-ssh`, `allow-healthcheck`, and `allow-nat`.

  9. For **Network interfaces** , select the following:

     * For **Network** , select `service-network`.
     * For **Subnet** , select `service-subnet`.
     * For **IP stack type** , select **IPv4 (single-stack)**.
     * For **Primary internal IPv4 address** , select **Ephemeral (automatic)**.
     * For **External IPv4 address** , select **Ephemeral**.
  10. In the navigation menu, go to **Advanced**.

  11. In the **Automation** section, in the **Startup script** field, enter the following script. 
         
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
         

  12. Click **Create**.

  13. Repeat these steps to create another VM named `vm-2` in the same region and zone as `vm-1`.




###  gcloud 

  1. Create two VMs by running the following commands:
         
         gcloud compute instances create vm-1 \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh,allow-healthcheck,allow-nat \
             --subnet=service-subnet \
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
         
         
         gcloud compute instances create vm-2 \
             --zone=ZONE \
             --image-family=debian-12 \
             --image-project=debian-cloud \
             --tags=allow-ssh,allow-healthcheck,allow-nati \
             --subnet=service-subnet \
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
         

Replace `ZONE` with the zone you want to use.




### Create an instance group

To use the VMs in a load balancer backend, you must add the VMs to an instance group.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**.

  3. In the navigation pane, click **New unmanaged instance group**.

  4. For **Name** , enter `ig-1`.

  5. In the **Location** section, select the same region and zone as your VMs.

  6. For **Network** , select **`service-network`**.

  7. For **Subnetwork** , select **`service-subnet`**.

  8. In the **VM instances** section, add `vm-1` and `vm-2` to the instance group.

  9. Click **Create**.




###  gcloud 

  1. Create an unmanaged instance group:
         
         gcloud compute instance-groups unmanaged create ig-1 \
             --zone=ZONE
         

Replace `ZONE` with the zone that contains the VMs.

  2. Add the VMs to the instance group:
         
         gcloud compute instance-groups unmanaged add-instances ig-1 \
             --zone=ZONE \
             --instances=vm-1,vm-2
         




## Configure load balancer components

Configure all of the internal passthrough Network Load Balancer components starting with the health check and backend service, and then the frontend components:

  * **Health check**. You use an HTTP health check that checks for an HTTP `200 OK` status code.

  * **Backend service**. Because you need to pass HTTP traffic through the internal load balancer, you need to use TCP, not UDP.

  * **Forwarding rule**. You create a single internal forwarding rule, `service-rule`.

  * **Internal IP address**. You specify an internal IP address, `10.10.10.99`, when you create the forwarding rule.




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

  * For **Load balancer name** , enter `service-lb`.
  * For **Region** , select the same region as your VMs.
  * For **Network** , select `service-network`.



#### Configure the backends

  1. Click **Backend configuration**.
  2. In the **Health check** list, click **Create a health check** , and enter the following information: 
     * For **Name:** , enter `hc-http-80`.
     * For **Protocol:** , select `HTTP`.
     * For **Port:** , enter `80`.
     * For **Proxy protocol:** , select `NONE`.
     * For **Request path:** , enter `/`.
  3. Click **Create**.
  4. In the **New Backend** section of **Backends** , select **IPv4 (single-stack)**.
  5. In **Instance group** , select the `ig-1` instance group and click **Done**.
  6. Verify that there is a blue check mark next to **Backend configuration** before continuing.



#### Configure the frontend

  1. Click **Frontend configuration**.
  2. In the **New Frontend IP and port** section, do the following: 
     1. For **Name** , enter `service-rule`.
     2. For **Subnetwork** , select `service-subnet`.
     3. In the **Internal IP purpose** section, in the **IP address** list, select **Create IP address** , enter the following information: 
        * For **Name** , enter `service-rule-ip`.
        * For **IP version** , select **IPv4**.
        * For **Static IP address** , select **Let me choose**.
        * For **Custom IP address** , enter `10.10.10.99`.
     4. Click **Reserve**.
     5. For **Ports** , select **Single** and then in **Port numbers** , enter `80`.
     6. Click **Done**.
     7. Verify that there is a blue check mark next to **Frontend configuration** before continuing.



#### Review the configuration

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Click **Create**.



###  gcloud 

  1. Create a new regional HTTP health check to test HTTP connectivity to the VMs on port 80.
         
         gcloud compute health-checks create http hc-http-80 \
             --region=REGION \
             --port=80
         

Replace `REGION` with the same region as the backend VMs.

  2. Create the backend service for HTTP traffic:
         
         gcloud compute backend-services create service-lb \
             --load-balancing-scheme=internal \
             --protocol=tcp \
             --region=REGION \
             --health-checks=hc-http-80 \
             --health-checks-region=REGION
         

Replace `REGION` with the same region as the backend VMs.

  3. Add the instance group to the backend service:
         
         gcloud compute backend-services add-backend service-lb \
             --region=REGION \
             --instance-group=ig-1 \
             --instance-group-zone=ZONE
         

Replace the following:

     * `REGION`: the same region as the backend VMs.
     * `ZONE`: the same zone as the backend VMs.
  4. Create a forwarding rule for the backend service:
         
         gcloud compute forwarding-rules create service-rule \
             --region=REGION \
             --load-balancing-scheme=internal \
             --network=service-network \
             --subnet=service-subnet \
             --address=10.10.10.99 \
             --ip-protocol=TCP \
             --ports=80 \
             --backend-service=service-lb \
             --backend-service-region=REGION
         

Replace `REGION` with the same region as the backend VMs.




## Test accessing the load balancer

To test that the load balancer is working, create a test VM and send a request from it to the load balancer.

### Create a client VM for testing

Create a client VM in the same region as the backend (server) VMs.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. For **Name** , enter `producer-test`.

  4. For **Region** , select the same region as the backend VMs.

  5. For **Zone** , select a zone in that region.

  6. Click **Networking** and configure the following fields:

     1. For **Network tags** , enter `allow-ssh`.
     2. For **Network interfaces** , select the following: 
        * For **Network** , select `service-network`
        * For **Subnet** , select `service-subnet`
  7. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create producer-test \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=allow-ssh \
        --subnet=service-subnet
    

Replace `ZONE` with a zone that's in the same region as the backend VMs.

### Test connectivity

This test contacts the load balancer from a client VM. The expected behavior is for traffic to be distributed across the load balancer's backend VMs.

  1. Connect to the client VM instance. 
         
         gcloud compute ssh producer-test --zone=ZONE
         

Replace `ZONE` with the zone of the client VM.
  2. Make a web request to the load balancer using `curl` to contact its IP address. Repeat the request so you can see that responses come from different backend VMs. The name of the VM generating the response is displayed in the text in the HTML response, because of the contents of `/var/www/html/index.html` on each backend VM. For example, expected responses look like `Page served from: vm-1` and `Page served from: vm-2`. 
         
         curl -s http://10.10.10.99
         




## What's next

  * [Make the service accessible from other VPC networks](https://docs.cloud.google.com/vpc/docs/make-service-accessible-other-vpc-networks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
