---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-trigger-inside-cluster/
title: Trigger Agent Sandbox snapshots from inside a cluster \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:16.492123+00:00
---

# Trigger Agent Sandbox snapshots from inside a cluster  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-trigger-inside-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Trigger Agent Sandbox snapshots from inside a cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Use Agent Sandbox snapshots within a Google Kubernetes Engine (GKE) cluster to preserve the state of your sandboxed environments. This approach provides consistent debugging, accelerates development iteration, and facilitates rapid recovery of complex setups. In this tutorial, you deploy and test this capability by running a client application that programmatically creates, pauses, and resumes sandboxed environments inside the cluster.

For more information about taking snapshots of Pods, see [Restore from a Pod snapshot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-snapshots).

## Costs

Agent Sandbox is offered at no extra charge in GKE. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Artifact Registry, Kubernetes Engine, Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com,cloudbuild.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Verify that you have the permissions required to complete this tutorial.



### Required roles

To get the permissions that you need to create and manage sandboxes, ask your administrator to grant you the [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

In a regional cluster, nodes in different zones might have different CPU microarchitectures. Because snapshots capture the CPU state, restoring a snapshot on a node with missing CPU features fails (for example, with the error `OCI runtime restore failed: incompatible FeatureSet`).

To avoid this issue, use the appropriate configuration for your environment:

  * **Production** : To preserve high availability across your cluster, don't pin workloads to a specific zone. Instead, help ensure CPU feature consistency across all zones by specifying a minimum CPU platform. For more information, see [Choose a minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform).
  * **Testing** : To simplify setup and avoid initial CPU mismatch errors, you can use a `nodeSelector` field in your `SandboxTemplate` manifest to pin the Pod to a specific zone, such as `us-central1-a`. The example in this tutorial uses this testing configuration.



## Define environment variables

To simplify the commands that you run in this tutorial, you can set environment variables in Cloud Shell. In Cloud Shell, define the following useful environment variables by running the following commands:
    
    
    export PROJECT_ID=$(gcloud config get project)
    export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
    export CLUSTER_NAME="test-snapshot"
    export LOCATION="us-central1"
    export BUCKET_LOCATION="us"
    export MACHINE_TYPE="n2-standard-2"
    export REPOSITORY_NAME="agent-sandbox"
    export BUCKET_NAME="${PROJECT_ID}_snapshots"
    export CLOUDBUILD_BUCKET_NAME="${PROJECT_ID}_cloudbuild"
    

Here's an explanation of these environment variables:

  * `PROJECT_ID`: the ID of your current Google Cloud project. Defining this variable helps ensure that all resources are created in the correct project.
  * `PROJECT_NUMBER`: the project number of your current Google Cloud project.
  * `CLUSTER_NAME`: the name of your GKE cluster—for example, `test-snapshot`.
  * `LOCATION`: the Google Cloud region where your GKE cluster and Artifact Registry repository are located—for example, `us-central1`.
  * `BUCKET_LOCATION`: the location of your Cloud Storage buckets—for example, `us`.
  * `BUCKET_NAME`: the name of the Cloud Storage bucket used for snapshots.
  * `CLOUDBUILD_BUCKET_NAME`: the name of the Cloud Storage bucket used for Cloud Build logs.
  * `MACHINE_TYPE`: the machine type to use for the cluster nodes—for example, `e2-standard-8`.
  * `REPOSITORY_NAME`: the name of the Artifact Registry repository—for example, `agent-sandbox`.



## Overview of configuration steps

To enable and test Pod snapshots of Agent Sandbox environments from within your cluster, you need to perform several configuration steps. To understand these steps, it's helpful to first understand the components involved in the overall workflow.

### Key components

This tutorial uses the following two Python applications to test the snapshot process:

  * **Client application** : a Python script running in a standard Pod in your cluster. This application manages the sandbox lifecycle: it programmatically creates the sandbox, pauses it to trigger a snapshot, resumes the sandbox, and verifies that the state was preserved. In this tutorial, you create a Kubernetes service account named `agent-sandbox-client-sa` and grant it RBAC permissions so that the client application Pod can manage sandbox custom resources and snapshot trigger objects using the Kubernetes API.
  * **Sandboxed application** : a Python script that increments and prints a counter every second. This application runs securely inside the isolated sandbox environment to generate a changing state that the client application can verify. In this tutorial, you create a dedicated Kubernetes service account named `snapshot-sa` and configure Workload Identity to authorize the sandboxed Pod to securely read and write snapshot objects in Cloud Storage.



### Configuration and testing process

The following list summarizes the steps you need to perform to set up your environment and run the test:

  1. **Create a cluster** : create an Autopilot or Standard cluster with Pod snapshots and the Agent Sandbox feature enabled.
  2. **Create an Artifact Registry repository** : create a Docker repository to store the container image for your client application.
  3. **Install Agent Sandbox** : install the core agent-sandbox components and extensions on your cluster.
  4. **Configure storage and permissions** : create a Cloud Storage bucket and configure Workload Identity permissions to allow snapshots to be saved securely.
  5. **Configure Pod snapshots** : create and apply the snapshot storage configuration, the snapshot policy, and the sandbox template.
  6. **Build the client application** : build the container image for the client application and push it to your Artifact Registry repository.
  7. **Run the test** : deploy the client application Pod, which creates the sandbox, pauses it to capture a snapshot, resumes it, and verifies that the counter's state was successfully restored.



## Create a cluster

Create a new GKE cluster with Pod snapshots enabled. For full feature compatibility, specify the rapid release channel.

### Autopilot

Create an Autopilot cluster with the required features:
    
    
    gcloud beta container clusters create-auto ${CLUSTER_NAME} \
       --enable-pod-snapshots \
       --release-channel=rapid \
       --location=${LOCATION}
    

### Standard

Create a Standard cluster with the required features:
    
    
    gcloud beta container clusters create ${CLUSTER_NAME} \
       --enable-pod-snapshots \
       --release-channel=rapid \
       --machine-type=${MACHINE_TYPE} \
       --workload-pool=${PROJECT_ID}.svc.id.goog \
       --workload-metadata=GKE_METADATA \
       --num-nodes=1 \
       --location=${LOCATION}
    

Create a node pool with gVisor enabled:
    
    
    gcloud container node-pools create gvisor-pool \
       --cluster ${CLUSTER_NAME} \
       --num-nodes=1 \
       --location=${LOCATION} \
       --project=${PROJECT_ID} \
       --sandbox type=gvisor
    

## Create an Artifact Registry repository

Create a Docker repository in Artifact Registry to store the container image for your client application (the application that creates and manages the sandbox):
    
    
    gcloud artifacts repositories create ${REPOSITORY_NAME} \
       --repository-format=docker \
       --location=${LOCATION} \
       --description="Docker repository for Agent Sandbox"
    

## Install Agent Sandbox

**Note:** To support the snapshot suspend and resume workflow, this tutorial uses a manual installation method to deploy the Agent Sandbox components directly from the open-source GitHub repository. This manual installation is a temporary workaround until the snapshot features are fully available in the GKE Agent Sandbox add-on.

Install the Agent Sandbox core components and extensions on your cluster (using version v0.4.6 as an example):
    
    
    # Install the core agent-sandbox components
    kubectl apply -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/v0.4.6/manifest.yaml
    
    # Install the extensions (e.g., Warm Pools, Claims)
    kubectl apply -f https://github.com/kubernetes-sigs/agent-sandbox/releases/download/v0.4.6/extensions.yaml
    

## Configure storage and permissions

Configure a Cloud Storage bucket for storing Pod snapshots and grant the required Workload Identity permissions to the `snapshot-sa` service account and the GKE service agent. This allows your sandboxed workloads to securely save and retrieve snapshot objects:

  1. Create a new Cloud Storage bucket:
         
         gcloud storage buckets create "gs://${BUCKET_NAME}" \
             --uniform-bucket-level-access \
             --enable-hierarchical-namespace \
             --soft-delete-duration=0d \
             --location="${BUCKET_LOCATION}"
         

  2. Create a Kubernetes service account in the `default` namespace. Your sandboxed application (the Python counter script) uses this identity to authenticate to external APIs and securely access snapshot objects stored in Cloud Storage:
         
         kubectl create serviceaccount "snapshot-sa" \
             --namespace "default"
         

  3. Bind the `storage.bucketViewer` role to your service account using Workload Identity. This role allows the sandboxed workload to list the bucket contents and locate specific snapshots:
         
         gcloud storage buckets add-iam-policy-binding "gs://${BUCKET_NAME}" \
             --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/snapshot-sa" \
             --role="roles/storage.bucketViewer"
         

  4. Bind the `storage.objectUser` role to your service account using Workload Identity. This role provides the permission to read, save, and delete snapshot binary objects within the bucket:
         
         gcloud storage buckets add-iam-policy-binding "gs://${BUCKET_NAME}" \
             --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${PROJECT_ID}.svc.id.goog/subject/ns/default/sa/snapshot-sa" \
             --role="roles/storage.objectUser"
         

  5. Grant the GKE service agent permissions to manage (create, list, read, and delete) snapshot objects within the bucket:
         
         gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
             --member="serviceAccount:service-${PROJECT_NUMBER}@container-engine-robot.iam.gserviceaccount.com" \
             --role="roles/storage.objectUser" \
             --condition="expression=resource.name.startsWith(\"projects/_/buckets/${BUCKET_NAME}\"),title=restrict_to_bucket,description=Restricts access to one bucket only"
         




## Configure Pod snapshots

Create and apply the configuration files to install the required Kubernetes custom resources. These resources define how the cluster stores and manages Pod snapshots:

  * **PodSnapshotStorageConfig** : specifies the Cloud Storage bucket designated for storing snapshot binary objects.
  * **PodSnapshotPolicy** : defines how snapshots are triggered manually, how frequently they are grouped, and their retention policies.
  * **SandboxTemplate** : defines the underlying container, node selectors, and service accounts for running the isolated sandboxed workload.


  1. Create a new directory for the test client files:
         
         mkdir test_client
         

  2. Navigate to the new directory:
         
         cd test_client
         

  3. Create a file named `snapshot_storage_config.yaml`. This configuration specifies the target Cloud Storage bucket where the cluster saves the binary Pod snapshot state:
         
         apiVersion: podsnapshot.gke.io/v1
         kind: PodSnapshotStorageConfig
         metadata:
           name: example-pod-snapshot-storage-config
         spec:
           snapshotStorageConfig:
             gcs:
               bucket: "$BUCKET_NAME"
         

  4. Substitute the environment variable placeholder in the configuration file:
         
         sed -i "s/\$BUCKET_NAME/$BUCKET_NAME/g" snapshot_storage_config.yaml
         

  5. Apply the storage configuration manifest:
         
         kubectl apply -f snapshot_storage_config.yaml
         

  6. Wait for the storage configuration to be ready:
         
         kubectl wait --for=condition=Ready podsnapshotstorageconfig/example-pod-snapshot-storage-config --timeout=60s
         

  7. Create a file named `snapshot_policy.yaml`. This configuration establishes a retention rule that retains a maximum of two snapshots for your sandboxed workload. The trigger type is set to `manual`: this allows the client application to control snapshots on demand:
         
         apiVersion: podsnapshot.gke.io/v1
         kind: PodSnapshotPolicy
         metadata:
           name: example-pod-snapshot-policy
           namespace: default
         spec:
           storageConfigName: example-pod-snapshot-storage-config
           selector:
             matchLabels:
               app: agent-sandbox-workload
           triggerConfig:
             type: manual
             postCheckpoint: resume
           snapshotGroupingRules:
             groupByLabelValue:
               labels: ["agents.x-k8s.io/sandbox-name-hash", "tenant-id", "user-id"]
               groupRetentionPolicy:
                 maxSnapshotCountPerGroup: 2
         

  8. Apply the snapshot policy manifest:
         
         kubectl apply -f snapshot_policy.yaml
         

  9. Create a file named `python-counter-template.yaml`. This configuration defines the sandbox Pod, and assigns the `snapshot-sa` service account identity to it. This assignment helps ensure that the sandbox runs securely. Inside that Pod, the sandboxed application (a Python script) continuously prints an incrementing counter to the container logs:
         
         apiVersion: extensions.agents.x-k8s.io/v1alpha1
         kind: SandboxTemplate
         metadata:
           name: python-counter-template
           namespace: default
         spec:
           podTemplate:
             metadata:
               labels:
                 app: agent-sandbox-workload
             spec:
               serviceAccountName: snapshot-sa
               runtimeClassName: gvisor
               nodeSelector:
                 topology.kubernetes.io/zone: us-central1-a # Pin to a zone to avoid CPU mismatch during restore
               containers:
               - name: python-counter
                 image: python:3.13-slim
                 command: ["python3", "-c"]
                 args:
                   - |
                     import time
                     i = 0
                     while True:
                       print(f"Count: {i}", flush=True)
                       i += 1
                       time.sleep(1)
         

  10. Apply the sandbox template manifest:
         
         kubectl apply -f python-counter-template.yaml
         




## Build the client application

Create the container image for the client application and upload it to Artifact Registry.

  1. Create a file named `Dockerfile.client`. This file defines the Python runtime environment and dependencies for the client application:
         
         FROM python:3.13-slim
         
         WORKDIR /app
         
         RUN pip install "k8s-agent-sandbox[tracing]==0.4.6"
         
         # Copy test script
         COPY client_test.py /app/client_test.py
         
         CMD ["python", "/app/client_test.py"]
         

  2. Create a file named `client_test.py`. This script manages the sandbox lifecycle and verifies that the state successfully resumes after taking a snapshot:
         
         import time
         import logging
         import re
         from kubernetes import config, client
         from k8s_agent_sandbox.gke_extensions.snapshots import PodSnapshotSandboxClient
         
         logging.basicConfig(level=logging.INFO)
         
         def get_last_count(pod_name, namespace):
             v1 = client.CoreV1Api()
             try:
                 logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace)
                 counts = re.findall(r"Count: (\d+)", logs)
                 if counts:
                     return int(counts[-1])
                 return None
             except Exception as e:
                 logging.error(f"Failed to read logs for pod {pod_name}: {e}")
                 return None
         
         def get_current_pod_name(sandbox_id, namespace):
             custom_api = client.CustomObjectsApi()
             try:
                 sandbox_cr = custom_api.get_namespaced_custom_object(
                     group="agents.x-k8s.io",
                     version="v1alpha1",
                     namespace=namespace,
                     plural="sandboxes",
                     name=sandbox_id
                 )
                 metadata = sandbox_cr.get("metadata", {})
                 annotations = metadata.get("annotations", {})
                 return annotations.get("agents.x-k8s.io/pod-name")
             except Exception as e:
                 logging.error(f"Failed to get sandbox CR: {e}")
                 return None
         
         def get_current_count(sandbox_id, namespace="default"):
             pod_name = get_current_pod_name(sandbox_id, namespace)
             if not pod_name:
                 logging.error(f"Could not determine pod name for sandbox {sandbox_id}")
                 return None
             return get_last_count(pod_name, namespace)
         
         def suspend_sandbox(sandbox):
             logging.info("Pausing sandbox (using snapshots)...")
             try:
                 suspend_resp = sandbox.suspend(snapshot_before_suspend=True)
                 if suspend_resp.success:
                     logging.info("Sandbox paused successfully.")
                     if suspend_resp.snapshot_response:
                         logging.info(f"Snapshot created: {suspend_resp.snapshot_response.snapshot_uid}")
                     return suspend_resp
                 else:
                     logging.error(f"Failed to pause: {suspend_resp.error_reason}")
                     exit(1)
             except Exception as e:
                 logging.error(f"Failed to pause sandbox: {e}")
                 exit(1)
         
         def resume_sandbox(sandbox):
             logging.info("Resuming sandbox (using snapshots)...")
             try:
                 resume_resp = sandbox.resume()
                 if resume_resp.success:
                     logging.info("Sandbox resumed successfully.")
                     if resume_resp.restored_from_snapshot:
                         logging.info(f"Restored from snapshot: {resume_resp.snapshot_uid}")
                     return resume_resp
                 else:
                     logging.error(f"Failed to resume: {resume_resp.error_reason}")
                     exit(1)
             except Exception as e:
                 logging.error(f"Failed to resume sandbox: {e}")
                 exit(1)
         
         def verify_continuity(count_before, count_after):
             if count_before is not None and count_after is not None:
                 logging.info(f"Verification: Count before={count_before}, Count after={count_after}")
                 if count_after >= count_before:
                     logging.info("SUCCESS: Sandbox resumed from where it left off (or later).")
                 else:
                     logging.error("FAIL: Sandbox counter reset or went backwards!")
             else:
                 logging.warning("Could not verify counter continuity.")
         
         def main():
             try:
                 config.load_incluster_config()
             except config.ConfigException:
                 config.load_kube_config()
         
             client_reg = PodSnapshotSandboxClient()
         
             logging.info("Creating sandbox...")
             sandbox = client_reg.create_sandbox(template="python-counter-template", namespace="default")
             logging.info(f"Sandbox created with ID: {sandbox.sandbox_id}")
         
             logging.info("Waiting for sandbox to run...")
             time.sleep(10)
         
             count_before = get_current_count(sandbox.sandbox_id)
             logging.info(f"Count before suspend: {count_before}")
         
             suspend_sandbox(sandbox)
         
             logging.info("Waiting 10 seconds...")
             time.sleep(10)
         
             resume_sandbox(sandbox)
         
             logging.info("Waiting for sandbox to be ready again...")
             time.sleep(10)
         
             count_after = get_current_count(sandbox.sandbox_id)
             logging.info(f"Count after resume: {count_after}")
         
             verify_continuity(count_before, count_after)
         
             logging.info("Snapshot test completed successfully.")
         
         if __name__ == "__main__":
             main()
         

  3. Build the client container image and upload it to Artifact Registry. If your environment (such as Cloud Shell) has Docker installed, you can use Docker to build the image locally. If you are working in an environment without Docker, you can use Cloud Build to build and push the image remotely:

### Docker

     1. Configure Docker authentication for Artifact Registry:
            
            gcloud auth configure-docker "${LOCATION}-docker.pkg.dev"
            

     2. Build and push the client container image locally:
            
            docker build -t "${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/sandbox-client:latest" -f Dockerfile.client .
            docker push "${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}/sandbox-client:latest"
            

###  Cloud Build 

     1. Create a file named `cloudbuild.yaml`:
            
            steps:
            - name: 'gcr.io/cloud-builders/docker'
              args: ['build', '-t', '$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/sandbox-client:latest', '-f', 'Dockerfile.client', '.']
            images:
            - '$LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/sandbox-client:latest'
            

     2. Substitute the environment variable placeholders in the configuration file:
            
            sed -i "s/\$REPOSITORY_NAME/$REPOSITORY_NAME/g" cloudbuild.yaml
            sed -i "s/\$LOCATION/$LOCATION/g" cloudbuild.yaml
            sed -i "s/\$PROJECT_ID/$PROJECT_ID/g" cloudbuild.yaml
            

     3. Create the Cloud Storage bucket for Cloud Build logs:
            
            gcloud storage buckets create "gs://${CLOUDBUILD_BUCKET_NAME}" \
                --location="${BUCKET_LOCATION}"
            

     4. Grant necessary permissions to the Cloud Build service account.

The following commands use the Compute Engine default service account (`$PROJECT_NUMBER-compute@developer.gserviceaccount.com`), which is the default for most projects. If your project uses the legacy Cloud Build service account, replace the member email address in the following commands with `$PROJECT_NUMBER@cloudbuild.gserviceaccount.com`.

Because you added a conditional IAM binding to your project earlier in this tutorial, you should include the `--condition=None` flag when adding these new bindings. This prevents `gcloud` from pausing to ask for interactive confirmation:
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
               --role="roles/artifactregistry.writer"
            
            gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
               --role="roles/logging.logWriter"
            
            gcloud storage buckets add-iam-policy-binding "gs://$CLOUDBUILD_BUCKET_NAME" \
               --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
               --role="roles/storage.objectAdmin"
            

     5. Run the build using Cloud Build:
            
            gcloud builds submit --config cloudbuild.yaml
            




## Run the test

Deploy the client application to create the sandbox, trigger a snapshot, and verify that the internal counter successfully resumes from its saved state.

  1. Create a file named `client_sa.yaml`. This manifest defines the `agent-sandbox-client-sa` service account and its required RBAC permissions for managing sandbox custom resources:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: agent-sandbox-client-sa
           namespace: default
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: agent-sandbox-client-role
           namespace: default
         rules:
         - apiGroups: ["agents.x-k8s.io"]
           resources: ["sandboxes"]
           verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
         - apiGroups: ["extensions.agents.x-k8s.io"]
           resources: ["sandboxclaims"]
           verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
         - apiGroups: ["podsnapshot.gke.io"]
           resources: ["podsnapshotmanualtriggers", "podsnapshots"]
           verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
         - apiGroups: [""]
           resources: ["pods", "pods/log"]
           verbs: ["get", "list", "watch"]
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: RoleBinding
         metadata:
           name: agent-sandbox-client-rolebinding
           namespace: default
         subjects:
         - kind: ServiceAccount
           name: agent-sandbox-client-sa
           namespace: default
         roleRef:
           kind: Role
           name: agent-sandbox-client-role
           apiGroup: rbac.authorization.k8s.io
         

  2. Apply the client service account and RBAC manifest:
         
         kubectl apply -f client_sa.yaml
         

  3. Create a file named `client_pod.yaml`. This manifest creates the client application Pod using the prebuilt container image:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: agent-sandbox-client-pod
           namespace: default
         spec:
           serviceAccountName: agent-sandbox-client-sa
           containers:
           - name: client
             image: $LOCATION-docker.pkg.dev/$PROJECT_ID/$REPOSITORY_NAME/sandbox-client:latest
             imagePullPolicy: Always
           restartPolicy: Never
         

  4. Substitute the environment variable placeholders in the manifest:
         
         sed -i "s/\$REPOSITORY_NAME/$REPOSITORY_NAME/g" client_pod.yaml
         sed -i "s/\$LOCATION/$LOCATION/g" client_pod.yaml
         sed -i "s/\$PROJECT_ID/$PROJECT_ID/g" client_pod.yaml
         

  5. Apply the client application Pod manifest:
         
         kubectl apply -f client_pod.yaml
         

  6. Stream the Pod logs to verify the execution flow:
         
         kubectl logs -f agent-sandbox-client-pod
         




When the test is running correctly, the output looks similar to this (shortened here for readability):
    
    
    2026-04-21 23:02:39,030 - INFO - Creating sandbox...
    ...
    2026-04-21 23:02:51,755 - INFO - Count before suspend: 23
    2026-04-21 23:02:51,755 - INFO - Pausing sandbox (using snapshots)...
    ...
    2026-04-21 23:03:07,115 - INFO - Resuming sandbox (using snapshots)...
    ...
    2026-04-21 23:03:21,329 - INFO - Count after resume: 38
    2026-04-21 23:03:21,329 - INFO - Verification: Count before=23, Count after=38
    2026-04-21 23:03:21,329 - INFO - SUCCESS: Sandbox resumed from where it left off (or later).
    

The output shows that the sandbox successfully preserves its state when suspended and resumed. The counter stops advancing while the sandbox is suspended (paused and scaled to zero), and resumes the counter when the sandbox is restored. Without suspending, the counter would have continued to advance during the suspension period and the count would be significantly higher.

## Clean up resources

To avoid incurring charges to your Google Cloud account, delete the resources that you created:

  1. Delete the GKE cluster. This also deletes the node pool and all Kubernetes service accounts inside it:
         
         gcloud beta container clusters delete ${CLUSTER_NAME} --location="${LOCATION}" --quiet
         

  2. Delete the Artifact Registry repository to remove the Docker repository you created for the test image:
         
         gcloud artifacts repositories delete ${REPOSITORY_NAME} --location="${LOCATION}" --quiet
         

  3. Delete the Cloud Storage bucket and all the snapshots inside it. This automatically removes the bucket-level Workload Identity IAM bindings applied to it:
         
         gcloud storage rm --recursive "gs://${BUCKET_NAME}"
         

  4. Remove the project-level IAM binding for the GKE service agent:
         
         gcloud projects remove-iam-policy-binding "${PROJECT_ID}" \
             --member="serviceAccount:service-${PROJECT_NUMBER}@container-engine-robot.iam.gserviceaccount.com" \
             --role="roles/storage.objectUser" \
             --condition="expression=resource.name.startsWith(\"projects/_/buckets/${BUCKET_NAME}\"),title=restrict_to_bucket,description=Restricts access to one bucket only"
         

  5. If you used Cloud Build instead of Docker to build and push the container image, delete the logs bucket and remove the service account permissions:
         
         gcloud storage rm --recursive "gs://${CLOUDBUILD_BUCKET_NAME}"
         
         gcloud projects remove-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/artifactregistry.writer"
         
         gcloud projects remove-iam-policy-binding $PROJECT_ID \
             --member="serviceAccount:$PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/logging.logWriter"
         




## What's next

  * Learn how to [Isolate AI code execution: external trigger](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox).
  * Learn how to [Save and restore Agent Sandbox environments](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).
  * To understand the isolation layers that protect your untrusted workloads, see [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
  * Explore the open-source [Agent Sandbox project](https://github.com/kubernetes-sigs/agent-sandbox) on GitHub.
  * Learn how to use open source [Kata Containers with Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/kata-gke-sandbox). Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
