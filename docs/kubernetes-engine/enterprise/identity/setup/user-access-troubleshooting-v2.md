---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting-v2/
title: Troubleshoot user login issues \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:42.764290+00:00
---

# Troubleshoot user login issues  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Troubleshoot user login issues Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting guidance for FQDN user login issues from third-party identity providers to fleet member clusters.

## Client can't reach the authentication service

This issue occurs in one of the following cases:

  * You're using a version that doesn't support this user login method.
  * The control plane VIP doesn't route the traffic to the correct component.



### Error message
    
    
      Error: could not start login. Please check if cluster supports server side authentication. Details: failed to ping well-known endpoint: Get "https://cluster-url:XXXXX/.well-known/configuration": dial tcp XXX:XXXXX: connect: connection refused
       ERROR: Configuring Anthos authentication failed
      

### Solution

To resolve this issue, verify that you're using a version of 1.28 or higher and the version of the control plane that supports authentication using FQDN access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
