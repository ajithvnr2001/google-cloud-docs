---
url: https://docs.cloud.google.com/service-directory/docs/configuring-netlb-in-sd/
title: Register a regional external passthrough Network Load Balancer \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:52.570624+00:00
---

# Register a regional external passthrough Network Load Balancer  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/configuring-netlb-in-sd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Register a regional external passthrough Network Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how to configure a [regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network) so that it is automatically registered in Service Directory.

When you create your load balancer, you can register it as an endpoint in an existing Service Directory namespace and service of your choice. Client applications can then use Service Directory (using HTTP or gRPC) to resolve the address of the regional external passthrough Network Load Balancer service and connect to it directly.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _and_ IAM roles.

**Permissions**

  * `servicedirectory.endpoints.create`
  * `servicedirectory.endpoints.delete`



**Roles**

  * `roles/compute.networkAdmin`
  * `roles/compute.securityAdmin`
  * `roles/compute.instanceAdmin`



## Limitations

Service Directory integration with regional external passthrough Network Load Balancers has the following limitations:

  * Automatic registration only supports external Layer 4 load balancers. You can register Google Kubernetes Engine load balancing services using the [GKE integration](https://docs.cloud.google.com/service-directory/docs/configuring-sd-for-gke). You can register other external load balancers, global load balancers, and Google Kubernetes Engine ingresses and gateways by calling the [Service Directory API](https://docs.cloud.google.com/service-directory/docs/apis).
  * You can use automatic registration only at the time of forwarding rule creation. Automatic registration using Google Cloud CLI update for an already existing forwarding rule is not available.
  * Service Directory does not provide connectivity, which means that although Service Directory stores the virtual IP address of the regional external passthrough Network Load Balancer, looking up the regional external passthrough Network Load Balancer in Service Directory does not guarantee that you can connect to the virtual IP address.



## Before you begin

These instructions require the following:

  * You must already have a Service Directory namespace and service in place. If you do not, create a namespace and service using the procedure in [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory).

The Service Directory namespace and service must be in the same project and region as the regional external passthrough Network Load Balancer forwarding rule that you are creating.

  * You must already have set up the necessary resources to create a regional external passthrough Network Load Balancer forwarding rule.

For information about how to create a regional external passthrough Network Load Balancer, see [Setting up a regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service).




## Set up forwarding rules to register a regional external passthrough Network Load Balancer in Service Directory

You must set up a forwarding rule to register the regional external passthrough Network Load Balancer in Service Directory. To register a regional external passthrough Network Load Balancer, see the following section.

### Register a regional external passthrough Network Load Balancer

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



### Verify the endpoint

The Service Directory endpoints that are created when you register a regional external passthrough Network Load Balancer have the following characteristics:

  * The endpoint has the same name as the name of the forwarding rule with the specified port number (`<forwarding rule name>-<port>`). For example, if you create a forwarding rule `RULE` with `--port=8080`, you get an endpoint called `RULE-8080`. For the same rule, if you specified two ports `--port=8080, 8081`, you get two endpoints, `RULE-8080` and `RULE-8081`. If you specify `--port=ALL`, the Service Directory endpoint is registered with port `0`. If you are the owner of the regional external passthrough Network Load Balancer, you must ensure that the API caller knows what port to connect on.
  * You cannot modify or delete the endpoint using the public Service Directory API. Only when you delete the forwarding rule does the endpoint get automatically deleted. This means that you cannot delete the service and namespace that the endpoint resides in while the forwarding rule exists.
  * The endpoint itself is not billed, although normal pricing details apply to any API calls to the endpoint.



To confirm that the endpoint is created, resolve the service in Service Directory. You should see an endpoint with the same name as the name of the forwarding rule with the specified port number.

To resolve the service in Service Directory, run the [`gcloud service-directory services resolve`](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory/services/resolve) command:
    
    
    gcloud service-directory services resolve SD_SERVICE_NAME \
        --namespace=SD_NAMESPACE_NAME \
        --location=REGION
    

Replace the following:

  * `SD_SERVICE_NAME`: the name of the Service Directory service to resolve. It must live in the Service Directory namespace name.
  * `SD_NAMESPACE_NAME`: the name that you gave the namespace containing your service.
  * `REGION`: the Google Cloud region containing the namespace. This should be the same as the region that you created the forwarding rule in.



## Cleanup

To delete the resources that you created, follow these steps.

  1. To delete the forwarding rule, run the [`gcloud compute forwarding-rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/delete) command:
         
         gcloud compute forwarding-rules delete FORWARDING_RULE_NAME \
           --region=REGION
         

Replace the following:

     * `FORWARDING_RULE_NAME`: the name of the forwarding rule that you created
     * `REGION`: the region for the forwarding rule

For further details, see [Deleting a forwarding rule](https://docs.cloud.google.com/load-balancing/docs/using-forwarding-rules#deleting-fr).

To confirm that deleting the forwarding rule has automatically deleted the endpoint from Service Directory, run the [`gcloud service-directory services resolve`](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory/services/resolve) command described in Verify the endpoint section on your Service Directory service.

  2. To delete the Service Directory namespace and service, see [Delete resources](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#delete_resources).




## What's next

  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
