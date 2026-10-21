---
url: https://docs.cloud.google.com/load-balancing/docs/network/networklb-sd-overview/
title: Regional external passthrough Network Load Balancer and Service Directory overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:32.378634+00:00
---

# Regional external passthrough Network Load Balancer and Service Directory overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/network/networklb-sd-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Regional external passthrough Network Load Balancer and Service Directory overview Stay organized with collections  Save and categorize content based on your preferences. 

You can choose to automatically register your regional external passthrough Network Load Balancer service with Service Directory when you create a regional external passthrough Network Load Balancer. This enables client applications to use Service Directory through HTTP, gRPC, or DNS to resolve the address of the regional external passthrough Network Load Balancer service and connect to it directly.

## Register a regional external passthrough Network Load Balancer with Service Directory

To register a regional external passthrough Network Load Balancer, run the [`gcloud compute forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) and set the `service-directory-registration` flag:
    
    
    gcloud beta compute forwarding-rules create FORWARDING_RULE_NAME \
        --region=REGION \
        --load-balancing-scheme=EXTERNAL \
        --address=RESERVED_IP_ADDRESS \
        --ip-protocol=PROTOCOL_TYPE \
        --ports=PORT_NUMBER \
        --backend-service=BACKEND_SERVICE_NAME \
        --backend-service-region=REGION \
        --service-directory-registration=SD_SERVICE_NAME
    

Replace the following:

  * `FORWARDING_RULE_NAME`: a name for the forwarding rule that you want to create
  * `REGION`: the region to create the forwarding rule in
  * `RESERVED_IP_ADDRESS`: the IP address that the forwarding rule serves
  * `PROTOCOL_TYPE`: the IP protocol that the rule is to serve
  * `PORT_NUMBER`: a list of comma-separated ports
  * `BACKEND_SERVICE_NAME`: the target backend service that receives the traffic
  * `SD_SERVICE_NAME`: the fully qualified name of the Service Directory service where you want to register the endpoint. This service must be in the same project and region as the forwarding rule being created. For example: projects/`PROJECT`/locations/`REGION`/namespaces/`NAMESPACE_NAME`/services/`SERVICE_NAME`.



## What's next

  * To learn more about Service Directory, see [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To learn about limitations of Service Directory integration with regional external passthrough Network Load Balancer and how to verify the endpoint, see [Register a regional external passthrough Network Load Balancer](https://docs.cloud.google.com/service-directory/docs/configuring-netlb-in-sd). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
