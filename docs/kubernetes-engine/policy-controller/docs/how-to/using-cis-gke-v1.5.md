---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-gke-v1.5
title: Use CIS Google Kubernetes Engine Benchmark v1.5.0 policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:49.428172+00:00
---

# Use CIS Google Kubernetes Engine Benchmark v1.5.0 policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-cis-gke-v1.5

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use CIS Google Kubernetes Engine Benchmark v1.5.0 policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [Center for Internet Security (CIS) GKE v1.5.0 policy bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/cis-gke-v1.5.0) to help audit the compliance of your GKE on Google Cloud cluster against the [CIS Google Kubernetes Engine (GKE) Benchmarks v1.5.0](https://www.cisecurity.org/benchmark/kubernetes). This benchmark is a set of recommended security controls for configuring GKE.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This bundle of constraints includes controls in the following domains:

  * RBAC and service accounts
  * Pod Security Policies
  * Network policies and CNI
  * Secrets management
  * Extensible Admission Control
  * General policies
  * Managed Services

**Note:** This bundle has not been certified by CIS.

## CIS GKE v1.5.0 policy bundle constraints

Constraint Name  | Constraint Description  | Control IDs   
---|---|---  
cis-gke-v1.5.0-apparmor  | Restricts the `AppArmor` profile for Pods.  | 4.2.1   
cis-gke-v1.5.0-restrict-creation-with-default-serviceaccount  | Restrict resource creation using a default `ServiceAccount`.  | 4.1.5   
cis-gke-v1.5.0-restrict-loadbalancer  | Disallows all services with type `LoadBalancer`.  | 5.6.8   
cis-gke-v1.5.0-restrict-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | 4.4.2   
cis-gke-v1.5.0-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | 4.5.1, 5.10.4   
cis-gke-v1.5.0-require-cos-node-image  | Requires Container-Optimized OS as the node OS image.  | 5.5.1   
cis-gke-v1.5.0-require-gke-metadata-server-enabled  | Requires the GKE Metadata Service is enabled on each node in the cluster.  | 5.4.2   
cis-gke-v1.5.0-require-ingress.class-gce  | Requires that all `Ingress` objects have a `kubernetes.io/ingress.class: gce` annotation.  | 5.6.8   
cis-gke-v1.5.0-require-managed-certificates  | Requires that all `Ingress` objects have a `networking.gke.io/managed-certificates` annotation.  | 5.6.8   
cis-gke-v1.5.0-require-namespace-networkpolicy  | Requires that every `Namespace` defined in the cluster has a `NetworkPolicy`.  | 4.3.2   
cis-gke-v1.5.0-require-seccomp-default  | Containers cannot run with a `seccomp` profile other than `runtime/default`.  | 4.6.2   
cis-gke-v1.5.0-require-securitycontext  | Requires that pods define `securityContext`.  | 4.6.3   
cis-gke-v1.5.0-capabilities  | Adding capabilities beyond those listed is not allowed.  | 4.2.1   
cis-gke-v1.5.0-restrict-cluster-admin-role  | Restricts the use of the `cluster-admin` role.  | 4.1.1   
cis-gke-v1.5.0-restrict-default-namespace  | Restricts pods from using the default `Namespace`.  | 4.6.1, 4.6.4   
cis-gke-v1.5.0-restrict-env-var-secrets  | Restricts the use of secrets as environment variables in container definitions.  | 4.4.1   
cis-gke-v1.5.0-host-namespace  | Restricts containers with `hostPID` or `hostIPC` set to true.  | 4.2.1   
cis-gke-v1.5.0-restrict-pods-create  | Restricts the creation of pods in `Roles` and `ClusterRoles`.  | 4.1.4   
cis-gke-v1.5.0-restrict-privileged-containers  | Restricts containers with `securityContext.privileged` set to true.  | 4.2.1   
cis-gke-v1.5.0-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.  | 5.8.2   
cis-gke-v1.5.0-restrict-role-wildcards  | Restricts the use of wildcards in `Roles` and `ClusterRoles`.  | 4.1.3   
cis-gke-v1.5.0-restrict-role-secrets  | Restricts the use of secrets in `Roles` and `ClusterRoles`.  | 4.1.2   
cis-gke-v1.5.0-restrict-automountserviceaccounttoken  | Restricts the use of service account tokens for pods.  | 4.1.5, 4.1.6   
cis-gke-v1.5.0-selinux  | Cannot set the SELinux type or set a custom SELinux user or role option.  | 4.2.1   
cis-gke-v1.5.0-host-port  | `HostPorts` should be disallowed.  | 4.2.1   
cis-gke-v1.5.0-hostpath-volumes  | `HostPath` volumes must be forbidden.  | 4.2.1   
cis-gke-v1.5.0-hostprocess  | Containers and pods cannot run with `securityContext.windowsOptions.hostProcess` set to `true`.  | 4.2.1   
cis-gke-v1.5.0-proc-mount-type  | Containers cannot run with a `procMount` set to a value other than `Default`.  | 4.2.1   
cis-gke-v1.5.0-restrict-bind-escalate-impersonate  | Restricts the access to the bind, escalate, impersonate on roles/clusterroles in `Roles` and `ClusterRoles`.  | 4.1.8   
cis-gke-v1.5.0-restrict-certificatesigningrequests-approval  | The approval of the client certificates is restricted.  | 4.1.11   
cis-gke-v1.5.0-restrict-nodes-proxy  | Restricts the access to the proxy sub-resource of nodes in `Roles` and `ClusterRoles`.  | 4.1.10   
cis-gke-v1.5.0-restrict-persistent-volume  | Restricts the creation of `persistentvolumes` in `Roles` and `ClusterRoles`.  | 4.1.9   
cis-gke-v1.5.0-restrict-serviceaccounts-token  | Restricts the creation of serviceaccount tokens in `Roles` and `ClusterRoles`.  | 4.1.13   
cis-gke-v1.5.0-restrict-system-masters-group  | Disallows the use of `system:masters` group.  | 5.1.7   
cis-gke-v1.5.0-restrict-system-masters-group  | Restricts the access to webhook configuration objects in `Roles` and `ClusterRoles`.  | 4.1.12   
cis-gke-v1.5.0-seccomp  | Seccomp profile must not be set to `Unconfined`.  | 4.2.1   
cis-gke-v1.5.0-sysctls  | Containers can set only sysctls listed in the `allowedSysctls` field.  | 4.2.1   
cis-gke-v1.5.0-host-namespaces-hostnetwork  | Host namespaces `hostNetwork` can only be `false`.  | 4.2.1   
  
## Before you begin

**Caution:** This policy bundle is intended for use only with [GKE on Google Cloud](https://docs.cloud.google.com/anthos/docs/concepts/gke-shared-responsibility#gke-on-google-cloud). For other GKE clusters, the [CIS Kubernetes Benchmarks](https://docs.cloud.google.com/anthos-config-management/docs/how-to/using-cis-k8s-benchmark) policy bundle is recommended.

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) v1.16.2 or higher on your cluster with the default library of constraint templates. You must also [enable support for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential), as this bundle contains referential constraints.



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

  1. Enablement and configuration of [Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac) is required in `cis-gke-v1.5.0-restrict-rbac-subjects`.
  2. Enablement and configuration of [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) is required in `cis-gke-v1.5.0-require-binauthz`.



## Audit policies

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the CIS GKE v1.5.0 policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal and address violations.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-gke-v1.5.0
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-gke-v1.5.0
         

The output is the following:
         
         k8savoiduseofsystemmastersgroup.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-system-masters-group created
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-creation-with-default-serviceaccount created
         k8sblockloadbalancer.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-loadbalancer created
         k8sblockobjectsoftype.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-secrets-of-type-basic-auth created
         k8snoenvvarsecrets.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-env-var-secrets created
         k8spspapparmor.constraints.gatekeeper.sh/cis-gke-v1.5.0-apparmor created
         k8spspcapabilities.constraints.gatekeeper.sh/cis-gke-v1.5.0-capabilities created
         k8spspforbiddensysctls.constraints.gatekeeper.sh/cis-gke-v1.5.0-sysctls created
         k8spsphostfilesystem.constraints.gatekeeper.sh/cis-gke-v1.5.0-hostpath-volumes created
         k8spsphostnamespace.constraints.gatekeeper.sh/cis-gke-v1.5.0-host-namespace created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/cis-gke-v1.5.0-host-port created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/cis-gke-v1.5.0-privileged-containers created
         k8spspprocmount.constraints.gatekeeper.sh/cis-gke-v1.5.0-proc-mount-type created
         k8spspselinuxv2.constraints.gatekeeper.sh/cis-gke-v1.5.0-selinux created
         k8spspseccomp.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-seccomp-default created
         k8spspseccomp.constraints.gatekeeper.sh/cis-gke-v1.5.0-seccomp created
         k8spspwindowshostprocess.constraints.gatekeeper.sh/cis-gke-v1.5.0-hostprocess created
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-securitycontext created
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-role-wildcards created
         k8srequirebinauthz.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-binauthz created
         k8srequirecosnodeimage.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-cos-node-image created
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-namespace-networkpolicy created
         k8srequiredannotations.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-ingress.class-gce created
         k8srequiredannotations.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-managed-certificates created
         k8srequiredlabels.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-gke-metadata-server-enabled created
         k8srestrictautomountserviceaccounttokens.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-automountserviceaccounttoken created
         k8srestrictnamespaces.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-default-namespace created
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-rbac-subjects created
         k8srestrictrolebindings.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-cluster-admin-role created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-bind-escalate-impersonate created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-certificatesigningrequests-approval created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-nodes-proxy created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-persistent-volume created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-pods-create created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-role-secrets created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-serviceaccounts-token created
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-webhook-config created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cis-gke-v1.5.0
         

The output is similar to the following:
         
         NAME                                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8savoiduseofsystemmastersgroup.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-system-masters-group   dryrun               0
         
         NAME                                                                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-creation-with-default-serviceaccount   dryrun               0
         
         NAME                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockloadbalancer.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-loadbalancer   dryrun               0
         
         NAME                                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockobjectsoftype.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-secrets-of-type-basic-auth   dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8snoenvvarsecrets.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-env-var-secrets   dryrun               0
         
         NAME                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-securitycontext   dryrun               0
         
         NAME                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-role-wildcards   dryrun               0
         
         NAME                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspapparmor.constraints.gatekeeper.sh/cis-gke-v1.5.0-apparmor   dryrun               0
         
         NAME                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/cis-gke-v1.5.0-capabilities   dryrun               0
         
         NAME                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspforbiddensysctls.constraints.gatekeeper.sh/cis-gke-v1.5.0-sysctls   dryrun               0
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostfilesystem.constraints.gatekeeper.sh/cis-gke-v1.5.0-hostpath-volumes   dryrun               0
         
         NAME                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnamespace.constraints.gatekeeper.sh/cis-gke-v1.5.0-host-namespace   dryrun               0
         
         NAME                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnetworkingports.constraints.gatekeeper.sh/cis-gke-v1.5.0-host-port   dryrun               0
         
         NAME                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/cis-gke-v1.5.0-privileged-containers   dryrun               0
         
         NAME                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprocmount.constraints.gatekeeper.sh/cis-gke-v1.5.0-proc-mount-type   dryrun               0
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-seccomp-default   dryrun               0
         k8spspseccomp.constraints.gatekeeper.sh/cis-gke-v1.5.0-seccomp                   dryrun               0
         
         NAME                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspselinuxv2.constraints.gatekeeper.sh/cis-gke-v1.5.0-selinux   dryrun               0
         
         NAME                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspwindowshostprocess.constraints.gatekeeper.sh/cis-gke-v1.5.0-hostprocess   dryrun               0
         
         NAME                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirebinauthz.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-binauthz   dryrun               0
         
         NAME                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirecosnodeimage.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-cos-node-image   dryrun               0
         
         NAME                                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredannotations.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-ingress.class-gce      dryrun               0
         k8srequiredannotations.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-managed-certificates   dryrun               0
         
         NAME                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-gke-metadata-server-enabled   dryrun               0
         
         NAME                                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/cis-gke-v1.5.0-require-namespace-networkpolicy   dryrun               0
         
         NAME                                                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictautomountserviceaccounttokens.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-automountserviceaccounttoken   dryrun               0
         
         NAME                                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictnamespaces.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-default-namespace   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-rbac-subjects   dryrun               0
         
         NAME                                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-cluster-admin-role   dryrun               0
         
         NAME                                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-bind-escalate-impersonate             dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-certificatesigningrequests-approval   dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-nodes-proxy                           dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-persistent-volume                     dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-pods-create                           dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-role-secrets                          dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-serviceaccounts-token                 dryrun               0
         k8srestrictrolerules.constraints.gatekeeper.sh/cis-gke-v1.5.0-restrict-webhook-config                        dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the CIS policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-gke-v1.5.0
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval cis-gke-v1.5.0 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd cis-gke-v1.5.0
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
         

  3. Download the CIS GKE v1.5.0 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/cis-gke-v1.5.0 policies/cis-gke-v1.5.0
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/cis-gke-v1.5.0 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/cis-gke-v1.5.0
         kpt live apply --dry-run policies/cis-gke-v1.5.0
         

  6. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/cis-gke-v1.5.0` to your root `kustomization.yaml`. Otherwise remove the `policies/cis-gke-v1.5.0/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/cis-gke-v1.5.0/kustomization.yaml
         

  7. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/cis-gke-v1.5.0
         git commit -m 'Adding CIS GKE v1.5.0 policy bundle'
         git push
         

  8. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=cis-gke-v1.5.0 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=cis-gke-v1.5.0 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change CIS GKE v1.5.0 policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=cis-gke-v1.5.0 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=cis-gke-v1.5.0
         




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
         
         kpt fn eval policies/cis-gke-v1.5.0 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/cis-gke-v1.5.0
         git commit -m 'Adding CIS GKE v1.5.0 policy bundle warn enforcement'
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
    
    
    Warning: [cis-gke-v1.5.0-restrict-default-namespace] <default> namespace is restricted
    Warning: [cis-gke-v1.5.0-require-seccomp-default] Seccomp profile 'not configured' is not allowed for container 'wordpress'. Found at: no explicit profile found. Allowed profiles: {"RuntimeDefault", "runtime/default"}
    Warning: [cis-gke-v1.5.0-require-securitycontext] securityContext must be defined for all Pod containers
    pod/wp-non-compliant configured
    

## Remove CIS GKE v1.5.0 policy bundle

If needed, the CIS GKE v1.5.0 policy bundle can be removed from the cluster.

### kubectl

Use kubectl to remove the policies:
    
    
      kubectl delete constraint -l policycontroller.gke.io/bundleName=cis-gke-v1.5.0
      

### kpt

Remove the policies:
    
    
      kpt live destroy
      

###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repository:
         
         git rm -r SYNC_ROOT_DIR/policies/cis-gke-v1.5.0
         git commit -m 'Removing CIS GKE v1.5.0 policy bundle'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


