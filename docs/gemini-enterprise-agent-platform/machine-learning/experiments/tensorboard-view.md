---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-view/
title: View Vertex AI TensorBoard data \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:16.991806+00:00
---

# View Vertex AI TensorBoard data  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  View Vertex AI TensorBoard data Stay organized with collections  Save and categorize content based on your preferences. 

The Vertex AI TensorBoard web app provides a visualization of logs associated with a Vertex AI TensorBoard experiment. This web application offers several tools and dashboards to visualize and compare data across experiment runs, and to [profile model training performance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/tensorboard-profiler).
    
    
    Note: If you are having trouble viewing results, make sure your user account
    has the [Agent Platform Viewer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.viewer) (or higher) role associated with it.
    

![TensorBoard view appear](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/tb-view-appears.png)

To learn more about each dashboard, see the [README](https://github.com/tensorflow/tensorboard/blob/master/README.md#the-visualizations) for "The Visualization".

## Access a Vertex AI TensorBoard web app

The Vertex AI TensorBoard web app is accessed using the following address format:

`https://REGION.tensorboard.googleusercontent.com/experiment/projects+PROJECT_NAME_OR_ID+locations+REGION+tensorboards+TENSORBOARD_ID+experiments+EXPERIMENT_NAME`

  * `REGION`: the region your TensorBoard is located in
  * `PROJECT_ID`: the project your TensorBoard was created in
  * `TENSORBOARD_ID`: the [TensorBoard ID](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-setup#tensorboard_id)
  * `EXPERIMENT_NAME`: the name of the TensorBoard experiment



This link can be shared and used by anyone who has permission.

You can navigate here directly by inserting the appropriate values, or by following a link available in the following ways.

### gcloud CLI and Agent Platform SDK for Python

When creating or uploading logs to a Vertex AI TensorBoard, the gcloud CLI and SDK output a link to the Vertex AI TensorBoard instance.

### Google Cloud console

You can access the TensorBoard web app using the Google Cloud console.

### Experiments

If your Vertex AI TensorBoard is associated with a Gemini Enterprise Agent Platform Experiment, which is automatic when a [default instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-setup#use_default_instance) is involved, you can access the TensorBoard web app directly from the Experiments page. ![tensorboard view](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/experiments-tb-view.png)

### Custom training

If you used Vertex AI TensorBoard with [custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-training) you can access the TensorBoard web app directly from the custom training job.

  1. In the Gemini Enterprise Agent Platform section of the Google Cloud console, go to the **Training** page. [Go to Training](https://console.cloud.google.com/agent-platform/training)
  2. Click **Custom Jobs** tab.
  3. Select your training job from the list of training runs. The details page appears
  4. Click the **Open TensorBoard** button.  
![open tensorboard button](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/custom-job-link.png)



### Gemini Enterprise Agent Platform Pipelines

If you used Vertex AI TensorBoard with [Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-with-pipelines), the TensorBoard web app can be accessed directly from the component information display.

  1. In the Gemini Enterprise Agent Platform section of the Google Cloud console, go to the **Pipelines** page. [Go to Pipelines](https://console.cloud.google.com/agent-platform/pipelines)
  2. From the pipelines tab, scroll or filter the pipeline list to find your pipeline.
  3. On the pipeline display select the component where TensorBoard metrics are captured, typically the training component.
  4. Select the **Open TensorBoard** button in the upper right.  
![tensorboard view for classification](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/image-classification-pipeline.png)



## Visualize Vertex AI TensorBoard metrics in the Google Cloud console

If your TensorBoard instance is associated with a Vertex AI Experiments, which is automatic when using a [default TensorBoard instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboard-setup#use_default_instance), certain metrics can be visualized directly in the Google Cloud console, without using the web application.

The [Compare and analyze runs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/experiments/compare-analyze-runs#console-compare-analyze-runs) document describes how to view details of your experiment runs and compare the experiment runs to each other in the Google Cloud console. TensorBoard timeseries metrics appear under the **Charts** tab in the navigation bar of the Gemini Enterprise Agent Platform Experiments console.

![Agent Platform navigation bar with timeseries data charts](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/experiments/images/compare-runs-single-run-details.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
