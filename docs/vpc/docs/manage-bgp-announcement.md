---
url: https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement/
title: Manage BGP announcement (v2) \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:54.402008+00:00
---

# Manage BGP announcement (v2)  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage BGP announcement (v2)

When you create v2 public advertised prefixes and v2 public delegated prefixes, they are not automatically announced. You choose when to announce or withdraw the prefixes.

## Specifications

Bring your own IP prefix announcements have the following specifications, depending on the [network tier](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#service-tiers) of your prefix.

  * **For Premium Tier** : 
    * Announcing a public delegated prefix announces that public delegated prefix within Google Cloud.
    * Announcing a public advertised prefix announces the whole public advertised prefix to the internet from all Google points of presence.
    * If you announce a public delegated prefix without announcing the parent public advertised prefix, the public delegated prefix is reachable from within Google Cloud but not from the internet.
  * **For Standard Tier** ([Preview](https://cloud.google.com/products#product-launch-stages)): 
    * Announcing a public delegated prefix announces that public delegated prefix within Google Cloud and also to the internet. The internet announcement is limited to Google points of presence near the prefix's region.
    * Announcing a public advertised prefix announces the whole public advertised prefix to the internet from all Google points of presence. This provides a global backup path for regional public delegated prefix announcements, where traffic can enter Google's network through any Google point of presence, instead of only through those near the prefix's region.
    * If you announce a public delegated prefix without announcing the parent public advertised prefix, the public delegated prefix is reachable from within Google Cloud and from the internet. Internet reachability is limited to Google points of presence that are near the prefix's region.
  * **General** : 
    * You must announce at least one public delegated prefix before you can announce the parent public advertised prefix.
    * You can't withdraw announcement for a public delegated prefix if it is the only public delegated prefix being announced for the parent public advertised prefix. First withdraw the parent public advertised prefix, then withdraw the public delegated prefix.
    * Announce and withdraw requests are rate limited. For more information, see [quotas for bring your own IP](https://docs.cloud.google.com/vpc/docs/quota#byoip).



## Before you begin

  * Verify that your public delegated prefix uses v2.

Run this command to verify which version you are using:
        
        gcloud compute public-delegated-prefixes describe PDP_NAME \
            --region=REGION | grep byoipApiVersion
        




### Announce BGP advertisement for a prefix

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Select the prefix that you want to announce.

  3. Click **Announce**.

A dialog is displayed to confirm announcing the public advertised prefix.

  4. Click **Announce** to confirm.




###  gcloud 

  * To announce a public delegated prefix, use the [`public-delegated-prefixes update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update).
        
        gcloud compute public-delegated-prefixes update PDP_NAME \
            --region=PDP_REGION \
            --announce-prefix
        

Replace the following:

    * `PDP_NAME`: the public delegated prefix that you want to announce.

    * `PDP_REGION`: the region of the public delegated prefix.

  * To announce a public advertised prefix, use the [`public-advertised-prefixes update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update).
        
        gcloud compute public-advertised-prefixes update PAP_NAME \
            --announce-prefix
        

Replace `PAP_NAME` with the name of the public advertised prefix that you want to announce.




### Withdraw advertisement of a prefix

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Select the prefix that you want to withdraw.

  3. Click **Withdraw**.

A dialog is displayed to confirm withdrawing the public advertised prefix.

  4. Click **Withdraw** to confirm.




###  gcloud 

  * To withdraw a public delegated prefix, use the [`public-delegated-prefixes update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/update).
        
        gcloud compute public-delegated-prefixes update PDP_NAME \
            --region=PDP_REGION \
            --withdraw-prefix
        

Replace the following:

    * `PDP_NAME`: the public delegated prefix that you want to withdraw.

    * `PDP_REGION`: the region of the public delegated prefix.

  * To withdraw a public advertised prefix, use the [`public-advertised-prefixes update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-advertised-prefixes/update).
        
        gcloud compute public-advertised-prefixes update PAP_NAME \
            --withdraw-prefix
        

Replace `PAP_NAME` with the name of the public advertised prefix that you want to withdraw.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
