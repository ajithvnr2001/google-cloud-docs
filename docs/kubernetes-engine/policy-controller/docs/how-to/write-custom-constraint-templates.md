---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates/
title: Write a custom constraint template \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:17.806242+00:00
---

# Write a custom constraint template  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Write a custom constraint template Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to write a custom constraint template and use it to extend [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) if you cannot find a [pre-written constraint template](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints) that suits your needs.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and use templating of declarative configuration. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Policy Controller policies are described by using the [OPA Constraint Framework](https://github.com/open-policy-agent/frameworks/tree/master/constraint) and are written in [Rego](https://www.openpolicyagent.org/docs/latest/language-reference/). A policy can evaluate any field of a Kubernetes object.

Writing policies using Rego is a specialized skill. For this reason, a [library of common constraint templates](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) is installed by default. You can likely invoke these constraint templates when creating constraints. If you have specialized needs, you can create your own constraint templates.

Constraint templates let you separate a policy's logic from its specific requirements, for reuse and delegation. You can create constraints by using constraint templates developed by third parties, such as open source projects, software vendors, or regulatory experts.

## Before you begin

  * Install [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller).



## Example constraint template

Following is an example constraint template that denies all resources whose name matches a value provided by the creator of the constraint. The rest of this page discusses the contents of the template, highlighting important concepts along the way.

If you are using Config Sync with a [hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo), we recommend that you create your constraints in the `cluster/` directory.
    
    
    apiVersion: templates.gatekeeper.sh/v1beta1
    kind: ConstraintTemplate
    metadata:
      name: k8sdenyname
    spec:
      crd:
        spec:
          names:
            kind: K8sDenyName
          validation:
            # Schema for the `parameters` field
            openAPIV3Schema:
              properties:
                invalidName:
                  type: string
      targets:
        - target: admission.k8s.gatekeeper.sh
          rego: |
            package k8sdenynames
            violation[{"msg": msg}] {
              input.review.object.metadata.name == input.parameters.invalidName
              msg := sprintf("The name %v is not allowed", [input.parameters.invalidName])
            }
    

### Example constraint

Following is an example constraint that you might implement to deny all resources named `policy-violation`:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sDenyName
    metadata:
      name: no-policy-violation
    spec:
      parameters:
        invalidName: "policy-violation"
    

## Parts of a constraint template

Constraint templates have two important pieces:

  * The _schema of the constraint_ that you want users to create. The schema of a constraint template is stored in the `crd` field.

  * The _Rego source code_ that is executed when the constraint is evaluated. The Rego source code for a template is stored in the `targets` field.




### Schema (`crd` field)

The CRD field is a blueprint for creating the [Kubernetes Custom Resource Definition](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions) that defines the constraint resource for the Kubernetes API server. You only need to populate the following fields.

Field | Description  
---|---  
`spec.crd.spec.names.kind` | The Kind of the constraint. When lower-cased, the value of this field must be equal to `metadata.name`.  
`spec.crd.spec.validation.openAPIV3Schema` | The schema for the `spec.parameters` field of the constraint resource (Policy Controller automatically defines the rest of the constraint's schema). It follows the same conventions as it would in a regular CRD resource.  
  
Prefixing the constraint template with the name `K8s` is a convention that lets you avoid collisions with other kinds of constraint templates, such as Forseti templates that target Google Cloud resources.

### Rego source code (`targets` field)

The following sections provide you with more information about the Rego source code.

#### Location

The Rego source code is stored under the `spec.targets` field, where `targets` is an array of objects of the following format:
    
    
    {"target": "admission.k8s.gatekeeper.sh","rego": REGO_SOURCE_CODE, "libs": LIST_OF_REGO_LIBRARIES}
    

  * `target`: tells Policy Controller what system we are looking at (in this case Kubernetes); only one entry in `targets` is allowed.
  * `rego`: the source code for the constraint.
  * `libs`: an optional list of libraries of Rego code that is made available to the constraint template; it is meant to make it easier to use shared libraries and is out of scope for this document.



#### Source code

Following is the Rego source code for the preceding constraint:
    
    
    package k8sdenynames
    
    violation[{"msg": msg}] {
       input.review.object.metadata.name == input.parameters.invalidName
       msg := sprintf("The name %v is not allowed", [input.parameters.invalidName])
    }
    

Note the following:

  * `package k8sdenynames` is required by OPA (Rego's runtime). The value is ignored.
  * The Rego rule that Policy Controller invokes to see if there are any violations is called `violation`. If this rule has matches, a violation of the constraint has occurred.
  * The `violation` rule has the signature `violation[{"msg": "violation message for the user"}]`, where the value of `"msg"` is the violation message that is returned to the user.
  * The parameters provided to the constraint are made available under the keyword `input.parameters`.
  * The `request-under-test` is stored under the keyword `input.review`.



The keyword `input.review` has the following fields.

Field | Description  
---|---  
`uid` | The unique ID for this particular request; it is not available during audit.  
`kind` | The Kind information for the `object-under-test`. It has the following format:

  * `kind`: the resource kind
  * `group`: the resource group
  * `version`: the resource version

  
`name` | The resource name. It might be empty if the user is relying on the API server to generate the name on a CREATE request.  
`namespace` | The resource namespace (not provided for cluster-scoped resources).  
`operation` | The operation requested (for example, CREATE or UPDATE); it is not available during audit.  
`userInfo` | The requesting user's information; it is not available during audit. It has the following format:

  * `username`: the user making the request
  * `uid`: the user's UID
  * `groups`: a list of groups that the user is a member of
  * `extra`: any extra user information provided by Kubernetes

  
`object` | The object that the user is attempting to modify or create.  
`oldObject` | The original state of the object; it is only available on UPDATE operations.  
`dryRun` | Whether this request was invoked with `kubectl --dry-run`; it is not available during audit.  
  
#### Write referential constraint templates

**Note:** If you didn't enable referential constraints when you installed Policy Controller, you must [enable referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential) first. Also take note of the [caveat about eventual consistency](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#eventual_consistency) and its implications for policy enforcement given as part of the instructions on how this feature can be enabled. Also note that for referential constraints to work, object syncing must be enabled for the resources being referenced.

Referential constraint templates are templates that let the user constrain one object with respect to other objects. An example of this might be "don't allow a Pod to be created before a matching Ingress is known to exist". Another example might be "do not allow two services to have the same hostname".

Policy Controller lets you write referential constraints by watching the API Server for a user-provided set of resources. When a resource is modified, Policy Controller caches it locally so that it can be easily referenced by Rego source code. Policy Controller makes this cache available under the `data.inventory` keyword.

**Cluster-scoped resources** are cached in the following location:
    
    
    data.inventory.cluster["GROUP_VERSION"]["KIND"]["NAME"]
    
    

For example, a Node named `my-favorite-node` could be found under

`data.inventory.cluster["v1"]["Node"]["my-favorite-node"]`

**Namespace-scoped resources** are cached here:
    
    
    data.inventory.namespace["NAMESPACE"]["GROUP_VERSION"]["KIND"]["NAME"]
    
    

For example, a ConfigMap named `production-variables` in the namespace `shipping-prod` could be found under

`data.inventory.namespace["shipping-prod"]["v1"]["ConfigMap"]["production-variables"]`

The full contents of the object are stored at this cache location and can be referenced in your Rego source code however you see fit.

#### More information about Rego

The preceding information provides the unique features of Policy Controller that make it easy to write constraints on Kubernetes resources in Rego. A full tutorial about how to write in Rego is out of scope for this guide. However, [Open Policy Agent's documentation](https://www.openpolicyagent.org/docs/latest/policy-language/) has information on the syntax and features of the Rego language itself.

## Install your constraint template

After you've created your constraint template, use `kubectl apply` to apply it, and Policy Controller takes care of ingesting it. Be sure to check the `status` field of your constraint template to make sure that there were no errors instantiating it. On successful ingestion, the `status` field should show `created: true` and the `observedGeneration` noted in the `status` field should equal the `metadata.generation` field.

After the template is ingested, you can apply constraints for it as described in [Creating constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints).

## Remove a constraint template

**Caution:** When you remove a constraint template that is in use by constraints, Policy Controller removes constraints that depend on that template.

To remove a constraint template, complete the following steps:

  1. Verify that no constraints that you want to preserve are using the constraint template:
         
         kubectl get TEMPLATE_NAME
         

If there's a naming conflict between the constraint template's name and a different object in the cluster, use the following command instead:
         
         kubectl get TEMPLATE_NAME.constraints.gatekeeper.sh
         

  2. Remove the constraint template:
         
         kubectl delete constrainttemplate CONSTRAINT_TEMPLATE_NAME
         




When you remove a constraint template, you can no longer create constraints that reference it.

## What's next

  * Learn more about [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview).
  * View the [constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library) reference documentation.
  * Learn how to [use constraints instead of PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-constraints-to-enforce-pod-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
