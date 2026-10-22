---
url: https://docs.cloud.google.com/deploy/docs/securing/sa-by-namespace/
title: Restrict deployment to a GKE namespace \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.246774+00:00
---

# Restrict deployment to a GKE namespace  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/securing/sa-by-namespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Restrict deployment to a GKE namespace Stay organized with collections  Save and categorize content based on your preferences. 

When you deploy to Google Kubernetes Engine (GKE), the default Cloud Deploy [execution service account](https://docs.cloud.google.com/deploy/docs/cloud-deploy-service-account#execution_service_account) has access to all namespaces in the target cluster. You can configure that service account to deploy to only one namespace.

**Note:** The instructions in this document are for deploying to GKE. If you're deploying to GKE attached clusters, see [Set up the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway/setup#configure_role-based_access_control_rbac_policies) for further instructions on setting up RBAC policies.

  1. Ensure that the execution service account doesn't have the `roles/container.developer` IAM role.

  2. Grant the service account the `roles/container.clusterViewer` role.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT" \
          --role="roles/container.clusterViewer"
         

This role allows the service account to authenticate on the cluster, but do nothing else.

  3. Create a Kubernetes RBAC Role that grants admin access to the namespace.

The RBAC role in this example has broad permissions, equivalent to the [`clouddeploy.developer` IAM role](https://docs.cloud.google.com/deploy/docs/iam-roles-permissions#predefined_roles). To minimize the risk of privilege escalation, we recommend you change these permissions to the minimum required for your applications. For instructions, see the [RBAC documentation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).
         
         kind: Role
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: admin
           namespace: NAMESPACE
         rules:
         - apiGroups: ["", "extensions", "apps"]
           resources: ["*"]
           verbs: ["*"]
         

  4. Create a `RoleBinding` that binds that RBAC Role in your chosen namespace to the Cloud Deploy execution service account:
         
         kind: RoleBinding
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: admin
           namespace: NAMESPACE
         subjects:
         # Google Cloud user account
         - kind: User
           name: SERVICE_ACCOUNT
         roleRef:
           kind: Role
           name: admin
           apiGroup: rbac.authorization.k8s.io
         

This manifest defines an RBAC policy binding the `admin` Role to your execution service account. `NAMESPACE` is the namespace for which you want to grant the service account access. The service account can't access any other namespace on the cluster.

  5. Apply the RBAC manifest to the cluster:
         
         kubectl apply -f YAML_NAME
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
