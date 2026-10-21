---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/dataflow_tpu_examples/
title: Running Dataflow on TPUs: Quickstart examples \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:47.096523+00:00
---

# Running Dataflow on TPUs: Quickstart examples  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/dataflow_tpu_examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Running Dataflow on TPUs: Quickstart examples Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/dataflow_tpu_examples.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/dataflow_tpu_examples.ipynb)   
  
This Colab notebook shows you how to set up two pipelines:

  1. A pipeline that runs a trivial computation on a TPU.
  2. A pipeline that runs inference using the [Gemma-3-27b-it model](https://huggingface.co/google/gemma-3-27b-it) on TPUs .

Both pipelines use a custom Docker image. The Dataflow jobs will launch using a [Flex Template](https://cloud.google.com/dataflow/docs/guides/templates/using-flex-templates) to allow the same job to be reproduced in different Colab environments.

## Prerequisites

First, you need to authenticate to your Google Cloud Project. After running the cell below, you might need to **click on the text prompts in the cell** and enter inputs as prompted.
    
    
    import sys
    if 'google.colab' in sys.modules:
        from google.colab import auth
        auth.authenticate_user()
    !gcloud auth login
    

Now, set environment variables to access pipeline resources, such as a Cloud Storage bucket or a repository to host container images in Artifact Registry.
    
    
    import os
    import datetime
    
    project_id = "some-project" # @param {type:"string"}
    gcs_bucket = "some-bucket" # @param {type:"string"}
    ar_repository = "some-ar-repo" # @param {type:"string"}
    
    # Use a region where you have TPU accelerator quota.
    region = "some-region1" # @param {type:"string"}
    !gcloud config set project {project_id}
    

Enable the necessary APIs if your project hasn't enabled them yet. If you have the appropriate permissions, you can enable the APIs by running the following cell.
    
    
    !gcloud services enable \
        dataflow.googleapis.com \
        compute.googleapis.com \
        logging.googleapis.com \
        storage.googleapis.com \
        cloudresourcemanager.googleapis.com \
        artifactregistry.googleapis.com \
        cloudbuild.googleapis.com
    

Now, you'll create a Cloud Storage bucket and Artifact Registry repository if you don't already have these resources.
    
    
    gcloud storage buckets describe gs://{gcs_bucket} >/dev/null 2>&1 || gcloud storage buckets create gs://{gcs_bucket} --location={region}
    gcloud artifacts repositories describe {ar_repository} --location={region} >/dev/null 2>&1 || gcloud artifacts repositories create {ar_repository} --repository-format=docker --location={region}

# Example 1: Minimal computation pipeline using TPU V5E

First, create a simple pipeline you can run to verify that TPUs are accessible, your custom Docker image has the necessary dependencies to interact with the TPUs and your Dataflow pipeline launch configuration is valid. With this sample you use the PyTorch library to interact with a TPU device.
    
    
    %%writefile minimal_tpu_pipeline.py
    from __future__ import annotations
    import torch
    import torch_xla
    import argparse
    import logging
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    
    
    class check_tpus(beam.DoFn):
        """Validates that a TPU is accessible."""
        def setup(self):
            tpu_devices = torch_xla.xm.get_xla_supported_devices()
            if not tpu_devices:
                raise RuntimeError("No TPUs found on the worker.")
            logging.info(f"Found TPU devices: {tpu_devices}")
            tpu = torch_xla.device()
            t1 = torch.randn(3, 3, device=tpu)
            t2 = torch.randn(3, 3, device=tpu)
            result = t1 + t2
            logging.info(f"Result of a sample TPU computation: {result}")
    
        def process(self, element):
            yield element
    
    
    def run(input_text: str, beam_args: list[str] | None = None) -> None:
        beam_options = PipelineOptions(beam_args, save_main_session=True)
        pipeline = beam.Pipeline(options=beam_options)
        (
            pipeline
            | "Create data" >> beam.Create([input_text])
            | "Check TPU availability" >> beam.ParDo(check_tpus())
            | "My transform" >> beam.LogElements(level=logging.INFO)
        )
        pipeline.run()
    
    
    if __name__ == "__main__":
        logging.getLogger().setLevel(logging.INFO)
    
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--input-text",
            default="Hello! This pipeline verified that TPUs are accessible.",
            help="Input text to display.",
        )
        args, beam_args = parser.parse_known_args()
    
        run(args.input_text, beam_args)
    

## Create a Dockerfile for your TPU-compatible container image.

In your Dockerfile you configure the environment variables to use with a `V5E` `1x1` TPU device. **You must use the region where you have V5E TPU quota to run this example.** To use a different TPU, adjust the configuration according to the [Dataflow documentation](https://cloud.google.com/dataflow/docs/tpu/use-tpus). This Dockerfile creates an image that serves both as a custom worker image for your Beam pipeline and also as a launcher image for your Flex template.
    
    
    %%writefile Dockerfile
    
    FROM python:3.11-slim
    
    COPY minimal_tpu_pipeline.py minimal_tpu_pipeline.py
    
    # Copy the Apache Beam worker dependencies from the Beam Python 3.10 SDK image.
    COPY --from=apache/beam_python3.10_sdk:2.67.0 /opt/apache/beam /opt/apache/beam
    
    # Copy Template Launcher dependencies
    COPY --from=gcr.io/dataflow-templates-base/python310-template-launcher-base /opt/google/dataflow/python_template_launcher /opt/google/dataflow/python_template_launcher
    
    # Install TPU software and Apache Beam SDK
    RUN pip install --no-cache-dir torch~=2.8.0 torch_xla[tpu]~=2.8.0 apache-beam[gcp]==2.67.0 -f https://storage.googleapis.com/libtpu-releases/index.html
    
    # Configuration for v5e 1x1 accelerator type.
    ENV TPU_CHIPS_PER_HOST_BOUNDS=1,1,1
    ENV TPU_ACCELERATOR_TYPE=v5litepod-1
    ENV TPU_SKIP_MDS_QUERY=1
    ENV TPU_HOST_BOUNDS=1,1,1
    ENV TPU_WORKER_HOSTNAMES=localhost
    ENV TPU_WORKER_ID=0
    
    ENV FLEX_TEMPLATE_PYTHON_PY_FILE=minimal_tpu_pipeline.py
    
    # Set the entrypoint to Apache Beam SDK worker launcher.
    ENTRYPOINT [ "/opt/apache/beam/boot"]
    

## Push your Docker image to Artifact Registry.

Finally, build your Docker image, and push it in Artifact Registry. This process should take about 15 minutes or so.
    
    
    container_tag = "20250801"
    container_image = ''.join([
        region, "-docker.pkg.dev/",
        project_id, "/",
        ar_repository, "/",
        "tpu-minimal-example", ":", container_tag
    ])
    
    !gcloud builds submit --tag {container_image}
    

## Build the Dataflow Flex Template.

To create a reproducible environment for launching the pipeline, build a Flex Template. First, create a `metadata.json` file to change the default Dataflow worker disk size when launching the template.
    
    
    %%writefile metadata.json
    {
        "name": "Minimal TPU Example on Dataflow",
        "description": "A Flex template launching a Dataflow Job doing a TPU computation ",
        "parameters": [
          {
            "name": "disk_size_gb",
            "label": "disk_size_gb",
            "helpText": "disk_size_gb for worker",
            "isOptional": true
          }
        ]
    }
    

Run the following cell to build the Flex Template and save it Cloud Storage.
    
    
    !gcloud dataflow flex-template build gs://{gcs_bucket}/minimal_tpu_pipeline.json \
      --image {container_image} \
      --sdk-language "PYTHON" \
      --metadata-file metadata.json \
      --project {project_id}
    

## Submit your pipeline to Dataflow.

Since you launch the pipeline as a Flex Template, make the following adjustments to the command line:

  * Use `--parameters` option to specify the container image and disk size.
  * Use `--additional-experiments` option to specify the necessary Dataflow service options.
  * To avoid using more than one process on a TPU simultaneously, limit process-level parallelism with the `no_use_multiple_sdk_containers` experiment.


    
    
    !gcloud dataflow flex-template run "minimal-tpu-example-`date +%Y%m%d-%H%M%S`" \
      --template-file-gcs-location gs://{gcs_bucket}/minimal_tpu_pipeline.json \
      --region {region} \
      --project {project_id} \
      --temp-location gs://{gcs_bucket}/tmp \
      --parameters sdk_container_image={container_image} \
      --worker-machine-type "ct5lp-hightpu-1t" \
      --parameters disk_size_gb=50 \
      --additional-experiments "worker_accelerator=type:tpu-v5-lite-podslice;topology:1x1" \
      --additional-experiments "no_use_multiple_sdk_containers"
    

Once the job is launched, use the following link to monitor its status: <https://console.cloud.google.com/dataflow/jobs/> Sample worker logs for the `Check TPU availability` step look like the following:
    
    
    Found TPU devices: ['xla:0']
    Result of a sample TPU computation: tensor([[ 0.3355, -1.4628, -3.2610], [-1.4656, 0.3196, -2.8766], [ 0.8667, -1.5060, 0.7125]], device='xla:0')
    

# Example 2: Inference Pipeline with Gemma 3 27B using TPU V6E

This example shows you how to perform inference on a TPU using Gemma 3 27b model. To fit this model in TPU memory, you need four V6E TPU chips connected in 2x2 topology. **You must use the region where you have V6E TPU quota to run this example.** The example uses [Apache Beam RunInference APIs](https://beam.apache.org/documentation/transforms/python/elementwise/runinference/) with the [VLLM Completions model handler](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.vllm_inference.html). The model is downloaded from HuggingFace at runtime, and running the example requires a [HuggingFace access token](https://huggingface.co/docs/hub/en/security-tokens). First, create a pipeline file.
    
    
    %%writefile gemma_tpu_pipeline.py
    from __future__ import annotations
    import argparse
    import logging
    import apache_beam as beam
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.ml.inference.vllm_inference import VLLMCompletionsModelHandler
    
    
    def run(input_text: str, beam_args: list[str] | None = None) -> None:
        beam_options = PipelineOptions(beam_args, save_main_session=True)
        pipeline = beam.Pipeline(options=beam_options)
        (
            pipeline
            | "Create data" >> beam.Create([input_text])
            | "Run Inference" >> RunInference(
                model_handler=VLLMCompletionsModelHandler(
                    'google/gemma-3-27b-it',
                    {
                        'max-model-len': '4096',
                        'no-enable-prefix-caching': None,
                        'disable-log-requests': None,
                        'tensor-parallel-size': '4',
                        'limit-mm-per-prompt': '{"image": 0}'
                    })
                )
            | "Log Output" >> beam.LogElements(level=logging.INFO)
        )
        pipeline.run()
    
    
    if __name__ == "__main__":
        logging.getLogger().setLevel(logging.INFO)
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--input-text",
            default="What are TPUs?",
            help="Input text query.",
        )
        args, beam_args = parser.parse_known_args()
        run(args.input_text, beam_args)
    

## Create a new Dockerfile for this pipeline with additional dependencies.

Note that this sample uses a different TPU device than the example 1, so the environment variables are different. **You must use your own HuggingFace Token in the Dockerfile.** For instructions on creating a token, see [User access tokens](https://huggingface.co/docs/hub/en/security-tokens).
    
    
    %%writefile Dockerfile
    # Use the official vLLM TPU base image, which has TPU dependencies.
    # To use the latest version, use: vllm/vllm-tpu:nightly
    FROM vllm/vllm-tpu:5964069367a7d54c3816ce3faba79e02110cde17
    
    # Copy your pipeline file.
    COPY gemma_tpu_pipeline.py gemma_tpu_pipeline.py
    
    # You can use a more recent version of Apache Beam
    COPY --from=apache/beam_python3.12_sdk:2.67.0 /opt/apache/beam /opt/apache/beam
    RUN pip install --no-cache-dir apache-beam[gcp]==2.67.0
    
    # Copy Template Launcher dependencies
    COPY --from=gcr.io/dataflow-templates-base/python310-template-launcher-base /opt/google/dataflow/python_template_launcher /opt/google/dataflow/python_template_launcher
    
    # Replace the Hugginface token here.
    RUN python -c 'from huggingface_hub import HfFolder; HfFolder.save_token("YOUR HUGGINGFACE TOKEN")'
    
    # TPU environment variables.
    ENV TPU_SKIP_MDS_QUERY=1
    
    # Configuration for v6e 2x2 accelerator type.
    ENV TPU_HOST_BOUNDS=1,1,1
    ENV TPU_CHIPS_PER_HOST_BOUNDS=2,2,1
    ENV TPU_ACCELERATOR_TYPE=v6e-4
    ENV VLLM_USE_V1=1
    
    ENV FLEX_TEMPLATE_PYTHON_PY_FILE=gemma_tpu_pipeline.py
    
    # Set the entrypoint to Apache Beam SDK worker launcher.
    ENTRYPOINT [ "/opt/apache/beam/boot"]
    

Run the following cell to build the Docker image and push it to Artifact Registry. This process should take 15 min or so.
    
    
    container_tag = "20250801"
    container_image = ''.join([
        region, "-docker.pkg.dev/",
        project_id, "/",
        ar_repository, "/",
        "tpu-run-inference-example", ":", container_tag
    ])
    !gcloud builds submit --tag {container_image}
    

## Build the Flex Template for this pipeline.

To create a reproducible environment for launching the pipeline, build a Flex Template. First, create a `metadata.json` file to change the default Dataflow worker disk size when launching the template.
    
    
    %%writefile metadata.json
    {
        "name": "Gemma 3 27b Run Inference pipeline with VLLM",
        "description": "A template for Dataflow RunInference pipeline with VLLM in a TPU-enabled environment with VLLM",
        "parameters": [
          {
            "name": "disk_size_gb",
            "label": "disk_size_gb",
            "helpText": "disk_size_gb for worker",
            "isOptional": true
          }
        ]
    }
    

Run the following cell to build the Flex Template and save it in Cloud Storage.
    
    
    !gcloud dataflow flex-template build gs://{gcs_bucket}/gemma_tpu_pipeline.json \
      --image {container_image} \
      --sdk-language "PYTHON" \
      --metadata-file metadata.json \
      --project {project_id}
    

## Finally, submit the job to Dataflow.

Since you launch the pipeline as a Flex Template, you are making the following adjustments to the command line:

  * Use the `--parameters` option to specify the container image and disk size
  * Use the `--additional-experiments` option to specify the necessary Dataflow service options.
  * The VLLMCompletionsModelHandler from Beam RunInference APIs only loads the model onto TPUs from a single process. Still, limit the intra-worker parallelism by reducing the value of `--number_of_worker_harness_threads`, which achieves better performance.

Once the job is launched, use the following link to monitor its status: <https://console.cloud.google.com/dataflow/jobs/>
    
    
    !gcloud dataflow flex-template run "gemma-tpu-example-`date +%Y%m%d-%H%M%S`" \
      --template-file-gcs-location gs://{gcs_bucket}/gemma_tpu_pipeline.json \
      --region {region} \
      --project {project_id} \
      --temp-location gs://{gcs_bucket}/tmp \
      --parameters number_of_worker_harness_threads=100 \
      --parameters sdk_container_image={container_image} \
      --parameters disk_size_gb=100 \
      --worker-machine-type "ct6e-standard-4t" \
      --additional-experiments "worker_accelerator=type:tpu-v6e-slice;topology:2x2"
    

Due to model loading and initialization time, the pipeline takes 25 min or so to complete. Sample worker logs for the `Run Inference` step look like the following:
    
    
    PredictionResult(example='What are TPUs?', inference=Completion(id='cmpl-57ebbddeb1c04dc0a8a74f2b60d10f67', choices=[CompletionChoice(finish_reason='length', index=0, logprobs=None, text='\n\nTensor Processing Units (TPUs) are custom-developed AI accelerator ASICs', stop_reason=None, prompt_logprobs=None)], created=1755614936, model='google/gemma-3-27b-it', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=16, prompt_tokens=6, total_tokens=22, completion_tokens_details=None, prompt_tokens_details=None), service_tier=None, kv_transfer_params=None), model_id=None)
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
