---
url: https://docs.cloud.google.com/load-balancing/docs/switch-between-target-instance-and-backend-service/
title: Switch between a target instance and a backend service \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:00.007039+00:00
---

# Switch between a target instance and a backend service  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/switch-between-target-instance-and-backend-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Switch between a target instance and a backend service Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to switch the target of a forwarding rule between a target instance and a backend service.

## External protocol forwarding

To switch an external forwarding rule's target from a target instance to a backend service (or the other way around), you need to delete and re-create the forwarding rule with the new target. This method requires a static IP address so that you can use the same address with the new forwarding rule.

Deleting and re-creating the forwarding rule is the only way to switch between external protocol forwarding and a backend service-based regional external passthrough Network Load Balancer.

## Internal protocol forwarding

There are two ways to switch between internal protocol forwarding and an internal passthrough Network Load Balancer:

  * You can switch between a target instance and a backend service by updating the forwarding rule with the `gcloud compute forwarding-rules set-target` command as described in Change the target of an internal forwarding rule. When switching between internal protocol forwarding and an internal passthrough Network Load Balancer, you don't need to delete and re-create the forwarding rule. The forwarding rule continues to use the same internal IP address (whether static or ephemeral).

  * You can also switch between a target instance and a backend service by deleting and re-creating the forwarding rule. However, this method requires a static IPv4 address in order to use the same address with the new forwarding rule. You can't use this method for IPv6 addresses because reserving an IPv6 address is not supported.




A target instance does not specify any protocol—it inherits the protocols and ports of the forwarding rule. Therefore, when switching a forwarding rule to reference a backend service, you must ensure that the IP protocol of the forwarding rule (either TCP or UDP) matches the protocol of the backend service (either TCP or UDP).

The following diagram shows an example that uses internal protocol forwarding.

[ ![Switch between a target instance and a backend service.](https://docs.cloud.google.com/static/load-balancing/images/pf-int-switch-target.svg)](https://docs.cloud.google.com/static/load-balancing/images/pf-int-switch-target.svg) Switch between a target instance and a backend service.

### Change the target of an internal forwarding rule

To change a forwarding rule from pointing to a target instance to pointing to a regional backend service, use the following command:
    
    
    gcloud compute forwarding-rules set-target FORWARDING_RULE \
        --backend-service=BACKEND_SERVICE \
        --region=REGION
    

To transition back to a target instance, use the following command:
    
    
    gcloud compute forwarding-rules set-target FORWARDING_RULE \
        --target-instance=TARGET_INSTANCE \
        --target-instance-zone=ZONE
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
