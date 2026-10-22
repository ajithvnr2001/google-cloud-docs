---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/
title: Create a backup and restore notebook data \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:01.208817+00:00
---

# Create a backup and restore notebook data  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/backup-restore-notebook-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a backup and restore notebook data Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped lets you create backups and restore data from the home directory of your JupyterLab instances.

This page describes creating and restoring backups of Vertex AI Workbench notebook data. If you are new to Vertex AI, [learn more about Vertex AI Workbench](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench-intro).

**Note:** Vertex AI Workbench doesn't support backing up the settings on the `Notebook` custom resource of the JupyterLab instance. You must create new JupyterLab instances and transfer the restored data into that instance.

## Before you begin

To get the permissions that you need to copy restored data, ask your IAM Org Admin to grant you the User Cluster Developer (`user-cluster-developer`) role.

## Create a backup and restore JupyterLab instance data

Define protected applications to create a backup of the home directory of an individual JupyterLab instance or the home directories of all JupyterLab instances in a project at once.

Create a `ProtectedApplication` custom resource in the cluster where you want to schedule backups. Backup and restore plans use protected applications to select resources. For information about creating protected applications, see [Protected application strategies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/protected-application-strategies).

The `ProtectedApplication` custom resource contains the following fields:

**Field** | **Description**  
---|---  
`resourceSelection` | The way in which the `ProtectedApplication` object selects resources for backups or restorations.  
| `type` | The method to select resources. A `Selector` type indicates that resources with matching labels must be selected.  
| `selector` | The selection rules. This field contains the following sub-fields:  
|  | `matchLabels` | The labels that the `ProtectedApplication` object uses to match resources. This field contains the following sub-fields:  
|  |  | `app.kubernetes.io/part-of` | The name of a higher level application this one is part of. Select Vertex AI Workbench as the high-level application for JupyterLab instances.  
|  |  | `app.kubernetes.io/component` | The component within the architecture. Select resources from Vertex AI Workbench that provide storage for JupyterLab instances.  
|  |  | `app.kubernetes.io/instance` | A unique name identifying the instance of an application. Narrow the scope to select a JupyterLab instance. The value is the same as the name of the JupyterLab instance on the GDC console.  
  
Use the `ProtectedApplication` custom resource to select the storage of a single JupyterLab instance or all JupyterLab instances in a project, as in the following examples:

  * **Select the storage of a single JupyterLab instance** :

The following example shows a `ProtectedApplication` custom resource that selects the storage for a JupyterLab instance named `my-instance-name` in the `my-project` namespace:
        
        apiVersion: gkebackup.gke.io/v1
        kind: ProtectedApplication
        metadata:
          name: my-protected-application
          namespace: my-project
        spec:
          resourceSelection:
            type: Selector
            selector:
              matchLabels:
                app.kubernetes.io/part-of: vtxwb
                app.kubernetes.io/component: storage
                app.kubernetes.io/instance: my-instance-name
        

  * **Select the storage of all JupyterLab instances** :

The following example shows a `ProtectedApplication` custom resource that selects the storage for all JupyterLab instances in the `my-project` namespace:
        
        apiVersion: gkebackup.gke.io/v1
        kind: ProtectedApplication
        metadata:
          name: my-protected-application
          namespace: my-project
        spec:
          resourceSelection:
            type: Selector
            selector:
              matchLabels:
                app.kubernetes.io/part-of: vtxwb
                app.kubernetes.io/component: storage
        

This example doesn't contain the `app.kubernetes.io/instance` label because it selects all JupyterLab instances.




To create a backup and restore data from a JupyterLab instance, [plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups) and [plan a set of restores](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/plan-restores) using the `ProtectedApplication` custom resource you defined.

## Copy restored data to a new JupyterLab instance

Follow these steps to copy restored data from the `PersistentVolumeClaim` resource of a JupyterLab instance to a new JupyterLab instance:

  1. Meet the prerequisites.
  2. [Create a JupyterLab notebook](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-workbench#create-notebook) associated with a JupyterLab instance to copy restored data.
  3. Get the pod name of the JupyterLab instance where you created the notebook:
         
         kubectl get pods -l notebook-name=INSTANCE_NAME -n PROJECT_NAMESPACE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the JupyterLab instance you configured.
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
  4. Get the name of the image that the JupyterLab instance is running:
         
         kubectl get pods POD_NAME -n PROJECT_NAMESPACE -o jsonpath="{.spec.containers[0].image}"
         

Replace the following:

     * `POD_NAME`: the pod name of the JupyterLab instance.
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
  5. Find the name of the `PersistentVolumeClaim` resource that was restored:
         
         kubectl get pvc -l app.kubernetes.io/part-of=vtxwb,app.kubernetes.io/component=storage,app.kubernetes.io/instance=RESTORED_INSTANCE_NAME -n PROJECT_NAMESPACE
         

Replace the following:

     * `RESTORED_INSTANCE_NAME`: the name of the JupyterLab instance that you restored.
     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
  6. Create a YAML file named `vtxwb-data.yaml` with the following content:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: vtxwb-data
           namespace: PROJECT_NAMESPACE
           labels:
             aiplatform.gdc.goog/service-type: workbench
         spec:
           containers:
           - args:
             - sleep infinity
             command:
             - bash
             - -c
             image: IMAGE_NAME
             imagePullPolicy: IfNotPresent
             name: vtxwb-data
             resources:
               limits:
                 cpu: "1"
                 memory: 1Gi
               requests:
                 cpu: "1"
                 memory: 1Gi
             terminationMessagePath: /dev/termination-log
             terminationMessagePolicy: File
             volumeMounts:
             - mountPath: /home/jovyan
               name: restore-data
             workingDir: /home/jovyan
           volumes:
           - name: restore-data
             persistentVolumeClaim:
               claimName: RESTORED_PVC_NAME
         

Replace the following:

     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
     * `IMAGE_NAME`: the name of the container image that the JupyterLab instance is running.
     * `RESTORED_PVC_NAME`: the name of the restored `PersistentVolumeClaim` resource.
**Note:** The name of the home directory of your JupyterLab instances is `/home/jovyan`.
  7. Create a new pod for your restored `PersistentVolumeClaim` resource:
         
         kubectl apply -f ./vtxwb-data --kubeconfig KUBECONFIG_PATH
         

Replace `KUBECONFIG_PATH` with the path of the kubeconfig file in the cluster.

  8. Wait for the `vtxwb-data` pod to reach the `RUNNING` state.

  9. Copy your restored data to a new JupyterLab instance:
         
         kubectl cp PROJECT_NAMESPACE/vtxwb-data:/home/jovyan ./restore --kubeconfig KUBECONFIG_PATH
         
         kubectl cp ./restore PROJECT_NAMESPACE/POD_NAME:/home/jovyan/restore --kubeconfig KUBECONFIG_PATH
         
         rm ./restore
         

Replace the following:

     * `PROJECT_NAMESPACE`: the project namespace where you created the JupyterLab instance.
     * `KUBECONFIG_PATH`: the path of the kubeconfig file in the cluster.
     * `POD_NAME`: the pod name of the JupyterLab instance.

After copying the data, your restored data is available in the `/home/jovyan/restore` directory.

  10. Delete the pod that you created to access your restored data:
         
         kubectl delete pod vtxwb-data -n my-namespace` --kubeconfig KUBECONFIG_PATH
         

Replace `KUBECONFIG_PATH` with the path of the kubeconfig file in the cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
