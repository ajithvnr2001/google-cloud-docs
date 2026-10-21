---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nist-sp-800-53-r5/
title: Use NIST SP 800-53 Rev. 5 policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:50.317005+00:00
---

# Use NIST SP 800-53 Rev. 5 policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-nist-sp-800-53-r5/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use NIST SP 800-53 Rev. 5 policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [NIST SP 800-53 Rev. 5 bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/nist-sp-800-53-r5) which implements controls listed in [National Institute of Standards and Technology (NIST) Special Publication (SP) 800-53 Rev. 5](https://doi.org/10.6028/NIST.SP.800-53r5). The bundle may help organizations protect their systems and data from a variety of threats by implementing out-of-the-box security and privacy policies.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## NIST SP 800-53 Rev. 5 policy bundle constraints

Constraint Name  | Constraint Description  | Control ID   
---|---|---  
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | AC-16 Security and Privacy Attributes   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.  | AC-2 Account Management   
nist-sp-800-53-r5-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.  | AC-3 Access Enforcement   
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | AC-4 Information Flow Enforcement   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.   
nist-sp-800-53-r5-require-namespace-network-policies  | Requires that every namespace defined in the cluster has a NetworkPolicy.   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | AC-6 Least Privilege   
nist-sp-800-53-r5-restrict-clusteradmin-rolebindings  | Restricts the use of the `cluster-admin` role.   
nist-sp-800-53-r5-restrict-repos  | Restricts container images to an allowed `repos` list.   
nist-sp-800-53-r5-restrict-role-wildcards  | Restricts the use of wildcards in `Roles` and `ClusterRoles`.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | AU-10 Non-Repudiation   
nist-sp-800-53-r5-nodes-have-consistent-time  | Ensures consistent and correct time on Nodes by allowing only Container-Optimized OS (COS) or Ubuntu as the OS image.  | AU-8 Time Stamps   
nist-sp-800-53-r5-require-namespace-network-policies  | Requires that every namespace defined in the cluster has a NetworkPolicy.  | CA-9 Internal System Connections   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | CM-14 Signed Components   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | CM-2 Baseline Configuration   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-apparmor  | Restricts AppArmor profiles allowed for Pods.  | CM-3 Configuration Change Control   
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.   
nist-sp-800-53-r5-capabilities  | Restricts additional Capabilities allowed for Pods.   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.   
nist-sp-800-53-r5-host-namespaces  | Restricts containers with `hostPID` or `hostIPC` set to `true`.   
nist-sp-800-53-r5-host-network  | Restricts containers from running with the `hostNetwork` flag set to `true`.   
nist-sp-800-53-r5-privileged-containers  | Restricts containers with `securityContext.privileged` set to `true`.   
nist-sp-800-53-r5-proc-mount-type  | Requires the default `/proc` masks for Pods   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-restrict-volume-types  | Restricts the mountable volumes types to the allowed list.   
nist-sp-800-53-r5-seccomp  | Seccomp profile must not be explicitly set to `Unconfined`.   
nist-sp-800-53-r5-selinux  | Restricts the SELinux configuration for Pods.   
nist-sp-800-53-r5-sysctls  | Restricts the allowed Sysctls for Pods.   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | CM-4 Security Impact Analysis   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-restrict-clusteradmin-rolebindings  | Restricts the use of the `cluster-admin` role.   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | CM-5 Access Restrictions for Change   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-restrict-clusteradmin-rolebindings  | Restricts the use of the `cluster-admin` role.   
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | CM-6 Configuration Settings   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-restrict-volume-types  | Restricts the mountable volumes types to the allowed list.   
nist-sp-800-53-r5-apparmor  | Restricts AppArmor profiles allowed for Pods.  | CM-7 Least Functionality   
nist-sp-800-53-r5-capabilities  | Restricts additional Capabilities allowed for Pods.   
nist-sp-800-53-r5-host-namespaces  | Restricts containers with `hostPID` or `hostIPC` set to `true`.   
nist-sp-800-53-r5-host-network  | Restricts containers from running with the `hostNetwork` flag set to `true`.   
nist-sp-800-53-r5-privileged-containers  | Restricts containers with `securityContext.privileged` set to `true`.   
nist-sp-800-53-r5-proc-mount-type  | Requires the default `/proc` masks for Pods   
nist-sp-800-53-r5-restrict-clusteradmin-rolebindings  | Restricts the use of the `cluster-admin` role.   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-restrict-volume-types  | Restricts the mountable volumes types to the allowed list.   
nist-sp-800-53-r5-seccomp  | Seccomp profile must not be explicitly set to `Unconfined`.   
nist-sp-800-53-r5-selinux  | Restricts the SELinux configuration for Pods.   
nist-sp-800-53-r5-sysctls  | Restricts the allowed Sysctls for Pods.   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | CP-10 Information System Recovery and Reconstitution   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | CP-9 System Backup   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.  | IA-2 Identification and Authentication (Organizational Users)   
nist-sp-800-53-r5-block-creation-with-default-serviceaccount  | Restrict resource creation using a default service account.  | IA-4 Identifier Management   
nist-sp-800-53-r5-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | IA-5 Authenticator Management   
nist-sp-800-53-r5-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.   
nist-sp-800-53-r5-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.  | MA-4 Nonlocal Maintenance   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | PL-1 Policy and Procedures   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | RA-5 Vulnerability Scanning   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.  | SA-10 Developer Configuration Management   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | SA-11 Trusted Path   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | SA-3 System Development Life Cycle   
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | SA-8 Security and Privacy Engineering Principles   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-restrict-volume-types  | Restricts the mountable volumes types to the allowed list.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | SC-12 Cryptographic Key Establishment and Management   
nist-sp-800-53-r5-restrict-storageclass  | Restricts `StorageClass` to a list of `StorageClass` which encrypt by default.  | SC-28 Protection of Information at Rest   
nist-sp-800-53-r5-require-namespace-network-policies  | Requires that every namespace defined in the cluster has a NetworkPolicy.  | SC-4 Information in Shared Resources   
nist-sp-800-53-r5-cpu-and-memory-limits-required  | Requires Pods specify cpu and memory limits.  | SC-6 Resource Availability   
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | SC-7 Boundary Protection   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-require-namespace-network-policies  | Requires that every namespace defined in the cluster has a NetworkPolicy.   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-restrict-volume-types  | Restricts the mountable volumes types to the allowed list.   
nist-sp-800-53-r5-asm-peer-authn-strict-mtls  | Ensures PeerAuthentications cannot overwrite strict mTLS.  | SC-8 Transmission Confidentiality and Integrity   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | SI-12 Information Management and Retention   
nist-sp-800-53-r5-restrict-storageclass  | Restricts `StorageClass` to a list of `StorageClass` which encrypt by default.   
nist-sp-800-53-r5-require-av-daemonset  | Requires the presence of an Anti-Virus daemonset.  | SI-3 Malicious Code Protection   
nist-sp-800-53-r5-block-secrets-of-type-basic-auth  | Restricts the use of basic-auth type secrets.  | SI-7 Software, Firmware, and Information Integrity   
nist-sp-800-53-r5-enforce-config-management  | Requires Config Sync is running and Drift Prevention enabled with at least one `RootSync` object on the cluster.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.   
nist-sp-800-53-r5-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.   
nist-sp-800-53-r5-restrict-hostpath-volumes  | Restricts the use of HostPath volumes.   
nist-sp-800-53-r5-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | SR-4 Provenance   
  
## Before you begin

**Note:** If you tried the [Preview](https://cloud.google.com/products/#product-launch-stages) NIST 800 r5 Policy Bundle, remove that version before installing this bundle. For example, `kubectl delete constraints -l policycontroller.gke.io/bundleName=nist-800-r5`

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
               - group: "apps"
                 version: "v1"
                 kind: "DaemonSet"
               - group: "networking.k8s.io"
                 version: "v1"
                 kind: "NetworkPolicy"
               - group: "configsync.gke.io"
                 version: "v1beta1"
                 kind: "RootSync"
               - group: "storage.k8s.io"
                 version: "v1"
                 kind: "StorageClass"
               - group: "admissionregistration.k8s.io"
                 version: "v1"
                 kind: "ValidatingWebhookConfiguration"
         

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




### Configure your cluster and workload

  1. Enablement and configuration of [Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)including [Drift Prevention admission webhook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) is required in `nist-sp-800-53-r5-enforce-config-management`.
  2. An antivirus solution is required. The default is the presence of a `daemonset` named [`clamav`](https://docs.clamav.net/) in the `clamav` `namespace`, however the `daemonset`'s name and namespace can be customized to your implementation in the `nist-sp-800-53-r5-require-av-daemonset` constraint.
  3. Container images are limited to an allowed repos list, which can be customized if required in `nist-sp-800-53-r5-restrict-repos`.
  4. Nodes must use [Container-Optimized OS or Ubuntu](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) for their image in `nist-sp-800-53-r5-nodes-have-consistent-time`.
  5. Use of storage classes is limited to an allowed list, which can be customized to add additional classes with default encryption in `nist-sp-800-53-r5-restrict-storageclass`.
  6. Enablement and configuration of [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) is required in `nist-sp-800-53-r5-require-binauthz`.

**Note:** Binary Authorization is available for [ Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/binary-authorization/docs/setting-up), and in Preview for [GKE on GDC](https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem).



## Audit NIST SP 800-53 Rev. 5 policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the NIST SP 800-53 policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview) , or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) .

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nist-sp-800-53-r5
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nist-sp-800-53-r5
         

The output is the following:
         
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/nist-sp-800-53-r5-asm-peer-authn-strict-mtls created
         k8sallowedrepos.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-repos created
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/nist-sp-800-53-r5-block-creation-with-default-serviceaccount created
         k8sblockobjectsoftype.constraints.gatekeeper.sh/nist-sp-800-53-r5-block-secrets-of-type-basic-auth created
         k8senforceconfigmanagement.constraints.gatekeeper.sh/nist-sp-800-53-r5-enforce-config-management created
         k8spspapparmor.constraints.gatekeeper.sh/nist-sp-800-53-r5-apparmor created
         k8spspcapabilities.constraints.gatekeeper.sh/nist-sp-800-53-r5-capabilities created
         k8spspforbiddensysctls.constraints.gatekeeper.sh/nist-sp-800-53-r5-sysctls created
         k8spsphostfilesystem.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-hostpath-volumes created
         k8spsphostnamespace.constraints.gatekeeper.sh/nist-sp-800-53-r5-host-namespaces created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/nist-sp-800-53-r5-host-network created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/nist-sp-800-53-r5-privileged-containers created
         k8spspprocmount.constraints.gatekeeper.sh/nist-sp-800-53-r5-proc-mount-type created
         k8spspselinuxv2.constraints.gatekeeper.sh/nist-sp-800-53-r5-selinux created
         k8spspseccomp.constraints.gatekeeper.sh/nist-sp-800-53-r5-seccomp created
         k8spspvolumetypes.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-volume-types created
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-role-wildcards created
         k8srequirebinauthz.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-binauthz created
         k8srequirecosnodeimage.constraints.gatekeeper.sh/nist-sp-800-53-r5-nodes-have-consistent-time created
         k8srequiredaemonsets.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-av-daemonset created
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-namespace-network-policies created
         k8srequiredlabels.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-managed-by-label created
         k8srequiredresources.constraints.gatekeeper.sh/nist-sp-800-53-r5-cpu-and-memory-limits-required created
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-rbac-subjects created
         k8srestrictrolebindings.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-clusteradmin-rolebindings created
         k8sstorageclass.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-storageclass created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=nist-sp-800-53-r5
         

The output is similar to the following:
         
         NAME                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspapparmor.constraints.gatekeeper.sh/nist-sp-800-53-r5-apparmor   dryrun               0
         
         NAME                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirebinauthz.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-binauthz   dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-rbac-subjects   dryrun               0
         
         NAME                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspforbiddensysctls.constraints.gatekeeper.sh/nist-sp-800-53-r5-sysctls   dryrun               0
         
         NAME                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspvolumetypes.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-volume-types   dryrun               0
         
         NAME                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnetworkingports.constraints.gatekeeper.sh/nist-sp-800-53-r5-host-network   dryrun               0
         
         NAME                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnamespace.constraints.gatekeeper.sh/nist-sp-800-53-r5-host-namespaces   dryrun               0
         
         NAME                                                                              ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredaemonsets.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-av-daemonset   dryrun               0
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-role-wildcards   dryrun               0
         
         NAME                                                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/nist-sp-800-53-r5-block-creation-with-default-serviceaccount   dryrun               0
         
         NAME                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostfilesystem.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-hostpath-volumes   dryrun               0
         
         NAME                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/nist-sp-800-53-r5-seccomp   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/nist-sp-800-53-r5-asm-peer-authn-strict-mtls   dryrun               0
         
         NAME                                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredresources.constraints.gatekeeper.sh/nist-sp-800-53-r5-cpu-and-memory-limits-required   dryrun               0
         
         NAME                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprocmount.constraints.gatekeeper.sh/nist-sp-800-53-r5-proc-mount-type   dryrun               0
         
         NAME                                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockobjectsoftype.constraints.gatekeeper.sh/nist-sp-800-53-r5-block-secrets-of-type-basic-auth   dryrun               0
         
         NAME                                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-namespace-network-policies   dryrun               0
         
         NAME                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/nist-sp-800-53-r5-capabilities   dryrun               0
         
         NAME                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sstorageclass.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-storageclass   dryrun               0
         
         NAME                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/nist-sp-800-53-r5-require-managed-by-label   dryrun               0
         
         NAME                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/nist-sp-800-53-r5-privileged-containers   dryrun               0
         
         NAME                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sallowedrepos.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-repos   dryrun               0
         
         NAME                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspselinuxv2.constraints.gatekeeper.sh/nist-sp-800-53-r5-selinux   dryrun               0
         
         NAME                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8senforceconfigmanagement.constraints.gatekeeper.sh/nist-sp-800-53-r5-enforce-config-management   dryrun               0
         
         NAME                                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/nist-sp-800-53-r5-restrict-clusteradmin-rolebindings   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirecosnodeimage.constraints.gatekeeper.sh/nist-sp-800-53-r5-nodes-have-consistent-time   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/).

kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the NIST SP 800-53 Rev. 5 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nist-sp-800-53-r5
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval nist-sp-800-53-r5 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
         -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd nist-sp-800-53-r5 kpt live init
         

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
         

  4. Download the NIST SP 800-53 Rev. 5 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/nist-sp-800-53-r5 policies/nist-sp-800-53-r5
         

  5. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/nist-sp-800-53-r5 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  6. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/nist-sp-800-53-r5 kpt live apply --dry-run policies/nist-sp-800-53-r5
         

  7. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/nist-sp-800-53-r5` to your root `kustomization.yaml`. Otherwise remove the `policies/nist-sp-800-53-r5/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/nist-sp-800-53-r5/kustomization.yaml
         

  8. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/nist-sp-800-53-r5 git commit -m 'Adding NIST SP 800-53 Rev. 5 policy audit enforcement'
         git push
         

  9. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

  1. You can also use `kubectl` to view violations on the cluster using the following command:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=nist-sp-800-53-r5 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
         

  2. If violations are present, a listing of the violation messages per constraint can be viewed with:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=nist-sp-800-53-r5 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
         




## Change NIST SP 800-53 Rev. 5 policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=nist-sp-800-53-r5 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=nist-sp-800-53-r5
         




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
         
         kpt fn eval policies/nist-sp-800-53-r5 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/nist-sp-800-53-r5
         git commit -m 'Adding NIST SP 800-53 Rev. 5 policy warn enforcement'
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
      name: wp-non-compliant
    spec:
      containers:
        ‐ image: wordpress
          name: wordpress
    EOF
    

The admission controller should produce a warning listing out the policy violations that this resource violates, as shown in the following example:
    
    
    Warning: [nist-sp-800-53-r5-cpu-and-memory-limits-required] container <wordpress> does not have <{"cpu", "memory"}> limits defined
    Warning: [nist-sp-800-53-r5-restrict-repos] container <wordpress> has an invalid image repo <wordpress>, allowed repos are ["gcr.io/gke-release/", "gcr.io/anthos-baremetal-release/", "gcr.io/config-management-release/", "gcr.io/kubebuilder/", "gcr.io/gkeconnect/", "gke.gcr.io/"]
    pod/wp-non-compliant created
    

## Remove NIST SP 800-53 Rev. 5 policy bundle

If needed, the NIST SP 800-53 Rev. 5 policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=nist-sp-800-53-r5
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repo:
         
         git rm -r SYNC_ROOT_DIR/policies/nist-sp-800-53-r5
         git commit -m 'Removing NIST SP 800-53 Rev. 5 policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
