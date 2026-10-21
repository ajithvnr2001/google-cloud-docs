---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-google-groups/
title: Connect Google groups to GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:53.047314+00:00
---

# Connect Google groups to GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-google-groups/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect Google groups to GKE on Azure

This document describes how you can connect to GKE on Azure as a member of a [Google group](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console).

Using Google groups to grant cluster access is more efficient than creating separate authorizations for individual users. For example, let's say you want to add 50 users to the cluster Administrator group, 75 users to an Editor group, and 100 users to a Reader group. Enabling all these users to connect to your cluster would require you to create RBAC rules in the Kubernetes manifest file for 225 users. Enabling access to your cluster with Google groups, however saves you time because you only need to create RBAC rules for three Google groups.

## Before you begin

To connect to your cluster as a member of a Google group, you need to satisfy the following prerequisites:

  1. Ensure that you have the latest version of the Google Cloud CLI. For information on updating gcloud CLI, see [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update).

  2. Use GKE on Azure version 1.25 or above, which is required for `kubectl` access using connect gateway.




## Connect to your cluster with Google groups

To authorize Google groups to connect to GKE on Azure, follow these steps:

  1. Enable the `connectgateway` and `cloudresourcemanager` APIs with the following command:
         
         gcloud services enable --project=PROJECT_ID \
               connectgateway.googleapis.com \
               cloudresourcemanager.googleapis.com
         

Replace `PROJECT_ID` with the ID of your Azure project.

  2. Create a group called `gke-security-groups` as a group in your project's domain if it doesn't exist.

  3. Create one or more sub-groups within the `gke-security-groups` group for cluster authentication.

  4. Add users to the newly created sub-groups.

  5. For `kubectl` access using connect gateway, you need to grant IAM roles to Google groups:

     1. Select an appropriate role for a group. This role determines how the group interacts with the connect gateway. The role can be one of the following: `roles/gkehub.gatewayAdmin`, `roles/gkehub.gatewayEditor`, `roles/gkehub.gatewayReader`. (Note that you're not granting permissions over the cluster here - that step comes later. Here, you're just determining how users of the group can manipulate the connect gateway.)

     2. Run the following command to grant the role to the group:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
              --member=group:GROUP_NAME@DOMAIN \
              --role=GATEWAY_ROLE
            

Replace the following:

        * `PROJECT_ID`: your Google project ID
        * `GROUP_NAME`: the name of the group to grant access to
        * `DOMAIN`: your Google Workspace domain
        * `GATEWAY_ROLE`: the selected role. For example `roles/gkehub.gatewayAdmin`, `roles/gkehub.gatewayEditor`, or `roles/gkehub.gatewayReader`.
**Note:** To grant `kubectl` access through a private endpoint, follow the preceding steps, but grant `roles/gkemulticloud.viewer` to the Google groups instead.
  6. In a Kubernetes manifest, define the permissions each Google group has on the cluster. For example, the following manifest grants the Google Group `cluster-admin-team` the role of cluster administrator:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: gateway-cluster-admin-group
         subjects:
         - kind: Group
           name: cluster-admin-team@example.com
         roleRef:
           kind: ClusterRole
           name: cluster-admin
           apiGroup: rbac.authorization.k8s.io
         

  7. Save the manifest to a file and apply it to the cluster by running the following command:
         
         kubectl apply -kubeconfig=KUBECONFIG_PATH -f FILENAME
         

Replace the following:

     * `KUBECONFIG_PATH`: the path to your `kubeconfig` file.
     * `FILENAME`: the name of the manifest file you created.



Once you've performed these steps, users belonging to certain Google groups can connect to the cluster. In the given example, users belonging to the Google group `cluster-admin-team` can connect to the cluster as administrators.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
