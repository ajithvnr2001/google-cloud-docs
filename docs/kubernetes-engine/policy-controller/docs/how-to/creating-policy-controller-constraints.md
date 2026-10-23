---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints/
title: Use the constraint template library \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:55.049672+00:00
---

# Use the constraint template library  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Use the constraint template library Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to define [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) constraints by using the pre-existing constraint templates provided by Google.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and use templating of declarative configuration. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Policy Controller lets you enforce policy for a Kubernetes cluster by defining one or more constraint objects. After a constraint is installed, requests to the API server are checked against the constraint and are rejected if they don't comply. Pre-existing non-compliant resources are reported at audit time.

Every constraint is backed by a constraint template that defines the schema and logic of the constraint. Constraint templates can be sourced from Google and third parties, or you can write your own. For more information about creating new templates, see [Write a constraint template](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates).

## Before you begin

  * [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller).



## Examine the constraint template library

When you define a constraint, you specify the constraint template that it extends. A library of common constraint templates developed by Google is installed by default, and many organizations don't need to create custom constraint templates directly in Rego. Constraint templates provided by Google have the label `configmanagement.gke.io/configmanagement`.

To list constraints, use the following command:
    
    
    kubectl get constrainttemplates \
        -l="configmanagement.gke.io/configmanagement=config-management"
    

To describe a constraint template and check its required parameters, use the following command:
    
    
    kubectl describe constrainttemplate CONSTRAINT_TEMPLATE_NAME
    

You can also view [all constraint templates in the library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library).

## Define a constraint

You define a constraint by using YAML, and you don't need to understand or write Rego. Instead, a constraint invokes a constraint template and provides it with parameters specific to the constraint.

If you are using Config Sync with a [hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo), we recommend that you create your constraints in the `cluster/` directory.

Constraints have the following fields:

  * The lowercased `kind` matches the name of a constraint template.
  * The `metadata.name` is the name of the constraint.
  * The `match` field defines which objects the constraint applies to. All conditions specified must be matched before an object is in-scope for a constraint. `match` conditions are defined by the following sub-fields: 
    * `kinds` are the kinds of resources the constraint applies to, determined by two fields: `apiGroups` is a list of Kubernetes API groups that match and `kinds` is a list of kinds that match. "*" matches everything. If at least one `apiGroup` and one `kind` entry match, the `kinds` condition is satisfied.
    * `scope` accepts *, Cluster, or Namespaced, which determines if cluster-scoped or namespaced-scoped resources are selected (defaults to *).
    * `namespaces` is a list of namespace names the object can belong to. The object must belong to at least one of these namespaces. Namespace resources are treated as if they belong to themselves.
    * `excludedNamespaces` is a list of namespaces that the object cannot belong to.
    * `labelSelector` is a Kubernetes label selector that the object must satisfy.
    * `namespaceSelector` is a label selector on the namespace the object belongs to. If the namespace does not satisfy the object, it won't match. Namespace resources are treated as if they belong to themselves.
  * The `parameters` field defines the arguments for the constraint, based on what the constraint template expects.



The following constraint, called `ns-must-have-geo`, invokes a constraint template called `K8sRequiredLabels`, which is included in the constraint template library provided by Google. The constraint defines parameters that the constraint template uses to evaluate whether namespaces have the `geo` label set to some value.
    
    
    # ns-must-have-geo.yaml
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sRequiredLabels
    metadata:
      name: ns-must-have-geo
    spec:
      match:
        kinds:
          - apiGroups: [""]
            kinds: ["Namespace"]
      parameters:
        labels:
          - key: "geo"
    

To create the constraint, use `kubectl apply -f`:
    
    
    kubectl apply -f ns-must-have-geo.yaml
    

### Audit a constraint

If the constraint is configured and installed correctly, its `status.byPod[].enforced` field is set to `true`, whether the constraint is configured to enforce or only test the constraint.

Constraints are enforced by default, and a violation of a constraint prevents a given cluster operation. You can set a constraint's `spec.enforcementAction` to `dryrun` to report violations in the `status.violations` field without preventing the operation.

To learn more about auditing, see [Audit using constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints).

## Caveats when syncing constraints

If you're syncing your constraints to a centralized source, like a Git repository, with Config Sync or another GitOps-style tool, keep the following caveats in mind when syncing constraints.

### Eventual consistency

You can commit constraints to a source of truth like a Git repository, and can limit their effects using [ClusterSelectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#configure_a_subset_of_clusters) or [NamespaceSelectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors). Because syncing is _eventually_ consistent, keep the following caveats in mind:

  * If a cluster operation triggers a constraint whose NamespaceSelector refers to a namespace that hasn't been synced, the constraint is enforced and the operation is prevented. In other words, a missing namespace "fails closed."
  * If you change the labels of a namespace, the cache may contain outdated data for a brief time.



Minimize the need to rename a namespace or change its labels, and test constraints that impact a renamed or relabeled namespace to ensure they work as expected.

### Configure Policy Controller for referential constraints

Before you can enable referential constraints, you must create a configuration that tells Policy Controller what kinds of objects to watch, such as namespaces.

Save the following YAML manifest to a file, and apply it with `kubectl`. The manifest configures Policy Controller to watch namespaces and Ingresses. Create an entry with `group`, `version`, and `kind` under `spec.sync.syncOnly`, with the values for each type of object you want to watch.
    
    
    apiVersion: config.gatekeeper.sh/v1alpha1
    kind: Config
    metadata:
      name: config
      namespace: "gatekeeper-system"
    **spec :
      sync:
        syncOnly:
          - group: ""
            version: "v1"
            kind: "Namespace"
          - group: "extensions"
            version: "v1beta1"
            kind: "Ingress"**
    

## Enable referential constraints

**Note:** Before you enable referential constraints, you must create a configuration for the `gatekeeper-system` namespace.

A _referential constraint_ references another object in its definition. For example, you could create a constraint that requires Ingress objects in a cluster to have unique hostnames. The constraint is referential if its constraint template contains the string `data.inventory` in its Rego.

Referential constraints are enabled by default if you install Policy Controller using the Google Cloud console. If you install Policy Controller using the Google Cloud CLI, you can choose whether to enable referential constraints when you [Install Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller#installing). Referential constraints are only guaranteed to be eventually consistent, and this creates risks:

  * On an overloaded API server, the contents of Policy Controller's cache may become stale, causing a referential constraint to "fail open", meaning that the enforcement action appears to be working when it isn't. For example, you can create Ingresses with duplicate hostnames too quickly to allow the admission controller to detect the duplicates.

  * The order in which constraints are installed and the order in which the cache is updated are both random.




You can update an existing cluster to allow referential constraints.

### Console

To disable referential constraints, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. Expand the **Edit Policy Controller configuration** menu.
  4. Select the **Enable Constraint Templates that reference to objects other than the object currently being evaluated.** checkbox.
  5. Select **Save changes**.



### gcloud

To enable support for referential constraints, run the following command:
    
    
    gcloud container fleet policycontroller update \
        --memberships=MEMBERSHIP_NAME \
        --referential-rules
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to enable referential rules on. You can specify multiple memberships separated by a comma.

**Note:** If you have the template library enabled, enabling referential constraints adds additional templates. If you disable referential constraints, those templates are removed from the cluster along with any referential constraints that use them.

## Disable referential constraints

When you disable referential constraints, any templates that use referential constraints are also removed from the cluster, along with any constraints that use those templates.

### Console

Referential constraints are enabled by default when you install Policy Controller with the Google Cloud console. To disable referential constraints, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. Expand the **Edit Policy Controller configuration** menu.
  4. Clear the **Enable Constraint Templates that reference to objects other than the object currently being evaluated.** checkbox.
  5. Select **Save changes**.



### gcloud

To disable support for referential constraints, run the following command:
    
    
    gcloud container fleet policycontroller update \
        --memberships=MEMBERSHIP_NAME \
        --no-referential-rules
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to enable referential rules on. You can specify multiple memberships separated by a comma.

## List all constraints

To list all constraints installed on a cluster, use the following command:
    
    
    kubectl get constraint
    

You can also see an overview of your applied constraints in the Google Cloud console. For more information, see [Policy Controller metrics](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-status).

## Remove a constraint

To find all constraints that use a constraint template, use the following command to list all objects with the same `kind` as the constraint template's `metadata.name`:
    
    
    kubectl get CONSTRAINT_TEMPLATE_NAME
    

To remove a constraint, specify its `kind` and `name`:
    
    
    kubectl delete CONSTRAINT_TEMPLATE_NAME CONSTRAINT_NAME
    

When you remove a constraint, it stops being enforced as soon as the API server marks the constraint as deleted.

**Important:** Records of violations of the constraint are stored in the constraint's object as persisted in the cluster, and cannot be retrieved after the constraint is removed.

### Remove all constraint templates

**Note:** When you remove all constraint templates, all constraints that use those templates are also removed. Constraints must be backed by constraint templates.

### Console

To disable the constraint template library, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. In the **Add/Edit policy bundles** menu, toggle the template library and all policy bundles off _do_not_disturb_on_.
  4. Select **Save changes**.



### gcloud

To disable the constraint template library, run the following command:
    
    
    gcloud container fleet policycontroller content templates disable \
        --memberships=MEMBERSHIP_NAME
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to disable the constraint template library on. You can specify multiple memberships separated by a comma.

## Restore the constraint template library

### Console

To enable the constraint template library, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. In the **Add/Edit policy bundles** menu, toggle the template library on _check_circle_. You can also enable any or all of the policy bundles.
  4. Select **Save changes**.



### gcloud

To restore the constraint template library, run the following command:
    
    
    gcloud container fleet policycontroller content templates enable \
        --memberships=MEMBERSHIP_NAME
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to enable the constraint template library on. You can specify multiple memberships separated by a comma.

## What's next

  * Learn about [Policy Controller bundles](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/concepts/policy-controller-bundles).
  * View the [constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) reference documentation.
  * Learn how to [create custom constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates).
  * [Troubleshoot Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/troubleshoot-policy-controller).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
