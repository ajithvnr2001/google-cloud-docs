---
url: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads/
title: Deploy workloads \u00a0|\u00a0 Confidential Space \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:13.483811+00:00
---

# Deploy workloads  |  Confidential Space  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-space/docs/deploy-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Confidential Space ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview)



Send feedback 

#  Deploy workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Workload operator ](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview#roles)

A workload operator can pass options to a Confidential Space workload VM instance to determine its behavior before it runs. While some flags have required values that don't change, you still need to make the following choices:

  * Whether to base the VM instance on a [production or debug Confidential Space image](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images).

  * Whether to use AMD SEV, Intel TDX, or Intel TDX with NVIDIA Confidential Computing to help keep your workload data private.

  * What VM metadata variables need to be passed, which include details like which workload container image to run, which attestation service to use, whether to log to Cloud Logging, and what environment variables to set.

  * What service account to attach to the VM to run the workload, and what permissions it needs to access confidential data in other projects and write the results somewhere.

  * What zone the VM instance should run in.




Here's an example that creates a Confidential VM, and runs a Docker container called WORKLOAD_CONTAINER_NAME:

###  CPU-based workloads 
    
    
    gcloud compute instances create INSTANCE_NAME \
        --confidential-compute-type=CONFIDENTIAL_COMPUTING_TECHNOLOGY \
        --machine-type=MACHINE_TYPE_NAME \
        --maintenance-policy=MAINTENANCE_POLICY \
        --shielded-secure-boot \
        --image-project=confidential-space-images \
        --image-family=IMAGE_FAMILY \
        --metadata="^~^tee-image-reference=us-docker.pkg.dev/WORKLOAD_AUTHOR_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest" \
        --service-account=WORKLOAD_SERVICE_ACCOUNT_NAME@WORKLOAD_OPERATOR_PROJECT_ID.iam.gserviceaccount.com \
        --scopes=cloud-platform \
        --zone=ZONE_NAME \
        --project=PROJECT_ID
    

Provide the following values:

  * `INSTANCE_NAME`: The name of the new VM instance.

  * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following values:

    * `SEV`

    * `TDX`

  * `MACHINE_TYPE_NAME`: The VM machine type, for example, `n2d-standard-2`. Valid machine types for Confidential VM instances are determined by the Confidential Computing technology you've chosen, either AMD SEV or Intel TDX. See [Machine types, CPUs, and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).

  * `MAINTENANCE_POLICY`: For N2D machine types that use SEV, set this to `MIGRATE` for live migration support. For all other machine types, set this value to `TERMINATE`, as they [don't support live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration).

  * `IMAGE_FAMILY_NAME`: The family for the [Confidential Space images](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images). Choose one of the following:

    * `confidential-space` for production workloads

    * `confidential-space-debug` for debug workloads

  * Additional metadata variables, which change how the VM behaves, including what attestation service to use.

  * `WORKLOAD_AUTHOR_PROJECT`: The ID of the project that hosts the Artifact Registry repository that the workload container is stored in.

  * `REPOSITORY_NAME`: The Artifact Registry repository name that the workload container is stored in.

  * `WORKLOAD_CONTAINER_NAME`: The name of the workload container.

  * `WORKLOAD_SERVICE_ACCOUNT_NAME`: The name of the service account that runs the workload.

  * `WORKLOAD_OPERATOR_PROJECT_ID`: The ID of the project that runs the workload.

  * `ZONE_NAME`: The zone that the VM instance runs in, for example, `us-west1-b`. Confidential Space requires the following services, which are available in specific locations:

    * [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=AMD%20SEV#supported-zones), based on the Confidential Computing technology in use

    * [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/locations)

  * `PROJECT_ID`: Optional. The ID of the project to create the VM instance in.




###  GPU-based workloads 

### Before you begin

  * Confidential Space only supports NVIDIA Confidential Computing on H100 GPUs.

  * To make sure that you have sufficient GPU quota for the resources you're requesting, check your [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota). For Confidential VM instances with GPUs, request preemptible GPU quota to use the resources. When you request GPU quota, you must request quota for the GPU models that you want to create in each region, and additional global quota (`GPUs (all regions)`) for the total number of GPUs of all types in all regions.

  * To understand quota consumption, read [GPU VMs and preemptible allocation quotas](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas).

  * Read the [limitations](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig#limitations) for creating a resize request in a MIG.

  * To install the drivers required for NVIDIA Confidential Computing, you must pass the metadata variable `tee-install-gpu-driver` with a value of `true`.

  * For NVIDIA drivers and the CUDA toolkit, a VM boot disk with 30GB or more space is recommended.

  * To use CUDA applications, NVIDIA CUDA-X libraries must be available in the container image you're using. To include the libraries, do one of the following:

    * Use a container image with pre-installed NVIDIA CUDA-X libraries. For example, you can use Google's Deep Learning Containers for pre-installed data science frameworks, NVIDIA CUDA-X libraries, and additional tools. Alternatively, you can use NVIDIA's CUDA container image for only the NVIDIA CUDA-X libraries.

    * Build and use your own container image. Set the `LD_LIBRARY_PATH` environment variable to `/usr/local/nvidia/lib64`, which must contain the NVIDIA CUDA-X libraries and device drivers.




### Known issues

  * When running a Confidential Space workload with an NVIDIA H100 GPU attached, you might see the following error message:
        
        failed to get launchspec, make sure you're running inside
        a GCE VM: GPU Driver installation is not supported.
        

This is a known issue with the Confidential Space image. To work around the issue, restart the Confidential VM.




### Deploy a GPU-based workload

To deploy a GPU-based workload, you must create a Confidential VM instance using the [spot](https://docs.cloud.google.com/compute/docs/instances/spot) or [flex-start](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) provisioning model.

###  Spot 

To use the spot provisioning model, create an accelerator-optimized VM instance.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --provisioning-model=SPOT \
        --confidential-compute-type=TDX \
        --machine-type=a3-highgpu-1g \
        --maintenance-policy=TERMINATE \
        --shielded-secure-boot \
        --image-project=confidential-space-images \
        --image-family=IMAGE_FAMILY_NAME \
        --metadata="^~^tee-image-reference=us-docker.pkg.dev/WORKLOAD_AUTHOR_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest~tee-install-gpu-driver=true" \
        --service-account=WORKLOAD_SERVICE_ACCOUNT_NAME@WORKLOAD_OPERATOR_PROJECT_ID.iam.gserviceaccount.com \
        --scopes=cloud-platform \
        --boot-disk-size=30G \
        --zone=ZONE_NAME \
        --project=PROJECT_ID
    

Provide the following values:

  * `INSTANCE_NAME`: The name of the new VM instance.

  * `IMAGE_FAMILY_NAME`: The family for the [Confidential Space images](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images). Choose one of the following:

    * `confidential-space` for production workloads

    * `confidential-space-debug` for debug workloads

  * Additional metadata variables, which change how the VM behaves, including what attestation service to use.

  * `WORKLOAD_AUTHOR_PROJECT`: The project ID that the workload is being run in.

  * `REPOSITORY_NAME`: The Artifact Registry repository name.

  * `WORKLOAD_CONTAINER_NAME`: The name of the workload container.

  * `WORKLOAD_SERVICE_ACCOUNT_NAME`: The name of the service account that runs the workload.

  * `WORKLOAD_OPERATOR_PROJECT_ID`: The ID of the project that runs the workload.

  * `ZONE_NAME`: One of the [zones that support NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=NVIDIA%20Confidential%20Computing#supported-zones).

  * `PROJECT_ID`: Optional. The ID of the project to create the VM instance in.




###  Flex-start 

To use the flex-start provisioning model, create an instance template, followed by a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) (MIG).

  1. Create an instance template:
         
         gcloud beta compute instance-templates create INSTANCE_TEMPLATE_NAME \
             --provisioning-model=FLEX_START \
             --confidential-compute-type=TDX \
             --machine-type=a3-highgpu-1g \
             --maintenance-policy=TERMINATE \
             --shielded-secure-boot \
             --image-project=confidential-space-images \
             --image-family=IMAGE_FAMILY_NAME \
             --metadata="^~^tee-image-reference=us-docker.pkg.dev/WORKLOAD_AUTHOR_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest~tee-install-gpu-driver=true" \
             --service-account=WORKLOAD_SERVICE_ACCOUNT_NAME@WORKLOAD_OPERATOR_PROJECT_ID.iam.gserviceaccount.com \
             --scopes=cloud-platform \
             --boot-disk-size=30G \
             --max-run-duration=RUN_DURATION \
             --instance-termination-action=DELETE \
             --project=PROJECT_ID
         

Provide the following values:

     * `INSTANCE_TEMPLATE_NAME`: The name of the new VM instance template.

     * `IMAGE_FAMILY_NAME`: The family for the [Confidential Space images](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-images). Choose one of the following:

       * `confidential-space` for production workloads

       * `confidential-space-debug` for debug workloads

     * `WORKLOAD_AUTHOR_PROJECT`: The project ID that the workload is being run in.

     * `REPOSITORY_NAME`: The Artifact Registry repository name.

     * `WORKLOAD_CONTAINER_NAME`: The name of the workload container.

     * `WORKLOAD_SERVICE_ACCOUNT_NAME`: The name of the service account that runs the workload.

     * `WORKLOAD_OPERATOR_PROJECT_ID`: The ID of the project that runs the workload.

     * `RUN_DURATION`: the duration you want the requested VM instances to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, or `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days.

     * `PROJECT_ID`: Optional. The ID of the project to create the VM instances in.

  2. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
         
         gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
             --template=INSTANCE_TEMPLATE_NAME \
             --size=0 \
             --zone=ZONE_NAME \
             --default-action-on-vm-failure=do_nothing
         

Provide the following values:

     * `INSTANCE_GROUP_NAME`: The name of the MIG.

     * `INSTANCE_TEMPLATE_NAME`: The name of the instance template for GPU VMs.

     * `ZONE_NAME`: One of the [zones that support NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=NVIDIA%20Confidential%20Computing#supported-zones).

  3. In the MIG, create a resize request. Specify the number of GPU VM instances that you want, and the duration to run those VM instances.
         
         gcloud compute instance-groups managed resize-requests create INSTANCE_GROUP_NAME \
             --resize-request=RESIZE_REQUEST_NAME \
             --resize-by=COUNT \
             --zone=ZONE_NAME
         

Provide the following values:

     * `INSTANCE_GROUP_NAME`: The name of the MIG.

     * `INSTANCE_TEMPLATE_NAME`: The name of the instance template for GPU VM instances.

     * `ZONE_NAME`: One of the [zones that support NVIDIA Confidential Computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=NVIDIA%20Confidential%20Computing#supported-zones).

     * `RESIZE_REQUEST_NAME`: The name of the resize request.

     * `COUNT`: The number of VM instances to add all at once in the group.

The resize request that you create stays in the `ACCEPTED` state until the MIG creates all the requested GPU VM instances. After all GPU VM instances are created in the group, the state of the request changes to `SUCCEEDED`.

  4. When enough resources are available for the resize request, VM instances are added to the MIG and launched to run your workload. To list instances that are present in the MIG, run the following command:
         
         gcloud compute instance-groups managed list-instances INSTANCE_GROUP_NAME \
             --zone=ZONE_NAME \
             --project=PROJECT_ID
         

Provide the following values:

     * `INSTANCE_GROUP_NAME`: The name of the MIG.

     * `ZONE_NAME`: The [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=NVIDIA%20Confidential%20Computing#supported-zones) to get a list of VM instances from.

     * `PROJECT_ID`: Optional. The ID of the project to get a list of VM instances from.




## Attached service account

A service account must be attached to a workload's Confidential VM to run the workload. The service account must be set up in the following way:

  * With the following roles:

    * `roles/confidentialcomputing.workloadUser` to generate an attestation token.

    * `roles/artifactregistry.reader` to retrieve a workload container image stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).

    * `roles/logging.logWriter` if you want to redirect `STDOUT` and `STDERR` to Cloud Logging.

  * With read access to where the data collaborators store their confidential data, for example, a Cloud Storage bucket or BigQuery table.

  * With write access to where the workload outputs the data, for example, a Cloud Storage bucket. Data collaborators must have read access to this location.




Additionally, data collaborators and workload operators need to set up the following things:

  * If data collaborators are using [service account impersonation instead of direct resources access](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources#external-access-methods), they must add the service account to their workload identity pool provider as an attribute condition:
        
        'WORKLOAD_SERVICE_ACCOUNT_NAME@DATA_COLLABORATOR_PROJECT_ID.iam.gserviceaccount.com' in assertion.google_service_accounts
        

  * The workload operator needs the `roles/iam.serviceAccountUser` role to impersonate the service account. This lets them attach it to a workload VM instance so it can run the workload.




## Metadata variables

You can change the Confidential Space workload VM behavior by passing variables into the `--metadata` option when you create the VM.

To pass in multiple variables, first set the delimiter by prefixing the `--metadata` value with `^~^`. This sets the delimiter to `~`, as `,` is used in variable values.

For example:
    
    
    metadata="^~^tee-restart-policy=Always**~** tee-image-reference=us-docker.pkg.dev/WORKLOAD_AUTHOR_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest"
    

The following table details the metadata variables you can set for your workload VM.

**Note:** Some metadata variables can be affected by the [launch policies](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#launch_policies) that workload authors set.Metadata key | Type | Description and values  
---|---|---  
`tee-image-reference` **Interacts with:**

  * **Data collaborators** : The [ `container.image_reference`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=container-assertions#image-reference) assertion. 

| String |  Required. This points to the location of the workload container. 

##### Example
    
    
    tee-image-reference=us-docker.pkg.dev/WORKLOAD_AUTHOR_PROJECT_ID/REPOSITORY_NAME/WORKLOAD_CONTAINER_NAME:latest  
  
`ita-api-key` | String |  Only required if you're using Intel Trust Authority as your attestation service. Set the value to your Intel Trust Authority API key.  See [ Intel's documentation](https://docs.trustauthority.intel.com/main/articles/articles/ita/tutorial-api-key.html#create-an-attestation-api-key) for how to create an Intel Trust Authority API key.  Intel Trust Authority supports Intel TDX VM instances that optionally have an NVIDIA H100 GPU. If the GPU is present, its evidence is also verified. 

##### Example
    
    
    ita-api-key=API_KEY  
  
`ita-region` | String |  Only required if you're using Intel Trust Authority as your attestation service. Set the value to the region that you want Intel Trust Authority to run in. The valid regions are: 

  * US: `https://api.trustauthority.intel.com`
  * Europe: `https://api.eu.trustauthority.intel.com`

Intel Trust Authority supports Intel TDX VM instances that optionally have an NVIDIA H100 GPU. If the GPU is present, its evidence is also verified. 

##### Example
    
    
    ita-region=REGION_NAME  
  
`tee-added-capabilities` **Interacts with:**

  * **Workload author** : The [ `allow_capabilities`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#allow-capabilities) launch policy. 

| JSON string array |  Adds additional [ Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) to the workload container. 

##### Example
    
    
    tee-added-capabilities="[\"CAP_SYS_ADMIN\", \"CAP_SYS_CHROOT\"]"  
  
`tee-cgroup-ns` **Interacts with:**

  * **Workload author** : The [ `allow_cgroups`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#allow-cgroups) launch policy. 

| Boolean |  Defaults to `false`. When set to `true`, enables a namespaced [ cgroup](https://docs.kernel.org/admin-guide/cgroup-v1/cgroups.html) mount at `/sys/fs/cgroup`. 

##### Example
    
    
    tee-cgroup-ns=true  
  
`tee-cmd` **Interacts with:**

  * **Workload author** : The [ `allow_cmd_override`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#allow-cmd-override) launch policy. 
  * **Data collaborators** : The [ `container.cmd_override`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=container-assertions#cmd-override) assertion. 

| JSON string array |  Overrides the [ CMD](https://docs.docker.com/engine/reference/builder/#cmd) instructions specified in the workload container's `Dockerfile`. 

##### Example
    
    
    tee-cmd="[\"params1\", \"params2\"]"  
  
`tee-container-log-redirect` **Interacts with:**

  * **Workload author** : The [ `log_redirect`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#log-redirect) launch policy. 

| Enumeration |  Outputs `STDOUT` and `STDERR` from the workload container to Cloud Logging or serial console, using the **confidential-space-launcher** field.  The valid values are:

  * `false`: (default) no logging occurs.
  * `true`: outputs to the serial console and Cloud Logging.
  * `cloud_logging`: outputs to Cloud Logging only. 
  * `serial`: outputs to the serial console only.

A high log volume in the serial console might impact workload performance. 

##### Example
    
    
    tee-container-log-redirect=true  
  
`tee-dev-shm-size-kb` | Integer |  Sets the size in kB of the `/dev/shm` shared memory mount. 

##### Example
    
    
    tee-dev-shm-size-kb=65536  
  
`tee-env-ENVIRONMENT_VARIABLE_NAME` **Interacts with:**

  * **Data collaborators** : The [ `container.env`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=container-assertions#env) and [ `container.env_override`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=container-assertions#env-override) assertions. 

| String |  Sets environment variables in the workload container. The workload author must also add the environment variable names to the [ `allow_env_override`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#allow-env-override) launch policy, or they won't be set. 

##### Example
    
    
    tee-env-example-env-1='value-1'~tee-env-example-env-2='value-2'  
  
`tee-impersonate-service-accounts` **Interacts with:**

  * **Data collaborators** : The [ `google_service_accounts`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=vm-assertions#google-service-accounts) assertion. 

| String |  A list of service accounts that can be impersonated by the workload operator. The workload operator must be [ allowed to impersonate the service accounts](https://docs.cloud.google.com/iam/docs/service-account-permissions#roles).  Multiple service accounts can be listed, separated by commas.

##### Example
    
    
    tee-impersonate-service-accounts=SERVICE_ACCOUNT_NAME_1@WORKLOAD_OPERATOR_PROJECT_ID.iam.gserviceaccount.com,SERVICE_ACCOUNT_NAME_2@WORKLOAD_OPERATOR_PROJECT_ID.iam.gserviceaccount.com  
  
`tee-install-gpu-driver` **Interacts with:**

  * **Data collaborators** : The [ `nvidia_gpu.cc_feature`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=vm-assertions#nvidia-cc-feature), [ `nvidia_gpu.cc_mode`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=vm-assertions#nvidia-cc-mode), and [ `nvidia_gpu.gpus`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=vm-assertions#nvidia-gpus) assertions. 

| Boolean |  Whether to install NVIDIA's Confidential Computing GPU driver. Requires a machine type that supports NVIDIA Confidential Computing. 

##### Example
    
    
    tee-install-gpu-driver=true  
  
`tee-monitoring-memory-enable` **Interacts with:**

  * **Data collaborators** : The [ `instance_memory_monitoring_enabled`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=vm-assertions#instance_memory_monitoring_enabled) assertion. 
  * **Workload author** : The [ `monitoring_memory_allow`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#monitoring-memory-allow) launch policy. 

| Boolean |  Defaults to `false`. When set to `true`, enables memory usage monitoring. The metrics collected by the Confidential VM are of the [ `guest/memory/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#compute/guest/memory/bytes_used) type, and can be viewed in [Cloud Logging](https://docs.cloud.google.com/logging) or [ Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). 

##### Example
    
    
    tee-monitoring-memory-enable=true  
  
`tee-mount` **Interacts with:**

  * **Workload author** : The [ `allow_mount_destinations`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-customize-workloads#allow-mount-destinations) launch policy. 

| String |  A list of semicolon-separated mount definitions. A mount definition consists of a comma-separated list of key-value pairs, requiring `type`, `source`, and `destination`. `destination` must be an absolute path and `type`/`source` must be `tmpfs`. 

##### Example
    
    
    type=tmpfs,source=tmpfs,destination=/tmp/tmpfs,size=12345;type=tmpfs,source=tmpfs,destination=/run/workload  
  
`tee-restart-policy` **Interacts with:**

  * **Data collaborators** : The [ `container.restart_policy`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=container-assertions#restart-policy) assertion. 

| Enumeration |  The restart policy of the container launcher when the workload stops.  The valid values are:

  * `Never` (default)
  * `Always`
  * `OnFailure`

This variable is only supported by the production Confidential Space image. 

##### Example
    
    
    tee-restart-policy=OnFailure  
  
`tee-signed-image-repos` **Interacts with:**

  * **Data collaborators** : The [ `container.image_signatures`](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/create-grant-access-confidential-resources?tab=container-assertions#image-signatures) assertion. 

| String |  A list of comma-separated container repositories that store the signatures that are generated by [ Sigstore Cosign](https://docs.sigstore.dev/signing/quickstart/). 

##### Example
    
    
    tee-signed-image-repos=us-docker.pkg.dev/projectA/repo/example,us-docker.pkg.dev/projectB/repo/example,us-docker.pkg.dev/projectC/repo/example  
  
## Scaling

For scaling and high availability of production Confidential Space workloads, see [Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
