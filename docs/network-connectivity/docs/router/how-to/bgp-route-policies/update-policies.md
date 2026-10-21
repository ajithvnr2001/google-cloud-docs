---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-policies/
title: Update BGP route policies \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:20.865362+00:00
---

# Update BGP route policies  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update BGP route policies

This guide describes how to do the following updates to BGP route policies for Cloud Router:

  * Remove a BGP route policy
  * Add BGP route policy terms
  * Update BGP route policy terms
  * Remove BGP route policy terms



## Remove a BGP route policy

Run the following:
    
    
    gcloud compute routers remove-route-policy ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `BGP_ROUTE_POLICY_NAME`: the name of the BGP route policy that you want to remove



## Add a BGP route policy term

Run the following:
    
    
    gcloud compute routers add-route-policy-term ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --priority=PRIORITY \
        --match="CEL_MATCH_EXPRESSION" \
        --actions="CEL_ACTIONS_EXPRESSION"
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `BGP_ROUTE_POLICY_NAME`: the name of the BGP route policy that you want to export
  * `PRIORITY`: the order of this term within the BGP route policy, where lower values indicate higher priority. The accepted range is [0, 2^31).
  * `CEL_MATCH_EXPRESSION`: a Common Expression Language (CEL) element that matches routes that this term applies to
  * `CEL_ACTIONS_EXPRESSION`: a semicolon separated CEL expression for actions to take for items that match this rule
  * `REGION`: the region that the Cloud Router is located in



## Update a BGP route policy term

Run the following:
    
    
    gcloud compute routers update-route-policy-term ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --priority=PRIORITY \
        --match="CEL_MATCH_EXPRESSION" \
        --actions="CEL_ACTIONS_EXPRESSION" \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `BGP_ROUTE_POLICY_NAME`: the name of the BGP route policy that you want to export
  * `PRIORITY`: The order of this term within the BGP route policy, where lower values indicate higher priority. The accepted range is [0, 2^31).
  * `CEL_MATCH_EXPRESSION`: a CEL element that matches routes that this term applies to
  * `CEL_ACTIONS_EXPRESSION`: a semicolon separated CEL expression for actions to take for items that match this rule
  * `REGION`: the region that the Cloud Router is located in



## Remove a BGP route policy term

Run the following:
    
    
    gcloud compute routers remove-route-policy-term ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --priority=PRIORITY
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `BGP_ROUTE_POLICY_NAME`: the name of the BGP route policy that you want to export
  * `PRIORITY`: the order of this term within the BGP route policy, where lower values indicate higher priority. The accepted range is [0, 2^31).
  * `REGION`: the region that the Cloud Router is located in



## Add and update named sets

You can add [named sets](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-named-sets)—named groups of literal values of either prefix or community types—and [add](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-named-sets#add-named-set-element) or [remove](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-named-sets#remove-named-set-element) individual named set elements.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
