---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms-auto/
title: Set up Compute Engine VMs using automatic Envoy deployment \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:58.250014+00:00
---

# Set up Compute Engine VMs using automatic Envoy deployment  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms-auto/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Compute Engine VMs using automatic Envoy deployment

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document applies to the older APIs. If you are deploying with the new service routing APIs, which are in preview, see [Cloud Service Mesh setup for Envoy proxies with HTTP services](https://docs.cloud.google.com/service-mesh/docs/service-routing/set-up-envoy-http-mesh).

Before you follow the instructions in this guide, complete the prerequisite tasks described in [Prepare to set up on service routing APIs with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/docs/onboarding/prepare-service-routing-envoy-proxyless).

This guide shows you how to automatically deploy a data plane that consists of Envoy sidecar proxies, configure it using Cloud Service Mesh, and verify your setup to ensure that it's functioning correctly. This process involves the following:

  1. Enabling the Cloud OS Config API.
  2. Creating a test service.
  3. Deploying a simple data plane on Compute Engine using Envoy proxies (Envoy version 1.18.4, which supports only xDS v3).
  4. Setting up Cloud Service Mesh using Compute Engine APIs, which enable Cloud Service Mesh to configure your Envoy sidecar proxies.
  5. Logging in to a VM that is running an Envoy proxy and send a request to a load-balanced backend through the Envoy proxy.



The configuration examples in this document are for demonstration purposes. For a production environment, you might need to deploy additional components, based on your environment and requirements.

## Enabling the Cloud OS Config API

Ensure that you enable the [Cloud OS Config API](https://docs.cloud.google.com/compute/docs/osconfig/rest). Unless you do this, you cannot install the required components on your VMs.

To do this:

### Console

  1. In the Google Cloud console, go to APIs & services.   
[Go to the API Library page](https://console.cloud.google.com/project/_/apis/library)
  2. Select the correct project.
  3. In the search box, enter **Cloud OS Config API** and press **Enter**.
  4. Select **Cloud OS Config API**.
  5. Click **Enable**.



###  gcloud 
    
    
    gcloud services enable osconfig.googleapis.com
    

## Creating the `Hello World` test service

This section shows you how to create a simple test service that returns the hostname of the VM that served the request from the client. The test service is uncomplicated; it's a web server deployed across a Compute Engine managed instance group.

### Creating the instance template for the `Hello World` test service

The instance template you create configures a sample apache2 web server using the `startup-script` parameter.

###  Console 

  1. In the Google Cloud console, go to the Instance Templates page. 

[Go to Instance Templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.
  3. In the fields, enter the following information: 
     * **Name** : `td-demo-hello-world-template`
     * **Boot disk** : Choose an operating system and version.
     * **Service account** : Compute Engine default service account
     * **Access scopes** : Allow full access to all Cloud APIs
  4. Click **Management, Security, Disks, Networking, Sole Tenancy**. 1 In the **Networking** tab, in the **Network tags** field, add the `td-http-server` tag.
  5. In the **Management** tab, copy the following script into the **Startup script** field.
         
         #!/bin/bash
         sudo apt-get update -y
         sudo apt-get install apache2 -y
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>'\`/bin/hostname\`'</h1></body></html>' | sudo tee /var/www/html/index.html
         

  6. Click **Create**.




###  gcloud 

You can choose among many operating system versions. This example uses the default value Debian 10.

To create the instance template:
    
    
    gcloud compute instance-templates create td-demo-hello-world-template \
      --machine-type=n1-standard-1 \
      --boot-disk-size=20GB \
      --image-family=debian-10  \
      --image-project=debian-cloud \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --tags=td-http-server \
      --metadata=startup-script="#! /bin/bash
    sudo apt-get update -y
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    sudo mkdir -p /var/www/html/
    echo '<!doctype html><html><body><h1>'\`/bin/hostname\`'</h1></body></html>' | sudo tee /var/www/html/index.html"
    

### Creating the managed instance group for the `Hello World` service

In this section, you specify that the managed instance group always has two instances of the test service. This is for demonstration purposes. Cloud Service Mesh supports autoscaled managed instance groups.

###  Console 

  1. In the Google Cloud console, go to the Instance Groups page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**.
  3. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
  4. Enter `td-demo-hello-world-mig` for the name for the managed instance group, and select the `us-central1-a` zone.
  5. Under Instance template, select `td-demo-hello-world-template`, which is the instance template you created.
  6. Under **Autoscaling mode** , select `Off:do not autoscale`.
  7. Under **Maximum number of instances** , specify at least two as the number of instances that you want to create in the group.
  8. Click **Create**.



###  gcloud 

Use the gcloud CLI to create a managed instance group with the instance template you previously created.
    
    
    gcloud compute instance-groups managed create td-demo-hello-world-mig \
      --zone us-central1-a \
      --size=2 \
      --template=td-demo-hello-world-template
    

## Creating the instance template and the managed instance group where Envoy is deployed

Use the instructions in this section to create an instance template and managed instance group for Cloud Service Mesh with Envoy proxies deployed automatically. [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) create new backend VMs by using autoscaling.

### Software components running on your VMs

The following components are installed on your VMs when you create an instance template with `--service-proxy=enabled`.

  * The Envoy proxy, which is configured by Cloud Service Mesh, is downloaded from a dedicated Cloud Storage bucket. The bucket contains a Google-provided build of the Envoy proxy.
  * The service proxy agent, which initializes the Envoy proxy and the proxy's components. The service proxy agent sets up traffic interception and monitors the health of the Envoy proxy when a VM is running. The service proxy agent is also downloaded from a Cloud Storage bucket.



The only available Envoy version is the most recent Envoy binary that is hosted in a dedicated Cloud Storage location. This Envoy version is supported on Compute Engine Debian, CentOS 7/8, and RHEL 7/8. During autohealing and scaling up, the managed instance group installs a recent version of Envoy on the VM. In some cases, this version might be more recent than the Envoy deployed to VM instances that were created previously. This might result in an inconsistency in versions installed across VMs in a managed instance group. The inconsistent versions function together correctly. If there is a security update to Envoy, we recommend that you upgrade the managed instance group using a [rolling replace](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#performing_a_rolling_replace_or_restart).

### Creating the instance template

An instance template specifies the configuration of the VM instances that are created in a managed instance group. The flags that you pass to the instance template install Envoy and configure your VM instances to be ready for Cloud Service Mesh.

You can use Debian 10/11, CentOS 7/8, or RHEL 7/8 for the boot disk image in the instance template.

To create such an instance template:
    
    
      gcloud compute instance-templates create td-vm-template-auto \
        --image-family=[ debian-10 | centos-7 | centos-8 | rhel-7 | rhel-8 ]  \
        --image-project=[ debian-cloud | centos-cloud |rhel-cloud ] \
        --service-proxy=enabled
     

To customize your Envoy deployment, see [Automated Envoy deployment reference guide](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-vms-options).

### Creating the managed instance group

###  Console 

  1. In the Google Cloud console, go to the Instance Groups page. 

[Go to Instance Groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create an instance group**.
  3. Enter `td-vm-mig-us-central1` for the name for the managed instance group, and select the `us-central1-a` zone.
  4. Under **Group type** , select **Managed instance group**.
  5. Under **Instance template** , select `td-vm-template-auto`, the instance template that you created.
  6. Specify `2` as the number of instances that you want to create in the group.
  7. Click **Create** to create the new group.



###  gcloud 

Use the gcloud CLI to create a managed instance group with the instance template you previously created.
    
    
     gcloud compute instance-groups managed create td-vm-mig-us-central1 \
        --zone us-central1-a --size=2 --template=td-vm-template-auto
    

## Configuring Cloud Service Mesh with Google Cloud load balancing components

The instructions in this section show you how to configure Cloud Service Mesh so that your Envoy proxies load balance outbound traffic across two backend instances. You configure the following components:

  * A health check. For more information on health checks, read [Health Check Concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) and [Creating Health Checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * A firewall rule, to enable the health check probes to reach the backends. See [Health Check Concepts](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) for more information.
  * A backend service. For more information on backend services, read [Backend Services](https://docs.cloud.google.com/load-balancing/docs/backend-service).
  * A routing rule map. This includes creating a forwarding rule and a URL map. For more information, read [Using forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rules) and [Using URL maps](https://docs.cloud.google.com/load-balancing/docs/https/url-map).



### Creating the health check

Use the following instructions to create a health check. For more information, refer to [Creating health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).

###  Console 

  1. Go to the Health checks page in the Google Cloud console.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click **Create Health Check**.
  3. For the name, enter `td-vm-health-check`.
  4. For the protocol, select **HTTP**.
  5. Click **Create**.



###  gcloud 

  1. Create the health check.
         
         gcloud compute health-checks create http td-vm-health-check
         




### Creating the firewall rule

Use the following instructions to create the firewall rule that is required for the health check probes. For more information, see [Firewall rules for health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule).

###  Console 

  1. Go to the **Firewall policies** page in the Google Cloud console.   
[Go to the Firewall policies page](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)
  2. Click **Create firewall rule**.
  3. On the _Create a firewall rule_ page, supply the following information: 
     * **Name** : `fw-allow-health-checks`
     * **Network** : Choose the VPC network.
     * **Priority** : Enter a number for the priority or 1000 by default.
     * **Direction of traffic** : Choose **ingress**.
     * **Action on match** : Choose **allow**.
     * **Targets** : Choose **Specified target tags** , and then enter `td-http-server` in the **Target tags** text box.
     * **Source filter** : Choose the correct IP range type.
     * **Source IP ranges** : `35.191.0.0/16,130.211.0.0/22`
     * **Destination filter** : Select the IP type.
     * **Protocols and ports** : Click **Specified ports and protocols** , then check `tcp` type in port `80`



###  gcloud 

  1. Create the firewall rule for the health check.
         
         gcloud compute firewall-rules create fw-allow-health-checks \
           --action ALLOW \
           --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags td-http-server \
           --rules tcp:80
         




### Creating the backend service

Create the backend service. If you use the Google Cloud CLI, you must designate it as a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service#create-backend-service) with a load balancing scheme of **INTERNAL_SELF_MANAGED**. Add the health check and a managed or unmanaged instance group to the backend service. Note that this example uses the managed instance group with the Compute Engine VM template that runs the sample HTTP service created in Creating the managed instance group.

###  Console 

  1. Go to the Cloud Service Mesh page in the Google Cloud console. 

[Go to the Cloud Service Mesh page](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. On the **Services** tab, click **Create Service**.

  3. Click **Continue**.

  4. For the service name, enter `td-vm-service`.

  5. Select the correct VPC network.

  6. Ensure that the **Backend type** is **Instance groups**.

  7. Select `td-demo-hello-world-mig`, which is the managed instance group you created that contains the backends for the `Hello World` test service.

  8. Enter the correct **Port numbers**.

  9. Choose **Utilization** or **Rate** as the **Balancing mode**. The default value is **Rate**.

  10. Click **Done**.

  11. Select the health check you created, or click **Create another health check** and make sure to select **HTTP** as the protocol.

  12. In **Connection draining timeout** , set the value to `30` seconds or longer.

  13. Click **Continue**.

  14. Click **Create**.




###  gcloud 

  1. Create the backend service.
         
         gcloud compute backend-services create td-vm-service \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED \
          --connection-draining-timeout=30s \
          --health-checks td-vm-health-check
         

  2. Add the backends to the backend service.
         
         gcloud compute backend-services add-backend td-vm-service \
           --instance-group td-demo-hello-world-mig \
           --instance-group-zone us-central1-a \
           --global
         




### Creating the routing rule map

The routing rule map defines how Cloud Service Mesh routes traffic in your mesh. As part of the routing rule map, you configure a virtual IP (VIP) address and a set of associated traffic management rules, such as host-based routing. When an application sends a request to the VIP, the Envoy proxy:

  1. Intercepts the request.
  2. Evaluates it according to the traffic management rules in the URL map.
  3. Elects a backend service based on the hostname in the request.
  4. Chooses a backend or endpoint associated with the selected backend service.
  5. Sends traffic to that backend or endpoint.



For more information on traffic management, see [Advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).

###  Console 

In the Google Cloud console, target proxy creation is combined with forwarding rule creation. When you create the forwarding rule, Google Cloud automatically creates a target HTTP proxy and attaches it to the URL map.

  1. Go to the Cloud Service Mesh page in the Google Cloud console. 

[Go to the Cloud Service Mesh page](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. On the **Routing rule maps** tab, click **Create Routing Rule Map**.

  3. Enter a name.

  4. Click **Add Forwarding Rule**.

  5. For the forwarding rule name, enter `td-vm-forwarding-rule`.

  6. Select your network.

  7. Select your **Internal IP**. Traffic sent to this IP address is intercepted by the Envoy proxy and sent to the appropriate service according to the host and path rules.

The forwarding rule is created as a global forwarding rule with the `load-balancing-scheme` set to `INTERNAL_SELF_MANAGED`.

  8. In the **Custom IP** field, type `10.0.0.1`. When your VM sends to this IP address, the Envoy proxy intercepts it and sends it to the appropriate backend service's endpoint according to the traffic management rules defined in the URL map.

Each forwarding rule in a VPC network must have a unique IP address and port per VPC network. If you create more than one forwarding rule with the same IP address and port in a particular VPC network, only the first forwarding rule is valid. Others are ignored. If `10.0.0.1` is not available in your network, choose a different IP address.

  9. Make sure that the **Port** is set to `80`.

  10. Click **Save**.

  11. In the **Routing rules** section, select **Simple host and path rule**.

  12. In the Host and path rules section, select `td-vm-service` as the Service.

  13. Click Add host and path rule.

  14. In **Hosts** , enter `hello-world`.

  15. In **Service** , select `td-vm-service`.

  16. Click **Save**.




###  gcloud 

  1. Create a URL map that uses the backend service `td-vm-service` as the default.
         
         gcloud compute url-maps create td-vm-url-map \
            --default-service td-vm-service
         

  2. Create a path matcher and a host rule to route traffic for your service based on hostname and a path. This example uses `td-vm-service` as the service name and a default path matcher that matches all path requests for this host (`/*`).
         
         gcloud compute url-maps add-path-matcher td-vm-url-map \
            --default-service td-vm-service \
            --path-matcher-name td-vm-path-matcher
         
         
         gcloud compute url-maps add-host-rule td-vm-url-map \
            --path-matcher-name=td-vm-path-matcher \
            --hosts=hello-world
         

  3. Create the target HTTP proxy.
         
         gcloud compute target-http-proxies create td-vm-proxy \
            --url-map=td-vm-url-map
         

  4. Create the forwarding rule.

The forwarding rule must be global and must be created with the value of `load-balancing-scheme` set to `INTERNAL_SELF_MANAGED`.
         
         gcloud compute forwarding-rules create td-vm-forwarding-rule \
            --global \
            --load-balancing-scheme=INTERNAL_SELF_MANAGED \
            --address=10.0.0.1 \
            --target-http-proxy=td-vm-proxy \
            --ports=80 \
            --network=default
         




At this point, Cloud Service Mesh is configured to load balance traffic for the services specified in the URL map across backends in the managed instance group.

## Verifying the configuration

In this final portion of the Cloud Service Mesh setup guide for Compute Engine VMs, you test that traffic sent from the client VM destined to the forwarding rule VIP is intercepted and redirected to the Envoy proxy, which then routes your request to the VMs hosting the `Hello World` service.

To do this, you log into the client VM, that has been configured to intercept traffic and redirect it to Envoy. You send a `curl` request to the VIP associated with your routing rule map. Envoy inspects the `curl` request, determines which service it should resolve to, and sends the request to an backend associated with that service.

  1. In the Google Cloud console, go to the Instance Groups page. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the `td-vm-mig-us-central1` instance group.
  3. In the VM summary section, under **Connect** , click **SSH**.
  4. After you are logged in to the client VM, use the `curl` tool to send a request to the `Hello World` service through Envoy:


    
    
    curl -H "Host: hello-world" http://10.0.0.1/
    

When you issue this command repeatedly, you should see different HTML responses containing the hostnames of backends in the `Hello World` managed instance group. This is because Envoy is using round robin load balancing, the default load balancing algorithm, when sending traffic to the `Hello World` service's backends.

## What's next

  * Learn about [advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).
  * Learn how to set up [observability with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-envoy).
  * Learn how to [troubleshoot Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting).
  * Learn about advanced deployment options in the [Automated Envoy deployment option guide](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-vms-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
