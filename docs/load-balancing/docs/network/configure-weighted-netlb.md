---
url: https://docs.cloud.google.com/load-balancing/docs/network/configure-weighted-netlb/
title: Configure weighted load balancing \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:27.248154+00:00
---

# Configure weighted load balancing  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/configure-weighted-netlb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Configure weighted load balancing Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides instructions for creating a weighted regional external passthrough Network Load Balancer deployment for each virtual machine (VM) instance using a regional backend service.

In this tutorial, you create an instance group with three VM instances and assign weights for each instance. You create an HTTP health check to report backend instance weights. Weighted load balancing is enabled on the backend service with locality load balancer policy as `WEIGHTED_MAGLEV`.

## Before you begin

  * Read the [Backend service-based regional external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).
  * Install the Google Cloud CLI. For a complete overview of the tool, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud). You can find commands related to load balancing in the [API and gcloud CLI reference](https://docs.cloud.google.com/load-balancing/docs/apis).

If you haven't run the Google Cloud CLI previously, first run [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) to authenticate.

  * Enable the compute API.
        
        gcloud services enable compute.googleapis.com
        


**Note:** You cannot use the Google Cloud console to configure the locality load balancer policy and assign weights to VM instances. Use the Google Cloud CLI instead.

## Create VPC network, subnets, and firewall rules

Create a VPC network, subnet, and ingress allow firewall rules to allow connections to the backend VMs of your load balancer.

  1. Create a VPC network and subnet.

a. To create the VPC network, run the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create NETWORK_NAME --subnet-mode custom
         

b. In this example, the subnet's primary IPv4 address range is `10.10.0.0/24`. To create the subnet, run the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create SUBNET_NAME \
           --network=NETWORK_NAME \
           --range=10.10.0.0/24 \
           --region=us-central1
         

Replace the following:

     * `NETWORK_NAME`: the name of the VPC network to create.
     * `SUBNET_NAME`: the name of the subnetwork to create.
  2. Create an ingress allow firewall rule to allow packets sent to destination TCP ports 80 and 443 to be delivered to the backend VMs. In this example, firewall rule allows connections from any source IP address. The firewall rule applies to VMs with the network tag `network-lb-tag`.

To create the firewall rule, run the [`gcloud compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create):
         
         gcloud compute firewall-rules create FIREWALL_RULE_NAME \
            --direction=INGRESS \
            --priority=1000 \
            --network=NETWORK_NAME \
            --action=ALLOW \
            --rules=tcp:80,tcp:443 \
            --source-ranges=0.0.0.0/0 \
            --target-tags=network-lb-tag
         

Replace `FIREWALL_RULE_NAME` with the name of the firewall rule to create.




## Create VM instances and assign weights

Create three VM instances and assign weights:

  1. Configure three backend VM instances to return the weights in the `X-Load-Balancing-Endpoint-Weight` header with HTTP responses. For this tutorial, you configure one backend instance to report a weight of zero, a second backend instance to report a weight of 100, and a third backend instance to report a weight of 900.

To create the instances, run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
         
         gcloud compute instances create instance-0 \
           --zone=us-central1-a \
           --tags=network-lb-tag \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --subnet=SUBNET_NAME \
           --metadata=load-balancing-weight=0,startup-script='#! /bin/bash
           apt-get update
           apt-get install apache2 -y
           ln -sr /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/headers.load
           vm_hostname="$(curl -H "Metadata-Flavor:Google" \
           http://169.254.169.254/computeMetadata/v1/instance/name)"
           echo "Page served from: $vm_hostname" | \
           tee /var/www/html/index.html
           lb_weight="$(curl -H "Metadata-Flavor:Google" \
           http://169.254.169.254/computeMetadata/v1/instance/attributes/load-balancing-weight)"
           echo "Header set X-Load-Balancing-Endpoint-Weight \"$lb_weight\"" | \
           tee /etc/apache2/conf-enabled/headers.conf
           systemctl restart apache2'
         
         
         gcloud compute instances create instance-100 \
           --zone=us-central1-a \
           --tags=network-lb-tag \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --subnet=SUBNET_NAME \
           --metadata=load-balancing-weight=100,startup-script='#! /bin/bash
           apt-get update
           apt-get install apache2 -y
           ln -sr /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/headers.load
           vm_hostname="$(curl -H "Metadata-Flavor:Google" \
           http://169.254.169.254/computeMetadata/v1/instance/name)"
           echo "Page served from: $vm_hostname" | \
           tee /var/www/html/index.html
           lb_weight="$(curl -H "Metadata-Flavor:Google" \
           http://169.254.169.254/computeMetadata/v1/instance/attributes/load-balancing-weight)"
           echo "Header set X-Load-Balancing-Endpoint-Weight \"$lb_weight\"" | \
           tee /etc/apache2/conf-enabled/headers.conf
           systemctl restart apache2'
         
         
         gcloud compute instances create instance-900 \
           --zone=us-central1-a \
           --tags=network-lb-tag \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --subnet=SUBNET_NAME \
           --metadata=load-balancing-weight=900,startup-script='#! /bin/bash
             apt-get update
             apt-get install apache2 -y
             ln -sr /etc/apache2/mods-available/headers.load /etc/apache2/mods-enabled/headers.load
             vm_hostname="$(curl -H "Metadata-Flavor:Google" \
             http://169.254.169.254/computeMetadata/v1/instance/name)"
             echo "Page served from: $vm_hostname" | \
             tee /var/www/html/index.html
             lb_weight="$(curl -H "Metadata-Flavor:Google" \
             http://169.254.169.254/computeMetadata/v1/instance/attributes/load-balancing-weight)"
             echo "Header set X-Load-Balancing-Endpoint-Weight \"$lb_weight\"" | \
             tee /etc/apache2/conf-enabled/headers.conf
             systemctl restart apache2'
         




## Create an instance group

In this tutorial, you provide instructions to create an unmanaged instance group containing all three VM instances(`instance-0`, `instance-100`, and `instance-900`).

  * To create the instance group, run the [`gcloud compute instance-groups unmanaged create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create):
        
        gcloud compute instance-groups unmanaged create INSTANCE_GROUP \     
          --zone=us-central1-a
        
        
        gcloud compute instance-groups unmanaged add-instances INSTANCE_GROUP \
          --zone=us-central1-a \
          --instances=instance-0,instance-100,instance-900
        

Replace `INSTANCE_GROUP` with the name of the instance group to create.




## Create an HTTP health check

In this tutorial, you provide instructions to create an HTTP health check to read the HTTP response containing the backend VM's weight."

  * To create the HTTP health check, run the [`gcloud compute health-checks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http):
        
        gcloud compute health-checks create http HTTP_HEALTH_CHECK_NAME \
          --region=us-central1
        

Replace `HTTP_HEALTH_CHECK_NAME` with the name of the HTTP health check to create.




## Create a backend service

The following example provides instructions to create a regional external backend service configured to use [weighted load balancing](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#weighted-lb).

  1. Create a backend service with the HTTP health check and set the locality load balancer policy to `WEIGHTED_MAGLEV`.

     * To create the backend service, run the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create):
           
           gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=external \
             --protocol=tcp \
             --region=us-central1 \
             --health-checks=HTTP_HEALTH_CHECK_NAME \
             --health-checks-region=us-central1 \
             --locality-lb-policy=WEIGHTED_MAGLEV
           

Replace `BACKEND_SERVICE_NAME` with the name of the backend service to create.

  2. Add the instance group to the backend service.

     * To add the instance group, run the [`gcloud compute backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend):
           
           gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --instance-group=INSTANCE_GROUP \
             --instance-group-zone=us-central1-a \
             --region=us-central1
           

  3. Reserve a regional external IP address for the load balancer.

     * To reserve one or more IP addresses, run the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create):
           
           gcloud compute addresses create ADDRESS_NAME \
            --region us-central1
           

Replace `ADDRESS_NAME` with the name of the IP address to create.

Use the [`compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the result. Note the reserved static external IP address (`IP_ADDRESS`).
           
           gcloud compute addresses describe ADDRESS_NAME
           

  4. Create a forwarding rule using the reserved regional external IP address `IP_ADDRESS`. Connect the forwarding rule to the backend service.

     * To create the forwarding rule, run the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create):
           
           gcloud compute forwarding-rules create FORWARDING_RULE \
             --region=us-central1 \
             --ports=80 \
             --address=IP_ADDRESS \
             --backend-service=BACKEND_SERVICE_NAME
           

Replace the following:

`FORWARDING_RULE`: the name of the forwarding rule to create.

`IP_ADDRESS`: the IP address to assign to the instance. Use the reserved static external IP address, not the address name.




## Verify backend weights using backend service API

Verify that the backend weights are properly reported to the HTTP health check.

  * To get backend weights (along with health statuses) from a backend service, run the [`gcloud compute backend-services get-health` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health):
        
        gcloud compute backend-services get-health BACKEND_SERVICE_NAME \
          --region=us-central1
        




The output is the following:
    
    
    backend: https://www.googleapis.com/compute/projects/project-name/{project}/zones/us-central1-a/instanceGroups/{instance-group-name}
    status:
      healthStatus:
      - forwardingRule: https://www.googleapis.com/compute/projects/{project}/regions/us-central1/forwardingRules/{firewall-rule-name}
        forwardingRuleIp: 34.135.46.66
        healthState: HEALTHY
        instance: https://www.googleapis.com/compute/projects/{project}/zones/us-central1-a/instances/instance-0
        ipAddress: 10.10.0.5
        port: 80
        weight: '0'
      - forwardingRule: https://www.googleapis.com/compute/projects/{project}/regions/us-central1/forwardingRules/{firewall-rule-name}
        forwardingRuleIp: 34.135.46.66
        healthState: HEALTHY
        instance: https://www.googleapis.com/compute/projects/{project}/zones/us-central1-a/instances/instance-100
        ipAddress: 10.10.0.6
        port: 80
        weight: '100'
      - forwardingRule: https://www.googleapis.com/compute/projects/{project}/regions/us-central1/forwardingRules/{firewall-rule-name}
        forwardingRuleIp: 34.135.46.66
        healthState: HEALTHY
        instance: https://www.googleapis.com/compute/projects/{project}/zones/us-central1-a/instances/instance-900
        ipAddress: 10.10.0.7
        port: 80
        weight: '900'
      kind: compute#backendServiceGroupHealth
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
