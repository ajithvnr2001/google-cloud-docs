---
url: https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl/
title: Set up a classic proxy Network Load Balancer (SSL proxy) with VM instance group backends \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:42.368444+00:00
---

# Set up a classic proxy Network Load Balancer (SSL proxy) with VM instance group backends  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up a classic proxy Network Load Balancer (SSL proxy) with VM instance group backends Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for setting up a classic proxy Network Load Balancer with a target SSL proxy and VM instance group backends. Before you start, read [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp) for information on how these load balancers work.

## Setup overview

This example demonstrates how to set up an external proxy Network Load Balancer for a service that exists in two regions: Region A and Region B. You will configure the following:

  1. Four instances spread across two regions
  2. Instance groups for holding the instances
  3. Backend components, which include the following: 
     * Health check - used to monitor instance health
     * Backend service - monitors instance groups and prevents them from exceeding configured usage
     * Backends - hold the instance groups
  4. Frontend components, which include the following: 
     * An SSL certificate resource.
     * The SSL proxy itself with its SSL certificate
     * An external static IPv4 address and a forwarding rule that sends user traffic to the proxy
     * An external static IPv6 address and a forwarding rule that sends user traffic to the proxy
  5. A firewall rule that allows traffic from the load balancer and health checker to the instances.
  6. Optionally, an [SSL policy](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) to control the features of SSL that your SSL proxy load balancer negotiates with clients.



After that, you'll test your configuration.

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



## Configure the network and subnets

To create the example network and subnet, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Enter a **Name** for the network.

  4. Choose **Custom** for the **Subnet creation mode**.

  5. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. In the **Name** field, provide a name for the subnet.
     2. In the **Region** field, enter a region name.
     3. For **IP stack type** , select **IPv4 (single-stack)**.
     4. In the **IP address range** field, enter an IP address range. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.
  6. Click **Done**.

  7. To add a subnet in a different region, click **Add subnet** and repeat the previous steps.

  8. Click **Create**.




###  gcloud 
    
    
    gcloud compute networks subnets update SUBNET \
        --network=NETWORK \
        --stack-type=IPV4_ONLY \
        --range=10.1.2.0/24 \
        --region=REGION_A
    

Replace the following:

  * `NETWORK`: a name for the VPC network

  * `SUBNET`: a name for the subnet

  * `REGION_A`: the name of the region




## Configure instances and instance groups

This section shows how to create instances and instance groups, then add the instances to the instance groups. A production system would normally use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) based on [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates), but this setup is quicker for initial testing.

### Create instances

Create these instances with the tag `ssl-lb`, which the firewall rule will use later.

###  Console 

**Create instances**

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.

  3. Set **Name** to `vm-a1`.

  4. Set the **Zone** to ZONE_A.

  5. Click **Advanced options**.

  6. Click **Networking** and configure the following field:

     * In the **Network tags** field, enter `ssl-lb` and `allow-health-check-ipv6`.
  7. In the **Network interfaces** section, click **Edit** and make the following changes:

     * Select the network.
     * Select a subnet. 

     * Click **Done**.

  8. Click **Management**. Enter the following script into the **Startup script** field.
         
         sudo apt-get update
         sudo apt-get install apache2 -y
         sudo a2ensite default-ssl
         sudo a2enmod ssl
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>vm-a1</h1></body></html>' | sudo tee /var/www/html/index.html

  9. Leave the default values for rest of the fields.

  10. Click **Create**.

  11. Create `vm-a2` with the same settings, except with **Startup script** set to the following:
         
         sudo apt-get update
         sudo apt-get install apache2 -y
         sudo a2ensite default-ssl
         sudo a2enmod ssl
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>vm-a2</h1></body></html>' | sudo tee /var/www/html/index.html

  12. Create `vm-b1` with the same settings, except with **Zone** set to `ZONE_B` and **Startup script** set to the following:
         
         sudo apt-get update
         sudo apt-get install apache2 -y
         sudo a2ensite default-ssl
         sudo a2enmod ssl
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>vm-b1</h1></body></html>' | sudo tee /var/www/html/index.html

  13. Create `vm-b2` with the same settings, except with **Zone** set to `ZONE_B` and **Startup script** set to the following:
         
         sudo apt-get update
         sudo apt-get install apache2 -y
         sudo a2ensite default-ssl
         sudo a2enmod ssl
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>vm-b2</h1></body></html>' | sudo tee /var/www/html/index.html




###  gcloud 

  1. Create `vm-a1` in zone `ZONE_A`.
         
         gcloud compute instances create vm-a1 \
            --image-family debian-12 \
            --image-project debian-cloud \
            --tags ssl-lb \
            --zone ZONE_A \
            --metadata startup-script="#! /bin/bash
              sudo apt-get update
              sudo apt-get install apache2 -y
              sudo a2ensite default-ssl
              sudo a2enmod ssl
              sudo service apache2 restart
              echo '<!doctype html><html><body><h1>vm-a1</h1></body></html>' | sudo tee /var/www/html/index.html
              EOF"
         

  2. Create `vm-a2` in zone `ZONE_A`.
         
         gcloud compute instances create vm-a2 \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --tags=ssl-lb \
           --zone=ZONE_A \
           --metadata=startup-script="#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>vm-a2</h1></body></html>' | sudo tee /var/www/html/index.html
              EOF"
         

  3. Create `vm-b1` in zone `ZONE_B`.
         
         gcloud compute instances create vm-b1 \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --tags=ssl-lb \
           --zone=ZONE_B \
           --metadata=startup-script="#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>vm-b1</h1></body></html>' | sudo tee /var/www/html/index.html
             EOF"
         

  4. Create `vm-b2` in zone `ZONE_B`.
         
         gcloud compute instances create vm-b2 \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --tags=ssl-lb \
           --zone=ZONE_B \
           --metadata=startup-script="#! /bin/bash
             sudo apt-get update
             sudo apt-get install apache2 -y
             sudo a2ensite default-ssl
             sudo a2enmod ssl
             sudo service apache2 restart
             echo '<!doctype html><html><body><h1>vm-b2</h1></body></html>' | sudo tee /var/www/html/index.html
             EOF"
         




### Create an instance group for each zone and add instances

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**.

  3. Set the **Name** to `instance-group-a`.

  4. Set the **Zone** to `ZONE_A`.

  5. Under **Port mapping** , click **Add port**. A load balancer sends traffic to an instance group through a [named port](https://docs.cloud.google.com/load-balancing/docs/backend-service#named_ports). Create a named port to map the incoming traffic to a specific port number.

     1. Enter a **Port name** of `ssl-lb` and **Port numbers** of `443`.
  6. Under **Instance definition** , click **Select existing instances**.

  7. From **VM instances** select `vm-a1` and `vm-a2`.

  8. Leave other settings as they are.

  9. Click **Create**.

  10. Repeat steps, but set the following:

     * **Name** : `instance-group-b`
     * **Zone** : `ZONE_B`
     * **Port name** of `ssl-lb` and **Port numbers** of `443`
     * **Instances** : **vm-b1** and **vm-b2**.
  11. Confirm that you now have two instance groups, each with two instances.




###  gcloud 

  1. Create the instance-group-a instance group.
         
         gcloud compute instance-groups unmanaged create instance-group-a --zone ZONE_A
         

  2. Set a named port for the instance group.
         
         gcloud compute instance-groups set-named-ports instance-group-a \
             --named-ports=ssl-lb:443 \
             --zone=ZONE_A
         

  3. Add `vm-a1` and `vm-a2` to instance-group-a
         
         gcloud compute instance-groups unmanaged add-instances instance-group-a \
             --instances=vm-a1,vm-a2 \
             --zone=ZONE_A
         

  4. Create the `instance-group-b` instance group.
         
         gcloud compute instance-groups unmanaged create instance-group-b --zone ZONE_B
         

  5. Set a named port for the instance group.
         
         gcloud compute instance-groups set-named-ports instance-group-b \
             --named-ports=ssl-lb:443 \
             --zone=ZONE_B
         

  6. Add `vm-b1` and `vm-b2` to instance-group-b
         
         gcloud compute instance-groups unmanaged add-instances instance-group-b \
             --instances=vm-b1,vm-b2 \
             --zone=ZONE_B
         




You now have an instance group in each of two regions, each with two instances.

## Set up an SSL certificate resource

To create the load balancer, you must have an [SSL certificate resource](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) that can be attached to the target proxy. The SSL certificate resource can be either a certificate map or a Compute Engine SSL certificate (classic certificate).

#### Certificate map

You can create a certificate map as described in one of the following documents:

  * [Deploy a global Google-managed certificate with load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-lb-auth)
  * [Deploy a global Google-managed certificate with DNS authorization](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-dns-auth)
  * [Deploy a global Google-managed certificate with Certificate Authority Service](https://docs.cloud.google.com/certificate-manager/docs/deploy-google-managed-cas)
  * [Deploy a global self-managed certificate](https://docs.cloud.google.com/certificate-manager/docs/deploy-self-managed)



#### Compute Engine SSL certificate

For an HTTPS load balancer, create a Compute Engine SSL certificate resource as described in one of the following documents:

  * [Use self-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs)
  * [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)



We recommend using a Google-managed certificate.

**Warning:** Don't use a self-signed certificate for production purposes.

## Create a firewall rule for the SSL load balancer

Configure the firewall to allow traffic from the load balancer and health checker to the instances.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. Click **Create firewall rule**.

  3. In the **Name** field, enter `allow-ssl-lb-and-health`.

  4. Select the network.

  5. Under **Targets** , select **Specified target tags**.

  6. Set **Target tags** to `ssl-lb`.

  7. Set **Source filter** to **IPv4 ranges**.

  8. Set **Source IPv4 ranges** to `130.211.0.0/22` and `35.191.0.0/16`.

  9. Under **Protocols and ports** , set **Specified protocols and ports** to `tcp:443`.

  10. Click **Create**.




###  gcloud 
    
    
    gcloud compute firewall-rules create allow-ssl-lb-and-health \
      --source-ranges=130.211.0.0/22,35.191.0.0/16 \
      --target-tags=ssl-lb \
      --allow=tcp:443
    

If you are using a Google-managed certificate, confirm that your certificate resource's status is ACTIVE. For more information, see [Google-managed SSL certificate resource status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#certificate-resource-status).
    
    
    gcloud compute ssl-certificates list
    

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

Set the **Name** to `my-ssl-lb`.

**Backend configuration**

  1. Click **Backend configuration**.
  2. In the **Backend type** list, select **Instance groups**.
  3. In the **Protocol** list, select **SSL**.
  4. In the **Named port** field, enter `ssl-lb`.
  5. Accept the default value for the **Timeout**.
  6. Configure the health check: 
     * In the **Health check** list, select **Create a health check**.
     * In the **Name** field, enter `my-ssl-health-check`.
     * In the **Protocol** list, select **SSL**.
     * Retain the remaining default values.
     * Click **Create**.
  7. Configure the first backend: 
     1. Under **New backend** , select instance group `instance-group-a`.
     2. Set **Port numbers** to `443`.
     3. Retain the remaining default values.
  8. Configure the second backend: 
     1. Click **Add backend**.
     2. Select instance group `instance-group-b`.
     3. Set **Port numbers** to `443`.
     4. Click **Done**.
  9. In the Google Cloud console, verify that there is a check mark next to **Backend configuration**. If not, double-check that you have completed all of the steps.



**Frontend configuration**

  1. Click **Frontend configuration**.
Add the first forwarding rule: 
     1. Enter a **Name** of `my-ssl-lb-forwarding-rule`.
     2. Under **Protocol** , select **SSL**.
     3. Under **IP address** , select **Create IP address** : 
        1. Enter a **Name** of `ssl-lb-static-ipv4`.
        2. Click **Reserve**.
     4. For **Choose certificate repository** , select **Use certificate map** or **Use classic certificates**. 
     5. Depending on your selection, select a certificate map or a classic certificate.
     6. (Optional) To create an SSL policy, do the following:
        1. Under **SSL policy** , select **Create a policy**.
        2. Enter a **Name** of `my-ssl-policy`.
        3. For **Minimum TLS Version** , select **TLS 1.0**.
        4. For **Profile** , select **Modern**. The **Enabled features** and **Disabled features** are displayed.
        5. Click **Save**.
     7. Optional: Turn on Proxy protocol.
     8. Click **Done**.
Add the second forwarding rule: 
     1. Click **Add frontend IP and port**.
     2. Enter a **Name** of `my-ssl-lb-ipv6-forwarding-rule`.
     3. Set **IP version** to `IPv6`.
     4. Under **IP address** , click **Create IP address**. 
        1. Enter a name of `ssl-lb-static-ipv6`.
        2. Click **Reserve**.
     5. Under **Certificate** , select `my-ssl-cert`.
     6. To add certificate resources in addition to the primary SSL certificate resource, either select a certificate from the **Certificates** list or click **Create a new certificate**.
     7. Optional: Use an SSL policy or turn on Proxy protocol.
     8. Click **Done**.
     9. Verify that there is a green check mark next to **Frontend configuration** in the Google Cloud console. If not, double-check that you have completed all the previous steps.
     10. Click **Done**.



**Review and finalize**

  1. Click **Review and finalize**.
  2. Review your load balancer configuration settings.
  3. Optional: Click **Equivalent code** to view the REST API request that will be used to create the load balancer.
  4. Click **Create**.



### gcloud

  1. Create a health check. 
         
         gcloud compute health-checks create ssl my-ssl-health-check --port=443
            

  2. Create a backend service. 
         
         gcloud compute backend-services create my-ssl-lb \
                --load-balancing-scheme EXTERNAL \
                --global-health-checks \
                --protocol=SSL \
                --port-name=ssl-lb \
                --health-checks=my-ssl-health-check \
                --timeout=5m \
                --global
            

Alternatively you can configure unencrypted communication from the load balancer to the instances by using `--protocol=TCP`.

  3. Add instance groups to your backend service. 
         
         gcloud compute backend-services add-backend my-ssl-lb \
                --instance-group=instance-group-a \
                --instance-group-zone=ZONE_A \
                --balancing-mode=UTILIZATION \
                --max-utilization=0.8 \
                --global
            
         
         gcloud compute backend-services add-backend my-ssl-lb \
                --instance-group=instance-group-b \
                --instance-group-zone=ZONE_B \
                --balancing-mode=UTILIZATION \
                --max-utilization=0.8 \
                --global
            

  4. Configure your SSL certificate resource. 

If you are using self-managed certificates, you must already have at least one SSL certificate to upload. If you don't, see [SSL certificates overview](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates). When you use multiple SSL certificates, you must create them one at a time.

If you are using self-managed SSL certificates and you don't have a private key and signed certificate, you can create and use a [self-signed certificate](https://wikipedia.org/wiki/Self-signed_certificate) for testing purposes.

To create a self-managed SSL certificate resource:
         
         gcloud compute ssl-certificates create my-ssl-cert \
                --certificate=CRT_FILE_PATH \
                --private-key=KEY_FILE_PATH
            

To create a Google-managed SSL certificate resource:
         
         gcloud compute ssl-certificates create www-ssl-cert \
                --domains=DOMAIN_1,DOMAIN_2
            

  5. Configure a target SSL proxy. 

External proxy Network Load Balancers support creating a target SSL proxy that has [from one to fifteen SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#multiplessl). Before you run this command, you must create an SSL certificate resource for each certificate.

If you want to turn on the proxy header, set it to `PROXY_V1` instead of `none`. You can optionally attach an [SSL policy](https://docs.cloud.google.com/compute/docs/load-balancing/ssl-policies) to the target proxy. First, create the policy.
         
         gcloud compute ssl-policies create my-ssl-policy \
                --profile=MODERN \
                --min-tls-version=1.0
            

Then attached the policy to the target proxy.
         
         gcloud compute target-ssl-proxies create my-ssl-lb-target-proxy \
                --backend-service=my-ssl-lb \
                --ssl-certificates=[SSL_CERT_1][,[SSL_CERT_2],...] \
                --ssl-policy=my-ssl-policy \
                --proxy-header=NONE
            

  6. Reserve global static IP addresses. 

Your customers use these IP addresses to access your load-balanced service.
         
         gcloud compute addresses create ssl-lb-static-ipv4 \
                --ip-version=IPV4 \
                --global
            
         
         gcloud compute addresses create ssl-lb-static-ipv6 \
                --ip-version=IPV6 \
                --global
            

  7. Configure global forwarding rules. 

Create global forwarding rules associated with the target proxy. Replace LB_STATIC_IP and LB_STATIC_IPV6 with the IP addresses you generated in Reserve global static IP addresses.
         
         gcloud compute forwarding-rules create my-ssl-lb-forwarding-rule \
                --load-balancing-scheme EXTERNAL \
                --global \
                --target-ssl-proxy=my-ssl-lb-target-proxy \
                --address=LB_STATIC_IP \
                --ports=443
            
         
         gcloud compute forwarding-rules create my-ssl-lb-ipv6-forwarding-rule \
                --load-balancing-scheme EXTERNAL \
                --global \
                --target-ssl-proxy=my-ssl-lb-target-proxy \
                --address=LB_STATIC_IPV6 \
                --ports=443
            




## Connect your domain to your load balancer

After the load balancer is created, note the IP address that is associated with the load balancer—for example, `30.90.80.100`. To point your domain to your load balancer, create an `A` record by using your domain registration service. If you added multiple domains to your SSL certificate, you must add an `A` record for each one, all pointing to the load balancer's IP address. For example, to create `A` records for `www.example.com` and `example.com`, use the following:
    
    
    NAME                  TYPE     DATA
    www                   A        30.90.80.100
    @                     A        30.90.80.100
    

If you use Cloud DNS as your DNS provider, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).

## Test the load balancer

In your web browser, connect to your static IP address using HTTPS. In this test setup, the instances are using self-signed certificates. Therefore, you will see a warning in your browser the first time you access a page. Click through the warning to see the actual page. Replace IP_ADDRESS with either the IPv4 or IPv6 address you created earlier.
    
    
    https://IP_ADDRESS
    

You should see one of the hosts from the region closest to you. Reload the page until you see the other instance in that region. To see instances from the other region, stop the instances in the closest region.

Alternatively, you can use `curl` from the your local machine's command line. If you are using a self-signed certificate on the SSL proxy, you must also specify `-k`. The `curl -k` option allows curl to work even if you have a self-signed certificate or no certificate at all. If you have a normal certificate, you can remove that parameter. You should only use the `-k` parameter for testing your own site. Under normal circumstances, a valid certificate is an important security measure and certificate warnings shouldn't be ignored.

Replace IP_ADDRESS with either the IPv4 or IPv6 address you created earlier.
    
    
    curl -k https://IP_ADDRESS
    

If you can't reach the load balancer, try the steps described in [Proxy Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring) to investigate the load balancer's logs and metrics.

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
    
    
    gcloud compute target-ssl-proxies update TARGET_PROXY_NAME \
        --proxy-header=[NONE | PROXY_V1]
    

### Configure session affinity

These procedures show you how to update a backend service for the example SSL proxy load balancer so that the backend service uses client IP affinity.

When client IP affinity is enabled, the load balancer directs a particular client's requests to the same backend VM based on a hash created from the client's IP address and the load balancer's IP address (the external IP address of an external forwarding rule).

###  Console

To enable client IP session affinity:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

  2. Click **Backends**.

  3. Click **my-ssl-lb** (the name of the backend service you created for this example) and click **Edit**.

  4. On the **Backend service details** page, click **Advanced configuration**.

  5. Under **Session affinity** , select **Client IP** from the menu.

  6. Click **Update**.




###  gcloud 

Use the following command to update the `my-ssl-lb` backend service, specifying client IP session affinity:
    
    
    gcloud compute backend-services update my-ssl-lb \
        --global \
        --session-affinity=CLIENT_IP
    

###  API

To set client IP session affinity, make a `PATCH` request to the [`backendServices/patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/patch) method.
    
    
    PATCH https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/global/us-west1/backendServices/my-ssl-lb
    {
      "sessionAffinity": "CLIENT_IP"
    }
    

### Enable connection draining

You can enable connection draining on backend services to ensure minimal interruption to your users when an instance that is serving traffic is terminated, removed manually, or removed by an autoscaler. To learn more about connection draining, see the [Enabling Connection Draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) documentation.

## What's next

  * See [External proxy Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/tcp/tcp-ssl-proxy-logging-monitoring) for information about how monitoring works for external proxy Network Load Balancers.
  * See [SSL Policy overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) for information about how SSL policies work.
  * See [Using SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies) for information about configuring SSL policies. 
    * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
