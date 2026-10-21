---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-mitre-v2024/
title: Use MITRE policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:50.033227+00:00
---

# Use MITRE policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-mitre-v2024/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use MITRE policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [MITRE policy bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/mitre-v2024) to evaluate the compliance of your cluster resources against some aspects of the MITRE knowledge base of adversary tactics and techniques based on real-world observations.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

## MITRE policy bundle constraints

Constraint Name | Constraint Description  
---|---  
mitre-v2024-apparmor  | Restricts the `AppArmor` profile for Pods.   
mitre-v2024-block-all-ingress  | Restricts the creation of Ingress objects.   
mitre-v2024-cronjob-restrict-repos  | Restricts container images for `CronJob` to an allowed `repos` list.   
mitre-v2024-no-anonymous  | Disallows associating `ClusterRole` and `Role` resources to the `system:anonymous` user and `system:unauthenticated` group.   
mitre-v2024-host-namespaces-host-pid-ipc  | Containers cannot run with `hostPID` or `hostIPC` set to `true`.   
mitre-v2024-host-namespaces-hostnetwork  | Containers cannot run with `hostNetwork` set to `true`.   
mitre-v2024-host-ports  | `HostPorts` should be disallowed, or at minimum restricted to a known list.   
mitre-v2024-no-secrets-as-env-vars  | Restricts the use of secrets as environment variables in container definitions.   
mitre-v2024-privileged-containers  | Restricts containers with `securityContext.privileged` set to `true`.   
mitre-v2024-proc-mount-type  | The default `/proc` masks reduce attack surface, and are required.   
mitre-v2024-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.   
mitre-v2024-require-namespace-networkpolicy  | Requires that every namespace defined in the cluster has a NetworkPolicy.   
mitre-v2024-restrict-admission-controller  | Restricts the use of dynamic admission controllers and webhooks.   
mitre-v2024-restrict-automountserviceaccounttoken  | Restricts the use of service accounts tokens.   
mitre-v2024-restrict-capabilities  | Adding capabilities beyond those listed is not allowed.   
mitre-v2024-restrict-cluster-admin-role  | Restricts the use of the `cluster-admin` role.   
mitre-v2024-restrict-hostpath-volumes  | Restricts the use of `HostPath` volumes.   
mitre-v2024-restrict-kubernetes-dashboard-namespace  | Restricts the use of the `kubernetes-dashboard` namespace.   
mitre-v2024-restrict-pods-exec  | Restricts the use of `pods/exec` in `Roles` and `ClusterRoles`.   
mitre-v2024-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.   
mitre-v2024-restrict-repos  | Restricts container images to an allowed `repos` list.   
mitre-v2024-restrict-role-secrets  | Restricts the use of secrets in `Roles` and `ClusterRoles`.   
mitre-v2024-restrict-windows-hostprocess  | Restricts running of Windows HostProcess containers / pods   
mitre-v2024-seccomp  | Seccomp profile must not be set to `Unconfined`.   
mitre-v2024-selinux  | Cannot set the SELinux type or set a custom SELinux user or role option.   
mitre-v2024-sysctls  | Containers can set only sysctls listed in the `allowedSysctls` field.   
  
## Before you begin

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) v1.17.2 or higher on your cluster with the default library of constraint templates. You must also [enable support for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential) as this bundle contains referential constraints.



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
               - group: "admissionregistration.k8s.io"
                 version: "v1"
                 kind: "ValidatingWebhookConfiguration"
         

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




## Audit MITRE policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the MITRE policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/mitre-v2024
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/mitre-v2024
         

The output is the following:
         
         k8sallowedrepos.constraints.gatekeeper.sh/mitre-v2024-restrict-repos created
         k8sblockallingress.constraints.gatekeeper.sh/mitre-v2024-block-all-ingress created
         k8scronjoballowedrepos.constraints.gatekeeper.sh/mitre-v2024-cronjob-restrict-repos created
         k8sdisallowanonymous.constraints.gatekeeper.sh/mitre-v2024-no-anonymous created
         k8snoenvvarsecrets.constraints.gatekeeper.sh/mitre-v2024-no-secrets-as-env-vars created
         k8spspapparmor.constraints.gatekeeper.sh/mitre-v2024-apparmor created
         k8spspcapabilities.constraints.gatekeeper.sh/mitre-v2024-restrict-capabilities created
         k8spspforbiddensysctls.constraints.gatekeeper.sh/mitre-v2024-sysctls created
         k8spsphostfilesystem.constraints.gatekeeper.sh/mitre-v2024-restrict-hostpath-volumes created
         k8spsphostnamespace.constraints.gatekeeper.sh/mitre-v2024-host-namespaces-host-pid-ipc created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/mitre-v2024-host-namespaces-hostnetwork created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/mitre-v2024-host-ports created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/mitre-v2024-privileged-containers created
         k8spspprocmount.constraints.gatekeeper.sh/mitre-v2024-proc-mount-type created
         k8spspselinuxv2.constraints.gatekeeper.sh/mitre-v2024-selinux created
         k8spspseccomp.constraints.gatekeeper.sh/mitre-v2024-seccomp created
         k8spspwindowshostprocess.constraints.gatekeeper.sh/mitre-v2024-restrict-windows-hostprocess created
         k8srequirebinauthz.constraints.gatekeeper.sh/mitre-v2024-require-binauthz created
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/mitre-v2024-require-namespace-networkpolicy created
         k8srestrictadmissioncontroller.constraints.gatekeeper.sh/mitre-v2024-restrict-admission-controller created
         k8srestrictautomountserviceaccounttokens.constraints.gatekeeper.sh/mitre-v2024-restrict-automountserviceaccounttoken created
         k8srestrictnamespaces.constraints.gatekeeper.sh/mitre-v2024-restrict-kubernetes-dashboard-namespace created
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/mitre-v2024-restrict-rbac-subjects created
         k8srestrictrolebindings.constraints.gatekeeper.sh/mitre-v2024-restrict-cluster-admin-role created
         k8srestrictrolerules.constraints.gatekeeper.sh/mitre-v2024-restrict-pods-exec created
         k8srestrictrolerules.constraints.gatekeeper.sh/mitre-v2024-restrict-role-secrets created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=mitre-v2024
         

The output is similar to the following:
         
         NAME                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sallowedrepos.constraints.gatekeeper.sh/mitre-v2024-restrict-repos   dryrun               0
         
         NAME                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockallingress.constraints.gatekeeper.sh/mitre-v2024-block-all-ingress   dryrun               0
         
         NAME                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8scronjoballowedrepos.constraints.gatekeeper.sh/mitre-v2024-cronjob-restrict-repos   dryrun               0
         
         NAME                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sdisallowanonymous.constraints.gatekeeper.sh/mitre-v2024-no-anonymous   dryrun               0
         
         NAME                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8snoenvvarsecrets.constraints.gatekeeper.sh/mitre-v2024-no-secrets-as-env-vars   dryrun               0
         
         NAME                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspapparmor.constraints.gatekeeper.sh/mitre-v2024-apparmor   dryrun               0
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/mitre-v2024-restrict-capabilities   dryrun               0
         
         NAME                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspforbiddensysctls.constraints.gatekeeper.sh/mitre-v2024-sysctls   dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostfilesystem.constraints.gatekeeper.sh/mitre-v2024-restrict-hostpath-volumes   dryrun               0
         
         NAME                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnamespace.constraints.gatekeeper.sh/mitre-v2024-host-namespaces-host-pid-ipc   dryrun               0
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnetworkingports.constraints.gatekeeper.sh/mitre-v2024-host-namespaces-hostnetwork   dryrun               0
         k8spsphostnetworkingports.constraints.gatekeeper.sh/mitre-v2024-host-ports                    dryrun               0
         
         NAME                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/mitre-v2024-privileged-containers   dryrun               0
         
         NAME                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprocmount.constraints.gatekeeper.sh/mitre-v2024-proc-mount-type   dryrun               0
         
         NAME                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/mitre-v2024-seccomp   dryrun               0
         
         NAME                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspselinuxv2.constraints.gatekeeper.sh/mitre-v2024-selinux   dryrun               0
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspwindowshostprocess.constraints.gatekeeper.sh/mitre-v2024-restrict-windows-hostprocess   dryrun               0
         
         NAME                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirebinauthz.constraints.gatekeeper.sh/mitre-v2024-require-binauthz   dryrun               0
         
         NAME                                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/mitre-v2024-require-namespace-networkpolicy   dryrun               0
         
         NAME                                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictadmissioncontroller.constraints.gatekeeper.sh/mitre-v2024-restrict-admission-controller   dryrun               0
         
         NAME                                                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictautomountserviceaccounttokens.constraints.gatekeeper.sh/mitre-v2024-restrict-automountserviceaccounttoken   dryrun               0
         
         NAME                                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictnamespaces.constraints.gatekeeper.sh/mitre-v2024-restrict-kubernetes-dashboard-namespace   dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/mitre-v2024-restrict-rbac-subjects   dryrun               0
         
         NAME                                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/mitre-v2024-restrict-cluster-admin-role   dryrun               0
         
         NAME                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolerules.constraints.gatekeeper.sh/mitre-v2024-restrict-pods-exec      dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/mitre-v2024-restrict-role-secrets   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the MITRE policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/mitre-v2024
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval mitre-v2024 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd mitre-v2024
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
         

**Note:** Kpt v1.0.0-beta.17 and later automatically create a `resourcegroup.yaml` file during `live init` which shouldn't be checked into your Config Sync repository. If not already present, add `resourcegroup.yaml` to your repo's `.gitignore` file.

To create or append `.gitignore` with `resourcegroup.yaml`: 
         
         echo resourcegroup.yaml >> .gitignore
         

  2. Create a dedicated `policies` directory:
         
         mkdir -p policies
         

  3. Download the MITRE policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/mitre-v2024 policies/mitre-v2024
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/mitre-v2024 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/mitre-v2024
         kpt live apply --dry-run policies/mitre-v2024
         

  6. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/mitre-v2024` to your root `kustomization.yaml`. Otherwise remove the `policies/mitre-v2024/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/mitre-v2024/kustomization.yaml
         

  7. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/mitre-v2024
         git commit -m 'Adding MITRE policy audit enforcement'
         git push
         

  8. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=mitre-v2024 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=mitre-v2024 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change MITRE policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=mitre-v2024 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=mitre-v2024
         




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
         
         kpt fn eval policies/mitre-v2024 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/mitre-v2024
         git commit -m 'Adding MITRE policy bundle warn enforcement'
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
    
    
    Warning: [mitre-v2024-restrict-repos] container <wordpress> has an invalid image repo <wordpress>, allowed repos are ["gcr.io/gke-release/", "gcr.io/anthos-baremetal-release/", "gcr.io/gke-on-prem-release/", "gcr.io/gke-multi-cloud-release/", "gcr.io/config-management-release/", "gcr.io/kubebuilder/", "gcr.io/gkeconnect/", "gke.gcr.io/"]
    pod/wp-non-compliant created
    

## Remove MITRE policy bundle

If needed, the MITRE policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=mitre-v2024
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repository:
         
         git rm -r SYNC_ROOT_DIR/policies/mitre-v2024
         git commit -m 'Removing MITRE policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
