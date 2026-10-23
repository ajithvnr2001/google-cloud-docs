---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pci-dss-v4/
title: Use PCI-DSS v4.0 policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:54.134613+00:00
---

# Use PCI-DSS v4.0 policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-pci-dss-v4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use PCI-DSS v4.0 policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [PCI-DSS v4.0 bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/anthos-bundles/pci-dss-v4.0) to evaluate the compliance of your cluster resources against some aspects of the [Payment Card Industry Data Security Standard (PCI-DSS) v4.0](https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub).

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## PCI-DSS v4.0 policy bundle constraints

Constraint Name | Constraint Description | Control IDs  
---|---|---  
pci-dss-v4.0-require-apps-annotations  | Requires that all apps in the cluster have a `network-controls/date` annotation.  | 2.2.5   
pci-dss-v4.0-require-av-daemonset  | Requires the presence of an Anti-Virus `DaemonSet`.  | 5.2.1, 5.2.2, 5.2.3, 5.3.1, 5.3.2, 5.3.5   
pci-dss-v4.0-require-binauthz  | Requires the Binary Authorization Validating Admission Webhook.  | 2.2.1, 2.2.4, 6.2.3, 6.3.1, 6.3.2   
pci-dss-v4.0-require-cloudarmor-backendconfig  | Enforces Google Cloud Armor configuration on `BackendConfig` resources.  | 6.4.1, 6.4.2   
pci-dss-v4.0-require-config-management  | Requires that Config Management is running with Drift Prevention enabled and at least one `RootSync` object on the cluster.  | 1.2.8, 2.2.6, 5.3.5, 6.3.2, 6.5.1   
pci-dss-v4.0-require-default-deny-network-policies  | Requires that every namespace defined in the cluster have a default deny `NetworkPolicy` for egress.  | 1.3.2, 1.4.4   
pci-dss-v4.0-require-managed-by-label  | Requires all apps have a valid `app.kubernetes.io/managed-by` label.  | 1.2.8, 2.2.6, 5.3.5, 6.3.2, 6.5.1   
pci-dss-v4.0-require-namespace-network-policies  | Requires that every `Namespace` defined in the cluster has a `NetworkPolicy`.  | 1.2.5, 1.2.6, 1.4.1, 1.4.4   
pci-dss-v4.0-require-peer-authentication-strict-mtls  | Ensures PeerAuthentications cannot overwrite strict mTLS.  | 2.2.7, 4.2.1, 8.3.2   
pci-dss-v4.0-require-valid-network-ranges  | Restricts CIDR ranges permitted for use with ingress and egress.  | 1.3.1, 1.3.2, 1.4.2, 1.4.4   
pci-dss-v4.0-resources-have-required-labels  | Requires all apps to contain a specified label to meet firewall requirements.  | 1.2.7   
pci-dss-v4.0-restrict-cluster-admin-role  | Restricts the use of the `cluster-admin` role.  | 7.2.1, 7.2.2, 7.2.5, 8.2.4   
pci-dss-v4.0-restrict-creation-with-default-serviceaccount  | Restricts the creation of resources using a default service account. Has no effect during audit.  | 2.2.2   
pci-dss-v4.0-restrict-default-namespace  | Restricts pods from using the default namespace.  | 2.2.3   
pci-dss-v4.0-restrict-ingress  | Restricts the creation of `Ingress` objects.  | 1.3.1, 1.4.2, 1.4.4   
pci-dss-v4.0-restrict-node-image  | Ensures consistent and correct time on Nodes by allowing only Container-Optimized OS or Ubuntu as the OS image.  | 10.6.1, 10.6.2, 10.6.3   
pci-dss-v4.0-restrict-pods-exec  | Restricts the use of `pods/exec` in `Roles` and `ClusterRoles`.  | 8.6.1   
pci-dss-v4.0-restrict-rbac-subjects  | Restricts the use of names in RBAC subjects to permitted values.  | 7.3.2, 8.2.1, 8.2.2, 8.2.4   
pci-dss-v4.0-restrict-role-wildcards  | Restricts the use of wildcards in `Roles` and `ClusterRoles`.  | 7.3.3, 8.2.4   
pci-dss-v4.0-restrict-storageclass  | Restricts `StorageClass` to a list of `StorageClass` which encrypt by default.  | 3.3.2, 3.3.3   
  
## Before you begin

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) v1.16.0 or higher on your cluster with the default library of constraint templates. You must also [enable support for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential) as this bundle contains referential constraints.



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
               - group: "storage.k8s.io"
                 version: "v1"
                 kind: "StorageClass"
         

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




### Configure your cluster's workload for PCI-DSS v4.0

  1. All apps (`ReplicaSet`, `Deployment`, `StatefulSet`, `DaemonSet`) must include a `network-controls/date` annotation with the schema of`YYYY-MM-DD`.
  2. An antivirus solution is required. The default is the presence of a `daemonset` named [`clamav`](https://docs.clamav.net/) in the `clamav` `Namespace`, however the `daemonset`'s name and namespace can be customized to your implementation in the `pci-dss-v4.0-require-av-daemonset` constraint.
  3. Enablement and configuration of [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) is required in `pci-dss-v4.0-require-binauthz`.
  4. All `BackendConfig` must be configured for [CloudArmor](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-features#cloud_armor).
  5. The presence and enablement of [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-config-sync) is required.
  6. Every `Namespace` defined in the cluster have a default deny `NetworkPolicy` for egress, permitted exceptions can be specific in `pci-dss-v4.0-require-namespace-network-policies`.
  7. The use of [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) for `configmanagement.gke.io` is required by default, however the permitted `app.kubernetes.io/managed-by` value can be customized in the `pci-dss-v4.0-enforce-managed-by-configmanagement-label` constraint.
  8. Every `Namespace` defined in the cluster must have a `NetworkPolicy`.
  9. If using [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh), ASM PeerAuthentication must use strict mTLS `spec.mtls.mode: STRICT`.
  10. Only permitted IP ranges can be used for Ingress and Express, these can be specified in `pci-dss-v4.0-require-valid-network-ranges`.
  11. All apps (`ReplicaSet`, `Deployment`, `StatefulSet`, and `DaemonSet`) must include a `pci-dss-firewall-audit label` with the schema of `pci-dss-[0-9]{4}q[1-4]`.
  12. The use of the cluster-admin `ClusterRole` is not permitted.
  13. Resources cannot be created using the default service account.
  14. The default `Namespace` cannot be used for pods.
  15. Only permitted Ingress objects (`Ingress`, `Gateway`, and `Service` types of `NodePort` and `LoadBalancer`) can be created, these can be specified in `pci-dss-v4.0-restrict-ingress`.
  16. All nodes must use [Container-Optimized OS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) or Ubuntu for their image for consistent time.
  17. The use of the wildcard character or the `pods/exec` permission in `Roles` and `ClusterRoles` is not permitted.
  18. Only permitted subjects can be used in RBAC bindings, your domain name(s) can be specified in `pci-dss-v4.0-restrict-rbac-subjects`.
  19. The use of encrypt by default `StorageClass` is required in `pci-dss-v4.0-restrict-storageclass`.



## Audit PCI-DSS v4.0 policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the PCI-DSS v4.0 policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pci-dss-v4.0
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pci-dss-v4.0
         

The output is the following:
         
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/pci-dss-v4.0-require-peer-authentication-strict-mtls created
         k8sblockallingress.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-ingress created
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-creation-with-default-serviceaccount created
         k8senforcecloudarmorbackendconfig.constraints.gatekeeper.sh/pci-dss-v4.0-require-cloudarmor-backendconfig created
         k8senforceconfigmanagement.constraints.gatekeeper.sh/pci-dss-v4.0-require-config-management created
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-role-wildcards created
         k8srequirebinauthz.constraints.gatekeeper.sh/pci-dss-v4.0-require-binauthz created
         k8srequirecosnodeimage.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-node-image created
         k8srequiredaemonsets.constraints.gatekeeper.sh/pci-dss-v4.0-require-av-daemonset created
         k8srequiredefaultdenyegresspolicy.constraints.gatekeeper.sh/pci-dss-v4.0-require-default-deny-network-policies created
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/pci-dss-v4.0-require-namespace-network-policies created
         k8srequirevalidrangesfornetworks.constraints.gatekeeper.sh/pci-dss-v4.0-require-valid-network-ranges created
         k8srequiredannotations.constraints.gatekeeper.sh/pci-dss-v4.0-require-apps-annotations created
         k8srequiredlabels.constraints.gatekeeper.sh/pci-dss-v4.0-require-managed-by-label created
         k8srequiredlabels.constraints.gatekeeper.sh/pci-dss-v4.0-resources-have-required-labels created
         k8srestrictnamespaces.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-default-namespace created
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-rbac-subjects created
         k8srestrictrolebindings.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-cluster-admin-role created
         k8srestrictrolerules.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-pods-exec created
         k8sstorageclass.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-storageclass created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get constraints -l policycontroller.gke.io/bundleName=pci-dss-v4.0
         

The output is similar to the following:
         
         NAME                                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/pci-dss-v4.0-require-peer-authentication-strict-mtls   dryrun               0
         
         NAME                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockallingress.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-ingress   dryrun               0
         
         NAME                                                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sblockcreationwithdefaultserviceaccount.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-creation-with-default-serviceaccount   dryrun               0
         
         NAME                                                                                                        ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8senforcecloudarmorbackendconfig.constraints.gatekeeper.sh/pci-dss-v4.0-require-cloudarmor-backendconfig   dryrun               0
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8senforceconfigmanagement.constraints.gatekeeper.sh/pci-dss-v4.0-require-config-management   dryrun               0
         
         NAME                                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-role-wildcards   dryrun               0
         
         NAME                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirebinauthz.constraints.gatekeeper.sh/pci-dss-v4.0-require-binauthz   dryrun               0
         
         NAME                                                                                ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirecosnodeimage.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-node-image   dryrun               0
         
         NAME                                                                               ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredaemonsets.constraints.gatekeeper.sh/pci-dss-v4.0-require-av-daemonset   dryrun               0
         
         NAME                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredannotations.constraints.gatekeeper.sh/pci-dss-v4.0-require-apps-annotations   dryrun               0
         
         NAME                                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredefaultdenyegresspolicy.constraints.gatekeeper.sh/pci-dss-v4.0-require-default-deny-network-policies   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequiredlabels.constraints.gatekeeper.sh/pci-dss-v4.0-require-managed-by-label         dryrun               0
         k8srequiredlabels.constraints.gatekeeper.sh/pci-dss-v4.0-resources-have-required-labels   dryrun               0
         
         NAME                                                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirenamespacenetworkpolicies.constraints.gatekeeper.sh/pci-dss-v4.0-require-namespace-network-policies   dryrun               0
         
         NAME                                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srequirevalidrangesfornetworks.constraints.gatekeeper.sh/pci-dss-v4.0-require-valid-network-ranges   dryrun               0
         
         NAME                                                                                      ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictnamespaces.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-default-namespace   dryrun               0
         
         NAME                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrbacsubjects.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-rbac-subjects   dryrun               0
         
         NAME                                                                                         ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-cluster-admin-role   dryrun               0
         
         NAME                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolerules.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-pods-exec   dryrun               0
         
         NAME                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sstorageclass.constraints.gatekeeper.sh/pci-dss-v4.0-restrict-storageclass   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the PCI-DSS v4.0 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pci-dss-v4.0
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval pci-dss-v4.0 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd pci-dss-v4.0
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
         

  3. Download the PCI-DSS v4.0 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/anthos-bundles/pci-dss-v4.0 policies/pci-dss-v4.0
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/pci-dss-v4.0 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/pci-dss-v4.0
         kpt live apply --dry-run policies/pci-dss-v4.0
         

  6. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/pci-dss-v4.0` to your root `kustomization.yaml`. Otherwise remove the `policies/pci-dss-v4.0/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/pci-dss-v4.0/kustomization.yaml
         

  7. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/pci-dss-v4.0
         git commit -m 'Adding PCI-DSS v4.0 policy audit enforcement'
         git push
         

  8. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=pci-dss-v4.0 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=pci-dss-v4.0 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change PCI-DSS v4.0 policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=pci-dss-v4.0 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=pci-dss-v4.0
         




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
         
         kpt fn eval policies/pci-dss-v4.0 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repository:
         
         git add SYNC_ROOT_DIR/policies/pci-dss-v4.0
         git commit -m 'Adding PCI-DSS v4.0 policy bundle warn enforcement'
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
    
    
    Warning: [pci-dss-v4.0-restrict-default-namespace] <default> namespace is restricted
    pod/wp-non-compliant created
    

## Remove PCI-DSS v4.0 policy bundle

If needed, the PCI-DSS v4.0 policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=pci-dss-v4.0
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repository:
         
         git rm -r SYNC_ROOT_DIR/policies/pci-dss-v4.0
         git commit -m 'Removing PCI-DSS v4.0 policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
