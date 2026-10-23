---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pss-restricted/
title: Use Pod Security Standards Restricted policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:16.721538+00:00
---

# Use Pod Security Standards Restricted policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pss-restricted/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use Pod Security Standards Restricted policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that you can use with the [Pod Security Standards Restricted bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/tree/main/anthos-bundles/pss-restricted-v2022). This bundle lets you achieve many of the same protections as the [Kubernetes Pod Security Standards (PSS) Restricted policy](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted), with the ability to test your policies before enforcing them and exclude coverage of specific resources.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

The bundle includes these constraints which map to the following [Kubernetes Pod Security Standards (PSS) Restricted policy](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted) controls:

Constraint Name | Constraint Description | Control Name  
---|---|---  
pss-restricted-v2022-psp-volume-types | Usage of volume types | Volume Types  
pss-restricted-v2022-privilege-escalation | Restricting escalation to root privileges | Privilege Escalation  
pss-restricted-v2022-running-as-non-root | The `runAsNonRoot` value of the container | Running as Non-root  
pss-restricted-v2022-running-as-non-root-user | The user ID of the container | Running as Non-root user  
pss-restricted-v2022-seccomp | The seccomp profile used by containers | Seccomp  
pss-restricted-v2022-capabilities | Linux capabilities | Capabilities  
  
## Before you begin

**Important:** The Pod Security Standards Restricted profile builds on and includes all the Pod Security Standards Baseline profile controls. Install the [PSS-Baseline bundle](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pss-baseline) prior to using the PSS-Restricted bundle.

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) v1.11.1 or higher on your cluster with the default library of constraint templates.



## Audit Pod Security Standards Restricted policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the Google recommended best practices outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pss-restricted-v2022
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pss-restricted-v2022
         

The output is the following:
         
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/pss-restricted-v2022-privilege-escalation created
         k8spspallowedusers.constraints.gatekeeper.sh/pss-restricted-v2022-running-as-non-root created
         k8spspcapabilities.constraints.gatekeeper.sh/pss-restricted-v2022-capabilities created
         k8spspseccomp.constraints.gatekeeper.sh/pss-restricted-v2022-seccomp created
         k8spspvolumetypes.constraints.gatekeeper.sh/pss-restricted-v2022-psp-volume-types created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pss-restricted-v2022
         

The output is similar to the following:
         
         NAME                                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/pss-restricted-v2022-privilege-escalation   dryrun               0
         
         NAME                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowedusers.constraints.gatekeeper.sh/pss-restricted-v2022-running-as-non-root   dryrun               0
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/pss-restricted-v2022-capabilities   dryrun               0
         
         NAME                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/pss-restricted-v2022-seccomp   dryrun               0
         
         NAME                                                                                ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspvolumetypes.constraints.gatekeeper.sh/pss-restricted-v2022-psp-volume-types   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the Pod Security Standards (PSS) Restricted v2022 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pss-restricted-v2022
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval pss-restricted-v2022 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd pss-restricted-v2022
         kpt live init
         

  5. Apply the policy constraints with kpt:
         
         kpt live apply
         

  6. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kpt live status --output table --poll-until current
         

A status of `CURRENT` confirms successful installation of the constraints.




###  Config Sync 

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.



Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Change into the sync directory for Config Sync:
         
         cd SYNC_ROOT_DIR
         

**Note:** Kpt v1.0.0-beta.17 and later automatically create a `resourcegroup.yaml` file during `live init` which shouldn't be checked into your Config Sync repo. If not already present, add `resourcegroup.yaml` to your repo's `.gitignore` file.

To create or append `.gitignore` with `resourcegroup.yaml`: 
         
         echo resourcegroup.yaml >> .gitignore
         

  2. Create a dedicated `policies` directory:
         
         mkdir -p policies
         

  3. Download the Pod Security Standards (PSS) Restricted v2022 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pss-restricted-v2022 policies/pss-restricted-v2022
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/pss-restricted-v2022 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/pss-restricted-v2022
         kpt live apply --dry-run policies/pss-restricted-v2022
         

  6. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/pss-baseline-v2022` to your root `kustomization.yaml`. Otherwise remove the `policies/pss-baseline-v2022/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/pss-baseline-v2022/kustomization.yaml
         

  7. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/pss-restricted-v2022
         git commit -m 'Adding Pod Security Standards Restricted audit enforcement'
         git push
         

  8. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=pss-restricted-v2022 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=pss-restricted-v2022 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change Pod Security Standards Restricted policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=pss-restricted-v2022 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=pss-restricted-v2022
         




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
         
         kpt fn eval policies/pss-restricted-v2022 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/pss-restricted-v2022
         git commit -m 'Adding Pod Security Standards Restricted policy bundle warn enforcement'
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
    
    
    Warning: [pss-baseline-v2022-host-ports] The specified hostNetwork and hostPort are not allowed, pod: wp-non-compliant. Allowed values: {"max": 0, "min": 0}
    pod/wp-non-compliant created
    

## Remove Pod Security Standards Restricted policy bundle

If needed, the Pod Security Standards Restricted policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=pss-restricted-v2022
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repo:
         
         git rm -r SYNC_ROOT_DIR/policies/pss-restricted-v2022
         git commit -m 'Removing Pod Security Standards Restricted policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
