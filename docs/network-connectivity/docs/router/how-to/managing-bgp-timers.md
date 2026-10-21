---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers/
title: Manage BGP timers \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:18.660116+00:00
---

# Manage BGP timers  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage BGP timers

This page describes the following:

  * Cloud Router's BGP timers and their settings, including guidance for configuring the same settings on your on-premises router.
  * Updating the BGP keepalive interval for Cloud Router.



## BGP timers and settings

The Cloud Router and your on-premises router maintain communication by using the following set of timer settings.

### Keepalive timer

BGP systems exchange keepalive messages to determine whether a link or host has failed or is no longer available. In conjunction with the hold timer, the keepalive timer indicates whether a router is reachable to its BGP peer.

The keepalive timer is the `KEEPALIVE_INTERVAL` between periodic BGP messages exchanged between a Cloud Router and its corresponding on-premises peer router. You can configure this value as described in Update the BGP keepalive interval. The default value is 20 seconds. Google recommends setting the keepalive timers to the same value on your on-premises router and the Cloud Router.

### Hold timer

This timer defines the amount of time that a Cloud Router or an on-premises router must wait, absent a graceful restart notification (TCP `FIN` or `RST` packet) or a BGP `CEASE` notification, before moving the BGP session to the `DOWN` state.

Routers negotiate a hold time for each BGP session. The negotiated hold time is the lower of the hold timer values configured on Cloud Router and the on-premises router. When the negotiated hold time is reached, and neither a graceful restart notification nor a BGP `CEASE` notification has been received, a router moves the BGP session to the `DOWN` state and takes the following actions:

  * Removes all learned routes from the BGP session
  * Stops advertising routes



To configure the Cloud Router hold timer, update the Cloud Router BGP keepalive interval. Cloud Router sets the value of the hold timer to three times the value of the configured keepalive interval. For example, if you set the keepalive timer to 20 seconds, the hold timer is 60 seconds. For more information, see Update the BGP keepalive interval.

### Graceful restart timer

This timer defines the amount of time that a router preserves the previous BGP session state following a graceful restart notification (TCP `FIN` or `RST` packet) from the peer router.

While preserving the previous BGP session state, the router keeps the session's learned routes received from the peer router and continues to advertise its routes to the peer router. If a new BGP session is established while the previous BGP session state is being preserved, there's no interruption to connectivity. However, if a new BGP session isn't established, the session transitions to the `DOWN` state at the end of the graceful restart timer. Once in the `DOWN` state, the session's learned routes received from the peer router are removed, and the router stops advertising its routes to the peer router.

A router that supports graceful restart advertises a graceful restart timer value that defines the amount of time that the other router must wait following a graceful restart notification. Two connected routers might use different graceful restart timer values, and each router is expected to honor the graceful restart timer value of its peer. When establishing a new BGP session, each router communicates its own graceful restart timer value to the peer router through the BGP `OPEN` message.

Cloud Router supports graceful restart, and the Cloud Router graceful restart timer is set to 120 seconds. Every Cloud Router sends a graceful restart notification before each [software maintenance](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#maintenance) event if the peer router also supports graceful restart.

If you configured your on-premises router with graceful restart, it can also send a graceful restart notification to the Cloud Router during on-premises router restart or maintenance events. Set your on-premises router's graceful restart timer to a value that is appropriate for your needs.

For more information about graceful restart, see [RFC 4724](https://datatracker.ietf.org/doc/html/rfc4724).

### Stalepath timer

This setting determines how long a router waits before deleting learned routes after it receives an end-of-record (EOR) message from the other router. This timer starts when the BGP session is reinitialized after a graceful restart, but the prefix in question hasn't been addressed by an `UPDATE` message. We recommend setting the stalepath timer to 300 seconds on your on-premises router to match the setting for the Cloud Router.

## Update the BGP keepalive interval

To modify the BGP keepalive interval on a Cloud Router, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Routers** page.

[Go to Cloud Routers](https://console.cloud.google.com/hybrid/routers/list)

  2. Select the Cloud Router that contains the BGP interval to modify.

  3. On the **Router details** page, click edit**Edit**.

  4. Update the **BGP peer keepalive interval**. This value must be an integer between 20 and 60 that specifies the number of seconds for the interval. The default is 20 seconds.

  5. Click **Save**.




###  gcloud 

Run the `update` command:
    
    
    gcloud compute routers update ROUTER_NAME \
        --project=PROJECT_ID \
        --keepalive-interval=KEEPALIVE_INTERVAL \
        --region=REGION
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router
  * `PROJECT_ID`: the project that contains the Cloud Router
  * `KEEPALIVE_INTERVAL`: the interval between BGP keepalive messages that are sent to the peer router

This value must be an integer between 20 and 60 that specifies the number of seconds for the interval. The default is 20 seconds.

  * `REGION`: the region where the Cloud Router is located




The output is similar to the following:
    
    
      Updating router [my-router]...done.
    

###  API 

Use the [`routers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) method to update the `bgp.keepaliveInterval` field:
    
    
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
        {
          "bgp": {
            "keepaliveInterval": KEEPALIVE_INTERVAL
         }
       }
    

Replace the following:

  * `PROJECT_ID`: the project that contains the Cloud Router
  * `REGION`: the region where the Cloud Router is located
  * `ROUTER_NAME`: the name of the Cloud Router
  * `KEEPALIVE_INTERVAL`: the interval between BGP keepalive messages that are sent to the peer router

This value must be an integer between 20 and 60 that specifies the number of seconds for the interval. The default is 20 seconds.




## What's next

  * To disable a BGP session temporarily or remove it entirely, see [Disable or remove BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp).
  * To troubleshoot issues when using Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
