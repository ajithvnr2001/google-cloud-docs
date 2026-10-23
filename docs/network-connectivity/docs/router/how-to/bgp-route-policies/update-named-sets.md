---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-named-sets/
title: Manage named sets \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:21.619407+00:00
---

# Manage named sets  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-named-sets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage named sets

This guide describes how to do the following updates to named sets for Cloud Router BGP route policies:

  * List named sets
  * Remove named sets
  * Update named sets
  * Add named set elements
  * Remove named set elements



## List named sets on a router

Use the [`list-named-sets`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/list-named-sets) command to view the names and types of named sets defined on a single router.
    
    
    gcloud compute routers list-named-sets ROUTER_NAME
    

Replace ROUTER_NAME with the name of your Cloud Router.

## Remove a named set

If a named set is referenced in any BGP route policies on the router, you can't remove the named set.
    
    
    gcloud compute routers remove-named-set ROUTER_NAME
        --set-name=SET_NAME
    

Replace the following:

  * ROUTER_NAME: The name of your Cloud Router
  * SET_NAME: The name of the named set that you want to remove



## Update a named set on a router

When updating an existing named set, we recommend that you download the named set from the router in either YAML or JSON format by using the [`download-named-set`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/download-named-set) command. Edit the YAML or JSON file locally, and then upload the updated file to the router by using the [`upload-named-set`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/upload-named-set) command. The `upload-named-set` command overwrites the existing named set.

The file that you download from the router includes the `fingerprint` field, which Cloud Router uses to match the existing named set and prevent conflicting updates.

  1. To download the named set, run the `download-named-set` command: 
         
         gcloud compute routers download-named-set ROUTER_NAME
             --set-name=SET_NAME
             --file-name=FILE_NAME
             --file-format=FORMAT
         

Replace the following:

     * ROUTER_NAME with the name of the Cloud Router.
     * SET_NAME with the name of the set.
     * FILE_NAME with the filename you want for the named set, including the path and filename extension.
     * FORMAT with the format of the named set, either JSON or YAML.
  2. Modify the downloaded named set in your preferred text editor using either JSON or YAML formatting.

The following examples use two YAML files to update named sets named `allowed-prefixes` and `allowed-communities`.

**allowed-prefixes.yaml:**
         
         # Prefix set
         resource:
           elements:
           - expression: "'192.168.1.0/24'"
           - expression: "'fd00::/8'"
           - expression: "prefix('10.0.0.0/20').orLonger()"
           name: allowed-prefixes
           type: NAMED_SET_TYPE_PREFIX
         

**allowed-communities.yaml:**
         
         # Community set
         resource:
           elements:
           - expression: "'64500:100'"
           - expression: "'64500:300'"
           name: allowed-communities
           type: NAMED_SET_TYPE_COMMUNITY
         

  3. To upload the named set, run the `upload-named-set` command: 
         
         gcloud compute routers upload-named-set ROUTER_NAME
             --set-name=SET
             --file-name=NAME
             --file-format=FORMAT
         

Replace the following:

     * ROUTER_NAME with the name of the Cloud Router.
     * SET with the name of the set.
     * NAME with the location and filename of the YAML or JSON file you edited.
     * FORMAT with the format of the named set, either JSON or YAML.



## Add a named set element

Run the following command:
    
    
    gcloud compute routers add-named-set-element ROUTER_NAME
        --set-name=SET_NAME
        --new-set-element=CEL_EXPRESSION
    

Replace the following:

  * ROUTER_NAME: The name of your Cloud Router
  * SET_NAME: The name of the named set that you want to update
  * CEL_EXPRESSION: An element to add to the set, expressed in Common Expression Language (CEL)



## Remove a named set element

Run the following command:
    
    
    gcloud compute routers remove-named-set-element ROUTER_NAME
        --set-name=SET_NAME
        --set-element=CEL_EXPRESSION
    

Replace the following:

  * ROUTER_NAME: The name of your Cloud Router
  * SET_NAME: The name of the named set that you want to update
  * CEL_EXPRESSION: An element to remove from the set, expressed in Common Expression Language (CEL)



## What's next

  * [Create BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-policies)
  * [Update BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
