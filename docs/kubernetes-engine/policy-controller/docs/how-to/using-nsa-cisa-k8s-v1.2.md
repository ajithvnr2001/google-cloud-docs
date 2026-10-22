---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nsa-cisa-k8s-v1.2
title: Use NSA CISA Kubernetes Hardening policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:37.265503+00:00
---

# Use NSA CISA Kubernetes Hardening policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nsa-cisa-k8s-v1.2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use NSA CISA Kubernetes Hardening policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [National Security Agency (NSA) Cybersecurity and Infrastructure Security Agency (CISA) Kubernetes Hardening Guide v1.2 Policy bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/nsa-cisa-k8s-v1.2) to evaluate the compliance of your cluster resources against some aspects of the [NSA CISA Kubernetes Hardening Guide v1.2](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF).

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## NSA CISA Kubernetes Hardening v1.2 policy bundle constraints

**Constraint Name** | **Constraint Description** | nsa-cisa-k8s-v1.2-apparmor  | Restricts `AppArmor` profile for Pods.   
---|---  
nsa-cisa-k8s-v1.2-automount-serviceaccount-token-pod  | Restricts Pods from using `automountServiceAccountToken`.   
nsa-cisa-k8s-v1.2-block-all-ingress  | Restricts the creation of `Ingress` objects.   
nsa-cisa-k8s-v1.2-block-secrets-of-type-basic-auth  | Restricts the use of `kubernetes.io/basic-auth` type secrets.   
nsa-cisa-k8s-v1.2-capabilities  | Containers must drop all capabilities, and are not permitted to add back any capabilities.   
nsa-cisa-k8s-v1.2-cpu-and-memory-limits-required  | All workload pods must specify `cpu` and `memory` limits.   
nsa-cisa-k8s-v1.2-host-namespaces  | Restricts containers with `hostPID` or `hostIPC` set to `true`.   
nsa-cisa-k8s-v1.2-host-namespaces-hostnetwork  | Sharing the host namespaces must be disallowed.   
nsa-cisa-k8s-v1.2-host-network  | Restricts containers from running with the `hostNetwork` flag set to `true`.   
nsa-cisa-k8s-v1.2-hostport  | Restricts containers from running with `hostPort` configured.   
nsa-cisa-k8s-v1.2-privilege-escalation  | Restricts containers with `allowPrivilegeEscalation` set to `true`.   
nsa-cisa-k8s-v1.2-privileged-containers  | Restricts containers with `securityContext.privileged` set to `true`.   
nsa-cisa-k8s-v1.2-readonlyrootfilesystem  | Requires the use of a read-only root file system by pod containers.   
nsa-cisa-k8s-v1.2-require-namespace-network-policies  | Requires that every namespace defined in the cluster has a `NetworkPolicy`.   
nsa-cisa-k8s-v1.2-restrict-clusteradmin-rolebindings  | Restricts the use of the `cluster-admin` role.   
nsa-cisa-k8s-v1.2-restrict-edit-rolebindings  | Restricts the use of the `edit` role.   
nsa-cisa-k8s-v1.2-restrict-hostpath-volumes  | Restricts the use of `HostPath` volumes.   
nsa-cisa-k8s-v1.2-restrict-pods-exec  | Restricts the use of `pods/exec` in `Roles` and `ClusterRoles`.   
nsa-cisa-k8s-v1.2-running-as-non-root  | Restricts containers from running as the root user.   
nsa-cisa-k8s-v1.2-seccomp  | Seccomp profile must not be explicitly set to `Unconfined`.   
nsa-cisa-k8s-v1.2-selinux  | Cannot set the SELinux type or set a custom SELinux user or role option.   
  
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
               - group: "networking.k8s.io"
                 version: "v1"
                 kind: "NetworkPolicy"
         

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




## Audit NSA CISA Kubernetes Hardening v1.2 policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the NSA CISA Kubernetes Hardening Guide v1.2 policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before optionally enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview) , or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) .

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nsa-cisa-k8s-v1.2
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nsa-cisa-k8s-v1.2
         

The output is the following:
         
         k8sblockallingress.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-block-all-ingress created
         k8sblockobjectsoftype.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-block-secrets-of-type-basic-auth created
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-privilege-escalation created
         k8spspallowedusers.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-running-as-non-root created
         k8spspapparmor.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-apparmor created
         k8spspautomountserviceaccounttokenpod.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-automount-serviceaccount-token-pod created
         k8spspcapabilities.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-capabilities created
         k8spsphostfilesystem.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-hostpath-volumes created
         k8spsphostnamespace.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-host-namespaces created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-host-network created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-hostport created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-privileged-containers created
         k8spspreadonlyrootfilesystem.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-readonlyrootfilesystem created
         k8spspselinuxv2.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-selinux created
         k8spspseccomp.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-seccomp created
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-require-namespace-network-policies created
         k8srequiredresources.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-cpu-and-memory-limits-required created
         k8srestrictrolebindings.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-clusteradmin-rolebindings created
         k8srestrictrolebindings.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-edit-rolebindings created
         k8srestrictrolerules.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-pods-exec created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=nsa-cisa-k8s-v1.2
         

The output is similar to the following:
         
         NAME                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockallingress.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-block-all-ingress   dryrun               0
         
         NAME                                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockobjectsoftype.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-block-secrets-of-type-basic-auth   dryrun               0
         
         NAME                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowedusers.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-running-as-non-root   dryrun               0
         
         NAME                                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-privilege-escalation   dryrun               0
         
         NAME                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspapparmor.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-apparmor   dryrun               0
         
         NAME                                                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspautomountserviceaccounttokenpod.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-automount-serviceaccount-token-pod   dryrun               0
         
         NAME                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-capabilities   dryrun               0
         
         NAME                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostfilesystem.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-hostpath-volumes   dryrun               0
         
         NAME                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnamespace.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-host-namespaces   dryrun               0
         
         NAME                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnetworkingports.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-host-network   dryrun               0
         k8spsphostnetworkingports.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-hostport       dryrun               0
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-privileged-containers   dryrun               0
         
         NAME                                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspreadonlyrootfilesystem.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-readonlyrootfilesystem   dryrun               0
         
         NAME                                                                ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-seccomp   dryrun               0
         
         NAME                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspselinuxv2.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-selinux   dryrun               0
         
         NAME                                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredresources.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-cpu-and-memory-limits-required   dryrun               0
         
         NAME                                                                                                                ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-require-namespace-network-policies   dryrun               0
         
         NAME                                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-clusteradmin-rolebindings   dryrun               0
         k8srestrictrolebindings.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-edit-rolebindings           dryrun               0
         
         NAME                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolerules.constraints.gatekeeper.sh/nsa-cisa-k8s-v1.2-restrict-pods-exec   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/).

kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the NSA CISA Kubernetes Hardening Guide v1.2 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nsa-cisa-k8s-v1.2
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval nsa-cisa-k8s-v1.2 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
         -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd nsa-cisa-k8s-v1.2 kpt live init
         

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
         

  4. Download the NSA CISA Kubernetes Hardening Guide v1.2 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nsa-cisa-k8s-v1.2 policies/nsa-cisa-k8s-v1.2
         

  5. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/nsa-cisa-k8s-v1.2 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  6. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/nsa-cisa-k8s-v1.2 kpt live apply --dry-run policies/nsa-cisa-k8s-v1.2
         

  7. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/nsa-cisa-k8s-v1.2` to your root `kustomization.yaml`. Otherwise remove the `policies/nsa-cisa-k8s-v1.2/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/nsa-cisa-k8s-v1.2/kustomization.yaml
         

  8. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/nsa-cisa-k8s-v1.2 git commit -m 'Adding NSA CISA Kubernetes Hardening v1.2 policy audit enforcement'
         git push
         

  9. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
      kubectl get constraint -l policycontroller.gke.io/bundleName=nsa-cisa-k8s-v1.2 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
      

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
      kubectl get constraint -l policycontroller.gke.io/bundleName=nsa-cisa-k8s-v1.2 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
      

## Change NSA CISA Kubernetes Hardening v1.2 policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=nsa-cisa-k8s-v1.2 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=nsa-cisa-k8s-v1.2
         




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
         
         kpt fn eval policies/nsa-cisa-k8s-v1.2 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/nsa-cisa-k8s-v1.2
         git commit -m 'Adding NSA CISA Kubernetes Hardening v1.2 policy warn enforcement'
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
            name: wordpress
    EOF
    

The admission controller should produce a warning listing out the policy violations that this resource violates, as shown in the following example:
    
    
    Warning: [nsa-cisa-k8s-v1.2-automount-serviceaccount-token-pod] Automounting service account token is disallowed, pod: wp-non-compliant
    Warning: [nsa-cisa-k8s-v1.2-running-as-non-root] Container wordpress is attempting to run without a required securityContext/runAsGroup. Allowed runAsGroup: {"ranges": [{"max": 65536, "min": 1000}], "rule": "MustRunAs"}
    Warning: [nsa-cisa-k8s-v1.2-running-as-non-root] Container wordpress is attempting to run without a required securityContext/runAsUser
    Warning: [nsa-cisa-k8s-v1.2-privilege-escalation] Privilege escalation container is not allowed: wordpress
    Warning: [nsa-cisa-k8s-v1.2-cpu-and-memory-limits-required] container <wordpress> does not have <{"cpu", "memory"}> limits defined
    Warning: [nsa-cisa-k8s-v1.2-capabilities] container <wordpress> is not dropping all required capabilities. Container must drop all of ["ALL"] or "ALL"
    Warning: [nsa-cisa-k8s-v1.2-readonlyrootfilesystem] only read-only root filesystem container is allowed: wordpress
    pod/wp-non-compliant created
    

## Remove NSA CISA Kubernetes Hardening v1.2 policy bundle

If needed, the NSA CISA Kubernetes Hardening v1.2 policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=nsa-cisa-k8s-v1.2
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repo:
         
         git rm -r SYNC_ROOT_DIR/policies/nsa-cisa-k8s-v1.2
         git commit -m 'Removing NSA CISA Kubernetes Hardening Guide v1.2 policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
