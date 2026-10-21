---
url: https://docs.cloud.google.com/load-balancing/docs/dns-names/
title: Internal load balancing and DNS names \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:46:21.201362+00:00
---

# Internal load balancing and DNS names  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/dns-names/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal load balancing and DNS names Stay organized with collections  Save and categorize content based on your preferences. 

A DNS address record, known as an _A record_ , is used to map a DNS name to an IP address. When you create the forwarding rule for an internal load balancer, you can optionally designate a _service label_ so that Google Cloud creates a unique [Compute Engine internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns) for the load balancer. This internal DNS name is constructed from your project ID, forwarding rule name, and a service label you specify.

**Note:** This page describes how to configure a specific load balancer component or feature before or after you've already created a load balancer. Working with specific components is useful for advanced configurations and necessary for some configuration options. Before using the information on this page, know the [type of Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) that you need.

## Specifications

  * This feature is supported by forwarding rules for these load balancers:

    * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
    * [Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
    * [Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
  * See DNS record format for details about the format of the DNS name that Google Cloud creates for your load balancer. Because the DNS name contains the forwarding rule's name, each DNS name is unique, even if you use the same service label for multiple forwarding rules.

  * [Unless an alternative name server is configured](https://docs.cloud.google.com/dns/docs/overview#vpc-name-resolution-order), client VMs in any region in the same project and VPC network can perform DNS lookups for the load balancer's internal DNS name. To access the load balancer, client VMs must be located [in the same region](https://docs.cloud.google.com/load-balancing/docs/internal#protocols_scheme_and_scope). If you enable global access, a client in any region can access the load balancer.

  * You can only specify a service label when you _create_ a forwarding rule. You cannot add a service label to an existing forwarding rule. However, you can replace an existing forwarding rule with a new forwarding rule that has a service label. The replacement can use the same internal IP address as the original if you delete the original forwarding rule first.

  * The internal DNS names created from service labels have the following restrictions:

    * No corresponding reverse (PTR) records are created.
    * Each forwarding rule can have only one service label.
    * Other than the service label and forwarding rule's name, you cannot change any other part of the internal DNS name. This includes its format and its domain name (`.internal`).

If you need more flexible DNS names for your internal load balancer, you can create custom records in a [Cloud DNS managed private zone](https://docs.cloud.google.com/dns/docs/overview).




### DNS record format

When you add a service label to a forwarding rule, Google Cloud creates a Compute Engine internal DNS A record using one of these formats:

  * For internal passthrough Network Load Balancers:

SERVICE_LABEL.FORWARDING_RULE_NAME.il4.REGION.lb.PROJECT_ID.internal

  * For regional internal Application Load Balancers and regional internal proxy Network Load Balancers:

SERVICE_LABEL.FORWARDING_RULE_NAME.il7.REGION.lb.PROJECT_ID.internal




SERVICE_LABEL is the forwarding rule's service label that you specify. It must follow this format:

  * You can use up to 63 lower case letters (`a` to `z`), numbers (`0` to `9`), or dashes (`-`).
  * The service label must start with a lowercase letter.
  * The service label must end with a lowercase letter or number.



FORWARDING_RULE_NAME is the name of the forwarding rule you're creating.

REGION is the load balancer's region.

PROJECT_ID is your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). Project IDs that have the form `organization:project-id` are converted to `project-id.organization`. For example, if your project ID is `example.com:example-marketing-prod`, Google Cloud uses `example-marketing-prod.example.com`.

## Creating a forwarding rule with a service label

This procedure shows how to create a forwarding rule with a service label.

This procedure _only_ focuses on how to create a forwarding rule with a service label. Properties of the load balancer's backend configuration and other properties of its frontend configuration are omitted. If you're new to internal passthrough Network Load Balancers, regional internal Application Load Balancers, or regional internal proxy Network Load Balancers, see these pages for complete examples:

  * [Set up an internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)
  * [Set up a regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
  * [Set up a regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)




###  Console 

**Note:** For regional internal proxy Network Load Balancers, creating a forwarding rule with a service label is not supported in the Google Cloud console. Use gcloud or the API instead.

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click **Create load balancer**.
  3. Complete the steps of the wizard to create either an internal passthrough Network Load Balancer or a regional internal Application Load Balancer, and click **Configure**.
  4. Specify a name for the load balancer.
  5. Click **Continue**.
  6. Complete the **Backend configuration**.
  7. Click **Frontend configuration**. Complete the frontend configuration, specifying a **Service label** at the bottom of that section.

  8. Click **Done** , and then **Review and finalize**.



###  gcloud 

To create a forwarding rule with a service label for an internal passthrough Network Load Balancer:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
        --load-balancing-scheme=INTERNAL \
        --region=REGION \
        --backend-service-region=REGION \
        --backend-service=BACKEND_SERVICE_NAME \
        --network=NETWORK \
        --subnet=SUBNET \
        --address=INTERNAL_IP \
        --ip-protocol=PROTOCOL \
        --ports=PORTS \
        --service-label=SERVICE_LABEL
    

To create a forwarding rule with a service label for a regional internal proxy Network Load Balancer:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
        --load-balancing-scheme=INTERNAL_MANAGED \
        --region=REGION \
        --target-tcp-proxy-region=REGION \
        --target-tcp-proxy=TARGET_PROXY_NAME \
        --network=NETWORK \
        --subnet=SUBNET \
        --address=INTERNAL_IP \
        --ip-protocol=TCP \
        --ports=PORT \
        --service-label=SERVICE_LABEL
    

To create a forwarding rule with a service label for a regional internal Application Load Balancer with **HTTPS** :
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
        --load-balancing-scheme=INTERNAL_MANAGED \
        --region=REGION \
        --target-https-proxy-region=REGION \
        --target-https-proxy=TARGET_PROXY_NAME \
        --network=NETWORK \
        --subnet=SUBNET \
        --address=INTERNAL_IP \
        --ip-protocol=TCP \
        --ports=PORT \
        --service-label=SERVICE_LABEL
    

To create a forwarding rule with a service label for a regional internal Application Load Balancer with **HTTP** :
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
        --load-balancing-scheme=INTERNAL_MANAGED \
        --region=REGION \
        --target-http-proxy-region=REGION \
        --target-http-proxy=TARGET_PROXY_NAME \
        --network=NETWORK \
        --subnet=SUBNET \
        --address=INTERNAL_IP \
        --ip-protocol=TCP \
        --ports=PORT \
        --service-label=SERVICE_LABEL
    

Replace the placeholders with appropriate values:

  * FORWARDING_RULE_NAME is the name of the load balancer's forwarding rule.
  * REGION is the load balancer's region.
  * BACKEND_SERVICE_NAME is the name of the load balancer's backend service.
  * TARGET_PROXY_NAME is the name of the target proxy.
  * NETWORK is the name of the VPC network where the load balancer is created.
  * SUBNET is the name of a subnet in the VPC network. The subnet must be in the same region as the load balancer's backend service or target proxy.
  * INTERNAL_IP is an internal IP address in the primary IP range of the chosen subnet. You can omit the `--address` flag to have Google Cloud choose an available IP address for you.
  * For internal passthrough Network Load Balancers, PROTOCOL is either `TCP` or `UDP`, matching the protocol of the load balancer's backend service. For regional internal Application Load Balancers and regional internal proxy Network Load Balancers, the protocol must be `TCP`.
  * For internal passthrough Network Load Balancers, PORTS is an array of up to five ports by number, or the word `ALL`. For regional internal Application Load Balancers and regional internal proxy Network Load Balancers, you can reference exactly one port from 1-65535. See [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications) in forwarding rules concepts for more details.
  * SERVICE_LABEL is your chosen service label. It must follow the naming conventions.



###  api 

**The following examples create forwarding rules using the[`forwardingRules.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/insert) method**

To create a forwarding rule with a service label for an internal passthrough Network Load Balancer:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/forwardingRules
    
    {
      "name": "FORWARDING_RULE_NAME",
      "loadBalancingScheme": "INTERNAL",
      "backendService": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/backendServices/BACKEND_SERVICE_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/NETWORK",
      "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/subnetworks/SUBNET",
      "IPAddress": "INTERNAL_IP",
      "IPProtocol": "PROTOCOL",
      "ports": PORTS,
      "serviceLabel": "SERVICE_LABEL"
    }
    

To create a forwarding rule with a service label for a regional internal proxy Network Load Balancer:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/forwardingRules
    
    {
      "name": "FORWARDING_RULE_NAME",
      "loadBalancingScheme": "INTERNAL_MANAGED",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/targetTcpProxies/TARGET_PROXY_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/NETWORK",
      "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/subnetworks/SUBNET",
      "IPAddress": "INTERNAL_IP",
      "IPProtocol": "TCP",
      "ports": PORT,
      "serviceLabel": "SERVICE_LABEL"
    }
    

To create a forwarding rule with a service label for a regional internal Application Load Balancer with **HTTPS** :
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/forwardingRules
    
    {
      "name": "FORWARDING_RULE_NAME",
      "loadBalancingScheme": "INTERNAL_MANAGED",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/targetHttpsProxies/TARGET_PROXY_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/NETWORK",
      "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/subnetworks/SUBNET",
      "IPAddress": "INTERNAL_IP",
      "IPProtocol": "TCP",
      "ports": PORT,
      "serviceLabel": "SERVICE_LABEL"
    }
    

To create a forwarding rule with a service label for a regional internal Application Load Balancer with **HTTP** :
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/forwardingRules
    
    {
      "name": "FORWARDING_RULE_NAME",
      "loadBalancingScheme": "INTERNAL_MANAGED",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/targetHttpProxies/TARGET_PROXY_NAME",
      "network": "https://www.googleapis.com/compute/v1/projects/PROJECT/global/networks/NETWORK",
      "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/subnetworks/SUBNET",
      "IPAddress": "INTERNAL_IP",
      "IPProtocol": "TCP",
      "ports": PORT,
      "serviceLabel": "SERVICE_LABEL"
    }
    

Replace the placeholders with appropriate values:

  * FORWARDING_RULE_NAME is the name of the load balancer's forwarding rule.
  * REGION is the load balancer's region.
  * BACKEND_SERVICE_NAME is the name of the internal passthrough Network Load Balancer's backend service.
  * TARGET_PROXY_NAME is the name of the target proxy.
  * NETWORK is the name of the VPC network where the load balancer is created.
  * SUBNET is the name of a subnet in the VPC network. The subnet must be in the same region as the load balancer's backend service or target proxy.
  * INTERNAL_IP is an internal IP address in the primary IP range of the chosen subnet. You can omit the `IPAddress` key to have Google Cloud choose an available IP address for you.
  * For internal passthrough Network Load Balancers, PROTOCOL is either `TCP` or `UDP`, matching the protocol of the load balancer's backend service. For regional internal Application Load Balancers and regional internal proxy Network Load Balancers, the protocol must be `TCP`.
  * For internal passthrough Network Load Balancers, PORTS is an array of up to five ports by number, or the word `ALL`. For regional internal Application Load Balancers and regional internal proxy Network Load Balancers, you can reference exactly one port from 1-65535. See [Port specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications) in forwarding rules concepts for more details.
  * SERVICE_LABEL is your chosen service label. It must follow the naming conventions.



## Viewing service labels

###  Console 

You can view the Compute Engine internal DNS name (created from the service label) for each internal forwarding rule of an internal load balancer:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of the internal load balancer to view its details page.

  3. The internal forwarding rules assigned to the load balancer are listed in the _Frontend_ section. The **DNS name** column shows you the Compute Engine internal DNS name that's assigned to each forwarding rule. The service label is the first part of that name (before the first dot). If no name is shown, the forwarding rule has no service label defined.




###  gcloud 

  1. List forwarding rules in your project used by either internal passthrough Network Load Balancers or regional internal Application Load Balancers. Locate the one you need, and note its name and region for the next step.
         
         gcloud compute forwarding-rules list \
             --filter="loadBalancingScheme=SCHEME"
         

The value of SCHEME depends on the forwarding rules you need to list:

     * For internal passthrough Network Load Balancers, use `INTERNAL`.
     * For regional internal Application Load Balancers and regional internal proxy Network Load Balancers, use `INTERNAL_MANAGED`.
  2. Describe the forwarding rule, replacing FORWARDING_RULE_NAME with its name and REGION with its region:
         
         gcloud compute forwarding-rules describe FORWARDING_RULE_NAME \
             --region=REGION \
             --format="get(serviceLabel)"
         




###  api 

**View the forwarding rule and service label with the** **[`forwardingRules.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules/get)** **method**

The response to the API request includes the service label (`serviceLabel`) and Compute Engine internal DNS name (`serviceName`).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/forwardingRules/FORWARDING_RULE_NAME
    

Internal passthrough Network Load Balancer response:
    
    
    {
      ...
      "serviceLabel": "SERVICE_LABEL",
      "serviceName": "SERVICE_LABEL.FORWARDING_RULE_NAME.il4.REGION.lb.PROJECT.internal",
      ...
    }
    

Regional internal proxy Network Load Balancer and regional internal Application Load Balancer response:
    
    
    {
      ...
      "serviceLabel": "SERVICE_LABEL",
      "serviceName": "SERVICE_LABEL.FORWARDING_RULE_NAME.il7.REGION.lb.PROJECT.internal",
      ...
    }
    

## Example

The following procedure demonstrates how to replace a forwarding rule with one that has a service label. This procedure works for all supported load balancers.

If you haven't created a forwarding rule for your internal load balancer yet, skip this example and refer to Creating a forwarding rule with a service label instead.

  1. Describe your load balancer's existing forwarding rule, noting the forwarding rule's internal IP address:
         
         gcloud compute forwarding-rules describe FORWARDING_RULE_NAME \
             --region=REGION \
             --format="get(IPAddress)"
         

  2. Delete the forwarding rule:
         
         gcloud compute forwarding-rules delete FORWARDING_RULE_NAME \
             --region=REGION
         

  3. Create a replacement forwarding rule with the same name and internal IP address with a service label. Refer to Creating a forwarding rule with a service label for directions.




## What's next

  * For information on configuring Logging and Monitoring for internal passthrough Network Load Balancers, see [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring).
  * For information about how to troubleshoot issues with your internal passthrough Network Load Balancer, see [Troubleshoot internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb).
  * For information about service discovery and DNS for Google Kubernetes Engine, see [Service discovery and DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
