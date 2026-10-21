---
url: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies/
title: Create and configure monitoring policies \u00a0|\u00a0 Network Intelligence Center - Cloud Network Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:22.929141+00:00
---

# Create and configure monitoring policies  |  Network Intelligence Center - Cloud Network Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/configure-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Cloud Network Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/overview)



#  Create and configure monitoring policies Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring policies are sets of rules that govern how probes on Monitoring Points behave. They generate active paths between a Monitoring Point (source) and a destination (target) that are continuous streams of telemetry data. Monitoring policies are created and managed within AppNeta, not Google Cloud console.

A monitoring policy includes the following:

  * **Source (Who)** : Defines which Monitoring Points should run these probes (for example, _All MPs in`us-east1`_ or _Only the MP named`office-proxy`_).
  * **Target (What)** : Defines what's being probed (for example, `www.google.com`, a specific internal IP, or a SaaS application).
  * **Configuration (How/When)** : Defines the test type (such as network or web monitoring), probe frequency, and specific protocols (ICMP, TCP, HTTP, HTTPS) to use.



To support monitoring environments of all sizes, Cloud Network Insights provides the ability to create single policies and to group policies together.

  * **Single monitoring policies** : An individual set of rules for defining a specific monitoring scenario. It contains all the Monitoring Point source, target, and configuration details for a single destination.
  * **Monitoring policy groups** : A container for multiple monitoring policies that targets a managed list of IPs or hostnames. Use monitoring policy groups for consistent monitoring preferences and more streamlined updates to policies. For more information about monitoring policy groups, see [Manage Monitoring Policy Groups](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring/delivery-setup-monitoring-policies/delivery-monitoring-policy-groups.html) in the AppNeta documentation.



You can also use tags attached to Monitoring Points to apply policies quickly and consistently to multiple Monitoring Points. Tags are key-value pairs that provide additional context, such as location or role. If you create a monitoring policy that uses tags as the source, then any Monitoring Point you add with that tag is included in the monitoring policy automatically.

For more information on tags, see [Tagging - Best Practices](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring/tag-best-practices.html) in the AppNeta documentation.

## Types of monitoring

Cloud Network Insights supports two types of monitoring policies: network monitoring (network paths) and web monitoring (web paths).

### Network monitoring

Network monitoring policies create network paths—hop-by-hop visualizations of the infrastructure (Layers 3 and 4) that support your applications. As data travels between the source and the target, Cloud Network Insights monitors the end-to-end path, including the hops. Network paths support two different types of paths:

  * **Single-ended paths** : The Monitoring Point probes an external target (for example, `google.com`, a SaaS VIP, or a router) that _does not_ have a Monitoring Point installed. This relies on standard protocols (ICMP, TCP, UDP, or Echo) and is ideal for monitoring public or third-party targets.
  * **Dual-ended paths** : The Monitoring Point probes a different Monitoring Point. Since you control both ends, this mode provides richer data, including precise one-way latency, jitter, and the ability to detect asymmetric routing (for example, different paths for uploading versus downloading).



For more information about Network Monitoring, see [Considerations for Network Monitoring Setup](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring/delivery-setup-monitoring-policies/path-considerations-monitoring-policies.html) in the AppNeta documentation.

### Web monitoring

Web monitoring policies create web paths—a monitor of the end-to-end experience of the web application (Layer 7). Web paths measure app responsiveness, including the following:

  * DNS resolution time
  * TCP/TLS handshake time
  * HTTP status codes (for example, `200 OK` or `503 Service Unavailable`)



You can set web monitoring policies to emulate user behaviors in the browser using Selenium scripts or to emulate API calls through HTTP or HTTPS requests. For more information about Web Monitoring, see [Web Monitoring Overview](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring/experience-deploy/experience-intro.html) in the AppNeta documentation.

## Before you begin

You must [deploy a Monitoring Point](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/add-monitoring-points) before you can create monitoring policies.

### Required roles

To get the permissions that you need to create monitoring policies, ask your administrator to grant you the [Cloud Network Insights Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkmanagement#networkmanagement.CloudNetworkInsightsEditor) (`roles/networkmanagement.CloudNetworkInsightsEditor`) IAM role on the project in which Cloud Network Insights is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create monitoring policies

While you deploy Monitoring Points using Google Cloud, you configure monitoring policies in AppNeta.

  1. In the Google Cloud console, navigate to **Network Intelligence** > **Cloud Network Insights**.

[Go to Cloud Network Insights](https://console.cloud.google.com/net-intelligence/cloud-network-insights)

  2. To create a network monitoring policy, open the **Network Paths** page and click **Create Network Monitoring Policy (AppNeta UI)**. The **Policy Details** page opens in AppNeta.

For detailed instructions on creating network monitoring policies, see [Manage Monitoring Policies](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring/delivery-setup-monitoring-policies/managing-monitoring-policies.html) in the AppNeta documentation.

  3. To create a web monitoring policy, open the **Web Paths** page and click **Create Web Monitoring Policy (AppNeta UI)**. The **Policy Details** page opens in AppNeta.

For detailed instructions on creating web monitoring policies, see [Create Monitoring Policies with Web Monitoring](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring/experience-deploy.html) in the AppNeta documentation.

  4. You might be prompted to sign in to AppNeta using Google Single Sign-On and asked to authorize AppNeta to read Google Cloud data.




For more information on creating monitoring policies, see [Set Up Monitoring](https://techdocs.broadcom.com/us/en/ca-enterprise-software/it-operations-management/appneta-for-google-cloud-network-insights/GA/set-up-monitoring.html) in the AppNeta documentation.

## What's next

Although the policies are configured in AppNeta, the resulting network path and web path data, including metrics, alarm logs, and event logs, are available within the Google Cloud console.

  * View performance metrics in [dashboards](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/view-dashboards) and analyze trends.
  * Set up alarm rules for [alerts and notifications](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-alerts) or [view logs](https://docs.cloud.google.com/network-intelligence-center/docs/cloud-network-insights/set-up-logging).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
