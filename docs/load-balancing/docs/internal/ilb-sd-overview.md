---
url: https://docs.cloud.google.com/load-balancing/docs/internal/ilb-sd-overview/
title: Internal passthrough Network Load Balancer and Service Directory overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:53.616886+00:00
---

# Internal passthrough Network Load Balancer and Service Directory overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/internal/ilb-sd-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Internal passthrough Network Load Balancer and Service Directory overview Stay organized with collections  Save and categorize content based on your preferences. 

You can choose to automatically register your internal load balancer service with Service Directory when you create an internal load balancer. This enables client applications to use Service Directory through HTTP, gRPC, or DNS to resolve the address of the internal load balancer service and connect to it directly.

Registering your internal load balancer with Service Directory lets you do the following:

  * Choose custom DNS names to serve the network locations of your internal load balancers as opposed to DNS accessing your internal load balancer only through an internally generated DNS name in the `.internal` domain.
  * Serve multiple internal load balancers from the same DNS domain name, which is otherwise not possible with the current auto-generated DNS records.
  * Register internal load balancers directly and automatically in Service Directory providing a single repository for all your services in Google Cloud.
  * See standalone services, endpoints, and your internal load balancer endpoints with a single command in the Service Directory API.
  * Apply administrative actions like access control to Service Directory resources at the namespace or service level to encompass both your internal load balancer endpoints as well as other backend services.

**Note:** Cross-region internal Application Load Balancers don't support Service Directory registrations. 

## Register an internal passthrough Network Load Balancer with Service Directory

To register an internal passthrough Network Load Balancer, run the [`gcloud compute forwarding-rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) command and set the `service-directory-registration` flag:
    
    
    gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
        --region=REGION \
        --load-balancing-scheme=INTERNAL \
        --network=NETWORK_NAME \
        --subnet=SUBNET_NAME \
        --address=RESERVED_IP_ADDRESS \
        --ip-protocol=PROTOCOL_TYPE \
        --ports=PORT_NUMBER \
        --backend-service=BACKEND_SERVICE_NAME \
        --backend-service-region=REGION \
        --service-directory-registration=SD_SERVICE_NAME
    

Replace the following:

  * `FORWARDING_RULE_NAME`: a name for the forwarding rule that you want to create
  * `REGION`: the region to create the forwarding rule in
  * `NETWORK_NAME`: the network that this forwarding rule applies to
  * `SUBNET_NAME`: the subnetwork that this forwarding rule applies to
  * `RESERVED_IP_ADDRESS`: the IP address that the forwarding rule serves
  * `PROTOCOL_TYPE`: the IP protocol that the rule will serve
  * `PORT_NUMBER`: a list of comma-separated ports
  * `BACKEND_SERVICE_NAME`: target backend service that receives the traffic
  * `SD_SERVICE_NAME`: the fully qualified name of the Service Directory service where you want to register the endpoint. It must live in the same project and region as the forwarding rule being created. For example: projects/`PROJECT`/locations/`REGION`/namespaces/`NAMESPACE_NAME`/services/`SERVICE_NAME`.



## What's next

  * To learn more about Service Directory, see [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To learn about limitations of Service Directory integration with internal passthrough Network Load Balancer and how to verify the endpoint, see [Register an internal load balancer](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd).
  * To troubleshoot next hop issues with your internal passthrough Network Load Balancer, see [Troubleshoot load balancer as next hop issues](https://docs.cloud.google.com/load-balancing/docs/internal/troubleshooting-ilb#lb-as-next-hop).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
