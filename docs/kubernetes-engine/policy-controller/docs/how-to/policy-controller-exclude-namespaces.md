---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces/
title: Exclude namespaces from Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:58.096308+00:00
---

# Exclude namespaces from Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Exclude namespaces from Policy Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure exempt namespaces in Policy Controller.

**Caution:** Namespace exemption from the admission webhook is possible only on Standard clusters. For Autopilot clusters, you can [define exemptions on the constraint](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#constraint) instead.

Exempt namespaces remove a namespace from admission webhook enforcement with Policy Controller, but any violations are still reported in [audit](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints). If you don't configure any namespaces, only the `gatekeeper-system` namespace is pre-configured as exempt from the Policy Controller admission webhook enforcement.

## Configure exempt namespaces

Configuring an exemptable namespace applies the `admission.gatekeeper.sh/ignore` label, which exempts the namespace from Policy Controller admission webhook enforcement. If you later remove an exemptable namespace, Policy Controller does not remove the `admission.gatekeeper.sh/ignore` label from the namespace.

### Exempt namespaces from enforcement

You can exempt namespaces either [during Policy Controller installation](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller#installing), or after installation. The following process shows you how to exempt namespaces after installation.

### Console

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. Expand the **Edit Policy Controller configuration** menu.
  4. In the **Exempt namespaces** field, provide a list of valid namespaces. Objects in these namespaces are ignored by all policies. The namespaces don't need to exist yet.
  5. Select **Save changes**.



### gcloud

To add namespaces to the list of namespaces that may be exempted from enforcement by the admission webhook, run the following command:
    
    
      gcloud container fleet policycontroller update \
        --memberships=MEMBERSHIP_NAME \
        --exemptable-namespaces=NAMESPACE_LIST
    

Replace the following:

  * `MEMBERSHIP_NAME`: the membership name of the registered cluster to exempt namespaces on. You can specify multiple memberships separated by a comma.
  * `NAMESPACE_LIST`: a comma-separated list of namespaces that you want Policy Controller to exempt from enforcement.



This command exempts resources only from the admission webhook. The resources are still audited. To instead exempt namespaces from audit, set the exemption at the policy bundle level instead:
    
    
      gcloud container fleet policycontroller content bundles set BUNDLE_NAME \
        --memberships=MEMBERSHIP_NAME \
        --exempted-namespaces=NAMESPACE_LIST
    

Replace the following:

  * `BUNDLE_NAME` with the name of the policy bundle that you want to update with exempted namespaces.
  * `MEMBERSHIP_NAME`: the membership name of the registered cluster to exempt namespaces on. You can specify multiple memberships separated by a comma.
  * `NAMESPACE_LIST`: a comma-separated list of namespaces that you want Policy Controller to exempt from enforcement.



### Namespaces to exempt from enforcement

The following list shows common system namespaces that you might want to exempt from enforcement to avoid unintended behavior like blocking upgrades. This list is not exhaustive:
    
    
    - anthos-creds
    - anthos-identity-service
    - apigee
    - apigee-system
    - asm-system
    - capi-kubeadm-bootstrap-system
    - capi-system
    - cert-manager
    - cnrm-system
    - config-management-monitoring
    - config-management-system
    - gke-connect
    - gke-gmp-system
    - gke-managed-cim
    - gke-managed-filestorecsi
    - gke-managed-metrics-server
    - gke-managed-system
    - gke-system
    - gmp-public
    - gmp-system
    - hnc-system
    - istio-system
    - kube-node-lease
    - kube-public
    - kube-system
    - poco-trial
    - resource-group-system
    - vm-system
    - krmapihosting-system
    - krmapihosting-monitoring
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
