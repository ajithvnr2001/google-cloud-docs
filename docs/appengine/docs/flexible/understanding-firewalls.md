---
url: https://docs.cloud.google.com/appengine/docs/flexible/understanding-firewalls/
title: Understanding the App Engine firewall \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:59.007078+00:00
---

# Understanding the App Engine firewall  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/understanding-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Understanding the App Engine firewall Stay organized with collections  Save and categorize content based on your preferences. 

A **firewall** determines which network traffic is allowed to pass and which traffic is rejected. Firewalls can apply to incoming traffic (ingress), outgoing traffic (egress), or both. For App Engine, the App Engine firewall only applies to incoming traffic routed to your app or service.

## Overview

The App Engine firewall is checked for all types of requests to your app, including:

  * Regular web traffic routed to the app's `appspot.com` address or custom domain.
  * Requests that arrive from [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing).
  * Traffic from internal sources such as Compute Engine virtual machines (VMs) and Cloud Tasks.



In cases where your app is configured to use other networking services or products, you might need to create rules for controlling incoming traffic in both the App Engine firewall and the firewall or security settings of other products. This guide covers the general behavior of the App Engine firewall, and details about those special use cases.

## App Engine firewall rules

You can [configure App Engine firewall rules](https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls) using the Google Cloud console, the Google Cloud CLI, or the Admin API by specifying rules that allow or block specified IP ranges.

By default, any request that does not match a rule is allowed access to your app. If you need to block all requests that do not match a specific rule (excluding requests from internal services allowed by default), change the `default` rule's action to `deny`.

In certain circumstances, it's possible for the App Engine flexible environment to automatically configure firewall rules at the [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/vpc) level, but note that the VPC firewall does not interact with the App Engine firewall.

## Allowing incoming requests from your services

The following table lists the IP ranges and App Engine firewall behavior for common services. The IP range you use depends on whether the incoming requests are delivered to a version that runs on the App Engine standard environment or flexible environment.

Service | IP range for requests sent to the App Engine standard environment | IP range for requests sent to the App Engine flexible environment  
---|---|---  
App Engine Cron  | 0.1.0.1/32 or 0.1.0.2/32, bypasses the default firewall rule if set to deny  | 0.1.0.1/32 or 0.1.0.2/32   
Compute Engine instances with external IP addresses  | External IP address of the instance  | External IP address of the instance   
Compute Engine instances without an external IP address  | 0.0.0.0/32  | 0.0.0.0/32   
Compute Engine instances without an external IP address using Cloud NAT for outbound connections  | 0.0.0.0/32  | 0.0.0.0/32   
Cloud Scheduler jobs using App Engine HTTP and App Engine tasks in Cloud Tasks (including App Engine Task Queues)  | 0.1.0.2/32, bypasses the default firewall rule if set to deny  | 0.1.0.2/32   
Cloud Storage or Blobstore  | 0.1.0.30/32  | Not applicable   
URL Fetch  | 0.1.0.40/32  | 0.1.0.40/32   
Warming requests  | 0.1.0.3/32, bypasses the default firewall rule if set to deny  | Not applicable   
  
Depending on your use case, these additional instructions might apply when configuring App Engine firewall rules:

  * Requests from newly created or updated App Engine Cron jobs sent to either the App Engine standard or flexible environment come from `0.1.0.2`. For Cron jobs created with older gcloud versions (earlier than 326.0.0), Cron requests will come from `0.1.0.1`. To learn more about how to identify requests from the App Engine Cron service, see [Validating cron requests](https://docs.cloud.google.com/appengine/docs/flexible/scheduling-jobs-with-cron-yaml#validating_cron_requests).
  * If your app interacts with Cloud Load Balancing or is connected to a VPC network, see the Interaction with other products or services section below.

**Caution:** Creating a rule for IP `0.0.0.0` will apply to **all** Compute Engine instances with Private Google Access enabled, not only the ones you own. Similarly, allowing requests from `0.1.0.40` will allow **any** App Engine app to make URL Fetch requests to your app.

### App Engine standard example

Your app running in the standard environment has two services: `frontend_service` and `backend_service`. `frontend_service` uses Cloud Tasks with App Engine HTTP to send messages to `backend_service`. Since the `default` firewall rule allows Cloud Tasks requests even if configured to `deny`, you do not need to create a firewall rule for Cloud Tasks.

However, if you wanted to restrict access to your app and explicitly block Cloud Tasks requests, you would create a `deny` firewall rule for IP range `0.1.0.2/32`.

### App Engine flexible example

Your app running in the flexible environment has two services: `frontend_service` and `backend_service`, and has a firewall configured to deny traffic by default. `frontend_service` uses Cloud Tasks with App Engine HTTP to send messages to `backend_service`. Since the `default` firewall rule denies Cloud Tasks requests, you would need to create an `allow` firewall rule for `0.1.0.2/32`.

## Interaction with other products or services

### Cloud Load Balancing

If you use [Cloud Load Balancing and serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts), note the following:

  * The load balancer does not interfere or interact with App Engine firewall rules. The App Engine firewall rules are not evaluated until a serverless NEG directs traffic to App Engine.


  * We recommend that you [use ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/application-security#ingress_controls) so that your app only receives requests sent from the load balancer (and the VPC if you use it). Otherwise, users can use your app's App Engine URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.

  * If your [ingress controls](https://docs.cloud.google.com/appengine/docs/flexible/application-security#ingress_controls) are set to receive `internal-and-cloud-load-balancing` traffic, leave the default App Engine firewall rule as is (`allow`), and use [Google Cloud Armor web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning).




### VPC firewall

App Engine firewalls are configured and enforced independently of [VPC-based](https://docs.cloud.google.com/vpc/docs/vpc) firewalls. VPC firewall rules apply to resources running in the VPC network, such as Compute Engine virtual machines, whereas App Engine firewall rules apply to incoming requests to your app or service.

If there are VPC-based firewall rules (such as [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) or [hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies)) configured in your network environment, **both** VPC-level firewalls and App Engine firewalls need to allow an incoming request's IP range for your App Engine app to receive it.

For VPC-level firewalls, Hierarchical firewall policies are evaluated before VPC firewall rules and follow a sequence during VPC firewall evaluation. Requests that are allowed by both the VPC-level firewall and App Engine firewall are received by your App Engine app or service. If the VPC firewall denies requests from the same IP range that is allowed by the App Engine firewall, access is not permitted to your App Engine app.

### Shared VPC

The App Engine flexible environment can create firewall(s) depending on whether your app is configured to use a VPC network through [Shared VPC](https://docs.cloud.google.com/appengine/docs/flexible/using-shared-vpc).

**If your App Engine flexible app uses Shared VPC** , the App Engine flexible environment does not automatically create firewall rules. if you need to control access and allow traffic on the VPC network, you can create firewall rules on the Shared VPC network.

Additionally, to allow requests from a traffic source, you need to allow the same IP range in the VPC firewall **and** in the App Engine firewall. Without specifying the IP range in both places (VPC firewall and App Engine firewall), that IP range won't be permitted to access your App Engine app or service.

**If your App Engine flexible environment app is not configured to use Shared VPC** , the App Engine flexible environment creates up to two hidden VPC firewall rules, depending on whether your app uses split [health checks](https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls#app_engine_flexible_considerations) (default) or legacy health checks. These hidden firewall rules allow serving traffic and health check traffic to the flexible environment:

  * **Network name** : The network specified in `app.yaml`, or the default network if no network is configured.
  * **Target tag** : The `instance_tags` specified in `app.yaml` file. By default, if no target tags are provided, the App Engine flexible environment generates a unique tag that follows the format of `aef-INSTANCE_ID`. This tag only affects the instances in that specific flexible version, and the firewall rule will target this tag.
  * **Direction of traffic** : Ingress
  * **Action on match** : Allow
  * **Source IP ranges** : `35.191.0.0/16` and `130.211.0.0/22`
  * **Protocols and ports** : 
    * **tcp** : `8443` (for legacy health checks) or `10402` (for split health checks)
  * **Priority** : `1000`



## Preventing access to cached content

The App Engine firewall sits behind mechanisms that cache content, for example web proxies and browsers. When content is cached, that content is served publicly from the specific URL until it expires and can be accessed even after creating new firewall rules.

To prevent your content from being cached, use the `Cache-Control` and `Expires` HTTP response headers. For more information about these HTTP headers, including how to control caching, see [Avoiding caching](https://wikipedia.org/wiki/List_of_HTTP_header_fields#Avoiding_caching). 

## What's next

Follow the instructions in [Creating Firewalls](https://docs.cloud.google.com/appengine/docs/flexible/creating-firewalls) to learn how to configure App Engine firewall rules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
