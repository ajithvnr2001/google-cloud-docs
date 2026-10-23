---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/list-policies/
title: List BGP route policies \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:28.848906+00:00
---

# List BGP route policies  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/list-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# List BGP route policies

This page describes how to list _Border Gateway Protocol (BGP)_ route policies on Cloud Router, which can help you troubleshoot your BGP route policies.

## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## List BGP route policies

###  Console 

  1. In the Google Cloud console, go to the **Cloud Router** page.

[Go to Cloud Router](https://console.cloud.google.com/hybrid/routers/list)

  2. On the **Cloud Router** page, click the **BGP Route Policies** tab.

  3. To view the BGP route policy terms for a BGP route policy, click the BGP route policy name.




###  gcloud 

Use the [`gcloud compute routers list-route-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list-route-policies):
    
    
    gcloud compute routers list-route-policies ROUTER_NAME \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router

  * `REGION`: the region in which your Cloud Router is located




The output is similar to the following:
    
    
    NAME: test-policy-1
    TYPE: ROUTE_POLICY_TYPE_EXPORT
    
    NAME: test-policy-2
    TYPE: ROUTE_POLICY_TYPE_IMPORT
    

###  API 

Use the [`routers.listRoutePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/listRoutePolicies):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME/listRoutePolicies
    

Replace the following:

  * `PROJECT_ID`: the project that contains your Cloud Router

  * `REGION`: the region in which your Cloud Router is located

  * `ROUTER_NAME`: the name of your Cloud Router




The output is similar to the following:
    
    
    {
      "kind": "compute#routersListRoutePolicies",
      "result": [
        {
          "name": "ROUTER_NAME",
          "type": "ROUTE_POLICY_TYPE_IMPORT",
          "terms": [
            {
              "priority": 1,
              "match": {
                "expression": "destination != \"192.168.10.0/24\" && communities.matchesEvery([\"65000:1\", \"65000:2\"])"
              },
              "actions": [
                {
                  "expression": "med.set(12345)"
                }
              ]
            },
            {
              "priority": 2,
              "match": {
                "expression": "destination != \"192.168.10.0/24\""
              },
              "actions": [
                {
                  "expression": "med.set(12345)"
                }
              ]
            }
          ],
          "fingerprint": "ulgdg-dGCms="
        }
      ]
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
