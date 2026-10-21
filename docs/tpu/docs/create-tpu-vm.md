---
url: https://docs.cloud.google.com/tpu/docs/create-tpu-vm/
title: Create Cloud TPU VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:20.910020+00:00
---

# Create Cloud TPU VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/create-tpu-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create Cloud TPU VMs 

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

You create TPU VMs using the Create Node API, the queued resources API, or Google Kubernetes Engine (GKE).

You call the Create Node API when you run the `gcloud compute tpus tpu-vm create` command using the Google Cloud CLI and when you create a TPU VM using the Google Cloud console. When you use the Create Node API, the system processes your request immediately. If there is not enough capacity to fulfill your request, the request fails.

We recommend creating TPU VMs using the queued resources API. When you create a TPU VM using the queued resource API, the Cloud TPU service adds your queued resource request to a queue that the service maintains. When the requested resource becomes available, the service assigns it to your Google Cloud project for your immediate and exclusive use. For more information, see [Manage queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).

**Note:** When using Multislice, you must use queued resources. For more information, see [Multislice introduction](https://docs.cloud.google.com/tpu/docs/multislice-introduction#set_up_your_environment).

If you want to use Google Kubernetes Engine (GKE) to manage TPU resources, first, create a GKE cluster. Then, add node pools containing TPU slices to your cluster. For more information, see [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

## Prerequisites

Complete the following prerequisites:

  1. Create a Google Cloud project for your TPUs as described in [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

  2. Determine your TPU requirements as described in [Plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).

  3. If you're using one of the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained), follow the setup instructions for the language you're using:

     * [Python](https://docs.cloud.google.com/python/docs/reference/tpu/latest)
     * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/overview)
     * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference)
  4. Set environment variables for creating a v5e TPU with eight chips. The following examples use a v5e TPU with eight chips. You can specify a different accelerator type and version. See [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions) for more information.
         
         export TPU_NAME=your-tpu-name
           export PROJECT_ID=your-project
           export ZONE=us-central1-a
           export ACCELERATOR_TYPE=v5litepod-8
           export VERSION=v2-alpha-tpuv5-lite
         




## Create a Cloud TPU using the Create Node API

You create a Cloud TPU using `gcloud`, the Google Cloud console, or the Cloud TPU API.

When creating a Cloud TPU, specify the TPU software version (also called runtime version). To determine which software version to use, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions).

Also, specify the number of TensorCores or TPU chips for the TPU configuration you are using. For more information, see the section for your TPU version in [System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

### gcloud

**Note:** Use the `--reserved` flag to create a Cloud TPU using a reservation when running the `gcloud compute tpus tpu-vm create` command. Use the `--spot` flag to create [TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot). For more information, see the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create) in the `gcloud` reference.

Use the [`gcloud compute tpus tpu-vm create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create) command to create a TPU using the Create Node API. See [External and internal IP addresses](https://docs.cloud.google.com/tpu/docs/configure-networking-access#custom-network-subnetworks) to configure specific internal or external IP addresses.

The following command creates a v5e TPU VM with 8 TPU chips:
    
    
    gcloud compute tpus tpu-vm create $TPU_NAME \
      --project=$PROJECT_ID
      --zone=$ZONE \
      --accelerator-type=$ACCELERATOR_TYPE \
      --version=$VERSION

#### Command flag descriptions

`zone`
    The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you create your Cloud TPU.
`accelerator-type`
    The accelerator type specifies the version and size of the Cloud TPU you create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
`version`
    The TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
See the [ `gcloud` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create) for more information about all optional flags.

### Console

These instructions create a v5e TPU VM with 8 TPU chips:

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** field, select the zone where you create the TPU.

  5. In the **TPU type** field, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** field, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click **Create** to create your resources.




### curl

The following command uses `curl` to create a v5e TPU VM with 8 TPU chips.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d "{accelerator_type: $ACCELERATOR_TYPE, \
    runtime_version:'$VERSION', \
    network_config: {enable_external_ips: true}, \
    shielded_instance_config: { enable_secure_boot: true }}" \
    https://tpu.googleapis.com/v2/projects/$PROJECT_ID/locations/$ZONE/nodes?node_id=$TPU_NAME

#### Required fields

`runtime_version`
    The Cloud TPU runtime version that you use.
`project-id`
    The name of your enrolled Google Cloud project.
`zone`
    The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you create your Cloud TPU.
`node_name`
    The name of the TPU VM you create.

###  Java 

This code example creates a v5e TPU VM with 8 TPU chips using the Cloud TPU API in Java.

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationTimedPollAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationTimedPollAlgorithm.html);
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.tpu.v2.[CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest.html);
    import com.google.cloud.tpu.v2.[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import com.google.cloud.tpu.v2.[TpuSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuSettings.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import org.threeten.bp.Duration;
    
    public class CreateTpuVm {
    
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
        // The accelerator type that specifies the version and size of the Cloud TPU you want to create.
        // For more information about supported accelerator types for each TPU version,
        // see https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions.
        String tpuType = "v2-8";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information see https://cloud.google.com/tpu/docs/runtimes
        String tpuSoftwareVersion = "v2-tpuv5-litepod";
    
        createTpuVm(projectId, zone, nodeName, tpuType, tpuSoftwareVersion);
      }
    
      // Creates a TPU VM with the specified name, zone, accelerator type, and version.
      public static [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) createTpuVm(
          String projectId, String zone, String nodeName, String tpuType, String tpuSoftwareVersion)
          throws IOException, ExecutionException, InterruptedException {
        // With these settings the client library handles the Operation's polling mechanism
        // and prevent CancellationException error
        [TpuSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuSettings.html).Builder clientSettings =
            [TpuSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuSettings.html).newBuilder();
        clientSettings
            .createNodeOperationSettings()
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
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
    
          [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) tpuVm = [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html).newBuilder()
                  .setName(nodeName)
                  .setAcceleratorType(tpuType)
                  .setRuntimeVersion(tpuSoftwareVersion)
                  .build();
    
          [CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest.html) request = [CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest.html).newBuilder()
                  .setParent(parent)
                  .setNodeId(nodeName)
                  .setNode(tpuVm)
                  .build();
    
          return tpuClient.[createNodeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html#com_google_cloud_tpu_v2_TpuClient_createNodeAsync__org_jspecify_annotations_Nullable_com_google_cloud_tpu_v2_LocationName_com_google_cloud_tpu_v2_Node_java_lang_String_)(request).[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
        }
      }
    }

###  Node.js 

This code example creates a v5e TPU VM with 8 TPU chips using the Cloud TPU API in Node.js.

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    const {Node, NetworkConfig} =
      require('[@google-cloud/tpu](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/overview.html)').protos.google.cloud.tpu.v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update below line before running the sample.
    // Project ID or project number of the Google Cloud project you want to create a node.
    const projectId = await tpuClient.getProjectId();
    
    // The name of the network you want the TPU node to connect to. The network should be assigned to your project.
    const networkName = 'compute-tpu-network';
    
    // The region of the network, that you want the TPU node to connect to.
    const region = 'europe-west4';
    
    // The name for your TPU.
    const nodeName = 'node-name-1';
    
    // The zone in which to create the TPU.
    // For more information about supported TPU types for specific zones,
    // see https://cloud.google.com/tpu/docs/regions-zones
    const zone = 'europe-west4-a';
    
    // The accelerator type that specifies the version and size of the Cloud TPU you want to create.
    // For more information about supported accelerator types for each TPU version,
    // see https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions.
    const tpuType = 'v5litepod-4';
    
    // Software version that specifies the version of the TPU runtime to install. For more information,
    // see https://cloud.google.com/tpu/docs/runtimes
    const tpuSoftwareVersion = 'v2-tpuv5-litepod';
    
    async function callCreateTpuVM() {
      // Create a node
      const node = new Node({
        name: nodeName,
        zone,
        acceleratorType: tpuType,
        runtimeVersion: tpuSoftwareVersion,
        // Define network
        networkConfig: new NetworkConfig({
          enableExternalIps: true,
          network: `projects/${projectId}/global/networks/${networkName}`,
          subnetwork: `projects/${projectId}/regions/${region}/subnetworks/${networkName}`,
        }),
      });
    
      const parent = `projects/${projectId}/locations/${zone}`;
      const request = {parent, node, nodeId: nodeName};
    
      const [operation] = await tpuClient.createNode(request);
    
      // Wait for the create operation to complete.
      const [response] = await operation.promise();
    
      console.log(`TPU VM: ${nodeName} created.`);
      return response;
    }
    return await callCreateTpuVM();

###  Python 

This code example creates a v5e TPU VM with 8 TPU chips using the Cloud TPU API in Python.

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    
    # Create a TPU node
    node = tpu_v2.Node()
    node.accelerator_type = tpu_type
    # To see available runtime version use command:
    # gcloud compute tpus versions list --zone={ZONE}
    node.runtime_version = runtime_version
    
    request = tpu_v2.CreateNodeRequest(
        parent=f"projects/{project_id}/locations/{zone}",
        node_id=tpu_name,
        node=node,
    )
    
    # Create a TPU client
    client = tpu_v2.TpuClient()
    operation = client.[create_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_create_node)(request=request)
    print("Waiting for operation to complete...")
    
    response = operation.result()
    print(response)
    # Example response:
    # name: "projects/[project_id]/locations/[zone]/nodes/my-tpu"
    # accelerator_type: "v5litepod-4"
    # state: READY
    # ...
    

## Run a startup script

You run a startup script on your TPU VM by specifying the `--metadata startup-script` flag when you create the TPU VM.

###  gcloud 

This command creates a TPU VM and specifies a startup script.
    
    
    gcloud compute tpus tpu-vm create $TPU_NAME \
      --zone=$ZONE \
      --accelerator-type=$ACCELERATOR_TYPE \
      --version=$VERSION \
      --metadata startup-script='#! /bin/bash
         pip3 install numpy
         EOF'

###  Java 

This code example creates a TPU VM and specifies a startup script in Java.

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2.[CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest.html);
    import com.google.cloud.tpu.v2.[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html);
    import com.google.cloud.tpu.v2.[TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    
    public class CreateTpuVmWithStartupScript {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to create a node.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which to create the TPU.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "us-central1-a";
        // The name for your TPU.
        String nodeName = "YOUR_TPU_NAME";
        // The accelerator type that specifies the version and size of the Cloud TPU you want to create.
        // For more information about supported accelerator types for each TPU version,
        // see https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions.
        String acceleratorType = "v5litepod-4";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information, see https://cloud.google.com/tpu/docs/runtimes
        String tpuSoftwareVersion = "v2-tpuv5-litepod";
    
        createTpuVmWithStartupScript(projectId, zone, nodeName, acceleratorType, tpuSoftwareVersion);
      }
    
      // Create a TPU VM with a startup script.
      public static [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) createTpuVmWithStartupScript(String projectId, String zone,
          String nodeName, String acceleratorType, String tpuSoftwareVersion)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html) tpuClient = [TpuClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html).create()) {
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
    
          String startupScriptContent = "#!/bin/bash\necho \"Hello from the startup script!\"";
          // Add startup script to metadata
          Map<String, String> metadata = new HashMap<>();
          metadata.put("startup-script", startupScriptContent);
    
          [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html) tpuVm =
              [Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.html).newBuilder()
                 .setName(nodeName)
                 .setAcceleratorType(acceleratorType)
                 .setRuntimeVersion(tpuSoftwareVersion)
                 .[putAllMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.Node.Builder.html#com_google_cloud_tpu_v2_Node_Builder_putAllMetadata_java_util_Map_java_lang_String_java_lang_String__)(metadata)
                 .build();
    
          [CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest.html) request =
              [CreateNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.CreateNodeRequest.html).newBuilder()
                 .setParent(parent)
                 .setNodeId(nodeName)
                 .setNode(tpuVm)
                 .build();
    
          return tpuClient.[createNodeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2.TpuClient.html#com_google_cloud_tpu_v2_TpuClient_createNodeAsync__org_jspecify_annotations_Nullable_com_google_cloud_tpu_v2_LocationName_com_google_cloud_tpu_v2_Node_java_lang_String_)(request).get();
        }
      }
    }

###  Node.js 

This code example creates a TPU VM and specifies a startup script in Node.js.

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the TPUClient
    // TODO(developer): Uncomment below line before running the sample.
    // const {TpuClient} = require('@google-cloud/tpu').v2;
    
    const {Node, NetworkConfig} =
      require('[@google-cloud/tpu](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/overview.html)').protos.google.cloud.tpu.v2;
    
    // Instantiate a tpuClient
    // TODO(developer): Uncomment below line before running the sample.
    // tpuClient = new TpuClient();
    
    // TODO(developer): Update these variables before running the sample.
    // Project ID or project number of the Google Cloud project you want to create a node.
    const projectId = await tpuClient.getProjectId();
    
    // The name of the network you want the TPU node to connect to. The network should be assigned to your project.
    const networkName = 'compute-tpu-network';
    
    // The region of the network, that you want the TPU node to connect to.
    const region = 'europe-west4';
    
    // The name for your TPU.
    const nodeName = 'node-name-1';
    
    // The zone in which to create the TPU.
    // For more information about supported TPU types for specific zones,
    // see https://cloud.google.com/tpu/docs/regions-zones
    const zone = 'europe-west4-a';
    
    // The accelerator type that specifies the version and size of the Cloud TPU you want to create.
    // For more information about supported accelerator types for each TPU version,
    // see https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions.
    const tpuType = 'v5litepod-4';
    
    // Software version that specifies the version of the TPU runtime to install. For more information,
    // see https://cloud.google.com/tpu/docs/runtimes
    const tpuSoftwareVersion = 'v2-tpuv5-litepod';
    
    async function callCreateTpuVMStartupScript() {
      // Create a node
      const node = new Node({
        name: nodeName,
        zone,
        acceleratorType: tpuType,
        runtimeVersion: tpuSoftwareVersion,
        // Define network
        networkConfig: new NetworkConfig({
          enableExternalIps: true,
          network: `projects/${projectId}/global/networks/${networkName}`,
          subnetwork: `projects/${projectId}/regions/${region}/subnetworks/${networkName}`,
        }),
        metadata: {
          // The script updates numpy to the latest version and logs the output to a file.
          'startup-script': `#!/bin/bash
            echo "Hello World" > /var/log/hello.log
            sudo pip3 install --upgrade numpy >> /var/log/hello.log 2>&1`,
        },
      });
    
      const parent = `projects/${projectId}/locations/${zone}`;
      const request = {parent, node, nodeId: nodeName};
    
      const [operation] = await tpuClient.createNode(request);
    
      // Wait for the create operation to complete.
      const [response] = await operation.promise();
    
      console.log(JSON.stringify(response));
      return response;
    }
    return await callCreateTpuVMStartupScript();

###  Python 

This code example creates a TPU VM and specifies a startup script in Python.

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    
    node = tpu_v2.Node()
    node.accelerator_type = tpu_type
    node.runtime_version = runtime_version
    
    # This startup script updates numpy to the latest version and logs the output to a file.
    metadata = {
        "startup-script": """#!/bin/bash
    echo "Hello World" > /var/log/hello.log
    sudo pip3 install --upgrade numpy >> /var/log/hello.log 2>&1
    """
    }
    
    # Adding metadata with startup script to the TPU node.
    node.metadata = metadata
    # Enabling external IPs for internet access from the TPU node.
    node.network_config = tpu_v2.[NetworkConfig](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.types.NetworkConfig.html)(enable_external_ips=True)
    
    request = tpu_v2.CreateNodeRequest(
        parent=f"projects/{project_id}/locations/{zone}",
        node_id=tpu_name,
        node=node,
    )
    
    client = tpu_v2.TpuClient()
    operation = client.[create_node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v1.services.tpu.TpuClient.html#google_cloud_tpu_v1_services_tpu_TpuClient_create_node)(request=request)
    print("Waiting for operation to complete...")
    
    response = operation.result()
    print(response.metadata)
    # Example response:
    # {'startup-script': '#!/bin/bash\n    echo "Hello World" > /var/log/hello.log\n
    # ...
    

## What's next

  * Learn about [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).
  * Learn how to [manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to [run JAX code on a TPU VM](https://docs.cloud.google.com/tpu/docs/run-calculation-jax).
  * Learn how to [run PyTorch code on a TPU VM](https://docs.cloud.google.com/tpu/docs/run-calculation-pytorch).
  * Learn how to run an ML workload on TPUs, for example, [Serve Qwen2-72B-Instruct with vLLM on TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen2-7b-instruct).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
