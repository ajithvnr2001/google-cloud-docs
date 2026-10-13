---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateful-workloads/
title: Create stateful workloads \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:03.423908+00:00
---

# Create stateful workloads  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateful-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create stateful workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create and manage stateful workloads within a Google Distributed Cloud (GDC) air-gapped appliance Kubernetes cluster. Stateful workloads let you scale your application deployment with persistent storage. Persistent storage provides your application with consistent identities and stable hostnames, regardless of where its workloads are scheduled.

This page is for developers within the application operator group, who are responsible for creating application workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view stateful workloads in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Create a `StatefulSet` resource

Create a `StatefulSet` object by writing a `StatefulSet` manifest and running `kubectl apply` to create the resource. To provide a stable way for clients to send requests to the pods of your `StatefulSet` resource, you must also create a `Service` object.

The `kubectl apply` command uses manifest files to create, update, and delete resources in your cluster. This is a declarative method of object configuration. This method retains writes made to live objects without merging the changes back into the object configuration files.

To create a `StatefulSet` and `Service` resource, run:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG -n NAMESPACE \
        apply -f - <<EOF
    apiVersion: v1
    kind: Service
    metadata:
      name: SERVICE_NAME
      labels:
        app: APP_NAME
    spec:
      ports:
      - port: 80
        name: web
      clusterIP: None
      selector:
        app: APP_NAME
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: STATEFULSET_NAME
    spec:
      selector:
        matchLabels:
          app: APP_LABEL_NAME
      serviceName: "SERVICE_NAME"
      replicas: NUMBER_OF_REPLICAS
      template:
        metadata:
          labels:
            app: APP_LABEL_NAME
        spec:
          terminationGracePeriodSeconds: 10
          containers:
          - name: CONTAINER_NAME
            image: CONTAINER_IMAGE
            resources:
              requests:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
              limits:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
            ports:
            - containerPort: 80
              name: web
            volumeMounts:
            - name: www
              mountPath: CONTAINER_STORAGE_VOLUME_PATH
      volumeClaimTemplates:
      - metadata:
          name: www
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 1Gi
    EOF
    

Replace the following:

  * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster to which you're deploying container workloads.

  * `NAMESPACE`: the project namespace in which to deploy the container workloads.

  * `SERVICE_NAME`: the name of the `Service` object. Ensure the `StatefulSet` object sets the `Service` object in its `serviceName` as well.

  * `APP_NAME`: the name of the application to run within the deployment.

  * `APP_LABEL_NAME`: the label selector that determines which pods belong to the `StatefulSet` object.

  * `STATEFULSET_NAME`: the name of the `StatefulSet` object.

  * `NUMBER_OF_REPLICAS`: the number of replicated `Pod` objects that the deployment manages.

  * `CONTAINER_NAME`: the name of the container.

  * `CONTAINER_IMAGE`: the name of the container image. You must include the container registry path and version of the image, such as `REGISTRY_PATH/nginx:1.23`. For more information about setting the container registry path, see the [Managed Harbor Service overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/mhs-overview).

  * `CONTAINER_STORAGE_VOLUME_PATH`: the path within the container at which a storage volume is mounted.


**Note:** You can also use `kubectl apply -f DIRECTORY` to create new objects defined by configuration files stored in a directory.

As an example, the following `StatefulSet` object and corresponding `Service` object create stateful container workloads:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      ports:
      - port: 80
        name: web
      clusterIP: None
      selector:
        app: nginx
    ---
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: web
    spec:
      selector:
        matchLabels:
          app: nginx
      serviceName: "nginx"
      replicas: 3
      template:
        metadata:
          labels:
            app: nginx
        spec:
          terminationGracePeriodSeconds: 10
          containers:
          - name: nginx
            image: REGISTRY_PATH/nginx:1.23
            resources:
              requests:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
              limits:
                nvidia.com/gpu-pod-NVIDIA_A100_80GB_PCIE: 1
            ports:
            - containerPort: 80
              name: web
            volumeMounts:
            - name: www
              mountPath: /usr/share/nginx/html
      volumeClaimTemplates:
      - metadata:
          name: www
        spec:
          accessModes: [ "ReadWriteOnce" ]
          resources:
            requests:
              storage: 1Gi
    

**Important:** If you're deploying GPU workloads to your containers, see [Manage GPU container workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/deploy-gpu-container-workloads) for more information.

In this example:

  * A `Service` object named `nginx` is created, indicated by the `metadata: name` field. The `Service` object targets an app called `nginx`, indicated by `labels.app: nginx` and `selector.app: nginx`. The `Service` object exposes port 80 and names it `web`. This `Service` object controls the network domain and routes internet traffic to the containerized application deployed by the `StatefulSet` object.
  * A `StatefulSet` named `web` is created with three replicated `Pod` objects, as set by the field `replicas: 3`.
  * The `Pod` template, set by the section `.spec.template`, indicates that its `Pod` objects are labelled `app: nginx`.
  * The `Pod` specification, set by the section `.template.spec`, indicates that the pods of the `StatefulSet` run one container, `nginx`, which runs the `nginx` image at version `1.23`.
  * The `Pod` specification uses the web port opened by the `Service` object.
  * The `.template.spec.volumeMounts` section specifies a `mountPath` field, which is named `www`. The `mountPath` is the path in the container where a storage volume is mounted.
  * The `StatefulSet` provisions three `PersistentVolumeClaim` objects, named `web-www-0`, `web-www-1`, and `web-www-2`, with 1GB of provisioned storage each.



After it's created, the `StatefulSet` ensures that the chosen number of `Pod` objects are running and available at all times. The `StatefulSet` automatically replaces `Pod` objects that fail or are evicted from their nodes, and associates new `Pod` objects with the storage resources, resource requests and limits, and other configurations defined in the `Pod` specification of the `StatefulSet` object.

## Request persistent storage in a `StatefulSet` resource

Persistent storage can be dynamically provisioned so that the underlying volumes are created on demand. Applications can request persistent storage with a `PersistentVolumeClaim` object.

Typically, you must create `PersistentVolumeClaim` objects in addition to creating the `Pod` object. However, `StatefulSet` objects include a `volumeClaimTemplates` array which generates the `PersistentVolumeClaim` objects. Each `StatefulSet` replica gets its own `PersistentVolumeClaim` object.

For more information, see [Configure container storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/access-multi-writer-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
