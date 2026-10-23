---
url: https://docs.cloud.google.com/migrate/kf/docs/2.11/concepts/kf-dependencies/
title: Kf dependencies and architecture \u00a0|\u00a0 Kf 2.11 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:27.732683+00:00
---

# Kf dependencies and architecture  |  Kf 2.11  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.11/concepts/kf-dependencies/

Version 2.11 - Latest version

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.11 ](https://docs.cloud.google.com/migrate/kf/docs/2.11)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.11/getting-started)



Send feedback 

#  Kf dependencies and architecture Stay organized with collections  Save and categorize content based on your preferences. 

Kf requires Kubernetes and several other OSS projects to run. Some of the dependencies are satisfied with Google-managed services—for example, Google Kubernetes Engine (GKE) provides Kubernetes.

## Dependencies

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs)
  * [Tekton Pipelines](https://github.com/tektoncd/pipeline)



![](https://docs.cloud.google.com/migrate/kf/docs/2.11/images/kf-components-diagram.svg)

## Get CRD details

Kf supports the `kubectl` subcommand `explain`. It allows you to list the fields in Kf CRDs to understand how to create Kf objects via automation instead of manually via the CLI. This command is designed to be used with Config Management to automate creation and management of resources like Spaces across many clusters. You can use this against any of the component `kinds` below.

In this example, we examine the `kind` called `space` in the `spaces` CRD:
    
    
    kubectl explain space.spec

The output looks similar to this:
    
    
    $ kubectl explain space.spec
    KIND:     Space
    VERSION:  kf.dev/v1alpha1
    
    RESOURCE: spec <Object>
    
    DESCRIPTION:
         SpaceSpec contains the specification for a space.
    
    FIELDS:
       buildConfig  <Object>
         BuildConfig contains config for the build pipelines.
    
       networkConfig        <Object>
         NetworkConfig contains settings for the space's networking environment.
    
       runtimeConfig        <Object>
         RuntimeConfig contains settings for the app runtime environment.
    

## Kf components

Kf installs several of its own Kubernetes [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) and [controllers](https://kubernetes.io/docs/concepts/workloads/controllers/). The custom resources effectively serve as the Kf API and are used by the `kf` CLI to interact with the system. The controllers use Kf's CRDs to orchestrate the other components in the system.

You can view the CRDs installed and used by Kf by running the following command:
    
    
    kubectl api-resources --api-group=kf.dev

The output of that command is as follows:
    
    
    NAME                      SHORTNAMES   APIGROUP   NAMESPACED   KIND
    apps                                   kf.dev     true         App
    builds                                 kf.dev     true         Build
    clusterservicebrokers                  kf.dev     false        ClusterServiceBroker
    routes                                 kf.dev     true         Route
    servicebrokers                         kf.dev     true         ServiceBroker
    serviceinstancebindings                kf.dev     true         ServiceInstanceBinding
    serviceinstances                       kf.dev     true         ServiceInstance
    spaces                                 kf.dev     false        Space
    

### Apps

Apps represent a [twelve-factor application](https://12factor.net/) deployed to Kubernetes. They encompass source code, configuration, and the current state of the application. Apps are responsible for reconciling:

  * Kf Builds
  * Kf Routes
  * Kubernetes Deployments
  * Kubernetes Services
  * Kubernetes ServiceAccounts
  * Kubernetes Secrets



You can list Apps using Kf or `kubectl`:
    
    
    kf apps
    kubectl get apps -n space-name

### Builds

Builds combine the source code and build configuration for Apps. They provision Tekton TaskRuns with the correct steps to actuate a Buildpack V2, Buildpack V3, or Dockerfile build.

You can list Builds using Kf or `kubectl`:
    
    
    kf builds
    kubectl get builds -n space-name

### ClusterServiceBrokers

ClusterServiceBrokers hold the connection information necessary to extend Kf with a service broker. They are responsible for fetching the catalog of services the broker provides and displaying them in the output of `kf marketplace`.

You can list ClusterServiceBrokers using `kubectl`:
    
    
    kubectl get clusterservicebrokers

### Routes

Routes are a high level structure that contain HTTP routing rules. They are responsible for reconciling Istio VirtualServices.

You can list Routes using Kf or `kubectl`:
    
    
    kf routes
    kubectl get routes -n space-name

### ServiceBrokers

ServiceBrokers hold the connection information necessary to extend Kf with a service broker. They are responsible for fetching the catalog of services the broker provides and displaying them in the output of `kf marketplace`.

You can list ServiceBrokers using `kubectl`:
    
    
    kubectl get servicebrokers -n space-name

### ServiceInstanceBinding

ServiceInstanceBindings hold the parameters to create a binding on a service broker and the credentials the broker returns for the binding. They are responsible for calling the bind API on the broker to bind the service.

You can list ServiceInstanceBindings using Kf or `kubectl`:
    
    
    kf bindings
    kubectl get serviceinstancebindings -n space-name

### ServiceInstance

ServiceInstances hold the parameters to create a service on a service broker. They are responsible for calling the provision API on the broker to create the service.

You can list ServiceInstances using Kf or `kubectl`:
    
    
    kf services
    kubectl get serviceinstances -n space-name

### Spaces

Spaces hold configuration information similar to Cloud Foundry organizations and spaces. They are responsible for:

  * Creating the Kubernetes Namespace that other Kf resources are provisioned into.
  * Creating Kubernetes NetworkPolicies to enforce network connection policies.
  * Holding configuration and policy for Builds, Apps, and Routes.



You can list Spaces using Kf or `kubectl`:
    
    
    kf spaces
    kubectl get spaces

## Kf RBAC / Permissions

The following sections list permissions for Kf and its components to have correct access at the cluster level. These permissions are required and enabled by default in Kf; do not attempt to disable them.

**Components** | **Namespace** | **Service Account**  
---|---|---  
`controller` | kf | controller  
`subresource-apiserver` | kf | controller  
`webhook` | kf | controller  
`appdevexperience-operator` | appdevexperience | appdevexperience-operator  
  
Note that the `appdevexperience-operator` service account has the same set of permissions as `controller`. The operator is what deploys all Kf components, including custom resource definitions and controllers.

### RBAC for Kf service accounts

The following `apiGroup` definitions detail which access control permissions components in Kf have on which API groups and resources for both the `controller` and `appdevexperience-operator` service accounts.
    
    
    - apiGroups:
      - "authentication.k8s.io"
      resources:
      - tokenreviews
      verbs:
      - create
    - apiGroups:
      - "authorization.k8s.io"
      resources:
      - subjectaccessreviews
      verbs:
      - create
    - apiGroups:
      - ""
      resources:
      - pods
      - services
      - persistentvolumeclaims
      - persistentvolumes
      - endpoints
      - events
      - configmaps
      - secrets
      verbs: *
    - apiGroups:
      - ""
      resources:
      - services
      - services/status
      verbs:
      - create
      - delete
      - get
      - list
      - watch
    - apiGroups:
      - "apps"
      resources:
      - deployments
      - daemonsets
      - replicasets
      - statefulsets
      verbs: *
    - apiGroups:
      - "apps"
      resources:
      - deployments/finalizers
      verbs:
      - get
      - list
      - create
      - update
      - delete
      - patch
      - watch
    - apiGroups:
      - "rbac.authorization.k8s.io"
      resources:
      - clusterroles
      - roles
      - clusterrolebindings
      - rolebindings
      verbs:
      - create
      - delete
      - update
      - patch
      - escalate
      - get
      - list
      - deletecollection
      - bind
    - apiGroups:
      - "apiregistration.k8s.io"
      resources:
      - apiservices
      verbs:
      - update
      - patch
      - create
      - delete
      - get
      - list
    - apiGroups:
      - "pubsub.cloud.google.com"
      resources:
      - topics 
      - topics/status
      verbs: *
    - apiGroups:
      - ""
      resources:
      - namespaces
      - namespaces/finalizers
      - serviceaccounts
      verbs: 
      - get
      - list
      - create
      - update
      - watch
      - delete
      - patch
      - watch
    - apiGroups:
      - "autoscaling"
      resources:
      - horizontalpodautoscalers
      verbs: 
      - create
      - delete
      - get
      - list
      - update
      - patch
      - watch
    - apiGroups:
      - "coordination.k8s.io"
      resources:
      - leases
      verbs: *
    - apiGroups:
      - "batch"
      resources:
      - jobs
      - cronjobs
      verbs: 
      - get
      - list
      - create
      - update
      - patch
      - delete
      - deletecollection
      - watch
    - apiGroups:
      - "messaging.cloud.google.com"
      resources:
      - channels
      verbs: 
      - delete
    - apiGroups:
      - "pubsub.cloud.google.com"
      resources:
      - pullsubscriptions
      verbs: 
      - delete
      - get
      - list
      - watch
      - create
      - update
      - patch
    - apiGroups:
      - "pubsub.cloud.google.com"
      resources:
      - [pullsubscriptions/status
      verbs: 
      - get
      - update
      - patch
    - apiGroups:
      - "events.cloud.google.com"
      resources: *
      verbs: *
    - apiGroups:
      - "keda.k8s.io"
      resources: *
      verbs: *
    - apiGroups:
      - "admissionregistration.k8s.io"
      resources:
      - mutatingwebhookconfigurations
      - validatingwebhookconfigurations
      verbs:
      - get
      - list
      - create
      - update
      - patch
      - delete
      - watch
    - apiGroups:
      - "extensions"
      resources:
      - ingresses
      - ingresses/status
      verbs: *
    - apiGroups:
      - ""
      resources: 
      - endpoints/restricted
      verbs:
      - create
    - apiGroups:
      - "certificates.k8s.io"
      resources: 
      - certificatesigningrequests
      - certificatesigningrequests/approval
      - certificatesigningrequests/status
      verbs: 
      - update
      - create
      - get
      - delete
    - apiGroups:
      - "apiextensions.k8s.io"
      resources:
      - customresourcedefinitions
      verbs:   
      - get
      - list
      - create
      - update
      - patch
      - delete
      - watch
    - apiGroups:
      - "networking.k8s.io"
      resources: 
      - networkpolicies
      verbs: 
      - get
      - list
      - create
      - update
      - patch
      - delete
      - deletecollection
      - watch
    - apiGroups:
      - ""
      resources: 
      - nodes
      verbs: 
      - get
      - list
      - watch
      - update
      - patch
    - apiGroups:
      - ""
      resources: 
      - nodes/status
      verbs: 
      - patch
    

The following table lists how the RBAC permissions are used in Kf, where:

  * **view** includes the verbs: get, list, watch
  * **modify** includes the verbs: create, update, delete, patch

**Permissions** | **Reasons**  
---|---  
Can view all `secrets` | Kf reconcilers need to read secrets for functionalities such as space creation and service instance binding.  
Can modify `pods` | Kf reconcilers need to modify pods for functionalities such as building/pushing Apps and Tasks.  
Can modify `secrets` | Kf reconcilers need to modify secrets for functionalities such as building/pushing Apps and Tasks and service instance binding.  
Can modify `configmaps` | Kf reconcilers need to modify configmaps for functionalities such as building/pushing Apps and Tasks.  
Can modify `endpoints` | Kf reconcilers need to modify endpoints for functionalities such as building/pushing Apps and route binding.  
Can modify `services` | Kf reconcilers need to modify pods for functionalities such as building/pushing Apps and route binding.  
Can modify `events` | Kf controller creates and emits events for the resources managed by Kf.  
Can modify `serviceaccounts` | Kf needs to modify service accounts for App deployments.  
Can modify `endpoints/restricted` | Kf needs to modify endpoints for App deployments.  
Can modify `deployments` | Kf needs to modify deployments for functionalities such as pushing Apps.  
Can modify `mutatingwebhookconfiguration` | Mutatingwebhookconfiguration is needed by Cloud Service Mesh, a Kf dependency, for admission webhooks.  
Can modify `customresourcedefinitions customresourcedefinitions/status` | Kf manages resources through Custom Resources such as Apps, Spaces and Builds.  
Can modify `horizontalpodautoscalers` | Kf supports autoscaling based on Horizontal Pod Autoscalers.  
Can modify `namespace/finalizer` | Kf needs to set owner reference of webhooks.  
  
## Third-party libraries

Third-party library source code and licenses can be found in the `/third_party` directory of any Kf container image.

You can also run `kf third-party-licenses` to view the third-party licenses for the version of the Kf CLI that you downloaded.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
