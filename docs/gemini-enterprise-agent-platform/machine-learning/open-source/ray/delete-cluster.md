---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray/delete-cluster/
title: Delete the Ray cluster on Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:58.234609+00:00
---

# Delete the Ray cluster on Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray/delete-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Delete the Ray cluster on Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

When you finish [developing an application](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray/develop-application) for your Ray cluster on Gemini Enterprise Agent Platform, delete the cluster to avoid unnecessary billing.

**Note:** You can't reuse the cluster name for up to two hours after deleting the cluster.

### Console

  1. In the Google Cloud console, go to the Ray on Agent Platform page.

[Go to the Ray page](https://console.cloud.google.com/vertex-ai/ray)

  2. Select the Ray cluster on Gemini Enterprise Agent Platform you want to delete.

  3. Click **Delete**.




###  Agent Platform SDK for Python 

From the same Python environment where you connected to your Ray cluster on Gemini Enterprise Agent Platform, run the following:
    
    
    # Shut down the Ray on Agent Platform if currently connected
    ray.shutdown()
    
    # Delete cluster
    vertex_ray.delete_ray_cluster(CLUSTER_RESOURCE_NAME)

Where:

  * CLUSTER_RESOURCE_NAME: CLUSTER_RESOURCE_NAME='projects/{}/locations/{}/persistentResources/{}'.format(PROJECT_ID, LOCATION, CLUSTER_NAME).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
