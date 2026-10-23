---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-policies/
title: Create BGP route policies \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:30.144482+00:00
---

# Create BGP route policies  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/create-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create BGP route policies

This guide describes how to create BGP route policies in Cloud Router.

You can create BGP route policies for Cloud Router using any of the following:

  * Use the Google Cloud CLI to build a BGP route policy.
  * Use your preferred text editor to create a BGP route policy, and then use the gcloud CLI to upload the BGP route policy.



## Build a BGP route policy

  1. Add a route policy to your Cloud Router:
         
         gcloud compute routers add-route-policy ROUTER_NAME \
             --policy-name=BGP_ROUTE_POLICY_NAME \
             --policy-type=ROUTE_POLICY_TYPE \
             --region=REGION
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `BGP_ROUTE_POLICY_NAME`: a name for the BGP route policy
     * `ROUTE_POLICY_TYPE`: the type of policy to add, either `IMPORT` for learned routes, or `EXPORT` for advertised routes.
     * `REGION`: the region that the Cloud Router is located in

For example, the following command adds a route policy for learned routes to your Cloud Router:
    
    gcloud compute routers add-route-policy ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --policy-type=IMPORT \
        --region=REGION
    

  2. Add a BGP route policy term by running the following command:
         
         gcloud compute routers add-route-policy-term ROUTER_NAME \
             --policy-name=BGP_ROUTE_POLICY_NAME \
             --region=REGION \
             --priority=ROUTE_POLICY_PRIORITY \
             --match=ROUTE_POLICY_MATCH_EXPRESSION \
             --actions=ROUTE_POLICY_ACTIONS_EXPRESSION
         

Replace the following:

     * `ROUTE_POLICY_PRIORITY`: the priority for this policy, such as `1`.
     * `ROUTE_POLICY_MATCH_EXPRESSION`: an expression to match for this route policy
     * `ROUTE_POLICY_ACTIONS_EXPRESSION`: actions for this route policy

For example, the following command creates a BGP policy to set the BGP multiple exit discriminator (MED) attribute value to `12345` for BGP routes that are included in the named set `allowed-prefixes`.
    
    gcloud compute routers add-route-policy-term ROUTER_NAME \
        --policy-name=BGP_ROUTE_POLICY_NAME \
        --region=REGION \
        --priority=ROUTE_POLICY_PRIORITY \
        --match='destination.inAnyRange(prefixSets("allowed-prefixes"))' \
        --actions='med.set(12345)'
    

Replace `ROUTE_POLICY_PRIORITY` with the priority you want for this policy, such as `1`.




## Upload a BGP route policy

  1. Create the BGP route policy in your preferred text editor. You can use JSON or YAML formatting to create your BGP route policy. The following example uses a YAML file:
         
         name: BGP_ROUTE_POLICY_NAME
         type: ROUTE_POLICY_TYPE 
         terms:
         - priority: ROUTE_POLICY_PRIORITY
           match:
             expression: >
               ROUTE_POLICY_MATCH_EXPRESSION
           actions:
           - expression: ROUTE_POLICY_ACTIONS_EXPRESSION
         

Replace the following:

     * `BGP_ROUTE_POLICY_NAME`: a name for the BGP route policy.
     * `ROUTE_POLICY_TYPE`: the type of BGP route policy you're creating. The type can be one of the following:

       * `ROUTE_POLICY_TYPE_IMPORT`: BGP route policies for learned routes.
       * `ROUTE_POLICY_TYPE_EXPORT`: BGP route policies for advertised routes.
     * `ROUTE_POLICY_PRIORITY`: the priority for this policy, such as `1`.

     * `ROUTE_POLICY_MATCH_EXPRESSION`: an expression to match for this route policy

     * `ROUTE_POLICY_ACTIONS_EXPRESSION`: actions for this route policy

For example, the following YAML file command creates a BGP policy for learned routes that sets the BGP multiple exit discriminator (MED) attribute value to `12345` for BGP routes that aren't included in `192.168.10.0/24` and that match the set of BGP communities `65000:1` and `65000:2`.
    
    # Set the MED value for BGP routes that aren't 192.168.10.0/24 and
    # communities that include (65000:1, 65000:2)
    name: BGP_ROUTE_POLICY_NAME
    type: ROUTE_POLICY_TYPE_IMPORT
    terms:
    - priority: 1
      match:
        expression: >
          destination != '192.168.10.0/24' && communities.matchesEvery(['65000:1', '65000:2'])
      actions:
      - expression: med.set(12345)
    

  2. Upload the BGP route policy:
         
         gcloud compute routers upload-route-policy ROUTER_NAME \
             --region=REGION \
             --policy-name=BGP_ROUTE_POLICY_NAME \
             --file-name=FILE_NAME \
             --file-format=yaml
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router
     * `REGION`: the region the Cloud Router is in
     * `FILENAME`: the filename that you're uploading
  3. Apply the BGP route policies to BGP peers:
         
         gcloud compute routers update-bgp-peer ROUTER_NAME \
             --region=REGION \
             --peer-name=PEER_NAME \
             --import-policies='IMPORT_POLICIES'
         

Replace the following:

     * `PEER_NAME`: the BGP peer's name to apply the BGP route policy to.
     * `IMPORT_POLICIES`: a comma-separated list of import policies. Passing an empty string removes all import policies.



## What's next

  * [Update BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/update-policies)
  * [Apply BGP route policies](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/bgp-route-policies/apply-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
