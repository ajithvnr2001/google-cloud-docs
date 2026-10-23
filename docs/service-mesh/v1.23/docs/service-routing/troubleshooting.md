---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/troubleshooting/
title: Troubleshoot Envoy deployments \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:36.716915+00:00
---

# Troubleshoot Envoy deployments  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/troubleshooting/

You are viewing archived v1.23 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Envoy deployments

This guide provides information to help you resolve configuration issues with Envoy clients when you run Cloud Service Mesh with Google APIs. For information about how to use the Client Status Discovery Service (CSDS) API to help you investigate issues with Cloud Service Mesh, see [Understanding Cloud Service Mesh client status](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/client-status).

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## Determining the version of Envoy installed on a VM

Use these instructions to verify which version of Envoy is running on a virtual machine (VM) instance.

To verify or check the Envoy version, you can do one of the following:

Check the guest attributes of the VM under the path `gce-service-proxy/proxy-version`:
    
    
      gcloud compute --project cloud-vm-mesh-monitoring instances get-guest-attributes INSTANCE_NAME   
    
          --zone ZONEc --query-path=gce-service-proxy/proxy-version
    
    
    
    NAMESPACE          KEY            VALUE
      gce-service-proxy  proxy-version  dc78069b10cc94fa07bb974b7101dd1b42e2e7bf/1.15.1-dev/Clean/RELEASE/BoringSSL
      

Check the Cloud Logging instance logs from the VM instance details Logging page in the Google Cloud console with a query such as this:
    
    
      resource.type="gce_instance"
      resource.labels.instance_id="3633122484352464042"
      jsonPayload.message:"Envoy version"
      

You receive a response such as this:
    
    
      {
        "insertId": "9zy0btf94961a",
        "jsonPayload": {
          "message": "Envoy Version: dc78069b10cc94fa07bb974b7101dd1b42e2e7bf/1.15.1-dev/Clean/RELEASE/BoringSSL",
          "localTimestamp": "2021-01-12T11:39:14.3991Z"
        },
        "resource": {
          "type": "gce_instance",
          "labels": {
            "zone": "asia-southeast1-b",
            "instance_id": "3633122484352464042",
            "project_id": "cloud-vm-mesh-monitoring"
          }
        },
        "timestamp": "2021-01-12T11:39:14.399200504Z",
        "severity": "INFO",
        "logName": "projects/cloud-vm-mesh-monitoring/logs/service-proxy-agent",
        "receiveTimestamp": "2021-01-12T11:39:15.407023427Z"
      }
      

Use SSH to connect to a VM and check the binary version:
    
    
      YOUR_USER_NAME@backend-mig-5f5651e1-517a-4269-b457-f6bdcf3d98bc-m3wt:~$ /usr/local/bin/envoy --version
    
    
    
    /usr/local/bin/envoy  version: dc78069b10cc94fa07bb974b7101dd1b42e2e7bf/1.15.1-dev/Clean/RELEASE/BoringSSL
      

Use SSH to connect to a VM and the admin interface as root:
    
    
      root@backend-mig-5f5651e1-517a-4269-b457-f6bdcf3d98bc-m3wt:~# curl localhost:15000/server_info
      {
       "version": "dc78069b10cc94fa07bb974b7101dd1b42e2e7bf/1.15.1-dev/Clean/RELEASE/BoringSSL",
       "state": "LIVE",
       "hot_restart_version": "disabled",
       ...
      }
      

## Envoy log locations

To troubleshoot some issues, you need to examine the Envoy proxy logs.

You can use SSH to connect to the VM instance to obtain the log file. The path is likely to be the following.
    
    
      /var/log/envoy/envoy.err.log
      

## Proxies don't connect to Cloud Service Mesh

If your proxies don't connect to Cloud Service Mesh, do the following:

  * Check the Envoy proxy logs for any errors connecting to `trafficdirector.googleapis.com`.

  * If you set up `netfilter` (by using `iptables`) to redirect all traffic to the Envoy proxy, make sure that the user (UID) as whom you run the proxy is excluded from redirection. Otherwise, this causes traffic to continuously loop back to the proxy.

  * Make sure that you enabled the Cloud Service Mesh [API](https://console.cloud.google.com/project/_/apis/library) for the project. Under **APIs & services** for your project, look for errors for the Cloud Service Mesh API.

  * Confirm that the API access scope of the VM is set to allow full access to the Google Cloud APIs by specifying the following when you create the VM:
        
        --scopes=https://www.googleapis.com/auth/cloud-platform
        

  * Confirm that the service account has the correct permissions. For more information, see [Enable the service account to access the Traffic Director API](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/prepare-service-routing-envoy-proxyless#enable-service-account).

  * Confirm that you can access `trafficdirector.googleapis.com:443` from the VM. If there are issues with this access, possible reasons could be a firewall preventing access to `trafficdirector.googleapis.com` over TCP port `443` or DNS resolution issues for the `trafficdirector.googleapis.com` hostname.

  * If you're using Envoy for the sidecar proxy, confirm that the Envoy version is release 1.24.9 or later.




## Service configured with Cloud Service Mesh is not reachable

If a service configured with Cloud Service Mesh is not reachable, confirm that the sidecar proxy is running and able to connect to Cloud Service Mesh.

If you are using Envoy as a sidecar proxy, you can confirm this by running the following commands:

  1. From the command line, confirm that the Envoy process is running:
         
         ps aux | grep envoy
         

  2. Inspect Envoy's runtime configuration to confirm that Cloud Service Mesh configured dynamic resources. To see the config, run this command:
         
         curl http://localhost:15000/config_dump
         

  3. Ensure that traffic interception for the sidecar proxy is set up correctly. For the redirect setup with `iptables`, run the `iptables` command and then `grep` the output to ensure that your rules are there:
         
         sudo iptables -t nat -S | grep ISTIO
         

The following is an example of the output for `iptables` intercepting the virtual IP address (VIP) `10.0.0.1/32` and forwarding it to an Envoy proxy running on port `15001` as UID `1006`:
         
         -N ISTIO_IN_REDIRECT
         -N ISTIO_OUTPUT
         -N ISTIO_REDIRECT
         -A OUTPUT -p tcp -j ISTIO_OUTPUT
         -A ISTIO_IN_REDIRECT -p tcp -j REDIRECT --to-ports 15001
         -A ISTIO_OUTPUT -m owner --uid-owner 1006 -j RETURN
         -A ISTIO_OUTPUT -d 127.0.0.1/32 -j RETURN
         -A ISTIO_OUTPUT -d 10.0.0.1/32 -j ISTIO_REDIRECT
         -A ISTIO_OUTPUT -j RETURN
         




If the VM instance is created through the Google Cloud console, some IPv6-related modules are not installed and available before a restart. This causes `iptables` to fail because of missing dependencies. In this case, restart the VM and rerun the setup process, which should solve the problem. A Compute Engine VM that you created by using the Google Cloud CLI is not expected to have this problem.

## Service stops being reachable when Envoy access logging is configured

If you used `TRAFFICDIRECTOR_ACCESS_LOG_PATH` to configure an Envoy access log as described in [Configure Envoy bootstrap attributes for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/per-proxy-config), make sure that the system user running Envoy proxy has permissions to write to the specified access log location.

Failure to provide necessary permissions results in listeners not being programmed on the proxy and can be detected by checking for the following error message in the Envoy proxy log:
    
    
    gRPC config for type.googleapis.com/envoy.api.v2.Listener rejected:
    Error adding/updating listener(s) TRAFFICDIRECTOR_INTERCEPTION_PORT:
    unable to open file '/var/log/envoy.log': Permission denied
    

To solve the problem, change the permissions of the chosen file for the access log to be writable by the Envoy user.

## Error messages in the Envoy logs indicate a configuration problem

This section applies to deployments using the load balancing APIs.

If you are having difficulty with your Cloud Service Mesh configuration, you might see any of the following error messages in the Envoy logs:

  * warning envoy config    StreamAggregatedResources gRPC config stream closed:
        5, Cloud Service Mesh configuration was not found for network "VPC_NAME" in
        project "PROJECT_NUMBER".

  * warning envoy upstream  StreamLoadStats gRPC config stream closed:
        5, Cloud Service Mesh configuration was not found for network "VPC_NAME" in
        project "PROJECT_NUMBER".

  * warning envoy config    StreamAggregatedResources gRPC config stream closed:
        5, Requested entity was not found.

  * warning envoy upstream  StreamLoadStats gRPC config stream closed:
        5, Requested entity was not found.

  * Cloud Service Mesh configuration was not found.




The last error message (`Traffic Director configuration was not found`) generally indicates that Envoy is requesting configuration from Cloud Service Mesh, but no matching configuration can be found. When Envoy connects to Cloud Service Mesh, it presents a VPC network name (for example, `my-network`). Cloud Service Mesh then looks for forwarding rules that have the `INTERNAL_SELF_MANAGED` load-balancing scheme and reference the same VPC network name.

To fix this error, do the following:

  1. Make sure that there is a forwarding rule in your network that has the load-balancing scheme `INTERNAL_SELF_MANAGED`. Note the forwarding rule's VPC network name.

  2. If you're using Cloud Service Mesh with [automatic Envoy deployments on Compute Engine](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/set-up-gce-vms-auto), ensure that the value provided to the `--service-proxy:network` flag matches the forwarding rule's VPC network name.

  3. If you're using Cloud Service Mesh with [manual Envoy deployments on Compute Engine](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/set-up-gce-vms), check the Envoy bootstrap file for the following:

     1. Ensure that the value for the `TRAFFICDIRECTOR_NETWORK_NAME` variable matches the forwarding rule's VPC network name.
     2. Ensure that the project number is set in the `TRAFFICDIRECTOR_GCP_PROJECT_NUMBER` variable.
  4. If you're deploying on GKE, and you are using the auto-injector, ensure that the project number and VPC network name are configured correctly, according to the directions in [Cloud Service Mesh setup for GKE Pods with automatic Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto#configuring_the_sidecar_injector).




## Troubleshooting for Compute Engine

This section provides instructions for troubleshooting Envoy deployments for Compute Engine.

The Envoy and VM bootstrapping processes and further lifecycle management operations can fail for many reasons, including temporary connectivity issues, broken repositories, bugs in bootstrapping scripts and on-VM agents, and unexpected user actions.

### Communication channels for troubleshooting

Google Cloud provides communications channels that you can use to help you understand the bootstrapping process and the current state of the components that reside on your VMs.

#### Virtual serial port output logging

A VM's operating system, BIOS, and other system-level entities typically write output to the serial ports. This output is useful for troubleshooting system crashes, failed boot-ups, start-up issues, and shutdown issues.

Compute Engine bootstrapping agents log all performed actions to serial port 1. This includes system events, starting with basic package installation through getting data from an instance's metadata server, `iptables` configuration, and Envoy installation status.

On-VM agents log Envoy process health status, newly discovered Cloud Service Mesh services, and any other information that might be useful when you investigate issues with VMs.

#### Cloud Monitoring logging

Data exposed in serial port output is also logged to Monitoring, which uses the Golang library and exports the logs to a separate log to reduce noise. Because this log is an instance-level log, you might find service proxy logs on the same page as other instance logs.

### VM guest attributes

[Guest attributes](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#guest_attributes) are a specific type of custom metadata that your applications can write to while running on your instance. Any application or user on your instances can read and write data to these guest attribute metadata values.

Compute Engine Envoy bootstrap scripts and on-VM agents expose attributes with information about the bootstrapping process and current status of Envoy. All guest attributes are exposed in the `gce-service-proxy` namespace:
    
    
    gcloud compute instances get-guest-attributes INSTANCE_NAME  \
        --query-path=gce-service-proxy/ \
        --zone=ZONE
    

If you find any issues, we recommend that you check the value of the guest attributes `bootstrap-status` and `bootstrap-last-failure`. Any `bootstrap-status` value other than `FINISHED` indicates that the Envoy environment is not configured yet. The value of `bookstrap-last-failure` might indicate what the problem is.

### Unable to reach Cloud Service Mesh service from a VM created using a service-proxy-enabled instance template

To correct this problem, follow these steps:

  1. _The installation of service proxy components on the VM might not have completed or might have failed._ Use the following command to determine whether all components are properly installed:
         
         gcloud compute instances get-guest-attributes INSTANCE_NAME \
             --query-path=gce-service-proxy/ \
             --zone=ZONE
         

The `bootstrap-status` guest attribute is set to one of the following:

     * `[none]` indicates that installation has not started yet. The VM might still be booting up. Check the status again in a few minutes.
     * `IN PROGRESS` indicates that the installation and configuration of the service proxy components are not yet complete. Repeat the status check for updates on the process.
     * `FAILED` indicates that the installation or configuration of a component failed. Check the error message by querying the `gce-service-proxy/bootstrap-last-failure1` attribute.
     * `FINISHED` indicates that the installation and configuration processes finished without any errors. Use the following instructions to verify that traffic interception and the Envoy proxy are configured correctly.
  2. _Traffic interception on the VM is not configured correctly for Cloud Service Mesh-based services._ Sign in to the VM and check the `iptables` configuration:
         
         gcloud compute ssh INSTANCE_NAME \
             --zone=ZONE \
             sudo iptables -L -t nat
         

Examine the chain `SERVICE_PROXY_SERVICE_CIDRS` for `SERVICE_PROXY_REDIRECT` entries such as these:
         
         Chain SERVICE_PROXY_SERVICE_CIDRS (1 references)
         target                   prot opt source         destination ...
         SERVICE_PROXY_REDIRECT   all  --  anywhere       10.7.240.0/20
         

For each service, there should be a matching IP address or CIDR in the `destination` column. If there is no entry for the virtual IP address (VIP), then there is a problem with populating the Envoy proxy configuration from Cloud Service Mesh, or the on-VM agent failed.

  3. _The Envoy proxies haven't received their configuration from Cloud Service Mesh yet._ Sign in to the VM to check the Envoy proxy configuration:
         
         gcloud compute ssh INSTANCE_NAME \
             --zone=ZONE \
             sudo curl localhost:15000/config_dump
         

Examine the listener configuration received from Cloud Service Mesh. For example:
         
         "dynamic_active_listeners": [
           ...
           "filter_chains": [{
             "filter_chain_match": {
               "prefix_ranges": [{
                 "address_prefix": "10.7.240.20",
                 "prefix_len": 32
               }],
               "destination_port": 80
             },
           ...
             "route_config_name": "URL_MAP/PROJECT_NUMBER.td-routing-rule-1"
           ...
         ]
         

The `address_prefix` is the virtual IP address (VIP) of a Cloud Service Mesh service. It points to the URL map called `td-routing-rule-1`. Check whether the service that you want to connect to is already included in the listener configuration.

  4. _The on-VM agent is not running._ The on-VM agent automatically configures traffic interception when new Cloud Service Mesh services are created. If the agent is not running, all traffic to new services goes directly to VIPs, bypassing the Envoy proxy, and times out.

     1. Verify the status of the on-VM agent by running the following command:
            
            gcloud compute instances get-guest-attributes INSTANCE_NAME \
               --query-path=gce-service-proxy/ \
               --zone=ZONE
            

     2. Examine the attributes of the on-VM agent. The value of the `agent-heartbeat` attribute has the time that the agent last performed an action or check. If the value is more than five minutes old, the agent is stuck, and you should re-create the VM by using the following command:
            
            gcloud compute instance-groups managed recreate-instance
            

     3. The `agent-last-failure` attribute exposes the last error that occurred in the agent. This might be a transient issue that resolves by the next time the agent checks—for example, if the error is `Cannot reach the Cloud Service Mesh API server`—or it might be a permanent error. Wait a few minutes and then recheck the error.




### Inbound traffic interception is configured to the workload port, but you cannot connect to the port from outside the VM

To correct this problem, follow these steps:

  1. _The installation of service proxy components on the VM might not have completed or might have failed._ Use the following command to determine whether all components are properly installed:
         
         gcloud compute instances get-guest-attributes INSTANCE_NAME \
             --query-path=gce-service-proxy/ \
             --zone=ZONE
         

The `bootstrap-status` guest attribute is set to one of the following:

     * `[none]` indicates that installation has not started yet. The VM might still be booting up. Check the status again in a few minutes.
     * `IN PROGRESS` indicates that the installation and configuration of the service proxy components are not yet complete. Repeat the status check for updates on the process.
     * `FAILED` indicates that the installation or configuration of a component failed. Check the error message by querying the `gce-service-proxy/bootstrap-last-failure1` attribute.
     * `FINISHED` indicates that the installation and configuration processes finished without any errors. Use the following instructions to verify that traffic interception and the Envoy proxy are configured correctly.
  2. _Traffic interception on the VM is not configured correctly for inbound traffic._ Sign in to the VM and check the `iptables` configuration:
         
         gcloud compute ssh INSTANCE_NAME \
             --zone=ZONE \
             sudo iptables -L -t nat
         

Examine the chain `SERVICE_PROXY_INBOUND` for `SERVICE_PROXY_IN_REDIRECT` entries such as these:
         
         Chain SERVICE_PROXY_INBOUND (1 references)
         target                      prot opt source       destination ...
         SERVICE_PROXY_IN_REDIRECT   tcp  --  anywhere     anywhere  tcp dpt:mysql
         

For each port that is defined in `service-proxy:serving-ports`, there should be a matching port in the `destination` column. If there is no entry for the port, all inbound traffic goes to this port directly, bypassing the Envoy proxy.

Verify that there are no other rules that drop traffic to this port or all ports except one specific port.

  3. _The Envoy proxies haven't received their configuration for the inbound port from Cloud Service Mesh yet._ Sign in to the VM to check the Envoy proxy configuration:
         
         gcloud compute ssh INSTANCE_NAME \
             --zone=ZONE \
             sudo curl localhost:15000/config_dump
         

Look for the _inbound_ listener configuration received from Cloud Service Mesh:
         
         "dynamic_active_listeners": [
           ...
           "filter_chains": [{
             "filter_chain_match": {
               "prefix_ranges": [{
                 "address_prefix": "10.0.0.1",
                 "prefix_len": 32
               }],
               "destination_port": 80
             },
           ...
             "route_config_name": "inbound|default_inbound_config-80"
           ...
         ]
         

The `route_config_name`, starting with `inbound`, indicates a special service created for inbound traffic interception purposes. Check whether the port that you want to connect to is already included in the listener configuration under `destination_port`.




## Issues when connections use server-first protocols

Some applications, such as MySQL, use protocols where the server sends the first packet. This means that upon initial connection the server sends the first bytes. These protocols and applications are not supported by Cloud Service Mesh.

## Troubleshoot the health of your service mesh

This guide provides information to help you resolve Cloud Service Mesh configuration issues.

### Cloud Service Mesh behavior when most endpoints are unhealthy

For better reliability, when 99% of endpoints are unhealthy, Cloud Service Mesh configures the data plane to disregard the health status of the endpoints. Instead, the data plane balances traffic among all of the endpoints because it is possible that the serving port is still functional.

### Unhealthy backends cause suboptimal distribution of traffic

Cloud Service Mesh uses the information in the `HealthCheck` resource attached to a backend service to evaluate the health of your backends. Cloud Service Mesh uses this health status to route traffic to the closest healthy backend. If some of your backends are unhealthy, traffic might continue to be processed, but with suboptimal distribution. For example, traffic might flow to a region where healthy backends are still present, but which is much farther from the client, introducing latency. To identify and monitor the health status of your backends, try the following steps:

  * Check the health status of your backend service in the Google Cloud console.   
[Go to Cloud Service Mesh services](https://console.cloud.google.com/net-services/trafficdirector/services/list)
  * Make sure that [logging is enabled](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) for the `HealthCheck` resource.
  * If the health checks started failing recently, inspect [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) to determine whether your `HealthCheck` configuration has changed recently.



## What's next

  * To resolve configuration issues when you deploy proxyless gRPC services, see [Troubleshooting deployments that use proxyless gRPC](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/troubleshooting-proxyless).
  * To find additional support for using Cloud Service Mesh, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.23/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
