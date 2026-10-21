---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vllm/
title: Deploy an agentic AI application on GKE with the Agent Development Kit (ADK) and a self-hosted LLM \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:47.998870+00:00
---

# Deploy an agentic AI application on GKE with the Agent Development Kit (ADK) and a self-hosted LLM  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vllm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Deploy an agentic AI application on GKE with the Agent Development Kit (ADK) and a self-hosted LLM Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This tutorial demonstrates a legacy approach that executes agentic AI application code in standard, un-isolated Pods. To isolate untrusted code from your host kernel and internal, refer to our [Deploying Secure AI Agents on GKE](https://codelabs.developers.google.com/codelabs/gke/ai-agents-on-gke), [Code Generation Agent on GKE](https://codelabs.developers.google.com/next26/code-generation-agent-gke), and [High-Performance Distributed Reinforcement Learning on GKE](https://codelabs.developers.google.com/codelabs/gke/high-performance-distributed-rl-sandbox) codelabs instead.

This tutorial demonstrates how to deploy and manage containerized agentic AI/ML applications by using Google Kubernetes Engine (GKE). By combining the Google Agent Development Kit (ADK) with a self-hosted large language model (LLM) like Llama 3.1 served by vLLM, you can operationalize AI agents efficiently and at scale while maintaining full control over the model stack. This tutorial walks you through the end-to-end process of taking a Python-based agent from development to production deployment on a GKE Autopilot cluster with GPU acceleration.

This tutorial is intended for Machine learning (ML) engineers, Developers, and Cloud architects who are interested in using Kubernetes container orchestration capabilities for serving agentic AI/ML applications. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

**Note:** The approach in this tutorial requires provisioning a GKE cluster with GPU hardware to run the LLM, which is different from the Vertex AI approach, where model inference is handled by Google's managed infrastructure. For more information about the Vertex AI approach, see [Deploy an agentic AI application on GKE with the ADK and Vertex AI](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex).

Before you begin, ensure you are familiar with the following:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [Containerization with Docker](https://www.cloudskillsboost.google/focuses/1029?parent=catalog)



## Background

This section describes the key technologies used in this tutorial.

### Agent Development Kit (ADK)

Agent Development Kit (ADK) is a flexible and modular framework for developing and deploying AI agents. Although it's optimized for Gemini and the Google ecosystem, ADK doesn't require you to use a specific model or deployment, and is built for compatibility with other frameworks. ADK was designed to make agent development feel more like software development, to make it easier for developers to create, deploy, and orchestrate agentic architectures that range from basic tasks to complex workflows.

For more information, see the [ADK documentation](https://google.github.io/adk-docs/).

### GKE managed Kubernetes service

Google Cloud offers a range of services, including GKE, which is well-suited to deploying and managing AI/ML workloads. GKE is a managed Kubernetes service that simplifies deploying, scaling, and managing containerized applications. GKE provides the necessary infrastructure—including scalable resources, distributed computing, and efficient networking—to handle the computational demands of LLMs.

For more information about key Kubernetes concepts, see [Start learning about Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes). For more information about the GKE and how it helps you scale, automate, and manage Kubernetes, see [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

### vLLM

vLLM is a highly optimized open source LLM serving framework that can increase serving throughput on GPUs, with features such as the following:

  * Optimized transformer implementation with [PagedAttention](https://huggingface.co/docs/text-generation-inference/en/conceptual/paged_attention).
  * Continuous batching to improve the overall serving throughput.
  * Tensor parallelism and distributed serving on multiple GPUs.



For more information, see the [vLLM documentation](https://docs.vllm.ai/en/latest/).

## Objectives

This tutorial shows you how to do the following:

  1. Set up your Google Cloud environment.
  2. Provision a GPU-enabled GKE cluster.
  3. Deploy a Llama 3.1 model by using the vLLM inference server.
  4. Build a container image for your ADK-based agent.
  5. Deploy the agent to the GKE cluster and connect it to the self-hosted LLM.
  6. Test your deployed agent.



## Architecture

This tutorial presents a scalable architecture for deploying agentic AI applications on GKE. The ADK agent application runs on a standard CPU node pool and the self-hosted LLM (Llama 3.1 on vLLM) runs on a GPU-enabled node pool, both within the same GKE cluster. This architecture separates the agent's application logic from the LLM inference workload, which allows each component to be scaled and managed independently.

![This diagram illustrates a scalable architecture for deploying agentic AI applications on GKE, separating the agent's application logic from the large language model \(LLM\) inference workload for independent scaling and management. The architecture consists of two core components: the ADK agent application running on a standard CPU node pool and the self-hosted LLM \(Llama 3.1 on vLLM\) running on a GPU-enabled node pool, both within the same GKE cluster.](https://docs.cloud.google.com/static/kubernetes-engine/images/adk-vllm-architecture.svg)**Figure 1** : A scalable architecture for deploying agentic AI on GKE.

The architecture has two core components, each on its own GKE Deployment:

  * **ADK agent application** : your agent's custom-built business logic and tools (like `get_weather`) are in a container image. The image runs on a standard CPU node pool and communicates with the LLM using an internal Kubernetes service.

  * **Self-hosted LLM (Llama 3.1 on vLLM)** : the Llama 3.1 model runs on a dedicated vLLM server on a GPU-enabled node pool. This deployment uses a public container image (`vllm/vllm-openai:v0.8.5`) that's configured to download and serve the specified model from Hugging Face when the container starts. The agent communicates with this server through a REST API exposed by the `vllm-llama3-service` Kubernetes service.




Both the ADK agent and the vLLM deployments run on the same GKE cluster. This colocation within a single cluster simplifies networking, management, and deployment while still allowing for specialized hardware assignment for components of the application.

## Costs

This tutorial uses the following billable components of Google Cloud:

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/pricing)
  * [Cloud Build](https://cloud.google.com/build/pricing)



Review the pricing for each service to understand potential costs.

## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,iam.googleapis.com)

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Enable the required APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,artifactregistry.googleapis.com,cloudbuild.googleapis.com,iam.googleapis.com)

  * Make sure that you have the following role or roles on the project: roles/container.admin, roles/iam.serviceAccountAdmin, roles/artifactregistry.admin, roles/cloudbuild.builds.editor, roles/resourcemanager.projectIamAdmin 

#### Check for the roles

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

    4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

    1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
    2. Select the project. 
    3. Click person_add **Grant access**. 
    4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

    5. Click **Select a role** , then search for the role. 
    6. To grant additional roles, click add **Add another role** and add each additional role. 
    7. Click **Save**. 
  * Obtain a [read-access token from Hugging Face](https://huggingface.co/docs/hub/en/security-tokens) to download the Llama model. You also need to request access to the [Llama 3.1 model](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct). 



## Prepare the environment

This tutorial uses Cloud Shell to manage resources hosted on Google Cloud. Cloud Shell comes preinstalled with the software you need for this tutorial, including `kubectl`, `terraform`, and the `Google Cloud CLI`.

To set up your environment with Cloud Shell, follow these steps:

  1. In the Google Cloud console, launch a Cloud Shell session and click ![Cloud Shell activation icon](https://docs.cloud.google.com/static/shell/docs/images/activate_cloud_shell.svg)**Activate Cloud Shell**. This action launches a session in a Google Cloud console pane.
  2. Set the default environment variables:
         
         gcloud config set project PROJECT_ID
         export GOOGLE_CLOUD_REGION=REGION
         export PROJECT_ID=PROJECT_ID
         

Replace the following values:

     * PROJECT_ID: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * REGION: the Google Cloud region (for example, `us-east4`) to provision your GKE cluster, Artifact Registry, and other regional resources. Make sure to specify a region that supports L4 GPUs and G2 machine type instances. To check for region availability, see [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) in the Compute Engine documentation.



### Clone the sample project

  1. From your Cloud Shell terminal, clone the tutorial's sample code repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         

  2. Navigate to the tutorial directory:
         
         cd kubernetes-engine-samples/ai-ml/adk-vllm
         




### Create and configure Google Cloud resources

To deploy your agent, you first need to provision the necessary Google Cloud resources. You can create the GKE cluster and Artifact Registry repository using either the gcloud CLI or Terraform.

### gcloud

This section provides gcloud CLI commands to set up your GKE cluster and Artifact Registry.

  1. **Create a GKE cluster** : You can deploy your containerized agentic application in a GKE Autopilot or Standard cluster. Use an Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that best fits your workloads, see [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

In Cloud Shell, run the following command:
         
         gcloud container clusters create-auto CLUSTER_NAME \
             --location=$GOOGLE_CLOUD_REGION
         

Replace CLUSTER_NAME with the name of your GKE cluster.

With Autopilot, GKE automatically provisions nodes based on your workload's resource requests. The GPU required for the LLM is requested in the `deploy-llm.yaml` manifest by using a `nodeSelector`.

To add a `nodeSelector` request the `nvidia-l4` GPU, follow these steps:

     1. Open `kubernetes-engine-samples/ai-ml/adk-vllm/deploy-llm/deploy-llm.yaml` in an editor.
     2. Add the following `nodeSelector` under `spec.template.spec`:
            
            nodeSelector:
            cloud.google.com/gke-accelerator: nvidia-l4
            

### Standard

     1. In Cloud Shell, create a Standard cluster by running the following command:
            
            gcloud container clusters create CLUSTER_NAME \
                --location=$GOOGLE_CLOUD_REGION
            

Replace CLUSTER_NAME with the name of your GKE cluster.

     2. Create a GPU-enabled [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) for your cluster by running the following command:
            
            gcloud container node-pools create gpu-node-pool \
                --cluster=CLUSTER_NAME \
                --location=$GOOGLE_CLOUD_REGION \
                --machine-type=g2-standard-8 \
                --accelerator=type=nvidia-l4,count=1 \
                --enable-gvnic
            

The `deploy-llm.yaml` file specifies an `nvidia-l4` GPU, which is available in the G2 machine series. For more information about this machine type, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus#h100-gpus) in the Compute Engine documentation.

  2. **Create an Artifact Registry repository** : Create an Artifact Registry repository to securely store and manage your agent's Docker container image.
         
         gcloud artifacts repositories create REPO_NAME \
             --repository-format=docker \
             --location=$GOOGLE_CLOUD_REGION
         

Replace REPO_NAME with the name of the Artifact Registry repository you want to use (for example, `adk-repo`).

  3. **Get the repository URL** : To verify the full path to your repository, run this command. You'll use this format to tag your Docker image when you build the agent image.
         
         gcloud artifacts repositories describe REPO_NAME \
             --location $GOOGLE_CLOUD_REGION
         




### Terraform

This section describes how to use the Terraform configuration included in the sample repository to provision your Google Cloud resources automatically.

  1. **Navigate to the Terraform directory** : The `\terraform` directory contains all the necessary configuration files to create the GKE cluster and other required resources.
         
         cd terraform
         

  2. **Create a Terraform variables file** : Copy the provided example variables file (`example_vars.tfvars`) to create your own `vars.tfvars` file.
         
         cp example_vars.tfvars vars.tfvars
         

Open the `vars.tfvars` file in an editor and replace the placeholder values with your specific configuration. At a minimum, you must replace PROJECT_ID with your Google Cloud project ID and CLUSTER_NAME with the name of your GKE cluster.

  3. **Initialize Terraform** : To download the necessary provider plugins for Google Cloud, run this command.
         
         terraform init
         

  4. **Review the execution plan** : This command shows the infrastructure changes Terraform will make.
         
         terraform plan -var-file=vars.tfvars
         

  5. **Apply the configuration** : To create the resources in your Google Cloud project, execute the Terraform plan. Confirm with `yes` when prompted.
         
         terraform apply -var-file=vars.tfvars
         




After you run these commands, Terraform provisions your GKE cluster and Artifact Registry repository, and configures the necessary IAM roles and service accounts, including Workload Identity Federation for GKE.

To learn more about using Terraform, see [Provision GKE resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Configure `kubectl` to communicate with your cluster

To configure `kubectl` to communicate with your cluster, run the following command:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --location=${GOOGLE_CLOUD_REGION}
    

Replace CLUSTER_NAME with the name of your GKE cluster.

## Build the agent image

After you create the infrastructure using either gcloud CLI or Terraform, follow these steps to build your agent application.

  1. **Grant the required IAM role for Cloud Build** : The Cloud Build service requires permissions to push the agent's container image to Artifact Registry. Grant the `roles/artifactregistry.writer` role to the Compute Engine default service account, which is used by Cloud Build.

     1. Construct the email for the Compute Engine default service account:
            
            export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
            export COMPUTE_SA_EMAIL=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
            

     2. Grant the `roles/artifactregistry.writer` role to the service account:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
                --member=serviceAccount:${COMPUTE_SA_EMAIL} \
                --role=roles/artifactregistry.writer
            

  2. **Build and push the agent container image** : From the project root directory (`adk/llama/vllm`), build your Docker image and push it to your Artifact Registry by running these commands.
         
         export IMAGE_URL="${GOOGLE_CLOUD_REGION}-docker.pkg.dev/${PROJECT_ID}/REPO_NAME/adk-agent:latest"
         gcloud builds submit --tag $IMAGE_URL
         

  3. **Verify that the image has been pushed** : After the build process completes successfully, verify that your agent's container image was pushed to Artifact Registry by listing the images in your repository.
         
         gcloud artifacts docker images list ${GOOGLE_CLOUD_REGION}-docker.pkg.dev/${PROJECT_ID}/REPO_NAME
         

You should see an output that lists the image you just pushed and tagged as `latest`.




## Deploy the model

After setting up your GKE cluster and building the agent image, the next step is to deploy the self-hosted Llama 3.1 model to your cluster. To do this, deploy a pre-configured vLLM inference server that pulls the model from Hugging Face and serves it internally within the cluster.

  1. **Create a Kubernetes secret for Hugging Face credentials** : To allow the GKE cluster to download the gated Llama 3.1 model, you must provide your [Hugging Face token](https://huggingface.co/docs/hub/security-tokens) as a Kubernetes secret. The `deploy-llm.yaml` manifest is configured to use this secret for authentication.
         
         kubectl create secret generic hf-secret \
             --from-literal=hf-token-secret=HUGGING_FACE_TOKEN
         

Replace HUGGING_FACE_TOKEN with your token.

  2. **View the manifest** : From your project root directory (`adk/llama/vllm`), navigate to the `/deploy-llm` directory that contains the model Deployment manifest.
         
         cd deploy-llm
         

  3. **Apply the manifest** : Run the following command to apply the `deploy-llm.yaml` manifest to your cluster.
         
         kubectl apply -f deploy-llm.yaml
         

The command creates three Kubernetes resources:

     * A Deployment that runs the vLLM server, configured to use the `meta-llama/Llama-3.1-8B-Instruct` model.
     * A Service named `vllm-llama3-service` that exposes the vLLM server on an internal cluster IP address, allowing the ADK agent to communicate with it.
     * A ConfigMap containing a Jinja chat template required by the Llama 3.1 model.
  4. **Verify the model Deployment** : The vLLM server pulls the model files from Hugging Face. This process can take several minutes. You can monitor the status of the Pod to ensure its readiness.

     1. Wait for the Deployment to become available.
            
            kubectl wait --for=condition=available --timeout=600s deployment/vllm-llama3-deployment
            

     2. View the logs from the running Pod to confirm that the server started successfully.
            
            export LLM_POD=$(kubectl get pods -l app=vllm-llama3 -o jsonpath='{.items[0].metadata.name}')
            kubectl logs -f $LLM_POD
            

The deployment is ready when you see log output similar to the following, indicating the LLM server has started and the API routes are available:
            
            INFO 07-16 14:15:16 api_server.py:129] Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
            

     3. Send a request directly to the model server to confirm that the LLM is ready. To do this, open a new Cloud Shell terminal and run the following command to forward the `vllm-llama3-service` to your local machine:
            
            kubectl port-forward service/vllm-llama3-service 8000:8000
            

     4. In another terminal, send a sample request to the model's API endpoint by using `curl`. For example:
            
            curl -X POST http://localhost:8000/v1/completions \
              -H "Content-Type: application/json" \
              -d '{
                "model": "meta-llama/Llama-3.1-8B-Instruct",
                "prompt": "Hello!",
                "max_tokens": 10
              }'
            

If the command returns a successful JSON response, your LLM is ready. You can now terminate the port-forward process by returning to its terminal window and pressing `Ctrl+C`, then proceed to deploy the agent.




## Deploy the agent application

The next step is to deploy the ADK-based agent application.

  1. **Navigate to the`/deploy-agent` directory**: From your project root directory (`adk/llama/vllm`), navigate to the `/deploy-agent` directory that contains the agent's source code and deployment manifest.
         
         cd ../deploy-agent
         

  2. **Update the agent deployment manifest** :

     1. The sample `deploy-agent.yaml` manifest file contains a placeholder for your project ID in the container image URL. You must replace the placeholder with your Google Cloud project ID.
            
            image: us-central1-docker.pkg.dev/PROJECT_ID/adk-repo/adk-agent:latest
            

To perform this substitution in place, you can run the following command:
            
            sed -i "s/<PROJECT_ID>/$PROJECT_ID/g" deploy-agent.yaml
            

     2. Make sure the `readinessProbe` path is set to `/` instead of `/dev-ui`. To perform this substitution in place, you can run the following command:
            
            sed -i "s|path: /dev-ui/|path: /|g" deploy-agent.yaml
            

  3. **Apply the manifest** : Run the following command to apply the `deploy-agent.yaml` manifest to your cluster.
         
         kubectl apply -f deploy-agent.yaml
         

This command creates two Kubernetes resources:

     * A Deployment named `adk-agent` that runs your custom-built agent container image.
     * A Service named `adk-agent` of type NodePort that exposes the agent application so it can be accessed for testing.
  4. **Verify the agent deployment** : Check the status of the Pod to ensure it is running correctly.

     1. Wait for the Deployment to become available:
            
            kubectl wait --for=condition=available --timeout=300s deployment/adk-agent
            

     2. View the logs from the running agent Pod:
            
            export AGENT_POD=$(kubectl get pods -l app=adk-agent -o jsonpath='{.items[0].metadata.name}')
            kubectl logs -f $AGENT_POD
            




The deployment is successful when you see log output similar to the following, indicating that the Uvicorn server is running and ready to accept requests:
    
    
    INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
    

## Test your deployed agent

After successfully deploying both the vLLM server and the agent application, you can test the end-to-end functionality by interacting with the agent's web UI.

**Note:** This tutorial uses the LLM to determine which tool to call based on your prompt, but the tool itself uses hardcoded mock data for simplicity instead of a live API. The agent's `get_weather` tool retrieves weather information from a predefined dictionary for "paris," "ottawa," and "tokyo," instead of a real-time external service.

  1. **Forward the agent's service to your local machine** : The `adk-agent` service is of type `NodePort`, but the most direct way to access it from your Cloud Shell environment is to use the `kubectl port-forward` command. Create a secure tunnel to the agent's Pod by running this command.
         
         kubectl port-forward $AGENT_POD 8001:8001
         

  2. **Access the agent's web UI** : In Cloud Shell, click the **Web Preview** button and select **Preview on port 8001**. A new browser tab opens, displaying the agent's chat interface.

  3. **Interact with the agent** : Ask the agent a question that will invoke its `get_weather` tool. For example:
         
         What's the weather like in Tokyo?
         

The agent will first call the LLM to understand the intent and identify the need to use the `get_weather` tool. Then, it will execute the tool with "Tokyo" as the parameter. Finally, it will use the tool's output to generate a response. You should see a response similar to the following:
         
         The weather in Tokyo is 25°C and sunny.
         

  4. **(Optional) Verify the tool call in the logs** : You can observe the agent's interaction with the LLM and the tool execution by viewing the logs of the respective Pods.

     1. **Agent Pod logs** : In a new terminal, view the logs of the `adk-agent` Pod. You see the tool call and its result.
            
            kubectl logs -f $AGENT_POD
            

The output shows the tool being called and the result being processed.

     2. **LLM Pod logs** : View the logs of the `vllm-llama3-deployment` Pod to see the incoming request from the agent.
            
            kubectl logs -f $LLM_POD
            

The logs shows the full prompt sent by the agent to the LLM, including the system message, your query, and the definition of the `get_weather` tool.




After you finish testing, you can terminate the `port-forward` process by returning to its terminal window and pressing `Ctrl+C`.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

## Delete the deployed resources

To avoid incurring charges to your Google Cloud account for the resources that you created in this tutorial, run the following commands:

### gcloud

If you used the gcloud CLI to create your resources, run the following commands to delete the GKE cluster and the Artifact Registry repository, and return the service account's permissions to its original state.
    
    
    gcloud container clusters delete CLUSTER_NAME \
        --location=$GOOGLE_CLOUD_REGION
    
    gcloud artifacts repositories delete REPO_NAME \
        --location=$GOOGLE_CLOUD_REGION
    
    gcloud projects remove-iam-policy-binding $PROJECT_ID \
        --member=serviceAccount:${COMPUTE_SA_EMAIL} \
        --role=roles/artifactregistry.writer
    

### Terraform

If you used Terraform to provision your infrastructure, you can destroy all the resources by running a single command from within the `/terraform` directory.

  1. From your project root directory (`adk/llama/vllm`), navigate to the `/terraform` directory:
         
         cd terraform
         

  2. Run this command to remove all resources defined in your Terraform configuration files:
         
         terraform destroy
         




## What's next

  * Learn how to configure [Horizontal Pod Autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) to automatically adjust your agent's resources on-demand.
  * Learn how to configure [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) for your web applications running on Google Cloud, providing centralized authorization for access to your agent's UI.
  * Learn how to use [Cloud Logging and Cloud Monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability) to gain insights into your agent's performance and health within your GKE cluster.
  * Explore experimental samples in [GKE AI Labs](https://gke-ai-labs.dev/docs/agentic/) that can help you use GKE to accelerate your agentic AI initiatives.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
