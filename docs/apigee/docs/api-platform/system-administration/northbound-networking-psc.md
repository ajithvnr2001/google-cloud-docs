---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc/
title: Northbound networking with Private Service Connect \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:21:50.859811+00:00
---

# Northbound networking with Private Service Connect  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Northbound networking with Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes the use of [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) to configure routing from clients to Apigee, also called "northbound" traffic. 

**Pricing information:** For information on how Private Service Connect is metered and billed, see [Private Service Connect](https://cloud.google.com/vpc/pricing#psc-forwarding-rules) on the Virtual Private Cloud pricing page.

##  Overview 

You can use Private Service Connect to connect the Apigee VPC with the VPC that you have peered with Apigee, or with any other VPC that you control. This architectural pattern eliminates the need to create managed instance groups (MIGs) to forward requests from the global load balancer to Apigee. With the Private Service Connect routing method, API proxy requests pass through an [external Application Load Balancer](https://cloud.google.com/load-balancing/docs/https) that you install in a VPC to a single point of attachment in the Apigee VPC, called a [Service Attachment](https://cloud.google.com/vpc/docs/private-service-connect#service-attachments). This configuration lets you send Apigee API proxy requests from any network-enabled machine. See Figure 1.

Note the following supported northbound Private Service Connect features: 

  * You can use Private Service Connect with any existing Apigee instance.
  * You can attach multiple Private Service Connect network endpoint groups (NEGs) to the Envoy-based, Google Cloud [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https).
  * Private Service Connect is supported with [VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc).
  * You can opt in to built-in health checking with Private Service Connect for automatic regional failover across multiple Apigee instances. No client- or load-balancer-initiated probes are required. For details, see the [PSC health check](https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check#psc-health-check) tab on _Performing health checks_.
  * You can set an outlier detection traffic policy on the backend service for handling failover scenarios automatically. See the following for more information:

    * [Traffic policies](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global#traffic_policies)
    * [Configure outlier detection](https://cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#configure_outlier_detection)
    * [REST Resource: backendServices](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices)

**Note:** If you currently use the MIG-based approach, you can migrate your system to Private Service Connect-based northbound routing. See [Migrate northbound routing to Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/migrate-from-mig-to-psc).![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/psc-arch.png)

**Figure 1: Private service connections**

##  Restrictions 

The use of Private Service Connect with Apigee currently has the following restrictions: 

**Restrictions:** Note the following restrictions for Private Service Connect configuration: 

  * [Global external HTTP(S) load balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https) is not supported for this configuration.
  * Limits apply to the number of Google Cloud projects that can connect to an Apigee instance through Private Service Connect, and to the number of Private Service Connect NEG connections that you can have per project. For details, see [ Private Service Connect Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).
  * If a Google cloud project is removed from `consumerAcceptList`, the existing Private Service Connect NEGs in that removed project will continue to work. However, any new NEGs will be rejected. You must delete existing NEGs if you remove their associated projects from the `consumerAcceptList`. Alternatively, you can recreate the Apigee instance, which recreates the service attachment in the Apigee project.



## Updating the consumer accept list for an Apigee instance

On October 10, 2024, the limit on Private Service Connect NEG connections allowed per project to an Apigee instance was raised from 20 to 100. For any Apigee instances created before that date, you must perform the steps in this section to update the consumer accept list to take advantage of the new limit. You only need to upgrade each Apigee instance once to receive the new connection limit. See also [Private Service Connect Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).

If you need to have more than 1000 Private Service Connect NEG connections in total across all of the Cloud projects connected to an Apigee instance, contact [Google Cloud Support](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support).

To update the consumer accept list of an Apigee instance to take advantage of the higher connection limit, do the following steps:

### Cloud console

For detailed steps, see [Edit the accepted projects list](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#accepted-projects).

### Apigee API

Edit the existing consumer accept list for your Apigee instance. To use the [instances API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances):

  1. Get the authentication token for the Apigee API: 
         
         TOKEN="$(gcloud auth print-access-token)"

  2. Get the list of Cloud projects in an instance's consumer accept list: 
         
         curl https://apigee.googleapis.com/v1/organizations/PROJECT_ID/instances/INSTANCE_ID \
           -H "Authorization: Bearer **$TOKEN** " -H Content-Type:application/json | jq .consumerAcceptList

  3. Create a JSON file named `update_consumer_accept_list.json` that contains the current list of accepted projects returned by the previous command. For example: 
         
         {
           "consumerAcceptList": [
             "dg-runtime-test1",
             "ne24b79b92c7db623p-tp",
             "dg-runtime-test2",
             "jd2fee78402218863p-tp"
           ]
         }

  4. Optionally, edit the file to add more projects.
  5. Update the instance, using the JSON file you created as input. For example: 
         
         curl https://apigee.googleapis.com/v1/organizations/PROJECT_ID/instances/INSTANCE_ID?updateMask="consumer_accept_list" \
           -X PATCH -H "Authorization: Bearer **$TOKEN** " -H Content-Type:application/json -d @update_consumer_accept_list.json
         




##  Configure Private Service Connect routing 

We support using Private Service Connect for northbound routing from both internal and external clients. For detailed steps, see [Step 8: Configure routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing) of the CLI provisioning instructions. 

##  Multi-region expansion with Private Service Connect 

You can expand an Apigee organization across multiple regions and use Private Service Connect for northbound routing in the new regions. For details, see [Expanding Apigee to multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region). 

##  Deleting an Apigee instance 

To delete an Apigee instance that uses Private Service Connect, follow these steps: 

  1. [Remove and delete the Private Service Connect NEG backend](https://cloud.google.com/load-balancing/docs/cleaning-up-lb-setup#deleting_the_negs) from the external load balancer.
  2. Delete the Apigee runtime instance using the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/delete). This is a long-running operation that can take up to 20 minutes to complete.
  3. Optionally retrieve the long-running operation state using the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations/get).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
