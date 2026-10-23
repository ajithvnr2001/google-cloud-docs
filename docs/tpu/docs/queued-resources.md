---
url: https://docs.cloud.google.com/tpu/docs/queued-resources/
title: Manage queued resources \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:18.621978+00:00
---

# Manage queued resources  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/queued-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage queued resources

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

Queued resources enable you to request Cloud TPU resources in a queued manner. When you create a queued resource request, the request is added to a queue maintained by the Cloud TPU service. When the resource you requested becomes available, it's assigned to your Google Cloud project for your immediate and exclusive use. It will remain assigned to your project unless you delete it or it's preempted. Only TPU Spot VMs and preemptible TPUs are eligible for preemption.

**Note:** The examples shown in this document use TPU v5e. If you want to use a different TPU version, update the `--accelerator-type` and `--runtime-version` flags. For more information about TPU versions, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). For more information about runtime versions, see [TPU runtime versions](https://docs.cloud.google.com/tpu/docs/runtimes).

You can specify an optional start and end time in a queued resource request. The start time specifies the earliest time in which to fill the request. If a request has not been filled by the specified end time, the request expires. The request remains in the queue after it has expired.

Queued resource requests can be in one the following states:

  * `WAITING_FOR_RESOURCES`: The request has passed initial validation and has been added to the queue. It remains in this state until there are sufficient free resources to begin provisioning your request or the allocation interval elapses. When demand is high, not all requests can be immediately provisioned. If you need more reliable obtainability of TPUs, consider purchasing a reservation. **Important:** `WAITING_FOR_RESOURCES` replaced the `ACCEPTED` state. If your code has logic that waits for queued resources to enter the `ACCEPTED` state, you may need to update the code to wait for the `WAITING_FOR_RESOURCES` state. 
  * `PROVISIONING`: The request has been selected from the queue and its resources are being allocated.
  * `ACTIVE`: The request has been allocated. When queued resource requests are in the `ACTIVE` state, you can manage your TPU VMs as described in [Manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm). 
  * `FAILED`: The request couldn't be completed, either because there is a problem with the request or the requested resources were not available within the allocation interval. The request remains in the queue until it is explicitly deleted.
  * `SUSPENDING`: The resources associated with the request are being deleted.
  * `SUSPENDED`: The resources specified in the request have been deleted. When a request is in the `SUSPENDED` state, it's no longer eligible for further allocation.



## Prerequisites

Before you run the commands in this guide, you must install the Google Cloud CLI, create a Google Cloud project, and enable the Cloud TPU API. For instructions, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

If you're using one of the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained), follow the setup instructions for the language you're using:

  * [Python](https://docs.cloud.google.com/python/docs/reference/tpu/latest)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/overview)



## Request an on-demand queued resource

On-demand resources won't be preempted, but on-demand quota doesn't guarantee there will be enough available Cloud TPU resources to satisfy your request. For more information about on-demand resources, see [Quota types](https://docs.cloud.google.com/tpu/docs/quota#quota_types).

###  gcloud 
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-central1-a \
        --accelerator-type v5litepod-8 \
        --runtime-version v2-alpha-tpuv5-lite

#### Command parameter descriptions

  * `queued-resource-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-assigned ID of the TPU which is created when the queued resource request is allocated.
  * `project`: Your Google Cloud project.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)



### curl
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-central1-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5litepod-8',
            'runtime_version': 'v2-alpha-tpuv5-lite',
            }
        }
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-central1-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-assigned ID of the TPU which is created when the queued resource request is allocated.
  * `project`: Your Google Cloud project.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. Click **Create** to create your queued resource request.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2alpha1.CreateQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.Node;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateQueuedResource {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to create a node.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which to create the TPU.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "us-central1-a";
        // The name for your TPU.
        String nodeName = "YOUR_NODE_ID";
        // The accelerator type that specifies the version and size of the Cloud TPU you want to create.
        // For more information about supported accelerator types for each TPU version,
        // see https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions.
        String tpuType = "v5litepod-4";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information see https://cloud.google.com/tpu/docs/runtimes
        String tpuSoftwareVersion = "v2-tpuv5-litepod";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
    
        createQueuedResource(
            projectId, zone, queuedResourceId, nodeName, tpuType, tpuSoftwareVersion);
      }
    
      // Creates a Queued Resource
      public static QueuedResource createQueuedResource(String projectId, String zone,
          String queuedResourceId, String nodeName, String tpuType, String tpuSoftwareVersion)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        String resource = String.format("projects/%s/locations/%s/queuedResources/%s",
                projectId, zone, queuedResourceId);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
          Node node =
              Node.newBuilder()
                  .setName(nodeName)
                  .setAcceleratorType(tpuType)
                  .setRuntimeVersion(tpuSoftwareVersion)
                  .setQueuedResource(resource)
                  .build();
    
          QueuedResource queuedResource =
              QueuedResource.newBuilder()
                  .setName(queuedResourceId)
                  .setTpu(
                      QueuedResource.Tpu.newBuilder()
                          .addNodeSpec(
                              QueuedResource.Tpu.NodeSpec.newBuilder()
                                  .setParent(parent)
                                  .setNode(node)
                                  .setNodeId(nodeName)
                                  .build())
                          .build())
                  .build();
    
          CreateQueuedResourceRequest request =
              CreateQueuedResourceRequest.newBuilder()
                  .setParent(parent)
                  .setQueuedResourceId(queuedResourceId)
                  .setQueuedResource(queuedResource)
                  .build();
    
          return tpuClient.createQueuedResourceAsync(request).get(1, TimeUnit.MINUTES);
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    # queued_resource_name = "resource-name"
    
    node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
    node.accelerator_type = tpu_type
    # To see available runtime version use command:
    # gcloud compute tpus versions list --zone={ZONE}
    node.runtime_version = runtime_version
    
    node_spec = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html).[NodeSpec](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.html)()
    node_spec.parent = f"projects/{project_id}/locations/{zone}"
    node_spec.node_id = tpu_name
    node_spec.node = node
    
    resource = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html)()
    resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html) = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html)(node_spec=[node_spec])
    
    request = tpu_v2alpha1.[CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest.html)(
        parent=f"projects/{project_id}/locations/{zone}",
        queued_resource_id=queued_resource_name,
        queued_resource=resource,
    )
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    operation = client.[create_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_create_queued_resource)(request=request)
    
    response = operation.result()
    print(response.name)
    print(response.state)
    # Example response:
    # projects/[project_id]/locations/[zone]/queuedResources/resource-name
    # State.WAITING_FOR_RESOURCES
    

**Important:** Queued resources consume quota regardless of the state of the queued resource request. You should delete queued resources after use to avoid blocking future requests on quota limits. For more information about TPU quotas, see [TPU quota](https://docs.cloud.google.com/tpu/docs/quota).

## Request a queued resource using a reservation

You can request a queued resource using a reservation. To purchase a reservation, contact your Google Cloud account team.

###  gcloud 
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-central1-a \
        --accelerator-type v5litepod-8 \
        --runtime-version v2-alpha-tpuv5-lite \
        --reserved

#### Command parameter descriptions

  * `queued-resource-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-assigned ID of the TPU which is created when the queued resource request is allocated.
  * `project`: Your Google Cloud project.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `reserved`: Use this flag when requesting queued resources as part of a Cloud TPU reservation.



### curl
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-central1-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5litepod-8',
            'runtime_version': 'v2-alpha-tpuv5-lite',
            }
        }
        },
        'guaranteed': {
        'reserved': true,
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-central1-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-assigned ID of the TPU which is created when the queued resource request is allocated.
  * `project`: Your Google Cloud project.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `reserved`: Use this flag when requesting queued resources as part of a Cloud TPU reservation.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. Expand the **Management** section.

  10. Select the **Use existing reservation** checkbox.

  11. Click **Create** to create your queued resource request.




## Request a TPU Spot VM queued resource

A [Spot VM](https://docs.cloud.google.com/tpu/docs/spot) is a resource that can be preempted and assigned to another workload at any time. Spot VM resources cost less, and you might get access to resources sooner compared to a non-Spot VM request. For more information about TPU Spot VMs, see [Manage TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot).

###  gcloud 
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-central1-a \
        --accelerator-type v5litepod-8 \
        --runtime-version v2-alpha-tpuv5-lite \
        --spot

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `spot`: A boolean flag specifying that the queued resource is a Spot VM.



### curl
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-central1-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5litepod-8',
            'runtime_version': 'v2-alpha-tpuv5-lite'
            }
        }
        },
        'spot': {}
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-central1-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `spot`: A boolean flag specifying that the queued resource is a Spot VM.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. Expand the **Management** section.

  10. Select the **Make this a TPU Spot VM** checkbox.

  11. Click **Create**.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2alpha1.CreateQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.Node;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.SchedulingConfig;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateSpotQueuedResource {
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
        String tpuType = "v5litepod-4";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information see https://cloud.google.com/tpu/docs/runtimes
        String tpuSoftwareVersion = "v2-tpuv5-litepod";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
    
        createQueuedResource(
            projectId, zone, queuedResourceId, nodeName, tpuType, tpuSoftwareVersion);
      }
    
      // Creates a Queued Resource with --preemptible flag.
      public static QueuedResource createQueuedResource(
          String projectId, String zone, String queuedResourceId,
          String nodeName, String tpuType, String tpuSoftwareVersion)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
          String resourceName = String.format("projects/%s/locations/%s/queuedResources/%s",
                  projectId, zone, queuedResourceId);
          SchedulingConfig schedulingConfig = SchedulingConfig.newBuilder()
              .setPreemptible(true)
              .build();
    
          Node node =
              Node.newBuilder()
                  .setName(nodeName)
                  .setAcceleratorType(tpuType)
                  .setRuntimeVersion(tpuSoftwareVersion)
                  .setSchedulingConfig(schedulingConfig)
                  .setQueuedResource(resourceName)
                  .build();
    
          QueuedResource queuedResource =
              QueuedResource.newBuilder()
                  .setName(queuedResourceId)
                  .setTpu(
                      QueuedResource.Tpu.newBuilder()
                          .addNodeSpec(
                              QueuedResource.Tpu.NodeSpec.newBuilder()
                                  .setParent(parent)
                                  .setNode(node)
                                  .setNodeId(nodeName)
                                  .build())
                          .build())
                  .build();
    
          CreateQueuedResourceRequest request =
              CreateQueuedResourceRequest.newBuilder()
                  .setParent(parent)
                  .setQueuedResourceId(queuedResourceId)
                  .setQueuedResource(queuedResource)
                  .build();
    
          return tpuClient.createQueuedResourceAsync(request).get();
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    # queued_resource_name = "resource-name"
    
    node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
    node.accelerator_type = tpu_type
    # To see available runtime version use command:
    # gcloud compute tpus versions list --zone={ZONE}
    node.runtime_version = runtime_version
    
    node_spec = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html).[NodeSpec](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.html)()
    node_spec.parent = f"projects/{project_id}/locations/{zone}"
    node_spec.node_id = tpu_name
    node_spec.node = node
    
    resource = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html)()
    resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html) = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html)(node_spec=[node_spec])
    # Create a spot resource
    resource.spot = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Spot](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Spot.html)()
    
    request = tpu_v2alpha1.[CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest.html)(
        parent=f"projects/{project_id}/locations/{zone}",
        queued_resource_id=queued_resource_name,
        queued_resource=resource,
    )
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    operation = client.[create_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_create_queued_resource)(request=request)
    response = operation.result()
    
    print(response.name)
    print(response.state)
    # Example response:
    # projects/[project_id]/locations/[zone]/queuedResources/resource-name
    # State.WAITING_FOR_RESOURCES
    

## Request a queued resource to be allocated before or after a specified time

You can specify an optional start time or end time in a queued resource request. The start time or start duration specifies the earliest time in which to fill the request. The end time or end duration specifies how long the request remains valid. If a request hasn't been filled by the specified end time or within the specified duration, the request expires. After the request has expired, it remains in the queue but is no longer eligible for allocation.

You can also specify an allocation interval by specifying a start time or duration and an end time or duration.

For a list of supported timestamp and duration formats, see [Datetime](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes).

### Request a queued resource to be fulfilled after a specified time

In a queued resource request, you can specify a time or duration after which a resource should be allocated.

###  gcloud 

The following command requests a v5p-4096 TPU with to be allocated after 9AM on December 14, 2022.
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-east5-a \
        --accelerator-type v5p-4096 \
        --runtime-version v2-alpha-tpuv5 \
        --valid-after-time 2022-12-14T09:00:00Z

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-after-time`: The time, after which, the resource should be allocated For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).



### curl

The following command requests a v5p-4096 TPU with to be allocated after 9AM on December 14, 2022.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-east5-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5p-4096',
            'runtime_version': 'v2-alpha-tpuv5',
            }
        }
        },
        'queueing_policy': {
        'valid_after_time': {
            'seconds': 2022-12-14T09:00:00Z
        }
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-east5-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-after-time`: The time, after which, the resource should be allocated For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. In the **Start request on** field, enter the time after which the resource should be allocated.

  10. Click **Create** to create your queued resource request.




The following example requests a v5p-32 to be allocated after six hours.

**Note:** Specifying a duration for the start time of the queued resource request is not supported in the Google Cloud console.

###  gcloud 
    
    
        gcloud compute tpus queued-resources create your-queued-resource-id \
            --node-id your-node-id \
            --project your-project-id \
            --zone us-east5-a \
            --accelerator-type v5p-32 \
            --runtime-version v2-alpha-tpuv5 \
            --valid-after-duration 6h

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-after-duration`: The duration before which the TPU must not be provisioned. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)



### curl
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-east5-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5p-32',
            'runtime_version': 'v2-alpha-tpuv5',
            }
        }
        },
    'queueing_policy': {
        'valid_after_duration': {
            'seconds': 21600
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-east5-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-after-duration`: The duration before which the TPU must not be provisioned. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)



###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2alpha1.CreateQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.Node;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class CreateTimeBoundQueuedResource {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to create a node.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which to create the TPU.
        // For more information about supported TPU types for specific zones,
        // see https://cloud.google.com/tpu/docs/regions-zones
        String zone = "us-central2-b";
        // The name of your node.
        String nodeId = "YOUR_NODE_ID";
        // The accelerator type that specifies the version and size of the Cloud TPU you want to create.
        // For more information about supported accelerator types for each TPU version,
        // see https://cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions.
        String acceleratorType = "v2-8";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information see https://cloud.google.com/tpu/docs/runtimes
        String runtimeVersion = "v2-tpuv5-litepod";
        // The name of your Queued Resource.
        String queuedResourceId = "YOUR_QUEUED_RESOURCE_ID";
    
        createTimeBoundQueuedResource(projectId, nodeId,
            queuedResourceId, zone, acceleratorType, runtimeVersion);
      }
    
      // Creates a Queued Resource with time bound configuration.
      public static QueuedResource createTimeBoundQueuedResource(
          String projectId, String nodeId, String queuedResourceId,
          String zone, String acceleratorType, String runtimeVersion)
              throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
          // Create a Duration object representing 6 hours.
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) validAfterDuration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(6 * 3600).build();
          // You could also use timestamps like this:
          // Timestamp validAfterTime = Timestamps.parse("2024-10-14T09:00:00Z");
    
          Node node =
              Node.newBuilder()
                  .setName(nodeId)
                  .setAcceleratorType(acceleratorType)
                  .setRuntimeVersion(runtimeVersion)
                  .setQueuedResource(
                      String.format(
                          "projects/%s/locations/%s/queuedResources/%s",
                          projectId, zone, queuedResourceId))
                  .build();
    
          QueuedResource queuedResource =
              QueuedResource.newBuilder()
                  .setName(queuedResourceId)
                  .setTpu(
                      QueuedResource.Tpu.newBuilder()
                          .addNodeSpec(
                              QueuedResource.Tpu.NodeSpec.newBuilder()
                                  .setParent(parent)
                                  .setNode(node)
                                  .setNodeId(nodeId)
                                  .build())
                          .build())
                  .setQueueingPolicy(
                      QueuedResource.QueueingPolicy.newBuilder()
                          .setValidAfterDuration(validAfterDuration)
                          // .setValidAfterTime(validAfterTime)
                          .build())
                  .build();
    
          CreateQueuedResourceRequest request =
              CreateQueuedResourceRequest.newBuilder()
                  .setParent(parent)
                  .setQueuedResource(queuedResource)
                  .setQueuedResourceId(queuedResourceId)
                  .build();
    
          return tpuClient.createQueuedResourceAsync(request).get();
        }
      }
    }

### Request a queued resource that expires after a specified time

In a queued resource request, you can specify how long a queued resource request remains valid. If the request hasn't been fulfilled by the time or duration you specify, the request expires.

###  gcloud 

The following command requests a v5p-4096 TPU. If the request isn't fulfilled by December 14, 2022 at 9:00 AM, the request expires.
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-east5-a \
        --accelerator-type v5p-4096 \
        --runtime-version v2-alpha-tpuv5 \
        --valid-until-time 2022-12-14T09:00:00Z

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-until-time`: The time after which the request is canceled. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).



### curl

The following command requests a v5p-4096 TPU. If the request isn't fulfilled by December 14, 2022 at 9:00 AM, the request expires.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-east5-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5p-4096',
            'runtime_version': 'v2-alpha-tpuv5',
            }
        }
        },
        'queueing_policy': {
        'valid_until_time': {
            'seconds': 1655197200
        }
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-east5-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-until-time`: The time after which the request is canceled. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. In the **Cancel request on** field, enter the time when the queued resource request should expire if not filled.

  10. Click **Create** to create your queued resource request.




The following example requests a v5p-32. The request expires if it's not filled in six hours.

**Note:** Specifying a duration for the time the request expires is not supported in the Google Cloud console.

###  gcloud 
    
    
        gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-east5-a \
        --accelerator-type v5p-32 \
        --runtime-version v2-alpha-tpuv5 \
        --valid-until-duration 6h

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-until-duration`: The duration for which the request is valid. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)



### curl
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-east5-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5p-32',
            'runtime_version': 'v2-alpha-tpuv5',
            }
        }
        },
    'queueing_policy': {
        'valid_until_duration': {
            'seconds': 21600
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-east5-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-until-duration`: The duration for which the request is valid. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes)



###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    # queued_resource_name = "resource-name"
    
    node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
    node.accelerator_type = tpu_type
    # To see available runtime version use command:
    # gcloud compute tpus versions list --zone={ZONE}
    node.runtime_version = runtime_version
    
    node_spec = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html).[NodeSpec](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.html)()
    node_spec.parent = f"projects/{project_id}/locations/{zone}"
    node_spec.node_id = tpu_name
    node_spec.node = node
    
    resource = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html)()
    resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html) = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html)(node_spec=[node_spec])
    
    # Use one of the following queueing policies
    resource.queueing_policy = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[QueueingPolicy](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.QueueingPolicy.html)(
        # valid_after_duration = "6000s", # Duration after which a resource should be allocated
        valid_until_duration="90s",  # Specify how long a queued resource request remains valid
        # valid_after_time="2024-10-31T09:00:00Z", # Specify a time after which a resource should be allocated
        # valid_until_time="2024-10-29T16:00:00Z",  # Specify a time before which the resource should be allocated
    )
    
    request = tpu_v2alpha1.[CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest.html)(
        parent=f"projects/{project_id}/locations/{zone}",
        queued_resource_id=queued_resource_name,
        queued_resource=resource,
    )
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    operation = client.[create_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_create_queued_resource)(request=request)
    
    response = operation.result()
    print(resource.queueing_policy)
    print(response.queueing_policy.valid_until_time)
    # Example response:
    # valid_until_duration {
    #   seconds: 90
    # }
    # 2024-10-29 14:22:53.562090+00:00
    

### Request a queued resource to be allocated within a specified interval

You can specify an allocation interval by specifying both the start time or duration and end time or duration.

###  gcloud 

The following command requests a v5p-32 in 5 hours and 30 minutes from the current time, to be created no later than December 14, 2022 at 9:00 AM.
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-east5-a \
        --accelerator-type v5p-32 \
        --runtime-version v2-alpha-tpuv5 \
        --valid-after-duration 5h30m \
        --valid-until-time 2022-12-14T09:00:00Z

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-until-time`: The time after which the request is canceled. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * `valid-after-duration`: The duration before which the TPU must not be provisioned. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).



### curl

The following command requests a v5p-32 in 5 hours and 30 minutes from the current time, to be created no later than December 14, 2022 at 9:00 AM.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-east5-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5p-32',
            'runtime_version': 'v2-alpha-tpuv5',
            }
        }
        },
    'queueing_policy': {
        'validInterval': {
            'startTime': '2022-12-10T14:30:00Z',
            'endTime': '2022-12-14T09:00:00Z'
        }
        },
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-east5-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `valid-until-time`: The time after which the request is canceled. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * `valid-until-duration`: The duration for which the request is valid. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. In the **Start request on** field, enter the time after which the resource should be allocated.

  10. In the **Cancel request on** field, enter the time when the queued resource request should expire if not filled.

  11. Click **Create** to create your queued resource request.




## Request a queued resource with a startup script

You can specify a script to be run on a queued resource after it has been provisioned.

### gcloud

When using the `gcloud` command, you can use either the `--metadata` or `--metadata-from-file` flag to specify a script command or a file containing the script code, respectively. The following example creates a queued resource request that will run the `startup-script.sh` script.
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-central1-a \
        --accelerator-type v5litepod-8 \
        --runtime-version v2-alpha-tpuv5-lite \
        --metadata-from-file='startup-script=startup-script.sh'

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `validInterval`: The time during which the request is valid after which the request is canceled. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * `metadata-from-file`: Specifies a file that contains metadata. If you don't specify a fully qualified path to the metadata file, the command assumes it is located in the current directory. In this example the file contains a startup script that is run when the queued resource is provisioned.
  * `metadata`: Specifies metadata for the request. In this example the metadata is a startup script command run when the queued resource is provisioned.



### curl

When using `curl`, you must include the script code in the JSON content. The following example includes an inline script in the JSON body.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        tpu: {
            node_spec: {
            parent: 'projects/your-project-number/locations/us-central1-a',
            node_id: 'your-node-id',
            node: {
                accelerator_type: 'v5e-8',
                runtime_version: 'v2-alpha-tpuv5-lite',
                metadata: {
                    "startup-script": "#! /bin/bash\npwd > /tmp/out.txt\nwhoami >> /tmp/out.txt"
                }
            }
            }
        },
    'queueing_policy': {
        'validInterval': {
            'startTime': '2022-12-10T14:30:00Z',
            'endTime': '2022-12-14T09:00:00Z'
        }
        },
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-central1-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-defined ID of the TPU created in response to the request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `validInterval`: The time during which the request is valid after which the request is canceled. For more information on duration formats, see [Google Cloud CLI topic datetime](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * `metadata-from-file`: Specifies a file that contains metadata. If you don't specify a fully qualified path to the metadata file, the command assumes it is located in the current directory. In this example the file contains a startup script that is run when the queued resource is provisioned.
  * `metadata`: Specifies metadata for the request. In this example the metadata is a startup script command run when the queued resource is provisioned.



###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2alpha1.CreateQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.Node;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    
    public class CreateQueuedResourceWithStartupScript {
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
        String tpuType = "v5litepod-4";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information see https://cloud.google.com/tpu/docs/runtimes
        String tpuSoftwareVersion = "v2-tpuv5-litepod";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
    
        createQueuedResource(projectId, zone, queuedResourceId, nodeName,
            tpuType, tpuSoftwareVersion);
      }
    
      // Creates a Queued Resource with startup script.
      public static QueuedResource createQueuedResource(
          String projectId, String zone, String queuedResourceId,
          String nodeName, String tpuType, String tpuSoftwareVersion)
          throws IOException, ExecutionException, InterruptedException {
        String parent = String.format("projects/%s/locations/%s", projectId, zone);
        String startupScriptContent = "#!/bin/bash\necho \"Hello from the startup script!\"";
        // Add startup script to metadata
        Map<String, String> metadata = new HashMap<>();
        metadata.put("startup-script", startupScriptContent);
        String queuedResourceForTpu =  String.format("projects/%s/locations/%s/queuedResources/%s",
                projectId, zone, queuedResourceId);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          Node node =
              Node.newBuilder()
                  .setName(nodeName)
                  .setAcceleratorType(tpuType)
                  .setRuntimeVersion(tpuSoftwareVersion)
                  .setQueuedResource(queuedResourceForTpu)
                  .putAllMetadata(metadata)
                  .build();
    
          QueuedResource queuedResource =
              QueuedResource.newBuilder()
                  .setName(queuedResourceId)
                  .setTpu(
                      QueuedResource.Tpu.newBuilder()
                          .addNodeSpec(
                              QueuedResource.Tpu.NodeSpec.newBuilder()
                                  .setParent(parent)
                                  .setNode(node)
                                  .setNodeId(nodeName)
                                  .build())
                          .build())
                  .build();
    
          CreateQueuedResourceRequest request =
              CreateQueuedResourceRequest.newBuilder()
                  .setParent(parent)
                  .setQueuedResourceId(queuedResourceId)
                  .setQueuedResource(queuedResource)
                  .build();
          // You can wait until TPU Node is READY,
          // and check its status using getTpuVm() from "tpu_vm_get" sample.
    
          return tpuClient.createQueuedResourceAsync(request).get();
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    # queued_resource_name = "resource-name"
    
    node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
    node.accelerator_type = tpu_type
    # To see available runtime version use command:
    # gcloud compute tpus versions list --zone={ZONE}
    node.runtime_version = runtime_version
    # This startup script updates numpy to the latest version and logs the output to a file.
    script = {
        "startup-script": """#!/bin/bash
    echo "Hello World" > /var/log/hello.log
    sudo pip3 install --upgrade numpy >> /var/log/hello.log 2>&1
    """
    }
    node.metadata = script
    # Enabling external IPs for internet access from the TPU node for updating numpy
    node.network_config = tpu_v2alpha1.[NetworkConfig](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.NetworkConfig.html)(
        enable_external_ips=True,
    )
    
    node_spec = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html).[NodeSpec](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.html)()
    node_spec.parent = f"projects/{project_id}/locations/{zone}"
    node_spec.node_id = tpu_name
    node_spec.node = node
    
    resource = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html)()
    resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html) = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html)(node_spec=[node_spec])
    
    request = tpu_v2alpha1.[CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest.html)(
        parent=f"projects/{project_id}/locations/{zone}",
        queued_resource_id=queued_resource_name,
        queued_resource=resource,
    )
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    operation = client.[create_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_create_queued_resource)(request=request)
    
    response = operation.result()
    print(response.name)
    print(response.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html).node_spec[0].node.metadata)
    # Example response:
    # projects/[project_id]/locations/[zone]/queuedResources/resource-name
    # {'startup-script': '#!/bin/bash\n    echo "Hello World" > /var/log/hello.log\n
    # sudo pip3 install --upgrade numpy >> /var/log/hello.log 2>&1\n    '}
    

## Request a queued resource with a specified network and subnetwork

In a queued resource request, you can specify a network and subnetwork that you want to connect your TPU to.

###  gcloud 
    
    
    gcloud compute tpus queued-resources create your-queued-resource-id \
        --node-id your-node-id \
        --project your-project-id \
        --zone us-central1-a \
        --accelerator-type v5e-8 \
        --runtime-version v2-alpha-tpuv5-lite \
        --network network-name \
        --subnetwork subnetwork-name

#### Command parameter descriptions

  * `queued-resource-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-assigned ID of the TPU which is created when the queued resource request is allocated.
  * `project`: Your Google Cloud project.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `reserved`: Use this flag when requesting queued resources as part of a Cloud TPU reservation.
  * `network`: A network that the queued resource will be a part of.
  * `subnetwork`: A subnetwork that the queued resource will be a part of.



### curl
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d "{
        'tpu': {
        'node_spec': {
            'parent': 'projects/your-project-number/locations/us-central1-a',
            'node_id': 'your-node-id',
            'node': {
            'accelerator_type': 'v5e-8',
            'runtime_version': 'v2-alpha-tpuv5-lite',
            'network_config': {
                'network': 'network-name',
                'subnetwork': 'subnetwork-name',
                'enable_external_ips': true
            }
        }
        },
        'guaranteed': {
        'reserved': true,
        }
    }" \
    https://tpu.googleapis.com/v2alpha1/projects/your-project-id/locations/us-central1-a/queuedResources?queued_resource_id=your-queued-resource-id

#### Command parameter descriptions

  * `queued-resource-id`: The user-assigned ID of the queued resource request.
  * `node-id`: The user-assigned ID of the TPU which is created when the queued resource request is allocated.
  * `project`: Your Google Cloud project.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.
  * `accelerator-type`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `runtime-version`: The Cloud TPU software [version.](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions)
  * `reserved`: Use this flag when requesting queued resources as part of a Cloud TPU reservation.
  * `network`: A network that the queued resource will be a part of.
  * `subnetwork`: A subnetwork that the queued resource will be a part of.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the zone where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. Expand the **Network** section.

  10. In the **Network** and **Subnetwork** fields, select the network and subnetwork you want to use.

  11. Click **Create** to create your queued resource request.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.tpu.v2alpha1.CreateQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.NetworkConfig;
    import com.google.cloud.tpu.v2alpha1.Node;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import com.google.cloud.tpu.v2alpha1.TpuSettings;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import org.threeten.bp.Duration;
    
    public class CreateQueuedResourceWithNetwork {
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
        String tpuType = "v5litepod-4";
        // Software version that specifies the version of the TPU runtime to install.
        // For more information see https://cloud.google.com/tpu/docs/runtimes
        String tpuSoftwareVersion = "v2-tpuv5-litepod";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
        // The name of the network you want the node to connect to.
        // The network should be assigned to your project.
        String networkName = "YOUR_COMPUTE_TPU_NETWORK";
    
        createQueuedResourceWithNetwork(projectId, zone, queuedResourceId, nodeName,
            tpuType, tpuSoftwareVersion, networkName);
      }
    
      // Creates a Queued Resource with network configuration.
      public static QueuedResource createQueuedResourceWithNetwork(
          String projectId, String zone, String queuedResourceId, String nodeName,
          String tpuType, String tpuSoftwareVersion, String networkName)
          throws IOException, ExecutionException, InterruptedException {
        // With these settings the client library handles the Operation's polling mechanism
        // and prevent CancellationException error
        TpuSettings.Builder clientSettings =
            TpuSettings.newBuilder();
        clientSettings
            .createQueuedResourceSettings()
            .setRetrySettings(
                [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                    .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(5000L))
                    .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(2.0)
                    .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                    .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1.0)
                    .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(45000L))
                    .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofHours(24L))
                    .build());
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create(clientSettings.build())) {
          String parent = String.format("projects/%s/locations/%s", projectId, zone);
          String region = zone.substring(0, zone.length() - 2);
    
          // Specify the network and subnetwork that you want to connect your TPU to.
          NetworkConfig networkConfig =
              NetworkConfig.newBuilder()
                  .setEnableExternalIps(true)
                  .setNetwork(String.format("projects/%s/global/networks/%s", projectId, networkName))
                  .setSubnetwork(
                      String.format(
                          "projects/%s/regions/%s/subnetworks/%s", projectId, region, networkName))
                  .build();
    
          // Create a node
          Node node =
              Node.newBuilder()
                  .setName(nodeName)
                  .setAcceleratorType(tpuType)
                  .setRuntimeVersion(tpuSoftwareVersion)
                  .setNetworkConfig(networkConfig)
                  .setQueuedResource(
                      String.format(
                          "projects/%s/locations/%s/queuedResources/%s",
                          projectId, zone, queuedResourceId))
                  .build();
    
          // Create queued resource
          QueuedResource queuedResource =
              QueuedResource.newBuilder()
                  .setName(queuedResourceId)
                  .setTpu(
                      QueuedResource.Tpu.newBuilder()
                          .addNodeSpec(
                              QueuedResource.Tpu.NodeSpec.newBuilder()
                                  .setParent(parent)
                                  .setNode(node)
                                  .setNodeId(nodeName)
                                  .build())
                          .build())
                  .build();
    
          CreateQueuedResourceRequest request =
              CreateQueuedResourceRequest.newBuilder()
                  .setParent(parent)
                  .setQueuedResource(queuedResource)
                  .setQueuedResourceId(queuedResourceId)
                  .build();
    
          // You can wait until TPU Node is READY,
          // and check its status using getTpuVm() from "tpu_vm_get" sample.
    
          return tpuClient.createQueuedResourceAsync(request).get();
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-a"
    # tpu_name = "tpu-name"
    # tpu_type = "v5litepod-4"
    # runtime_version = "v2-tpuv5-litepod"
    # queued_resource_name = "resource-name"
    # network = "default"
    
    node = tpu_v2alpha1.[Node](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.Node.html)()
    node.accelerator_type = tpu_type
    node.runtime_version = runtime_version
    # Setting network configuration
    node.network_config = tpu_v2alpha1.[NetworkConfig](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.NetworkConfig.html)(
        network=network,  # Update if you want to use a specific network
        subnetwork="default",  # Update if you want to use a specific subnetwork
        enable_external_ips=True,
        can_ip_forward=True,
    )
    
    node_spec = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html).[NodeSpec](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.NodeSpec.html)()
    node_spec.parent = f"projects/{project_id}/locations/{zone}"
    node_spec.node_id = tpu_name
    node_spec.node = node
    
    resource = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html)()
    resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html) = tpu_v2alpha1.[QueuedResource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.html).[Tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.QueuedResource.Tpu.html)(node_spec=[node_spec])
    
    request = tpu_v2alpha1.[CreateQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.CreateQueuedResourceRequest.html)(
        parent=f"projects/{project_id}/locations/{zone}",
        queued_resource_id=queued_resource_name,
        queued_resource=resource,
    )
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    operation = client.[create_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_create_queued_resource)(request=request)
    
    response = operation.result()
    print(response.name)
    print(response.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html).node_spec[0].node.network_config)
    print(resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html).node_spec[0].node.network_config.network == "default")
    # Example response:
    # network: "default"
    # subnetwork: "default"
    # enable_external_ips: true
    # can_ip_forward: true
    

## Delete a queued resource request

You can delete a queued resource request and the TPU associated with the request by deleting the queued resource request:

### gcloud

Pass the `--force` flag to the `queued-resource delete` command:

**Note:** The command can take two to five minutes to complete. You can run the command asynchronously by passing the `--async` flag to the `gcloud` command as shown in the following command.
    
    
    gcloud compute tpus queued-resources delete your-queued-resource-id \
        --project your-project-id \
        --zone us-central1-a \
        --force \
        --async

#### Command flag descriptions

  * `your-queued-resource-id`: The user-assigned ID of the queued resource request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) of the Cloud TPU to delete.
  * `force`: Delete both the TPU VM and the queued resource request.



### curl

Use the query parameter `force=true` in your `curl` request:
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://tpu.googleapis.com/v2/projects/your-project-id/locations/us-central1-a/queuedResources/your-queued-resource-id?force=true

#### Command flag descriptions

  * `your-queued-resource-id`: The user-assigned ID of the queued resource request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) of the Cloud TPU to delete.
  * `force`: Delete both the TPU VM and the queued resource request.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click the **Queued resources** tab.

  3. Select the checkbox next to your queued resource request.

  4. Click delete **Delete**.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.tpu.v2alpha1.DeleteQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import com.google.cloud.tpu.v2alpha1.TpuSettings;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import org.threeten.bp.Duration;
    
    public class DeleteForceQueuedResource {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which the TPU was created.
        String zone = "us-central1-f";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
    
        deleteForceQueuedResource(projectId, zone, queuedResourceId);
      }
    
      // Deletes a Queued Resource asynchronously with --force flag.
      public static void deleteForceQueuedResource(
          String projectId, String zone, String queuedResourceId)
              throws ExecutionException, InterruptedException, IOException {
        String name = String.format("projects/%s/locations/%s/queuedResources/%s",
            projectId, zone, queuedResourceId);
        // With these settings the client library handles the Operation's polling mechanism
        // and prevent CancellationException error
        TpuSettings.Builder clientSettings =
            TpuSettings.newBuilder();
        clientSettings
            .deleteQueuedResourceSettings()
            .setRetrySettings(
                [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html).newBuilder()
                    .[setInitialRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(5000L))
                    .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(2.0)
                    .[setInitialRpcTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setInitialRpcTimeout_org_threeten_bp_Duration_)(Duration.ZERO)
                    .[setRpcTimeoutMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRpcTimeoutMultiplier_double_)(1.0)
                    .[setMaxRetryDelay](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxRetryDelay_org_threeten_bp_Duration_)(Duration.ofMillis(45000L))
                    .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofHours(24L))
                    .build());
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create(clientSettings.build())) {
          DeleteQueuedResourceRequest request =
              DeleteQueuedResourceRequest.newBuilder().setName(name).setForce(true).build();
          // Waiting for updates in the library. Until then, the operation will complete successfully,
          // but the user will receive an error message with UnknownException and IllegalStateException.
          tpuClient.deleteQueuedResourceAsync(request).get();
    
          System.out.printf("Deleted Queued Resource: %s\n", name);
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    # queued_resource_name = "resource-name"
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    request = tpu_v2alpha1.[DeleteQueuedResourceRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.types.DeleteQueuedResourceRequest.html)(
        name=f"projects/{project_id}/locations/{zone}/queuedResources/{queued_resource_name}",
        force=True,  # Set force=True to delete the resource with tpu nodes.
    )
    
    try:
        op = client.[delete_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_delete_queued_resource)(request=request)
        op.result()
        print(f"Queued resource '{queued_resource_name}' successfully deleted.")
    except TypeError as e:
        print(f"Error deleting resource: {e}")
        print(f"Queued resource '{queued_resource_name}' successfully deleted.")
    

If you delete the TPU directly, you also need to delete the queued resource, as shown in the following example. When you delete the TPU, the queued resource request transitions to the `SUSPENDED` state, after which the queued resource request can be deleted.

### gcloud

Delete the TPU:
    
    
    $ gcloud compute tpus tpu-vm delete your-node-id \
        --project=your-project-id \
        --zone=us-central1-a \
        --quiet

#### Command flag descriptions

  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) of the Cloud TPU to delete.
  * `your-node-id`: The name of the TPU you want to delete.



When you delete your TPU, the associated queued resource goes into the `SUSPENDING` state, then the `SUSPENDED` state. When your queued resource is in the `SUSPENDED` state, you can delete it:
    
    
    gcloud compute tpus queued-resources delete your-queued-resource-id \
        --project your-project-id \
        --zone us-central1-a

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) of the Cloud TPU to delete.



### curl

Delete the TPU:
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://tpu.googleapis.com/v2/projects/your-project/locations/us-central1-a/nodes?node_id=your-node-id

#### Command flag descriptions

  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) of the Cloud TPU to delete.
  * `your-node-id`: The name of the TPU you want to delete.



When you delete your TPU, the associated queued resource goes into the `SUSPENDING` state, then the `SUSPENDED` state. When your queued resource is in the `SUSPENDED` state, you can delete it:
    
    
    curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://tpu.googleapis.com/v2/projects/your-project-id/locations/us-central1-a/queuedResources/your-queued-resource-id

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) of the Cloud TPU to delete.



### Console

Delete your TPU:

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Select the checkbox next to your TPU.

  3. Click delete **Delete**.




When you delete your TPU, the associated queued resource goes into the **Suspending** state, then the **Suspended** state. When your queued resource is in the **Suspended** state, you can delete it:

  1. Click the **Queued resources** tab.
  2. Select the checkbox next to your queued resource request.
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

When you delete your TPU, the associated queued resource goes into the `SUSPENDING` state, then the `SUSPENDED` state. When your queued resource is in the `SUSPENDED` state, you can delete it:
    
    
    import com.google.cloud.tpu.v2alpha1.DeleteQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class DeleteQueuedResource {
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which the TPU was created.
        String zone = "us-central1-f";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
    
        deleteQueuedResource(projectId, zone, queuedResourceId);
      }
    
      // Deletes a Queued Resource asynchronously.
      public static void deleteQueuedResource(String projectId, String zone, String queuedResourceId)
          throws ExecutionException, InterruptedException, IOException {
        String name = String.format("projects/%s/locations/%s/queuedResources/%s",
            projectId, zone, queuedResourceId);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          // Before deleting the queued resource it is required to delete the TPU VM.
          // For more information about deleting TPU
          // see https://cloud.google.com/tpu/docs/managing-tpus-tpu-vm
    
          DeleteQueuedResourceRequest request =
                  DeleteQueuedResourceRequest.newBuilder().setName(name).build();
    
          tpuClient.deleteQueuedResourceAsync(request).get();
        }
      }
    }

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
    

When you delete your TPU, the associated queued resource goes into the `SUSPENDING` state, then the `SUSPENDED` state. When your queued resource is in the `SUSPENDED` state, you can delete it:
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    # queued_resource_name = "resource-name"
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    name = (
        f"projects/{project_id}/locations/{zone}/queuedResources/{queued_resource_name}"
    )
    
    try:
        op = client.[delete_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_delete_queued_resource)(name=name)
        op.result()
        print(f"Queued resource '{queued_resource_name}' successfully deleted.")
    except TypeError as e:
        print(f"Error deleting resource: {e}")
        print(f"Queued resource '{queued_resource_name}' successfully deleted.")
    

## Retrieve state and diagnostic information about a queued resource request

Retrieve the state and diagnostic information about a queued resource request:

###  gcloud 
    
    
    gcloud compute tpus queued-resources describe queued-resource-request-id \
        --project your-project-id \
        --zone us-central1-a

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.



### curl
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://tpu.googleapis.com/v2/projects/your-project-id/locations/us-central1-a/queuedResources/your-queued-resource-id

#### Command flag descriptions

  * `queued-resource-request-id`: The user-assigned ID of the queued resource request.
  * `project`: The ID of the project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click the **Queued resources** tab.

  3. Click the name of your queued resource request.




After your TPU has been provisioned, you can also view details about your queued resource request by going to the [**TPUs** page](https://console.cloud.google.com/compute/tpus), finding your TPU, and clicking on the name of the corresponding queued resource request.

###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2alpha1.GetQueuedResourceRequest;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import java.io.IOException;
    
    public class GetQueuedResource {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which the TPU was created.
        String zone = "us-central1-f";
        // The name for your Queued Resource.
        String queuedResourceId = "QUEUED_RESOURCE_ID";
    
        getQueuedResource(projectId, zone, queuedResourceId);
      }
    
      // Get a Queued Resource.
      public static QueuedResource getQueuedResource(
          String projectId, String zone, String queuedResourceId) throws IOException {
        String name = String.format("projects/%s/locations/%s/queuedResources/%s",
            projectId, zone, queuedResourceId);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          GetQueuedResourceRequest request =
              GetQueuedResourceRequest.newBuilder().setName(name).build();
    
          return tpuClient.getQueuedResource(request);
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    # queued_resource_name = "resource-name"
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    name = (
        f"projects/{project_id}/locations/{zone}/queuedResources/{queued_resource_name}"
    )
    resource = client.[get_queued_resource](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_get_queued_resource)(name=name)
    print("Resource name:", resource.name)
    print(resource.state)
    # Example response:
    # Resource name: projects/{project_id}/locations/{zone}/queuedResources/resource-name
    # State.ACTIVE
    

If the request fails, the output will contain error information. For a request that is waiting for resources, the output looks similar to the following:

### gcloud
    
    
        name: projects/your-project-id/locations/us-central1-a/queuedResources/your-queued-resource-id
        state:
        state: WAITING_FOR_RESOURCES
        tpu:
        nodeSpec:
        - node:
            acceleratorType: v4-8
            bootDisk: {}
            networkConfig:
                enableExternalIps: true
            queuedResource: projects/your-project-number/locations/us-central1-a/queuedResources/your-queued-resource-id
            runtimeVersion: v2-alpha-tpuv5-lite
            schedulingConfig: {}
            serviceAccount: {}
            shieldedInstanceConfig: {}
            useTpuVm: true
            nodeId: your-node-id
            parent: projects/your-project-number/locations/us-central1-a

### Console

The **Queued resource status** field displays **Waiting for resources**.

## List queued resource requests in your project

List the queued resource requests in your project:

###  gcloud 
    
    
    gcloud compute tpus queued-resources list --project your-project-id \
        --zone us-central1-a

#### Command flag descriptions

  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.



### curl
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://tpu.googleapis.com/v2/projects/your-project-id/locations/your-zone/queuedResources

#### Command flag descriptions

  * `project`: The Google Cloud project where the queued resource is allocated.
  * `zone`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones-tpu-vm) where you plan to create your Cloud TPU.



### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click the **Queued resources** tab.




###  Java 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.tpu.v2alpha1.ListQueuedResourcesRequest;
    import com.google.cloud.tpu.v2alpha1.QueuedResource;
    import com.google.cloud.tpu.v2alpha1.TpuClient;
    import com.google.cloud.tpu.v2alpha1.TpuClient.ListQueuedResourcesPage;
    import java.io.IOException;
    
    public class ListQueuedResources {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project.
        String projectId = "YOUR_PROJECT_ID";
        // The zone in which the TPU was created.
        String zone = "us-central1-a";
    
        listQueuedResources(projectId, zone);
      }
    
      // List Queued Resources.
      public static ListQueuedResourcesPage listQueuedResources(
          String projectId, String zone) throws IOException {
        String parent = String.format("projects/%s/locations/%s", projectId, zone);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (TpuClient tpuClient = TpuClient.create()) {
          ListQueuedResourcesRequest request =
              ListQueuedResourcesRequest.newBuilder().setParent(parent).build();
          ListQueuedResourcesPage response =  tpuClient.listQueuedResources(request).getPage();
    
          for (QueuedResource queuedResource : response.iterateAll()) {
            System.out.println(queuedResource.getName());
          }
          return response;
        }
      }
    }

###  Python 

To authenticate to Cloud TPU, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import tpu_v2alpha1
    
    # TODO(developer): Update and un-comment below lines
    # project_id = "your-project-id"
    # zone = "us-central1-b"
    
    client = tpu_v2alpha1.[TpuClient](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html)()
    parent = f"projects/{project_id}/locations/{zone}"
    resources = client.[list_queued_resources](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.TpuClient.html#google_cloud_tpu_v2alpha1_services_tpu_TpuClient_list_queued_resources)(parent=parent)
    for resource in resources:
        print("Resource name:", resource.name)
        print("TPU id:", resource.[tpu](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2alpha1.services.tpu.html).node_spec[0].node_id)
    # Example response:
    # Resource name: projects/{project_id}/locations/{zone}/queuedResources/resource-name
    # TPU id: tpu-name
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
