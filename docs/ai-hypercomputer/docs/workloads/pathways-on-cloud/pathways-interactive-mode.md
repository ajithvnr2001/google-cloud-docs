---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode/
title: Run an interactive workload with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:00.402567+00:00
---

# Run an interactive workload with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run an interactive workload with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

Pathways interactive workloads are remote JAX workloads that run within a VM that is not part of GKE cluster hosting the Pathways cluster. Unlike batch workloads, the completion of interactive workload operation does not shut down the Pathways cluster components, which remain available for connection by other JAX clients. This document uses a Jupyter notebook as an example to demonstrate interactive workloads.

Using the [IFRT](https://github.com/openxla/xla/blob/main/xla/python/ifrt/README.md) interface, JAX users send commands to a Pathways cluster. JAX code, whether executed from a terminal, notebook, or any Python-compatible environment, can seamlessly interact with Pathways resources.

## Before you begin

Make sure you have:

  * [Created a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Installed Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Installed the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install)
  * [Enabled the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)
  * Ensure Pathways is enabled for your Google Cloud project



## Run Pathways in interactive mode

  1. Set the following environment variables:
         
         export WORKLOAD=WORKLOAD
         export WORKLOAD_NODEPOOL_COUNT=WORKLOAD_NODEPOOL_COUNT
         export COMPUTE_TYPE="COMPUTE_TYPE"
         export TOPOLOGY="TOPOLOGY"
         export PROJECT_ID=PROJECT_ID
         export REGION=REGION
         export ZONE=ZONE
         export CLUSTER=CLUSTER
         export BUCKET_NAME=BUCKET_NAME

Replace the following:

     * `WORKLOAD`: set this to a unique name to identify your workload (must be 22 characters or fewer due to DNS label limits)
     * `WORKLOAD_NODEPOOL_COUNT`: the number of node pools used by a Pathways workload
     * `COMPUTE_TYPE`: the TPU machine type (for example, `ct6e-standard-4t`). For more information about supported TPU types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `TOPOLOGY`: the TPU placement topology (for example, `2x4`)
     * `PROJECT_ID`: your Google Cloud project ID
     * `REGION`: the region where your bucket and cluster are located
     * `ZONE`: the zone where you plan to run your workload
     * `CLUSTER`: the name of your GKE cluster
     * `BUCKET_NAME`: the Cloud Storage bucket for Pathways artifacts
  2. If you haven't already created a Cloud Storage bucket for Pathways artifacts, create one:
         
         gcloud storage buckets create gs://${BUCKET_NAME} --location=${REGION}
         

  3. Create the Pathways containers on the cluster. To run a headless workload, use the `gcluster job submit` command (for more information, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md)):
         
         gcluster job submit \
             --pathways \
             --pathways-gcs-location="gs://${BUCKET_NAME}/pathways-artifacts" \
             --name=${WORKLOAD} \
             --cluster=${CLUSTER} \
             --project=${PROJECT_ID} \
             --location=${ZONE} \
             --num-slices=${WORKLOAD_NODEPOOL_COUNT} \
             --compute-type=${COMPUTE_TYPE} \
             --topology=${TOPOLOGY} \
             --pathways-headless
         




At this point, your JAX workload can connect to the IFRT proxy server.

## Connecting to the Pathways cluster in interactive mode

You can connect to the Pathways cluster with or without port forwarding. Use one of the following sections to connect to the Pathways cluster.

### Connect using port-forwarding

At this point you can use port-forwarding (from any host with access to your cluster's control plane) to access the proxy server:

Use the command appropriate for your workload:

### Cluster Toolkit
    
    
    PROXY_POD=$(kubectl get pods | grep ${WORKLOAD}-pathways-head | awk '{print $1}')
    PROXY_PORT=29000
    kubectl port-forward ${PROXY_POD} ${PROXY_PORT}:${PROXY_PORT}
    

You should see output similar to:
    
    
    Forwarding from 127.0.0.1:29000 -> 29000
    Forwarding from [::1]:29000 -> 29000
    

### kubectl
    
    
    PROXY_POD=$(kubectl get pods | grep pathways-${USER}-pathways-head | awk '{print $1}')
    PROXY_PORT=29000
    kubectl port-forward ${PROXY_POD} ${PROXY_PORT}:${PROXY_PORT}
    

You should see output similar to:
    
    
    Forwarding from 127.0.0.1:29000 -> 29000
    Forwarding from [::1]:29000 -> 29000
    

On the same host, open a new terminal window. Set the `JAX_PLATFORMS` and `JAX_BACKEND_TARGET` environment variables, and run a Python script that imports `pathwaysutils` and `jax`:
    
    
    python3 -m venv .venv
    source .venv/bin/activate
    pip install pathwaysutils jax
    
    JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://127.0.0.1:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'
    

You should see output like the following:
    
    
    [device(144,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(145,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(146,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(147,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
    device(148,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(149,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(150,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(151,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
    device(162,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(163,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(164,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(165,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
    device(166,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
    device(167,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
    device(168,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
    device(169,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3)]
    Waiting up to 5 seconds.
    Sent all pending logs.
    2024-11-13 21:38:51.267523: W external/xla/xla/python/ifrt_proxy/client/grpc_client.cc:63] IFRT proxy server disconnected: CANCELLED: Cancelled
    

### Connect from hosts in the VPC without using port forwarding

If you don't want to use port forwarding you can connect to the Pathways cluster using Cloud DNS or an internal load balancer.

#### Connect using Cloud DNS

Enabling Cloud DNS in your cluster switches the Cloud DNS provider from kube-dns to Cloud DNS. When enabled, a private Cloud DNS zone is created in your Virtual Private Cloud for the Cloud DNS names. For more information, see [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns).

If you enable Cloud DNS with either the cluster, additive VPC or VPC scope, the Kubernetes Cloud DNS names are resolvable from non-GKE VMs inside your Virtual Private Cloud. The names have the format `<service_name>.<namespace>.svc.<custom_dns_domain>`. The Pathways head Pod has a service named `<jobset_name>-pathways-head-0-0.<jobset_name>.<namespace>.svc.<custom_dns_domain>`.

The following commands show how to connect to your Pathways cluster using Cloud DNS:

  1. Confirm the leader Cloud DNS entry is resolvable from a non-GKE host:

### Cluster Toolkit
         
         host WORKLOAD-pathways-head-0-0.WORKLOAD.default.svc.USERNAME-test

You should see output similar to:
         
         <WORKLOAD>-pathways-head-0-0.<WORKLOAD>.default.svc.<user>-test has address 10.0.2.75

### kubectl
         
         host pathways-USERNAME-pathways-head-0-0.pathways-USERNAME.default.svc.USERNAME-test

You should see output similar to:
         
         pathways-<user>-pathways-head-0-0.pathways-<user>.default.svc.<user>-test has address 10.0.2.75

  2. Connect to the Pathways cluster using the Cloud DNS name:

### Cluster Toolkit
         
         JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://WORKLOAD-pathways-head-0-0.WORKLOAD.default.svc.USERNAME-test:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'

### kubectl
         
         JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://pathways-USERNAME-pathways-head-0-0.pathways-USERNAME.default.svc.USERNAME-test:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'

You should see output similar to:
         
         [device(216,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(217,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(218,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(219,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
         device(220,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(221,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(222,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(223,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
         device(234,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(235,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(236,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(237,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
         device(238,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
         device(239,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
         device(240,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
         device(241,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3)]
         Waiting up to 5 seconds.
         Sent all pending logs.
         2024-11-14 00:02:49.882044: W external/xla/xla/python/ifrt_proxy/client/grpc_client.cc:63] IFRT proxy server disconnected: CANCELLED: Cancelled




#### Connect using an internal load balancer

For a private IP address in your VPC that points to your pathways deployment, create a service backed by an internal load balancer. **This does not require your cluster to have Cloud DNS enabled**.

For clusters with many VMs, we recommend that you enable the ILB subsetting if your are creating internal load balancers. For more information, see [Enable GKE subsetting in an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#enable_ilb_subsetting_existing_cluster). When the ILB subsetting is not enabled, all nodes in the cluster will be part of the backend instance group for all internal load balancers. This does not scale beyond 250 nodes. With ILB subsetting enabled, GKE creates network endpoint groups instead of instance groups and only nodes that are running one of the service's serving Pods are included. Enabling ILB subsetting has a one-time setup latency (~15 minutes). The following command shows how to enable the ILB subsetting:
    
    
    gcloud container clusters update ${CLUSTER} \
      --project=${PROJECT} \
      [--zone=${ZONE} | --region=${REGION}] \
      --enable-l4-ilb-subsetting

Once ILB subsetting is enabled, You can create a Kubernetes service of type LoadBalancer using the following yaml. This will cause GKE to create an internal load balancer inside your cluster's VPC:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: pathways-USERNAME-ilb
      annotations:
        networking.gke.io/load-balancer-type: "Internal"
        networking.gke.io/internal-load-balancer-allow-global-access: "true"
    spec:
      type: LoadBalancer
      externalTrafficPolicy: Local
      selector:
        jobset.sigs.k8s.io/jobset-name: pathways-USER
        jobset.sigs.k8s.io/replicatedjob-name: pathways-head
      ports:
      - name: tcp-port
        protocol: TCP
        port: 29000
        targetPort: 29000

Update the `USER` with your Google Cloud user ID and save the file as `pathways-headless-ilb.yaml`.

Apply the manifest:
    
    
    kubectl apply -f pathways-headless-ilb.yaml
    

After the load balancer is created (~a minute later), the EXTERNAL-IP column will have a value:
    
    
    kubectl get services
    NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
    pathways-$USER       ClusterIP      None            <none>        <none>         30m
    pathways-$USER-ilb   LoadBalancer   34.118.232.46   10.0.0.22     80:31246/TCP   2m41s
    

You can access the pathways deployment without port-forwarding on hosts in the same VPC as your cluster:
    
    
    JAX_PLATFORMS=proxy JAX_BACKEND_TARGET=grpc://10.0.0.22:29000 python -c 'import pathwaysutils; import jax; import pprint; pathwaysutils.initialize(); pprint.pprint(jax.devices())'

**Note:** Replace the IP address of the JAX backend (`10.0.0.22`) in the previous command for the value displayed by `kubectl get services`.

You should see output similar to:
    
    
    [device(288,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(289,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(290,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(291,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=0,default_mem=device,mem_spaces=3),
     device(292,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(293,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(294,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(295,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=0,default_mem=device,mem_spaces=3),
     device(306,TPU_DEVICE,coords=[0,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(307,TPU_DEVICE,coords=[1,0,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(308,TPU_DEVICE,coords=[0,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(309,TPU_DEVICE,coords=[1,1,0,0],vtask=0,slice=1,default_mem=device,mem_spaces=3),
     device(310,TPU_DEVICE,coords=[0,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
     device(311,TPU_DEVICE,coords=[1,0,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
     device(312,TPU_DEVICE,coords=[0,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3),
     device(313,TPU_DEVICE,coords=[1,1,1,0],vtask=1,slice=1,default_mem=device,mem_spaces=3)]
    Waiting up to 5 seconds.
    Sent all pending logs.
    2024-11-14 00:30:07.296917: W external/xla/xla/python/ifrt_proxy/client/grpc_client.cc:63] IFRT proxy server disconnected: CANCELLED: Cancelled
    

**Note:** Your IP addresses will be different than the ones shown in the preceding command and output examples.

## Jupyter notebooks

You can create a Jupyter notebook using Vertex AI or you can create a self hosted Jupyter notebook.

### Create a Vertex AI workbench instance

After setting up and verifying your Pathways cluster, you can access the GKE TPU VMs from a Vertex AI Jupyter notebook. The following setup instructions assume your GKE Pathways cluster resides in the same Virtual Private Cloud network (which is the default network unless you've configured otherwise). Navigate to the [Vertex AI Workbench console](https://console.cloud.google.com/vertex-ai/workbench).

Create a new Workbench instance (from the **Instances** tab) with the **Create new** button. Ensure that the network is the same as your GKE cluster's network. You can use the command line to create a new Workbench instance.
    
    
    gcloud workbench instances create INSTANCE_NAME \
    --machine-type=e2-standard-4 \
    --data-disk-size=100 \
    --location=ZONE \
    [--network=NETWORK]

**Note:** the `--network` flag is optional, if you omit it, the default network is used.

Once the instance is created, navigate to it and click **Open Jupyterlab**.

### Create a self-hosted Jupyter notebook instance

The following command shows how to create a self-hosted Jupyter notebook instance by using the `gcluster job submit` command:
    
    
    gcluster job submit \
        --pathways \
        --name=${WORKLOAD} \
        --cluster=${CLUSTER} \
        --project=${PROJECT_ID} \
        --location=${ZONE} \
        --num-slices=${WORKLOAD_NODEPOOL_COUNT} \
        --compute-type=${COMPUTE_TYPE} \
        --topology=${TOPOLOGY} \
        --pathways-gcs-location="gs://${BUCKET_NAME}/pathways-artifacts" \
        --image=jupyter/base-notebook \
        --command="start-notebook.sh"
    

The following YAML shows how to create a self-hosted Jupyter notebook instance by using `kubectl`. Apply the following YAML after a headless Pathways cluster has been created. For more information, see Run Pathways in interactive mode with kubectl.
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: jupyter-notebook-USERNAME
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
          - name: jupyter-notebook
            image: jupyter/base-notebook  # Use the appropriate Jupyter image
            ports:
            - containerPort: 8888

### Navigate to the notebook instance

Connect to the notebook from your local machine by using port forwarding:

### Cluster Toolkit
    
    
      MAIN_POD=$(kubectl get pods | grep ${WORKLOAD}-pathways-head | awk '{print $1}')
      kubectl port-forward pod/${MAIN_POD} 8888:8888
    

### kubectl
    
    
      MAIN_POD=$(kubectl get pods | grep jupyter-notebook-USERNAME | awk '{print $1}')
      kubectl port-forward pod/${MAIN_POD} 8888:8888
    

Navigate on your local browser to `http://localhost:8888?token=<var>your-token</var>`. Replace `<your-token>` with the token from the Jupyter notebook container's logs.
    
    
    kubectl logs ${MAIN_POD}

Which should output:
    
    
    ...
    Or copy and paste one of these URLs:
      http://jupyter-notebook-<user>-bbbdh:8888/lab?token=<token>
      http://127.0.0.1:8888/lab?token=<token>

### Notebook connectivity to the Pathways cluster

  1. From within Jupyterlab, create a new Python 3 notebook
  2. Connect to the Pathways proxy server



In the notebook, add a cell to install `pathwaysutils`, set `JAX_PLATFORMS` to `proxy`, and set `JAX_BACKEND_TARGET` to `PROXY_ADDRESS`.

**Note:** The value for `PROXY_ADDRESS` depends on the connection option you chose in Connect to the Pathways proxy server.
    
    
    !pip install pathwaysutils
    %env JAX_PLATFORMS=proxy
      # Replace your proxy address below:
    %env JAX_BACKEND_TARGET=PROXY_ADDRESS

Add a second cell as a "hello world" type check and print the devices in the Pathways cluster.
    
    
    import pathwaysutils
    import jax
    
    pathwaysutils.initialize()
    print(jax.devices())
    

If everything is working well, you should see a message indicating the Pathways-on-Cloud backend was detected.

The number of JAX devices listed should match the number of TPU chips and the number of slices you specified when you created the Pathways cluster.

##### Add your code to a notebook

Add your own JAX code and execute interactively on the TPUs in the Pathways cluster. The following code shows how to perform computations across two slices from a single notebook.
    
    
    import jax
    import jax.numpy as jnp
    from jax import lax
    import numpy as np
    
    # You can use JAX APIs as usual across any of the devices.
    jax.jit(jnp.sin, device=jax.devices()[-1])(np.pi / 2.)
    
    # pmap can run across all devices on all slices
    num_tpus = jax.device_count()
    f = jax.pmap(lambda x: lax.psum(1, 'i'), 'i')
    x = jnp.arange(num_tpus)
    y = f(x)
    print(y)
    
    # You can also target devices from a specific slice
    slice0_devices = [d for d in jax.devices() if d.slice_index == 0]
    f = jax.pmap(lambda x: lax.psum(1, 'i'), 'i', devices=slice0_devices)
    x = jnp.arange(len(slice0_devices))
    y = f(x)
    print(y)
    print(y.global_shards)
    
    # You can send data produced on one slice to another slice
    slice1_devices = [d for d in jax.devices() if d.slice_index == 1]
    g = jax.pmap(lambda x: x + lax.axis_index('i'), 'i', devices=slice1_devices)
    z = g(y)
    print(z)
    print(z.global_shards)
    

#### Delete your Pathways interactive workload

### Cluster Toolkit
    
    
    gcluster job cancel WORKLOAD --cluster=CLUSTER --project=PROJECT_ID --location=ZONE
    

### kubectl
    
    
    kubectl delete -f pathways-headless-workload.yaml

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Multihost inference with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
