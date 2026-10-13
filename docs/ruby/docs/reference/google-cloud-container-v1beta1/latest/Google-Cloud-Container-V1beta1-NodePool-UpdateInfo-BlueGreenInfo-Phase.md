---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodePool-UpdateInfo-BlueGreenInfo-Phase/
title: Kubernetes Engine V1beta1 API - Module Google::Cloud::Container::V1beta1::NodePool::UpdateInfo::BlueGreenInfo::Phase (v0.57.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:12:37.762332+00:00
---

# Kubernetes Engine V1beta1 API - Module Google::Cloud::Container::V1beta1::NodePool::UpdateInfo::BlueGreenInfo::Phase (v0.57.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1beta1/latest/Google-Cloud-Container-V1beta1-NodePool-UpdateInfo-BlueGreenInfo-Phase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1beta1 API - Module Google::Cloud::Container::V1beta1::NodePool::UpdateInfo::BlueGreenInfo::Phase (v0.57.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.57.1 (latest)  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.1  0.50.0  0.49.1  0.48.0  0.47.0  0.46.0  0.45.1  0.44.0  0.43.0  0.42.1  0.41.0  0.40.1  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.3  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.3 

Reference documentation and code samples for the Kubernetes Engine V1beta1 API module Google::Cloud::Container::V1beta1::NodePool::UpdateInfo::BlueGreenInfo::Phase.

Phase represents the different stages blue-green upgrade is running in.

## Constants 

### PHASE_UNSPECIFIED

**value:** 0  
Unspecified phase.

### UPDATE_STARTED

**value:** 1  
blue-green upgrade has been initiated.

### CREATING_GREEN_POOL

**value:** 2  
Start creating green pool nodes.

### CORDONING_BLUE_POOL

**value:** 3  
Start cordoning blue pool nodes.

### WAITING_TO_DRAIN_BLUE_POOL

**value:** 8  
Start waiting after cordoning the blue pool and before draining it.

### DRAINING_BLUE_POOL

**value:** 4  
Start draining blue pool nodes.

### NODE_POOL_SOAKING

**value:** 5  
Start soaking time after draining entire blue pool.

### DELETING_BLUE_POOL

**value:** 6  
Start deleting blue nodes.

### ROLLBACK_STARTED

**value:** 7  
Rollback has been initiated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
