---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/mutation/
title: Mutate resources \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:55.055879+00:00
---

# Mutate resources  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/mutation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Mutate resources Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to mutate resources using [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview). This is useful for doing things like setting default values. For example, you might want to inject a label for all resources in a specific namespace, or default a Pod's `imagePullPolicy` to `Always` if it's not already set.

## Enable mutation

**Note:** you cannot enable mutation on Autopilot clusters.

### Console

To enable mutation, complete the following steps:

  1. In the Google Cloud console, go to the **Policy** page under the **Posture Management** section. 

[Go to Policy](https://console.cloud.google.com/kubernetes/policy_controller)

  2. Under the **Settings** tab, in the cluster table, select **Edit** _edit_ in the **Edit configuration** column.
  3. Expand the **Edit Policy Controller configuration** menu.
  4. Select the **Enable mutation webhook** checkbox.
  5. Select **Save changes**.



### gcloud

To enable mutation, run the following command:
    
    
    gcloud container fleet policycontroller update \
        --memberships=MEMBERSHIP_NAME \
        --mutation
    

Replace `MEMBERSHIP_NAME` with the membership name of the registered cluster to enable mutation on. You can specify multiple memberships separated by a comma.

## Definitions

  * _mutator:_ A Kubernetes resource that helps configure the mutation behavior of Policy Controller.
  * _system:_ An arrangement of multiple mutators



## Mutation example

The following example shows a mutator that sets the `imagePullPolicy` for all containers in all Pods to `Always`:
    
    
    # set-image-pull-policy.yaml
    
    apiVersion: mutations.gatekeeper.sh/v1alpha1
    kind: Assign
    metadata:
      name: always-pull-image
    spec:
      applyTo:
      - groups: [""]
        kinds: ["Pod"]
        versions: ["v1"]
      location: "spec.containers[name: *].imagePullPolicy"
      parameters:
        assign:
          value: "Always"
    

In this example, there are the standard Kubernetes metadata fields (`apiVersion`, `kind`, `metadata.name`), but `spec` is where the mutator's behavior is configured.

`spec.applyTo` binds the mutator to the specified resources. Because we are changing specific fields in an object, we are implicitly defining that object's schema. For example, the current mutator would make no sense if it were applied to a `Namespace` resource. Because of this, this field is required so Policy Controller knows what schemas this mutator is relevant for. `GroupVersionKinds` missing from this list are not mutated.

`spec.location` is telling us which field to modify. In this case, we are using a glob (`*`) to indicate that we want to modify all entries in the container list. Note that the only kinds of lists that might be traversed by the `location` field are map-type lists, and the key field for the map must be specified. Map-type lists are a Kubernetes construct. More details about them can be found in Kubernetes' [documentation](https://kubernetes.io/docs/reference/using-api/server-side-apply/#merge-strategy).

`spec.parameters.assign.value` is the value to assign to `location`. This field is untyped and can take any value, though do note that Kubernetes still validates the request post-mutation, so inserting values with an incorrect schema for the object being modified results in the request being rejected.

### Use mutators for Jobs

If you are configuring a Job or CronJob, you must specify the version and group separately as shown in the following example:
    
    
    applyTo:
    - groups: ["batch"]
      kind: ["Job"]
      versions: ["v1"]
    

When you use a mutator for Jobs, the existing Jobs aren't mutated unless they are modified. Modifying a Job triggers a request to the mutation webhook and causes it to be mutated.

## Execution flow

Perhaps the most important concept to understand about Kubernetes mutation webhooks is their [reinvocation policy](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#reinvocation-policy), because the output of one mutator might change how another mutator behaves. For instance, if you add a new sidecar container, a mutator that sets the image pull policy for all containers now has a new container to mutate.

Practically, what this means is that for any given request Policy Controller's mutation webhook might be called more than one time.

In order to reduce latency, Policy Controller reinvokes itself to avoid additional HTTP requests. This means that sidecar injection and image pull policy have the expected result.

Policy Controller's mutation routine will continue to reinvoke itself until the resource "converges", which means additional iterations have no further effect.

## Location syntax

The location syntax uses the dot (`.`) accessor to traverse fields. In the case of keyed lists, users can reference individual objects in a list using the syntax `[<key>: <value>]`, or all objects in the list using `[<key>: *]`.

Values and fields can be quoted with either single (`'`) or double (`"`) quotes. This is necessary when they have special characters, like dots or spaces.

In quoted values, special characters can be escaped by prefixing them with `\`. `"Use \" to escape and \\\" to escape"` turns into `Use " to escape and \" to escape`.

Some examples for the `v1/Pod` resource:

  * `spec.priority` references `spec.priority`
  * `spec.containers[name: "foo"].volumeMounts[mountPath: "/my/mount"].readOnly` references the `readOnly` field of the `/my/mount` mount of the `foo` container.
  * `spec.containers[name: *].volumeMounts[mountPath: "/my/mount"].readOnly` references the `readOnly` field of the `/my/mount` mount of all containers.



If you reference a location that doesn't currently exist on a resource, that location is created by default. This behavior can be configured via path testing.

## Path testing

How can we perform defaulting, where we avoid modifying a value that already exists? Maybe we want to set `/secure-mount` to read-only for all containers, but we don't want to create a `/secure-mount` if one doesn't already exist. We can do either of these things via path testing.

Here is an example that avoids mutating `imagePullPolicy` if it's already set:
    
    
    # set-image-pull-policy.yaml
    
    apiVersion: mutations.gatekeeper.sh/v1alpha1
    kind: Assign
    metadata:
      name: always-pull-image
    spec:
      applyTo:
      - groups: [""]
        kinds: ["Pod"]
        versions: ["v1"]
      location: "spec.containers[name: *].imagePullPolicy"
      parameters:
        assign:
          value: "Always"
        pathTests:
        - subPath: "spec.containers[name: *].imagePullPolicy"
          condition: "MustNotExist"
    

Here is another example that avoids creating an empty `sidecar` container if it doesn't already exist:
    
    
    # set-image-pull-policy.yaml
    
    apiVersion: mutations.gatekeeper.sh/v1alpha1
    kind: Assign
    metadata:
      name: always-pull-image
    spec:
      applyTo:
      - groups: [""]
        kinds: ["Pod"]
        versions: ["v1"]
      location: 'spec.containers[name: "sidecar"].imagePullPolicy'
      parameters:
        assign:
          value: "Always"
        pathTests:
        - subPath: 'spec.containers[name: "sidecar"]'
          condition: "MustExist"
    

Multiple path tests can be specified, if necessary.

`subPath` _must_ be a prefix of (or equal to) `location`.

The only valid values for `condition` are `MustExist` and `MustNotExist`.

## Matching

Mutators also allow for matching, using the same criteria as [constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#constraint).

## Mutators

Currently there are two kinds of mutators: `Assign` and `AssignMetadata`.

### Assign

`Assign` can change any value outside of the `metadata` field of a resource. Because all `GroupVersionKinds` have a unique schema, it must be bound to a set of particular `GroupVersionKinds`.

It has the following schema:
    
    
    apiVersion: mutations.gatekeeper.sh/v1alpha1
    kind: Assign
    metadata:
      name: always-pull-image
    spec:
      applyTo:
      - groups: [""]
        kinds: ["Pod"]
        versions: ["v1"]
      match:
        kinds: # redundant because of `applyTo`, but left in for consistency
          - apiGroups: ["*"]
            kinds: ["*"]
        namespaces: ["my-namespace"]
        scope: "Namespaced" # or "Cluster"
        excludedNamespaces: ["some-other-ns"]
        labelSelector:
          matchLabels:
            mutate: "yes"
          matchExpressions:
          - key: "my-label"
            operator: "In" # or, "NotIn", "Exists", or "DoesNotExist"
            values: ["my-value"]
        namespaceSelector:
          matchLabels:
            mutate: "yes"
          matchExpressions:
          - key: "my-label"
            operator: "In" # or, "NotIn", "Exists", or "DoesNotExist"
            values: ["my-value"]
      location: "spec.containers[name: *].imagePullPolicy"
      parameters:
        pathTests:
        - subPath: 'spec.containers[name: "sidecar"]' # must be a prefix of `location`
          condition: "MustExist" # or "MustNotExist"
        - subPath: "spec.containers[name: *].imagePullPolicy"
          condition: "MustNotExist"
        assign:
          value: "Always" # any type can go here, not just a string
    

### AssignMetadata

`AssignMetadata` can add new metadata labels. It cannot change the value of existing metadata labels. Otherwise, it would be possible to write a system of mutators that would recurse indefinitely, causing requests to time out.

Because all resources share the same `metadata` schema, there is no need to specify which resource an `AssignMetadata` applies to.

Also, because `AssignMetadata` isn't allowed to do as much, its schema is a bit simpler.
    
    
    apiVersion: mutations.gatekeeper.sh/v1alpha1
    kind: AssignMetadata
    metadata:
      name: set-team-name
    spec:
      match:
        kinds:
          - apiGroups: ["*"]
            kinds: ["*"]
        namespaces: ["my-namespace"]
        scope: "Namespaced" # or "Cluster"
        excludedNamespaces: ["some-other-ns"]
        labelSelector:
          matchLabels:
            mutate: "yes"
          matchExpressions:
          - key: "my-label"
            operator: "In" # or, "NotIn", "Exists", or "DoesNotExist"
            values: ["my-value"]
        namespaceSelector:
          matchLabels:
            mutate: "yes"
          matchExpressions:
          - key: "my-label"
            operator: "In" # or, "NotIn", "Exists", or "DoesNotExist"
            values: ["my-value"]
      location: "metadata.labels.team" # must start with `metadata.labels`
      parameters:
        assign:
          value: "Always" # any type can go here, not just a string
    

## Best practices

### Kubernetes caveats

The Kubernetes documentation lists some [important considerations](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#use-caution-when-authoring-and-installing-mutating-webhooks) around using mutation webhooks. Because Policy Controller operates as a Kubernetes admission webhook, that advice applies here.

Policy Controller's mutation syntax is designed to make it easier to comply with [operational concerns](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#best-practices-and-warnings) around mutation webhooks, including idempotence.

### Write mutators

#### Atomicity

It is best practice to make each mutator as self-sufficient as possible. Because Kubernetes is eventually consistent, one mutator should not rely on a second mutator to have been recognized in order to do its job properly. For example, when adding a sidecar, add the whole sidecar, do not construct it piecemeal using multiple mutators.

#### Validation

If there is a condition that you want to enforce, it is a good idea for the mutator to have a matching constraint. This helps make sure violating requests get rejected and pre-existing violations are detected in audit.

## Emergency recovery

Mutation is implemented as a Kubernetes mutating webhook. It can be stopped in the same manner as [the validating webhook](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/stopping-policy-controller), but the relevant resource is a `MutatingWebhookConfiguration` called `gatekeeper-mutating-webhook-configuration`.

## What's next

  * For Gatekeeper mutation explanations and examples, see the [open source documentation](https://open-policy-agent.github.io/gatekeeper/website/docs/mutation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
