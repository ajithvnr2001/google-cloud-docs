---
url: https://docs.cloud.google.com/load-balancing/docs/srl-policy/set-up-srl-policy-reg-int-app-lb/
title: Set up service rate limiting policies \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:19:45.163729+00:00
---

# Set up service rate limiting policies  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/srl-policy/set-up-srl-policy-reg-int-app-lb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up service rate limiting policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to set up service rate limiting policies for regional internal Application Load Balancers.

## Before you begin

  * Familiarize yourself with the [Service rate limiting overview](https://docs.cloud.google.com/load-balancing/docs/srl-policy/service-rate-limiting-overview).
  * [Enable the following APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#enabling_an_api):

    * Network Security API (`networksecurity.googleapis.com`)
    * Network Services API (`networkservices.googleapis.com`)

To enable the APIs, run the following command:
    
    gcloud services enable \
        networksecurity.googleapis.com \
        networkservices.googleapis.com
    

  * If you haven't already configured a regional internal Application Load Balancer, see the [Set up a regional internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal) page and create one.




## Create a service rate limiting policy

To create a service rate limiting policy, create a YAML file that defines the target and the rules, and then import the file using the `gcloud network-security service-rate-limit-policies` command. The following sections provide examples of service rate limiting policies.

### Apply rate limiting based on custom groups

The following example uses a custom tag from the HTTP header, `x-custom-group-tag`, to identify two groups: `group1` and `group2`. It limits requests per minute (RPM) to 10,000 for `group1` and 20,000 for `group2`.

###  gcloud 

  1. Create the `custom-groups-policy.yaml` file and specify the policy parameters.
         
         $ cat >custom-groups-policy.yaml <<EOF
         name: projects/PROJECT_ID/locations/LOCATION/rateLimitPolicies/custom-groups-policy
         description: Rate limit each API key based on custom tags.
         httpRules:
         # Match on traffic on the custom tag header.
         - to:
             destination:
               headerSet:
                 headers:
                 - name: "x-custom-group-tag"
                   value:
                     exact: "group1"
         
             rateLimitActions:
               - rateLimitBucket: rl_group1_rpm_limit
         
         - to:
             destination:
               headerSet:
                 headers:
                 - name: "x-custom-group-tag"
                   value:
                     exact: "group2"
         
             rateLimitActions:
               - rateLimitBucket: rl_group2_rpm_limit
         
         rateLimitBuckets:
         - name: rl_group1_rpm_limit
           # Set threshold for ALL the traffic matching this bucket.
           keys:
           - keyType: ALL
         
           defaultLimit:
             countLimit:
               count: 10000
               interval: 1
               intervalUnit: MINUTES
         
         - name: rl_group2_rpm_limit
           # Set threshold for ALL the traffic matching this bucket.
           keys:
           - keyType: ALL
         
           defaultLimit:
             countLimit:
               count: 20000
               interval: 1
               intervalUnit: MINUTES
         
         targets:
         - resource: projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_NAME
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.
     * `FORWARDING_RULE_NAME`: the name of your forwarding rule.
  2. Create the service rate limiting policy by importing the YAML file that you created in the previous step:
         
         gcloud network-security service-rate-limit-policies import custom-groups-policy \
          --source=custom-groups-policy.yaml \
          --location=LOCATION \
          --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.



### Apply rate limiting to all clients

The following example limits requests per minute to 10,000 for all clients.

###  gcloud 

  1. Create the `all-clients-policy.yaml` file and specify the policy parameters.
         
         $ cat >all-clients-policy.yaml <<EOF
         name: projects/PROJECT_ID/locations/LOCATION/rateLimitPolicies/all-clients-policy
         description: Service rate limiting example.
         httpRules:
           # Match on all traffic.
         
           # Service rate limiting bucket
         - rateLimitActions:
           - rateLimitBucket: rl_default_rpm_limit
         
         rateLimitBuckets:
         - name: "rl_default_rpm_limit"
           # Match on 'ALL' requests for this bucket.
           keys:
           - keyType: ALL
         
           defaultLimit:
             countLimit:
               count: 10000
               interval: 1
               intervalUnit: MINUTES
         
         targets:
         - resource: projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_NAME
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.
     * `FORWARDING_RULE_NAME`: the name of your forwarding rule.
  2. Create the service rate limiting policy by importing the YAML file that you created in the previous step:
         
         gcloud network-security service-rate-limit-policies import all-clients-policy \
          --source=all-clients-policy.yaml \
          --location=LOCATION \
          --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.



### Apply rate limiting based on host and API key

The following example rate limits the APIs that are destined for the host `example.com` to 1000 requests per 5 minutes for each unique value of the API key that's fetched from the `x-api-key` HTTP Header. A special API key `abc123` instead has an increased limit of 10,000 requests per 5 minutes.

###  gcloud 

  1. Create the `host-and-api-key-policy.yaml` file and specify the policy parameters.
         
         $ cat >host-and-api-key-policy.yaml <<EOF
         name: projects/PROJECT_ID/locations/LOCATION/rateLimitPolicies/host-and-api-key-policy
         description: Rate limit each api key.
         httpRules:
           # Match on traffic to example.com
         - to:
             destination:
               hosts:
               - exact: "example.com"
         
           rateLimitActions:
             - rateLimitBucket: rl_default_rpm_limit
         
         rateLimitBuckets:
         - name: rl_default_rpm_limit
           # Identify API key from its header, say 'x-api-key'.
           keys:
           - header: "x-api-key"
             keyType: HTTP_HEADER
         
           defaultLimit:
             countLimit:
               count: 1000
               interval: 5
               intervalUnit: MINUTES
         
           # Override the threshold for specific API key 'abc123'.
           userOverrides:
           - overrideKey:
               httpHeaders:
               - header: "x-api-key"
                 value: "abc123"
             limit:
               countLimit:
                 count: 10000
                 interval: 5
                 intervalUnit: MINUTES
         
         targets:
         - resource: projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_NAME
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.
     * `FORWARDING_RULE_NAME`: the name of your forwarding rule.
  2. Create the service rate limiting policy by importing the YAML file that you created in the previous step:
         
         gcloud network-security service-rate-limit-policies import host-and-api-key-policy \
          --source=host-and-api-key-policy.yaml \
          --location=LOCATION \
          --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.



### Apply rate limiting based on URL path and client name

The following example limits the APIs hosted on the `/public` path for each client, identified by its Client Certificate Common Name, to 100 requests per minute.

###  gcloud 

  1. Create the `path-and-client-name-policy.yaml` file and specify the policy parameters.
         
         $ cat >path-and-client-name-policy.yaml <<EOF
         name: projects/PROJECT_ID/locations/LOCATION/rateLimitPolicies/path-and-client-name-policy
         description: Simple API rate limiting example.
         httpRules:
           # Match on traffic to /public .
         - to:
             destination:
               paths:
               - exact: "/public"
         
           # Default RPM bucket
           rateLimitActions:
           - rateLimitBucket: rl_default_rpm_limit
         
         rateLimitBuckets:
         - name: "rl_default_rpm_limit"
           # Identify client by its client cert name
           keys:
           - keyType: PRINCIPAL
             principalType: CLIENT_CERT_COMMON_NAME
           defaultLimit:
             countLimit:
               count: 100
               interval: 1
               intervalUnit: MINUTES
         
         targets:
         - resource: projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_NAME
         
         EOF
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.
     * `FORWARDING_RULE_NAME`: the name of your forwarding rule.
  2. Create the service rate limiting policy by importing the YAML file that you created in the previous step:
         
         gcloud network-security service-rate-limit-policies import path-and-client-name-policy \
          --source=path-and-client-name-policy.yaml \
          --location=LOCATION \
          --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION`: the location of your forwarding rule.



## What's next

  * [Understand service rate limiting policy logs](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#srl_info)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
