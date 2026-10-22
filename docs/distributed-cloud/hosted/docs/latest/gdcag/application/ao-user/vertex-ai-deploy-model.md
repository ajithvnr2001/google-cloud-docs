---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model/
title: Deploy a model to an endpoint \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:58.126005+00:00
---

# Deploy a model to an endpoint  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Deploy a model to an endpoint Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).**Note:** Authorization is not enforced for Online Prediction because it is a Preview feature.

You must deploy a model to an endpoint before you can use that model to serve online predictions. Deploying a model associates physical resources to serve online predictions with low latency.

This page describes the steps you must follow to deploy a model to an endpoint using Online Prediction.

## Before you begin

To deploy Online Prediction models, contact your IAM Project Admin to request the **Vertex AI Prediction Admin** (`vertex-ai-prediction-admin`) role in your project namespace.

For more information about this role, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

Before deploying your model to an endpoint, [export your model artifacts for prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-export-model-artifacts) and ensure you meet all the prerequisites from that page.

## Create a resource pool

A `ResourcePool` custom resource lets you have fine-grained control over the behavior of your model. You can define settings such as the following:

  * Autoscaling configurations.
  * The machine type, which defines CPU and memory requirements.
  * Accelerator options such as GPU resources.



The machine type is essential for the node pool specification request you send to [create the prediction cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/prediction-user-cluster).

For the resource pool of the deployed model, the accelerator count and type determine GPU usage. The machine type only dictates the requested CPU and memory resources. For this reason, when including GPU accelerators in the `ResourcePool` specification, the `machineType` field controls the CPU and memory requirements for the model, while the `acceleratorType` field controls the GPU. Furthermore, the `acceleratorCount` field controls the number of GPU slices.

**Important:** You must give fewer computing units to the resource pool than to the node pool. For example, if you use a node pool with a GPU machine type, such as `a2-highgpu-1g-gdc`, you have 12 vCPUs. Therefore, you must specify a smaller CPU machine type for the resource pool. Also, specify the `acceleratorType` and `acceleratorCount` fields to enable GPU workloads. In this same example, you would choose a machine type in the `ResourcePool` specification with a maximum of 8 vCPUs and specify the `acceleratorType` field for GPU workloads.

Follow these steps to create a `ResourcePool` custom resource:

  1. Create a YAML file defining the `ResourcePool` custom resource. The following examples contain YAML files for resource pools with GPU accelerators (GPU-based models) and without GPU accelerators (CPU-based models):

###  GPU-based models 
         
         apiVersion: prediction.aiplatform.gdc.goog/v1
           kind: ResourcePool
           metadata:
             name: RESOURCE_POOL_NAME
             namespace: PROJECT_NAMESPACE
           spec:
             resourcePoolID: RESOURCE_POOL_NAME
             enableContainerLogging: false
             dedicatedResources:
               machineSpec:
                 # The system adds computing overhead to the nodes for mandatory components.
                 # Choose a machineType value that allocates fewer CPU and memory resources
                 # than those used by the nodes in the prediction cluster.
                 machineType: a2-highgpu-1g-gdc
                 acceleratorType: nvidia-a100-80gb
                 # The accelerator count is a slice of the requested virtualized GPUs.
                 # The value corresponds to one-seventh of 80 GB of GPUs for each count.
                 acceleratorCount: 2
               autoscaling:
                 minReplica: 2
                 maxReplica: 10
         

**Note:** This example shows a partial Multi-Instance GPU (MIG) tag name for the GPU accelerator type in the `acceleratorType` field (`nvidia-a100-80gb`). However, a format with full MIG tag names is also supported, like `nvidia.com/mig-1g.12gb-NVIDIA_H100_NVL`.

###  CPU-based models 
         
         apiVersion: prediction.aiplatform.gdc.goog/v1
           kind: ResourcePool
           metadata:
             name: RESOURCE_POOL_NAME
             namespace: PROJECT_NAMESPACE
           spec:
             resourcePoolID: RESOURCE_POOL_NAME
             enableContainerLogging: false
             dedicatedResources:
               machineSpec:
                 # The system adds computing overhead to the nodes for mandatory components.
                 # Choose a machineType value that allocates fewer CPU and memory resources
                 # than those used by the nodes in the prediction cluster.
                 machineType: n2-highcpu-8-gdc
               autoscaling:
                 minReplica: 2
                 maxReplica: 10
         

Replace the following:

     * `RESOURCE_POOL_NAME`: the name you want to give to the `ResourcePool` definition file.
     * `PROJECT_NAMESPACE`: the name of the project namespace associated with the prediction cluster.

Modify the values on the `dedicatedResources` fields according to your resource needs and what is available in your prediction cluster.

  2. Apply the `ResourcePool` definition file to the prediction cluster:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG apply -f RESOURCE_POOL_NAME.yaml
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `RESOURCE_POOL_NAME`: the name of the `ResourcePool` definition file.



When you create the `ResourcePool` custom resource, the Kubernetes API and the webhook service validate the YAML file and report success or failure. The prediction operator provisions and reserves your resources from the resource pool when you deploy your models to an endpoint.

## Deploy your model to an endpoint

If you have a resource pool, you can deploy more than one model to an endpoint, and you can deploy a model to more than one endpoint. Deploy a prediction model targeting [supported containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#available-container-images). Depending on whether the endpoint already exists or not, choose between one of the following two methods:

  * Deploy a model to a new endpoint
  * Deploy a model to an existing endpoint



### Deploy a model to a new endpoint

Follow these steps to deploy a prediction model to a new endpoint:

  1. Create a YAML file defining a `DeployedModel` custom resource:

###  TensorFlow 

The following YAML file shows a sample configuration for a TensorFlow model:
         
         apiVersion: prediction.aiplatform.gdc.goog/v1
         kind: DeployedModel
         metadata:
           name: DEPLOYED_MODEL_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           # The endpoint path structure is endpoints/<endpoint-id>
           endpointPath: endpoints/PREDICTION_ENDPOINT
           modelSpec:
             # The artifactLocation field must be the s3 path to the folder that
             # contains the various model versions.
             # For example, s3://my-prediction-bucket-fqn/tensorflow
             artifactLocation: s3://PATH_TO_MODEL
             # The value in the id field must be unique to each model.
             id: img-detection-model
             modelDisplayName: my_img_detection_model
             # The model resource name structure is models/<model-id>/<model-version-id>
             modelResourceName: models/img-detection-model/1
             # The model version ID must match the name of the first folder in
             # the artifactLocation bucket, inside the 'tensorflow' folder.
             # For example, if the bucket path is
             # s3://my-prediction-bucket-fqn/tensorflow/1/,
             # then the value for the model version ID is "1".
             modelVersionID: "1"
             modelContainerSpec:
               args:
               - --model_config_file=/models/models.config
               - --rest_api_port=8080
               - --port=8500
               - --file_system_poll_wait_seconds=30
               - --model_config_file_poll_wait_seconds=30
               command:
               - /bin/tensorflow_model_server
               # The image URI field must contain one of the following values:
               # For CPU-based models: gcr.io/aiml/prediction/containers/tf2-cpu.2-18:latest
               # For GPU-based models: gcr.io/aiml/prediction/containers/tf2-gpu.2-18:latest
               imageURI: gcr.io/aiml/prediction/containers/tf2-gpu.2-18:latest
               ports:
               - 8080
               grpcPorts:
               - 8500
           resourcePoolRef:
             kind: ResourcePool
             name: RESOURCE_POOL_NAME
             namespace: PROJECT_NAMESPACE
         

Replace the following:

     * `DEPLOYED_MODEL_NAME`: the name you want to give to the `DeployedModel` definition file.
     * `PROJECT_NAMESPACE`: the name of the project namespace associated with the prediction cluster.
     * `PREDICTION_ENDPOINT`: the name you want to give to the new endpoint, such as `my-img-prediction-endpoint`.
     * `PATH_TO_MODEL`: the path to your model in the storage bucket.
     * `RESOURCE_POOL_NAME`: the name you gave to the `ResourcePool` definition file when you created a resource pool to host the model.

Modify the values on the remaining fields according to your prediction model.

###  PyTorch 

The following YAML file shows a sample configuration for a PyTorch model:
    
    apiVersion: prediction.aiplatform.gdc.goog/v1
    kind: DeployedModel
    metadata:
      name: DEPLOYED_MODEL_NAME
      namespace: PROJECT_NAMESPACE
    spec:
      endpointPath: PREDICTION_ENDPOINT
      endpointInfo:
        id: PREDICTION_ENDPOINT
      modelSpec:
        # The artifactLocation field must be the s3 prefix that
        # includes the model artifacts for the model version.
        # For example, s3://my-prediction-bucket-fqn/pytorch-model/1
        artifactLocation: s3://PATH_TO_MODEL
        # The value in the id field must be unique to each model.
        id: "pytorch"
        modelDisplayName: my-pytorch-model
        # The model resource name structure is models/<model-id>/<model-version-id>
        modelResourceName: models/pytorch/1
        modelVersionID: "1"
        modelContainerSpec:
          # The image URI field must contain one of the following values:
          # For CPU-based models: gcr.io/aiml/prediction/containers/pytorch-cpu.2-1:latest
          # For GPU-based models: gcr.io/aiml/prediction/containers/pytorch-gpu.2-1:latest
          imageURI: gcr.io/aiml/prediction/containers/pytorch-cpu.2-1:latest
          ports:
          - 8080
          grpcPorts:
          - 7070
      sharesResourcePool: false
      resourcePoolRef:
        kind: ResourcePool
        name: RESOURCE_POOL_NAME
        namespace: PROJECT_NAMESPACE
    

Replace the following:

     * `DEPLOYED_MODEL_NAME`: the name you want to give to the `DeployedModel` definition file.
     * `PROJECT_NAMESPACE`: the name of the project namespace associated with the prediction cluster.
     * `PREDICTION_ENDPOINT`: the name you want to give to the new endpoint, such as `my-img-prediction-endpoint`.
     * `PATH_TO_MODEL`: the path to your model in the storage bucket.
     * `RESOURCE_POOL_NAME`: the name you gave to the `ResourcePool` definition file when you created a resource pool to host the model.

Modify the values on the remaining fields according to your prediction model.

  2. Apply the `DeployedModel` definition file to the prediction cluster:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG apply -f DEPLOYED_MODEL_NAME.yaml
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `DEPLOYED_MODEL_NAME`: the name of the `DeployedModel` definition file.

When you create the `DeployedModel` custom resource, the Kubernetes API and the webhook service validate the YAML file and report success or failure. The prediction operator reconciles the `DeployedModel` custom resource and serves it in the prediction cluster.

**Tip:** You can check the status of the `DeployedModel` custom resource and ensure it is ready to accept prediction requests using the `kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get -f DEPLOYED_MODEL_NAME.yaml -o jsonpath='{.status.primaryCondition}'` command. The `DeployedModel` must be in a ready state.
  3. Create a YAML file defining an `Endpoint` custom resource.

The following YAML file shows a sample configuration:
         
         apiVersion: aiplatform.gdc.goog/v1
         kind: Endpoint
         metadata:
           name: ENDPOINT_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           createDns: true
           id: PREDICTION_ENDPOINT
           destinations:
             - serviceRef:
                 kind: DeployedModel
                 name: DEPLOYED_MODEL_NAME
                 namespace: PROJECT_NAMESPACE
               trafficPercentage: 50
               grpcPort: 8501
               httpPort: 8081
             - serviceRef:
                 kind: DeployedModel
                 name: DEPLOYED_MODEL_NAME_2
                 namespace: PROJECT_NAMESPACE
               trafficPercentage: 50
               grpcPort: 8501
               httpPort: 8081
         

Replace the following:

     * `ENDPOINT_NAME`: the name you want to give to the `Endpoint` definition file.
     * `PROJECT_NAMESPACE`: the name of the project namespace associated with the prediction cluster.
     * `PREDICTION_ENDPOINT`: the name of the new endpoint. You defined this name on the `DeployedModel` definition file.
     * `DEPLOYED_MODEL_NAME`: the name you gave to the `DeployedModel` definition file.

You can have one or more `serviceRef` destinations. If you have a second `serviceRef` object, add it to the YAML file on the `destinations` field and replace `DEPLOYED_MODEL_NAME_2` with the name you gave to the second `DeployedModel` definition file you created. Keep adding or removing `serviceRef` objects as you need them, depending on the amount of models you are deploying.

Set the `trafficPercentage` fields based on how you want to split traffic between the models on this endpoint. Modify the values on the remaining fields according to your endpoint configurations.

  4. Apply the `Endpoint` definition file to the prediction cluster:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG apply -f ENDPOINT_NAME.yaml
         

Replace `ENDPOINT_NAME` with the name of the `Endpoint` definition file.




To get the endpoint URL path for the prediction model, run the following command:
    
    
    kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get endpoint PREDICTION_ENDPOINT -n PROJECT_NAMESPACE -o jsonpath='{.status.endpointFQDN}'
    

Replace the following:

  * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
  * `PREDICTION_ENDPOINT`: the name of the new endpoint.
  * `PROJECT_NAMESPACE`: the name of the prediction project namespace.



### Deploy a model to an existing endpoint

You can only deploy a model to an existing endpoint if you had previously deployed another model to that endpoint when it was new. The system requires this previous step to create the endpoint.

Follow these steps to deploy a prediction model to an existing endpoint:

  1. Create a YAML file defining a `DeployedModel` custom resource.

The following YAML file shows a sample configuration:
         
         apiVersion: prediction.aiplatform.gdc.goog/v1
         kind: DeployedModel
         metadata:
           name: DEPLOYED_MODEL_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           # The endpoint path structure is endpoints/<endpoint-id>
           endpointPath: endpoints/PREDICTION_ENDPOINT
           modelSpec:
             # The artifactLocation field must be the s3 path to the folder that
             # contains the various model versions.
             # For example, s3://my-prediction-bucket-fqn/tensorflow
             artifactLocation: s3://PATH_TO_MODEL
             # The value in the id field must be unique to each model.
             id: img-detection-model-v2
             modelDisplayName: my_img_detection_model
             # The model resource name structure is models/<model-id>/<model-version-id>
             modelResourceName: models/img-detection-model/2
             # The model version ID must match the name of the first folder in
             # the artifactLocation bucket,
             # inside the 'tensorflow' folder.
             # For example, if the bucket path is
             # s3://my-prediction-bucket-fqn/tensorflow/2/,
             # then the value for the model version ID is "2".
             modelVersionID: "2"
             modelContainerSpec:
               args:
               - --model_config_file=/models/models.config
               - --rest_api_port=8080
               - --port=8500
               - --file_system_poll_wait_seconds=30
               - --model_config_file_poll_wait_seconds=30
               command:
               - /bin/tensorflow_model_server
               # The image URI field must contain one of the following values:
               # For CPU-based models: gcr.io/aiml/prediction/containers/tf2-cpu.2-6:latest
               # For GPU-based models: gcr.io/aiml/prediction/containers/tf2-gpu.2-6:latest
               imageURI: gcr.io/aiml/prediction/containers/tf2-gpu.2-6:latest
               ports:
               - 8080
               grpcPorts:
               - 8500
           resourcePoolRef:
             kind: ResourcePool
             name: RESOURCE_POOL_NAME
             namespace: PROJECT_NAMESPACE
         

Replace the following:

     * `DEPLOYED_MODEL_NAME`: the name you want to give to the `DeployedModel` definition file.
     * `PROJECT_NAMESPACE`: the name of the project namespace associated with the prediction cluster.
     * `PREDICTION_ENDPOINT`: the name of the existing endpoint, such as `my-img-prediction-endpoint`.
     * `PATH_TO_MODEL`: the path to your model in the storage bucket.
     * `RESOURCE_POOL_NAME`: the name you gave to the `ResourcePool` definition file when you created a resource pool to host the model.

Modify the values on the remaining fields according to your prediction model.

  2. Apply the `DeployedModel` definition file to the prediction cluster:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG apply -f DEPLOYED_MODEL_NAME.yaml
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `DEPLOYED_MODEL_NAME`: the name of the `DeployedModel` definition file.

When you create the `DeployedModel` custom resource, the Kubernetes API and the webhook service validate the YAML file and report success or failure. The prediction operator reconciles the `DeployedModel` custom resource and serves it in the prediction cluster.

**Tip:** You can check the status of the `DeployedModel` custom resource and ensure it is ready to accept prediction requests using the `kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get -f DEPLOYED_MODEL_NAME.yaml -o jsonpath='{.status.primaryCondition}'` command. The `DeployedModel` must be in a ready state.
  3. Show details of the existing `Endpoint` custom resource:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG describe -f ENDPOINT_NAME.yaml
         

Replace `ENDPOINT_NAME` with the name of the `Endpoint` definition file.

  4. Update the YAML file of the `Endpoint` custom resource definition by adding a new `serviceRef` object on the `destinations` field. On the new object, include the appropriate service name based on your newly created `DeployedModel` custom resource.

The following YAML file shows a sample configuration:
         
         apiVersion: aiplatform.gdc.goog/v1
         kind: Endpoint
         metadata:
           name: ENDPOINT_NAME
           namespace: PROJECT_NAMESPACE
         spec:
           createDns: true
           id: PREDICTION_ENDPOINT
           destinations:
             - serviceRef:
                 kind: DeployedModel
                 name: DEPLOYED_MODEL_NAME
                 namespace: PROJECT_NAMESPACE
               trafficPercentage: 40
               grpcPort: 8501
               httpPort: 8081
             - serviceRef:
                 kind: DeployedModel
                 name: DEPLOYED_MODEL_NAME_2
                 namespace: PROJECT_NAMESPACE
               trafficPercentage: 50
               grpcPort: 8501
               httpPort: 8081
             - serviceRef:
                 kind: DeployedModel
                 name: DEPLOYED_MODEL_NAME_3
                 namespace: PROJECT_NAMESPACE
               trafficPercentage: 10
               grpcPort: 8501
               httpPort: 8081
         

Replace the following:

     * `ENDPOINT_NAME`: the name of the existing `Endpoint` definition file.
     * `PROJECT_NAMESPACE`: the name of the project namespace associated with the prediction cluster.
     * `PREDICTION_ENDPOINT`: the name of the existing endpoint. You referenced this name on the `DeployedModel` definition file.
     * `DEPLOYED_MODEL_NAME`: the name of a previously created `DeployedModel` definition file.
     * `DEPLOYED_MODEL_NAME_2`: the name you gave to the newly created `DeployedModel` definition file.

You can have one or more `serviceRef` destinations. If you have a third `serviceRef` object, add it to the YAML file on the `destinations` field and replace `DEPLOYED_MODEL_NAME_3` with the name you gave to the third `DeployedModel` definition file you created. Keep adding or removing `serviceRef` objects as you need them, depending on the amount of models you are deploying.

Set the `trafficPercentage` fields based on how you want to split traffic between the models of this endpoint. Modify the values on the remaining fields according to your endpoint configurations.

  5. Apply the `Endpoint` definition file to the prediction cluster:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG apply -f ENDPOINT_NAME.yaml
         

Replace `ENDPOINT_NAME` with the name of the `Endpoint` definition file.




To get the endpoint URL path for the prediction model, run the following command:
    
    
    kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get endpoint PREDICTION_ENDPOINT -n PROJECT_NAMESPACE -o jsonpath='{.status.endpointFQDN}'
    

Replace the following:

  * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
  * `PREDICTION_ENDPOINT`: the name of the endpoint.
  * `PROJECT_NAMESPACE`: the name of the prediction project namespace.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
