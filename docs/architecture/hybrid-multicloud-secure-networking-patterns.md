---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/
title: Hybrid and multicloud secure networking architecture patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:24.859460+00:00
---

# Hybrid and multicloud secure networking architecture patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Hybrid and multicloud secure networking architecture patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-29 UTC

This document is the third of three documents in a set. It discusses hybrid and multicloud networking architecture patterns. This part explores several common secure network architecture patterns that you can use for hybrid and multicloud architectures. It describes the scenarios that these networking patterns are best suited for, and provides best practices for implementing them with Google Cloud.

The document set for hybrid and multicloud architecture patterns consists of these parts:

  * [Build hybrid and multicloud architectures](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns): discusses planning a strategy for architecting a hybrid and multicloud setup with Google Cloud.
  * [Hybrid and multicloud architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices): discusses common architecture patterns to adopt as part of a hybrid and multicloud strategy.
  * Hybrid and multicloud secure networking architecture patterns: discusses hybrid and multicloud networking architecture patterns from a networking perspective (this document).



Connecting private computing environments to Google Cloud securely and reliably is essential for any successful hybrid and multicloud architecture. The hybrid networking connectivity and cloud networking architecture pattern you choose for a hybrid and multicloud setup must meet the unique requirements of your enterprise workloads. It must also suit the architecture patterns you intend to apply. Although you might need to tailor each design, there are common patterns you can use as a blueprint.

The networking architecture patterns in this document shouldn't be considered alternatives to the [landing zone design in Google Cloud](https://docs.cloud.google.com/architecture/landing-zones). Instead, you should design and deploy the architecture patterns you select as part of the overall Google Cloud landing zone design, which spans the following areas:

  * Identities
  * Resource management
  * Security
  * Networking
  * Monitoring



Different applications can use different networking architecture patterns, which are incorporated as part of a landing zone architecture. In a multicloud setup, you should maintain the consistency of the landing zone design across all environments.

This series contains the following pages:

  * [Design considerations](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations)
  * [Architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/architecture-patterns)
    * [Mirrored pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern)
    * [Meshed pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/meshed-pattern)
    * [Gated patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-patterns)
      * [Gated egress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress)
      * [Gated ingress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress)
      * [Gated egress and ingress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress)
    * [Handover](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern)
  * [General best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices)



## Contributors

Author: [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer

Other contributors: 

  * [Saud Albazei](https://www.linkedin.com/in/albazei) | Customer Engineer, Application Modernization
  * [Anna Berenberg](https://www.linkedin.com/in/annaberenberg) | Engineering Fellow
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Johannes Passing](https://www.linkedin.com/in/johannespassing) | Cloud Solutions Architect
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Daniel Strebel](https://www.linkedin.com/in/danistrebel) | EMEA Solution Lead, Application Modernization
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer



[ Next Design considerations  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/design-considerations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-29 UTC."],[],[]] 
