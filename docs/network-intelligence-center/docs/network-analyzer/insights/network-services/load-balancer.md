---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/load-balancer/
title: Load balancer insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:32.805965+00:00
---

# Load balancer insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/network-services/load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Load balancer insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for load balancers. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

## View insights in the Recommender API

To view these insights in the gcloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.networkservices.loadBalancerInsight`



You need the following permissions:

  * `recommender.networkAnalyzerLoadBalancerInsights.list`
  * `recommender.networkAnalyzerLoadBalancerInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## Health check firewall is not configured

This insight indicates that the health check firewall is not configured on the VPC network the load balancer is using. The insight includes the following information:

  * **Load balancer:** Name of the load balancer.
  * **Forwarding rule:** Name of the specific forwarding rule.
  * **Network:** Name of the network where the load balancer is configured.
  * **Blocking firewalls:** Name of the firewalls that are blocking health check IP address ranges.
  * **Misconfigured backends:** The backends of the load balancer that do not include the allowing firewall rule for health check IP address ranges.



### Recommendations

Configure the health check firewall rule to explicitly allow the health check IP address range access to the load balancer backends. For more information, see [Firewall rules for load balancers](https://docs.cloud.google.com/load-balancing/docs/firewall-rules).

## Health check IP address range is blocked

This insight indicates that a user-configured firewall rule is blocking the health check IP address range. From the insight details, you can find the firewall rule that blocks the health check address range.

### Recommendations

To identify the health check address range of your load balancer type, see [Firewall rules for load balancers](https://docs.cloud.google.com/load-balancing/docs/firewall-rules).

  * If the blocking firewall rule has a wider IP address range, create an allow rule of higher priority for the health check IP address range.
  * If the blocking firewall rule has the same or smaller IP address range than the health check IP address range, remove the blocking firewall rule.



## Firewall configuration is inconsistent

This insight indicates that the firewall configuration is inconsistent among backend VMs. The health check IP address range is allowed on some backend VMs, while it is denied on others. This issue occurs when network tags or service accounts are modified by mistake on some backend VMs. The insight includes the following information:

  * **Load balancer:** Name of the load balancer
  * **Forwarding rule:** Name of the specific forwarding rule
  * **Network:** Name of the network where the load balancer is configured
  * **Blocking firewalls:** Name of the firewalls that are blocking health check ranges
  * **Partially allowing firewalls:** Name of the firewalls that allow health check traffic on the properly configured backend VMs
  * **Misconfigured backends:** Backends that have this issue, where the firewall configuration for the health check IP address range is not working properly



### Related topics

  * [Filtering by service account versus network tag](https://docs.cloud.google.com/vpc/docs/firewalls#service-accounts-vs-tags)
  * [Firewall rules for load balancers](https://docs.cloud.google.com/load-balancing/docs/firewall-rules)



### Recommendations

Find the misconfigured tags by comparing the tags configured on misconfigured backend VMs with the tags configured on the partially allowing firewall rules. Modify the tags and service accounts on the misconfigured backend VMs to have the same values as the tags and service accounts on the working backend VMs.

## Health check IP address range is partially blocked

This insight indicates that all backends have partially blocked traffic on the health check range. Health check traffic is allowed for some health check IP address ranges and denied for other health check IP address ranges. The insight includes the following information:

  * **Load balancer:** Name of the load balancer
  * **Forwarding rule:** Name of the specific forwarding rule
  * **Network:** Name of the network where the load balancer is configured
  * **Blocking firewalls:** Name of the firewalls that are blocking health check ranges
  * **Partially allowing firewalls:** Name of the firewalls that allow health check traffic on the properly configured backend VMs
  * **Misconfigured backends:** Backends that have this issue, where the firewall configuration for health check range is not working properly
  * **Blocked health check ranges:** IP address ranges where the health check traffic is blocked



### Related topics

  * [Firewall rules for load balancers](https://docs.cloud.google.com/load-balancing/docs/firewall-rules)



### Recommendations

Compare the IP address ranges on your partially allowing firewall rules with the health check IP address range for your load balancer type. If any IP address ranges are missing, add them to your allowing firewall rule. If the insight persists, ensure that the priority of the partially allowing firewall rules is higher than the priority of the denying firewall rule.

## Backend service balancing mode breaks session affinity

This insight is triggered when a proxy based load balancer's backend service has a session affinity other than `NONE` and has one or more instance group backends using the `UTILIZATION` balancing mode. The session affinity can break when the traffic to the load balancer is low. The load balancer also drops a portion of sessions when the amount of backends change when backends are added or removed from the load balancer, such as in cases of a health check failure or a consequent success. The amount of sessions being dropped is proportionate to the amount of backends changing. Such changes also break session affinity for those sessions.

This insight includes the following information:

  * **Backend service:** The affected backend service.
  * **Forwarding rules:** The forwarding rules that direct traffic to this backend service.
  * **Session affinity:** The session affinity used by the backend service.
  * **Impacted backends:** The backends using the `UTILIZATION` balancing mode.



### Related topics

  * [Losing session affinity with utilization balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#losing_session_affinity)
  * [Supported balancing modes by load balancer type](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution)



### Recommendations

To use a session affinity other than `NONE`, you must use either the `RATE` or `CONNECTION` balancing modes. You can do this operation only with Google Cloud CLI or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1), not on the Google Cloud console.

For proxy load balancer backend services that use the HTTP, HTTPS, or HTTP/2 protocols, switch the balancing mode to `RATE` by using the `gcloud compute backend-services update-backend` command and choosing the [rate balancing mode](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update-backend#RATE).

The following code sample shows how to use this command to switch the mode to `RATE`:
    
    
    gcloud compute backend-services update-backend BACKEND_SERVICE_NAME \
        BACKEND_SERVICE_SCOPE \
        --instance-group=INSTANCE_GROUP_NAME \
        INSTANCE_GROUP_SCOPE \
        --balancing-mode=RATE \
        TARGET_CAPACITY
    

For proxy load balancer backend services that use non-HTTP protocols (like TCP or SSL), switch the balancing mode to `CONNECTION` by using the `gcloud compute backend-services update-backend` command and choosing the [connection balancing mode](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update-backend#CONNECTION).

The following code sample shows how to use this command to switch the mode to `CONNECTION`:
    
    
    gcloud compute backend-services update-backend BACKEND_SERVICE_NAME \
        BACKEND_SERVICE_SCOPE \
        --instance-group=INSTANCE_GROUP_NAME \
        INSTANCE_GROUP_SCOPE \
        --balancing-mode=CONNECTION \
        TARGET_CAPACITY
    

In both the examples, replace the following:

  * BACKEND_SERVICE_NAME: the backend service's name.
  * BACKEND_SERVICE_SCOPE: the backend service's scope. For global backend services, use `--global`. For regional backend services, use `--region=`REGION, replacing REGION with the region.
  * INSTANCE_GROUP_NAME: the name of the backend instance group.
  * INSTANCE_GROUP_SCOPE: the location of the instance group. For regional managed instance groups, use `--region=`REGION, replacing REGION with the region. For zonal instance groups, use `--zone=`ZONE, replacing ZONE with the zone.
  * TARGET_CAPACITY: a target rate or target connection specification. For rate balancing mode, use either the `--max-rate=` or `--max-rate-per-instance=` flags, referring to [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode) in the Backend services overview. For drop connection balancing mode, use either the `--max-connections=` or `--max-connections-per-instance=` flags, referring to [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode) in the Backend services overview.



## Backend service uses different ports for health check and traffic

The load balancer is performing health checks on some backends on a different port and not on the named port used by the load balancer for serving traffic. This configuration can be problematic unless you have configured the load balancer to use a different port purposefully.

This insight includes the following information:

  * **Backend service:** The affected backend service.
  * **Forwarding rules:** The forwarding rules which direct traffic to the backend service.
  * **Serving port name:** The port name the backend service uses for service traffic.
  * **Health check:** The health check used by the backend service.
  * **Health check port number:** The port used by the health check.
  * **Impacted backends:** The instance groups on which the serving port is different from the health check port.



### Related topics

See [Category and port specification](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_port_specification).

### Recommendations

Configure the health check with the _use serving port specification_ so that the health check uses the same port that the backend service uses. The following code sample shows how to use Google Cloud CLI commands to update your health check to use the serving port:
    
    
    gcloud compute health-checks update PROTOCOL HEALTH_CHECK_NAME \
          HEALTH_CHECK_SCOPE \
          --use-serving-port
    

Replace the following:

  * PROTOCOL: the protocol used by the health check.
  * HEALTH_CHECK_NAME: the health check's name.
  * HEALTH_CHECK_SCOPE: the scope of the health check. For global health checks, use `--global`. For regional health checks, use `--region=`REGION, replacing REGION with the region.



## SSL certificates are not associated with load balancers

This indicates that your project has Google-managed SSL certificates that are not associated with a load balancer that handles either SSL or HTTPS traffic. Google-managed SSL certificates cannot be used until the certificates are attached to a load balancer. You can view the list of unattached certificates in the insight details.

### Related topics

  * [Use Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#load-balancer)
  * [Troubleshoot Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#troubleshoot_google-managed_certificates)



### Recommendations

You can create a Google-managed SSL certificate before, during, or after creating your load balancer. To become `ACTIVE`, the Google-managed SSL certificate must be associated with a load balancer, specifically the load balancer's target proxy.

After you've created your SSL certificate and it's in the `PROVISIONING` state, you can use it during the creation of your load balancer, or you can use it to update an existing load balancer. For more information about your Google-managed certificate, see [Troubleshoot Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#troubleshoot_google-managed_certificates).

## SSL certificates associated with a load balancer that doesn't expose port 443

This indicates that your project has Google-managed SSL certificates that are not working properly because the forwarding rules associated with them don't expose port `443`. You can view a list of these certificates in the [insight details](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

### Related topics

  * [Create a forwarding rule](https://docs.cloud.google.com/load-balancing/docs/using-forwarding-rules#adding-fr)
  * [Troubleshoot Google-managed certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#troubleshoot_google-managed_certificates)



### Recommendations

Create a forwarding rule by using port `443` when you're creating or updating a load balancer.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
