---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers/
title: Prebuilt containers for inference and explanation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:51.264322+00:00
---

# Prebuilt containers for inference and explanation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Prebuilt containers for inference and explanation Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform provides Docker container images that you run as _prebuilt containers_ for serving inferences and [explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview) from trained model artifacts. These containers, which are organized by machine learning (ML) framework and framework version, provide [HTTP inference servers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/custom-container-requirements#server) that you can use to serve inferences with minimal configuration. In many cases, using a prebuilt container is simpler than [creating your own custom container for inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/use-custom-container).

This document lists the prebuilt containers for inferences and explanations, and it describes how to use them with model artifacts that you [created using Agent Platform's custom training functionality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/code-requirements) or model artifacts that you created outside of Agent Platform.

## Support policy and schedule

Gemini Enterprise Agent Platform supports each framework version based on a schedule to minimize security vulnerabilities. Review the [Support policy schedule](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/framework-support-policy#support_policy_schedule) to understand the implications of the end-of-support and end-of-availability dates.

## Available container images

Each of the following container images is available in several Artifact Registry repositories, which [store data in various locations](https://docs.cloud.google.com/artifact-registry/docs/repo-locations). You can use any of the URIs for an image when you perform custom training; each provides the same container image. If you use the Google Cloud console to create a [`Model`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models) resource, the Google Cloud console selects the URI that best matches the [location where you are using Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations) in order to reduce latency.

**Note:** Using image names without the `latest` tag isn't supported. You must use an image with the `latest` tag.

### TensorFlow

#### Available TensorFlow container images (Click to expand)

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.15 | CPU only | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-15:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-15:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-15:latest`

  
2.15 | GPU (CUDA 12.x) | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/tf2-gpu.2-15:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/tf2-gpu.2-15:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/tf2-gpu.2-15:latest`

  
2.14 | CPU only | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-14:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-14:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-14:latest`

  
2.14 | GPU (CUDA 12.x) | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/tf2-gpu.2-14:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/tf2-gpu.2-14:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/tf2-gpu.2-14:latest`

  
2.13 | CPU only | Nov 28, 2024 | Nov 28, 2025 |   
2.13 | GPU (CUDA 12.x) | Nov 28, 2024 | Nov 28, 2025 |   
2.12 | CPU only | June 30, 2024 | June 30, 2025 |   
2.12 | GPU (CUDA 11.x) | June 30, 2024 | June 30, 2025 |   
2.11 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.11 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.10 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.10 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.9 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.9 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.8 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.8 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.7 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.7 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.6 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.6 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.5 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.5 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.4 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.4 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.3 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.3 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.2 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.2 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.1 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.1 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
1.15 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
1.15 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
  
### Optimized TensorFlow runtime

The following container images use the optimized TensorFlow runtime. For more information, see [Use the optimized TensorFlow runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/optimized-tensorflow-runtime). 

#### Available optimized TensorFlow runtime container images (Click to expand)

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
nightly | CPU only | Not applicable | Not applicable | 

  * `us-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-cpu.nightly:latest`
  * `europe-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-cpu.nightly:latest`
  * `asia-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-cpu.nightly:latest`

  
nightly | GPU (CUDA 12.x) | Not applicable | Not applicable | 

  * `us-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-gpu.nightly:latest`
  * `europe-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-gpu.nightly:latest`
  * `asia-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-gpu.nightly:latest`

  
nightly | Cloud TPU | Not applicable | Not applicable | 

  * `us-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-tpu.nightly:latest`
  * `europe-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-tpu.nightly:latest`
  * `asia-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-tpu.nightly:latest`

  
2.17 | CPU only | Jul 11, 2024 | Jul 11, 2025 | 

  * `us-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-cpu.2-17:latest`
  * `europe-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-cpu.2-17:latest`
  * `asia-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-cpu.2-17:latest`

  
2.17 | GPU (CUDA 12.x) | Jul 11, 2024 | Jul 11, 2025 | 

  * `us-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-gpu.2-17:latest`
  * `europe-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-gpu.2-17:latest`
  * `asia-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-gpu.2-17:latest`

  
2.17 | Cloud TPU | Jul 11, 2024 | Jul 11, 2025 | 

  * `us-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-tpu.2-17:latest`
  * `europe-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-tpu.2-17:latest`
  * `asia-docker.pkg.dev/vertex-ai-restricted/prediction/tf_opt-tpu.2-17:latest`

  
2.16 | CPU only | Apr 26, 2024 | Apr 26, 2025 |   
2.16 | GPU (CUDA 12.x) | Apr 26, 2024 | Apr 26, 2025 |   
2.16 | Cloud TPU | Apr 26, 2024 | Apr 26, 2025 |   
2.15 | CPU only | Aug 15, 2024 | Aug 15, 2025 |   
2.15 | GPU (CUDA 12.x) | Aug 15, 2024 | Aug 15, 2025 |   
2.15 | Cloud TPU | Aug 15, 2024 | Aug 15, 2025 |   
2.14 | CPU only | Aug 15, 2024 | Aug 15, 2025 |   
2.14 | GPU (CUDA 12.x) | Aug 15, 2024 | Aug 15, 2025 |   
2.13 | CPU only | Aug 15, 2024 | Aug 15, 2025 |   
2.13 | GPU (CUDA 11.x) | Aug 15, 2024 | Aug 15, 2025 |   
2.12 | CPU only | May 15, 2024 | May 15, 2025 |   
2.12 | GPU (CUDA 11.x) | May 15, 2024 | May 15, 2025 |   
2.11 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.11 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.10 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.10 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.9 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.9 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
2.8 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
2.8 | GPU (CUDA 11.x) | Nov 15, 2023 | Nov 15, 2024 |   
  
### PyTorch

#### Available PyTorch container images (Click to expand)

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.4 (Python 3.9) | CPU only | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-4:latest`

  
2.4 (Python 3.9) | GPU (CUDA 12.x) | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-4:latest`

  
2.4 (Python 3.9) | Cloud TPU | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-4:latest`

  
2.3 (Python 3.9) | CPU only | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-3:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-3:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-3:latest`

  
2.3 (Python 3.9) | GPU (CUDA 12.x) | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-3:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-3:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-3:latest`

  
2.3 (Python 3.9) | Cloud TPU | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-3:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-3:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-3:latest`

  
2.2 (Python 3.9) | CPU only | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-2:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-2:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-cpu.2-2:latest`

  
2.2 (Python 3.9) | GPU (CUDA 12.x) | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-2:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-2:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-gpu.2-2:latest`

  
2.2 (Python 3.9) | Cloud TPU | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-2:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-2:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/pytorch-tpu.2-2:latest`

  
2.1 (Python 3.9) | CPU only | Dec 01, 2024 | Dec 01, 2025 |   
2.1 (Python 3.9) | GPU (CUDA 12.x) | Dec 01, 2024 | Dec 01, 2025 |   
2.1 (Python 3.9) | Cloud TPU | Dec 01, 2024 | Dec 01, 2025 |   
2.0 (Python 3.9) | CPU only | Jul 27, 2024 | Jul 27, 2025 |   
2.0 (Python 3.9) | GPU (CUDA 11.x) | Jul 27, 2024 | Jul 27, 2025 |   
1.13 (Python 3.8) | CPU only | May 15, 2024 | May 15, 2025 |   
1.13 (Python 3.8) | GPU (CUDA 11.x) | May 15, 2024 | May 15, 2025 |   
1.12 | CPU only | May 15, 2024 | May 15, 2025 |   
1.12 | GPU (CUDA 11.x) | May 15, 2024 | May 15, 2025 |   
1.11 | CPU only | May 15, 2024 | May 15, 2025 |   
1.11 | GPU (CUDA 11.x) | May 15, 2024 | May 15, 2025 |   
  
### scikit-learn

#### Available scikit-learn container images (Click to expand)

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
1.6 (Python 3.10) | CPU only | Oct 14, 2026 | Oct 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-6:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-6:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-6:latest`

  
1.5 (Python 3.10) | CPU only | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-5:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-5:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-5:latest`

  
1.4 (Python 3.10) | CPU only | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-4:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-4:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-4:latest`

  
1.3 (Python 3.10) | CPU only | Nov 28, 2024 | Nov 28, 2025 |   
1.2 (Python 3.10) | CPU only | June 30, 2024 | June 30, 2025 |   
1.0 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
0.24 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
0.23 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
0.22 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
0.20 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
  
### XGBoost

#### Available XGBoost container images (Click to expand)

ML framework version | Supported accelerators (and CUDA version, if applicable) | End of patch and support date | End of availability | Supported images  
---|---|---|---|---  
2.1 (Python 3.10) | CPU only | July 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.2-1:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.2-1:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.2-1:latest`

  
2.0 (Python 3.10) | CPU only | Jan 14, 2026 | Jan 14, 2027 | 

  * `us-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.2-0:latest`
  * `europe-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.2-0:latest`
  * `asia-docker.pkg.dev/vertex-ai/prediction/xgboost-cpu.2-0:latest`

  
1.7 (Python 3.10) | CPU only | June 30, 2024 | Dec 30, 2025 |   
1.6 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
1.5 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
1.4 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
1.3 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
1.2 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
1.1 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
0.90 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
0.82 | CPU only | Nov 15, 2023 | Nov 15, 2024 |   
  
## Use a prebuilt container

You can specify a prebuilt container for inference when you [create a custom `TrainingPipeline` resource that uploads a `Model`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/create-training-pipeline#custom-job-model-upload) or when you [import model artifacts as a `Model`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/import-model).

To use one of these prebuilt containers, you must save your model as one or more _model artifacts_ that comply with the requirements of the prebuilt container. For more information, see [Export model artifacts for inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/exporting-model-artifacts).

The following notebooks demonstrate how to use a prebuilt container to serve inferences.

What do you want to do? | Notebook  
---|---  
Train and serve a TensorFlow model using a prebuilt container | [Custom training and online inference](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/custom/sdk-custom-image-classification-online.ipynb)  
Serve a PyTorch model using a prebuilt container | [Serving PyTorch image models with prebuilt containers on Agent Platform](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/prediction/pytorch_image_classification_with_prebuilt_serving_containers.ipynb)  
Serve a Stable Diffusion model using a prebuilt container | [Deploy and host a Stable Diffusion model on Agent Platform](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/vertex_endpoints/torchserve/dreambooth_stablediffusion.ipynb)  
  
## Notebooks

To learn more, run the "Serving PyTorch image models with prebuilt containers on " notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/prediction/pytorch_image_classification_with_prebuilt_serving_containers.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fprediction%2Fpytorch_image_classification_with_prebuilt_serving_containers.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fprediction%2Fpytorch_image_classification_with_prebuilt_serving_containers.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/prediction/pytorch_image_classification_with_prebuilt_serving_containers.ipynb)

## What's next

  * Learn how to [deploy a model to an endpoint to serve inferences](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/deploy-model-api). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
