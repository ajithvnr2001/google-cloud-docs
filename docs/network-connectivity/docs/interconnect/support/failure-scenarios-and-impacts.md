---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/failure-scenarios-and-impacts/
title: Failure scenarios and impacts \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:42.157816+00:00
---

# Failure scenarios and impacts  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/failure-scenarios-and-impacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Failure scenarios and impacts Stay organized with collections  Save and categorize content based on your preferences. 

The following table describes potential failure scenarios that can occur on Cloud Interconnect and how they can affect you. The failure scenarios described assume that you follow [Best practices for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).

Failure type and description | Worst case scenario | Best case scenario  
---|---|---  
**Link failure** A physical link failure between the Google edge router and your on-premises router. |  You experience a minor service interruption with an estimated duration of several minutes.  |  Traffic is disrupted for several seconds with alternate paths available for traffic.   
**Google edge router failure** A device failure that affects the connection between Cloud Router and your on-premises router. |  You experience a minor service interruption with an estimated duration of several minutes.  |  Traffic is disrupted for several seconds with alternate paths available for traffic.   
**Cloud Router failure** Typically a Cloud Router maintenance event that usually takes less than 60 seconds.  |  No impact expected with graceful restart enabled.  |  No impact expected with graceful restart enabled. For more information about graceful restart, see [ Graceful restart and BFD](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd#graceful-restart-and-bfd)  
**On-premises router control plane failure** Your on-premises router experiences a control plane failure.  |  A brief service interruption with an estimated duration of several minutes.  |  A short pause in service.   
  
## Next steps

  * Implement Cloud Interconnect [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
