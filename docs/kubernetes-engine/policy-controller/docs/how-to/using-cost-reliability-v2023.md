---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cost-reliability-v2023/
title: Use Cost and Reliability policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:18.595547+00:00
---

# Use Cost and Reliability policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cost-reliability-v2023/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use Cost and Reliability policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [Cost and Reliability Policy bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/cost-reliability-v2023) which helps adopt [best practices](https://cloud.google.com/blog/products/containers-kubernetes/new-report-state-of-kubernetes-cost-optimization) for running cost-efficient GKE clusters without compromising the performance or reliability of their workloads.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

## Cost and Reliability policy bundle constraints

Constraint Name  | Constraint Description   
---|---  
cost-reliability-v2023-pod-disruption-budget  | Requires PodDisruptionBudget configuration for Deployments, ReplicaSets, StatefulSets, and ReplicationControllers.   
cost-reliability-v2023-pod-resources-best-practices  | Requires that containers are setting resource requests and are following the best practices.   
cost-reliability-v2023-required-labels  | Requires all Pods and Controllers (ReplicaSet, Deployment, StatefulSet, and DaemonSet) to have the required labels: environment, team, and app.   
cost-reliability-v2023-restrict-repos  | Restricts container images to an allowed repos list to use Artifact Registry to take advantage of [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming).   
cost-reliability-v2023-spotvm-termination-grace  | Requires terminationGracePeriodSeconds of 15s or less for Pods and Pod Templates with a nodeSelector or nodeAfffinty for gke-spot.   
  
## Before you begin

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) , which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) on your cluster with the default library of constraint templates. You must also [enable support for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential) as this bundle contains referential constraints.



### Configure Policy Controller for referential constraints

**Warning:** You can overwrite your changes. If you already have an existing `Config` in the `gatekeeper-system` namespace, you must include all previous customization settings to preserve your changes.

  1. Save the following YAML manifest to a file as `policycontroller-config.yaml`. The manifest configures Policy Controller to watch specific kinds of objects.
         
         apiVersion: config.gatekeeper.sh/v1alpha1
         kind: Config
         metadata:
           name: config
           namespace: "gatekeeper-system"
         spec:
           sync:
             syncOnly:
               - group: ""
                 version: "v1"
                 kind: "Service"
               - group: "policy"
                 version: "v1"
                 kind: "PodDisruptionBudget"
         

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




### Configure your cluster and workload

  1. Any `pod` selected by a `service` must include a [Readiness Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).
  2. All `deployment`, `replicaset`, `statefulset`, and `replicationcontroller` must include a [`poddisruptionbudget`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).
  3. All containers should include `cpu` and `memory` requests, and `memory` limit equal to `memory` requests following [best practices](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/).
  4. Add `environment`, `team`, and `app` labels to all Pods and Pod Templates.
  5. Host container images using [Artifact Registry](https://docs.cloud.google.com/artifact-registry) in the same [region](https://docs.cloud.google.com/compute/docs/regions-zones) as your cluster to enable [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming). Allow the relevant Artifact Registry by following the example in `cost-reliability-v2023-restrict-repos`.
  6. All Pods and Pod Templates using [`gke-spot`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) must include a [`terminationGracePeriodSeconds`](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) of 15 seconds or less.



## Audit Cost and Reliability policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the Cost and Reliability policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview) , or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) .

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cost-reliability-v2023
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cost-reliability-v2023
         

The output is the following:
         
         gkespotvmterminationgrace.constraints.gatekeeper.sh/cost-reliability-v2023-spotvm-termination-grace created
         k8sallowedrepos.constraints.gatekeeper.sh/cost-reliability-v2023-restrict-repos created
         k8spoddisruptionbudget.constraints.gatekeeper.sh/cost-reliability-v2023-pod-disruption-budget created
         k8spodresourcesbestpractices.constraints.gatekeeper.sh/cost-reliability-v2023-pod-resources-best-practices created
         k8srequiredlabels.constraints.gatekeeper.sh/cost-reliability-v2023-required-labels created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cost-reliability-v2023
         

The output is similar to the following:
         
         NAME                                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         gkespotvmterminationgrace.constraints.gatekeeper.sh/cost-reliability-v2023-spotvm-termination-grace   dryrun               0
         
         NAME                                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spodresourcesbestpractices.constraints.gatekeeper.sh/cost-reliability-v2023-pod-resources-best-practices   dryrun               0
         
         NAME                                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spoddisruptionbudget.constraints.gatekeeper.sh/cost-reliability-v2023-pod-disruption-budget   dryrun               0
         
         NAME                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sallowedrepos.constraints.gatekeeper.sh/cost-reliability-v2023-restrict-repos   dryrun               0
         
         NAME                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/cost-reliability-v2023-required-labels   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/).

kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the PCI-DSS v3.2.1 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cost-reliability-v2023
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval cost-reliability-v2023 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
         -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd cost-reliability-v2023 kpt live init
         

  5. Apply the policy constraints with kpt:
         
         kpt live apply
         

  6. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kpt live status --output table --poll-until current
         

A status of `CURRENT` confirms successful installation of the constraints.




###  Config Sync 

  1. Install and setup [kpt](https://kpt.dev/installation/).

kpt is used in these instructions to customize and deploy Kubernetes resources.

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  2. Change into the sync directory for Config Sync:
         
         cd SYNC_ROOT_DIR
         

**Note:** Kpt v1.0.0-beta.17 and later automatically create a `resourcegroup.yaml` file during `live init` which shouldn't be checked into your Config Sync repo. If not already present, add `resourcegroup.yaml` to your repo's `.gitignore` file.

To create or append `.gitignore` with `resourcegroup.yaml`:
         
         echo resourcegroup.yaml >> .gitignore
         

  3. Create a dedicated `policies` directory:
         
         mkdir -p policies
         

  4. Download the Cost and Reliability policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cost-reliability-v2023 policies/cost-reliability-v2023
         

  5. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/cost-reliability-v2023 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  6. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/cost-reliability-v2023
         kpt live apply --dry-run policies/cost-reliability-v2023
         

  7. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/cost-reliability-v2023` to your root `kustomization.yaml`. Otherwise remove the `policies/cost-reliability-v2023/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/cost-reliability-v2023/kustomization.yaml
         

  8. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/cost-reliability-v2023 git commit -m 'Adding Cost and Reliability policy audit enforcement'
         git push
         

  9. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
      kubectl get constraint -l policycontroller.gke.io/bundleName=cost-reliability-v2023 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
      

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
      kubectl get constraint -l policycontroller.gke.io/bundleName=cost-reliability-v2023 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
      

## Change Cost and Reliability policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cost-reliability-v2023 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cost-reliability-v2023
         




### kpt

  1. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `warn`:
         
         kpt fn eval -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  2. Apply the policy constraints:
         
         kpt live apply
         




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Change into the sync directory for Config Sync:
         
         cd SYNC_ROOT_DIR
         

  2. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `warn`:
         
         kpt fn eval policies/cost-reliability-v2023 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/cost-reliability-v2023
         git commit -m 'Adding Cost and Reliability policy bundle warn enforcement'
         git push
         

  4. Verify the status of the installation:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the installed policies.




## Test policy enforcement

Create a non-compliant resource on the cluster using the following command:
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: v1
    kind: Pod
    metadata:
      namespace: default
      name: wp-non-compliant
      labels:
        app: wordpress
    spec:
      containers:
        - image: wordpress
          name: wordpress
          ports:
          - containerPort: 80
            hostPort: 80
            name: wordpress
    EOF
    

The admission controller should produce a warning listing out the policy violations that this resource violates, as shown in the following example:
    
    
    Warning: [cost-reliability-v2023-pod-resources-best-practices] Container <wordpress> must set <cpu> request.
    Warning: [cost-reliability-v2023-pod-resources-best-practices] Container <wordpress> must set <memory> request.
    Warning: [cost-reliability-v2023-required-labels] This app is missing one or more required labels: `environment`, `team`, and `app`.
    Warning: [cost-reliability-v2023-restrict-repos] container <wordpress> has an invalid image repo <wordpress>, allowed repos are ["gcr.io/gke-release/", "gcr.io/anthos-baremetal-release/", "gcr.io/config-management-release/", "gcr.io/kubebuilder/", "gcr.io/gkeconnect/", "gke.gcr.io/"]
    pod/wp-non-compliant created
    

## Remove Cost and Reliability policy bundle

If needed, the Cost and Reliability policy bundle can be removed from the cluster.

### kubectl

Use kubectl to remove the policies:
    
    
      kubectl delete constraint -l policycontroller.gke.io/bundleName=cost-reliability-v2023
      

### kpt

Remove the policies:
    
    
      kpt live destroy
      

###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repo:
         
         git rm -r SYNC_ROOT_DIR/policies/cost-reliability-v2023
         git commit -m 'Removing Cost and Reliability policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
