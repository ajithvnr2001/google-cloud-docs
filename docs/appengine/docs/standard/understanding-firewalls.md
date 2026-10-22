---
url: https://docs.cloud.google.com/appengine/docs/standard/understanding-firewalls/
title: Understanding the App Engine firewall \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:26.911078+00:00
---

# Understanding the App Engine firewall  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/understanding-firewalls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
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

You can [configure App Engine firewall rules](https://docs.cloud.google.com/appengine/docs/standard/creating-firewalls) using the Google Cloud console, the Google Cloud CLI, or the Admin API by specifying rules that allow or block specified IP ranges.

By default, any request that does not match a rule is allowed access to your app. If you need to block all requests that do not match a specific rule (excluding requests from internal services allowed by default), change the `default` rule's action to `deny`.

### Firewall feature

In the App Engine standard environment, the App Engine firewall can allow certain internal traffic to bypass the firewall. This means that if you set the `default` rule to `deny`, requests from certain services destined for the App Engine standard environment do not get blocked. These are all types of traffic requested in the app's own configuration, or sent from the same app. Requests that bypass firewall rules in this way include:

  * [Warmup requests](https://docs.cloud.google.com/appengine/docs/standard/configuring-warmup-requests)
  * Cloud Scheduler jobs using [App Engine HTTP](https://docs.cloud.google.com/scheduler/docs/creating#creating_jobs) (including [App Engine Cron](https://docs.cloud.google.com/appengine/docs/standard/scheduling-jobs-with-cron-yaml))
  * [App Engine tasks in Cloud Tasks](https://docs.cloud.google.com/tasks/docs/creating-appengine-tasks) (including App Engine Task Queues)



For apps that use the App Engine standard environment and services bundled with the [first generation runtimes](https://docs.cloud.google.com/appengine/docs/standard/runtimes), notifications from the legacy Mail API also bypass the firewall.

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

  * Requests from newly created or updated App Engine Cron jobs sent to either the App Engine standard or flexible environment come from `0.1.0.2`. For Cron jobs created with older gcloud versions (earlier than 326.0.0), Cron requests will come from `0.1.0.1`. To learn more about how to identify requests from the App Engine Cron service, see [Validating cron requests](https://docs.cloud.google.com/appengine/docs/standard/scheduling-jobs-with-cron-yaml#validating_cron_requests).
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


  * We recommend that you [use ingress controls](https://docs.cloud.google.com/appengine/docs/standard/application-security#ingress_controls) so that your app only receives requests sent from the load balancer (and the VPC if you use it). Otherwise, users can use your app's App Engine URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.

  * If your [ingress controls](https://docs.cloud.google.com/appengine/docs/standard/application-security#ingress_controls) are set to receive `internal-and-cloud-load-balancing` traffic, leave the default App Engine firewall rule as is (`allow`), and use [Google Cloud Armor web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning).




## Preventing access to cached content

The App Engine firewall sits behind mechanisms that cache content, for example web proxies and browsers. When content is cached, that content is served publicly from the specific URL until it expires and can be accessed even after creating new firewall rules.

For information about changing the default expiration time for static content or preventing static content from being cached, see [Cache expiration](https://docs.cloud.google.com/appengine/docs/standard/how-requests-are-handled#static_cache_expiration). 

To prevent dynamic content output from your app's code from being cached, use the `Cache-Control` and `Expires` HTTP response headers. For more information about these HTTP headers, including how to control caching, see [Avoiding caching](https://wikipedia.org/wiki/List_of_HTTP_header_fields#Avoiding_caching). 

## What's next

Follow the instructions in [Creating Firewalls](https://docs.cloud.google.com/appengine/docs/standard/creating-firewalls) to learn how to configure App Engine firewall rules.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
