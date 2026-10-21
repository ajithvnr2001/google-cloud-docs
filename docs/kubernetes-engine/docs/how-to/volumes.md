---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volumes/
title: Creating Kubernetes Volumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:05.124385+00:00
---

# Creating Kubernetes Volumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Creating Kubernetes Volumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows you how to create Volume resources in your Google Kubernetes Engine (GKE) cluster.

You manage how your containerized applications store and share data in a Kubernetes cluster by creating Kubernetes Volumes and configuring them within your Deployments. By creating Kubernetes Volumes, you can deploy stateful microservices. This also increases development velocity as you manage application data consistently.

This document is for developers and administrators who manage GKE container storage. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Using Volumes with Deployments

You can [create a Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) of Pods where each Pod contains one or more Volumes. The following Deployment manifest describes a Deployment of three Pods that each have an [emptyDir Volume](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir). For more information, see [Creating a Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps#create).

In this example:

  * The `metadata: name` field specifies a Deployment named `volumes-example-deployment`.
  * The [Pod template](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/#pod-templates) specification includes a `volumes` field that describes an emptyDir volume named `cache-volume`.
  * The container specification includes a `volumeMounts:` field that specifies that the Volume named `cache-volume` is mounted at the path `/cache`.
  * The manifest file is named `volumes-demo.yaml`.


    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
     name: volumes-example-deployment
    spec:
     replicas: 3
     selector:
      matchLabels:
       app: demo
     template:
      metadata:
       labels:
        app: demo
      spec:
       containers:
       - name: test-container
        image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
        volumeMounts:
        - mountPath: /cache
         name: cache-volume
       volumes:
        - name: cache-volume
         emptyDir: {}
    

To create a Deployment from this manifest file, run the following command:
    
    
    kubectl apply -f volumes-demo.yaml
    

Verify that your Deployment is running correctly and has the expected Volume with this command:
    
    
    kubectl describe pods volumes-example-deployment
    

This prints information about each of the three Pods in the Deployment. The output shows that each Pod has a container, test-container, with the `/cache` mount:
    
    
    Mounts:
      /cache from cache-volume (rw)
    

The output also shows that each Pod contains a Volume named `cache-volume`:
    
    
    Volumes:
      cache-volume:
        Type:    EmptyDir (a temporary directory that shares a pod's lifetime)
    

## What's next

  * [Learn about PersistentVolumes, PersistentVolumeClaims, and dynamic storage provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).
  * [Learn about using the Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
