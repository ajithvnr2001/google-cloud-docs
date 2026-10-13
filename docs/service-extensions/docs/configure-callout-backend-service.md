---
url: https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service/
title: Configure a user-managed callout backend service \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:40.400785+00:00
---

# Configure a user-managed callout backend service  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Configure a user-managed callout backend service Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions lets [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) send callouts from the data processing path to callout backend services managed by the user. This helps Application Load Balancers use custom logic in the processing path. This page describes how to configure a user-managed callout backend service.

For an overview about Application Load Balancer extensions, see [Cloud Load Balancing extensions overview](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview).

## Before you begin

  1. Ensure that you have either a project [owner or editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) or the following [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam):

     * To create instances: [`compute.instanceAdmin.v1`](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1)
     * To create Cloud Load Balancing components: [`compute.networkAdmin`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin)
  2. Enable these APIs: Compute Engine API and Network Services API.

### Console

     1. In the Google Cloud console, go to the **Enable access to APIs** page.

[Go to Enable access to APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networkservices.googleapis.com)

     2. Follow the instructions.

### gcloud

Use the `gcloud services enable` command:
    
    gcloud services enable compute.googleapis.com networkservices.googleapis.com
    

  3. Create and configure an [Application Load Balancer that supports extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs). For this example, [set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal). Use the sample values mentioned.

  4. [Create a client VM for testing](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#test_client).

  5. For route extensions only. Set up an additional backend service and update the URL map to add a host matcher that routes traffic to this backend service for all traffic with the HTTP host matching the specified condition.

### Console

     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

Specify the following sample values:

        * **Name** : `l7-ilb-backend2-vm`
        * **Tags** : `allow-ssh` and `load-balanced-backend`
        * **Zone** : `us-west1-a`
        * **Network** : `lb-network`
        * **Subnetwork** : `backend-subnet`
        * **Image** : `debian-11`
        * **Family** : `debian-cloud`
        * **Advanced options** > **Management** > **Automation** :
              
              '#! /bin/bash
              apt-get update
              apt-get install apache2 -y
              a2ensite default-ssl
              a2enmod ssl
              echo "Page served from second backend service" | tee /var/www/html/index.html
              systemctl restart apache2'
              

     2. [Create an unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#create_unmanaged_group).

Specify the following sample values:

        * **Name** : `l7-ilb-backend-service2-ig`
        * **Zone** : `us-west1-a`
     3. [Add the new VM to the instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#addinstances).

For **VM instances** , specify `l7-ilb-backend2-vm`.

     4. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

     5. [Update the load balancer](https://docs.cloud.google.com/compute/docs/tutorials/globally-autoscaling-a-web-service-on-compute-engine#configure_the_load_balancer) by creating a backend service and adding a backend to it.

For the backend service, specify the following sample values:

        * **Name** : `l7-ilb-backend-service2`
        * **Protocol** : `HTTP`
        * **Health check** > **Name** : `l7-ilb-basic-check`
        * **Health check** > **Region** : `us-west1`

For the backend, specify the following sample values:

        * **Instance group** : `l7-ilb-backend-service2-ig`
        * **Balancing mode** : `Utilization`
     6. [Add a host matcher to the URL map of the backend service](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps).

Specify the following sample values:

        * **Name** : `l7-ilb-map`
        * **Host** : `service-extensions.com`
        * **Path** : `callouts`
        * **Protocol** : `HTTP`
        * **Backend** : `l7-ilb-backend-service2`

### gcloud

     1. Create a VM instance. Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the following sample values:
            
            gcloud compute instances create l7-ilb-backend2-vm \
              --zone=us-west1-a \
              --network=lb-network \
              --subnet=backend-subnet \
              --tags=allow-ssh,load-balanced-backend \
              --image-family=debian-11 \
              --image-project=debian-cloud \
              --metadata=startup-script='#! /bin/bash
                  apt-get update
                  apt-get install apache2 -y
                  a2ensite default-ssl
                  a2enmod ssl
                  echo "Page served from second backend service" | tee /var/www/html/index.html
                  systemctl restart apache2'
            

     2. Create an unmanaged instance group. Use the [`gcloud compute instance-groups unmanaged create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) with the following sample values:
            
            gcloud compute instance-groups unmanaged create l7-ilb-backend-service2-ig \
              --zone us-west1-a
            

     3. Add the new VM to the instance group. Use the [`gcloud compute instance-groups unmanaged add-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) with the following sample values:
            
            gcloud compute instance-groups unmanaged add-instances l7-ilb-backend-service2-ig \
              --zone=us-west1-a \
              --instances=l7-ilb-backend2-vm
            

     4. Create a backend service. Use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) with the following sample values:
            
            gcloud compute backend-services create l7-ilb-backend-service2 \
              --load-balancing-scheme=INTERNAL_MANAGED \
              --protocol=HTTP \
              --health-checks=l7-ilb-basic-check \
              --health-checks-region=us-west1 \
              --region=us-west1
            

     5. Add a backend to the backend service. Use the [`gcloud compute backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) with the following sample values:
            
            gcloud compute backend-services add-backend l7-ilb-backend-service2 \
              --balancing-mode=UTILIZATION \
              --instance-group=l7-ilb-backend-service2-ig \
              --instance-group-zone=us-west1-a \
              --region=us-west1
            

     6. Add a host matcher to the URL map of the backend service. Use the [`gcloud compute url-maps add-path-matcher` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/add-path-matcher) with the following sample values:
            
            gcloud compute url-maps add-path-matcher l7-ilb-map \
              --path-matcher-name=callouts \
              --default-service=l7-ilb-backend-service2 \
              --new-hosts=service-extensions.com \
              --region=us-west1
              




## Set up a callout backend service

For this example, a basic Python-based extension server implementing Envoy's `ext_proc` gRPC API is available. A docker container with this server is at `us-docker.pkg.dev/service-extensions-samples/callouts/python-example-basic:main` in the [Service Extensions GitHub repository](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/callouts/python) of Google Cloud. This repository contains several other Python and Go samples of `ext_proc` servers to do tasks such as header mutation and body mutation.

**Note:** If you're using your own extension server, ensure that the gRPC server is configured to use TLS. Without TLS, connections to the extension server fail.

To create and set up a callout backend service, follow these steps:

  1. Create a virtual machine (VM) instance for the callout backend service that's running the sample Python extension server.

### Console

[Create an instance by using a container image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#from-container-image).

     1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

     2. Specify the following sample values:

        * **Name** : `callouts-vm`
        * **Zone** : `us-west1-a`
        * **Network** : `lb-network`
        * **Subnetwork** : `backend-subnet`
        * **Tags** : `allow-ssh` and `load-balanced-backend`
        * **Container image** : `us-docker.pkg.dev/service-extensions-samples/callouts/python-example-basic:main`

### gcloud

Create an instance by using a container image. Use the [`gcloud compute instances create-with-container` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create-with-container) with the following sample values:
    
    gcloud compute instances create-with-container callouts-vm \
      --container-image=us-docker.pkg.dev/service-extensions-samples/callouts/python-example-basic:main \
      --network=lb-network \
      --subnet=backend-subnet \
      --zone=us-west1-a \
      --tags=allow-ssh,load-balanced-backend
    

  2. Add the VM to an unmanaged instance group.

### Console

[Create an unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

     1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

Specify the following sample values:

        * **Name** : `callouts-ig`
        * **Zone** : `us-west1-a`
     2. [Set a port for the instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#creating_named_ports).

For **Port mapping** , specify these port names and values: `http:80` and `grpc:443`.

     3. [Add the new VM to the instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#addinstances).

For **VM instances** , specify `callouts-vm`.

### gcloud

     1. Create an unmanaged instance group. Use the [`gcloud compute instance-groups unmanaged create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/create) with the following sample values:
            
            gcloud compute instance-groups unmanaged create callouts-ig \
              --zone=us-west1-a
            

     2. Set a port for the instance group. Use the [`gcloud compute instance-groups unmanaged set-named-ports` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/set-named-ports) with the following sample values:
            
            gcloud compute instance-groups unmanaged set-named-ports callouts-ig \
              --named-ports=http:80,grpc:443 \
              --zone=us-west1-a
            

     3. Add the new VM instance to the unmanaged instance group. Use the [`gcloud compute instance-groups unmanaged add-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/unmanaged/add-instances) with the following sample values:
            
            gcloud compute instance-groups unmanaged add-instances callouts-ig \
              --zone=us-west1-a \
              --instances=callouts-vm
            

  3. [Create a callout backend service](https://docs.cloud.google.com/compute/docs/tutorials/globally-autoscaling-a-web-service-on-compute-engine#configure_the_load_balancer) and add a backend. Like other backend servers, callout servers might need [firewall rules](https://docs.cloud.google.com/load-balancing/docs/firewall-rules) to allow proxy traffic.

### Console

Create a callout backend service that uses the HTTP/2 protocol and has an HTTP health check.

     1. In the Google Cloud console, go to the Cloud Load Balancing **Backends** page.

[Go to Backends](https://console.cloud.google.com/net-services/loadbalancing/list/backends)

     2. Add a regional backend service with the following sample values:

        * **Name** : `l7-ilb-callout-service`
        * **Region** : `us-west1`
        * **Load balancer type** : `Regional external Application Load Balancer (EXTERNAL_MANAGED)`
        * **Protocol** : `HTTP2`
        * **Port name** : `grpc`
        * **Health check** > **Name** : `callouts-hc`
        * **Health check** > **Port number** : `80`
        * **Cloud Armor backend security policy** : `None`
     3. Add the instance group with the extension server as a backend to the backend service. The instance group runs the `ext_proc` service.

Specify the following sample values:

        * **Instance group** : `callouts-ig`
        * **Balancing mode** : `Utilization`

### gcloud

     1. Create a basic HTTP health check for the instance. Use the [`gcloud compute health-checks create http` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks/create/http) with the following sample values:
            
            gcloud compute health-checks create http callouts-hc \
              --region=us-west1 \
              --port=80
            

     2. Create a callout backend service that uses the HTTP/2 protocol. Use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create).
            
            gcloud compute backend-services create l7-ilb-callout-service \
              --load-balancing-scheme=INTERNAL_MANAGED \
              --protocol=HTTP2 \
              --port-name=grpc \
              --health-checks=callouts-hc \
              --health-checks-region=us-west1 \
              --region=us-west1
            

     3. Add the instance group with the extension server as a backend to the backend service. The instance group runs the `ext_proc` service. Use the [`gcloud compute backend-services add-backend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend) with the following sample values:
            
            gcloud compute backend-services add-backend l7-ilb-callout-service \
              --balancing-mode=UTILIZATION \
              --instance-group=callouts-ig \
              --instance-group-zone=us-west1-a \
              --region=us-west1
            




Having set up a backend service, you can configure [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions), [authorization](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions), and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions) extensions.

## What's next

  * [Configure a route extension](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions)
  * [Configure an authorization extension](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions)
  * [Configure a traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
