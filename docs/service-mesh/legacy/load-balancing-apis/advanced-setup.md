---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-setup/
title: Set up advanced configurations \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:53.862943+00:00
---

# Set up advanced configurations  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-setup/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up advanced configurations

This document contains notes that might be helpful when configuring Cloud Service Mesh.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## Configuring a single Compute Engine VM for Cloud Service Mesh

Use this procedure as an example of how sidecar proxy deployment and traffic interception can be implemented to provide a VM with access to Cloud Service Mesh services.

To use this procedure, you need to have Docker installed. Follow [Docker's instructions](https://docs.docker.com/engine/install/) for installing Docker Engine.

If you are following this process to configure Cloud Service Mesh on a single VM, some setup tasks require that you have access to a Linux host. The host can be a local machine or a VM running on your Virtual Private Cloud network.

First, download and prepare the configuration files and sample scripts.

  1. Log in to the Linux host you are using during the setup process.

  2. Download the archive of required files to the Linux host and untar the archive:
         
         wget https://storage.googleapis.com/traffic-director/traffic-director-xdsv3.tar.gz
         tar -xzvf traffic-director-xdsv3.tar.gz; cd traffic-director-xdsv3
         

The archive contains the following files:

     * **sidecar.env** – Config file with environment variables.
     * **iptables.sh** – Script for setting up netfilter rules.
     * **bootstrap_template.yaml** – Bootstrap template file for Envoy.
     * **run.sh** – Top-level script that uses the `sidecar.env` configuration file to set up `iptables` for interception and to run the Envoy sidecar proxy.
  3. On each host that runs a sidecar proxy, create a system user to run the Envoy proxy process. This is the Envoy proxy user. Login is disabled for the Envoy proxy user.
         
         sudo adduser --system --disabled-login envoy
         

  4. Edit the `sidecar.env` file to modify the configuration. Read the inline comments in the configuration file for a detailed description of each variable.

     1. In the `sidecar.env` file, set the `ENVOY_USER` variable to the username that you choose to be the Envoy proxy user.



Next, for each VM host that runs applications using Cloud Service Mesh, perform the following steps:

  1. Copy the entire `traffic-director-xdsv3` directory with the modified `sidecar.env` file to each VM host running applications that you expect to use Cloud Service Mesh.
  2. Add the `run.sh` script to your system's startup script, which ensures that the script is run after every VM reboot.
  3. On each VM host, run the `run.sh` script:
         
         cd traffic-director-xdsv3
         sudo ./run.sh start
         

  4. Verify that the Envoy proxy started correctly.
         
         sudo ./run.sh status
         

You should see the following output:
         
         OK: Envoy seems to be running.
         OK: Traffic interception seems to be enabled.
         

You can verify traffic interception direction by using the following:
         
         sudo iptables -S -t nat | grep ISTIO_REDIRECT
         

The expected output is: 
         
         -N ISTIO_REDIRECT
         -A ISTIO_OUTPUT -j ISTIO_REDIRECT
         -A ISTIO_REDIRECT -p tcp -j REDIRECT --to-ports 15001`
         


**Note:** With this configuration, all TCP traffic, except traffic on port tcp/22, is intercepted by the sidecar proxy. Traffic to TCP services that are not configured in Cloud Service Mesh are silently discarded by the proxy. To avoid losing traffic, follow the Advanced traffic interception configuration section below.

## Routing rule maps

There are two ways to configure routing in a routing rule map.

You can enable routing based on the actual destination VIP and port of the service. If you configure a VIP of your service as the `IPAddress` parameter of the forwarding rule, only traffic destined to this address, and the associated port, is matched, and routed, based on the host and path parameters specified in the URL map.

Alternatively, you can set the address of your forwarding rule to `0.0.0.0`. This will configure the proxies to only match traffic based on the destination port, regardless of the destination IP address of the request. Traffic is then routed based on the host and path parameters specified in the URL map.

Based on these two approaches, hostnames, as configured in the host rules, associated with a destination VIP and port pair, or with a destination port (when VIP is `0.0.0.0`), must be unique within your service mesh configuration. That is, you cannot have two different services, with different sets of backends, that both use the same hostname.

Regardless of the method selected, traffic to the VIP that your service hostname/FQDN resolves to, and the port that your service is listening on, must be intercepted and redirected to the sidecar proxy. Refer to Configuring a single Compute Engine VM for Cloud Service Mesh for full host configuration details.

Each forwarding rule in a VPC network must have a unique combination of IP address and port per VPC network, including the `0.0.0.0` address. If you create more than one forwarding rule with the same IP address and port in a particular VPC network, only the first forwarding rule is valid. The others are ignored.

To avoid losing traffic, follow the Advanced traffic interception configuration section below.

## Advanced traffic interception configuration

If your VMs run applications that need access to services configured by Cloud Service Mesh, you must install a sidecar proxy and configure traffic interception on the VMs to allow the sidecar proxy to manage traffic routing to the backends of those services.

**Note:** If the managed instance group VMs serve as a backend only and its applications do not need access to Cloud Service Mesh services, you can skip this section.

If intercepting all outgoing VM traffic is not acceptable for your deployment, you can redirect specific traffic to the sidecar proxy, while the rest of the traffic will follow the regular route defined by your host networking configuration.

To achieve this, modify the Compute Engine VM host setup in [Cloud Service Mesh setup with VMs and manual Envoy deployment](https://docs.cloud.google.com/service-mesh/docs/service-routing/set-up-gce-vms) procedure as follows:

  1. Decide on the range of IP addresses that Cloud Service Mesh-controlled services should resolve to. Traffic destined to these IP addresses is intercepted and redirected to the sidecar proxy. The range is specific to your deployment.

  2. In the `sidecar.env` file, set the value of `SERVICE_CIDR` to this range. Traffic to these IP addresses is redirected by netfilter to a sidecar proxy and load-balanced according to the configuration provided by Cloud Service Mesh.

  3. The sidecar proxy is not strictly required to run as a dedicated user that is excluded from traffic interception. However, this is still recommended.

  4. After you execute the `run.sh` script, as directed in the main procedure, `iptables` is configured for the interception and redirection of this specific range, only.

  5. Run the following command to verify that the netfilter is configured correctly. For ${SERVICE_CIDR}, substitute the value you configured as the intercepted IP address range.
         
         sudo iptables -L -t nat | grep -E "(ISTIO_REDIRECT).+${SERVICE_CIDR})"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
