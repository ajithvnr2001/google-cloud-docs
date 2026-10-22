---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-llm-l4-ray/
title: Serve an LLM on L4 GPUs with Ray \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:56.416583+00:00
---

# Serve an LLM on L4 GPUs with Ray  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-llm-l4-ray/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve an LLM on L4 GPUs with Ray Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This guide demonstrates how to serve large language models (LLM) using Ray and the Ray Operator add-on with Google Kubernetes Engine (GKE). The [Ray framework](https://www.ray.io/) provides an end-to-end AI/ML platform for training, fine-training, and inferencing of machine learning workloads. Ray Serve is a framework in Ray that you can use to serve popular LLMs from Hugging Face.

Before reading this guide, ensure that you're familiar with the model that you want to serve in this tutorial. You can serve any of the following models:

  * [Gemma 2B IT](https://huggingface.co/google/gemma-2b-it)
  * [Gemma 7B IT](https://huggingface.co/google/gemma-7b-it)
  * [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
  * [Llama 3 8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
  * [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)

**Note:** We don't recommend using base models like Llama 3 8B for production chatbots due to safety concerns. For more information about best practices, see [System instructions for safety](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/safety-system-instructions).

This page is intended for Machine learning (ML) engineers and Platform admins and operators who facilitate ML workloads. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This guide covers the following steps:

  1. Create an Autopilot or Standard GKE cluster with the [Ray Operator add-on](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview) enabled.
  2. Deploy a RayService resource that downloads and serves a large language model (LLM) from Hugging Face.
  3. Deploy a chat interface and dialog with LLMs.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Create a [Hugging Face](https://huggingface.co/) account, if you don't already have one.
  * Ensure that you have a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).
  * Ensure that you have access to the Hugging Face model that you want to use. This is usually granted by signing an agreement and requesting access from the model owner on the Hugging Face model page.
  * Ensure that you have GPU quota in the `us-central1` region. To learn more, see [GPU quota](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus#gpu-quota).



## Prepare your environment

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Clone the sample repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         cd kubernetes-engine-samples/ai-ml/gke-ray/rayserve/llm
         export TUTORIAL_HOME=`pwd`
         

  3. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         export PROJECT_ID=$(gcloud config get project)
         export COMPUTE_REGION=us-central1
         export CLUSTER_VERSION=CLUSTER_VERSION
         export HF_TOKEN=HUGGING_FACE_TOKEN
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `CLUSTER_VERSION`: the GKE version to use. Must be `1.30.1` or later.
     * `HUGGING_FACE_TOKEN`: your Hugging Face access token.



## Create a cluster with a GPU node pool

You can serve an LLM on L4 GPUs with Ray in a GKE Autopilot or Standard cluster using the Ray Operator add-on. We generally recommend that you use an Autopilot cluster for a fully managed Kubernetes experience. Choose a Standard cluster instead if your use case requires high scalability or if you want more control over cluster configuration. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

Use Cloud Shell to create an Autopilot or Standard cluster:

###  Autopilot 

Create an Autopilot cluster with the Ray Operator add-on enabled:
    
    
    gcloud container clusters create-auto rayserve-cluster \
        --enable-ray-operator \
        --cluster-version=${CLUSTER_VERSION} \
        --location=${COMPUTE_REGION}
    

###  Standard 

Create a Standard cluster with the Ray Operator add-on enabled:
    
    
    gcloud container clusters create rayserve-cluster \
        --addons=RayOperator \
        --cluster-version=${CLUSTER_VERSION} \
        --machine-type=g2-standard-24 \
        --location=${COMPUTE_ZONE} \
        --num-nodes=2 \
        --accelerator type=nvidia-l4,count=2,gpu-driver-version=latest
    

## Create a Kubernetes Secret for Hugging Face credentials

In Cloud Shell, create a Kubernetes Secret by doing the following:

  1. Configure `kubectl` to communicate with your cluster:
         
         gcloud container clusters get-credentials ${CLUSTER_NAME} --location=${COMPUTE_REGION}
         

  2. Create a Kubernetes Secret that contains the Hugging Face token:
         
         kubectl create secret generic hf-secret \
           --from-literal=hf_api_token=${HF_TOKEN} \
           --dry-run=client -o yaml | kubectl apply -f -
         




## Deploy the LLM model

The GitHub repository that you cloned has a directory for each model that includes a RayService configuration. The configuration for each model includes the following components:

  * Ray Serve deployment: The Ray Serve deployment, which includes resource configuration and runtime dependencies.
  * Model: The Hugging Face model ID.
  * Ray cluster: The underlying Ray cluster and the resources required for each component, which includes head and worker Pods.




###  Gemma 2B IT

  1. Deploy the model:
         
         kubectl apply -f gemma-2b-it/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice gemma-2b-it -o yaml
         

The output is similar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T02:51:52Z"
                 serveDeploymentStatuses:
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T02:51:52Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm that GKE created the Service for the Ray Serve application:
         
         kubectl get service gemma-2b-it-serve-svc
         

The output is similar to the following:
         
         NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         gemma-2b-it-serve-svc   ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         




###  Gemma 7B IT

  1. Deploy the model:
         
         kubectl apply -f gemma-7b-it/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice gemma-7b-it -o yaml
         

The output is similar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T02:51:52Z"
                 serveDeploymentStatuses:
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T02:51:52Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm that GKE created the Service for the Ray Serve application:
         
         kubectl get service gemma-7b-it-serve-svc
         

The output is similar to the following:
         
         NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         gemma-7b-it-serve-svc   ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         




### Llama 2 7B

  1. Deploy the model:
         
         kubectl apply -f llama-2-7b/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice llama-2-7b -o yaml
         

The output is similar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T02:51:52Z"
                 serveDeploymentStatuses:
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T02:51:52Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm that GKE created the Service for the Ray Serve application:
         
         kubectl get service llama-2-7b-serve-svc
         

The output is similar to the following:
         
         NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         llama-2-7b-serve-svc    ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         




### Llama 3 8B

  1. Deploy the model:
         
         kubectl apply -f llama-3-8b/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice llama-3-8b -o yaml
         

The output is similar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T02:51:52Z"
                 serveDeploymentStatuses:
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T02:51:52Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm that GKE created the Service for the Ray Serve application:
         
         kubectl get service llama-3-8b-serve-svc
         

The output is similar to the following:
         
         NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         llama-3-8b-serve-svc    ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         




### Mistral 7B

  1. Deploy the model:
         
         kubectl apply -f mistral-7b/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice mistral-7b -o yaml
         

The output is similar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T02:51:52Z"
                 serveDeploymentStatuses:
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T02:51:52Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm that GKE created the Service for the Ray Serve application:
         
         kubectl get service mistral-7b-serve-svc
         

The output is similar to the following:
         
         NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         mistral-7b-serve-svc    ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         




## Serve the model

The Llama2 7B and Llama3 8B models use the [OpenAI API chat spec](https://platform.openai.com/docs/guides/text-generation). The other models only support text generation, which is a technique that generates text based on a prompt.

### Set up port-forwarding

Set up port forwarding to the inferencing server:

###  Gemma 2B IT
    
    
    kubectl port-forward svc/gemma-2b-it-serve-svc 8000:8000
    

###  Gemma 7B IT
    
    
    kubectl port-forward svc/gemma-7b-it-serve-svc 8000:8000
    

### Llama2 7B
    
    
    kubectl port-forward svc/llama-7b-serve-svc 8000:8000
    

### Llama 3 8B
    
    
    kubectl port-forward svc/llama-3-8b-serve-svc 8000:8000
    

### Mistral 7B
    
    
    kubectl port-forward svc/mistral-7b-serve-svc 8000:8000
    

### Interact with the model using curl

Use curl to chat with your model:

###  Gemma 2B IT

In a new terminal session:
    
    
    curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Be brief.", "max_tokens": 1024}'
    

###  Gemma 7B IT

In a new terminal session:
    
    
    curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Be brief.", "max_tokens": 1024}'
    

### Llama2 7B

In a new terminal session:
    
    
    curl http://localhost:8000/v1/chat/completions     -H "Content-Type: application/json"     -d '{
          "model": "meta-llama/Llama-2-7b-chat-hf",
          "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are the top 5 most popular programming languages? Please be brief."}
          ],
          "temperature": 0.7
        }'
    

### Llama 3 8B

In a new terminal session:
    
    
    curl http://localhost:8000/v1/chat/completions     -H "Content-Type: application/json"     -d '{
          "model": "meta-llama/Meta-Llama-3-8B-Instruct",
          "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are the top 5 most popular programming languages? Please be brief."}
          ],
          "temperature": 0.7
        }'
    

### Mistral 7B

In a new terminal session:
    
    
    curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Be brief.", "max_tokens": 1024}'
    

Because the models that you served don't retain any history, each message and reply must be sent back to the model to create an interactive dialogue experience. The follow example shows how you can create an interactive dialogue using the Llama 3 8B model:

Create a dialogue with the model using `curl`:
    
    
    curl http://localhost:8000/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d '{
          "model": "meta-llama/Meta-Llama-3-8B-Instruct",
          "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are the top 5 most popular programming languages? Please be brief."},
            {"role": "assistant", "content": " \n1. Java\n2. Python\n3. C++\n4. C#\n5. JavaScript"},
            {"role": "user", "content": "Can you give me a brief description?"}
          ],
          "temperature": 0.7
    }'
    

The output is similar to the following:
    
    
    {
      "id": "cmpl-3cb18c16406644d291e93fff65d16e41",
      "object": "chat.completion",
      "created": 1719035491,
      "model": "meta-llama/Meta-Llama-3-8B-Instruct",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "Here's a brief description of each:\n\n1. **Java**: A versatile language for building enterprise-level applications, Android apps, and web applications.\n2. **Python**: A popular language for data science, machine learning, web development, and scripting, known for its simplicity and ease of use.\n3. **C++**: A high-performance language for building operating systems, games, and other high-performance applications, with a focus on efficiency and control.\n4. **C#**: A modern, object-oriented language for building Windows desktop and mobile applications, as well as web applications using .NET.\n5. **JavaScript**: A versatile language for client-side scripting on the web, commonly used for creating interactive web pages, web applications, and mobile apps.\n\nNote: These descriptions are brief and don't do justice to the full capabilities and uses of each language."
          },
          "logprobs": null,
          "finish_reason": "stop",
          "stop_reason": null
        }
      ],
      "usage": {
        "prompt_tokens": 73,
        "total_tokens": 245,
        "completion_tokens": 172
      }
    }
    

### (Optional) Connect to the chat interface

You can use Gradio to build web applications that let you interact with your model. Gradio is a Python library that has a `ChatInterface` wrapper that creates user interfaces for chatbots. For Llama 2 7B and Llama 3 7B, you installed Gradio when you deployed the LLM model.

  1. Set up port-forwarding to the `gradio` Service:
         
         kubectl port-forward service/gradio 8080:8080 &
         

  2. Open http://localhost:8080 in your browser to chat with the model.




## Serve multiple models with model multiplexing

[Model multiplexing](https://docs.ray.io/en/latest/serve/model-multiplexing.html) is a technique used to serve multiple models within the same Ray cluster. You can route traffic to specific models using request headers or by load balancing.

In this example, you create a multiplexed Ray Serve application consisting of two models: Gemma 7B IT and Llama 3 8B.

**Warning:** This section uses 4 GPUs. Ensure you have enough GPU capacity in your cluster.

  1. Deploy the RayService resource:
         
         kubectl apply -f model-multiplexing/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice model-multiplexing -o yaml
         

The output is simlar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T14:00:41Z"
                 serveDeploymentStatuses:
                   MutliModelDeployment:
                     healthLastUpdateTime: "2024-06-22T14:00:41Z"
                     status: HEALTHY
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T14:00:41Z"
                     status: HEALTHY
                   VLLMDeployment_1:
                     healthLastUpdateTime: "2024-06-22T14:00:41Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm GKE created the Kubernetes Service for the Ray Serve application:
         
         kubectl get service model-multiplexing-serve-svc
         

The output is similar to the following:
         
         NAME                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         model-multiplexing-serve-svc   ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         

  4. Set up port-forwarding to the Ray Serve application:
         
         kubectl port-forward svc/model-multiplexing-serve-svc 8000:8000
         

  5. Send a request to the Gemma 7B IT model:
         
         curl -X POST http://localhost:8000/ -H "Content-Type: application/json" --header "serve_multiplexed_model_id: google/gemma-7b-it" -d '{"prompt": "What are the top 5 most popular programming languages? Please be brief.", "max_tokens": 200}'
         

The output is similar to the following:
         
         {"text": ["What are the top 5 most popular programming languages? Please be brief.\n\n1. JavaScript\n2. Java\n3. C++\n4. Python\n5. C#"]}
         

  6. Send a request to the Llama 3 8B model:
         
         curl -X POST http://localhost:8000/ -H "Content-Type: application/json" --header "serve_multiplexed_model_id: meta-llama/Meta-Llama-3-8B-Instruct" -d '{"prompt": "What are the top 5 most popular programming languages? Please be brief.", "max_tokens": 200}'
         

The output is similar to the following:
         
         {"text": ["What are the top 5 most popular programming languages? Please be brief. Here are your top 5 most popular programming languages, based on the TIOBE Index, a widely used measure of the popularity of programming languages.\r\n\r\n1. **Java**: Used in Android app development, web development, and enterprise software development.\r\n2. **Python**: A versatile language used in data science, machine learning, web development, and automation.\r\n3. **C++**: A high-performance language used in game development, system programming, and high-performance computing.\r\n4. **C#**: Used in Windows and web application development, game development, and enterprise software development.\r\n5. **JavaScript**: Used in web development, mobile app development, and server-side programming with technologies like Node.js.\r\n\r\nSource: TIOBE Index (2022).\r\n\r\nThese rankings can vary depending on the source and methodology used, but this gives you a general idea of the most popular programming languages."]}
         

  7. Send a request to a random model by excluding the header `serve_multiplexed_model_id`:
         
         curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"prompt": "What are the top 5 most popular programming languages? Please be brief.", "max_tokens": 200}'
         

The output is one of the outputs from the previous steps.




## Compose multiple models with model composition

[Model composition](https://docs.ray.io/en/latest/serve/model_composition.html) is a technique used to compose multiple models into a single application. Model composition lets you chain together inputs and outputs across multiple LLMs and scale your models as a single application.

In this example, you compose two models, Gemma 7B IT and Llama 3 8B, into a single application. The first model is the assistant model that answers questions provided in the prompt. The second model is the summarizer model. The output of the assistant model is chained into the input of the summarizer model. The final result is the summarized version of the response from the assistant model.

**Warning:** This section uses 4 GPUs. Ensure you have enough GPU capacity in your cluster.

  1. Deploy the RayService resource:
         
         kubectl apply -f model-composition/
         

  2. Wait for the RayService resource to be ready:
         
         kubectl get rayservice model-composition -o yaml
         

The output is simlar to the following:
         
         status:
           activeServiceStatus:
             applicationStatuses:
               llm:
                 healthLastUpdateTime: "2024-06-22T14:00:41Z"
                 serveDeploymentStatuses:
                   MutliModelDeployment:
                     healthLastUpdateTime: "2024-06-22T14:00:41Z"
                     status: HEALTHY
                   VLLMDeployment:
                     healthLastUpdateTime: "2024-06-22T14:00:41Z"
                     status: HEALTHY
                   VLLMDeployment_1:
                     healthLastUpdateTime: "2024-06-22T14:00:41Z"
                     status: HEALTHY
                 status: RUNNING
         

In this output, `status: RUNNING` indicates the RayService resource is ready.

  3. Confirm GKE created the Service for the Ray Serve application:
         
         kubectl get service model-composition-serve-svc
         

The output is similar to the following:
         
         NAME                           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
         model-composition-serve-svc    ClusterIP   34.118.226.104   <none>        8000/TCP   45m
         

  4. Send a request to the model:
         
         curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"prompt": "What is the most popular programming language for machine learning and why?", "max_tokens": 1000}'
         

  5. The output is similar to the following:
         
         {"text": ["\n\n**Sure, here is a summary in a single sentence:**\n\nThe most popular programming language for machine learning is Python due to its ease of use, extensive libraries, and growing community."]}
         




### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resources

If you used an existing project and you don't want to delete it, you can delete the individual resources.

  1. Delete the cluster:
         
         gcloud container clusters delete rayserve-cluster
         




## What's next

  * Discover how to run optimized AI/ML workloads with [GKE platform orchestration capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * [Train a model with GPUs on GKE Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/train-model-gpus-standard)
  * Learn how to use RayServe on GKE, by viewing the [sample code in GitHub](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/gke-ray/rayserve).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
