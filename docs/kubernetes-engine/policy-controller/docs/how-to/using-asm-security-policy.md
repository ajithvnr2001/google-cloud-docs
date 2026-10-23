---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-asm-security-policy/
title: Use Cloud Service Mesh security policy constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:56.859674+00:00
---

# Use Cloud Service Mesh security policy constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-asm-security-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use Cloud Service Mesh security policy constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller comes with a default library of [constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) that can be used with the Cloud Service Mesh [security bundle](https://github.com/GoogleCloudPlatform/gke-policy-library/blob/main/bundles/asm-policy-v0.0.1) to audit the compliance of your mesh security vulnerabilities and best practices.

This page contains instructions for manually applying a policy bundle. Alternatively, you can [apply policy bundles directly](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/apply-policy-bundles).

**Warning:** After you choose a method to apply policy bundles (manual, gcloud CLI, or Google Cloud console), using a different method to install policy bundles can cause errors in your environment. 

This bundle of constraints addresses and enforces policies in the following domains:

  * Cloud Service Mesh enforce mTLS traffic
  * Cloud Service Mesh AuthorizationPolicy best practices
  * Cloud Service Mesh workload security enforcement



## Cloud Service Mesh policy bundle constraints

Constraint Name | Constraint Description | Control ID  
---|---|---  
asm-policy-v0.0.1-asm-ingressgateway-label | Enforce the istio ingressgateway label usage only on ingressgateway pods | 1.1.1  
asm-policy-v0.0.1-asm-sidecar-injection | Enforce the istio proxy sidecar always been injected to workload pods | 1.1.2  
asm-policy-v0.0.1-asm-authz-policy-mesh-default-deny | Enforce the mesh level [default deny](https://istio.io/latest/docs/ops/best-practices/security/#use-default-deny-patterns) AuthorizationPolicy | 1.2.1  
asm-policy-v0.0.1-asm-authz-policy-normalization | Enforce the AuthorizationPolicy [normalization](https://istio.io/latest/docs/reference/config/security/normalization) | 1.2.2  
asm-policy-v0.0.1-asm-authz-policy-safe-pattern | Enforce the AuthorizationPolicy [safe patterns](https://istio.io/latest/docs/ops/best-practices/security/#safer-authorization-policy-patterns) | 1.2.3  
asm-policy-v0.0.1-asm-peer-authn-mesh-strict-mtls | Enforce the mesh level [strict mtls](https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls) PeerAuthentication | 1.3.1  
asm-policy-v0.0.1-asm-peer-authn-strict-mtls | Enforce all PeerAuthentications cannot overwrite [strict mtls](https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls) | 1.3.2  
asm-policy-v0.0.1-asm-request-authn-prohibited-output-headers | Enforce the jwtRules outputPayloadToHeader to not contain well known HTTP request headers | 1.4.1  
  
## Bundle profiles

In the Cloud Service Mesh security policy bundle, you can use two profiles based on the strictness level. Low strictness level has fewer constraints applied, which provides more flexibility. High strictness level has more constraints applied, which provides more secure policy control.

### Low strictness level

The low strictness level profile has the following policy constraints:

  * The label `istio:ingressgateway` can only be used by Istio ingress gateway Pods.

  * In `AuthorizationPolicy`, the `hosts` or `notHosts` fields can only be used by selecting Istio ingress gateway which has the label `istio:ingressgateway`.

  * In `AuthorizationPolicy`, when the `methods` or `notMethods` fields are used, the values must be uppercase letters.

  * In `AuthorizationPolicy`, when the `request.headers` field is used, the values cannot contain white spaces.

  * In `AuthorizationPolicy`, when the `paths` or `notPaths` fields are used, the values must be [normalized](https://istio.io/latest/docs/reference/config/security/normalization/) values.




### High strictness level

The high strictness level includes all of the constraints from the low strictness level as well as the following constraints:

  * For all workload Pods, annotation `sidecar.istio.io/inject: false` cannot be applied to bypass proxy injection.

  * A mesh level `AuthorizationPolicy` that defines a [default deny](https://istio.io/latest/docs/ops/best-practices/security/#use-default-deny-patterns) rule is enforced.

  * The `AuthorizationPolicy` must follow either [ALLOW-with-positive-matching](https://istio.io/latest/docs/ops/best-practices/security/#use-allow-with-positive-matching-and-deny-with-negative-match-patterns) or [DENY-with-negative-match](https://istio.io/latest/docs/ops/best-practices/security/#use-allow-with-positive-matching-and-deny-with-negative-match-patterns).

  * In `AuthorizationPolicy`, when the `hosts` or `notHosts` fields are used, the values must be pairs of `<host-name>` and `<host-name>:*`.

  * A mesh level `PeerAuthentication` that defines [strict mTLS](https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls) is enforced.

  * For all `PeerAuthentication` in the mesh, the mTLS mode can only be either `UNSET` or `STRICT`, to follow [strict mTLS](https://istio.io/latest/docs/ops/best-practices/security/#mutual-tls).




## Bundle settings

KPT setter | Description  
---|---  
strictness-level | Cloud Service Mesh bundle strictness level profile, options are `Low` or `High` (default)  
  
## Before you begin

  1. Install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs), which provides the `gcloud` and `kubectl` commands used in these instructions. If you use Cloud Shell, Google Cloud CLI comes pre-installed.
  2. [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller) v.1.11.2 or higher on your cluster with the default library of constraint templates. You must also [enable support for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential), as this bundle contains referential constraints.
  3. Ensure that [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) is installed on your cluster.



### Configure Policy Controller for referential constraints

**Warning:** You can overwrite your changes. If you already have an existing `Config` in the `gatekeeper-system` namespace, you must include all previous customization settings to preserve your changes.

  1. Save the following YAML manifest as `policycontroller-config.yaml`:
         
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
                 kind: "Namespace"
               - group: "security.istio.io"
                 version: "v1beta1"
                 kind: "AuthorizationPolicy"
               - group: "security.istio.io"
                 version: "v1beta1"
                 kind: "PeerAuthentication"
         

This manifest configures Policy Controller to watch specific kinds of objects.

  2. Apply the `policycontroller-config.yaml` manifest:
         
         kubectl apply -f policycontroller-config.yaml
         




## Audit Cloud Service Mesh policy bundle

Policy Controller lets you enforce policies for your Kubernetes cluster. To help test your workloads and their compliance with regard to the Cloud Service Mesh security policies outlined in the preceding table, you can deploy these constraints in "audit" mode to reveal violations and more importantly give yourself a chance to fix them before enforcing on your Kubernetes cluster.

You can apply these policies with `spec.enforcementAction` set to `dryrun` using kubectl, [kpt](https://kpt.dev/?id=overview), or [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview).

### kubectl

  1. (Optional) Preview the policy constraints with kubectl:
         
         kubectl kustomize https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/asm-policy-v0.0.1
         

  2. Apply the policy constraints with kubectl:
         
         kubectl apply -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/asm-policy-v0.0.1
         

The output is the following:
         
         asmauthzpolicydefaultdeny.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-mesh-default-deny created
         asmauthzpolicynormalization.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-normalization created
         asmauthzpolicysafepattern.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-safe-pattern created
         asmingressgatewaylabel.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-ingressgateway-label created
         asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-peer-authn-mesh-strict-mtls created
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-peer-authn-strict-mtls created
         asmrequestauthnprohibitedoutputheaders.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-request-authn-prohibited-output-headers created
         asmsidecarinjection.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-sidecar-injection created
         

  3. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
         kubectl get -k https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/asm-policy-v0.0.1
         

The output is similar to the following:
         
         NAME                                                                                                       ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmauthzpolicydefaultdeny.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-mesh-default-deny   dryrun               0
         
         NAME                                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmauthzpolicynormalization.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-normalization   dryrun               0
         
         NAME                                                                                                  ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmauthzpolicysafepattern.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-safe-pattern   dryrun               0
         
         NAME                                                                                          ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmingressgatewaylabel.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-ingressgateway-label   dryrun               0
         
         NAME                                                                                                     ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-peer-authn-mesh-strict-mtls   dryrun               0
         
         NAME                                                                                            ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-peer-authn-strict-mtls   dryrun               0
         
         NAME                                                                                                                             ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmrequestauthnprohibitedoutputheaders.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-request-authn-prohibited-output-headers   dryrun               0
         
         NAME                                                                                    ENFORCEMENT-ACTION   TOTAL-VIOLATIONS
         asmsidecarinjection.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-sidecar-injection   dryrun               0
         




### kpt

  1. Install and setup [kpt](https://kpt.dev/installation/). kpt is used in these instructions to customize and deploy Kubernetes resources.

  2. Download the Cloud Service Mesh security policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/asm-policy-v0.0.1
         

  3. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval asm-policy-v0.0.1 -i ghcr.io/kptdev/krm-functions-catalog/set-enforcement-action:v0.1 \
           -- enforcementAction=dryrun
         

  4. Run the kpt [setter function](https://catalog.kpt.dev/apply-setters/v0.2/) to set Cloud Service Mesh security policies specific fields:
         
         kpt fn eval asm-policy-v0.0.1 --image ghcr.io/kptdev/krm-functions-catalog/apply-setters:v0.2 -- \
         strictness-level="Low"
         

  5. Initialize the working directory with kpt, which creates a resource to track changes:
         
         cd asm-policy-v0.0.1
         kpt live init
         

  6. Apply the policy constraints with kpt:
         
         kpt live apply
         

The output is the following:
         
         asmauthzpolicydefaultdeny.constraints.gatekeeper.sh/asm-authz-policy-mesh-default-deny created
         asmauthzpolicynormalization.constraints.gatekeeper.sh/asm-authz-policy-normalization created
         asmauthzpolicysafepattern.constraints.gatekeeper.sh/asm-authz-policy-safe-pattern created
         asmingressgatewaylabel.constraints.gatekeeper.sh/asm-ingressgateway-label created
         asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/asm-peer-authn-mesh-strict-mtls created
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/asm-peer-authn-strict-mtls created
         asmsidecarinjection.constraints.gatekeeper.sh/asm-sidecar-injection created
         7 resource(s) applied. 7 created, 0 unchanged, 0 configured, 0 failed
         

  7. Verify that policy constraints have been installed and check if violations exist across the cluster:
         
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
         

  3. Download the Cloud Service Mesh security policy bundle from GitHub using kpt:
         
         kpt pkg get https://github.com/GoogleCloudPlatform/gke-policy-library.git/bundles/asm-policy-v0.0.1 policies/asm-policy-v0.0.1
         

  4. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `dryrun`:
         
         kpt fn eval policies/asm-policy-v0.0.1 -i ghcr.io/kptdev/krm-functions-catalog/set-enforcement-action:v0.1 -- enforcementAction=dryrun
         

  5. Run the kpt [setter function](https://catalog.kpt.dev/apply-setters/v0.2/) to set Cloud Service Mesh security policies specific fields:
         
         kpt fn eval policies/asm-policy-v0.0.1 --image ghcr.io/kptdev/krm-functions-catalog/apply-setters:v0.2 -- \
         strictness-level="Low"
         

  6. (Optional) Preview the policy constraints to be created:
         
         kpt live init policies/asm-policy-v0.0.1
         kpt live apply --dry-run policies/asm-policy-v0.0.1
         

The output is the following:
         
         Dry-run strategy: client
         inventory update started
         inventory update finished
         apply phase started
         asmauthzpolicydefaultdeny.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-mesh-default-deny apply successful
         asmauthzpolicynormalization.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-normalization apply successful
         asmauthzpolicysafepattern.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-authz-policy-safe-pattern apply successful
         asmingressgatewaylabel.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-ingressgateway-label apply successful
         asmpeerauthnmeshstrictmtls.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-peer-authn-mesh-strict-mtls apply successful
         asmpeerauthnstrictmtls.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-peer-authn-strict-mtls apply successful
         asmrequestauthnprohibitedoutputheaders.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-request-authn-prohibited-output-headers apply successful
         asmsidecarinjection.constraints.gatekeeper.sh/asm-policy-v0.0.1-asm-sidecar-injection apply successful
         apply phase finished
         inventory update started
         inventory update finished
         apply result: 8 attempted, 8 successful, 0 skipped, 0 failed
         

  7. If your sync directory for Config Sync uses [Kustomize](https://kustomize.io/), add `policies/asm-policy-v0.0.1` to your root `kustomization.yaml`. Otherwise remove the `policies/asm-policy-v0.0.1/kustomization.yaml` file:
         
         rm SYNC_ROOT_DIR/policies/asm-policy-v0.0.1/kustomization.yaml
         

  8. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/asm-policy-v0.0.1
         git commit -m 'Adding ASM security policy audit enforcement'
         git push
         

  9. Verify the status of the installation:
         
         watch gcloud beta container fleet config-management status --project PROJECT_ID
         

A status of `SYNCED` confirms the installation of the policies.




## View policy violations

Once the policy constraints are installed in audit mode, violations on the cluster can be viewed in the UI using the [Policy Controller Dashboard](https://docs.cloud.google.com/anthos-config-management/docs/how-to/policy-controller-status).

You can also use `kubectl` to view violations on the cluster using the following command:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=asm-policy-v0.0.1 -o json | jq -cC '.items[]| [.metadata.name,.status.totalViolations]'
    

If violations are present, a listing of the violation messages per constraint can be viewed with:
    
    
    kubectl get constraint -l policycontroller.gke.io/bundleName=asm-policy-v0.0.1 -o json | jq -C '.items[]| select(.status.totalViolations>0)| [.metadata.name,.status.violations[]?]'
    

## Change Cloud Service Mesh policy bundle enforcement action

Once you've reviewed policy violations on your cluster, you can consider changing the enforcement mode so the Admission Controller will either `warn` on or even `deny` block non-compliant resource from getting applied to the cluster.

**Warning:** The `deny` enforcement action should be used with care as it can potentially block required changes resulting in interruption to critical workloads or the cluster. It is strongly recommended that only the `warn` or `dryrun` enforcement actions are used on clusters with production workloads, when testing new constraints, or performing migrations such as upgrading platforms. For more information about enforcement actions, see [Auditing using constraints](https://docs.cloud.google.com/anthos-config-management/docs/how-to/auditing-constraints).

### kubectl

  1. Use kubectl to set the policies' enforcement action to `warn`:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=asm-policy-v0.0.1 -o name | xargs -I {} kubectl patch {} --type='json' -p='[{"op":"replace","path":"/spec/enforcementAction","value":"warn"}]'
         

  2. Verify that policy constraints enforcement action have been updated:
         
         kubectl get constraint -l policycontroller.gke.io/bundleName=asm-policy-v0.0.1
         




### kpt

  1. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `warn`:
         
         kpt fn eval -i ghcr.io/kptdev/krm-functions-catalog/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  2. Apply the policy constraints:
         
         kpt live apply
         




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Change into the sync directory for Config Sync:
         
         cd SYNC_ROOT_DIR
         

  2. Run the [`set-enforcement-action`](https://catalog.kpt.dev/set-enforcement-action/v0.1/) kpt function to set the policies' enforcement action to `warn`:
         
         kpt fn eval policies/asm-policy-v0.0.1 -i ghcr.io/kptdev/krm-functions-catalog/set-enforcement-action:v0.1 -- enforcementAction=warn
         

  3. Push changes to the Config Sync repo:
         
         git add SYNC_ROOT_DIR/policies/asm-policy-v0.0.1
         git commit -m 'Adding ASM security policy bundle warn enforcement'
         git push
         

  4. Verify the status of the installation:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the installed policies.




## Test policy enforcement

Create a non-compliant resource on the cluster using the following command:
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: non-compliant-authz-policy
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            methods: ["get"]
    EOF
    

The admission controller should produce a warning listing out the policy violations that this resource violates, as shown in the following example:
    
    
    Warning: [asm-policy-v0.0.1-asm-authz-policy-normalization] in rules-to-operation, methods or notMethods must be uppercase
    authorizationpolicy.security.istio.io/non-compliant-authz-policy created
    

## Remove Cloud Service Mesh policy bundle

If needed, the Cloud Service Mesh policy bundle can be removed from the cluster.

### kubectl

  * Use kubectl to remove the policies:
        
        kubectl delete constraint -l policycontroller.gke.io/bundleName=asm-policy-v0.0.1
        




### kpt

  * Remove the policies:
        
        kpt live destroy
        




###  Config Sync 

Operators using Config Sync to deploy policies to their clusters can use the following instructions:

  1. Push changes to the Config Sync repo:
         
         git rm -r SYNC_ROOT_DIR/policies/asm-policy-v0.0.1
         git commit -m 'Removing Cloud Service Mesh  policies'
         git push
         

  2. Verify the status:
         
         nomos status
         

The cluster should display a status of `SYNCED` with the resources removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
