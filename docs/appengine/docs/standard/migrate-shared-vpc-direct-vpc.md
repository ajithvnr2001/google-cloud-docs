---
url: https://docs.cloud.google.com/appengine/docs/standard/migrate-shared-vpc-direct-vpc/
title: Migrate Shared VPC connector to Direct VPC egress \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:35.019236+00:00
---

# Migrate Shared VPC connector to Direct VPC egress  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/migrate-shared-vpc-direct-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Migrate Shared VPC connector to Direct VPC egress Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Direct VPC egress for App Engine**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page is for networking specialists who want to migrate Shared VPC network traffic from using [Serverless VPC Access connectors](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc) to using [Direct VPC egress](https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-direct-vpc) when sending traffic to a Shared VPC network.

Direct VPC egress is faster and can handle more traffic than connectors, delivering lower latency and higher throughput because it uses a new, direct network path instead of connector instances.

Before migration, we recommend that you familiarize yourself with Direct VPC egress [prerequisites](https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-direct-vpc#before-you-begin), [limitations](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#limitations), [IP address allocation](https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-direct-vpc#direct-vpc-ip-addresses), and [IAM permissions](https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-direct-vpc#iam).

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
         

  2. Add the following `vpc_access` configuration section in your `app.yaml` file, specifying the fully qualified resource names for the Shared VPC network and subnet in the host project:
         
         vpc_access:
           network_interface:
             network: projects/HOST_PROJECT_ID/global/networks/VPC_NETWORK
             subnet: projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
             tags:
                 - NETWORK_TAGS
           vpc_egress: EGRESS_SETTING

Replace the following:

     * HOST_PROJECT_ID: the ID of your Shared VPC host project.

     * VPC_NETWORK: the name of your Shared VPC network.

     * REGION: the region for your App Engine service, which must match the region of your subnet.

     * SUBNET_NAME: the name of your subnet.

     * Optional: NETWORK_TAGS: a list of network tags to associate with your App Engine service's instances for use in firewall rules and routing policies.

     * Optional: EGRESS_SETTING: controls how outbound traffic is routed. This field supports the following configuration settings:

       * `all-traffic`: All outbound requests are routed through the VPC network.
       * `private-ranges-only` (default): Only traffic to internal IP addresses is routed through the VPC network. Internet traffic uses the default App Engine path.
  3. Re-deploy your service to App Engine by running the following command:
         
         gcloud beta app deploy

  4. After verifying that your service connects to the VPC network correctly, delete the old Serverless VPC Access connector to stop incurring costs.




## What's next

  * Learn more about the [Best practices for IP management](https://docs.cloud.google.com/appengine/docs/standard/vpc-direct-vpc#best-practices).
  * Learn how to [secure your App Engine app](https://docs.cloud.google.com/appengine/docs/standard/application-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
