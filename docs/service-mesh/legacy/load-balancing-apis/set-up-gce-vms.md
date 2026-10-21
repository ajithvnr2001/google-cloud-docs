---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms/
title: Set up VMs using manual Envoy deployment \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:59.606369+00:00
---

# Set up VMs using manual Envoy deployment  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up VMs using manual Envoy deployment

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document is for network administrators who want to set up Cloud Service Mesh manually. The manual process is a legacy mechanism that is intended only for advanced users who are setting up Cloud Service Mesh with the load balancing APIs.

We strongly recommend that you set up Cloud Service Mesh using the [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview) rather than the older load balancing APIs. If you must use the load balancing APIs, we recommend using [automated Envoy deployment](https://docs.cloud.google.com/service-mesh/docs/service-routing/set-up-gce-vms-auto) rather than the manual process that is described on this page.

Before you follow the instructions in this guide, complete the prerequisite tasks described in [Prepare to set up on service routing APIs with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/docs/onboarding/prepare-service-routing-envoy-proxyless).

This guide shows you how to manually deploy a data plane that consists of Envoy sidecar proxies with Compute Engine virtual machines (VMs), configure it using Cloud Service Mesh, and verify your setup to ensure that it's functioning correctly. This process involves:

  1. Creating a test service.
  2. Deploying a simple data plane on Compute Engine using Envoy proxies.
  3. Setting up Cloud Service Mesh using Compute Engine APIs, which enable Cloud Service Mesh to configure your Envoy sidecar proxies.
  4. Log in to a VM that is running an Envoy proxy and send a request to a load-balanced backend through the Envoy proxy.



The configuration examples in this document are for demonstration purposes. For a production environment, you might need to deploy additional components, based on your environment and requirements.

## Overview of the configuration process

This section provides the manual configuration process for services that run on Compute Engine VMs. The configuration process for the client VMs consists of setting up a sidecar proxy and traffic interception on a Compute Engine VM host. Then you configure load balancing using Google Cloud load balancing APIs.

This section provides information about how to obtain and inject Envoy proxies from third-party sources that are not managed by Google.

When an application sends traffic to the service configured in Cloud Service Mesh, the traffic is intercepted and redirected to the xDS API-compatible sidecar proxy and then load balanced to the backends according to the configuration in the Google Cloud load balancing components. For more information on host networking and traffic interception, read [Sidecar proxy traffic interception in Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/traffic-management/service-discovery#traffic-interception-host-networking).

For each VM host that requires access to Cloud Service Mesh services, perform the following steps:

  1. Assign a service account to the VM.

  2. Set the API access scope of the VM to allow full access to the Google Cloud APIs.

     * When you create the VMs, under **Identity and API access** , click **Allow full access to all Cloud APIs**. 

[Go to the VM instances page](https://console.cloud.google.com/compute/instances).

     * With the gcloud CLI, specify the following:

`--scopes=https://www.googleapis.com/auth/cloud-platform`.

  3. Allow outgoing connections to `trafficdirector.googleapis.com` (TCP, port 443) from the VM, so that the sidecar proxy can connect to the Cloud Service Mesh control plane over gRPC. Outgoing connections to port 443 are enabled by default.

  4. Deploy an xDS API-compatible sidecar proxy (such as Envoy), with a bootstrap configuration pointing to `trafficdirector.googleapis.com:443` as its xDS server. To obtain a sample bootstrap configuration file, open [the compressed file traffic-director-xdsv3.tar.gz](https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz) and modify the `bootstrap_template.yaml` file to suit your needs.

  5. Redirect IP traffic that is destined to the services to the sidecar proxy interception listener port.

     * The sidecar proxy interception listener port is defined as `TRAFFICDIRECTOR_INTERCEPTION_PORT` in the proxy's bootstrap metadata configuration and is set to 15001 in the [sample bootstrap configuration file in this compressed file](https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz).
     * The [Istio `iptables.sh` script in the compressed file](https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz) can be used to set up traffic interception.



## Create the `Hello World` test service

This section shows you how to create a simple test service that returns the hostname of the VM that served the request from the client. The test service is uncomplicated; it's a web server deployed across a Compute Engine managed instance group.

### Create the instance template

The instance template that you create configures a sample apache2 web server by using the `startup-script` parameter.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.
  3. In the fields, enter the following information: 
     * **Name** : `td-demo-hello-world-template`
     * **Boot disk** : Debian GNU/Linux 10 (buster)
     * **Service account** : Compute Engine default service account
     * **Access scopes** : Allow full access to all Cloud APIs
  4. Click **Management, Security, Disks, Networking, Sole Tenancy**.
  5. On the **Networking** tab, in the **Network tags** field, add the `td-http-server` tag.
  6. On the **Management** tab, copy the following script into the **Startup script** field.
         
         #! /bin/bash
         sudo apt-get update -y
         sudo apt-get install apache2 -y
         sudo service apache2 restart
         echo '<!doctype html><html><body><h1>'`/bin/hostname`'</h1></body></html>' | sudo tee /var/www/html/index.html
         

  7. Click **Create**.




###  gcloud 

Create the instance template:
    
    
    gcloud compute instance-templates create td-demo-hello-world-template \
      --machine-type=n1-standard-1 \
      --boot-disk-size=20GB \
      --image-family=debian-10 \
      --image-project=debian-cloud \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --tags=td-http-server \
      --metadata=startup-script="#! /bin/bash
    sudo apt-get update -y
    sudo apt-get install apache2 -y
    sudo service apache2 restart
    sudo mkdir -p /var/www/html/
    echo '<!doctype html><html><body><h1>'`/bin/hostname`'</h1></body></html>' | sudo tee /var/www/html/index.html"
    

### Create the managed instance group

In this section, you specify that the managed instance group always has two instances of the test service. This is for demonstration purposes. Cloud Service Mesh supports autoscaled managed instance groups.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**.
  3. Select **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
  4. Enter `td-demo-hello-world-mig` for the name for the managed instance group, and select the `us-central1-a` zone.
  5. Under **Instance template** , select `td-demo-hello-world-template`, which is the instance template you created.
  6. Under **Autoscaling mode** , select **Don't autoscale**.
  7. Under **Number of instances** , specify at least two as the number of instances that you want to create in the group.
  8. Click **Create**.



###  gcloud 

Use the gcloud CLI to create a managed instance group with the instance template you previously created.
    
    
    gcloud compute instance-groups managed create td-demo-hello-world-mig \
      --zone us-central1-a \
      --size=2 \
      --template=td-demo-hello-world-template
    

## Create the instance template and managed instance group where Envoy is deployed

Use the instructions in this section to manually create an instance template and managed instance group for Cloud Service Mesh. [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) create new backend VMs by using autoscaling.

This example shows how to:

  * Create a VM template with a full Envoy configuration and a sample service that serves its hostname by using the HTTP protocol.
  * Configure a managed instance group using this template.



### Create the instance template

First, create the Compute Engine VM instance template. This template auto-configures the Envoy sidecar proxy and sample apache2 web service through the `startup-script` parameter.

**Note:** You must provide a PROJECT_NUMBER and NETWORK_NAME.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.
  3. Fill in the fields as follows:

     * **Name:** td-vm-template
     * **Boot disk:** Debian GNU/Linux 10 (buster)
     * **Service account:** Compute Engine default service account
     * **Access scopes:** Allow full access to all Cloud APIs
  4. Under **Firewall** , select the boxes next to **Allow HTTP traffic** and **Allow HTTPS traffic**.

  5. Click **Management, Security, Disks, Networking, Sole Tenancy**.

  6. On the **Management** tab, copy the following script into the **[Startup script](https://docs.cloud.google.com/compute/docs/startupscript)** field.
         
         #! /usr/bin/env bash
         
         # Set variables
         export ENVOY_USER="envoy"
         export ENVOY_USER_UID="1337"
         export ENVOY_USER_GID="1337"
         export ENVOY_USER_HOME="/opt/envoy"
         export ENVOY_CONFIG="${ENVOY_USER_HOME}/config.yaml"
         export ENVOY_PORT="15001"
         export ENVOY_ADMIN_PORT="15000"
         export ENVOY_TRACING_ENABLED="false"
         export ENVOY_XDS_SERVER_CERT="/etc/ssl/certs/ca-certificates.crt"
         export ENVOY_ACCESS_LOG="/dev/stdout"
         export ENVOY_NODE_ID="$(cat /proc/sys/kernel/random/uuid)~$(hostname -i)"
         export BOOTSTRAP_TEMPLATE="${ENVOY_USER_HOME}/bootstrap_template.yaml"
         export GCE_METADATA_SERVER="169.254.169.254/32"
         export INTERCEPTED_CIDRS="*"
         export GCP_PROJECT_NUMBER=PROJECT_NUMBER
         export VPC_NETWORK_NAME=NETWORK_NAME
         export GCE_ZONE=$(curl -sS -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone | cut -d"/" -f4)
         
         # Create system user account for Envoy binary
         sudo groupadd ${ENVOY_USER} \
          --gid=${ENVOY_USER_GID} \
          --system
         sudo adduser ${ENVOY_USER} \
          --uid=${ENVOY_USER_UID} \
          --gid=${ENVOY_USER_GID} \
          --home=${ENVOY_USER_HOME} \
          --disabled-login \
          --system
         
         # Download and extract the Cloud Service Mesh tar.gz file
         cd ${ENVOY_USER_HOME}
         sudo curl -sL https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz -o traffic-director-xdsv3.tar.gz
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/bootstrap_template.yaml \
          -C bootstrap_template.yaml \
          --strip-components 1
         sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/iptables.sh \
          -C iptables.sh \
          --strip-components 1
         sudo rm traffic-director-xdsv3.tar.gz
         
         # Generate Envoy bootstrap configuration
         cat "${BOOTSTRAP_TEMPLATE}" \
          | sed -e "s|ENVOY_NODE_ID|${ENVOY_NODE_ID}|g" \
          | sed -e "s|ENVOY_ZONE|${GCE_ZONE}|g" \
          | sed -e "s|VPC_NETWORK_NAME|${VPC_NETWORK_NAME}|g" \
          | sed -e "s|CONFIG_PROJECT_NUMBER|${GCP_PROJECT_NUMBER}|g" \
          | sed -e "s|ENVOY_PORT|${ENVOY_PORT}|g" \
          | sed -e "s|ENVOY_ADMIN_PORT|${ENVOY_ADMIN_PORT}|g" \
          | sed -e "s|XDS_SERVER_CERT|${ENVOY_XDS_SERVER_CERT}|g" \
          | sed -e "s|TRACING_ENABLED|${ENVOY_TRACING_ENABLED}|g" \
          | sed -e "s|ACCESSLOG_PATH|${ENVOY_ACCESS_LOG}|g" \
          | sed -e "s|BACKEND_INBOUND_PORTS|${BACKEND_INBOUND_PORTS}|g" \
          | sudo tee "${ENVOY_CONFIG}"
         
         # Install Envoy binary
         curl -sL "https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key" | sudo gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg
         echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check
         echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/debian $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/getenvoy.list
         sudo apt update
         sudo apt -y install getenvoy-envoy
         
         # Run Envoy as systemd service
         sudo systemd-run --uid=${ENVOY_USER_UID} --gid=${ENVOY_USER_GID} \
          --working-directory=${ENVOY_USER_HOME} --unit=envoy.service \
          bash -c "/usr/bin/envoy --config-path ${ENVOY_CONFIG} | tee"
         
         # Configure iptables for traffic interception and redirection
         sudo ${ENVOY_USER_HOME}/iptables.sh \
          -p "${ENVOY_PORT}" \
          -u "${ENVOY_USER_UID}" \
          -g "${ENVOY_USER_GID}" \
          -m "REDIRECT" \
          -i "${INTERCEPTED_CIDRS}" \
          -x "${GCE_METADATA_SERVER}"
         

  7. Click **Create** to create the template.




###  gcloud 

Create the instance template.
    
    
    gcloud compute instance-templates create td-vm-template \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --tags=http-td-tag,http-server,https-server \
      --image-family=debian-10 \
      --image-project=debian-cloud \
      --metadata=startup-script='#! /usr/bin/env bash
    
    # Set variables
    export ENVOY_USER="envoy"
    export ENVOY_USER_UID="1337"
    export ENVOY_USER_GID="1337"
    export ENVOY_USER_HOME="/opt/envoy"
    export ENVOY_CONFIG="${ENVOY_USER_HOME}/config.yaml"
    export ENVOY_PORT="15001"
    export ENVOY_ADMIN_PORT="15000"
    export ENVOY_TRACING_ENABLED="false"
    export ENVOY_XDS_SERVER_CERT="/etc/ssl/certs/ca-certificates.crt"
    export ENVOY_ACCESS_LOG="/dev/stdout"
    export ENVOY_NODE_ID="$(cat /proc/sys/kernel/random/uuid)~$(hostname -i)"
    export BOOTSTRAP_TEMPLATE="${ENVOY_USER_HOME}/bootstrap_template.yaml"
    export GCE_METADATA_SERVER="169.254.169.254/32"
    export INTERCEPTED_CIDRS="*"
    export GCP_PROJECT_NUMBER=PROJECT_NUMBER
    export VPC_NETWORK_NAME=NETWORK_NAME
    export GCE_ZONE=$(curl -sS -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/zone | cut -d"/" -f4)
    
    # Create system user account for Envoy binary
    sudo groupadd ${ENVOY_USER} \
      --gid=${ENVOY_USER_GID} \
      --system
    sudo adduser ${ENVOY_USER} \
      --uid=${ENVOY_USER_UID} \
      --gid=${ENVOY_USER_GID} \
      --home=${ENVOY_USER_HOME} \
      --disabled-login \
      --system
    # Download and extract the Cloud Service Mesh tar.gz file
    cd ${ENVOY_USER_HOME}
    sudo curl -sL https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz -o traffic-director-xdsv3.tar.gz
    sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/bootstrap_template.yaml \
      -C bootstrap_template.yaml \
      --strip-components 1
    sudo tar -xvzf traffic-director-xdsv3.tar.gz traffic-director-xdsv3/iptables.sh \
      -C iptables.sh \
      --strip-components 1
    sudo rm traffic-director-xdsv3.tar.gz
    
    # Generate Envoy bootstrap configuration
    cat "${BOOTSTRAP_TEMPLATE}" \
      | sed -e "s|ENVOY_NODE_ID|${ENVOY_NODE_ID}|g" \
      | sed -e "s|ENVOY_ZONE|${GCE_ZONE}|g" \
      | sed -e "s|VPC_NETWORK_NAME|${VPC_NETWORK_NAME}|g" \
      | sed -e "s|CONFIG_PROJECT_NUMBER|${GCP_PROJECT_NUMBER}|g" \
      | sed -e "s|ENVOY_PORT|${ENVOY_PORT}|g" \
      | sed -e "s|ENVOY_ADMIN_PORT|${ENVOY_ADMIN_PORT}|g" \
      | sed -e "s|XDS_SERVER_CERT|${ENVOY_XDS_SERVER_CERT}|g" \
      | sed -e "s|TRACING_ENABLED|${ENVOY_TRACING_ENABLED}|g" \
      | sed -e "s|ACCESSLOG_PATH|${ENVOY_ACCESS_LOG}|g" \
      | sed -e "s|BACKEND_INBOUND_PORTS|${BACKEND_INBOUND_PORTS}|g" \
      | sudo tee "${ENVOY_CONFIG}"
    
    # Install Envoy binary
    curl -sL "https://deb.dl.getenvoy.io/public/gpg.8115BA8E629CC074.key" | sudo gpg --dearmor -o /usr/share/keyrings/getenvoy-keyring.gpg
    echo a077cb587a1b622e03aa4bf2f3689de14658a9497a9af2c427bba5f4cc3c4723 /usr/share/keyrings/getenvoy-keyring.gpg | sha256sum --check
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/getenvoy-keyring.gpg] https://deb.dl.getenvoy.io/public/deb/debian $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/getenvoy.list
    sudo apt update
    sudo apt -y install getenvoy-envoy
    
    # Run Envoy as systemd service
    sudo systemd-run --uid=${ENVOY_USER_UID} --gid=${ENVOY_USER_GID} \
      --working-directory=${ENVOY_USER_HOME} --unit=envoy.service \
      bash -c "/usr/bin/envoy --config-path ${ENVOY_CONFIG} | tee"
    
    # Configure iptables for traffic interception and redirection
    sudo ${ENVOY_USER_HOME}/iptables.sh \
      -p "${ENVOY_PORT}" \
      -u "${ENVOY_USER_UID}" \
      -g "${ENVOY_USER_GID}" \
      -m "REDIRECT" \
      -i "${INTERCEPTED_CIDRS}" \
      -x "${GCE_METADATA_SERVER}"
    '
    

### Create the managed instance group

If you don't have a managed instance group with services running, [create a managed instance group](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create), using a VM template such as the one shown in the previous section. This example uses the instance template created in the previous section to demonstrate functionality. You don't have to use the instance template.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create an instance group**. By default, you see the page for creating a managed instance group.
  3. Choose **New managed instance group (stateless)**. For more information, see [Stateless or stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#stateless_or_stateful_migs).
  4. Enter `td-vm-mig-us-central1` for the name for the managed instance group, and select the `us-central1-a` zone.
  5. Under **Instance template** , select the instance template you created.
  6. Specify 2 as the number of instances that you want to create in the group.
  7. Click **Create**.



###  gcloud 

Use the gcloud CLI to create a managed instance group with the instance template you previously created.
    
    
    gcloud compute instance-groups managed create td-vm-mig-us-central1 \
        --zone us-central1-a --size=2 --template=td-vm-template
    

## Configure Cloud Service Mesh with Google Cloud load balancing components

The instructions in this section show you how to configure Cloud Service Mesh so that your Envoy proxies load balance outbound traffic across two backend instances. You configure the following components:

  * A health check. For more information about health checks, read [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) and [Create health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
  * A firewall rule, to enable the health check probes to reach the backends. For more information, see [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).
  * A backend service. For more information about backend services, see [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).
  * A routing rule map. This includes creating a forwarding rule and a URL map. For more information, see [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rules) and [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/https/url-map).



### Create the health check

Use the following instructions to create a health check. For more information, refer to [Create health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).

###  Console 

  1. In the Google Cloud console, go to the **Health checks** page.

[Go to Health checks](https://console.cloud.google.com/compute/healthChecks)

  2. Click **Create health check**.
  3. For the name, enter `td-vm-health-check`.
  4. For the protocol, select **HTTP**.
  5. Click **Create**.



###  gcloud 

  1. Create the health check:
         
         gcloud compute health-checks create http td-vm-health-check
         

  2. Create the firewall rule:
         
         gcloud compute firewall-rules create fw-allow-health-checks \
           --action ALLOW \
           --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags http-td-tag,http-server,https-server \
           --rules tcp
         




### Create the backend service

If you use the Google Cloud CLI, you must designate the backend service as a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service#create-backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED`. Add the health check and a managed or unmanaged instance group to the backend service. Note that this example uses the managed instance group with Compute Engine VM template that runs the sample HTTP service created in Create the managed instance group.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

  2. On the **Services** tab, click **Create Service**.
  3. Click **Continue**.
  4. For the service name, enter `td-vm-service`.
  5. Select the correct VPC network.
  6. Ensure that the **Backend type** is **Instance groups**.
  7. Select the managed instance group you created.
  8. Enter the correct **Port numbers**.
  9. Choose **Utilization** or **Rate** as the **Balancing mode**. The default value is **Rate**.
  10. Click **Done**.
  11. Select the health check you created.
  12. Click **Save and continue**.
  13. Click **Create**.



###  gcloud 

  1. Create the backend service:
         
         gcloud compute backend-services create td-vm-service \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --health-checks td-vm-health-check
         

  2. Add the backends to the backend service:
         
         gcloud compute backend-services add-backend td-vm-service \
            --instance-group td-demo-hello-world-mig \
            --instance-group-zone us-central1-a \
            --global
         




### Create the routing rule map

The routing rule map defines how Cloud Service Mesh routes traffic in your mesh.

Use these instructions to create the route rule, forwarding rule, target proxy, and internal IP address for your Cloud Service Mesh configuration.

Traffic sent to the internal IP address is intercepted by the Envoy proxy and sent to the appropriate service according to the host and path rules.

The forwarding rule is created as a global forwarding rule with the `load-balancing-scheme` set to `INTERNAL_SELF_MANAGED`.

You can set the address of your forwarding rule to `0.0.0.0`. If you do, traffic is routed based on the HTTP hostname and path information configured in the URL map, regardless of the actual destination IP address of the request. In this case, the hostnames of your services, as configured in the host rules, must be unique within your service mesh configuration. That is, you cannot have two different services, with different sets of backends, that both use the same hostname.

Alternatively, you can enable routing based on the actual destination VIP of the service. If you configure the VIP of your service as an `address` parameter of the forwarding rule, only requests destined to this address are routed based on the HTTP parameters specified in the URL map.

This example uses `10.0.0.1` as the address parameter, meaning that routing for your service is performed based on the actual destination VIP of the service.

**Note:** Regardless of the method selected, traffic to the VIP address that your service hostname resolves to must be intercepted by the sidecar proxy on the host that needs access to it. Refer to [Configuring a single Compute Engine VM for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-setup#per_host_config) for full host configuration details.**Note:** Each forwarding rule in a VPC network must have a unique combination of IP address and port per VPC network, including the `0.0.0.0` address. If you create more than one forwarding rule with the same IP address and port in a particular VPC network, only the first forwarding rule is valid. The others are ignored.

###  Console 

In the Google Cloud console, the target proxy is combined with the forwarding rule. When you create the forwarding rule, Google Cloud automatically creates a target HTTP proxy and attaches it to the URL map.

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

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

  12. In the **Host and path rules** section, select `td-vm-service` as the Service.

  13. Click **Add host and path rule**.

  14. In **Hosts** , enter `hello-world`.

  15. In **Service** , select `td-vm-service`.

  16. Click **Save**.




###  gcloud 

  1. Create a URL map that uses the backend service:
         
         gcloud compute url-maps create td-vm-url-map \
            --default-service td-vm-service
         

  2. Create a URL map path matcher and a host rule to route traffic for your service based on hostname and a path. This example uses `service-test` as the service name and a default path matcher that matches all path requests for this host (`/*`).
         
         gcloud compute url-maps add-path-matcher td-vm-url-map \
            --default-service td-vm-service --path-matcher-name td-vm-path-matcher
         
         
         gcloud compute url-maps add-host-rule td-vm-url-map --hosts service-test \
            --path-matcher-name td-vm-path-matcher \
            --hosts hello-world
         

  3. Create the target HTTP proxy:
         
         gcloud compute target-http-proxies create td-vm-proxy \
            --url-map td-vm-url-map
         

  4. Create the forwarding rule. The forwarding rule must be global and must be created with the value of `load-balancing-scheme` set to `INTERNAL_SELF_MANAGED`.
         
         gcloud compute forwarding-rules create td-vm-forwarding-rule \
            --global \
            --load-balancing-scheme=INTERNAL_SELF_MANAGED \
            --address=10.0.0.1 \
            --target-http-proxy=td-vm-proxy \
            --ports 80 \
            --network default
         




At this point, Cloud Service Mesh is configured to load balance traffic for the services specified in the URL map across backends in the managed instance group.

## Verify the configuration

In this final portion of the Cloud Service Mesh setup guide for Compute Engine VMs, you test that traffic sent from the client VM destined to the forwarding rule VIP is intercepted and redirected to the Envoy proxy, which then routes your request to the VMs hosting the `Hello World` service.

First, verify that the backends are healthy by using the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Service Mesh** page.

[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)

The **Summary** tells you whether the services are healthy.

  2. Click the name of a service. The **Service details** page has information about the health of the backends.
  3. If the backends are unhealthy, you can reset them by clicking the name of the backends and then clicking **Reset** on the **VM instance details page**.



###  gcloud 

Use the [`compute backend-services get-health`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/get-health) command to verify that the backends are healthy:
    
    
    gcloud compute backend-services get-health td-vm-service \
        --global \
        --format=get(name, healthStatus)
    

After verifying the health states of your backends, log into the client VM that has been configured to intercept traffic and redirect it to Envoy. Send a `curl` request to the VIP associated with your routing rule map. Envoy inspects the `curl` request, determines which service it should resolve to, and sends the request to a backend associated with that service.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the `td-vm-mig-us-central1` instance group.
  3. Under **Connect** , click **SSH**.
  4. After you are logged in to the client VM, use the `curl` tool to send a request to the `Hello World` service through Envoy:
         
         curl -H "Host: hello-world" http://10.0.0.1/
         




When you issue this command repeatedly, you will see different HTML responses containing the hostnames of backends in the `Hello World` managed instance group. This is because Envoy is using round robin load balancing, the default load balancing algorithm, when sending traffic to the `Hello World` service's backends.

When the configuration is complete, each Compute Engine VM that has a sidecar proxy can access services configured in Cloud Service Mesh using the HTTP protocol.

If you followed the specific examples in this guide by using the Compute Engine VM template with the demonstration HTTP server and service hostname `service-test`, use these steps to verify the configuration:

  1. Sign in to one of the VM hosts that has a sidecar proxy installed.
  2. Execute the command `curl -H 'Host: service-test' 10.0.0.1`. This request returns the hostname of the managed instance group backend that served the request.



In step 2, note that you can use any IP address. For example, the command `curl -I -H 'Host: service-test' 1.2.3.4` would work in Step 2.

This is because the forwarding rule has the address parameter set to `0.0.0.0`, which instructs Cloud Service Mesh to match based on the host defined in the URL map. In the example configuration, the hostname is `service-test`.

## What's next

  * Learn about [advanced traffic management](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).
  * Learn how to [troubleshoot Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting).
  * Learn how to set up [observability with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-envoy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
