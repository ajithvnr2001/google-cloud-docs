---
url: https://docs.cloud.google.com/nat/docs/apis/
title: APIs and reference \u00a0|\u00a0 Cloud NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:07.736679+00:00
---

# APIs and reference  |  Cloud NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Reference ](https://docs.cloud.google.com/nat/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APIs and reference

This page describes individual resources that can be used with Cloud NAT.

The Cloud NAT APIs and `gcloud` commands are part of Compute Engine.

Cloud NAT is configured using new [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router) commands and parameters.

## gcloud CLI commands

Existing Cloud Router commands can be found in the [Google Cloud CLI interface documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers).

The following table lists the commonly used Cloud NAT commands:

Command | Description  
---|---  
[`gcloud compute routers nats create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create) | Adds a NAT configuration to a router.  
[`gcloud compute routers nats update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update) | Updates a NAT configuration on a router.  
[`gcloud compute routers nats delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/delete) | Removes a NAT configuration from a router.  
[`gcloud compute routers nats list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/list) | Lists NAT configurations on a router.  
[`gcloud compute routers nats describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/describe) | Shows a NAT configuration on a router.  
[`gcloud compute routers get-status`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-status) | Gets runtime information on the specified Cloud Router, including the status of the NAT.  
[`gcloud compute routers get-nat-mapping-info`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-mapping-info) | Shows NAT IP:port-ranges.  
[`gcloud compute routers get-nat-ip-info`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info) | Shows NAT IP address usage.  
[`gcloud compute routers nats rules create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/create) | Adds a NAT rule to an existing NAT gateway.  
[`gcloud compute routers nats rules update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update) | Updates a single NAT rule.  
[`gcloud compute routers nats rules delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/delete) | Deletes a NAT rule from a NAT gateway.  
[`gcloud compute routers nats rules describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/describe) | Describes a NAT rule.  
[`gcloud compute routers nats rules list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/list) | Lists all NAT rules in a NAT gateway.  
  
## Rest API

All NAT operations are performed on the [Router](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers) resource. They all require OAuth 2.0 authentication.

The following table lists the commonly used Cloud Router APIs:

Command | Description  
---|---  
[`routers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert) | Creates a Cloud Router. You can specify a NAT configuration when you create the router.  
[`routers.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update) | Updates a Cloud Router. You can specify a NAT configuration when you update the router.  
[`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) | Patches a Cloud Router. You can specify a NAT configuration when you patch the router.  
[`routers.getRouterStatus`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus) | Gets runtime information on the specified Cloud Router, including the status of the NAT.  
[`routers.getNatMappingInfo`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getNatMappingInfo) | Retrieves runtime NAT mapping information of VM endpoints.  
[`routers.getNatIpInfo`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getNatIpInfo) | Retrieves runtime NAT IP address information for the specified Cloud Router.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
