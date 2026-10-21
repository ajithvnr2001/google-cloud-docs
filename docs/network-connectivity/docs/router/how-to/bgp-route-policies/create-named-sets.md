---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-named-sets/
title: Create named sets \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:20.970907+00:00
---

# Create named sets  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-named-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create named sets

This guide describes how to create a named set in Cloud Router.

The examples on this page create two named sets of different types: a prefix set and a community set.

The prefix set is named `allowed-prefixes` and contains the following items:

  * `'192.168.0.0/16'`
  * `'fd00::/8'`
  * `prefix('10.0.0.0/20').orLonger()`



The community set is named `allowed-communities` contains the following items:

  * `'64500:100'`
  * `'64500:200'`



You can create named sets for Cloud Router in two ways:

  * Use Google Cloud CLI to build a named set
  * Use your preferred text editor to create a JSON or YAML file, and then use gcloud CLI to upload the named set



## Build named sets

The names of the named sets must be unique within the router. This section builds named sets using the gcloud CLI.

### Build a prefix set

To build a prefix set, do the following:

  1. To create an empty prefix named set called `allowed-prefixes`, run the following command: 
         
         gcloud compute routers add-named-set ROUTER_NAME
             --set-name=allowed-prefixes
             --set-type=prefix
         

Replace ROUTER_NAME with the name of the Cloud Router.
  2. To add each of the elements to the `allowed-prefixes` named set, run the [`add-named-set-element`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/add-named-set-element) command for each element: 
         
         gcloud compute routers add-named-set-element ROUTER_NAME
             --set-name=allowed-prefixes
             --new-set-element="'192.168.0.0/16'"
         
         
         
         gcloud compute routers add-named-set-element ROUTER_NAME
             --set-name=allowed-prefixes
             --new-set-element="'fd00::/8'"
         
         
         
         
         
         gcloud compute routers add-named-set-element ROUTER_NAME
             --set-name=allowed-prefixes
             --new-set-element="prefix('10.0.0.0/20').orLonger()"
         




### Build a community set

To build a community set, do the following:

  1. To create an empty community set called `allowed-communities`, run the following command: 
         
         gcloud compute routers add-named-set ROUTER_NAME
             --set-name=allowed-communities
             --set-type=community
         

  2. To add each of the elements to the `allowed-communities` named set, run the [`add-named-set-element`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/add-named-set-element) command for each element: 
         
         gcloud compute routers add-named-set-element ROUTER_NAME
             --set-name=allowed-communities
             --new-set-element="'64500:100'"
         
         
         
         gcloud compute routers add-named-set-element ROUTER_NAME
             --set-name=allowed-communities
             --new-set-element="'64500:200'"
         




## Upload named sets

When creating a JSON or YAML file, use one of the following named set types:

  * NAMED_SET_TYPE_COMMUNITY
  * NAMED_SET_TYPE_PREFIX



The [`upload-named-set`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/upload-named-set) command overwrites any named set with the same name.

  1. To create named sets called `allowed-prefixes` and `allowed-communities`, create the named sets in your preferred text editor. You can use YAML or JSON formatting to create them.

**allowed-prefixes.yaml:**
         
         # Prefix set
         resource:
           elements:
           - expression: "'192.168.0.0/16'"
           - expression: "'fd00::/8'"
           - expression: "prefix('10.0.0.0/20').orLonger()"
           name: allowed-prefixes
           type: NAMED_SET_TYPE_PREFIX
         

**allowed-communities.yaml:**
         
         # Community set
         resource:
           elements:
           - expression: "'64500:100'"
           - expression: "'64500:200'"
           name: allowed-communities
           type: NAMED_SET_TYPE_COMMUNITY
         

  2. To upload the named sets, run the following commands: 
         
         gcloud compute routers upload-named-set ROUTER_NAME
             --set-name=allowed-prefixes
             --file-name=allowed-prefixes.yaml
             --file-format=json
         
         
         gcloud compute routers upload-named-set ROUTER_NAME
             --set-name=allowed-communities
             --file-name=allowed-communities.json
             --file-format=json
         

Replace ROUTER_NAME with the name of the Cloud Router.




## Prefix Set Elements

Elements of prefix sets must be either a prefix literal (string) or a prefix range object. These are the same prefix literal and prefix ranges defined for use in route policies.

The following table describes each element of a prefix set.

Expression | Description  
---|---  
`'192.168.0.0/24'` | Prefix literal.  
`prefix('192.168.0.0/24')` | Prefix match object.  
`p.longer()` | Prefix range object that is a copy of _p_ with the end of the range set to the input prefix's per-address family max (/32 or /128), and the start of the range set to the input prefix's length plus one.  
`p.orLonger()` | Prefix range object that's a copy of _p_ with the end of the range set to the input prefix's per-address family max (/32 or /128).  
`p.lengthRange(20, 30)` | Prefix range object that's a copy of _p_ with the start of the range set to /20, and the end set to /30.  
`p.upTo(30)` | Prefix range object that's a copy of _p_ with the end of the range set to the input prefix's /30.  
  
## Community Set Elements

Elements of community sets must be community strings in human readable `A:B` format.

The following table describes the elements of a community set. 

Expression | Description  
---|---  
`'A:B'` | Community literal.  
  
## What's next

  * [Update named sets](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-named-sets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
