---
url: https://docs.cloud.google.com/load-balancing/docs/network/networklb-setting-up-failover/
title: Configure failover for regional external passthrough Network Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:46.357173+00:00
---

# Configure failover for regional external passthrough Network Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/networklb-setting-up-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Configure failover for regional external passthrough Network Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes how failover works for backend service-based regional external passthrough Network Load Balancers. It does not apply to regional external passthrough Network Load Balancers with a target pool backend.

This guide uses an example to teach you how to configure failover for a regional external passthrough Network Load Balancer with a backend service. Before following this guide, familiarize yourself with the following:

  * [Regional external passthrough Network Load Balancer with a backend service overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Traffic distribution for backend service-based regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution)
  * [Firewall rules overview](https://docs.cloud.google.com/vpc/docs/firewalls)
  * [Health check concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts)



## Permissions

To follow this guide, you need to create instances and modify a network in a project. You should be either a project [owner or editor](https://docs.cloud.google.com/iam/docs/understanding-roles#primitive_roles), or you should have all of the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

Task | Required Role  
---|---  
Create load balancer components | [Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)  
Add and remove firewall rules | [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
Create instances | [Compute Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin)  
  
For more information, see the following guides:

  * [Access control](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Setup

This guide shows you how to configure and test a regional external passthrough Network Load Balancer that uses failover. The steps in this section describe how to configure the following:

  1. Backend VMs: 
     * One primary backend in an unmanaged instance group in zone `us-west1-a`
     * One failover backend in an unmanaged instance group in zone `us-west1-c`
  2. Firewall rules that allow incoming connections to backend VMs
  3. One client VM to test connections and observe failover behavior
  4. The following regional external passthrough Network Load Balancer components: 
     * A health check for the backend service
     * A backend service in the `us-west1` region to manage connection distribution among the backend VMs
     * A forwarding rule and IP address for the frontend of the load balancer



The architecture for this example looks like this:

[ ![Failover with a regional external passthrough Network Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/netlb-failover.svg)](https://docs.cloud.google.com/static/load-balancing/images/netlb-failover.svg) Failover with a regional external passthrough Network Load Balancer (click to enlarge).**Note:** Unmanaged instance groups are used for both the primary and failover backends in this example.

### Creating backend VMs and instance groups

In this step, you'll create the backend VMs and unmanaged instance groups:

  * The instance group `ig-a` in `us-west1-a` is a primary backend with two VMs: 
    * `vm-a1`
    * `vm-a2`
  * The instance group `ig-c` in `us-west1-c` is a failover backend with two VMs: 
    * `vm-c1`
    * `vm-c2`



The primary and failover backends are placed in separate zones for instructional clarity and to handle failover in case one zone goes down.

Each primary and failover VM is configured to run an Apache web server on TCP port 80. By default, Apache is configured to bind to any IP address. Network load balancers deliver packets by preserving the destination IP.

Ensure that server software running on your primary and failover VMs listens on the IP address of the load balancer's forwarding rule. The destination IP address of a packet delivered to a backend VM by a regional external passthrough Network Load Balancer is the IP address of the forwarding rule.

For instructional simplicity, all primary and failover VMs run Debian GNU/Linux 9.

###  Console 

**Create backend VMs**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat the following steps to create four VMs, using the following name and zone combinations.

     * Name: `vm-a1`, zone: `us-west1-a`
     * Name: `vm-a2`, zone: `us-west1-a`
     * Name: `vm-c1`, zone: `us-west1-c`
     * Name: `vm-c2`, zone: `us-west1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated in step 2.

  5. For the **Region** , choose `us-west1`, and choose a **Zone** as indicated in step 2.

  6. In the **Boot disk** section, ensure that the selected image is **Debian GNU/Linux 12 (bookworm)**. Click **Choose** to change the image if necessary.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following field:

     1. For **Network tags** , enter `network-lb`.
  9. Click **Management**. Enter the following script into the **Startup script** field. The script contents are identical for all four VMs:
         
         #! /bin/bash
         apt-get update
         apt-get install apache2 -y
         a2ensite default-ssl
         a2enmod ssl
         vm_hostname="$(curl -H "Metadata-Flavor:Google" \
         http://metadata.google.internal/computeMetadata/v1/instance/name)"
         echo "Page served from: $vm_hostname" | \
         tee /var/www/html/index.html
         systemctl restart apache2
         

  10. Click **Create**.




**Create instance groups**

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Repeat the following steps to create two unmanaged instance groups each with two VMs in them, using these combinations.

     * Instance group: `ig-a`, zone: `us-west1-a`, VMs: `vm-a1` and `vm-a2`
     * Instance group: `ig-c`, zone: `us-west1-c`, VMs: `vm-c1` and `vm-c2`
  3. Click **Create instance group**.

  4. Click **New unmanaged instance group**.

  5. Set **Name** as indicated in step 2.

  6. In the **Location** section, choose `us-west1` for the **Region** , and then choose a **Zone** as indicated in step 2.

  7. For **Network** , enter `default`.

  8. In the **VM instances** section, add the VMs as indicated in step 2.

  9. Click **Create**.




###  gcloud 

  1. Create four VMs by running the following command four times, using these four combinations for `VM-NAME` and `ZONE`. The script contents are identical for all four VMs.

     * `VM-NAME` of `vm-a1` and `ZONE` of `us-west1-a`
     * `VM-NAME` of `vm-a2` and `ZONE` of `us-west1-a`
     * `VM-NAME` of `vm-c1` and `ZONE` of `us-west1-c`
     * `VM-NAME` of `vm-c2` and `ZONE` of `us-west1-c`
    
    gcloud compute instances create VM-NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=network-lb \
        --metadata=startup-script='#! /bin/bash
          apt-get update
          apt-get install apache2 -y
          a2ensite default-ssl
          a2enmod ssl
          vm_hostname="$(curl -H "Metadata-Flavor:Google" \
          http://metadata.google.internal/computeMetadata/v1/instance/name)"
          echo "Page served from: $vm_hostname" | \
          tee /var/www/html/index.html
          systemctl restart apache2'
    

  2. Create the two unmanaged instance groups in each zone:
         
         gcloud compute instance-groups unmanaged create ig-a \
             --zone us-west1-a
         gcloud compute instance-groups unmanaged create ig-c \
             --zone us-west1-c
         

  3. Add the VMs to the appropriate instance groups:
         
         gcloud compute instance-groups unmanaged add-instances ig-a \
             --zone us-west1-a \
             --instances vm-a1,vm-a2
         gcloud compute instance-groups unmanaged add-instances ig-c \
             --zone us-west1-c \
             --instances vm-c1,vm-c2
         




### Configuring firewall rules

Create a firewall rule that allows external traffic to reach the backend instances.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule** to create the rule to allow traffic from any source. Use the following values:

     1. **Name** : `allow-network-lb`.
     2. **Network** :`default`
     3. **Priority** : `1000`
     4. **Direction of traffic** : Ingress
     5. **Action on match** : Allow.
     6. **Targets** : Specified target tags
     7. **Target tags** : `network-lb`
     8. **Source filter** : **IPv4 ranges**
     9. **Source IPv4 ranges** : `0.0.0.0/0`, which allows traffic from any source. This allows both external traffic and health check probes to reach the backend instances.
     10. **Protocols and ports** : Choose **Specified protocols and ports**. Select the **TCP** checkbox and enter `80`.
  3. Click **Create**.

  4. Click **Create firewall rule** again to create the rule to allow incoming SSH connections to the instances. Use the following values:

     1. **Name** : `allow-ssh`
     2. **Network** : `default`
     3. **Priority** : `1000`
     4. **Direction of traffic** : Ingress
     5. **Action on match** : Allow
     6. **Targets** : Specified target tags
     7. **Target tags** : `network-lb`
     8. **Source filter** : **IPv4 ranges**
     9. **Source IPv4 ranges** : `0.0.0.0/0`
     10. **Protocols and ports** : Choose **Specified protocols and ports**. Select the **TCP** checkbox and enter `22`.
  5. Click **Create**.




###  gcloud 
    
    
    gcloud compute firewall-rules create allow-network-lb \
        --target-tags network-lb \
        --allow tcp:80
    
    
    
    gcloud compute firewall-rules create allow-ssh \
        --target-tags network-lb \
        --allow tcp:22
    

### Configuring load balancer components

These steps configure the following regional external passthrough Network Load Balancer components:

  * **Health check**. This example uses an HTTP health check that checks for an HTTP `200 OK` status code.

  * **Backend service**. Because the example passes HTTP traffic through the load balancer, the configuration specifies TCP, not UDP. To illustrate failover, this backend service has a failover ratio of `0.75`.

  * **Forwarding rule**. This example creates a single forwarding rule.




###  Console 

#### Start your configuration

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click **Create load balancer**.
  3. For **Type of load balancer** , select **Network Load Balancer (TCP/UDP/SSL)** and click **Next**.
  4. For **Proxy or passthrough** , select **Passthrough load balancer** and click **Next**.
  5. For **Public facing or internal** , select **Public facing (external)** and click **Next**.
  6. Click **Configure**.



#### Backend configuration

  1. On the **Create external passthrough Network Load Balancer** page, in the **Load Balancer name** field, enter `tcp-network-lb`.
  2. In the **Region** list, select **us-west1**.
  3. Click **Backend configuration**. The load balancer **Name** you entered previously appears, but is not modifiable.
  4. Click **Backend configuration** and do the following: 
     1. In the **Health check** list, click **Create a health check** , and then enter the following information: 
        * **Name** : `hc-http-80`
        * **Protocol** : **TCP**
        * **Port** : `80`
     2. Click **Create**.
     3. In the **Backends** section, in the **Instance group** list, select `ig-a`.
     4. Click **Add backend** and repeat this step to add `ig-c`.
     5. Select the **Use this instance group as a failover group for backup** checkbox.
     6. Click **Save and continue**.
     7. Click **Advanced configurations**.
     8. For **Failover Ratio** , enter `0.75`.
     9. Verify that there is a blue check mark next to **Backend configuration** before continuing.



#### Frontend configuration

  1. Click **Frontend configuration**.
  2. Enter a **Name** of `network-lb-forwarding-rule`.
  3. Under **IP** , click the drop-down menu and select **Create IP address**. 
     1. On the **Reserve a new static IP address** screen, assign a **Name** of `network-lb-ip`.
     2. Click **Reserve**.
  4. Choose **Single** , and enter `80` for the **Port number**.
  5. Click the **Done** button.

A blue circle with a checkmark to the left of **Frontend configuration** indicates a successful set-up.




#### Review the configuration

  1. Click the **Review and finalize** button to check all of your configuration settings for the load balancer.
  2. If the settings are correct, click **Create**. It takes a few minutes for the load balancer to be created.

On the load balancing screen, under the Backend column for your new load balancer, you should see a green checkmark showing that the new load balancer is healthy.




###  gcloud 

  1. Create a static external IP address for your load balancer.
         
         gcloud compute addresses create network-lb-ip \
             --region us-west1
         

  2. Create a new HTTP health check to test TCP connectivity to the VMs on 80.
         
         gcloud compute health-checks create http hc-http-80 \
             --region us-west1 \
             --port 80
         

  3. Create the backend service for HTTP traffic:
         
         gcloud compute backend-services create network-lb-backend-service \
             --protocol tcp \
             --region us-west1 \
             --health-checks hc-http-80 \
             --health-checks-region us-west1 \
             --failover-ratio 0.75
         

  4. Add the primary backend to the backend service:
         
         gcloud compute backend-services add-backend network-lb-backend-service \
             --region us-west1 \
             --instance-group ig-a \
             --instance-group-zone us-west1-a
         

  5. Add the failover backend to the backend service:
         
         gcloud compute backend-services add-backend network-lb-backend-service \
             --region us-west1 \
             --instance-group ig-c \
             --instance-group-zone us-west1-c \
             --failover
         

  6. Create a forwarding rule for the backend service. Use the IP address reserved in step 1 as the static external IP address of the load balancer.
         
         gcloud compute forwarding-rules create network-lb-forwarding-rule \
             --region us-west1 \
             --load-balancing-scheme external \
             --address network-lb-ip\
             --ports 80 \
             --backend-service network-lb-backend-service
         




## Testing

These tests show how to validate your load balancer configuration and learn about its expected behavior.

### Send traffic to the load balancer

This procedure sends external traffic to the load balancer. You'll use this procedure to complete the other tests.

  1. Connect to the client VM instance.
         
         gcloud compute forwarding-rules describe network-lb-forwarding-rule \
             --region us-west1
         

  2. Make a web request to the load balancer using `curl` to contact its IP address.
         
         curl http://IP_ADDRESS
         

  3. Note the text returned by the `curl` command. The name of the backend VM generating the response is displayed in that text; for example: `Page served from: vm-a1`




### Testing initial state

After you've configured the example load balancer, all four of the backend VMs should be healthy:

  * the two primary VMs, `vm-a1` and `vm-a2`
  * the two failover VMs, `vm-c1` and `vm-c2`



Follow the test procedure to send traffic to the load balancer. Repeat the second step a few times. The expected behavior is for traffic to be served by the two primary VMs, `vm-a1` and `vm-a2`, because both of them are healthy. You should see each primary VM serve a response approximately half of the time [because no session affinity has been configured](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#traffic-distribution) for this load balancer.

### Testing failover

This test simulates the failure of `vm-a1` so you can observe failover behavior.

  1. Connect to the `vm-a1` VM.
         
         gcloud compute ssh vm-a1 --zone us-west1-a
         

  2. Stop the Apache web server. After ten seconds, Google Cloud considers this VM to be unhealthy. (The `hc-http-80` health check that you created in the setup uses the default check interval of five seconds and unhealthy threshold of two consecutive failed probes.)
         
         sudo apachectl stop
         

  3. Follow the test procedure to send traffic to the load balancer. Repeat the second step a few times. The expected behavior is for new connections to be distributed between the two healthy failover VMs, `vm-c1` and `vm-c2`. This happens because only one primary VM, `vm-a2`, is healthy, and the ratio of healthy primary VMs to total primary VMs is `0.5`—less than the failover threshold of `0.75`. Each failover VM serves a response approximately half of the time [as long as the session affinity is set to `NONE`](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution).




### Testing failback

This test simulates failback by restarting the Apache server on `vm-a1`.

  1. Connect to the `vm-a1` VM.
         
         gcloud compute ssh vm-a1 --zone us-west1-a
         

  2. Start the Apache web server and wait 10 seconds.
         
         sudo apachectl start
         

  3. Follow the client test procedure. Repeat the second step a few times. The expected behavior is for traffic to be served by the two primary VMs, `vm-a1` and `vm-a2`. With both primary VMs being healthy, the ratio of healthy primary VMs to total primary VMs is `1.0`, greater than the failover threshold of `0.75`, so the load balancer's eligible backends consist of all healthy primary backend VMs.




## Adding more backend VMs

This section extends the example configuration by adding more primary and failover VMs to the load balancer. It does so by creating two more backend instance groups to demonstrate that you can distribute primary and failover VMs among multiple zones in the same region:

  * A third instance group, `ig-d` in `us-west1-c`, serves as a primary backend with two VMs: 
    * `vm-d1`
    * `vm-d2`
  * A fourth instance group, `ig-b` in `us-west1-a`, serves as a failover backend with two VMs: 
    * `vm-b1`
    * `vm-b2`



The modified architecture for this example looks like this:

[ ![Multi-zone regional external passthrough Network Load Balancer failover.](https://docs.cloud.google.com/static/load-balancing/images/netlb-expanded-failover.svg)](https://docs.cloud.google.com/static/load-balancing/images/netlb-expanded-failover.svg) Multi-zone regional external passthrough Network Load Balancer failover (click to enlarge).

### Create additional VMs and instance groups

Follow these steps to create the additional primary and failover VMs and their corresponding unmanaged instance groups.

###  Console 

**Create backend VMs**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Repeat the following steps to create four VMs, using the following name and zone combinations.

     * Name: `vm-b1`, zone: `us-west1-a`
     * Name: `vm-b2`, zone: `us-west1-a`
     * Name: `vm-d1`, zone: `us-west1-c`
     * Name: `vm-d2`, zone: `us-west1-c`
  3. Click **Create instance**.

  4. Set the **Name** as indicated in step 2.

  5. For the **Region** , choose `us-west1`, and choose a **Zone** as indicated in step 2.

  6. In the **Boot disk** section, ensure that the selected image is _Debian GNU/Linux 9 Stretch_. Click **Choose** to change the image if necessary.

  7. Click **Advanced options**.

  8. Click **Networking** and configure the following field:

     1. For **Network tags** , enter `network-lb`.
  9. Click **Management**. Enter the following script into the **Startup script** field. The script contents are identical for all four VMs:
         
         #! /bin/bash
         apt-get update
         apt-get install apache2 -y
         a2ensite default-ssl
         a2enmod ssl
         vm_hostname="$(curl -H "Metadata-Flavor:Google" \
         http://metadata.google.internal/computeMetadata/v1/instance/name)"
         echo "Page served from: $vm_hostname" | \
         tee /var/www/html/index.html
         systemctl restart apache2
         

  10. Click **Create**.




**Create instance groups**

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Repeat the following steps to create two unmanaged instance groups each with two VMs in their one, using these combinations.

     * Instance group: `ig-b`, zone: `us-west1-a`, VMs: `vm-b1` and `vm-b2`
     * Instance group: `ig-d`, zone: `us-west1-c`, VMs: `vm-d1` and `vm-d2`
  3. Click **Create instance group**.

  4. Click **New unmanaged instance group**.

  5. Set **Name** as indicated in step 2.

  6. In the **Location** section, choose `us-west1` for the **Region** , and then choose a **Zone** as indicated in step 2.

  7. For **Network** , enter `default`.

  8. In the **VM instances** section, add the VMs as indicated in step 2.

  9. Click **Create**.




###  gcloud 

  1. Create four VMs by running the following command four times, using these four combinations for `VM-NAME` and `ZONE`. The script contents are identical for all four VMs.

     * `VM-NAME` of `vm-b1` and `ZONE` of `us-west1-a`
     * `VM-NAME` of `vm-b2` and `ZONE` of `us-west1-a`
     * `VM-NAME` of `vm-d1` and `ZONE` of `us-west1-c`
     * `VM-NAME` of `vm-d2` and `ZONE` of `us-west1-c`
    
    gcloud compute instances create VM-NAME \
        --zone=ZONE \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --tags=network-lb \
        --metadata=startup-script='#! /bin/bash
          apt-get update
          apt-get install apache2 -y
          a2ensite default-ssl
          a2enmod ssl
          vm_hostname="$(curl -H "Metadata-Flavor:Google" \
          http://metadata.google.internal/computeMetadata/v1/instance/name)"
          echo "Page served from: $vm_hostname" | \
          tee /var/www/html/index.html
          systemctl restart apache2'
    

  2. Create the two unmanaged instance groups in each zone:
         
         gcloud compute instance-groups unmanaged create ig-b \
             --zone us-west1-a
         gcloud compute instance-groups unmanaged create ig-d \
             --zone us-west1-c
         

  3. Add the VMs to the appropriate instance groups:
         
         gcloud compute instance-groups unmanaged add-instances ig-b \
             --zone us-west1-a \
             --instances vm-b1,vm-b2
         gcloud compute instance-groups unmanaged add-instances ig-d \
             --zone us-west1-c \
             --instances vm-d1,vm-d2
         




### Adding a primary backend

You can use this procedure as a template for how to add an unmanaged instance group to an existing regional external passthrough Network Load Balancer's backend service as a primary backend. For the example configuration, this procedure shows you how to add instance group `ig-d` as a primary backend to the `network-lb` load balancer.

###  Console 

Edit the load balancer configuration to add a primary backend.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/loadbalancing/loadBalancers/list)

  2. Click on the load balancer you want to modify.

  3. Click **Edit**.

  4. Click **Backend configuration** and make the following changes:

     1. Under **Backends** , click **Add Backend**.
     2. From the dropdown, select the instance group to be added as a primary backend. In this case, `ig-d`.
     3. Click **Done**.
     4. Verify that there is a blue check mark next to **Backend configuration** before continuing.



### Review the configuration

  1. Click the **Review and finalize** button and confirm that the new primary backend is visible under **Backend**.
  2. If the settings are correct, click **Create**. It takes a few minutes for the load balancer to be created.

On the load balancing screen, under the Backend column for your new load balancer, you should see a green checkmark showing that the new load balancer is healthy.




###  gcloud 

Use the following `gcloud` command to add a primary backend to an existing regional external passthrough Network Load Balancer's backend service.
    
    
    gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
       --instance-group INSTANCE_GROUP_NAME \
       --instance-group-zone INSTANCE_GROUP_ZONE \
       --region REGION
    

where:

  * `BACKEND_SERVICE_NAME` is the name of the load balancer's backend service. For the example, use `network-lb-backend-service`.
  * `INSTANCE_GROUP_NAME` is the name of the instance group to add as a primary backend. For the example, use `ig-d`.
  * `INSTANCE_GROUP_ZONE` is the zone where the instance group is defined. For the example, use `us-west1-c`.
  * `REGION` is the region of the load balancer. For the example, use `us-west1`.



### Adding a failover backend

You can use this procedure as a template for how to add an unmanaged instance group to an existing regional external passthrough Network Load Balancer's backend service as a failover backend. For the example configuration, this procedure shows you how to add instance group `ig-b` as a failover backend to the `network-lb` load balancer.

###  Console 

Edit the load balancer configuration to add a primary backend.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/loadbalancing/loadBalancers/list)

  2. Click on the load balancer you want to modify.

  3. Click **Edit**.

  4. Click **Backend configuration** and make the following changes:

     1. Under **Backends** , click **Add Backend**.
     2. From the dropdown, select the instance group to be added as a failover backend. In this case, `ig-b`.
     3. Select the **Use this instance group as a failover group for backup** checkbox.
     4. Click **Done**.
     5. Verify that there is a blue check mark next to **Backend configuration** before continuing.



### Review the configuration

  1. Click the **Review and finalize** button and confirm that the new primary backend is visible under **Backend**.
  2. If the settings are correct, click **Create**. It takes a few minutes for the load balancer to be created.

On the load balancing screen, under the Backend column for your new load balancer, you should see a green checkmark showing that the new load balancer is healthy.




###  gcloud 

Use the following `gcloud` command to add a failover backend to an existing regional external passthrough Network Load Balancer's backend service.
    
    
    gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
       --instance-group INSTANCE_GROUP_NAME \
       --instance-group-zone INSTANCE_GROUP_ZONE \
       --region REGION \
       --failover
    

where:

  * `BACKEND_SERVICE_NAME` is the name of the load balancer's backend service. For the example, use `network-lb-backend-service`.
  * `INSTANCE_GROUP_NAME` is the name of the instance group to add as a failover backend. For the example, use `ig-b`.
  * `INSTANCE_GROUP_ZONE` is the zone where the instance group is defined. For the example, use `us-west1-a`.
  * `REGION` is the region of the load balancer. For the example, use `us-west1`.



### Converting a primary or failover backend

You can convert a primary backend to a failover backend, or a failover backend to a primary backend, without having to remove the instance group from the regional external passthrough Network Load Balancer's backend service.

###  gcloud 

Use the following `gcloud` command to convert an existing primary backend to a failover backend:
    
    
    gcloud compute backend-services update-backend BACKEND_SERVICE_NAME \
       --instance-group INSTANCE_GROUP_NAME \
       --instance-group-zone INSTANCE_GROUP_ZONE \
       --region REGION \
       --failover
    

Use the following `gcloud` command to convert an existing failover backend to a primary backend:
    
    
    gcloud compute backend-services update-backend BACKEND_SERVICE_NAME \
       --instance-group INSTANCE_GROUP_NAME \
       --instance-group-zone INSTANCE_GROUP_ZONE \
       --region REGION \
       --no-failover
    

where:

  * `BACKEND_SERVICE_NAME` is the name of the load balancer's backend service.
  * `INSTANCE_GROUP_NAME` is the name of the instance group.
  * `INSTANCE_GROUP_ZONE` is the zone where the instance group is defined.
  * `REGION` is the region of the load balancer.



## Configuring failover policies

This section describes how to configure a failover policy for a regional external passthrough Network Load Balancer backend service. For more information on the parameters of a failover policy, see [Failover](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#failover).

### Defining a failover policy

The following instructions describe how to define the failover policy for an existing regional external passthrough Network Load Balancer.

###  gcloud 

To define a failover policy using the gcloud CLI, update the load balancer's backend service:
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
       --region REGION \
       --failover-ratio FAILOVER_RATIO \
       --connection-drain-on-failover \
       --drop-traffic-if-unhealthy
    

where:

  * `BACKEND_SERVICE_NAME` is the name of the load balancer's backend service. For the example, use `network-lb`.
  * `REGION` is the region of the load balancer. For the example, use `us-west1`.
  * `FAILOVER_RATIO` is the failover ratio. Possible values are between `0.0` and `1.0`, inclusive. For the example, use `0.75`.



### Viewing a failover policy

The following instructions describe how to view the existing failover policy for a regional external passthrough Network Load Balancer.

###  gcloud 

To list the failover policy settings using the gcloud CLI, use the following command. Undefined settings in a failover policy use [default failover policy values](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#failover_policy).
    
    
    gcloud compute backend-services describe BACKEND_SERVICE_NAME \
       --region REGION \
       --format="get(failoverPolicy)"
    

where:

  * `BACKEND_SERVICE_NAME` is the name of the load balancer's backend service. For the example, use `network-lb-backend-service`.
  * `REGION` is the region of the load balancer. For the example, use `us-west1`.



## What's next

  * See [Regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service) for important fundamentals.
  * See [Set up a regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service) for an example configuration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
