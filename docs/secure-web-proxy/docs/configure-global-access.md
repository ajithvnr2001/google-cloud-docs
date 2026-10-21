---
url: https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access/
title: Configure global access for Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:32.431008+00:00
---

# Configure global access for Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Configure global access for Secure Web Proxy Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Secure Web Proxy is a regional service. By default, your clients must be in the same Google Cloud region as the Secure Web Proxy instance.

When you enable global access for a Secure Web Proxy instance, clients can connect from _any_ region, not only the region where the proxy is deployed. This feature supports the following use cases:

  * **Outbound traffic from a specific region** : to meet cost-optimization or regulatory compliance requirements, you can enforce all outbound internet traffic to exit from a particular region.

  * **Cross-region failover** : if the primary proxy experiences any issues, you can _manually_ redirect traffic to an alternative Secure Web Proxy instance in a different region.


**Note:** Activating global access for your Secure Web Proxy instance might increase network latency and inter-region data transfer costs. You must consider these trade-offs when you design your outbound traffic management.

## Benefits

  * **Increased reliability and availability** : if a regional outage occurs, you can reroute traffic to alternative Secure Web Proxy instances in other available regions. To reroute traffic, you can either adjust routes for next hop mode or change DNS records for explicit proxy mode.

  * **Simplified network management** : manage your outbound traffic from a centralized location to simplify network administration for your organization.




## Enable global access

To enable global access, you must set the `allowGlobalAccess` field to `true` in your `gateway.yaml` file when you create a Secure Web Proxy instance.

**Important:** You can enable `allowGlobalAccess` only when you create a Secure Web Proxy instance. You can't configure this setting later.

You can enable global access for Secure Web Proxy in the following deployment modes:

  * [Explicit proxy](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart#create-a-gateway)
  * [Next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop)
  * [As a Private Service Connect (PSC) service](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)



### Configuration example

The following example shows how to enable global access when you create a Secure Web Proxy instance in the explicit proxy deployment mode:

  1. Use a text editor to create a `gateway.yaml` file.

  2. Add the following code to the `gateway.yaml` file with the `allowGlobalAccess` field set to `true`.
         
         name: projects/PROJECT_ID/locations/REGION
             /gateways/swp1
         type: SECURE_WEB_GATEWAY
         addresses: ["IP_ADDRESS"]
         ports: [443]
         gatewaySecurityPolicy: projects/PROJECT_ID/locations/REGION/gatewaySecurityPolicies/policy1
         network: projects/PROJECT_ID/global/networks/
             NETWORK
         subnetwork: projects/PROJECT_ID/regions/REGION
             /subnetworks/SUBNETWORK
         routingMode: EXPLICIT_ROUTING_MODE
         allowGlobalAccess: true
         

Replace the following:

     * `PROJECT_ID`: ID of your project

     * `REGION`: region of your Secure Web Proxy instance

     * `IP_ADDRESS`: IP address of your Secure Web Proxy instance

     * `NETWORK`: network of your Secure Web Proxy instance

     * `SUBNETWORK`: subnetwork of your Secure Web Proxy instance. You must use the [VPC subnet](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps#create-vpc-subnet) that you created as part of the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).

  3. To create the Secure Web Proxy instance, use the [`gcloud network-services gateways import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/gateways/import).
         
         gcloud network-services gateways import swp1 \
             --source=gateway.yaml
         




## Identity attributes in policy rules

Identity attributes, such as [service accounts](https://docs.cloud.google.com/secure-web-proxy/docs/use-service-accounts) and [tags](https://docs.cloud.google.com/secure-web-proxy/docs/use-tags), that are available for use in Secure Web Proxy policy rules remain functional regardless of whether you enable the global access feature.

Client applications and workloads from various Google Cloud regions can provide their identities, which your Secure Web Proxy instance can then use to enforce your policy rules. For more information, see [Supported identities for source attributes](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy#supported-identities).

## Logging and monitoring

Secure Web Proxy logs include information about the source of your outbound traffic. When you enable global access for your Secure Web Proxy instance, the logs show a client application's original region, even if it differs from your proxy region. For more information, see [Logs and metrics](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-logs).

## What's next

  * [TLS inspection overview](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview)
  * [Create an authorization policy](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies#create-authz-policy)
  * [Create a gateway security policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy#create-policy)
  * [Create a gateway security rule](https://docs.cloud.google.com/secure-web-proxy/docs/configure-rules#create-swp-rule)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
