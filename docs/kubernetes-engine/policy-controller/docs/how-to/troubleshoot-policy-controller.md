---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/troubleshoot-policy-controller/
title: Troubleshoot Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:41.387292+00:00
---

# Troubleshoot Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/troubleshoot-policy-controller/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Troubleshoot Policy Controller Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Policy Controller.

## General tips

The following section provides general advice for resolving issues with Policy Controller.

### Stop Policy Controller

If Policy Controller is causing issues in your cluster, you can [stop Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/stopping-policy-controller) while you investigate the issue.

### Examine metrics

[Examining the Policy Controller metrics](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-metrics) can help you to diagnose issues with Policy Controller.

### Verify installation

You can [verify](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller#verifying) if Policy Controller and the constraint template library were installed successfully.

### Detach Policy Controller

In rare cases, you might need to detach Policy Controller from your clusters. This fully disables management of Policy Controller. Try [temporarily stopping Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/stopping-policy-controller) to see if you can resolve issues before using the `detach` command.

**Warning:** This command should only be used in an emergency situation. Don't leave your clusters in a detached state for an extended period of time. If you're experiencing a serious issue with your clusters, reach out to [Google Cloud Support](https://docs.cloud.google.com/support/docs) to report and resolve the issue with the managed control plane so you can reattach your cluster.

  1. Detach Policy Controller across your fleet:
         
         gcloud container fleet policycontroller detach
         

  2. Re-attach Policy Controller:
         
         gcloud container fleet policycontroller enable
         




## Error creating a constraint template

If you see an error that mentions a `disallowed ref`, confirm you enabled referential constraints. For example, if you use `data.inventory` in a constraint template without [enabling referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential) first, the error is similar to the following:
    
    
    admission webhook "validation.gatekeeper.sh" denied the request: check refs failed on module {templates["admission.k8s.gatekeeper.sh"]["MyTemplate"]}: disallowed ref data.inventory...
    

## Constraint not enforced

The following section provides troubleshooting guidance if you suspect or know your constraints aren't being enforced.

### Check if your constraint is enforced

If you're concerned that your constraint is not enforced, you can check the `spec.status` of your constraint and the constraint template. To check the status, run the following command:
    
    
    kubectl describe CONSTRAINT_TEMPLATE_NAME CONSTRAINT_NAME
    

Replace the following:

  * `CONSTRAINT_TEMPLATE_NAME`: the name of the constraint template that you want to check. For example, `K8sNoExternalServices`.
  * `CONSTRAINT_NAME`: the `Name` of the constraint that you want to check.

If needed, run `kubectl get constraint` to see which constraint templates and constraints are installed on your system.




In the output of the `kubectl describe` command, take note the values in the `metadata.generation` and `status.byPod.observedGeneration` fields. In the following example these values are bolded:
    
    
    Name:         no-internet-services
    Namespace:
    API Version:  constraints.gatekeeper.sh/v1beta1
    Kind:         K8sNoExternalServices
    Metadata:
      Creation Timestamp:  2021-12-03T19:00:06Z
      **Generation:          1**
      Managed Fields:
        API Version:  constraints.gatekeeper.sh/v1beta1
        Fields Type:  FieldsV1
        fieldsV1:
          f:metadata:
            f:annotations:
              f:config.k8s.io/owning-inventory:
              f:configmanagement.gke.io/cluster-name:
              f:configmanagement.gke.io/managed:
              f:configmanagement.gke.io/source-path:
              f:configmanagement.gke.io/token:
              f:configsync.gke.io/declared-fields:
              f:configsync.gke.io/git-context:
              f:configsync.gke.io/manager:
              f:configsync.gke.io/resource-id:
            f:labels:
              f:app.kubernetes.io/managed-by:
              f:configsync.gke.io/declared-version:
          f:spec:
            f:parameters:
              f:internalCIDRs:
        Manager:      configsync.gke.io
        Operation:    Apply
        Time:         2022-02-15T17:13:20Z
        API Version:  constraints.gatekeeper.sh/v1beta1
        Fields Type:  FieldsV1
        fieldsV1:
          f:status:
        Manager:         gatekeeper
        Operation:       Update
        Time:            2021-12-03T19:00:08Z
      Resource Version:  41460953
      UID:               ac80849d-a644-4c5c-8787-f73e90b2c988
    Spec:
      Parameters:
        Internal CID Rs:
    Status:
      Audit Timestamp:  2022-02-15T17:21:51Z
      By Pod:
        Constraint UID:       ac80849d-a644-4c5c-8787-f73e90b2c988
        Enforced:             true
        Id:                   gatekeeper-audit-5d4d474f95-746x4
        **Observed Generation:  1**
        Operations:
          audit
          status
        Constraint UID:       ac80849d-a644-4c5c-8787-f73e90b2c988
        Enforced:             true
        Id:                   gatekeeper-controller-manager-76d777ddb8-g24dh
        **Observed Generation:  1**
        Operations:
          webhook
      Total Violations:  0
    Events:              <none>
    

If you see every Policy Controller Pod with an `observedGeneration` value equal to the `metadata.generation` value (which is the case in the preceding example), then your constraint is likely enforced. However, if these values match, but you are still experiencing problems with your constraint being enforced, see the following section for tips. If you notice that there are only some values that match, or some Pods aren't listed, then the status of your constraint is unknown. The constraint might be inconsistently enforced across Policy Controller's Pods, or not enforced at all. If there are no values that match, then your constraint is not enforced.

### Constraint not enforced, but audit results reported

If the `observedGeneration` check described in the preceding section had matching values and there are [audit results](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints) reported on the constraint that show expected violations (for pre-existing objects, not for inbound requests), but the constraint is still not enforced then the problem is likely to do with the webhook. The webhook might be experiencing one of the following issues:

  * The Policy Controller webhook Pod might not be operational. [Kubernetes debugging techniques](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/) might help you to resolve issues with the webhook Pod.
  * There could be a firewall between the API server and the webhook service. Refer to your firewall provider's documentation for details on how to fix the firewall.



### Referential constraint not enforced

If your constraint is a [referential constraint](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#referential), make sure the necessary resources are being cached. For details on how to cache resources, see [Configure Policy Controller for referential constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints#gatekeeper-config).

### Check the constraint template syntax

If you [wrote your own constraint template](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/write-custom-constraint-templates), and it's not enforced, there might be an error in the constraint template syntax.

You can review the template by using the following command:
    
    
    kubectl describe constrainttemplate CONSTRAINT_TEMPLATE_NAME
    

Replace `CONSTRAINT_TEMPLATE_NAME` with the name of the template that you want to investigate. Errors should be reported in the `status` field.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/get-support-policy-controller) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub)

    * Opening bugs or feature requests by using the [public Google Cloud issue tracker](https://issuetracker.google.com/issues/new?component=1161523) or [opening a public bug for Gatekeeper](https://github.com/open-policy-agent/gatekeeper/issues) on GitHub.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
