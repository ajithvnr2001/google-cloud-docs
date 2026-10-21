---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_vllm/
title: Run ML inference by using vLLM on GPUs \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:50.029798+00:00
---

# Run ML inference by using vLLM on GPUs  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_vllm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Run ML inference by using vLLM on GPUs Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_vllm.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_vllm.ipynb) [vLLM](https://github.com/vllm-project/vllm) is a fast and user-friendly library for LLM inference and serving. vLLM optimizes LLM inference with mechanisms like PagedAttention for memory management and continuous batching for increasing throughput. For popular models, vLLM has been shown to increase throughput by a multiple of 2 to 4. With Apache Beam, you can serve models with vLLM and scale that serving with just a few lines of code. This notebook demonstrates how to run machine learning inference by using vLLM and GPUs in three ways:

  * locally without Apache Beam
  * locally with the Apache Beam local runner
  * remotely with the Dataflow runner

It also shows how to swap in a different model without modifying your pipeline structure by changing the configuration.

## Requirements

This notebook assumes that a GPU is enabled in Colab. If this setting isn't enabled, the locally executed sections of this notebook might not work. To enable a GPU, in the Colab menu, click **Runtime** > **Change runtime type**. For **Hardware accelerator** , choose a GPU accelerator. If you can't access a GPU in Colab, you can run the Dataflow section of this notebook. To run the Dataflow section, you need access to the following resources:

  * a computer with Docker installed
  * a [Google Cloud](https://cloud.google.com/) account



## Install dependencies

Before creating your pipeline, download and install the dependencies required to develop with Apache Beam and vLLM. vLLM is supported in Apache Beam versions 2.60.0 and later.
    
    
    pip install openai>=1.52.2
    pip install vllm>=0.6.3
    pip install triton>=3.1.0
    pip install apache-beam[gcp]==2.61.0
    pip install nest_asyncio # only needed in colab
    pip check

## Colab only: allow nested asyncio

The vLLM model handler logic below uses asyncio to feed vLLM records. This only works if we are not already in an asyncio event loop. Most of the time, this is fine, but colab already operates in an event loop. To work around this, we can use nest_asyncio to make things work smoothly in colab. Do not include this step outside of colab.
    
    
    # This should not be necessary outside of colab.
    import nest_asyncio
    nest_asyncio.apply()
    
    
    
    
    

## Run locally without Apache Beam

In this section, you run a vLLM server without using Apache Beam. Use the `facebook/opt-125m` model. This model is small enough to fit in Colab memory and doesn't require any extra authentication. First, start the vLLM server. This step might take a minute or two, because the model needs to download before vLLM starts running inference.
    
    
     python -m vllm.entrypoints.openai.api_server --model facebook/opt-125m
    
    
    
    

Next, while the vLLM server is running, open a separate terminal to communicate with the vLLM serving process. To open a terminal in Colab, in the sidebar, click **Terminal**. In the terminal, run the following commands.
    
    
    pip install openai
    python
    
    from openai import OpenAI
    
    # Modify OpenAI's API key and API base to use vLLM's API server.
    openai_api_key = "EMPTY"
    openai_api_base = "http://localhost:8000/v1"
    client = OpenAI(
        api_key=openai_api_key,
        base_url=openai_api_base,
    )
    completion = client.completions.create(model="facebook/opt-125m",
                                          prompt="San Francisco is a")
    print("Completion result:", completion)
    

This code runs against the server running in the cell. You can experiment with different prompts.

## Run locally with Apache Beam

In this section, you set up an Apache Beam pipeline to run a job with an embedded vLLM instance. First, define the `VllmCompletionsModelHandler` object. This configuration object gives Apache Beam the information that it needs to create a dedicated vLLM process in the middle of the pipeline. Apache Beam then provides examples to the pipeline. No additional code is needed.
    
    
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.vllm_inference import VLLMCompletionsModelHandler
    from apache_beam.ml.inference.base import PredictionResult
    import apache_beam as beam
    
    model_handler = VLLMCompletionsModelHandler('facebook/opt-125m')
    
    
    
    
    

Next, define examples to run inference against, and define a helper function to print out the inference results.
    
    
    class FormatOutput(beam.DoFn):
      def process(self, element, *args, **kwargs):
        yield "Input: {input}, Output: {output}".format(input=element.example, output=element.inference)
    
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
        "Emperor penguins are",
    ]
    
    
    
    
    

Finally, run the pipeline. This step might take a minute or two, because the model needs to download before Apache Beam can start running inference.
    
    
    with beam.Pipeline() as p:
      _ = (p | beam.Create(prompts) # Create a PCollection of the prompts.
             | RunInference(model_handler) # Send the prompts to the model and get responses.
             | beam.ParDo(FormatOutput()) # Format the output.
             | beam.Map(print) # Print the formatted output.
      )
    
    
    
    
    

## Run remotely on Dataflow

After you validate that the pipeline can run against a vLLM locally, you can productionalize the workflow on a remote runner. This notebook runs the pipeline on the Dataflow runner.

### Build a Docker image

To run a pipeline with vLLM on Dataflow, you must create a Docker image that contains your dependencies and is compatible with a GPU runtime. For more information about building GPU compatible Dataflow containers, see [Build a custom container image](https://cloud.google.com/dataflow/docs/gpu/use-gpus#custom-container) in the Datafow documentation. First, define and save your Dockerfile. This file uses an Nvidia GPU-compatible base image. In the Dockerfile, install the Python dependencies needed to run the job. Before proceeding, make sure that your configuration meets the following requirements:

  * The Python version in the following cell matches the Python version defined in the Dockerfile.
  * The Apache Beam version defined in your dependencies matches the Apache Beam version defined in the Dockerfile.


    
    
    python --version
    
    
    
    
    
    
    cell_str='''
    FROM nvidia/cuda:12.4.1-devel-ubuntu22.04
    
    RUN apt update
    RUN apt install software-properties-common -y
    RUN add-apt-repository ppa:deadsnakes/ppa
    RUN apt update
    RUN apt-get update
    
    ARG DEBIAN_FRONTEND=noninteractive
    
    RUN apt install python3.10-full -y
    # RUN apt install python3.10-venv -y
    # RUN apt install python3.10-dev -y
    RUN rm /usr/bin/python3
    RUN ln -s python3.10 /usr/bin/python3
    RUN python3 --version
    RUN apt-get install -y curl
    RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 && pip install --upgrade pip
    
    # Copy the Apache Beam worker dependencies from the Beam Python 3.10 SDK image.
    COPY --from=apache/beam_python3.10_sdk:2.61.0 /opt/apache/beam /opt/apache/beam
    
    RUN pip install --no-cache-dir -vvv apache-beam[gcp]==2.61.0
    RUN pip install openai>=1.52.2 vllm>=0.6.3 triton>=3.1.0
    
    RUN apt install libcairo2-dev pkg-config python3-dev -y
    RUN pip install pycairo
    
    # Set the entrypoint to Apache Beam SDK worker launcher.
    ENTRYPOINT [ "/opt/apache/beam/boot" ]
    '''
    
    with open('VllmDockerfile', 'w') as f:
      f.write(cell_str)
    

After you save the Dockerfile, build and push your Docker image. Because Docker is not accessible from Colab, you need to complete this step in a separate environment.

  1. In the sidebar, click **Files** to open the **Files** pane.
  2. In an environment with Docker installed, download the file **VllmDockerfile** file to an empty folder.
  3. Run the following commands. Replace `<REPOSITORY_NAME>:<TAG>` with a valid [Artifact Registry](https://cloud.google.com/artifact-registry/docs/overview) repository and tag.
         
         docker build -t "<REPOSITORY_NAME>:<TAG>" -f VllmDockerfile ./
         docker image push "<REPOSITORY_NAME>:<TAG>"
         




### Define and run the pipeline

When you have a working Docker image, define and run your pipeline. First, define the pipeline options that you want to use to launch the Dataflow job. Before running the next cell, replace the following variables:

  * `<BUCKET_NAME>`: the name of a valid [Google Cloud Storage](https://cloud.google.com/storage?e=48754805&hl=en) bucket. Don't include a `gs://` prefix or trailing slashes.
  * `<REPOSITORY_NAME>`: the name of the Google Artifact Registry repository that you used in the previous step. 
  * `<IMAGE_TAG>`: image tag used in the previous step. Prefer a versioned tag or SHA instead of :latest tag or mutable tags.
  * `<PROJECT_ID>`: the name of the Google Cloud project that you created your bucket and Artifact Registry repository in.

This workflow uses the following Dataflow service option: `worker_accelerator=type:nvidia-tesla-t4;count:1;install-nvidia-driver:5xx`. When you use this service option, Dataflow to installs a T4 GPU that uses a `5xx` series Nvidia driver on each worker machine. The 5xx driver is required to run vLLM jobs.
    
    
    from apache_beam.options.pipeline_options import GoogleCloudOptions
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.options.pipeline_options import SetupOptions
    from apache_beam.options.pipeline_options import StandardOptions
    from apache_beam.options.pipeline_options import WorkerOptions
    
    
    options = PipelineOptions()
    
    # Replace with your bucket name.
    BUCKET_NAME = '<BUCKET_NAME>' # @param {type:'string'}
    # Replace with the image repository and tag from the previous step.
    CONTAINER_IMAGE = '<REPOSITORY_NAME>:<TAG>'  # @param {type:'string'}
    # Replace with your GCP project
    PROJECT_NAME = '<PROJECT_ID>' # @param {type:'string'}
    
    options.view_as(GoogleCloudOptions).project = PROJECT_NAME
    
    # Provide required pipeline options for the Dataflow Runner.
    options.view_as(StandardOptions).runner = "DataflowRunner"
    
    # Set the Google Cloud region that you want to run Dataflow in.
    options.view_as(GoogleCloudOptions).region = 'us-central1'
    
    # IMPORTANT: Replace BUCKET_NAME with the name of your Cloud Storage bucket.
    dataflow_gcs_location = "gs://%s/dataflow" % BUCKET_NAME
    
    # The Dataflow staging location. This location is used to stage the Dataflow pipeline and the SDK binary.
    options.view_as(GoogleCloudOptions).staging_location = '%s/staging' % dataflow_gcs_location
    
    
    # The Dataflow staging location. This location is used to stage the Dataflow pipeline and the SDK binary.
    options.view_as(GoogleCloudOptions).staging_location = '%s/staging' % dataflow_gcs_location
    
    # The Dataflow temp location. This location is used to store temporary files or intermediate results before outputting to the sink.
    options.view_as(GoogleCloudOptions).temp_location = '%s/temp' % dataflow_gcs_location
    
    # Enable GPU runtime. Make sure to enable 5xx driver since vLLM only works with 5xx drivers, not 4xx
    options.view_as(GoogleCloudOptions).dataflow_service_options = ["worker_accelerator=type:nvidia-tesla-t4;count:1;install-nvidia-driver:5xx"]
    
    options.view_as(SetupOptions).save_main_session = True
    
    # Choose a machine type compatible with GPU type
    options.view_as(WorkerOptions).machine_type = "n1-standard-4"
    
    options.view_as(WorkerOptions).sdk_container_image = CONTAINER_IMAGE
    
    
    
    
    

Next, authenticate Colab so that it can to submit a job on your behalf.
    
    
    def auth_to_colab():
      from google.colab import auth
      auth.authenticate_user()
    
    auth_to_colab()
    
    
    
    
    

Finally, run the pipeline on Dataflow. The pipeline definition is almost exactly the same as the definition used for local execution. The pipeline options are the only change to the pipeline. The following code creates a Dataflow job in your project. You can view the results in Colab or in the Google Cloud console. Creating a Dataflow job and downloading the model might take a few minutes. After the job starts performing inference, it quickly runs through the inputs.
    
    
    import logging
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.vllm_inference import VLLMCompletionsModelHandler
    from apache_beam.ml.inference.base import PredictionResult
    import apache_beam as beam
    
    class FormatOutput(beam.DoFn):
      def process(self, element, *args, **kwargs):
        yield "Input: {input}, Output: {output}".format(input=element.example, output=element.inference)
    
    logging.getLogger().setLevel(logging.INFO)  # Output additional Dataflow Job metadata and launch logs. 
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
        "John cena is",
    ]
    
    # Specify the model handler, providing a path and the custom inference function.
    model_handler = VLLMCompletionsModelHandler('facebook/opt-125m')
    
    with beam.Pipeline(options=options) as p:
      _ = (p | beam.Create(prompts) # Create a PCollection of the prompts.
             | RunInference(model_handler) # Send the prompts to the model and get responses.
             | beam.ParDo(FormatOutput()) # Format the output.
             | beam.Map(logging.info) # Print the formatted output.
      )
    
    
    
    
    

## Run vLLM with a Gemma model

After you configure your pipeline, switching the model used by the pipeline is relatively straightforward. You can run the same pipeline, but switch the model name defined in the model handler. This example runs the pipeline created previously but uses a [Gemma](https://ai.google.dev/gemma) model. Before you start, sign in to HuggingFace, and make sure that you can access the Gemma models. To access Gemma models, you must accept the terms and conditions.

  1. Navigate to the [Gemma Model Card](https://huggingface.co/google/gemma-2b).
  2. Sign in, or sign up for a free HuggingFace account.
  3. Follow the prompts to agree to the conditions

When you complete these steps, the following message appears on the model card page: `You have been granted access to this model`. Next, sign in to your account from this notebook by running the following code and then following the prompts.
    
    
     huggingface-cli login
    
    
    
    

Verify that the notebook can now access the Gemma model. Run the following code, which starts a vLLM server to serve the Gemma 2b model. Because the default T4 Colab runtime doesn't support the full data type precision needed to run Gemma models, the `--dtype=half` parameter is required. When successful, the following cell runs indefinitely. After it starts the server process, you can shut it down. When the server process starts, the Gemma 2b model is successfully downloaded, and the server is ready to serve traffic.
    
    
     python -m vllm.entrypoints.openai.api_server --model google/gemma-2b --dtype=half
    
    
    
    

To run the pipeline in Apache Beam, run the following code. Update the `VLLMCompletionsModelHandler` object with the new parameters, which match the command from the previous cell. Reuse all of the pipeline logic from the previous pipelines.
    
    
    model_handler = VLLMCompletionsModelHandler('google/gemma-2b', vllm_server_kwargs={'dtype': 'half'})
    
    with beam.Pipeline() as p:
      _ = (p | beam.Create(prompts) # Create a PCollection of the prompts.
             | RunInference(model_handler) # Send the prompts to the model and get responses.
             | beam.ParDo(FormatOutput()) # Format the output.
             | beam.Map(print) # Print the formatted output.
      )
    
    
    
    
    

### Run Gemma on Dataflow

As a next step, run this pipeline on Dataflow. Follow the same steps described in the "Run remotely on Dataflow" section of this page:

  1. Construct a Dockerfile and push a new Docker image. You can use the same Dockerfile that you created previously, but you need to add a step to set your HuggingFace authentication key. In your Dockerfile, add the following line before the entrypoint:
         
         RUN python3 -c 'from huggingface_hub import HfFolder; HfFolder.save_token("<TOKEN>")'
         

  2. Set pipeline options. You can reuse the options defined in this notebook. Replace the Docker image location with your new Docker image.
  3. Run the pipeline. Copy the pipeline that you ran on Dataflow, and replace the pipeline options with the pipeline options that you just defined.

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
