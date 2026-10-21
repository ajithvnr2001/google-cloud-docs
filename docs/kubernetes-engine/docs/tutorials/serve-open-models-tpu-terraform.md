---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-tpu-terraform/
title: Serve open LLMs on GKE using TPUs with a pre-configured architecture \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:30.954979+00:00
---

# Serve open LLMs on GKE using TPUs with a pre-configured architecture  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-tpu-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Serve open LLMs on GKE using TPUs with a pre-configured architecture Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to quickly deploy and serve popular open large language models (LLMs) on GKE with TPUs for inference using a pre-configured, production-ready [GKE inference reference architecture](https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/docs/platforms/gke/base/use-cases/inference-ref-arch/README.md). This approach uses Infrastructure as Code (IaC), with Terraform wrapped in CLI scripts, to create a standardized, secure, and scalable GKE environment designed for AI inference workloads. 

In this guide, you deploy and serve LLMs using single-host TPU nodes on GKE with the vLLM serving framework. This guide provides instructions and configurations for deploying the following open models:

  * [Google Gemma 4 26B-A4B-it](https://huggingface.co/google/gemma-4-26B-A4B-it)
  * [Google Gemma 4 31B-it](https://huggingface.co/google/gemma-4-31B-it)
  * [Google Gemma 3 1B-it](https://huggingface.co/google/gemma-3-1B-it)
  * [Google Gemma 3 4B-it](https://huggingface.co/google/gemma-3-4B-it)
  * [Google Gemma 3 27B-it](https://huggingface.co/google/gemma-3-27B-it)
  * [Qwen 3 32B](https://huggingface.co/Qwen/Qwen3-32B)

**Note:** You must accept the license terms for any gated models you want to use (such as Gemma) on their respective Hugging Face model page.

This guide is intended for Machine learning (ML) engineers and Data and AI specialists who are interested in exploring Kubernetes container orchestration capabilities for serving open models for inference. To learn more about common roles and example tasks referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,secretmanager.googleapis.com,cloudresourcemanager.googleapis.com)

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

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,secretmanager.googleapis.com,cloudresourcemanager.googleapis.com)

  * Make sure that you have the following role or roles on the project: roles/artifactregistry.admin, roles/browser, roles/compute.networkAdmin, roles/container.clusterAdmin, roles/iam.roleAdmin, roles/iam.serviceAccountAdmin, roles/resourcemanager.projectIamAdmin, and roles/serviceusage.serviceUsageAdmin, roles/secretmanager.secretVersionManager 

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


  * Create a [Hugging Face account](https://huggingface.co/).
  * Ensure your project has sufficient [TPU quota (GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#ensure-quota) or [TPU quota (GKE Autopilot)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot#ensure-tpu-quota). For more information, see [Plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).



## Get access to the model

Accept the license terms for any gated models you want to use (such as Gemma) on their respective Hugging Face model page.

To access the model through Hugging Face, you need a [Hugging Face token](https://huggingface.co/docs/hub/security-tokens).

Follow these steps to generate a new token if you don't have one already:

  1. Click **Your Profile** > **Settings** > **Access Tokens**.
  2. Select **New Token**.
  3. Specify a **Name** of your choice and a **Role** of at least **Read**.
  4. Select **Generate a token**.
  5. Copy the generated token to your clipboard.



## Provision the GKE inference environment

In this section, you deploy the necessary infrastructure to serve your model.

### Launch Cloud Shell

This guide uses [Cloud Shell](https://docs.cloud.google.com/shell) to execute commands. Cloud Shell comes preinstalled with the necessary tools, including `gcloud`, `kubectl`, and `git`.

In the Google Cloud console, start a Cloud Shell instance:

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

This action launches a session in the bottom pane of Google Cloud console.

### Deploy the base architecture

To provision the GKE cluster and the necessary resources for accessing models from Hugging Face, follow these steps:

  1. In Cloud Shell, clone the following repository:
         
         git clone https://github.com/GoogleCloudPlatform/accelerated-platforms --branch hf-model-vllm-tpu-tutorial && \
         cd accelerated-platforms && \
         export ACP_REPO_DIR="$(pwd)"
         

  2. Set your environment variables:
         
         export TF_VAR_platform_default_project_id=PROJECT_ID
         export HF_TOKEN_READ=HF_TOKEN
         

Replace the following values:

     * `PROJECT_ID`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `HF_TOKEN`: the Hugging Face token you generated earlier.
  3. This guide requires Terraform version 1.8.0 or later. Cloud Shell has Terraform v1.5.7 installed by default.

To update the Terraform version in Cloud Shell, you can run the following script. This script installs the [`tfswitch`](https://tfswitch.warrensbox.com/) tool and installs Terraform v1.8.0 in your home directory. Follow the instruction from the script to set the necessary environment variable or pass the `--modify-rc-file` flag to the script.
         
         "${ACP_REPO_DIR}/tools/bin/install_terraform.sh" && \
         export PATH=${HOME}/bin:${HOME}/.local/bin:${PATH}
         

  4. Run the following deployment script. The deployment script enables the required Google Cloud APIs and provisions the necessary infrastructure for this guide. This includes a new VPC network, a GKE cluster with private nodes, and other supporting resources. The script can take several minutes to complete.

You can serve models using TPUs in a GKE Autopilot or Standard cluster. An Autopilot cluster provides a fully managed Kubernetes experience. For more information about choosing the GKE mode of operation that's the best fit for your workloads, see [About GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot
         
         "${ACP_REPO_DIR}/platforms/gke/base/tutorials/hf-tpu-model/deploy-ap.sh"
         

### Standard
         
         "${ACP_REPO_DIR}/platforms/gke/base/tutorials/hf-tpu-model/deploy-standard.sh"
         

After this script completes, you will have a GKE cluster ready for inference workloads.

  5. Run the following command to set environment variables from the shared configuration:
         
         source "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/terraform/_shared_config/scripts/set_environment_variables.sh"
         

  6. The deployment script creates a secret in Secret Manager to store your Hugging Face token. You must manually add your token to this secret before deploying the cluster. In Cloud Shell, run this command to add the token to Secret Manager.
         
         echo ${HF_TOKEN_READ} | gcloud secrets versions add ${huggingface_hub_access_token_read_secret_manager_secret_name} \
         --data-file=- \
         --project=${huggingface_secret_manager_project_id}
         




## Deploy an open model

You are now ready to download and deploy the model.

### Select a model

  1. Set the environment variables for the model you want to deploy:

### Gemma 4 26B-A4B-it
         
         export ACCELERATOR_TYPE="v6e"
         export HF_MODEL_ID="google/gemma-4-26b-a4b-it"
         

### Gemma 4 31B-it
         
         export ACCELERATOR_TYPE="v6e"
         export HF_MODEL_ID="google/gemma-4-31b-it"
         

### Gemma 3 1B-it
         
         export ACCELERATOR_TYPE="v5e"
         export HF_MODEL_ID="google/gemma-3-1b-it"
         

### Gemma 3 4B-it
         
         export ACCELERATOR_TYPE="v5e"
         export HF_MODEL_ID="google/gemma-3-4b-it"
         

### Gemma 3 27B-it
         
         export ACCELERATOR_TYPE="v5e"
         export HF_MODEL_ID="google/gemma-3-27b-it"
         

### Qwen 3 32B
         
         export ACCELERATOR_TYPE="v6e"
         export HF_MODEL_ID="Qwen/Qwen3-32B"
         

For additional configurations, including other model variants and TPU types, see the manifests available in the [`accelerated-platforms` GitHub repository](https://github.com/GoogleCloudPlatform/accelerated-platforms/tree/main/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/online-inference-tpu/vllm).




### Download the model

  1. Source the environment variables from your deployment. These environment variables contain the necessary configuration details from the infrastructure you provisioned.
         
         source "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/terraform/_shared_config/scripts/set_environment_variables.sh"
         

  2. Run the following script to configure the Hugging Face model download resources that downloads the model to Cloud Storage:
         
         "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/model-download/configure_huggingface.sh"
         

  3. Apply the Hugging Face model download resources:
         
         kubectl apply --kustomize "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/model-download/huggingface"
         

  4. Monitor the Hugging Face model download job until it is complete.
         
         until kubectl --namespace=${huggingface_hub_downloader_kubernetes_namespace_name} wait job/${HF_MODEL_ID_HASH}-hf-model-to-gcs --for=condition=complete --timeout=10s >/dev/null; do
             clear
             kubectl --namespace=${huggingface_hub_downloader_kubernetes_namespace_name} get job/${HF_MODEL_ID_HASH}-hf-model-to-gcs | GREP_COLORS='mt=01;92' egrep --color=always -e '^' -e 'Complete'
             echo -e "\nhf-model-to-gcs logs(last 10 lines):"
             kubectl --namespace=${huggingface_hub_downloader_kubernetes_namespace_name} logs job/${HF_MODEL_ID_HASH}-hf-model-to-gcs --container=hf-model-to-gcs --tail 10
         done
         

  5. Verify the Hugging Face model download job is complete.
         
         kubectl --namespace=${huggingface_hub_downloader_kubernetes_namespace_name} get job/${HF_MODEL_ID_HASH}-hf-model-to-gcs | GREP_COLORS='mt=01;92' egrep --color=always -e '^' -e 'Complete'
         

  6. Delete the Hugging Face model download resources.
         
         kubectl delete --ignore-not-found --kustomize "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/model-download/huggingface"
         




### Deploy the model

  1. Source the environment variables from your deployment.
         
         source "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/terraform/_shared_config/scripts/set_environment_variables.sh"
         

  2. Verify the Hugging Face model name is set.
         
         echo "HF_MODEL_NAME=${HF_MODEL_NAME}"
         

  3. Configure the vLLM resources.
         
         "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/online-inference-tpu/vllm/configure_vllm.sh"
         

  4. Deploy the inference workload to your GKE cluster.
         
         kubectl apply --kustomize "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/online-inference-tpu/vllm/${ACCELERATOR_TYPE}-${HF_MODEL_NAME}"
         




## Test your deployment

  1. Monitor the inference workload deployment until it is available.
         
         until kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} wait deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} --for=condition=available --timeout=10s >/dev/null; do
             clear
             kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} get deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} | GREP_COLORS='mt=01;92' egrep --color=always -e '^' -e '1/1     1            1'
             echo -e "\nfetch-safetensors logs(last 10 lines):"
             kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} logs deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} --container=fetch-safetensors --tail 10
             echo -e "\ninference-server logs(last 10 lines):"
             kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} logs deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} --container=inference-server --tail 10
         done
         

  2. Verify the inference workload deployment is available.
         
         kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} get deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} | GREP_COLORS='mt=01;92' egrep --color=always -e '^' -e '1/1     1            1'
         echo -e "\nfetch-safetensors logs(last 10 lines):"
         kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} logs deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} --container=fetch-safetensors --tail 10
         echo -e "\ninference-server logs(last 10 lines):"
         kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} logs deployment/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} --container=inference-server --tail 10
         

  3. Run the following script to set up port forwarding and send a sample request to the model.
         
         kubectl --namespace=${ira_online_tpu_kubernetes_namespace_name} port-forward service/vllm-${ACCELERATOR_TYPE}-${HF_MODEL_NAME} 8000:8000 >/dev/null &
         PF_PID=$!
         while ! echo -e '\x1dclose\x0d' | telnet localhost 8000 >/dev/null 2>&1; do
             sleep 0.1
         done
         curl http://127.0.0.1:8000/v1/chat/completions \
         --data '{
         "model": "/gcs/'${HF_MODEL_ID}'",
         "messages": [ { "role": "user", "content": "What is GKE?" } ]
         }' \
         --header "Content-Type: application/json" \
         --request POST \
         --show-error \
         --silent | jq
         kill -9 ${PF_PID}
         

You should see a JSON response from the model answering the question.




## Clean up

To avoid incurring charges, delete all the resources you created.

  1. Delete the inference workload:
         
         kubectl delete --ignore-not-found --kustomize "${ACP_REPO_DIR}/platforms/gke/base/use-cases/inference-ref-arch/kubernetes-manifests/online-inference-tpu/vllm/${ACCELERATOR_TYPE}-${HF_MODEL_NAME}"
         

  2. Clean up the resources:

### Autopilot
         
         "${ACP_REPO_DIR}/platforms/gke/base/tutorials/hf-tpu-model/teardown-ap.sh"
         

### Standard
         
         "${ACP_REPO_DIR}/platforms/gke/base/tutorials/hf-tpu-model/teardown-standard.sh"
         




## What's next

  * Learn more about [AI/ML model inference on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference).
  * Analyze model inference performance and costs with the [GKE Inference Quickstart tool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart).
  * Explore the [accelerated-platforms GitHub repository](https://github.com/GoogleCloudPlatform/accelerated-platforms) used to build this architecture.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
