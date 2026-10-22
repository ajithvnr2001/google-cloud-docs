---
url: https://docs.cloud.google.com/dataflow/docs/tutorials/streaming-llm/
title: Run an LLM in a streaming pipeline \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:48.305419+00:00
---

# Run an LLM in a streaming pipeline  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tutorials/streaming-llm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Run an LLM in a streaming pipeline Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to run a large language model (LLM) in a streaming Dataflow pipeline by using the Apache Beam RunInference API.

For more information about the RunInference API, see [About Beam ML](https://beam.apache.org/documentation/ml/about-ml/) in the Apache Beam documentation.

The example code is [available on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/run-inference).

## Objectives

  * Create Pub/Sub topics and subscriptions for the model's input and responses.
  * Load the model into Cloud Storage by using a Gemini Enterprise Agent Platform custom job.
  * Run the pipeline.
  * Ask the model a question and get a response.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Dataflow](https://cloud.google.com/dataflow/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)
  * [Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

Run this tutorial on a machine that has at least 5 GB of free disk space to install the dependencies.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataflow, Compute Engine, Cloud Storage, Pub/Sub, and Agent Platform API APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow.googleapis.com compute.googleapis.com storage.googleapis.com pubsub.googleapis.com aiplatform.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Dataflow, Compute Engine, Cloud Storage, Pub/Sub, and Agent Platform API APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable dataflow.googleapis.com compute.googleapis.com storage.googleapis.com pubsub.googleapis.com aiplatform.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  18. Grant roles to your Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.admin`
     * `roles/pubsub.editor`
     * `roles/aiplatform.user`
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role=SERVICE_ACCOUNT_ROLE

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `PROJECT_NUMBER`: your project number. To find your project number, use the [`gcloud projects describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe).
     * `SERVICE_ACCOUNT_ROLE`: each individual role.
  19. Copy the Google Cloud project ID. You need this value later in this tutorial.



## Create the Google Cloud resources

This section explains how to create the following resources:

  * A Cloud Storage bucket to use as a temporary storage location
  * A Pub/Sub topic for the model's prompts
  * A Pub/Sub topic and subscription for the model's responses



### Create a Cloud Storage bucket

Create a Cloud Storage bucket by using the gcloud CLI. This bucket is used as a temporary storage location by the Dataflow pipeline.

To create the bucket, use the [`gcloud storage buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create):
    
    
    gcloud storage buckets create gs://BUCKET_NAME --location=LOCATION
    

Replace the following:

  * BUCKET_NAME: a name for your Cloud Storage bucket that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). Cloud Storage bucket names must be globally unique.
  * LOCATION: the [location](https://docs.cloud.google.com/storage/docs/locations#available-locations) for the bucket.



Copy the bucket name. You need this value later in this tutorial.

### Create Pub/Sub topics and subscriptions

Create two Pub/Sub topics and one subscription. One topic is for the input prompts that you send to the model. The other topic and its attached subscription is for the model's responses.

  1. To create the topics, run the [`gcloud pubsub topics create` command](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) twice, once for each topic: 
         
         gcloud pubsub topics create PROMPTS_TOPIC_ID
         gcloud pubsub topics create RESPONSES_TOPIC_ID
         

Replace the following:

     * PROMPTS_TOPIC_ID: the topic ID for the input prompts to send to the model, such as `prompts`
     * RESPONSES_TOPIC_ID: the topic ID for the model's responses, such as `responses`
  2. To create the subscription and attach it to your responses topic, use the [`gcloud pubsub subscriptions create` command](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create):
         
         gcloud pubsub subscriptions create RESPONSES_SUBSCRIPTION_ID --topic=RESPONSES_TOPIC_ID
         

Replace RESPONSES_SUBSCRIPTION_ID with the subscription ID for the model's responses, such as `responses-subscription`.




Copy the topic IDs and the subscription ID. You need these values later in this tutorial.

## Prepare your environment

Download the code samples and then set up your environment to run the tutorial.

The code samples in the [python-docs-samples GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/run-inference) provide the code that you need to run this pipeline. When you are ready to build your own pipeline, you can use this sample code as a template.

You create an isolated Python virtual environment to run your pipeline project by using [venv](https://docs.python.org/3/library/venv.html). A virtual environment lets you isolate the dependencies of one project from the dependencies of other projects. For more information about how to install Python and create a virtual environment, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

  1. Use the `git clone` command to clone the GitHub repository:
         
         git clone https://github.com/GoogleCloudPlatform/python-docs-samples.git
         

  2. Navigate to the `run-inference` directory:
         
         cd python-docs-samples/dataflow/run-inference
         

  3. If you're using a command prompt, check that you have Python 3 and `pip` running in your system:
         
         python --version
         python -m pip --version
         

If required, [install Python 3](https://docs.cloud.google.com/python/docs/setup#installing_python).

If you're using Cloud Shell, you can skip this step because Cloud Shell already has Python installed.

  4. Create a [Python virtual environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv):
         
         python -m venv /tmp/env
         source /tmp/env/bin/activate
         

  5. Install the dependencies:
         
         pip install -r requirements.txt --no-cache-dir
         




### Model loading code sample

The model loading code in this tutorial launches a Agent Platform custom job that loads the model's `state_dict` object into Cloud Storage.

The starter file looks like the following:
    
    
    # Copyright 2023 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Loads the state_dict for an LLM model into Cloud Storage."""
    
    from __future__ import annotations
    
    import os
    
    import torch
    from transformers import AutoModelForSeq2SeqLM
    
    
    def run_local(model_name: str, state_dict_path: str) -> None:
        """Loads the state dict and saves it into the desired path.
    
        If the `state_dict_path` is a Cloud Storage location starting
        with "gs://", this assumes Cloud Storage is mounted with
        Cloud Storage FUSE in `/gcs`. Vertex AI is set up like this.
    
        Args:
            model_name: HuggingFace model name compatible with AutoModelForSeq2SeqLM.
            state_dict_path: File path to the model's state_dict, can be in Cloud Storage.
        """
        print(f"Loading model: {model_name}")
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name, torch_dtype=torch.bfloat16
        )
        print(f"Model loaded, saving state dict to: {state_dict_path}")
    
        # Assume Cloud Storage FUSE is mounted in `/gcs`.
        state_dict_path = state_dict_path.replace("gs://", "/gcs/")
        directory = os.path.dirname(state_dict_path)
        if directory and not os.path.exists(directory):
            os.makedirs(os.path.dirname(state_dict_path), exist_ok=True)
        torch.save(model.state_dict(), state_dict_path)
        print("State dict saved successfully!")
    
    
    def run_vertex_job(
        model_name: str,
        state_dict_path: str,
        job_name: str,
        project: str,
        bucket: str,
        location: str = "us-central1",
        machine_type: str = "e2-highmem-2",
        disk_size_gb: int = 100,
    ) -> None:
        """Launches a Vertex AI custom job to load the state dict.
    
        If the model is too large to fit into memory or disk, we can launch
        a Vertex AI custom job with a large enough VM for this to work.
    
        Depending on the model's size, it might require a different VM
        configuration. The model MUST fit into the VM's memory, and there
        must be enough disk space to stage the entire model while it gets
        copied to Cloud Storage.
    
        Args:
            model_name: HuggingFace model name compatible with AutoModelForSeq2SeqLM.
            state_dict_path: File path to the model's state_dict, can be in Cloud Storage.
            job_name: Job display name in the Vertex AI console.
            project: Google Cloud Project ID.
            bucket: Cloud Storage bucket name, without the "gs://" prefix.
            location: Google Cloud regional location.
            machine_type: Machine type for the VM to run the job.
            disk_size_gb: Disk size in GB for the VM to run the job.
        """
        from google.cloud import aiplatform
    
        aiplatform.[init](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.html)(project=project, staging_bucket=bucket, location=location)
    
        job = aiplatform.[CustomJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.CustomJob.html).from_local_script(
            display_name=job_name,
            container_uri="us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-13:latest",
            script_path="download_model.py",
            args=[
                "local",
                f"--model-name={model_name}",
                f"--state-dict-path={state_dict_path}",
            ],
            machine_type=machine_type,
            boot_disk_size_gb=disk_size_gb,
            requirements=["transformers"],
        )
        job.run()
    
    
    if __name__ == "__main__":
        import argparse
    
        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(required=True)
    
        parser_local = subparsers.add_parser("local")
        parser_local.add_argument(
            "--model-name",
            required=True,
            help="HuggingFace model name compatible with AutoModelForSeq2SeqLM",
        )
        parser_local.add_argument(
            "--state-dict-path",
            required=True,
            help="File path to the model's state_dict, can be in Cloud Storage",
        )
        parser_local.set_defaults(run=run_local)
    
        parser_vertex = subparsers.add_parser("vertex")
        parser_vertex.add_argument(
            "--model-name",
            required=True,
            help="HuggingFace model name compatible with AutoModelForSeq2SeqLM",
        )
        parser_vertex.add_argument(
            "--state-dict-path",
            required=True,
            help="File path to the model's state_dict, can be in Cloud Storage",
        )
        parser_vertex.add_argument(
            "--job-name", required=True, help="Job display name in the Vertex AI console"
        )
        parser_vertex.add_argument(
            "--project", required=True, help="Google Cloud Project ID"
        )
        parser_vertex.add_argument(
            "--bucket",
            required=True,
            help='Cloud Storage bucket name, without the "gs://" prefix',
        )
        parser_vertex.add_argument(
            "--location", default="us-central1", help="Google Cloud regional location"
        )
        parser_vertex.add_argument(
            "--machine-type",
            default="e2-highmem-2",
            help="Machine type for the VM to run the job",
        )
        parser_vertex.add_argument(
            "--disk-size-gb",
            type=int,
            default=100,
            help="Disk size in GB for the VM to run the job",
        )
        parser_vertex.set_defaults(run=run_vertex_job)
    
        args = parser.parse_args()
        kwargs = args.__dict__.copy()
        kwargs.pop("run")
    
        args.run(**kwargs)
    

### Pipeline code sample

The pipeline code in this tutorial deploys a Dataflow pipeline that does the following things:

  * Reads a prompt from Pub/Sub and encodes the text into token tensors.
  * Runs the `RunInference` transform.
  * Decodes the output token tensors into text and writes the response to Pub/Sub.



The starter file looks like the following:
    
    
    # Copyright 2023 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    """Runs a streaming RunInference Language Model pipeline."""
    
    from __future__ import annotations
    
    import logging
    
    import apache_beam as beam
    from apache_beam.ml.inference.base import PredictionResult
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.pytorch_inference import make_tensor_model_fn
    from apache_beam.ml.inference.pytorch_inference import PytorchModelHandlerTensor
    from apache_beam.options.pipeline_options import PipelineOptions
    import torch
    from transformers import AutoConfig
    from transformers import AutoModelForSeq2SeqLM
    from transformers import AutoTokenizer
    from transformers.tokenization_utils import PreTrainedTokenizer
    
    MAX_RESPONSE_TOKENS = 256
    
    
    def to_tensors(input_text: str, tokenizer: PreTrainedTokenizer) -> torch.Tensor:
        """Encodes input text into token tensors.
    
        Args:
            input_text: Input text for the language model.
            tokenizer: Tokenizer for the language model.
    
        Returns: Tokenized input tokens.
        """
        return tokenizer(input_text, return_tensors="pt").input_ids[0]
    
    
    def decode_response(result: PredictionResult, tokenizer: PreTrainedTokenizer) -> str:
        """Decodes output token tensors into text.
    
        Args:
            result: Prediction results from the RunInference transform.
            tokenizer: Tokenizer for the language model.
    
        Returns: The model's response as text.
        """
        output_tokens = result.inference
        return tokenizer.decode(output_tokens, skip_special_tokens=True)
    
    
    class AskModel(beam.PTransform):
        """Asks an language model a prompt message and gets its responses.
    
        Attributes:
            model_name: HuggingFace model name compatible with AutoModelForSeq2SeqLM.
            state_dict_path: File path to the model's state_dict, can be in Cloud Storage.
            max_response_tokens: Maximum number of tokens for the model to generate.
        """
    
        def __init__(
            self,
            model_name: str,
            state_dict_path: str,
            max_response_tokens: int = MAX_RESPONSE_TOKENS,
        ) -> None:
            self.model_handler = PytorchModelHandlerTensor(
                state_dict_path=state_dict_path,
                model_class=AutoModelForSeq2SeqLM.from_config,
                model_params={"config": AutoConfig.from_pretrained(model_name)},
                inference_fn=make_tensor_model_fn("generate"),
            )
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.max_response_tokens = max_response_tokens
    
        def expand(self, pcollection: beam.PCollection[str]) -> beam.PCollection[str]:
            return (
                pcollection
                | "To tensors" >> beam.Map(to_tensors, self.tokenizer)
                | "RunInference"
                >> RunInference(
                    self.model_handler,
                    inference_args={"max_new_tokens": self.max_response_tokens},
                )
                | "Get response" >> beam.Map(decode_response, self.tokenizer)
            )
    
    
    if __name__ == "__main__":
        import argparse
    
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--messages-topic",
            required=True,
            help="Pub/Sub topic for input text messages",
        )
        parser.add_argument(
            "--responses-topic",
            required=True,
            help="Pub/Sub topic for output text responses",
        )
        parser.add_argument(
            "--model-name",
            required=True,
            help="HuggingFace model name compatible with AutoModelForSeq2SeqLM",
        )
        parser.add_argument(
            "--state-dict-path",
            required=True,
            help="File path to the model's state_dict, can be in Cloud Storage",
        )
        args, beam_args = parser.parse_known_args()
    
        logging.getLogger().setLevel(logging.INFO)
        beam_options = PipelineOptions(
            beam_args,
            pickle_library="cloudpickle",
            streaming=True,
        )
    
        simple_name = args.model_name.split("/")[-1]
        pipeline = beam.Pipeline(options=beam_options)
        _ = (
            pipeline
            | "Read from Pub/Sub" >> beam.io.ReadFromPubSub(args.messages_topic)
            | "Decode bytes" >> beam.Map(lambda msg: msg.decode("utf-8"))
            | f"Ask {simple_name}" >> AskModel(args.model_name, args.state_dict_path)
            | "Encode bytes" >> beam.Map(lambda msg: msg.encode("utf-8"))
            | "Write to Pub/Sub" >> beam.io.WriteToPubSub(args.responses_topic)
        )
        pipeline.run()
    

## Load the model

LLMs can be very large models. Larger models that are trained with more parameters generally give better results. However, larger models require a bigger machine and more memory to run. Larger models can also be slower to run on CPUs.

Before you run a PyTorch model on Dataflow, you need to load the model's `state_dict` object. A model's [`state_dict` object](https://pytorch.org/tutorials/recipes/recipes/what_is_state_dict.html) stores the weights for the model.

In a Dataflow pipeline that uses the Apache Beam `RunInference` transform, the model's `state_dict` object must be loaded to Cloud Storage. The machine that you use to load the`state_dict` object to Cloud Storage needs to have enough memory to load the model. The machine also needs a fast internet connection to download the weights and to upload them to Cloud Storage.

The following table shows the number of parameters for each model and the minimum memory that's needed to load each model.

Model | Parameters | Memory needed  
---|---|---  
[`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small) | 80 million | > 320 MB  
[`google/flan-t5-base`](https://huggingface.co/google/flan-t5-base) | 250 million | > 1 GB  
[`google/flan-t5-large`](https://huggingface.co/google/flan-t5-large) | 780 million | > 3.2 GB  
[`google/flan-t5-xl`](https://huggingface.co/google/flan-t5-xl) | 3 billion | > 12 GB  
[`google/flan-t5-xxl`](https://huggingface.co/google/flan-t5-xxl) | 11 billion | > 44 GB  
[`google/flan-ul2`](https://huggingface.co/google/flan-ul2) | 20 billion | > 80 GB  
  
Although you can load a smaller model locally, this tutorial shows how to launch a Agent Platform custom job that loads the model with an appropriately sized VM.

Because LLMs can be so large, the example in this tutorial saves the `state_dict` object as `float16` format instead of the default `float32` format. With this configuration, each parameter uses 16 bits instead of 32 bits, making the `state_dict` object half the size. A smaller size minimizes the time that's needed to load the model. However, converting the format means that the VM has to fit both the model and the `state_dict` object into memory.

The following table shows the minimum requirements to load a model after the `state_dict` object is saved as `float16` format. The table also shows the suggested machine types to load a model by using Agent Platform. The minimum (and default) disk size for Agent Platform is 100 GB, but some models might require a larger disk.

Model name | Memory needed | Machine type | VM memory | VM disk  
---|---|---|---|---  
`google/flan-t5-small` | > 480 MB | `e2-standard-4` | 16 GB | 100 GB  
`google/flan-t5-base` | > 1.5 GB | `e2-standard-4` | 16 GB | 100 GB  
`google/flan-t5-large` | > 4.8 GB | `e2-standard-4` | 16 GB | 100 GB  
`google/flan-t5-xl` | > 18 GB | `e2-highmem-4` | 32 GB | 100 GB  
`google/flan-t5-xxl` | > 66 GB | `e2-highmem-16` | 128 GB | 100 GB  
`google/flan-ul2` | > 120 GB | `e2-highmem-16` | 128 GB | 150 GB  
  
Load the model's `state_dict` object into Cloud Storage by using a Agent Platform custom job:
    
    
    python download_model.py vertex \
        --model-name="MODEL_NAME" \
        --state-dict-path="gs://BUCKET_NAME/run-inference/MODEL_NAME.pt" \
        --job-name="Load MODEL_NAME" \
        --project="PROJECT_ID" \
        --bucket="BUCKET_NAME" \
        --location="LOCATION" \
        --machine-type="AGENT_PLATFORM_MACHINE_TYPE" \
        --disk-size-gb="DISK_SIZE_GB"
    

Replace the following:

  * MODEL_NAME: the name of the model, such as `google/flan-t5-xl`.
  * AGENT_PLATFORM_MACHINE_TYPE: the type of machine to run the Agent Platform custom job on, such as `e2-highmem-4`.
  * DISK_SIZE_GB: the disk size for the VM, in GB. The minimum size is 100 GB.



Depending on the size of the model, it might take a few minutes to load the model. To view the status, go to the Agent Platform **Custom jobs** page.

[Go to Custom jobs](https://console.cloud.google.com/vertex-ai/training/custom-jobs)

## Run the pipeline

After you load the model, you run the Dataflow pipeline. To run the pipeline, both the model and the memory used by each worker must fit into memory.

The following table shows the recommended machine types to run an inference pipeline.

Model name | Machine type | VM memory  
---|---|---  
`google/flan-t5-small` | `n2-highmem-2` | 16 GB  
`google/flan-t5-base` | `n2-highmem-2` | 16 GB  
`google/flan-t5-large` | `n2-highmem-4` | 32 GB  
`google/flan-t5-xl` | `n2-highmem-4` | 32 GB  
`google/flan-t5-xxl` | `n2-highmem-8` | 64 GB  
`google/flan-ul2` | `n2-highmem-16` | 128 GB  
  
Run the pipeline:
    
    
    python main.py \
        --messages-topic="projects/PROJECT_ID/topics/PROMPTS_TOPIC_ID" \
        --responses-topic="projects/PROJECT_ID/topics/RESPONSES_TOPIC_ID" \
        --model-name="MODEL_NAME" \
        --state-dict-path="gs://BUCKET_NAME/run-inference/MODEL_NAME.pt" \
        --runner="DataflowRunner" \
        --project="PROJECT_ID" \
        --temp_location="gs://BUCKET_NAME/temp" \
        --region="REGION" \
        --machine_type="DATAFLOW_MACHINE_TYPE" \
        --requirements_file="requirements.txt" \
        --requirements_cache="skip" \
        --experiments="use_sibling_sdk_workers" \
        --experiments="no_use_multiple_sdk_containers"
    

Replace the following:

  * PROJECT_ID: the project ID
  * PROMPTS_TOPIC_ID: the topic ID for the input prompts to send to the model
  * RESPONSES_TOPIC_ID: the topic ID for the model's responses
  * MODEL_NAME: the name of the model, such as `google/flan-t5-xl`
  * BUCKET_NAME: the name of the bucket
  * REGION: the region to deploy the job in, such as `us-central1`
  * DATAFLOW_MACHINE_TYPE: the VM to run the pipeline on, such as `n2-highmem-4`



To ensure that the model is loaded only once per worker and doesn't run out of memory, you configure workers to use a single process by setting the pipeline option `--experiments=no_use_multiple_sdk_containers`. You don't have to limit the number of threads because the `RunInference` transform shares the same model with multiple threads.

The pipeline in this example runs with CPUs. For a larger model, more time is required to process each request. You can [enable GPUs](https://docs.cloud.google.com/dataflow/docs/concepts/gpu-support) if you need faster responses.

To view the status of the pipeline, go to the Dataflow **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

## Ask the model a question

After the pipeline starts running, you provide a prompt to the model and receive a response.

  1. Send your prompt by publishing a message to Pub/Sub. Use the [`gcloud pubsub topics publish` command](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish):
         
         gcloud pubsub topics publish PROMPTS_TOPIC_ID \
             --message="PROMPT_TEXT"
         

Replace `PROMPT_TEXT` with a string that contains the prompt that you want to provide. Surround the prompt with quotation marks.

Use your own prompt, or try one of the following examples:

     * `Translate to Spanish: My name is Luka`
     * `Complete this sentence: Once upon a time, there was a`
     * `Summarize the following text: Dataflow is a Google Cloud service that provides unified stream and batch data processing at scale. Use Dataflow to create data pipelines that read from one or more sources, transform the data, and write the data to a destination.`
  2. To get the response, use the [`gcloud pubsub subscriptions pull` command](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull).

Depending on the size of the model, it might take a few minutes for the model to generate a response. Larger models take longer to deploy and to generate a response.
         
         gcloud pubsub subscriptions pull RESPONSES_SUBSCRIPTION_ID --auto-ack
         

Replace `RESPONSES_SUBSCRIPTION_ID` with the subscription ID for the model's responses.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

  1. Exit the Python virtual environment:
         
         deactivate

  2. Stop the pipeline:

     1. List the job IDs for the Dataflow jobs that are running, and then note the job ID for the tutorial's job:
            
            gcloud dataflow jobs list --region=REGION --status=active

     2. Cancel the job:
            
            gcloud dataflow jobs cancel JOB_ID --region=REGION

  3. Delete the bucket and anything inside of it:
         
         gcloud storage rm gs://BUCKET_NAME --recursive

  4. Delete the topics and the subscription:
         
         gcloud pubsub topics delete PROMPTS_TOPIC_ID
         gcloud pubsub topics delete RESPONSES_TOPIC_ID
         gcloud pubsub subscriptions delete RESPONSES_SUBSCRIPTION_ID

  5. Revoke the roles that you granted to the Compute Engine default service account. Run the following command once for each of the following IAM roles:

     * `roles/dataflow.admin`
     * `roles/dataflow.worker`
     * `roles/storage.admin`
     * `roles/pubsub.editor`
     * `roles/aiplatform.user`
    
    gcloud projects remove-iam-policy-binding PROJECT_ID --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com --role=SERVICE_ACCOUNT_ROLE

  6. Optional: Revoke roles from your Google Account.
         
         gcloud projects remove-iam-policy-binding PROJECT_ID --member="user:EMAIL_ADDRESS" --role=roles/iam.serviceAccountUser

  7. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  8. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * [Explore Dataflow ML](https://docs.cloud.google.com/dataflow/docs/machine-learning).
  * Learn more about the [RunInference API](https://beam.apache.org/documentation/ml/about-ml/).
  * Get in-depth information about using ML with Apache Beam in the Apache Beam [AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) documentation.
  * Work through the notebook [Use RunInference for Generative AI](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_generative_ai).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
