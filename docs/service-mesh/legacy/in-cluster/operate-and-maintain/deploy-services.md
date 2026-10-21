---
url: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/operate-and-maintain/deploy-services/
title: Deploying Services \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:10.882322+00:00
---

# Deploying Services  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/in-cluster/operate-and-maintain/deploy-services/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploying Services

Deploying Services to clusters with Cloud Service Mesh is almost the same as deploying Services to clusters without Cloud Service Mesh. You do need to make some changes to your Kubernetes manifests:

  * Create [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#services) for all containers. All [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) should have a Kubernetes Service attached.

  * Name your Service ports. Although GKE lets you define unnamed Service ports, Cloud Service Mesh requires that you provide a [name for a port](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/operate-and-maintain/name-service-ports) that matches the port's protocol.

  * Label your Deployments. This lets you use Cloud Service Mesh traffic management features such as splitting traffic between versions of the same service.




The following example Deployment and Service illustrate these requirements:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: helloserver
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: helloserver
      template:
        metadata:
          labels:
            app: helloserver
        spec:
          containers:
          - image: gcr.io/google-samples/istio/helloserver:v0.0.1
            imagePullPolicy: Always
            name: main
          restartPolicy: Always
          terminationGracePeriodSeconds: 5
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: hellosvc
    spec:
      ports:
      - name: http
        port: 80
        targetPort: 8080
      selector:
        app: helloserver
      type: LoadBalancer

After deploying your Services on a cluster with Cloud Service Mesh, be sure to [inject sidecar proxies](https://docs.cloud.google.com/service-mesh/legacy/in-cluster/operate-and-maintain/proxy-injection).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
