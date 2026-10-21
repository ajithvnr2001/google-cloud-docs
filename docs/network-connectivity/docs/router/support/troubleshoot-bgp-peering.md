---
url: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering/
title: Troubleshoot BGP peering \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:02:08.668719+00:00
---

# Troubleshoot BGP peering  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot BGP peering

This guide is for troubleshooting peering issues, such as MD5 authentication or on-premises routes without MED values having priority.

For additional troubleshooting information, see the following:

  * [Troubleshoot BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-sessions)
  * [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes)
  * [Troubleshoot Cloud Router log messages](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-log-messages)



## BGP peer status is `MD5_AUTH_INTERNAL_PROBLEM`

Sometimes the status of a BGP peer includes the following values:

  * `md5AuthEnabled`: `true`
  * `statusReason`: `MD5_AUTH_INTERNAL_PROBLEM`



The first value indicates that you have successfully configured MD5 authentication. However, the second value—a `statusReason` value of `MD5_AUTH_INTERNAL_PROBLEM`—indicates that an internal error has prevented Cloud Router from being able to configure MD5 authentication. For that reason, the BGP session status is `DOWN`. In this case, you don't need to do anything. Cloud Router tries to recover and bring the session back up. If the session is taking more than one hour to back up, contact [Google Cloud Support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

For information about how to check the peer's status, see [Check authentication status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#check-status).

## Cloud Router and peer use different MD5 keys

When you set up MD5 authentication, the Cloud Router and its peer router must use the same secret authentication key. If a mismatch occurs, the two routers cannot communicate. If you think that there's been a mismatch, one solution is to update the key that is used by the Cloud Router. For information about how to make this change, see [Update the authentication key](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#update-key).

If you're not sure whether there's been a key mismatch, look for troubleshooting solutions in your peer router's documentation. Many routers have logs that record whether or not there's been a key mismatch.

## Auto generated MD5 key is longer than on-premises device can support

You can auto generate the MD5 key by clicking **Generate and Copy** in the UI console. For more information, see [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication). If the auto generated MD5 key is longer than your on-premises can support, you can configure MD5 key manually through UI or Google Cloud CLI or API.

## On-premises routes without a MED value are taking priority

If the Cloud Router receives an on-premises route that doesn't have a MED value, the Cloud Router follows the behavior described in [RFC 4271](https://datatracker.ietf.org/doc/html/rfc4271). The Cloud Router treats the route with the highest priority by assuming the lowest possible MED value (`0`).

## What's next

  * For more information about how to use Cloud Logging to monitor Cloud Router, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

  * For additional support, see [Getting support](https://docs.cloud.google.com/network-connectivity/docs/router/support/getting-support).

  * For information about BGP session states, see [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).

  * For information about diagnostic messages and session states related to Bidirectional Forwarding Detection (BFD), see [BFD diagnostic messages and session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd-states).

  * For issues related to using Cloud Router with Router appliance, see [Troubleshooting Router appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra) in the Network Connectivity Center documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
