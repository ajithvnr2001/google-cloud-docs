---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox/
title: Enable Agent Sandbox on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:15.448298+00:00
---

# Enable Agent Sandbox on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Enable Agent Sandbox on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to enable the Agent Sandbox feature in a Google Kubernetes Engine (GKE) cluster. It also explains how to create a sandboxed environment on the cluster to safely execute untrusted code.

For an overview of how the Agent Sandbox feature isolates untrusted AI-generated code, see [About GKE Agent Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/agent-sandbox).

## Costs

Agent Sandbox is offered at no extra charge in GKE. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create.

To avoid unnecessary charges, ensure that you disable GKE or delete the project after you have completed this document.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Artifact Registry, Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,container.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Ensure that your cluster is running GKE version 1.36.3-gke.1767000 or later (supports the `v1beta1` API).



## Define environment variables

To simplify the commands that you run in this document, you can set environment variables in Cloud Shell. In Cloud Shell, define the following useful environment variables by running the following commands:
    
    
    export PROJECT_ID=$(gcloud config get project)
    export CLUSTER_NAME="agent-sandbox-cluster"
    export LOCATION="us-central1"
    export CLUSTER_VERSION="1.36.3-gke.1767000"
    export NODE_POOL_NAME="agent-sandbox-pool"
    export MACHINE_TYPE="e2-standard-2"
    

Here's an explanation of these environment variables:

  * `PROJECT_ID`: the ID of your current Google Cloud project. Defining this variable helps ensure that all resources, like your GKE cluster, are created in the correct project.
  * `CLUSTER_NAME`: the name of your GKE cluster—for example, `agent-sandbox-cluster`.
  * `LOCATION`: the Google Cloud region or zone where your GKE cluster is created. Set this to the region (for example, `us-central1`) if you create an Autopilot cluster, or the zone (for example, `us-central1-a`) if you create a Standard cluster.
  * `CLUSTER_VERSION`: the version of GKE your cluster will run (`1.36.3-gke.1767000` or later).
  * `NODE_POOL_NAME`: the name of the node pool that will run sandboxed workloads—for example, `agent-sandbox-pool`. This variable is only required if you are creating a GKE Standard cluster.
  * `MACHINE_TYPE`: the machine type of the nodes in your node pool—for example, `e2-standard-2`. For details about different machine series and choosing between different options, see the [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource). This variable is only required if you are creating a GKE Standard cluster.



## Enable Agent Sandbox

You can enable the Agent Sandbox feature when you create a new cluster, or when updating an existing cluster.

### Enable Agent Sandbox when creating a new GKE cluster

We recommend that you use a Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Autopilot

To create a new GKE Autopilot cluster with Agent Sandbox enabled, include the `--enable-agent-sandbox` flag:
    
    
    gcloud beta container clusters create-auto ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --cluster-version=${CLUSTER_VERSION} \
        --enable-agent-sandbox
    

For an Autopilot cluster, ensure that the `LOCATION` environment variable is set to a region (for example, `us-central1`).

### Standard

To create a new GKE Standard cluster with Agent Sandbox enabled, you must create the cluster, add a node pool with gVisor enabled, and then enable the Agent Sandbox feature. To save costs, we recommend creating a zonal cluster with a single node per pool:

  1. Create the cluster:
         
         gcloud beta container clusters create ${CLUSTER_NAME} \
             --location=${LOCATION} \
             --num-nodes=1 \
             --cluster-version=${CLUSTER_VERSION}
         

For this Standard cluster, ensure that the `LOCATION` environment variable is set to a zone (for example, `us-central1-a`).

  2. Create a separate node pool with gVisor enabled:
         
         gcloud container node-pools create ${NODE_POOL_NAME} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=${MACHINE_TYPE} \
             --location=${LOCATION} \
             --num-nodes=1 \
             --image-type=cos_containerd \
             --sandbox=type=gvisor
         

The `LOCATION` must be the same zone you used when creating the cluster.

  3. Update the cluster to enable the Agent Sandbox feature:
         
         gcloud beta container clusters update ${CLUSTER_NAME} \
             --location=${LOCATION} \
             --enable-agent-sandbox
         




### Enable Agent Sandbox when updating an existing GKE cluster

To enable Agent Sandbox on an existing cluster, the cluster must be running version 1.36.3-gke.1767000 or later, which supports the `v1beta1` API.

Ensure that your `LOCATION` environment variable is set to the region or zone where your existing cluster is located.

  1. If you are using a GKE Standard cluster, Agent Sandbox relies on gVisor. If your Standard cluster doesn't have a gVisor-enabled node pool, you must create one first:
         
         gcloud container node-pools create ${NODE_POOL_NAME} \
             --cluster=${CLUSTER_NAME} \
             --machine-type=${MACHINE_TYPE} \
             --location=${LOCATION} \
             --image-type=cos_containerd \
             --sandbox=type=gvisor
         

  2. Update the cluster to enable the Agent Sandbox feature:
         
         gcloud beta container clusters update ${CLUSTER_NAME} \
             --location=${LOCATION} \
             --enable-agent-sandbox
         




## Verify the configuration

You can verify whether the Agent Sandbox feature is enabled by inspecting the cluster description.
    
    
    gcloud beta container clusters describe ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --format="value(addonsConfig.agentSandboxConfig.enabled)"
    

If you created an Autopilot cluster, the location is the region (for example, `us-central1`). If you created a Standard cluster, the location is the zone (for example, `us-central1-a`).

If the feature is successfully enabled, the command returns `True`.

## Agent Sandbox deployment requirements

To successfully deploy a workload, such as a `Sandbox` or `SandboxTemplate`, your YAML manifest must include specific security and configuration settings. GKE enforces these requirements using a Validating Admission Policy (VAP). If these requirements are not met, the admission controller rejects the deployment.

### Required configuration

Your deployment manifest must include the following settings:

  * `runtimeClassName: gvisor`: ensures the Pod runs in a gVisor sandbox.
  * `automountServiceAccountToken: false`: prevents the Pod from automatically mounting the default service account token.
  * `securityContext.runAsNonRoot: true`: ensures the container does not run as the root user.
  * `securityContext.capabilities.drop: ["ALL"]`: drops all Linux capabilities from the container.
  * `resources.limits`: you must specify CPU and memory limits to prevent potential denial-of-service (DoS) scenarios.
  * `nodeSelector`: must target `sandbox.gke.io/runtime: gvisor`.
  * `tolerations`: must include a toleration for the `sandbox.gke.io/runtime=gvisor:NoSchedule` taint.



### Prohibited configuration

Your deployment manifest must **not** include any of the following:

  * `hostNetwork: true`, `hostPID: true`, or `hostIPC: true`.
  * `privileged: true` in container security contexts.
  * `HostPath` volumes.
  * Added capabilities (`capabilities.add`).
  * `hostPort` settings.
  * Custom sysctls.
  * Projected volumes for service account tokens or certificates.



## Deploy a sandboxed environment

We recommend deploying a sandboxed environment by defining a SandboxTemplate and keeping pre-warmed instances ready using a SandboxWarmPool. You can then request an instance from this warm node pool using a SandboxClaim. Alternatively, you can create a Sandbox directly, but this approach doesn't support warm pools.

SandboxTemplate, SandboxWarmPool, SandboxClaim, and Sandbox are [Kubernetes custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

### Recommended: Create a SandboxTemplate and SandboxWarmPool

The SandboxTemplate acts as a reusable blueprint. The SandboxWarmPool helps ensure that a specified number of pre-warmed Pods are always running and ready to be claimed. Use of this custom resource minimizes startup latency.

To deploy a sandboxed environment by creating the SandboxTemplate and SandboxWarmPool, complete the following steps:

  1. In Cloud Shell, create a file named `sandbox-template.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxTemplate
         metadata:
           name: python-runtime-template
           namespace: default
         spec:
           podTemplate:
             metadata:
               labels:
                 sandbox-type: python-runtime
             spec:
               runtimeClassName: gvisor # Required
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor # Required
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: runtime
                 image: registry.k8s.io/agent-sandbox/python-runtime-sandbox:v0.1.0
                 ports:
                 - containerPort: 8888
                 resources:
                   requests:
                     cpu: "250m"
                     memory: "512Mi"
                   limits:
                     cpu: "500m"
                     memory: "1Gi" # Required
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
               restartPolicy: OnFailure
         

  2. Apply the `SandboxTemplate` manifest:
         
         kubectl apply -f sandbox-template.yaml
         

  3. Create a file named `sandbox-warmpool.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxWarmPool
         metadata:
           name: python-runtime-warmpool
           namespace: default
           labels:
             app: python-runtime-warmpool
         spec:
           replicas: 2
           sandboxTemplateRef:
             # This must match the name of the SandboxTemplate.
             name: python-runtime-template
         

  4. Apply the `SandboxWarmPool` manifest:
         
         kubectl apply -f sandbox-warmpool.yaml
         




### Create a SandboxClaim

The SandboxClaim requests a sandbox from the warm pool. Because you created a warm pool, the created Sandbox adopts a running Pod from the pool instead of starting a fresh Pod.

To request a sandbox from the warm pool by creating a `SandboxClaim`, complete the following steps:

  1. Create a file named `sandbox-claim.yaml` with the following content:
         
         apiVersion: extensions.agents.x-k8s.io/v1beta1
         kind: SandboxClaim
         metadata:
           name: sandbox-claim
           namespace: default
         spec:
           warmPoolRef:
             # This must match the name of the SandboxWarmPool.
             name: python-runtime-warmpool
         

  2. Apply the `SandboxClaim` manifest:
         
         kubectl apply -f sandbox-claim.yaml
         

  3. Verify that the sandbox, claim, and warm pool are ready:
         
         kubectl get sandboxwarmpool,sandboxclaim,sandbox,pod
         




### Alternative: Create a Sandbox directly

If you don't need the fast startup times provided by warm pools, you can deploy a Sandbox directly without using templates.

To deploy a sandboxed environment by creating a Sandbox directly, complete the following steps:

  1. Create a file named `sandbox.yaml` with the following content:
         
         apiVersion: agents.x-k8s.io/v1beta1
         kind: Sandbox
         metadata:
           name: sandbox-example-2
         spec:
           replicas: 1
           podTemplate:
             metadata:
               labels:
                 sandbox: sandbox-example
             spec:
               runtimeClassName: gvisor
               restartPolicy: OnFailure
               automountServiceAccountToken: false # Required
               securityContext:
                 runAsNonRoot: true # Required
                 runAsUser: 1000 # Required if image defaults to root (e.g. busybox)
               nodeSelector:
                 sandbox.gke.io/runtime: gvisor
               tolerations:
               - key: "sandbox.gke.io/runtime"
                 value: "gvisor"
                 effect: "NoSchedule" # Required
               containers:
               - name: my-container
                 image: busybox
                 command: ["/bin/sh", "-c"]
                 args: ["sleep 3600000; echo 'Container finished successfully'; exit 0"]
                 securityContext:
                   capabilities:
                     drop: ["ALL"] # Required
                   allowPrivilegeEscalation: false
                 resources:
                   limits:
                     cpu: "100m"
                     memory: "128Mi" # Required
         

  2. Apply the `Sandbox` manifest:
         
         kubectl apply -f sandbox.yaml
         

  3. Verify that the sandbox is running:
         
         kubectl get sandbox
         




## Migrate Agent Sandbox from `v1alpha1` to `v1beta1`

If your cluster was deployed with an earlier version of Agent Sandbox by using `v1alpha1` custom resources, you can upgrade to GKE version 1.36.3-gke.1767000 or later with _near-zero workload downtime_.

> **Note:** This migration procedure applies to clusters using the managed GKE Agent Sandbox feature (`--enable-agent-sandbox`). If you deployed Agent Sandbox using open-source manifests, refer to the [upstream migration guide](https://github.com/kubernetes-sigs/agent-sandbox/blob/v0.5.6/docs/api-migration-guide.md).

### Main API differences between `v1alpha1` and `v1beta1`

Concept | `v1alpha1` behavior | `v1beta1` behavior | Migration impact  
---|---|---|---  
**SandboxClaim targets** | Allowed direct reference to `SandboxTemplate` without a warm pool (cold start). | _Requires_ a reference to a `SandboxWarmPool` (`spec.warmPoolRef.name`). | Cold-start claims must be mapped to a shadow warm pool (`replicas: 0`).  
**Sandbox operating mode** | Inferred from replicas or state fields. | Explicit value for the `spec.operatingMode` field (such as `Running` or `Suspended`). | Conversion webhook automatically maps and sets this field.  
**CustomResourceDefinition storage version** | `v1alpha1` stored in etcd (`storage: true`). | `v1beta1` stored in etcd (`storage: true`). | Webhook dynamically converts; post-upgrade step re-persists etcd objects.  
**Conversion webhook** | None. | Active on `/convert` (Port 9447). | Bidirectional conversion between `v1alpha1` and `v1beta1`.  
  
### Migrate using the migration tool

To automatically create shadow warm pools and re-persist storage, use the canonical migration script from the [Agent Sandbox repository](https://github.com/kubernetes-sigs/agent-sandbox/blob/v0.5.6/docs/api-migration-guide.md).

Download and prepare the script:
    
    
    curl -LO https://raw.githubusercontent.com/kubernetes-sigs/agent-sandbox/v0.5.6/helm/files/migrate.sh
    chmod +x migrate.sh
    

### Step-by-step migration runbook

To migrate an existing cluster with near-zero workload downtime, complete the following three phases in order:

#### Phase 1: Pre-upgrade bootstrap phase

> **Important:** The bootstrap phase _must_ be executed while the cluster is running `v1alpha1`. You can't run the bootstrap phase after upgrading because the `v1beta1` API schema will no longer expose the previous `spec.sandboxTemplateRef` on claims.

  1. **Back up existing resources:** Save a YAML backup of your declarative Agent Sandbox resources (`sandboxtemplates`, `sandboxwarmpools`, and `sandboxclaims`):
         
         kubectl get sandboxtemplates,sandboxwarmpools,sandboxclaims \
             --all-namespaces -o yaml > agent-sandbox-v1alpha1-backup.yaml
         

**Note:** This command excludes `Sandbox` objects managed by a `SandboxClaim` or `SandboxWarmPool` because the controller dynamically recreates them when claims and warm pools are restored. If you created standalone `Sandbox` resources directly without a claim or warm pool, include `sandboxes` in your backup (or back them up separately) so they are not lost on restore.
  2. Verify template security compliance: ensure that existing `SandboxTemplate` resources meet the Agent Sandbox deployment requirements. During the storage migration in Phase 3, the admission controller rejects updates to any templates that do not comply with these security policies.

  3. Preview the shadow pools to be created:
         
         ./migrate.sh --phase=bootstrap --dry-run
         

  4. Execute the bootstrap phase:
         
         ./migrate.sh --phase=bootstrap
         

  5. Verify the created shadow pools:
         
         kubectl get sandboxwarmpools --all-namespaces \
             -o custom-columns="NAMESPACE:.metadata.namespace,NAME:.metadata.name,REPLICAS:.spec.replicas,SHADOW:.metadata.annotations.agents\.x-k8s\.io/migration-shadow"
         

**Note:** Shadow pools are created without replicas, and don't incur additional compute cost or increase the node footprint.



#### Phase 2: Upgrade the GKE control plane

Upgrade the GKE control plane to version 1.36.3-gke.1767000 or later:
    
    
    gcloud container clusters upgrade ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --master \
        --cluster-version=1.36.3-gke.1767000
    

During the control plane rollout, note the following:

  * Pods experience _no restarts or downtime_.
  * The new controller and `/convert` webhook endpoint are deployed on the control plane.



> **Warning:** Phase 3 is the point of no return for zero-downtime migration. Running `./migrate.sh --phase=migrate` rewrites all objects in etcd to the `v1beta1` schema. After this step, older control plane versions cannot deserialize `v1beta1` objects. Confirm that Phases 1 and 2 completed cleanly before proceeding.

#### Phase 3: Post-upgrade storage migration

After the control plane upgrade completes, refresh your credentials and rewrite the stored etcd objects by running the storage migration phase:
    
    
    ./migrate.sh --phase=migrate
    

### Post-migration verification checklist

Check item | Command | Expected result  
---|---|---  
**CustomResourceDefinition storage versions** | `kubectl get crd sandboxes.agents.x-k8s.io sandboxclaims.extensions.agents.x-k8s.io sandboxtemplates.extensions.agents.x-k8s.io sandboxwarmpools.extensions.agents.x-k8s.io -o jsonpath='{range .items[*]}{.metadata.name}{": storedVersions="}{.status.storedVersions}{"\n"}{end}'` | All 4 CustomResourceDefinitions display:  
`storedVersions=["v1beta1"]`  
**Pod continuity** | `kubectl get pods -n default -o wide` | `Status: 1/1 Running`  
`Restarts: 0`  
(applies to clusters with active running sandboxes)  
**Claim binding** | `kubectl get sandboxclaims -n default -o yaml` | `spec.warmPoolRef.name: shadow-pool-...`  
`status.conditions: Ready=True` (requires template compliance with admission requirements)  
**v1alpha1 compatibility** | `kubectl get sandboxes.v1alpha1.agents.x-k8s.io` | Displays deprecation warning and returns resource  
**v1beta1 native CRUD** | `kubectl apply -f sandbox-claim.yaml` | Applies with 0 warnings  
  
If a CustomResourceDefinition continues to list `["v1alpha1", "v1beta1"]` in `.status.storedVersions` after the migration phase completes, this is expected Kubernetes behavior. The migration script rewrites all existing records to `v1beta1` in etcd, but Kubernetes does not automatically remove deprecated versions from the `status.storedVersions` list.

After confirming that all resources are migrated, you can optionally prune `v1alpha1` from the stored versions:
    
    
    for crd in \
        sandboxes.agents.x-k8s.io \
        sandboxclaims.extensions.agents.x-k8s.io \
        sandboxtemplates.extensions.agents.x-k8s.io \
        sandboxwarmpools.extensions.agents.x-k8s.io; do
      kubectl patch crd "${crd}" --subresource=status --type=merge \
        -p '{"status":{"storedVersions":["v1beta1"]}}'
    done
    

### Troubleshoot migration issues

If you encounter issues after upgrading the control plane or running the storage migration, resolve them forward rather than attempting to downgrade the control plane:

  * **Claim stuck in`WarmPoolNotFound`:**

    * If a cold-start `v1alpha1` claim was upgraded without running `./migrate.sh --phase=bootstrap`, create the missing shadow warm pool manually:
          
          apiVersion: extensions.agents.x-k8s.io/v1beta1
          kind: SandboxWarmPool
          metadata:
            name: shadow-pool-TEMPLATE_NAME
            namespace: NAMESPACE
            annotations:
              agents.x-k8s.io/migration-shadow: "true"
          spec:
            replicas: 0
            sandboxTemplateRef:
              name: TEMPLATE_NAME
          

    * If a claim named a specific warm pool that no longer exists, create the missing `SandboxWarmPool` resource with that name, or update `spec.warmPoolRef.name` on the claim to reference an existing warm pool.

  * **Claim condition`Ready=False`:** Run `kubectl describe sandboxclaim` to inspect the events on the claim. Ensure that the referenced `SandboxTemplate` meets all Agent Sandbox deployment requirements, and re-apply the template if needed.

  * **Conversion or controller errors:** Verify that the control plane leader election lease is active by running `kubectl get leases -n gke-managed-agentsandbox`. If issues persist, contact [Cloud Customer Care](https://docs.cloud.google.com/support).




## Disable Agent Sandbox

To disable the Agent Sandbox feature, use the `gcloud beta container clusters update` command with the `--no-enable-agent-sandbox` flag.
    
    
    gcloud beta container clusters update ${CLUSTER_NAME} \
        --location=${LOCATION} \
        --no-enable-agent-sandbox
    

If you created an Autopilot cluster, the location is the region (for example, `us-central1`). If you created a Standard cluster, the location is the zone (for example, `us-central1-a`).

## Clean up resources

To avoid incurring charges to your Google Cloud account, delete the GKE cluster that you created.
    
    
    gcloud container clusters delete $CLUSTER_NAME \
        --location=${LOCATION} \
        --quiet
    

If you created an Autopilot cluster, the location is the region (for example, `us-central1`). If you created a Standard cluster, the location is the zone (for example, `us-central1-a`).

## What's next

  * Learn how to [save and restore Agent Sandbox environments with Pod snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/agent-sandbox-pod-snapshots).
  * Learn about the underlying technology used by [Agent Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
  * Learn more about [GKE security](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Explore the [Agent Sandbox open-source project](https://github.com/kubernetes-sigs/agent-sandbox) on GitHub.
  * Learn how to use open source [Kata Containers with Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox/tree/main/examples/kata-gke-sandbox). Kata Containers isn't a Google Cloud product. If you install and use this software, then you're responsible for management and troubleshooting. Google's support and SLAs don't apply to Kata Containers.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
