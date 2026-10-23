---
url: https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip/
title: Configure private internal-only services \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:28.636669+00:00
---

# Configure private internal-only services  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Configure private internal-only services Stay organized with collections  Save and categorize content based on your preferences. 

This page shows the required configuration for exposing an App Engine flexible environment service only on its internal IP address.

By default, flexible environment services receive both an internal IP address and an ephemeral external IP address when they are first deployed. The ephemeral external IP address allows your service to send requests to App Engine services with custom domains, and resources on the internet. Ephemeral external IP addresses incur [costs](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).

If your service does not require an external IP address, you can prevent your service from sending requests to resources on the internet and reduce costs by limiting your service to using only its internal IP address. This does not prevent your service from receiving requests from the internet or App Engine services with custom domains, because the fully qualified domain name of your service is still externally visible.

## Limitations

Disabling ephemeral external IP addresses has the following limitations:

  * **Services with custom domains:** To send requests to App Engine services with custom domains you must [configure Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation).
  * **External resources:** To send requests to external resources you must [configure Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation).
  * **Private Google Access dependency:** Instances with IP mode set to `internal` require [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access#pga-supported) on the target subnetwork.
  * **Legacy networks:** [Legacy networks](https://docs.cloud.google.com/vpc/docs/legacy) cannot use Private Google Access, and thus cannot disable ephemeral external IP addresses.



## Before you begin

To deploy flexible environment apps without external IP addresses, you must enable Private Google Access on the target subnetwork.

  * To learn about Private Google Access, see the [Overview](https://docs.cloud.google.com/vpc/docs/private-google-access#pga-supported).
  * For step-by-step configuration instructions, see [Enabling Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).



### Prepare your Shared VPC network

If you use Shared VPC, follow these steps to prepare your Shared VPC network for further configuration.

  1. Verify that you have a route that is compatible with Private Google Access. Typically the [default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) of a network is compatible with Private Google Access. For other routes, confirm that the route is configured as follows.
         
         Network: SHARED_VPC_NETWORK_NAME
         Destination IP address range: 0.0.0.0/0
         Instance tags: INSTANCE_TAGS
         Next hop: DEFAULT_INTERNET_GATEWAY
         

Replace the following:

     * `SHARED_VPC_NETWORK_NAME`: The name of your Shared VPC network.
     * `INSTANCE_TAGS`: If you do not use any instance tags, do not specify anything in this field. If you do use instance tags, include `aef-instances` in your list of instance tags.
     * `DEFAULT_INTERNET_GATEWAY`: The default internet gateway.

To learn more about compatible routes for Private Google Access, see the Private Google Access documentation on [routing options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing).

  2. Verify that you have a firewall rule that is compatible with Private Google Access. The firewall rule must be configured as follows.
         
         Network: SHARED_VPC_NETWORK_NAME
         Destination IP address range: 0.0.0.0/0
         Destination filter: IP ranges
         Direction of traffic: Egress
         Attach on match: Allow
         Instance tags: INSTANCE_TAGS
         

Replace the following:

     * `SHARED_VPC_NETWORK_NAME`: The name of your Shared VPC network.
     * `INSTANCE_TAGS`: If you do not use any instance tags, do not specify anything in this field. If you do use instance tags, include `aef-instances` in your list of instance tags.

To learn more about compatible firewall rules for Private Google Access, see the Private Google Access documentation on [firewall configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-firewall).




## Configure your service to use only its internal IP address

  1. Update the Google Cloud CLI. This ensures that you are using a version of the gcloud CLI that supports private IP addresses for flexible environment apps.
         
         gcloud components update

  2. In your `app.yaml` file, add the `instance_ip_mode` field to the [`network` section](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#network_settings) and set it to `internal`.

     * If your `app.yaml` file already has a `network` section, add the following line inside the `network` section: 
           
           instance_ip_mode: internal

     * If your `app.yaml` file doesn't have a `network` section, create the section and specify the instance IP mode by adding the following lines: 
           
           network:
            instance_ip_mode: internal

Save these changes.

  3. Deploy the service.
         
         gcloud beta app deploy

  4. Verify configuration by checking the Instances page of the Google Cloud console.

[Go to Instances](https://console.cloud.google.com/appengine/instances)

Scroll down to the **Instances** table (below the **Summary** chart). In the **External IP** column, confirm that there is no IP address listed. The absence of an IP address in this column means that your instance has no external IP address. Even though this field is empty, your instance still has an internal IP address.




## Send external requests without an external IP address

If your service sends requests to the internet but you want to limit it to using only its internal IP address, you can use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to create a gateway. Your service can send external requests through the Cloud NAT gateway without using the default ephemeral external IP addresses.

  1. Follow the steps in the section Configure your service to use only its internal IP address.

  2. Follow the steps to [Configure Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation).




To learn more about this approach, see the Cloud Architecture Center documentation on [Deploying Cloud NAT for fetching](https://docs.cloud.google.com/architecture/building-internet-connectivity-for-private-vms#deploying_cloud_nat_for_fetching).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
