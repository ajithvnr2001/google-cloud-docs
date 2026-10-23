---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-policy-essentials-v2022/
title: Use Policy Essentials v2022 policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:42.981668+00:00
---

# Use Policy Essentials v2022 policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-policy-essentials-v2022/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use Policy Essentials v2022 policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the [Policy Essentials v2022 bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/tree/main/bundles/policy-essentials-v2022) to apply Google recommended best practices to your cluster resources.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This bundle of constraints addresses and enforces policies in the following domains:

  * RBAC and service accounts
  * Pod Security Policies
  * Container Network Interface (CNI)
  * Secrets management
  * General policies



## Policy Essentials policy bundle constraints

Constraint Name | Constraint Description  
---|---  
policy-essentials-v2022-no-secrets-as-env-vars | Prefer using Secrets as files over Secrets as environment variables  
policy-essentials-v2022-pods-require-security-context | Apply Security Context to your Pods and containers  
policy-essentials-v2022-prohibit-role-wildcard-access | Minimize the use of wildcards in Roles and ClusterRoles.  
policy-essentials-v2022-psp-allow-privilege-escalation-container | Minimize the admission of containers with allowPrivilegeEscalation  
policy-essentials-v2022-psp-capabilities | Containers must drop the `NET_RAW` capability and aren't permitted to add back any capabilities.  
policy-essentials-v2022-psp-host-namespace | Minimize the admission of containers with `hostPID` or `hostIPC` set to `true`.  
policy-essentials-v2022-psp-host-network-ports | Minimize the admission of containers wanting to share the host network namespace  
policy-essentials-v2022-psp-privileged-container | Minimize the admission of privileged containers  
policy-essentials-v2022-psp-pods-must-run-as-nonroot | Minimize the admission of root containers  
policy-essentials-v2022-psp-seccomp-default | Ensure that the seccomp profile is set to `runtime/default` or `docker/default` in your Pod definitions  
policy-essentials-v2022-restrict-clusteradmin-rolebindings | Minimize the use of the cluster-admin role.  
  
## Before you begin

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) v1.14.3 or higher on your cluster with the default library of constraint templates.



## Audit Policy Essentials policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the Google recommended best practices outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/policy-essentials-v2022
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/policy-essentials-v2022
         

The output is the following:
         
         k8snoenvvarsecrets.constraints.gatekeeper.sh/policy-essentials-v2022-no-secrets-as-env-vars created
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-allow-privilege-escalation created
         k8spspallowedusers.constraints.gatekeeper.sh/policy-essentials-v2022-psp-pods-must-run-as-nonroot created
         k8spspcapabilities.constraints.gatekeeper.sh/policy-essentials-v2022-psp-capabilities created
         k8spsphostnamespace.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-namespace created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-network-ports created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-privileged-container created
         k8spspseccomp.constraints.gatekeeper.sh/policy-essentials-v2022-psp-seccomp-default created
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/policy-essentials-v2022-pods-require-security-context created
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/policy-essentials-v2022-prohibit-role-wildcard-access created
         k8srestrictrolebindings.constraints.gatekeeper.sh/policy-essentials-v2022-restrict-clusteradmin-rolebindings created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/policy-essentials-v2022
         

The output is similar to the following:
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8snoenvvarsecrets.constraints.gatekeeper.sh/policy-essentials-v2022-no-secrets-as-env-vars   dryrun               0
         
         NAME                                                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-allow-privilege-escalation   dryrun               0
         
         NAME                                                                                                ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspallowedusers.constraints.gatekeeper.sh/policy-essentials-v2022-psp-pods-must-run-as-nonroot   dryrun               0
         
         NAME                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspcapabilities.constraints.gatekeeper.sh/policy-essentials-v2022-psp-capabilities   dryrun               0
         
         NAME                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnamespace.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-namespace   dryrun               0
         
         NAME                                                                                                 ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spsphostnetworkingports.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-network-ports   dryrun               0
         
         NAME                                                                                                   ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-privileged-container   dryrun               0
         
         NAME                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spspseccomp.constraints.gatekeeper.sh/policy-essentials-v2022-psp-seccomp-default   dryrun               0
         
         NAME                                                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/policy-essentials-v2022-pods-require-security-context   dryrun               0
         
         NAME                                                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/policy-essentials-v2022-prohibit-role-wildcard-access   dryrun               0
         
         NAME                                                                                                           ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         k8srestrictrolebindings.constraints.gatekeeper.sh/policy-essentials-v2022-restrict-clusteradmin-rolebindings   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the Policy Essentials v2022 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/policy-essentials-v2022
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policy-essentials-v2022 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd policy-essentials-v2022
         kpt live init
         

  5. Apply the policy constraints with kpt:
         
         kpt live apply
         

The output is the following:
         
         k8spspseccomp.constraints.gatekeeper.sh/policy-essentials-v2022-psp-seccomp-docker-default created
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/policy-essentials-v2022-pods-require-security-context created
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/policy-essentials-v2022-prohibit-role-wildcard-access created
         k8snoenvvarsecrets.constraints.gatekeeper.sh/policy-essentials-v2022-no-secrets-as-env-vars created
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-allow-privilege-escalation-container created
         k8spspallowedusers.constraints.gatekeeper.sh/policy-essentials-v2022-psp-pods-must-run-as-nonroot created
         k8spsphostnetworkingports.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-network-ports created
         k8srestrictrolebindings.constraints.gatekeeper.sh/policy-essentials-v2022-restrict-clusteradmin-rolebindings created
         k8spspcapabilities.constraints.gatekeeper.sh/policy-essentials-v2022-psp-capabilities created
         k8spsphostnamespace.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-namespace created
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-privileged-container created
         11 resource(s) applied. 11 created, 0 unchanged, 0 configured, 0 failed
         

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
         

  3. Download the Policy Essentials v2022 policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/policy-essentials-v2022 policies/policy-essentials-v2022
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/policy-essentials-v2022 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/policy-essentials-v2022
         kpt live apply --dry-run policies/policy-essentials-v2022
         

The output is the following:
         
         Dry-run strategy: client
         inventory update started
         inventory update finished
         apply phase started
         k8snoenvvarsecrets.constraints.gatekeeper.sh/policy-essentials-v2022-no-secrets-as-env-vars apply successful
         k8spspallowprivilegeescalationcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-allow-privilege-escalation apply successful
         k8spspallowedusers.constraints.gatekeeper.sh/policy-essentials-v2022-psp-pods-must-run-as-nonroot apply successful
         k8spspcapabilities.constraints.gatekeeper.sh/policy-essentials-v2022-psp-capabilities apply successful
         k8spsphostnamespace.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-namespace apply successful
         k8spsphostnetworkingports.constraints.gatekeeper.sh/policy-essentials-v2022-psp-host-network-ports apply successful
         k8spspprivilegedcontainer.constraints.gatekeeper.sh/policy-essentials-v2022-psp-privileged-container apply successful
         k8spspseccomp.constraints.gatekeeper.sh/policy-essentials-v2022-psp-seccomp-default apply successful
         k8spodsrequiresecuritycontext.constraints.gatekeeper.sh/policy-essentials-v2022-pods-require-security-context apply successful
         k8sprohibitrolewildcardaccess.constraints.gatekeeper.sh/policy-essentials-v2022-prohibit-role-wildcard-access apply successful
         k8srestrictrolebindings.constraints.gatekeeper.sh/policy-essentials-v2022-restrict-clusteradmin-rolebindings apply successful
         apply phase finished
         inventory update started
         inventory update finished
         apply result: 11 attempted, 11 successful, 0 skipped, 0 failed
         

  6. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/policy-essentials-v2022` to your root `kustomization.yaml`. Otherwise remove the `policies/policy-essentials-v2022/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/policy-essentials-v2022/kustomization.yaml
         

  7. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policy-essentials-v2022
         git commit -m 'Adding Policy Essentials v2022 policy audit enforcement'
         git push
         

  8. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=policy-essentials-v2022 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=policy-essentials-v2022 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change Policy Essentials policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=policy-essentials-v2022 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=policy-essentials-v2022
         




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
         
         kpt fn eval policies/policy-essentials-v2022 -i gcr.io/kpt-fn/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/policy-essentials-v2022
         git commit -m 'Adding Policy Essentials policy bundle warn enforcement'
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
    
    
    Warning: [policy-essentials-v2022-psp-capabilities] container <wordpress> is not dropping all required capabilities. Container must drop all of ["NET_RAW"] or "ALL"
    pod/wp-non-compliant created
    

## Remove Policy Essentials policy bundle

If needed, the Policy Essentials policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=policy-essentials-v2022
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repo:
         
         git rm -r SYNC_ROOT_DIR/policies/policy-essentials-v2022
         git commit -m 'Removing Policy Essentials v2022 policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
