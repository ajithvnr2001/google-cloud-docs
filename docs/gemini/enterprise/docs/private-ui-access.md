---
url: https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/
title: Configure private UI access \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:06.407610+00:00
---

# Configure private UI access  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure private UI access Stay organized with collections  Save and categorize content based on your preferences. 

By default, users access Gemini Enterprise interfaces for features such as agents, the assistant, and Gemini Notebook Enterprise, through the public internet. To meet organizational security requirements, you can establish private UI access using hybrid networking solutions like Cloud VPN or Cloud Interconnect.

To configure private connectivity to Gemini Enterprise, you must route Google Cloud API traffic through a Private Service Connect (PSC) endpoint. This allows users to access Gemini Enterprise interfaces through an internal IP address within your Virtual Private Cloud (VPC), avoiding the public internet.

![Reference
  architecture using VPC Service Controls to provide private access to
  Gemini Enterprise UIs.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/private-ui-access.png)Reference architecture using VPC Service Controls to provide private access to Gemini Enterprise UIs.

In this reference architecture, on-premises or multi-cloud users connect to a [PSC endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints), which enables access to Google APIs through a user-defined internal IP address within your Google Cloud Virtual Private Cloud. In addition, you must configure your internal DNS to resolve Gemini Enterprise domains to the IP address of the PSC endpoint.

## Before you begin

Before configuring private UI access, ensure that you have the following:

  * A Google Cloud Virtual Private Cloud network connected to your on-premises network through Cloud Router, using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * Permissions to create Private Service Connect endpoints and manage Cloud Router custom routes.




## Configure Private Service Connect

Private and restricted virtual IP addresses (VIPs) used for Private Google Access don't support private access to the Gemini Enterprise UI. To ensure full functionality, you must resolve the Gemini Enterprise domains to a Private Service Connect endpoint configured with the `all-apis` bundle.

  1. Create a new PSC endpoint in the same Virtual Private Cloud as the Cloud Router used for hybrid networking.

  2. Target the **All Google APIs** API bundle. This bundle provides access to most Google APIs, including `*.googleapis.com` service endpoints. The **VPC-SC** API bundle doesn't support all Gemini Enterprise domains.


**Note:** The Google APIs DNS zone `*.p.googleapis.com` is automatically generated when you create a PSC endpoint. However, using this zone from an on-premises or VPC network isn't supported in Gemini Enterprise.

## Configure network routing

The PSC endpoint uses a `/32` IP address that doesn't originate from a standard VPC subnet and won't be visible from on-premises or multi-cloud networks. You must configure your Cloud Router to advertise the IP address. For more information about IP address requirements for Private Service Connect endpoints, see [IP address requirements](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#ip-address-requirements).

  1. Identify the IP address that you assigned to your PSC endpoint.

  2. In your Cloud Router configuration, create a custom route for the IP address. For more information about specifying custom advertised routes on a Cloud Router, see [Advertise custom address ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).

  3. Update on-premises or multi-cloud firewalls to permit outbound traffic to the IP address.




## Update DNS settings

Finally, update your DNS settings to resolve the Gemini Enterprise domains using the PSC endpoint. For more information, see [Create DNS records by using default DNS names](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default).

  1. Configure internal on-premises or cloud network DNS records to resolve the following Gemini Enterprise domains to the internal IP address of the PSC endpoint:

     * `content-discoveryengine.googleapis.com`
     * `content-discoveryengine.mtls.googleapis.com`
     * `content-eu-discoveryengine.googleapis.com`
     * `content-eu-discoveryengine.mtls.googleapis.com`
     * `content-global-discoveryengine.googleapis.com`
     * `content-global-discoveryengine.mtls.googleapis.com`
     * `content-us-discoveryengine.googleapis.com`
     * `content-us-discoveryengine.mtls.googleapis.com`
     * `content-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-us-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-eu-webchannel-assistant-discoveryengine.googleapis.com`
     * `discoveryengine.googleapis.com`
     * `discoveryengine.mtls.googleapis.com`
     * `discoveryengine.clients6.google.com`
     * `eu-discoveryengine.clients6.google.com`
     * `us-discoveryengine.clients6.google.com`
     * `eu-discoveryengine.googleapis.com`
     * `eu-discoveryengine.mtls.googleapis.com`
     * `global-discoveryengine.googleapis.com`
     * `global-discoveryengine.mtls.googleapis.com`
     * `us-discoveryengine.googleapis.com`
     * `us-discoveryengine.mtls.googleapis.com`
     * `vertexaisearch.cloud.google.com`
     * `vertexaisearch.cloud.google`
     * `notebooklm.cloud.google.com`
     * `notebooklm.cloud.google`
     * `auth.cloud.google`
     * `payments.cloud.google`
     * `accounts.googleapis.com`
  2. If your environment requires strict data exfiltration protection boundaries, configure the `discoveryengine.googleapis.com` domain to the VPC-SC bundle IP address.




## Configure proxies, firewalls, and TLS inspection

If your users access Gemini Enterprise through a corporate proxy, secure web gateway, or firewall, configure these devices so that they don't block, buffer, or time out Gemini Enterprise traffic. These requirements apply whether users connect through the public internet or through a Private Service Connect endpoint.

If you don't configure these devices correctly, users might see the following symptoms:

  * The assistant stays in the **Thinking...** state and then displays the whole answer at once, instead of streaming the answer as it's generated.
  * Requests consistently fail after a fixed duration, such as 20, 30, or 60 seconds, with errors such as `HTTP 499` or `HTTP 504`.
  * The web app works on some networks, such as a home network, but not on the corporate network.



To avoid these issues, do the following:

  1. Allow outbound HTTPS traffic on port `443` to all of the Gemini Enterprise domains listed in Update DNS settings. Allow the `global`, `us`, and `eu` domains even if your app uses a single location, because the web app can call more than one of these endpoints.

  2. Exclude the following streaming domains from TLS (SSL) inspection and from response buffering or content scanning. The assistant streams its answers over these connections, and devices that hold the response until it's complete cause delays and timeouts.

     * `content-discoveryengine.googleapis.com`
     * `content-us-discoveryengine.googleapis.com`
     * `content-eu-discoveryengine.googleapis.com`
     * `content-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-us-webchannel-assistant-discoveryengine.googleapis.com`
     * `content-eu-webchannel-assistant-discoveryengine.googleapis.com`
     * `discoveryengine.clients6.google.com`
     * `us-discoveryengine.clients6.google.com`
     * `eu-discoveryengine.clients6.google.com`
  3. Set the idle and read timeouts on proxies, load balancers, and firewalls in the request path to at least 300 seconds. Complex requests, such as requests that use several connectors or agents, can take several minutes to complete.

  4. If you call the Gemini Enterprise API from your own applications, set the client request timeout to at least 300 seconds and use streaming methods where available.




## About securing your app with VPC Service Controls

For advanced security, you can implement VPC Service Controls (VPC-SC) to prevent data exfiltration from managed services like Gemini Enterprise and BigQuery. Unlike Identity and Access Management, which controls _who_ can access data, VPC-SC controls dictate _where_ data can be accessed and moved.

If considering this approach, keep the following in mind:

  * While optional, using VPC Service Controls is a best practice for blocking public access to Google services exposed through `googleapis.com`.

  * Among other implications, services (such as `discoveryengine.googleapis.com`) that are added to a VPC-SC perimeter are blocked to all public access, including access through the Google Cloud console.

  * To allow access to protected services within a VPC-SC perimeter, admins must explicitly allow ingress, by using [VPC-SC ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) or [defining access levels using Access Context Manager](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls#access-context-manager).




For more information about securing your Gemini Enterprise app using VPC-SC and Access Context Manager, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
