---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vertical-pod-autoscaling/
title: Troubleshoot vertical Pod autoscaling \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:10.753426+00:00
---

# Troubleshoot vertical Pod autoscaling  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/vertical-pod-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot vertical Pod autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

When vertical Pod autoscaling doesn't function as expected in Google Kubernetes Engine (GKE), your workloads might not scale correctly. These issues can prevent applications from handling load, which might cause performance issues or outages. You might see Pods not restarting with new resource recommendations, or recommendations that don't match actual usage.

Use this document to resolve common issues with VerticalPodAutoscaler configuration or unexpected recommendations. Following these troubleshooting steps can help your applications scale efficiently and reliably based on demand.

This information is important for Application developers who configure VerticalPodAutoscaler resources and need to ensure that their applications scale correctly. It also helps Platform admins and operators to troubleshoot issues with cluster configuration that affect autoscaled workloads. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Diagnose VerticalPodAutoscaler issues

To diagnose issues with a VerticalPodAutoscaler, inspect the status and configuration by using `kubectl` or the Google Cloud console.

### Describe the VerticalPodAutoscaler

To view real-time calculations and recent scaling decisions, use the `kubectl describe vpa` command:
    
    
    kubectl describe vpa VPA_NAME -n NAMESPACE_NAME
    

Replace the following:

  * `VPA_NAME`: the name of your VerticalPodAutoscaler.
  * `NAMESPACE_NAME`: the namespace of your VerticalPodAutoscaler.



The output is similar to the following:
    
    
    Name:         sample-deployment-vpa
    Namespace:    default
    API Version:  autoscaling.k8s.io/v1
    Kind:         VerticalPodAutoscaler
    # Multiple lines are omitted here
    Spec:
      Target Ref:
        API Version:  apps/v1
        Kind:         Deployment
        Name:         sample-deployment
      Update Policy:
        Update Mode:  Auto
    Status:
      Conditions:
        Last Transition Time:  2025-10-09T10:00:00Z
        Message:               VPA is fetching history in order to provide recommendation
        Reason:                FetchingHistory
        Status:                True
        Type:                  FetchingHistory
        Last Transition Time:  2025-10-09T10:05:00Z
        Message:               VPA pod metrics aren't available yet
        Reason:                NoMetrics
        Status:                True
        Type:                  LowConfidence
        Last Transition Time:  2025-10-09T10:10:00Z
        Message:               VPA is able to provide a recommendation
        Reason:                RecommendationProvided
        Status:                True
        Type:                  RecommendationProvided
      Recommendation:
        Container Recommendations:
          Container Name:  sample-container
          Lower Bound:
            Cpu:     100m
            Memory:  128Mi
          Target:
            Cpu:     200m
            Memory:  256Mi
          Upper Bound:
            Cpu:     500m
            Memory:  512Mi
    Events:          <none>
    

In the output, review these main sections:

  * **`Spec`** : shows configuration details, including the `targetRef` field (the targeted workload) and the `updatePolicy` field (how updates are applied).
  * **`Status`** : shows the `Conditions` section (operational health) and `Recommendation` section (CPU and memory resource values generated for each container).
  * **`Events`** : lists recent actions or errors related to the VerticalPodAutoscaler object.



### View the VerticalPodAutoscaler manifest

To view the complete configuration and state of a VerticalPodAutoscaler, inspect its YAML manifest by using `kubectl` or the Google Cloud console:

### Console

  1. In the Google Cloud console, go to the **Object Browser** page.

[Go to Object Browser](https://console.cloud.google.com/kubernetes/object/browser)

  2. Click the **Object Kind** filters list.

  3. Clear any existing selections.

  4. Select **VerticalPodAutoscaler** and click **OK**.

  5. In the filtered list, select the **autoscaling.k8s.io** API group.

  6. Select the **VerticalPodAutoscaler** object kind.

  7. Click the name of the VerticalPodAutoscaler that you want to inspect.




### kubectl
    
    
    kubectl get vpa VPA_NAME \
        -n NAMESPACE_NAME \
        -o yaml
    

Replace the following:

  * `VPA_NAME`: the name of your VerticalPodAutoscaler.
  * `NAMESPACE_NAME`: the namespace of your VerticalPodAutoscaler.



### Check VerticalPodAutoscaler status in Google Cloud console

To inspect VerticalPodAutoscaler status for your workloads in the Google Cloud console:

  1. Go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click the name of your workload.

  3. Go to the **Details** tab and locate the **Autoscaler** section.

  4. Review the **Vertical Pod Autoscaler** row for status messages regarding metric collection and configuration health.




### Collect decision logs

For detailed insights into VerticalPodAutoscaler calculations and decisions, enable **vertical Pod autoscaler decision logs** (Preview) in Cloud Logging.

These logs capture events such as `UPDATE_RECOMMENDATION`, `EVICT_POD`, `APPLY_RECOMMENDATION_IN_PLACE`, and `APPLY_RECOMMENDATION_ON_EVICTION`.

To enable and inspect decision logs, see [Collect vertical Pod autoscaler event logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-vertical-pod-autoscaling-events).

## Troubleshoot VerticalPodAutoscaler recommendations

The following sections address issues where a VerticalPodAutoscaler fails to produce recommendations or generates recommendations that differ from expectations.

### A VerticalPodAutoscaler isn't providing recommendations

**Symptoms** :

  * The `Status.Recommendation` field in the VerticalPodAutoscaler manifest is empty.
  * Conditions in the VerticalPodAutoscaler manifest show the `NoPodsMatched`, `FetchingHistory`, or `LowConfidence` status conditions.



**Cause** :

  * **Incorrect target** : the `spec.targetRef` field in the VerticalPodAutoscaler manifest doesn't point to an existing workload in the same namespace.
  * **Initial metric collection** : the VerticalPodAutoscaler was recently created and is still gathering historical resource usage data.
  * **`metrics-server` component issues**: The VerticalPodAutoscaler relies on metrics from the `metrics-server` component. If the `metrics-server` component isn't functioning correctly, the VerticalPodAutoscaler cannot retrieve usage data.
  * **No running Pods** : the target workload has no running or ready Pods for the VerticalPodAutoscaler to observe.



**Resolution** :

  * **Verify the`targetRef` field**: check the values for the `kind`, `name`, and `apiVersion` fields in the `spec.targetRef` section. Ensure that all values match the target workload. To confirm that the workload exists, run:
        
        kubectl get KIND WORKLOAD_NAME \
            -n NAMESPACE_NAME
        

Replace the following:

    * `KIND`: the workload type, for example, `deployment` or `statefulset`.
    * `WORKLOAD_NAME`: the name of your workload.
    * `NAMESPACE_NAME`: the namespace of your workload.
  * **Allow time for metric collection** : new VerticalPodAutoscaler resources require time to collect data. Monitor the `Status.Conditions` field for a transition to the `RecommendationProvided` status condition.

  * **Check the`metrics-server` component**:

    1. Verify that the Pod for the `metrics-server` component is running:
           
           kubectl get pods -n kube-system | grep metrics-server
           

    2. If the Pod isn't running or has a high restart count, check its logs:
           
           kubectl logs -n kube-system -l k8s-app=metrics-server
           

Log entries containing words such as `error`, `failed`, or `unable to fetch` indicate issues with metric collection.

  * **Ensure Pods are running** : verify that the target workload has at least one running and ready Pod.




### VerticalPodAutoscaler recommendations are unexpected

**Symptoms** :

  * The CPU or memory values in the `Status.Recommendation` section are higher or lower than expected.
  * Recommendations don't align with observed workload resource consumption.



**Cause** :

  * **Workload behavior changes** : VerticalPodAutoscaler recommendations are based on historical usage. Recent shifts in application consumption patterns might not yet be reflected.
  * **Workload characteristics** : short-lived jobs or workloads with highly spiky usage patterns might not receive optimal recommendations.
  * **Conflicting VerticalPodAutoscaler resources** : multiple VerticalPodAutoscaler resources might be configured to target the same workload.



**Resolution** :

  * **Allow adjustment time** : give the VerticalPodAutoscaler time to learn new usage patterns after application changes.
  * **Evaluate suitability** : assess whether a VerticalPodAutoscaler or a Horizontal Pod Autoscaler is best suited for the workload type.
  * **Check for conflicting VerticalPodAutoscaler resources** :

    1. List all VerticalPodAutoscaler resources in your cluster:
           
           kubectl get vpa --all-namespaces
           

    2. Examine the `spec.targetRef` field for each resource. If multiple VerticalPodAutoscaler resources target the same workload, remove or adjust the conflicting resources so that only one VerticalPodAutoscaler targets a given workload.




## Troubleshoot Pod resource updates

The following sections address issues where recommendations exist but are not applied to target Pods.

### Pod resource requests aren't updated

**Symptoms** :

  * The VerticalPodAutoscaler manifest shows recommendations in the `Status` section, but the `resources.requests` field in the Pod manifest isn't updated.
  * Pods aren't restarting to apply recommendations when using the `Auto` or `Recreate` update mode.



**Cause** :

  * **The`updateMode` field is `Off`**: when the `spec.updatePolicy.updateMode` field is set to `Off`, the VerticalPodAutoscaler generates recommendations but does not apply them.
  * **Workload has only one replica** : in the `Auto` or `Recreate` update mode, the VerticalPodAutoscaler avoids evicting single-replica workloads to prevent downtime.



**Resolution** :

  * **Check the`updateMode` field**: modify the VerticalPodAutoscaler manifest to set the `spec.updatePolicy.updateMode` field to `Auto`, `Recreate`, or `InPlaceOrRecreate`.
  * **Increase replica count** : for workloads using the `Auto` or `Recreate` update mode, ensure that the Deployment or StatefulSet has more than one replica.



### In-place updates fail or remain deferred

**Symptoms** :

  * In-place container resizing fails to complete or remains deferred.



**Cause** :

  * **Insufficient node capacity** : if the node lacks capacity for the updated resource requests, the in-place resize operation is deferred.



**Resolution** :

  * **Verify deferred resize status and node capacity** :

If the resize remains deferred for more than five minutes, the VerticalPodAutoscaler falls back to evicting and re-creating the Pod to apply the recommendation. To check the status of the deferred update, do the following:

    1. Inspect the Pod annotations to check if the `vpaInPlaceUpdated` annotation is set to `"true"`:
           
           metadata:
             annotations:
               vpaInPlaceUpdated: "true"
               vpaUpdates: 'Pod resources updated by sample-deployment-vpa: container 0: cpu request, memory request'
           

    2. Check the deferred status by inspecting the `status.conditions` field for deferred resize events:
           
           status:
             conditions:
             - type: PodResizePending
               status: "True"
               reason: Deferred
               message: "Node didn't have enough resource: ..."
           

    3. Inspect the Kubernetes events for the Pod:
           
           kubectl get events -n NAMESPACE_NAME --field-selector involvedObject.kind=Pod,involvedObject.name=POD_NAME
           

Replace the following:

       * `NAMESPACE_NAME`: the namespace of your Pod.
       * `POD_NAME`: the name of your Pod.

Look for events with either of the following reasons: `ResizedPod` (successful in-place update) or `EvictedByVPA` (fallback to re-creation).




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
