---
url: https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp/
title: Set up a classic proxy Network Load Balancer (TCP proxy) with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:28.676633+00:00
---

# Set up a classic proxy Network Load Balancer (TCP proxy) with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a classic proxy Network Load Balancer (TCP proxy) with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud classic proxy Network Load Balancers let you use a single IP address for all users around the world. Classic proxy Network Load Balancers automatically route traffic to backend instances that are closest to the user.

This page contains instructions for setting up a classic proxy Network Load Balancer with a target TCP proxy and VM instance group backends. Before you start, read the [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp) for detailed information about how these load balancers work.

## Setup overview

This example demonstrates how to set up an external proxy Network Load Balancer for a service that exists in two regions: Region A and Region B. For purposes of the example, the service is a set of [Apache](https://httpd.apache.org/) servers configured to respond on port `110`. Many browsers don't allow port `110`, so the testing section uses `curl`.

In this example, you configure the following:

  1. Four instances distributed between two regions
  2. Instance groups, which contain the instances
  3. A health check for verifying instance health
  4. A backend service, which monitors the instances and prevents them from exceeding configured usage
  5. The target TCP proxy
  6. An external static IPv4 address and forwarding rule that sends user traffic to the proxy
  7. An external static IPv6 address and forwarding rule that sends user traffic to the proxy
  8. A firewall rule that allows traffic from the load balancer and health checker to reach the instances



After the load balancer is configured, you test the configuration.

## Permissions

To follow this guide, you must be able to create instances and modify a network in a project. You must be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic), or you must have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required Role  
---|---  
Create networks, subnets, and load balancer components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Configure instance group backends

This section shows how to create basic instance groups, add instances to them, and then add those instances to a backend service with a health check. A production system would normally use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) based on [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates), but this configuration is quicker for initial testing.

### Configure instances

For testing purposes, install Apache on four instances, two in each of two instance groups. Typically, external proxy Network Load Balancers aren't used for HTTP traffic, but Apache software is commonly used for testing.

In this example, the instances are created with the tag `tcp-lb`. This tag is used later by the firewall rule.

###  Console 

**Create instances**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set **Name** to `vm-a1`.

  4. Set the **Region** to `REGION_A`.

  5. Set the **Zone** to `ZONE_A`.

  6. Click **Advanced options**.

  7. Click **Networking** and configure the following field:

     * For **Network tags** , enter `tcp-lb`,`allow-health-check-ipv6`. 


* Click **Management**. Enter the following script into the **Startup script** field.
    
    
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>vm-a1</h1></body></html>' | sudo tee /var/www/html/index.html

* Click **Create**.

* Create `vm-a2` with the same settings, except with the following script in the **Startup script** field: 
    
    
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>vm-a2</h1></body></html>' | sudo tee /var/www/html/index.html

* Create `vm-b1` with the same settings, except with **Region** set to `REGION_B` and **Zone** set to `ZONE_B`. Enter the following script in the **Startup script** field: 
    
    
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>vm-b1</h1></body></html>' | sudo tee /var/www/html/index.html

* Create `vm-b2` with the same settings, except with **Region** set to `REGION_B` and **Zone** set to `ZONE_B`. Enter the following script in the **Startup script** field: 
    
    
    sudo apt-get update
    sudo apt-get install apache2 -y
    sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
    sudo service apache2 restart
    echo '<!doctype html><html><body><h1>vm-b2</h1></body></html>' | sudo tee /var/www/html/index.html

###  gcloud 

  1. Create `vm-a1` in zone `ZONE_A`
         
         gcloud compute instances create vm-a1 \
            --image-family debian-12 \
            --image-project debian-cloud \
            --tags tcp-lb \
            --zone ZONE_A \
            --metadata startup-script="#! /bin/bash
              sudo apt-get update
              sudo apt-get install apache2 -y
              sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
              sudo service apache2 restart
              echo '<!doctype html><html><body><h1>vm-a1</h1></body></html>' | tee /var/www/html/index.html
              EOF"
         

  2. Create `vm-a2` in zone `ZONE_A`
         
         gcloud compute instances create vm-a2 \
            --image-family debian-12 \
            --image-project debian-cloud \
            --tags tcp-lb \
            --zone ZONE_A \
            --metadata startup-script="#! /bin/bash
              sudo apt-get update
              sudo apt-get install apache2 -y
              sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
              sudo service apache2 restart
              echo '<!doctype html><html><body><h1>vm-a2</h1></body></html>' | tee /var/www/html/index.html
              EOF"
         

  3. Create `vm-b1` in zone `ZONE_B`
         
         gcloud compute instances create vm-b1 \
            --image-family debian-12 \
            --image-project debian-cloud \
            --tags tcp-lb \
            --zone ZONE_B \
            --metadata startup-script="#! /bin/bash
              sudo apt-get update
              sudo apt-get install apache2 -y
              sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
              sudo service apache2 restart
              echo '<!doctype html><html><body><h1>vm-b1</h1></body></html>' | tee /var/www/html/index.html
              EOF"
         

  4. Create `vm-b2` in zone `ZONE_B`
         
         gcloud compute instances create vm-b2 \
            --image-family debian-12 \
            --image-project debian-cloud \
            --tags tcp-lb \
            --zone ZONE_B \
            --metadata startup-script="#! /bin/bash
              sudo apt-get update
              sudo apt-get install apache2 -y
              sudo sed -i '/Listen 80/c\Listen 110' /etc/apache2/ports.conf
              sudo service apache2 restart
              echo '<!doctype html><html><body><h1>vm-b2</h1></body></html>' | tee /var/www/html/index.html
              EOF"
         




### Create instance groups

In this section you create an instance group in each zone and add the instances.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**.

  3. Click **New unmanaged instance group**.

  4. Set the **Name** to `instance-group-a`.

  5. Set the **Zone** to `ZONE_A`.

  6. Under **Port mapping** , click **Add port**. A load balancer sends traffic to an instance group through a [named port](https://docs.cloud.google.com/load-balancing/docs/backend-service#named_ports). Create a named port to map the incoming traffic to a specific port number.

     1. Set **Port name** to `tcp110`.
     2. Set **Port numbers** to `110`.
  7. Under **VM instances** , select `vm-a1` and `vm-a2`.

  8. Leave the other settings as they are.

  9. Click **Create**.

  10. Repeat the steps, but set the following values:

     * **Name** : `instance-group-b`
     * **Region** : `REGION_B`
     * **Zone** : `ZONE_B`
     * **Port name** : `tcp110`
     * **Port numbers** : `110`
     * **Instances** : **vm-b1** and **vm-b2**.



###  gcloud 

  1. Create the `instance-group-a` instance group.
         
         gcloud compute instance-groups unmanaged create instance-group-a \
            --zone ZONE_A
         

  2. Create a named port for the instance group.
         
         gcloud compute instance-groups set-named-ports instance-group-a \
            --named-ports tcp110:110 \
            --zone ZONE_A
         

  3. Add `vm-a1` and `vm-a2` to `instance-group-a`.
         
         gcloud compute instance-groups unmanaged add-instances instance-group-a \
            --instances vm-a1,vm-a2 \
            --zone ZONE_A
         

  4. Create the `us-ig2` instance group.
         
         gcloud compute instance-groups unmanaged create instance-group-b \
            --zone ZONE_B
         

  5. Create a named port for the instance group.
         
         gcloud compute instance-groups set-named-ports instance-group-b \
            --named-ports tcp110:110 \
            --zone ZONE_B
         

  6. Add `vm-b1` and `vm-b2` to instance-group-b
         
         gcloud compute instance-groups unmanaged add-instances instance-group-b \
            --instances vm-b1,vm-b2 \
            --zone ZONE_B
         




You now have one instance group per region. Each instance group has two VM instances.

## Create a firewall rule for the external proxy Network Load Balancer

Configure the firewall to allow traffic from the load balancer and health checker to the instances. In this case, we will open TCP port 110. The health check will use the same port. Since the traffic between the load balancer and your instances uses IPv4, only IPv4 ranges need be opened.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule**.

  3. In the **Name** field, enter `allow-tcp-lb-and-health`.

  4. Select a network.

  5. Under **Targets** , select **Specified target tags**.

  6. Set **Target tags** to `tcp-lb`.

  7. Set **Source filter** to **IPv4 ranges**.

  8. Set **Source IPv4 ranges** to `130.211.0.0/22`,`35.191.0.0/16`.

  9. Under **Protocols and ports** , set **Specified protocols and ports** to `tcp:110`.

  10. Click **Create**.




###  gcloud 
    
    
    gcloud compute firewall-rules create allow-tcp-lb-and-health \
       --source-ranges 130.211.0.0/22,35.191.0.0/16 \
       --target-tags tcp-lb \
       --allow tcp:110
    

## Configure the load balancer

### Console

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Proxy load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  6. For **Global or single region deployment** , select **Best for global workloads** and click **Next**.
  7. For **Load balancer generation** , select **Classic proxy Network Load Balancer** and click **Next**.
  8. Click **Configure**.



**Basic configuration**

Set the **Name** to `my-tcp-lb`.

**Backend configuration**

  1. Click **Backend configuration**.
  2. In the **Backend type** list, select **Instance groups**.
  3. In the **Protocol** list, select **TCP**.
  4. Configure the health check: 
     * In the **Health check** list, select **Create health check**.
     * In the **Name** field, enter `my-tcp-health-check`.
     * In the **Protocol** list, select **TCP**.
     * In the **Port** field, enter `110`.
     * Retain the remaining default values.
     * Click **Create**.
  5. Configure the first backend: 
     1. Under **New backend** , select instance group `instance-group-a`.
     2. Retain the remaining default values.
  6. Configure the second backend: 
     1. Click **Add backend**.
     2. Select instance group `instance-group-b`.
     3. Under **Port numbers** , delete `80` and add `110`.
  7. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.



**Frontend configuration**

  1. Click **Frontend configuration**.
  2. Add the first forwarding rule: 
     1. Enter a **Name** of `my-tcp-lb-forwarding-rule`.
     2. Under **Protocol** , select **TCP**.
     3. Under **IP address** , select **Create IP address** : 
        1. Enter a **Name** of `tcp-lb-static-ip`.
        2. Click **Reserve**.
     4. Set **Port** to `110`.
     5. In this example, don't enable the **Proxy Protocol** because it doesn't work with the Apache HTTP Server software. For more information, see Proxy protocol.
     6. Click **Done**.
  3. Add the second forwarding rule: 
     1. Click **Add frontend IP and port**.
     2. Enter a **Name** of `my-tcp-lb-ipv6-forwarding-rule`.
     3. Under **Protocol** , select **TCP**.
     4. Set **IP version** to `IPv6`.
     5. Under **IP address** , click **Create IP address**. 
        1. Enter a name of `tcp-lb-ipv6-static-ip`.
        2. Click **Reserve**.
     6. Set **Port** to `110`.
     7. In this example, don't enable the **Proxy Protocol** because it doesn't work with the Apache HTTP Server software. For more information, see Proxy protocol.
     8. Click **Done**.
  4. In the Google Cloud console, verify that there is a check mark next to **Frontend configuration**. If not, double-check that you have completed all the previous steps.




**Review and finalize**

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.



### gcloud

  1. Create a health check. 
         
         gcloud compute health-checks create tcp my-tcp-health-check --port 110
             

  2. Create a backend service. 
         
         gcloud compute backend-services create my-tcp-lb \
                 --load-balancing-scheme EXTERNAL \
                 --global-health-checks \
                 --global \
                 --protocol TCP \
                 --health-checks my-tcp-health-check \
                 --timeout 5m \
                 --port-name tcp110
             

  3. Add instance groups to your backend service. 
         
         gcloud compute backend-services add-backend my-tcp-lb \
                 --global \
                 --instance-group instance-group-a \
                 --instance-group-zone ZONE_A \
                 --balancing-mode UTILIZATION \
                 --max-utilization 0.8
             
         
         gcloud compute backend-services add-backend my-tcp-lb \
                 --global \
                 --instance-group instance-group-b \
                 --instance-group-zone ZONE_B \
                 --balancing-mode UTILIZATION \
                 --max-utilization 0.8
             

  4. Configure a target TCP proxy. If you want to turn on the proxy header, set it to `PROXY_V1` instead of `NONE`. 
         
         gcloud compute target-tcp-proxies create my-tcp-lb-target-proxy \
                 --backend-service my-tcp-lb \
                 --proxy-header NONE
             

  5. Reserve global static IPv4 and IPv6 addresses. 

Your customers can use these IP addresses to reach your load balanced service.
         
         gcloud compute addresses create tcp-lb-static-ipv4 \
                 --ip-version=IPV4 \
                 --global
             
         
         gcloud compute addresses create tcp-lb-static-ipv6 \
                 --ip-version=IPV6 \
                 --global
             

  6. Configure global forwarding rules for the two addresses. 
         
         gcloud compute forwarding-rules create my-tcp-lb-ipv4-forwarding-rule \
                 --load-balancing-scheme EXTERNAL \
                 --global \
                 --target-tcp-proxy my-tcp-lb-target-proxy \
                 --address tcp-lb-static-ipv4 \
                 --ports 110
             
         
         gcloud compute forwarding-rules create my-tcp-lb-ipv6-forwarding-rule \
                 --load-balancing-scheme EXTERNAL \
                 --global \
                 --target-tcp-proxy my-tcp-lb-target-proxy \
                 --address tcp-lb-static-ipv6 \
                 --ports 110
             




## Test the load balancer

  1. Get the load balancer's IP address.

To get the IPv4 address, run the following command:
         
         gcloud compute addresses describe tcp-lb-static-ipv4
         

To get the IPv6 address, run the following command:
         
         gcloud compute addresses describe tcp-lb-static-ipv6
         

  2. Send traffic to your load balancer by running the following command. Replace `LB_IP_ADDRESS` with your load balancer's IPv4 or IPv6 address.
         
         curl -m1 LB_IP_ADDRESS:110
         

For example, if the assigned IPv6 address is `[2001:db8:1:1:1:1:1:1/96]:110`, the command should look like:
         
         curl -m1 http://[2001:db8:1:1:1:1:1:1]:110
         




If you can't reach the load balancer, try the steps described under Troubleshooting your setup.

## Additional configuration options

This section expands on the configuration example to provide alternative and additional configuration options. All of the tasks are optional. You can perform them in any order.

### PROXY protocol for retaining client connection information

The proxy Network Load Balancer ends TCP connections from the client and creates new connections to the instances. By default, the original client IP and port information is not preserved.

To preserve and send the original connection information to your instances, enable [PROXY protocol version 1](http://www.haproxy.org/download/1.5/doc/proxy-protocol.txt). This protocol sends an additional header that contains the source IP address, destination IP address, and port numbers to the instance as a part of the request.

Make sure that the proxy Network Load Balancer's backend instances are running servers that support PROXY protocol headers. If the servers are not configured to support PROXY protocol headers, the backend instances return empty responses.

If you set the PROXY protocol for user traffic, you can also set it for your health checks. If you are checking health and serving content on the same port, set the health check's `--proxy-header` to match your load balancer setting.

The PROXY protocol header is typically a single line of user-readable text in the following format:
    
    
    PROXY TCP4 <client IP> <load balancing IP> <source port> <dest port>\r\n
    

The following example shows a PROXY protocol:
    
    
    PROXY TCP4 192.0.2.1 198.51.100.1 15221 110\r\n

In the preceding example, the client IP is `192.0.2.1`, the load balancing IP is `198.51.100.1`, the client port is `15221`, and the destination port is `110`.

When the client IP is not known, the load balancer generates a PROXY protocol header in the following format:
    
    
    PROXY UNKNOWN\r\n
    

#### Update PROXY protocol header for target proxy

The example load balancer setup on this page shows you how to enable the PROXY protocol header while creating the proxy Network Load Balancer. Use these steps to change the PROXY protocol header for an existing target proxy.

### Console

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click edit**Edit** for your load balancer.
  3. Click **Frontend configuration**.
  4. Change the value of the **Proxy protocol** field to **On**.
  5. Click **Update** to save your changes.



### gcloud

In the following command, edit the `--proxy-header` field and set it to either `NONE` or `PROXY_V1` depending on your requirement.
    
    
    gcloud compute target-tcp-proxies update TARGET_PROXY_NAME \
        --proxy-header=[NONE | PROXY_V1]
    

### Configure session affinity

The example configuration creates a backend service without session affinity.

These procedures show you how to update a backend service for the example load balancer so that the backend service uses client IP affinity or generated cookie affinity.

When client IP affinity is enabled, the load balancer directs a particular client's requests to the same backend VM based on a hash created from the client's IP address and the load balancer's IP address (the external IP address of an external forwarding rule).

###  Console

To enable client IP session affinity:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click **Backends**.

  3. Click **my-tcp-lb** (the name of the backend service you created for this example) and click **Edit**.

  4. On the **Backend service details** page, click **Advanced configuration**.

  5. Under **Session affinity** , select **Client IP** from the menu.

  6. Click **Update**.




###  gcloud 

Use the following Google Cloud CLI command to update the `my-tcp-lb` backend service, specifying client IP session affinity:
    
    
    gcloud compute backend-services update my-tcp-lb \
        --global \
        --session-affinity=CLIENT_IP
    

###  API

To set client IP session affinity, make a `PATCH` request to the [`backendServices/patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch) method.
    
    
    PATCH https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/global/us-west1/backendServices/my-tcp-lb
    {
      "sessionAffinity": "CLIENT_IP"
    }
    

### Enable connection draining

You can enable connection draining on backend services to ensure minimal interruption to your users when an instance that is serving traffic is terminated, removed manually, or removed by an autoscaler. To learn more about connection draining, read the [Enabling connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) documentation.

## What's next

  * [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp)
  * [Proxy Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring)
  * [Clean up a load balancing setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
