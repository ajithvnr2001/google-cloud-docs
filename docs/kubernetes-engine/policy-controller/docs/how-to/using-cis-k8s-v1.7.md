---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-v1.7
title: Use CIS Kubernetes Benchmark v1.7.1 policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:09:02.009841+00:00
---

# Use CIS Kubernetes Benchmark v1.7.1 policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-k8s-v1.7

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use CIS Kubernetes Benchmark v1.7.1 policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [CIS bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/cis-k8s-v1.7.1) to audit the compliance of your cluster against the [CIS Kubernetes Benchmark v1.7.1](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cis-benchmarks#cis_kubernetes_benchmark). This benchmark is a set of recommendations for configuring Kubernetes to support a strong security posture.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This bundle of constraints addresses and enforces policies in the following domains:

  * RBAC and service accounts
  * Pod Security Policies
  * Network policies and CNI
  * Secrets management
  * Extensible Admission Control
  * General policies

**Note:** This bundle has not been certified by CIS.

## CIS Kubernetes v1.7.1 policy bundle constraints

Constraint Name  | Constraint Description  | Control IDs   
---|---|---  
cis-k8s-v1.7.1-restrict-system-masters-group  | Disallows the use of `system:masters` group. Has no effect during audit.  | 5.1.7   
cis-k8s-v1.7.1-restrict-env-var-secrets  | Restricts the use of secrets as environment variables in container definitions.  | 5.4.1   
cis-k8s-v1.7.1-restrict-capabilities  | Containers must drop the `NET_RAW` capability and are not permitted to add back any capabilities.  | 5.2.8, 5.2.9, 5.2.10   
cis-k8s-v1.7.1-require-admission-controller  | Requires either Pod Security Admission or an external policy control system.  | 5.2.1   
cis-k8s-v1.7.1-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | 5.5.1   
cis-k8s-v1.7.1-require-namespace-networkpolicy  | Requires that every namespace defined in the cluster has a `NetworkPolicy`.  | 5.3.2   
cis-k8s-v1.7.1-require-seccomp-default  | Requires that Pods have seccomp profile set to `runtime/default` or `docker/default`.  | 5.7.2   
cis-k8s-v1.7.1-require-securitycontext  | Requires that Pods define `securityContext`.  | 5.7.3   
cis-k8s-v1.7.1-restrict-aggregation-controller  | Restricts the use of the `clusterrole-aggregation-controller` role.  | 5.1.8   
cis-k8s-v1.7.1-restrict-automountserviceaccounttoken  | Restricts the use of service accounts tokens.  | 5.1.5, 5.1.6   
cis-k8s-v1.7.1-restrict-bind-escalate-impersonate  | Restricts access to bind, escalate, impersonate in `Roles` and `ClusterRoles`.  | 5.1.8   
cis-k8s-v1.7.1-restrict-certificatesigningrequests-approval  | Restricts access to the client certificate approval API.  | 5.1.11   
cis-k8s-v1.7.1-restrict-cluster-admin-role  | Restricts the use of the `cluster-admin` role.  | 5.1.1, 5.1.8   
cis-k8s-v1.7.1-restrict-creation-with-default-serviceaccount  | Restricts the creation of resources using a default service account. Has no effect during audit.  | 5.1.5   
cis-k8s-v1.7.1-restrict-default-namespace  | Restricts pods from using the default namespace.  | 5.7.1, 5.7.4   
cis-k8s-v1.7.1-restrict-host-namespace  | Restricts containers with `hostPID` or `hostIPC` set to `true`.  | 5.2.3, 5.2.4   
cis-k8s-v1.7.1-restrict-host-port  | Restricts containers from running with `hostPort` configured.  | 5.2.13   
cis-k8s-v1.7.1-restrict-hostpath-volumes  | Restricts the use of `hostPath` volumes.  | 5.2.12   
cis-k8s-v1.7.1-restrict-hostnetwork  | Restricts containers from running with the `hostNetwork` flag set to `true`.  | 5.2.5   
cis-k8s-v1.7.1-restrict-nodes-proxy  | Restricts the access to the proxy sub-resource of nodes in `Roles` and `ClusterRoles`.  | 5.1.10   
cis-k8s-v1.7.1-restrict-persistent-volume  | Restricts the creation of `persistentvolumes` in `Roles` and `ClusterRoles`.  | 5.1.9   
cis-k8s-v1.7.1-restrict-pods-create  | Restricts the creation of pods in `Roles` and `ClusterRoles`.  | 5.1.4   
cis-k8s-v1.7.1-restrict-privilege-escalation  | Restricts containers with `allowPrivilegeEscalation` set to `true`.  | 5.2.6   
cis-k8s-v1.7.1-restrict-privileged-containers  | Restricts containers with `securityContext.privileged` set to `true`.  | 5.2.2   
cis-k8s-v1.7.1-restrict-role-secrets  | Restricts the use of secrets in `Roles` and `ClusterRoles`.  | 5.1.2   
cis-k8s-v1.7.1-restrict-role-wildcards  | Restricts the use of wildcards in `Roles` and `ClusterRoles`.  | 5.1.3   
cis-k8s-v1.7.1-restrict-root-containers  | Restricts containers from running as the root user.  | 5.2.7   
cis-k8s-v1.7.1-restrict-secrets-of-type-basic-auth  | Restricts the use of `basic-auth` type secrets.  | 5.4.2   
cis-k8s-v1.7.1-restrict-serviceaccounts-token  | Restricts the creation of serviceaccount tokens in `Roles` and `ClusterRoles`.  | 5.1.13   
cis-k8s-v1.7.1-restrict-webhook-config  | Restricts the access to webhook configuration objects in `Roles` and `ClusterRoles`.  | 5.1.12   
cis-k8s-v1.7.1-restrict-windows-hostprocess  | Restricts running of Windows `hostProcess` containers or pods.  | 5.2.11   
  
## Before you begin

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) on your cluster with the default library of constraint templates. You must also [enable support for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential), as this bundle contains referential constraints.



### Configure for referential constraints

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
               - group: "admissionregistration.k8s.io"
                 version: "v1"
                 kind: "ValidatingWebhookConfiguration"
               - group: "networking.k8s.io"
                 version: "v1"
                 kind: "NetworkPolicy"
         

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




### Configure your cluster and workload

  1. Enablement and configuration of [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) is required in `cis-k8s-v1.7.1-require-binauthz`.



## Audit CIS Kubernetes v1.7.1 policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the CIS Kubernetes v1.7.1 policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal and address violations.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/config-sync-overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-k8s-v1.7.1
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-k8s-v1.7.1
         

The output is the following:
         
         k8savoiduseofsystemmastersgroup.constraints.gatekeeper.sh/cis-k8s-v1.7.1-avoid-use-of-system-masters-group created
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-creation-with-default-serviceaccount created
         k8sblockobjectsoftype.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-secrets-of-type-basic-auth created
         k8snoenvvarsecrets.constraints.gatekeeper.sh/cis-k8s-v1.7.1-no-secrets-as-env-vars created
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-privilege-escalation created
         k8spspallowedusers.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-root-containers created
         k8spspcapabilities.constraints.gatekeeper.sh/cis-k8s-v1.7.1-psp-capabilities created
         k8spsphostfilesystem.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-hostpath-volumes created
         k8spsphostnamespace.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-host-namespace created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-host-port created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-hostnetwork created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-privileged-containers created
         k8spspseccomp.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-seccomp-default created
         k8spspwindowshostprocess.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-windows-hostprocess created
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-securitycontext created
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-role-wildcards created
         k8srequireadmissioncontroller.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-admission-controller created
         k8srequirebinauthz.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-binauthz created
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-namespace-networkpolicy created
         k8srestrictautomountserviceaccounttokens.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-automountserviceaccounttoken created
         k8srestrictnamespaces.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-default-namespace created
         k8srestrictrolebindings.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-aggregation-controller created
         k8srestrictrolebindings.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-cluster-admin-role created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-bind-escalate-impersonate created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-certificatesigningrequests-approval created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-nodes-proxy created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-persistent-volume created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-pods-create created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-role-secrets created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-serviceaccounts-token created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-webhook-config created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cis-k8s-v1.7.1
         

The output is similar to the following:
         
         NAME                                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-privilege-escalation   dryrun               0
         
         NAME                                                                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-creation-with-default-serviceaccount   dryrun               0
         
         NAME                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-role-wildcards   dryrun               0
         
         NAME                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirebinauthz.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-binauthz   dryrun               0
         
         NAME                                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequireadmissioncontroller.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-admission-controller   dryrun               0
         
         NAME                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspwindowshostprocess.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-windows-hostprocess   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnetworkingports.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-host-port     dryrun               0
         k8spsphostnetworkingports.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-hostnetwork   dryrun               0
         
         NAME                                                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictautomountserviceaccounttokens.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-automountserviceaccounttoken   dryrun               0
         
         NAME                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-securitycontext   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostfilesystem.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-hostpath-volumes   dryrun               0
         
         NAME                                                                                                ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-privileged-containers   dryrun               0
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-seccomp-default   dryrun               0
         
         NAME                                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-aggregation-controller   dryrun               0
         k8srestrictrolebindings.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-cluster-admin-role       dryrun               0
         
         NAME                                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-bind-escalate-impersonate             dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-certificatesigningrequests-approval   dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-nodes-proxy                           dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-persistent-volume                     dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-pods-create                           dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-role-secrets                          dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-serviceaccounts-token                 dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-webhook-config                        dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowedusers.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-root-containers   dryrun               0
         
         NAME                                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/cis-k8s-v1.7.1-require-namespace-networkpolicy   dryrun               0
         
         NAME                                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8savoiduseofsystemmastersgroup.constraints.gatekeeper.sh/cis-k8s-v1.7.1-avoid-use-of-system-masters-group   dryrun               0
         
         NAME                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8snoenvvarsecrets.constraints.gatekeeper.sh/cis-k8s-v1.7.1-no-secrets-as-env-vars   dryrun               0
         
         NAME                                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockobjectsoftype.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-secrets-of-type-basic-auth   dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnamespace.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-host-namespace   dryrun               0
         
         NAME                                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictnamespaces.constraints.gatekeeper.sh/cis-k8s-v1.7.1-restrict-default-namespace   dryrun               0
         
         NAME                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/cis-k8s-v1.7.1-psp-capabilities   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the CIS policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-k8s-v1.7.1
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval cis-k8s-v1.7.1 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd cis-k8s-v1.7.1
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
         

**Caution:** Kpt v1.0.0-beta.17 and later automatically create a `resourcegroup.yaml` file during `live init` which shouldn't be checked into your Config Sync repository. If not already present, add `resourcegroup.yaml` to your repository's `.gitignore` file.

To create or append `.gitignore` with `resourcegroup.yaml`: 
         
         echo resourcegroup.yaml >> .gitignore
         

  2. Create a dedicated `policies` directory:
         
         mkdir -p policies
         

  3. Download the CIS Kubernetes v1.7.1 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-k8s-v1.7.1 policies/cis-k8s-v1.7.1
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/cis-k8s-v1.7.1 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/cis-k8s-v1.7.1
         kpt live apply --dry-run policies/cis-k8s-v1.7.1
         

  6. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/cis-k8s-v1.7.1` to your root `kustomization.yaml`. Otherwise remove the `policies/cis-k8s-v1.7.1/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/cis-k8s-v1.7.1/kustomization.yaml
         

  7. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/cis-k8s-v1.7.1
         git commit -m 'Adding CIS Kubernetes v1.7.1 policy bundle'
         git push
         

  8. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=cis-k8s-v1.7.1 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=cis-k8s-v1.7.1 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change CIS Kubernetes v1.7.1 policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=cis-k8s-v1.7.1 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cis-k8s-v1.7.1
         




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
         
         kpt fn eval policies/cis-k8s-v1.7.1 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/cis-k8s-v1.7.1
         git commit -m 'Adding CIS Kubernetes v1.7.1 policy bundle warn enforcement'
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
    
    
    Warning: [cis-k8s-v1.7.1-restrict-default-namespace] <default> namespace is restricted
    Warning: [cis-k8s-v1.7.1-restrict-root-containers] Container wordpress is attempting to run without a required securityContext/runAsNonRoot or securityContext/runAsUser != 0
    Warning: [cis-k8s-v1.7.1-restrict-privilege-escalation] Privilege escalation container is not allowed: wordpress
    Warning: [cis-k8s-v1.7.1-require-seccomp-default] Seccomp profile 'not configured' is not allowed for container 'wordpress'. Found at: no explicit profile found. Allowed profiles: {"RuntimeDefault", "docker/default", "runtime/default"}
    Warning: [cis-k8s-v1.7.1-psp-capabilities] container <wordpress> is not dropping all required capabilities. Container must drop all of ["NET_RAW"] or "ALL"
    Warning: [cis-k8s-v1.7.1-require-securitycontext] securityContext must be defined for all Pod containers
    pod/wp-non-compliant created
    

## Remove CIS Kubernetes v1.7.1 policy bundle

If needed, the CIS Kubernetes v1.7.1 policy bundle can be removed from the cluster.

### kubectl

Use kubectl to remove the policies:
    
    
      kubectl delete constraint -l policycontroller.gke.io/bundleName=cis-k8s-v1.7.1
      

### kpt

Remove the policies:
    
    
      kpt live destroy
      

###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repository:
         
         git rm -r SYNC_ROOT_DIR/policies/cis-k8s-v1.7.1
         git commit -m 'Removing CIS Kubernetes v1.7.1 policy bundle'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
