---
url: https://docs.cloud.google.com/appengine/docs/standard/migrate-direct-vpc/
title: Migrate standard VPC connector to Direct VPC egress \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:26.837890+00:00
---

# Migrate standard VPC connector to Direct VPC egress  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/migrate-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Migrate standard VPC connector to Direct VPC egress Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Direct VPC egress for App Engine**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Direct VPC egress is faster and can handle more traffic than [Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc), delivering lower latency and higher throughput because it uses a new, direct network path instead of connector instances.

Before you migrate, we recommend that you familiarize yourself with the following:

  * [Required roles for migrating to Direct VPC](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#required-roles)
  * [Direct VPC egress limitations](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#limitations)
  * [IP address management](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#best-practices)



## Migrate services to Direct VPC egress

Connectors continue to incur charges even if they have no traffic and are disconnected. For details, see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing). If you no longer need your connector, be sure to delete it.

## Migrate services to Direct VPC egress gradually

When you migrate App Engine services from Serverless VPC Access connectors to Direct VPC egress, we recommend that you do so in a gradual transition.

To transition gradually:

  1. Follow the instructions in this section to update your service to use Direct VPC egress.
  2. [Split a small percentage of traffic](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic#turning_on_traffic_splitting_in_the_console_name) to determine if the traffic routes correctly.
  3. Update the traffic split to send all traffic to the new version using Direct VPC egress.



To migrate traffic with Direct VPC egress for a service, use the Google Cloud CLI:

  1. Open your service's `app.yaml` file and remove any existing `vpc_access_connector` configurations. For example:
         
         vpc_access_connector:
           name: projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME
         

  2. Add the following `vpc_access` configuration section in your `app.yaml` file:
         
         vpc_access:
           network_interface:
             network: NETWORK
             subnet: SUBNET
             tags:
                 - NETWORK_TAGS
           vpc_egress: EGRESS_SETTING

Replace the following:

     * NETWORK: the name of the existing network your application instances connect to, for example, `default`.

     * SUBNET: the name of the existing subnetwork your application instances connect to, for example, `default`.

     * Optional: NETWORK_TAGS: a list of network tags to associate with your App Engine service's instances for use in firewall rules and routing policies.

     * Optional EGRESS_SETTING: controls how outbound traffic is routed. This field supports the following configuration settings:

       * `all-traffic`: All outbound requests are routed through the VPC network.
       * `private-ranges-only` (default): Only traffic to internal IP addresses is routed through the VPC network. Internet traffic uses the default App Engine path.
  3. Re-deploy your service to App Engine by running the following command. The deployed version won't handle any live traffic initially:
         
         gcloud beta app deploy --no-promote

  4. To determine if traffic routes correctly, [split a small percentage of traffic](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic#turning_on_traffic_splitting_in_the_console_name) to the new version that uses Direct VPC egress.

  5. After verifying that traffic is routed correctly, [migrate all traffic](https://docs.cloud.google.com/appengine/docs/standard/migrating-traffic) to the new version.

  6. If you no longer need your Serverless VPC Access connector, [delete it](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#delete) to stop incurring costs.




## What's next

  * Learn more about the [best practices for IP management](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#best-practices).
  * Learn how to [secure your App Engine app](https://docs.cloud.google.com/appengine/docs/standard/application-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
