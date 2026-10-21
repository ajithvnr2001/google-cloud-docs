---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/migrate-from-mig-to-psc/
title: Migrate northbound routing to Private Service Connect \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:18:23.542796+00:00
---

# Migrate northbound routing to Private Service Connect  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/migrate-from-mig-to-psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Migrate northbound routing to Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Important:** This topic only applies to organizations that were created with VPC peering enabled. See also [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

This document explains how to migrate your client-to-Apigee (also called "northbound") routing configuration from a managed instance group (MIG) configuration to a [Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc) based configuration. 

##  Overview 

If you are currently using the [managed instance group (MIG) based configuration](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing) using a [Global external HTTPS Load Balancer (Classic)](https://docs.cloud.google.com/load-balancing/docs/https) for routing external traffic to Apigee, you can choose to migrate this "northbound" traffic to use a Private Service Connect-based configuration.

**Important:** Because the classic global external HTTPS load balancer does not support Private Service Connect NEG backends, you must create a new external Application Load Balancer and switch the incoming traffic through DNS.

##  Migration steps 

**Note:** To ensure that the load balancer operates as expected, you must carry over any classic HTTPS load balancer [configurations or add-on features](https://docs.cloud.google.com/load-balancing/docs/features) to the new external Application Load Balancer.

  1. Configure northbound routing to Apigee endpoints. For this task, follow the steps under the **External routing (Private Service Connect)** tab under [Configure routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing) in the Apigee CLI provisioning document.
  2. If you have multiple Apigee instances (a multi-region use case), create corresponding NEGs for each of the Apigee regions and attach them to the backend service of the load balancer. See [Expanding Apigee to multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region).
  3. Test the new global load balancer endpoint.
  4. When testing is complete, switch all of your existing DNS entries to point to the new load balancer endpoint. Note the following: **Note:**
     * Different DNS providers support different kinds of routing policies. For example: [Cloud DNS supports](https://docs.cloud.google.com/dns/docs/zones/manage-routing-policies) weighted round robin (WRR) routing policy, which ensures the traffic is distributed according to the configured weights. Such routing policy can be leveraged for switching the traffic between the 2 load balancer endpoints. 
     * The new global external load balancer (GXLB) endpoint can be added to the customer's DNS endpoint with small weight, enough to allow 5% or 10% of their traffic. This can be slowly ramped to allow 100% of traffic on the new GXLB endpoint and 0% on the old GXLB (Classic) endpoint. 
     * Remove the old GXLB (Classic) endpoint from the DNS, and delete the old GXLB (Classic) along with the MIG backend.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
