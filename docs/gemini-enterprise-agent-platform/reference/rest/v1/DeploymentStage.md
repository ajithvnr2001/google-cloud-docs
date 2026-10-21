---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DeploymentStage/
title: DeploymentStage \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:18:56.517306+00:00
---

# DeploymentStage  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/DeploymentStage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  DeploymentStage Stay organized with collections  Save and categorize content based on your preferences. 

Stage field indicating the current progress of a deployment.

Enums  
---  
`DEPLOYMENT_STAGE_UNSPECIFIED` | Default value. This value is unused.  
`STARTING_DEPLOYMENT` | The deployment is initializing and setting up the environment.  
`PREPARING_MODEL` | The deployment is preparing the model assets.  
`CREATING_SERVING_CLUSTER` | The deployment is creating the underlying serving cluster.  
`ADDING_NODES_TO_CLUSTER` | The deployment is adding nodes to the serving cluster.  
`GETTING_CONTAINER_IMAGE` | The deployment is getting the container image for the model server.  
`STARTING_MODEL_SERVER` | The deployment is starting the model server.  
`FINISHING_UP` | The deployment is performing finalization steps.  
`DEPLOYMENT_TERMINATED` | The deployment has terminated.  
`SUCCESSFULLY_DEPLOYED` | The deployment has succeeded.  
`FAILED_TO_DEPLOY` | The deployment has failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
