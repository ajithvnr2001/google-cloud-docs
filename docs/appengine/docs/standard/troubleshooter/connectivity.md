---
url: https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/connectivity/
title: App Engine connectivity strategies \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:48.528834+00:00
---

# App Engine connectivity strategies  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  App Engine connectivity strategies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes commonly used App Engine connectivity strategies, including steps related to using [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) and internal IP addresses.

  * Connect from VPC to App Engine instances
  * Connect App Engine to Cloud SQL private IP addresses
  * Customize access permissions between App Engine services



## Connect from VPC to App Engine instances

Serverless VPC Access is useful when making calls from Google's serverless offerings to a Virtual Private Cloud (VPC) network, but you can't access App Engine instances using an internal IP address.

To connect to App Engine from the VPC network using an internal IP address without an assigned external IP address, do the following:

  1. Set up [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). Ensure that the App Engine service uses a Private Google Access-enabled subnet.
  2. Use a [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoint. Ensure that the endpoint is connected to the Private Google Access-enabled subnet.
  3. Send traffic to the Private Service Connect endpoint. Ensure that the endpoint is connected to the subnet.



App Engine instances with external IP addresses can send traffic to Private Service Connect endpoints without any requirements.

### Outbound connection resets

Google Cloud can occasionally terminate and replace connection streams from your application to both [VPC](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc) and the internet when updating or restarting the underlying infrastructure. If your application reuses long-lived connections, we recommend that you configure your application to re-establish connections to avoid the reuse of a dead connection.

## Customize access permissions between App Engine services

When you have multiple App Engine services and want to configure access permissions differently between services (for example, you want to enable access to App Engine Service A only from App Engine Service B), you can use [App Engine with Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/solutions/authenticating-web-users).

For more information, see [Controlling access to websites and apps](https://docs.cloud.google.com/solutions/authenticating-web-users) and [IAP documentation](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts).

## Connect App Engine to Cloud SQL private IP addresses

To connect your App Engine apps to [Cloud SQL](https://docs.cloud.google.com/sql) instances over private IP addresses, use one of the following options:

  * **App Engine standard environment** : Use the [Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) to connect to Cloud SQL over internal IP addresses. For more information, see [Connecting from App Engine standard environment to Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard#configuring).
  * **App Engine flexible environment** : Deploy your flexible environment app in the same VPC network as your Cloud SQL instance. Your app should now be able to connect directly using Cloud SQL instance's private IP address. For more information, see [Connecting from App Engine flexible environment to Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible#configuring).



### Troubleshoot issues connecting an App Engine app to Cloud SQL

When deploying an older App Engine standard environment app with Cloud SQL using Unix sockets, you might see a few error messages if your app isn't correctly configured to connect to a Cloud SQL instance. For detailed steps to configure your app, see [Connect from App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard#configure).

The following warning message indicates that App Engine was able to fall back on a legacy connection method to complete the operation successfully:
    
    
    CloudSQL warning: your action is needed to update your application and avoid potential disruptions. Please see https://cloud.google.com/sql/docs/mysql/connect-app-engine-standard for additional details: ... 

The following error message indicates that the operation to connect to Cloud SQL wasn't completed successfully:
    
    
    Cloud SQL connection failed. Please see https://cloud.google.com/sql/docs/mysql/connect-app-engine-standard for additional details: ...

For both error messages, check the following to ensure that the [Cloud SQL Auth proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-proxy) is correctly configured to connect to a Cloud SQL instance:

  * The Cloud SQL Admin API must be enabled.
  * The service account for the App Engine app must have the correct permissions.
  * The instance connection name must include the region.



If the failure message persists after troubleshooting, contact [Google Cloud Support](https://support.google.com/cloud/#topic=3473162) for assistance. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
