---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/terminating-namespaces/
title: Troubleshoot namespace stuck in the Terminating state \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:32:02.714519+00:00
---

# Troubleshoot namespace stuck in the Terminating state  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/terminating-namespaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot namespace stuck in the Terminating state Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to resolve issues with a namespace stuck in the `Terminating` state.

Namespaces use Kubernetes [finalizers](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#finalizers) to prevent deletion if one or more resources within a namespace still exist. When you delete a namespace using the `kubectl delete` command, the namespace enters the `Terminating` state. The namespace stays in the `Terminating` state until Kubernetes deletes its dependent resources and clears all finalizers. The namespace lifecycle controller first lists all resources in the namespace that GKE needs to delete.

If GKE can't delete a dependent resource, or if the namespace lifecycle controller can't verify that the namespace is empty, then the namespace remains in the `Terminating` state until you resolve the issue.

To resolve a namespace stuck in the `Terminating` state, identify and remove any unhealthy components blocking the deletion. Try these solutions in order:

  1. Find and remove unavailable API services.
  2. Find and remove remaining resources.
  3. Force delete the namespace.



## Find and remove unavailable API services

  1. List unavailable API services:
         
         kubectl get apiservice | grep False
         

  2. Troubleshoot any unresponsive services:
         
         kubectl describe apiservice API_SERVICE
         

Replace `API_SERVICE` with the name of the unresponsive service.

  3. Check if the status of the namespace is still `Terminating`:
         
         kubectl get ns | grep Terminating
         




## Find and remove remaining resources

  1. List all the resources remaining in the terminating namespace:
         
         kubectl api-resources --verbs=list --namespaced -o name | xargs -n 1 kubectl get -n NAMESPACE
         

Replace `NAMESPACE` with the name of the namespace you want to delete.

  2. Remove any resources displayed in the output.

  3. Check if the status of the namespace is still `Terminating`:
         
         kubectl get ns | grep Terminating
         




## Force delete the namespace

**Caution:** Use the solution in this section only as a last resort if the previous solutions don't work. Force deleting a namespace could result in resources remaining in your cluster that you can't access.

Remove the finalizers blocking namespace deletion to force the namespace to terminate:

  1. Save the namespace manifest as a YAML file:
         
         kubectl get ns NAMESPACE -o yaml > ns-terminating.yml
         

  2. Open the manifest in a text editor and remove all values in the `spec.finalizers` field:
         
         vi ns-terminating.yml
         

  3. Verify that the finalizers field is empty:
         
         cat ns-terminating.yml
         

The output should look similar to the following:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           annotations:
           name: NAMESPACE
         spec:
           **finalizers :**
         status:
           phase: Terminating
         

  4. Start an HTTP proxy to access the Kubernetes API:
         
         kubectl proxy
         

  5. Replace the namespace manifest using `curl`:
         
         curl -H "Content-Type: application/yaml" -X PUT --data-binary @ns-terminating.yml http://127.0.0.1:8001/api/v1/namespaces/NAMESPACE/finalize
         

  6. Check if the status of the namespace is still `Terminating`:
         
         kubectl get ns | grep Terminating
         




## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
