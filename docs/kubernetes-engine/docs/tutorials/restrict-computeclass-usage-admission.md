---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/restrict-computeclass-usage-admission/
title: Restrict access to modify and select ComputeClasses \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:10.184125+00:00
---

# Restrict access to modify and select ComputeClasses  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/restrict-computeclass-usage-admission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Restrict access to modify and select ComputeClasses Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can use Google Kubernetes Engine (GKE) [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes) to create nodes that meet various workload requirements. Pods can use ComputeClasses to create hardware. Depending on the ComputeClass, that hardware might be in-demand, limited in availability, or relatively expensive for your enterprise. This tutorial shows you how to use Kubernetes RBAC and [ValidatingAdmissionPolicies](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) to restrict the creation, deletion, modification, and selection of ComputeClasses.

These restrictions can help you to prevent situations like the following:

  * Pods that don't need specialized hardware like GPUs or TPUs select ComputeClasses that request that hardware.
  * An unauthorized entity creates or modifies ComputeClasses to get access to hardware that's reserved for critical workloads.



This document uses an example ValidatingAdmissionPolicy that blocks common types of misuse, such as wildcard ComputeClass tolerations or the selection of specific disallowed ComputeClasses. You can modify the ValidatingAdmissionPolicy to meet requirements that are specific to your organization, such as blocking workloads from certain teams from using ComputeClasses.

## Objectives

  * Use a ValidatingAdmissionPolicy to limit the ComputeClasses that Pods can select in each namespace to an approved list.
  * Use role-based access control (RBAC) to restrict who can create, modify, or delete ComputeClasses in your clusters.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Google Workspace](https://workspace.google.com/pricing) or [Cloud Identity](https://cloud.google.com/identity/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Kubernetes Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Kubernetes Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  16. If you use a local shell, install the `kubectl` component: 
         
         gcloud components install kubectl

  17. Ensure that you have a GKE cluster that uses version 1.30 or later. You can also [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version) for this tutorial.
  18. Configure your cluster for Google Groups for RBAC: 
     1. Set up the `gke-security-groups` group in your domain.
     2. Enable Google Groups for RBAC in your cluster.

For more information, see [Set up your Google Groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac#setup-group).




### Required roles

To get the permissions that you need to create RBAC policies and Kubernetes objects in your cluster, ask your administrator to grant you the Kubernetes Engine Admin (`role/container.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare the environment

To prepare your cluster for the creation and verification tasks in this tutorial, follow these steps:

  1. Connect to your cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the [region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the cluster control plane, such as `us-central1` or `us-central1-a`.
  2. Create a namespace to use for this tutorial. You can also use any existing namespace in the cluster.
         
         kubectl create namespace computeclass-vap-tutorial
         

  3. Create an RBAC policy that grants access to manage ValidatingAdmissionPolicies and ValidatingAdmissionPolicyBindings:

     1. Save the following manifest as `validatingadmissionpolicy-editor.yaml`:
            
            apiVersion: rbac.authorization.k8s.io/v1
            kind: ClusterRole
            metadata:
              name: validatingadmissionpolicy-editor
            rules:
            - apiGroups: ["admissionregistration.k8s.io"]
              resources: ["validatingadmissionpolicies","validatingadmissionpolicybindings"]
              verbs: ["get", "list", "create", "update", "patch", "delete"]
            ---
            apiVersion: rbac.authorization.k8s.io/v1
            kind: ClusterRoleBinding
            metadata:
              name: edit-validatingadmissionpolicies
            subjects:
            - kind: User
              name: USER_ACCOUNT
              apiGroup: rbac.authorization.k8s.io
            roleRef:
              apiGroup: rbac.authorization.k8s.io
              kind: ClusterRole
              name: validatingadmissionpolicy-editor
            

Replace `USER_ACCOUNT` with the email address of your user account.

     2. Create the RBAC policy:
            
            kubectl apply -f validatingadmissionpolicy-editor.yaml
            

  4. Create a ComputeClass in your cluster. If the cluster already has a ComputeClass, skip this step.

     1. Save the following manifest as `access-computeclass.yaml`:
            
            apiVersion: cloud.google.com/v1
            kind: ComputeClass
            metadata:
              name: access-restriction-class
            spec:
              priorities:
              - machineFamily: e2
              nodePoolAutoCreation:
                enabled: true
              whenUnsatisfiable: ScaleUpAnyway
            

     2. Create the ComputeClass:
            
            kubectl apply -f access-computeclass.yaml
            




## Create a ValidatingAdmissionPolicy

To restrict the ComputeClasses that Pods can select, you create a ValidatingAdmissionPolicy and enforce it in a specific namespace. You use the ValidatingAdmissionPolicy specification to control how Pods can select ComputeClasses. The following steps show you how to create and enforce this policy:

  1. Save the following ValidatingAdmissionPolicy manifest as `restrict-computeclass-usage-vap.yaml`:
         
         apiVersion: admissionregistration.k8s.io/v1
         kind: ValidatingAdmissionPolicy
         metadata:
           name: restrict-computeclass-usage
         spec:
           failurePolicy: Fail # If an internal error occurs, deny the request.
           variables:
           # Check whether the admission request is for a Deployment.
           - name: isDeployment
             expression: "object.kind == 'Deployment'"
           # Get the Pod specification from the admission request by reading the
           # spec.template.spec field for Deployments or the spec field for static Pods.
           - name: podSpec
             expression: "variables.isDeployment ? object.spec.template.spec : object.spec"
           # Check whether a node selector or an affinity rule that explicitly requests a
           # disallowed ComputeClass.
           - name: hasForbiddenNodeSelectorOrAffinity
             expression: >-
               (has(variables.podSpec.nodeSelector) &&
               variables.podSpec.nodeSelector['cloud.google.com/compute-class'] == 'COMPUTECLASS_NAME') ||
               (has(variables.podSpec.affinity) &&
               has(variables.podSpec.affinity.nodeAffinity) &&
               has(variables.podSpec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution) &&
               variables.podSpec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.exists(term, has(term.matchExpressions) &&
                 term.matchExpressions.exists(
                   exp, exp.key == 'cloud.google.com/compute-class' &&
                   exp.operator == 'In' && exp.values.exists(v, v == 'COMPUTECLASS_NAME')
                 )
               ))
         
           # Check whether the Pod has a toleration for the taint that corresponds to a
           # disallowed ComputeClass.
           - name: hasForbiddenComputeClassToleration
             expression: >-
               has(variables.podSpec.tolerations) &&
               variables.podSpec.tolerations.exists(t, 
                 t.key == 'cloud.google.com/compute-class' &&
                 (t.operator == 'Exists' || (t.operator == 'Equal' && t.value == 'COMPUTECLASS_NAME')) &&
                 has(t.effect) && t.effect == 'NoSchedule')
         
           # Check whether the Pod has a toleration that could match any taint.
           - name: hasWildcardToleration
             expression: >-
               has(variables.podSpec.tolerations) &&
               variables.podSpec.tolerations.exists(t, 
                 (t.operator == 'Exists' && !(has(t.key) && t.key != ''))
               )
         
           # Trigger the ValidatingAdmissionPolicy when Pods or Deployments are created or
           # updated.
           matchConstraints:
             resourceRules:
             - apiGroups: [""]
               apiVersions: ["v1"]
               operations: ["CREATE", "UPDATE"]
               resources: ["pods"]
             - apiGroups: ["apps"]
               apiVersions: ["v1"]
               operations: ["CREATE", "UPDATE"]
               resources: ["deployments"]
         
           # Validate whether any of the expressions in the variables section evaluate to
           # true.
           validations:
             - expression: >-
                 !(variables.hasForbiddenNodeSelectorOrAffinity ||
                   variables.hasForbiddenComputeClassToleration ||
                   variables.hasWildcardToleration)
               message: >-
                 Pods and Deployments in this namespace cannot request ComputeClass
                 COMPUTECLASS_NAME or use wildcard
                 tolerations.
         

Replace `COMPUTECLASS_NAME` with the name of a ComputeClass that you want to prevent Pods from selecting.

This ValidatingAdmissionPolicy has the following properties:

     * Triggers for static Pods or Pods in Deployments.
     * Finds Pods that do any of the following:

       * Use a node selector or a node affinity rule to explicitly select a specific disallowed ComputeClass.
       * Use a [toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) that corresponds to a node taint for a specific disallowed ComputeClass.
       * Use a toleration that matches all node taints in the cluster.

This ValidatingAdmissionPolicy is an example. You can use expressions to trigger the policy based on your own conditions, such as preventing Pods that have specific labels from selecting certain ComputeClasses.

  2. Create the ValidatingAdmissionPolicy:
         
         kubectl apply -f restrict-computeclass-usage-vap.yaml
         

  3. Save the following ValidatingAdmissionPolicyBinding as `restrict-computeclass-usage-binding.yaml`:
         
         apiVersion: admissionregistration.k8s.io/v1
         kind: ValidatingAdmissionPolicyBinding
         metadata:
           name: restrict-computeclass-usage-binding
         spec:
           policyName: restrict-computeclass-usage
           validationActions: ["Deny","Audit"]
           matchResources:
             namespaceSelector:
               matchLabels:
                 kubernetes.io/metadata.name: computeclass-vap-tutorial # Replace with the name of any namespace in the cluster.
         

This ValidatingAdmissionPolicyBinding enforces the ValidatingAdmissionPolicy from the previous step in the `computeclass-vap-tutorial` namespace. The values in the `validationActions` field reject Pods or Deployments that violate the ValidatingAdmissionPolicy and add an entry to the Kubernetes audit log.

  4. Create the ValidatingAdmissionPolicyBinding:
         
         kubectl apply -f restrict-computeclass-usage-binding.yaml
         




## Configure RBAC policies

In addition to using a ValidatingAdmissionPolicy to prevent workloads from using certain ComputeClasses, use RBAC to prevent unauthorized principals from creating and modifying the ComputeClasses in your cluster. The following steps show you how to grant access to ComputeClasses to a specific group of users by using Google Groups for RBAC:

  1. Create a group for ComputeClass editors:

     1. In the Google Admin console, go to the **Groups** page.

[Go to Groups](https://admin.google.com/ac/groups)

     2. Click **Create group**.

     3. On the **Group details** page, do the following:

        1. In the **Group name** field, specify `computeclass-editors`.
        2. In the **Group email** field, specify `computeclass-editors`.
        3. Select the **Security** checkbox.
        4. Click **Next**.
     4. On the **Access type** page, in the **Group members** column, verify that the **Who can view members** checkbox is selected.

     5. Click **Create group**.

     6. In the navigation menu, click **Directory** > **Groups**.

     7. Hover over the **gke-security-groups** row, and then click **Add members**.

     8. In the **Add members to gke-security-groups** dialog, specify `computeclass-editors` and select that group from the results.

     9. Click **Add to group**.

  2. Add the email addresses of authorized users to the `computeclass-editors` group.

  3. Save the following ClusterRole as `computeclass-editor-clusterrole.yaml`:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRole
         metadata:
           name: computeclass-editor
         rules:
         -   apiGroups: ["cloud.google.com"]
           resources: ["computeclasses"]
           verbs: ["create","update"]
         

  4. Create the ClusterRole:
         
         kubectl apply -f computeclass-editor-clusterrole.yaml
         

  5. Save the following ClusterRoleBinding as `computeclass-editor-role-binding.yaml`:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: computeclass-editor-role-binding
         subjects:
         - kind: Group
           name: computeclass-editors@GROUP_DOMAIN
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: ClusterRole
           name: computeclass-editor
           apiGroup: rbac.authorization.k8s.io # Required for role references
         

Replace `GROUP_DOMAIN` with the domain name of the `computeclass-editors` group.

  6. Create the ClusterRoleBinding:
         
         kubectl apply -f computeclass-editor-role-binding.yaml
         




## Verify your restrictions

The following sections show you how to verify that the restrictions that you configured in the preceding sections work as expected. If you configure your own restrictions in ValidatingAdmissionPolicies or RBAC policies, then test the restrictions by creating a workload that violates those policies.

### Verify the ValidatingAdmissionPolicy

  1. Save any of the following manifests, each of which violates a different condition of the ValidatingAdmissionPolicy:

     * Deployment that uses a node selector to select a disallowed ComputeClass:
           
           apiVersion: apps/v1
           kind: Deployment
           metadata:
             name: disallowed-computeclass-deployment
             namespace: computeclass-vap-tutorial
           spec:
             replicas: 1
             selector:
               matchLabels:
                 app: forbidden-selector-app
             template:
               metadata:
                 labels:
                   app: forbidden-selector-app
               spec:
                 containers:
                 - name: my-app-container
                   image: nginx:latest
                 # The node selector triggers the policy.
                 nodeSelector:
                   cloud.google.com/compute-class: COMPUTECLASS_NAME
           

     * Deployment that has a toleration for a disallowed ComputeClass:
           
           apiVersion: apps/v1
           kind: Deployment
           metadata:
             name: disallowed-computeclass-deployment-toleration
             namespace: computeclass-vap-tutorial
           spec:
             replicas: 1
             selector:
               matchLabels:
                 app: forbidden-selector-app
             template:
               metadata:
                 labels:
                   app: forbidden-selector-app
               spec:
                 containers:
                 - name: my-app-container
                   image: nginx:latest
                 tolerations:
                 - key: cloud.google.com/compute-class
                   operator: Equal
                   value: COMPUTECLASS_NAME
                   effect: NoSchedule
           

     * Deployment that has a node affinity rule for a disallowed ComputeClass:
           
           apiVersion: apps/v1
           kind: Deployment
           metadata:
             name: disallowed-computeclass-deployment-toleration
             namespace: computeclass-vap-tutorial
           spec:
             replicas: 1
             selector:
               matchLabels:
                 app: forbidden-selector-app
             template:
               metadata:
                 labels:
                   app: forbidden-selector-app
               spec:
                 containers:
                 - name: my-app-container
                   image: nginx:latest
                 affinity:
                   nodeAffinity:
                     requiredDuringSchedulingIgnoredDuringExecution:
                       nodeSelectorTerms:
                       - matchExpressions:
                         - key: cloud.google.com/compute-class
                           operator: In
                           values:
                           - COMPUTECLASS_NAME
           

     * Pod that has a toleration for any node taint in the cluster:
           
           apiVersion: v1
           kind: Pod
           metadata:
             name: disallowed-computeclass-deployment-toleration
             namespace: computeclass-vap-tutorial
           spec:
             containers:
             - name: my-app-container
               image: nginx:latest
             tolerations:
             - operator: Exists
               effect: NoSchedule
           

  2. Create the test workload:
         
         kubectl apply -f PATH_TO_WORKLOAD_MANIFEST
         

The output is similar to the following:
         
         Error from server (BadRequest): admission webhook "validation-policy.kubernetes.io" denied the request: Pods and Deployments in this namespace cannot request ComputeClass COMPUTECLASS_NAME or use wildcard tolerations.
         




### Verify the RBAC configuration

To verify your RBAC configuration, follow these steps:

  1. Authenticate to the cluster by using the credentials of the a user who is a member of the `computeclass-editors` group.

  2. Check whether the user can create a ComputeClass:
         
         kubectl auth can-i create computeclasses.cloud.google.com \
             --as=MEMBER_USER
         

Replace `MEMBER_USER` with the email address of a user who is a member of the group.

The output is `yes`.

  3. Authenticate to the cluster by using the credentials of the a user who isn't a member of the `computeclass-editors` group.

  4. Check whether the user can create a ComputeClass:
         
         kubectl auth can-i create computeclasses.cloud.google.com \
             --as=NON_MEMBER_USER
         

Replace `NON_MEMBER_USER` with the email address of a user who isn't a member of the group.

The output is `no`.




If the output of the `kubectl auth can-i` command is `yes` for a user who isn't a member of the group, verify the following:

  * The `computeclass-editors` group is a member of the `gke-security-groups` group.
  * The email address of the group in your ClusterRoleBinding is the exact email address of the group, such as `computeclass-editors@example.com`.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

If you deploy the ValidatingAdmissionPolicy and RBAC policies in this tutorial in a production cluster, then GKE blocks incoming Pods and API requests that violate the policies. To keep these policies active, skip this section. The following sections show you how to delete the project or individual resources if you followed this tutorial in a learning or testing environment.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

  1. Delete the ComputeClass that you created:
         
         kubectl delete computeclass access-restriction-class
         

  2. Delete the ValidatingAdmissionPolicy and the ValidatingAdmissionPolicyBinding:
         
         kubectl delete validatingadmissionpolicy restrict-computeclass-usage
         kubectl delete validatingadmissionpolicybinding restrict-computeclass-usage-binding
         

  3. Delete the ClusterRoles and the ClusterRoleBindings:
         
         kubectl delete clusterroles \
             computeclass-editor validatingadmissionpolicy-editor
         kubectl delete clusterrolebindings \
             computeclass-editor-role-binding edit-validatingadmissionpolicies
         

  4. Delete the example namespace:
         
         kubectl delete namespace computeclass-vap-tutorial
         




## What's next

  * [Review best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses)
  * [Review best practices for cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
