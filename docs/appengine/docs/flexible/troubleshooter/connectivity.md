---
url: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/connectivity/
title: App Engine connectivity strategies \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:36.290213+00:00
---

# App Engine connectivity strategies  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/troubleshooter/connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  App Engine connectivity strategies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes commonly used App Engine connectivity strategies, including steps related to using [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) and internal IP addresses.

  * Connect from VPC to App Engine instances
  * Connect App Engine to Cloud SQL private IP addresses
  * Customize access permissions between App Engine services
  * Deploy an App Engine app in a Shared VPC network



## Connect from VPC to App Engine instances

Serverless VPC Access is useful when making calls from Google's serverless offerings to a Virtual Private Cloud (VPC) network, but you can't access App Engine instances using an internal IP address.

To connect to App Engine from the VPC network using an internal IP address without an assigned external IP address, do the following:

  1. Set up [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). Ensure that the App Engine service uses a Private Google Access-enabled subnet.
  2. Use a [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint. Ensure that the endpoint is connected to the Private Google Access-enabled subnet.
  3. Send traffic to the Private Service Connect endpoint. Ensure that the endpoint is connected to the subnet.



App Engine instances with external IP addresses can send traffic to Private Service Connect endpoints without any requirements.

## Customize access permissions between App Engine services

When you have multiple App Engine services and want to configure access permissions differently between services (for example, you want to enable access to App Engine Service A only from App Engine Service B), you can use [App Engine with Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/solutions/authenticating-web-users).

For more information, see [Controlling access to websites and apps](https://docs.cloud.google.com/solutions/authenticating-web-users) and [IAP documentation](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts).

## Connect App Engine to Cloud SQL private IP addresses

To connect your App Engine apps to [Cloud SQL](https://docs.cloud.google.com/sql) instances over private IP addresses, use one of the following options:

  * **App Engine standard environment** : Use the [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) to connect to Cloud SQL over internal IP addresses. For more information, see [Connecting from App Engine standard environment to Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard#configuring).
  * **App Engine flexible environment** : Deploy your flexible environment app in the same VPC network as your Cloud SQL instance. Your app should now be able to connect directly using Cloud SQL instance's private IP address. For more information, see [Connecting from App Engine flexible environment to Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible#configuring).



## Deploy an App Engine app in a Shared VPC network

Deploying an application in the App Engine flexible environment in a Shared VPC network requires an internal IP address. The internal IP address adds a route to avoid `0.0.0.0/0`.

For instances with IP mode set to `internal`, you must make the following changes to the network:

  * Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) for each subnetwork that you use.
  * Create a route compatible with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) if it doesn't already exist.
  * Create a firewall rule compatible with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) if it doesn't already exist.
  * If you need outgoing internet access, you must also deploy Cloud NAT for each region attached to subnetworks that you use.



As documented in the [internet access requirement for VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs), the network must have a valid default internet gateway route or custom route whose destination IP range is the most general (`0.0.0.0/0`). If you remove this setting, it could cause deployment or serving failures.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
