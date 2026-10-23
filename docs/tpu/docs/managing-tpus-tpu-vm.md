---
url: https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm/
title: Manage TPU resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:20.888443+00:00
---

# Manage TPU resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage TPU resources

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This page describes how to list, stop, start, delete, and connect to TPU VMs.

## Prerequisites

Before you run these procedures, complete the following steps:

  1. Create a Google Cloud project for your TPUs as described in [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

  2. Determine your TPU requirements as described in [Plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).

  3. Create a TPU VM as described in [Create a TPU VM](https://docs.cloud.google.com/tpu/docs/create-tpu-vm).

  4. If you use one of the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained), follow the setup instructions for the language you're using:

     * [Python](https://docs.cloud.google.com/python/docs/reference/tpu/latest)
     * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/overview)
     * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest)
  5. Set up environment variables.
         
         export TPU_NAME=your-tpu-name
           export ZONE=your-zone
         




## Connect to a Cloud TPU

You can connect to a Cloud TPU using SSH.

If you can't connect to a TPU VM using SSH, the TPU VM might not have an external IP address. To access a TPU VM without an external IP address, follow the instructions in [Connect to a TPU VM without a public IP address](https://docs.cloud.google.com/tpu/docs/tpu-iap).

### gcloud

Connect to your Cloud TPU using SSH:
    
    
    $ gcloud compute tpus tpu-vm ssh $TPU_NAME --zone=$ZONE

When you request a slice larger than a single host, Cloud TPU creates a TPU VM for each host. The number of TPU chips per host depends on the [TPU version](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

To install binaries or run code, connect to each TPU VM using the `tpu-vm ssh` [command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/ssh).
    
    
    $ gcloud compute tpus tpu-vm ssh $TPU_NAME --zone=$ZONE

To connect to a specific TPU VM using SSH, use the `--worker` flag with a 0-based index:
    
    
    $ gcloud compute tpus tpu-vm ssh $TPU_NAME --zone=$ZONE --worker=1

To run a command on all TPU VMs, use the `--worker=all` and `--command` flags:
    
    
    $ gcloud compute tpus tpu-vm ssh $TPU_NAME \
      --zone=$ZONE \
      --worker=all \
      --command='pip install "jax[tpu]==0.4.20" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html'

For Multislice, you can run a command on a single VM using the enumerated TPU name, with each slice prefix and the number appended to it. To run a command on all TPU VMs in all slices, use the `--node=all`, `--worker=all`, and `--command` flags, with an optional [`--batch-size`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/ssh#--batch-size) flag.
    
    
    $ gcloud compute tpus queued-resources ssh your-queued-resource-id \
      --zone=$ZONE \
      --node=all \
      --worker=all \
      --command='pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html' \
      --batch-size=4

When you connect to VMs using the Google Cloud CLI, Compute Engine creates a persistent SSH key.

### Console

To connect to your TPUs in the Google Cloud console, use SSH in your browser:

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. In the list of TPU VMs, click **SSH** in the row of the TPU VM that you want to connect to.

When you connect to TPU VMs using the Google Cloud console, Compute Engine creates an ephemeral SSH key.




## List Cloud TPU resources

You can list all Cloud TPU resources in a specified zone.

### gcloud
    
    
    $ gcloud compute tpus tpu-vm list --zone=$ZONE

### Console

In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2.[ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListNodesRequest.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import java.io.IOException;
    
    public class ListTpuVms {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // The zone where the TPUs are located.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "us-central1-f";
    
        listTpuVms(projectId, zone);
      }
    
      // Lists TPU VMs in the specified zone.
      public static [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).[ListNodesPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.ListNodesPage.html) listTpuVms(String projectId, String zone)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html) tpuClient = [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).create()) {
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
    
          [ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListNodesRequest.html) request = [ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.ListNodesRequest.html).newBuilder().setParent(parent).build();
    
          return tpuClient.listNodes(request).getPage();
        }
      }
    }

###  Node.js 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update these variables before running the sample.
    // Project ID or project number of the Google Cloud project you want to retrive a list of TPU nodes.
    const projectId = await tpuClient.getProjectId();
    
    // The zone from which the TPUs are retrived.
    const zone = 'europe-west4-a';
    
    async function callTpuVMList() {
      const request = {
        parent: `projects/${projectId}/locations/${zone}`,
      };
    
      const [response] = await tpuClient.listNodes(request);
    
      return response;
    }
    
    return await callTpuVMList();

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    
    client = tpu_v2.TpuClient()
    
    nodes = client.[list_nodes](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_list_nodes)(parent=f"projects/{project_id}/locations/{zone}")
    for node in nodes:
        print(node.name)
        print(node.state)
        print(node.accelerator_type)
    # Example response:
    # projects/[project_id]/locations/[zone]/nodes/node-name
    # State.READY
    # v2-8
    

## Retrieve Cloud TPU information

You can retrieve information about a specific Cloud TPU.

### gcloud
    
    
    $ gcloud compute tpus tpu-vm describe $TPU_NAME \
      --zone=$ZONE

### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click the name of your Cloud TPU. The console displays the Cloud TPU details page.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2.[GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetNodeRequest.html);
    import com.google.cloud.tpu.v2.[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html);
    import com.google.cloud.tpu.v2.[NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import java.io.IOException;
    
    public class GetTpuVm {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which to create the TPU.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "europe-west4-a";
        // The name for your TPU.
        String nodeName = "YOUR_TPU_NAME";
    
        getTpuVm(projectId, zone, nodeName);
      }
    
      // Describes a TPU VM with the specified name in the given project and zone.
      public static [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) getTpuVm(String projectId, String zone, String nodeName)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html) tpuClient = [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).create()) {
          String name = [NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html).of(projectId, zone, nodeName).toString();
    
          [GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetNodeRequest.html) request = [GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.GetNodeRequest.html).newBuilder().setName(name).build();
    
          return tpuClient.getNode(request);
        }
      }
    }

###  Node.js 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update these variables before running the sample.
    // Project ID or project number of the Google Cloud project you want to retrive a node.
    const projectId = await tpuClient.getProjectId();
    
    // The name of TPU to retrive.
    const nodeName = 'node-name-1';
    
    // The zone, where the TPU is created.
    const zone = 'europe-west4-a';
    
    async function callGetTpuVM() {
      const request = {
        name: `projects/${projectId}/locations/${zone}/nodes/${nodeName}`,
      };
    
      const [response] = await tpuClient.getNode(request);
    
      console.log(`Node: ${nodeName} retrived.`);
      return response;
    }
    
    return await callGetTpuVM();

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    # tpu_name = "tpu-name"
    
    client = tpu_v2.TpuClient()
    node = client.[get_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_get_node)(
        name=f"projects/{project_id}/locations/{zone}/nodes/{tpu_name}"
    )
    
    print(node)
    # Example response:
    # name: "projects/[project_id]/locations/[zone]/nodes/tpu-name"
    # state: "READY"
    # runtime_version: ...
    

## Stop Cloud TPU resources

You can stop a single Cloud TPU to avoid incurring charges without losing its VM configuration and software.

The [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources) API does not support stopping TPU slices or TPUs. To stop incurring charges for TPUs allocated through the queued resources API, delete the TPU.

### gcloud
    
    
    $ gcloud compute tpus tpu-vm stop $TPU_NAME \
      --zone=$ZONE

### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Select the checkbox next to your Cloud TPU.

  3. Click stop **Stop**.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2.[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html);
    import com.google.cloud.tpu.v2.[NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html);
    import com.google.cloud.tpu.v2.[StopNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StopNodeRequest.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class StopTpuVm {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // The zone where the TPU is located.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "us-central1-f";
        // The name for your TPU.
        String nodeName = "YOUR_TPU_NAME";
    
        stopTpuVm(projectId, zone, nodeName);
      }
    
      // Stops a TPU VM with the specified name in the given project and zone.
      public static [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) stopTpuVm(String projectId, String zone, String nodeName)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html) tpuClient = [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).create()) {
          String name = [NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html).of(projectId, zone, nodeName).toString();
    
          [StopNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StopNodeRequest.html) request = [StopNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StopNodeRequest.html).newBuilder().setName(name).build();
    
          return tpuClient.[stopNodeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html#com_google_cloud_tpu_v2_TpuClient_stopNodeAsync_com_google_cloud_tpu_v2_StopNodeRequest_)(request).get();
        }
      }
    }

###  Node.js 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update these variables before running the sample.
    // Project ID or project number of the Google Cloud project you want to stop a node.
    const projectId = await tpuClient.getProjectId();
    
    // The name of TPU to stop.
    const nodeName = 'node-name-1';
    
    // The zone, where the TPU is created.
    const zone = 'europe-west4-a';
    
    async function callStopTpuVM() {
      const request = {
        name: `projects/${projectId}/locations/${zone}/nodes/${nodeName}`,
      };
    
      const [operation] = await tpuClient.stopNode(request);
      // Wait for the operation to complete.
      const [response] = await operation.promise();
    
      console.log(`Node: ${nodeName} stopped.`);
      return response;
    }
    
    return await callStopTpuVM();

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    
    client = tpu_v2.TpuClient()
    
    request = tpu_v2.StopNodeRequest(
        name=f"projects/{project_id}/locations/{zone}/nodes/{tpu_name}",
    )
    try:
        operation = client.[stop_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_stop_node)(request=request)
        print("Waiting for stop operation to complete...")
        response = operation.result()
        print(f"This TPU {tpu_name} has been stopped")
        print(response.state)
        # Example response:
        # State.STOPPED
    
    except Exception as e:
        print(e)
        raise e
    

## Start Cloud TPU resources

You can start a stopped Cloud TPU.

The [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources) API does not support starting TPU Pods or TPUs.

### gcloud
    
    
    $ gcloud compute tpus tpu-vm start $TPU_NAME \
      --zone=$ZONE

### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Select the checkbox next to your Cloud TPU.

  3. Click play_arrow **Start**.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2.[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html);
    import com.google.cloud.tpu.v2.[NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html);
    import com.google.cloud.tpu.v2.[StartNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StartNodeRequest.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class StartTpuVm {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // The zone where the TPU is located.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "us-central1-f";
        // The name for your TPU.
        String nodeName = "YOUR_TPU_NAME";
    
        startTpuVm(projectId, zone, nodeName);
      }
    
      // Starts a TPU VM with the specified name in the given project and zone.
      public static [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) startTpuVm(String projectId, String zone, String nodeName)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html) tpuClient = [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).create()) {
          String name = [NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html).of(projectId, zone, nodeName).toString();
    
          [StartNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StartNodeRequest.html) request = [StartNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.StartNodeRequest.html).newBuilder().setName(name).build();
    
          return tpuClient.[startNodeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html#com_google_cloud_tpu_v2_TpuClient_startNodeAsync_com_google_cloud_tpu_v2_StartNodeRequest_)(request).get();
        }
      }
    }

###  Node.js 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update these variables before running the sample.
    // Project ID or project number of the Google Cloud project you want to start a node.
    const projectId = await tpuClient.getProjectId();
    
    // The name of TPU to start.
    const nodeName = 'node-name-1';
    
    // The zone, where the TPU is created.
    const zone = 'europe-west4-a';
    
    async function callStartTpuVM() {
      const request = {
        name: `projects/${projectId}/locations/${zone}/nodes/${nodeName}`,
      };
    
      const [operation] = await tpuClient.startNode(request);
    
      // Wait for the operation to complete.
      const [response] = await operation.promise();
    
      console.log(`Node: ${nodeName} started.`);
      return response;
    }
    
    return await callStartTpuVM();

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    
    client = tpu_v2.TpuClient()
    
    request = tpu_v2.StartNodeRequest(
        name=f"projects/{project_id}/locations/{zone}/nodes/{tpu_name}",
    )
    try:
        operation = client.[start_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_start_node)(request=request)
        print("Waiting for start operation to complete...")
        response = operation.result()
        print(f"TPU {tpu_name} has been started")
        print(response.state)
        # Example response:
        # State.READY
    
    except Exception as e:
        print(e)
        raise e
    

## Delete a Cloud TPU

Delete your TPU VM slices after your session.

### gcloud
    
    
    $ gcloud compute tpus tpu-vm delete $TPU_NAME \
      --zone=$ZONE \
      --quiet

#### Command flag descriptions

  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to delete your Cloud TPU.
  * `quiet`: Disables all interactive prompts when running gcloud CLI commands.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Select the checkbox next to your Cloud TPU.

  3. Click delete **Delete**.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.tpu.v2.[DeleteNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.DeleteNodeRequest.html);
    import com.google.cloud.tpu.v2.[NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import com.google.cloud.tpu.v2.[TpuSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuSettings.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import org.threeten.bp.Duration;
    
    public class DeleteTpuVm {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to create a node.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which to create the TPU.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "europe-west4-a";
        // The name for your TPU.
        String nodeName = "YOUR_TPU_NAME";
    
        deleteTpuVm(projectId, zone, nodeName);
      }
    
      // Deletes a TPU VM with the specified name in the given project and zone.
      public static void deleteTpuVm(String projectId, String zone, String nodeName)
          throws IOException, ExecutionException, InterruptedException {
        // With these settings the client library handles the Operation's polling mechanism
        // and prevent CancellationException error
        [TpuSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuSettings.html).Builder clientSettings =
            [TpuSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuSettings.html).newBuilder();
        clientSettings
            .deleteNodeOperationSettings()
            .setPollingAlgorithm(
                [OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html).create(
                    [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                        .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(5000L))
                        .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(1.5)
                        .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(45000L))
                        .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                        .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1.0)
                        .[setMaxRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                        .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofHours(24L))
                        .build()));
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html) tpuClient = [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).create(clientSettings.build())) {
          String name = [NodeName](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.NodeName.html).of(projectId, zone, nodeName).toString();
    
          [DeleteNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.DeleteNodeRequest.html) request = [DeleteNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.DeleteNodeRequest.html).newBuilder().setName(name).build();
    
          tpuClient.[deleteNodeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html#com_google_cloud_tpu_v2_TpuClient_deleteNodeAsync__org_jspecify_annotations_Nullable_com_google_cloud_tpu_v2_NodeName_)(request).[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.println("TPU VM deleted");
        }
      }
    }

###  Node.js 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update these variables before running the sample.
    // Project ID or project number of the Google Cloud project you want to delete a node.
    const projectId = await tpuClient.getProjectId();
    
    // The name of TPU to delete.
    const nodeName = 'node-name-1';
    
    // The zone, where the TPU is created.
    const zone = 'europe-west4-a';
    
    async function callDeleteTpuVM() {
      const request = {
        name: `projects/${projectId}/locations/${zone}/nodes/${nodeName}`,
      };
    
      const [operation] = await tpuClient.deleteNode(request);
    
      // Wait for the delete operation to complete.
      const [response] = await operation.promise();
    
      console.log(`Node: ${nodeName} deleted.`);
      return response;
    }
    
    return await callDeleteTpuVM();

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    # tpu_name = "tpu-name"
    
    client = tpu_v2.TpuClient()
    try:
        client.[delete_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_delete_node)(
            name=f"projects/{project_id}/locations/{zone}/nodes/{tpu_name}"
        )
        print("The TPU node was deleted.")
    except Exception as e:
        print(e)
    

## What's next

  * Learn how to [configure networking and access to your Cloud TPU](https://docs.cloud.google.com/tpu/docs/configure-networking-access)
  * Learn about [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to [run JAX code on a TPU VM](https://docs.cloud.google.com/tpu/docs/run-calculation-jax).
  * Learn how to [run PyTorch code on a TPU VM](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
