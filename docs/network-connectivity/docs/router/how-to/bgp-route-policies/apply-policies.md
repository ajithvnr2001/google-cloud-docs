---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/apply-policies/
title: Apply BGP route policies \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:04.857329+00:00
---

# Apply BGP route policies  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/apply-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Apply BGP route policies

This guide describes how to apply BGP route policies in Cloud Router.

## Create a BGP peer with policies applied

When creating a new BGP peer with import or export policies already applied, the route policies must already exist. The BGP peer autonomous system number (ASN) must be a 16-bit or 32-bit private ASN. See [RFC 6996](https://tools.ietf.org/html/rfc6996).

Create a new BGP peer with BGP route policies applied:
    
    
    gcloud compute routers add-bgp-peer ROUTER_NAME \
        --interface=INTERFACE \
        --peer-name=PEER_NAME \
        --peer-asn=PEER_ASN \
        --import-policies=IMPORT_POLICIES \
        --export-policies=EXPORT_POLICIES
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router to add the new BGP peer to
  * `INTERFACE`: the name of the interface for the new BGP peer
  * `PEER_NAME`: the name for the new BGP peer to apply the policies to
  * `PEER_ASN`: the BGP ASN for the new BGP peer
  * `IMPORT_POLICIES`: a comma-separated list of import policies to apply to the new BGP peer
  * `EXPORT_POLICIES`: a comma-separated list of export policies to apply to the new BGP peer



## Update a BGP route policy applied to an existing BGP peer

When you update BGP route policies applied to a BGP peer, the policies replace existing BGP policies. Each policy type is updated independently.

For example, assume you have a BGP peer with the `my-import-policy` and `my-export-policy` route policies applied.
    
    
    gcloud compute routers update-bgp-peer Router --peer-name=Name \
    
        --import-policies= \
        --export-policies=my-export-policy1,my-export-policy2
    

This command removes all existing import policies for the listed BGP peer, and replaces the existing export policy for the peer with `my-export-policy1,my-export-policy2`.

Any peer, import policies, or export policies must already exist.

Add a BGP route policy to an existing BGP peer:
    
    
    gcloud compute routers update-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME \
        --import-policies=IMPORT_POLICIES \
        --export-policies=EXPORT_POLICIES
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `PEER_NAME`: the name of the BGP peer that the policies apply to
  * `IMPORT_POLICIES`: a comma-separated list of import policies to apply to the BGP peer
  * `EXPORT_POLICIES`: a comma-separated list of export policies to apply to the BGP peer



## Download a BGP route policy

Download a YAML file of the BGP route policy to your computer:
    
    
    gcloud compute routers download-route-policy ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --file-name=FILE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `BGP_ROUTE_POLICY_NAME`: the name of the BGP route policy that you want to export
  * `FILE_NAME`: the name of the file to download the route policy to



You can also export the BGP route policy to a JSON file:
    
    
    gcloud compute routers download-route-policy ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --file-name=FILE_NAME \
        --format=json
    

## Display a BGP route policy

View a YAML representation of a BGP route policy:
    
    
    gcloud compute routers get-route-policy ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of your Cloud Router
  * `BGP_ROUTE_POLICY_NAME`: the name of the BGP route policy that you want to export



View a JSON representation of a BGP route policy:
    
    
    gcloud compute routers get-route-policy ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --format=json
    

## What's next

  * [Create BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-policies)
  * To learn more about Router Google Cloud CLI commands, see [gcloud compute routers](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers) in the Google Cloud SDK documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
