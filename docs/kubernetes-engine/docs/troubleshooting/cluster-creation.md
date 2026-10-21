---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-creation/
title: Troubleshoot cluster creation \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:34:18.750417+00:00
---

# Troubleshoot cluster creation  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot cluster creation Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Failures during Google Kubernetes Engine (GKE) cluster creation can prevent you from provisioning necessary infrastructure. A common cause for failures is a violation of the `constraints/compute.vmExternalIpAccess` policy. Use this page to help you troubleshoot and resolve cluster creation failures caused by this organization policy.

This information is important for Platform admins and operators or other users responsible for creating and managing GKE clusters within a Google Cloud organization. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For general issues with a Kubernetes cluster, see [Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/) in the Kubernetes documentation.

## Error: Constraint constraints/compute.vmExternalIpAccess violated

An error similar to the following can occur when you try to create a public GKE cluster:
    
    
    Constraint constraints/compute.vmExternalIpAccess violated for project
    

This only affects public GKE clusters, including GKE Autopilot clusters.

When you create public GKE clusters, the underlying Compute Engine VMs, which make up the worker nodes of this cluster, have [external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) assigned. If you configure the organization policy constraint [`constraints/compute.vmExternalIpAccess`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to `Deny All` or to restrict external IP addresses to specific VM instances at the organization, folder, or project level, then the policy prevents the GKE worker nodes from obtaining external IP addresses, which results in cluster creation failure.

To find the logs of the cluster creation operation, you can review the [GKE Cluster Operations Audit Logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/audit-logging) using [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) with a search query similar to the following:
    
    
    resource.type="gke_cluster"
    logName="projects/test-last-gke-sa/logs/cloudaudit.googleapis.com%2Factivity"
    protoPayload.methodName="google.container.v1beta1.ClusterManager.CreateCluster"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.project_id="PROJECT_ID"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster that wasn't created.
  * `PROJECT_ID`: your project ID.



To resolve this issue, ensure that the effective policy for the constraint `constraints/compute.vmExternalIpAccess` is `Allow All` on the project where you are trying to create a GKE public cluster. For information on working with this constraint, see [Restricting external IP addresses to specific VM instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#disableexternalip).

After setting the constraint to `Allow All`, delete the failed cluster and create a new cluster. This is required because repairing the failed cluster is not possible.

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
