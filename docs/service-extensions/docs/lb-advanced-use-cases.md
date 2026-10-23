---
url: https://docs.cloud.google.com/service-extensions/docs/lb-advanced-use-cases/
title: Advanced use cases \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:23.234488+00:00
---

# Advanced use cases  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/lb-advanced-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Advanced use cases Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure Service Extensions with Application Load Balancers for advanced use cases.

## Dynamic forwarding

Dynamic forwarding helps you bind thousands or even millions of tenants to individual virtual machine (VM) instances or sets of VMs. You can use Service Extensions to programmatically determine which VMs an individual tenant gets mapped to without having to make updates to a URL map. This helps you scale far beyond the limitations of the existing URL map.

You can configure dynamic forwarding by using traffic and route callouts with these Application Load Balancers: regional external Application Load Balancer, regional internal Application Load Balancer, and cross-region internal Application Load Balancer.

This section guides you through an example where you configure a traffic extension to randomly route traffic between two VMs. Use the sample values provided.

  1. [Configure a network](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure-a-network) named `lb-network`, a subnet named `backend-subnet`, and a proxy-only subnet in the region `us-west1`.

  2. [Configure two VMs](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) in `us-west1` to represent the dynamically routable endpoints.

Specify the IP addresses as `10.1.2.1` and `10.1.2.2`, respectively. Ensure that both VMs are associated with the tag `load-balanced-backend`.

  3. Configure a firewall rule, `fw-allow-proxies`, that allows traffic from the proxy subnet to VMs in your network.
         
         gcloud compute firewall-rules create fw-allow-proxies \
             --network=df-network \
             --action=allow \
             --direction=ingress \
             --source-ranges=source-range \
             --target-tags=load-balanced-backend \
             --rules=tcp:80,tcp:443,tcp:8080
         

  4. [Create a backend service](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-services/create), `l7-ilb-backend-service`, with dynamic forwarding and logging enabled:
         
         gcloud beta compute backend-services create l7-ilb-backend-service \
             --ip-port-dynamic-forwarding \
             --enable-logging \
             --region=us-west1
         

  5. [Create a URL map](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create), `l7-ilb-map`, for the backend service.
         
         gcloud compute url-maps create l7-ilb-map \
             --default-service=l7-ilb-backend-service \
             --region=us-west1
         

  6. [Create a target proxy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-http-proxies/create), `l7-ilb-proxy`.
         
         gcloud compute target-http-proxies create l7-ilb-proxy \
             --url-map=l7-ilb-map \
             --url-map-region=us-west1 \
             --region=us-west1
         

  7. [Create a forwarding rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create) and [reserve an IP address for the Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#reserve-ip).
         
         gcloud compute forwarding-rules create l7-ilb-forwarding-rule \
             --load-balancing-scheme=INTERNAL_MANAGED \
             --network=lb-network \
             --subnet=backend-subnet \
             --subnet-region=us-west1 \
             --ports=80 \
             --region=us-west1 \
             --target-http-proxy=l7-ilb-proxy \
             --target-http-proxy-region=us-west1
         

  8. [Set up a callout backend service](https://docs.cloud.google.com/service-extensions/docs/configure-callout-backend-service#configure-extension-service) for the traffic extension.

For the extension server, use the [dynamic forwarding](https://github.com/GoogleCloudPlatform/service-extensions/blob/main/callouts/python/extproc/example/dynamic_forwarding/service_callout_example.py) example in the [Service Extensions GitHub repository](https://github.com/GoogleCloudPlatform/service-extensions).

  9. Create a YAML file, `dynamic-ext.yaml`, with the following contents:
         
         name: traffic-ext
             forwardingRules:
             - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/forwardingRules/l7-ilb-forwarding-rule
             loadBalancingScheme: INTERNAL_MANAGED
             extensionChains:
             - name: "chain1"
               matchCondition:
                 celExpression: 'request.host == "example.com"'
               extensions:
               - name: 'ext11'
                 authority: ext11.com
                 allowDynamicForwarding: true
                 service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/backendServices/l7-ilb-callout-service
                 failOpen: false
                 timeout: 0.1s
                 supportedEvents:
                 - REQUEST_HEADERS
         

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Import the traffic extension to the forwarding rule:
         
         gcloud beta service-extensions lb-traffic-extensions import traffic-ext \
             --source=dynamic-ext.yaml \
             --location=us-west1
         




With the extension configured, traffic is routed based on the extension server implementation.

## What's next

  * [Manage extensions](https://docs.cloud.google.com/service-extensions/docs/manage-extensions)
  * View Python and Go samples of `ext-proc` servers in the [Service Extensions GitHub repository for callouts](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/callouts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
