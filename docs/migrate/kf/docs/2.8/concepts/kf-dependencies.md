---
url: https://docs.cloud.google.com/migrate/kf/docs/2.8/concepts/kf-dependencies/
title: Kf dependencies and architecture \u00a0|\u00a0 Kf 2.8 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:25:09.029435+00:00
---

# Kf dependencies and architecture  |  Kf 2.8  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.8/concepts/kf-dependencies/

Version 2.8

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
  * [ 2.8 ](https://docs.cloud.google.com/migrate/kf/docs/2.8)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.8/getting-started)



Send feedback 

#  Kf dependencies and architecture Stay organized with collections  Save and categorize content based on your preferences. 

Kf requires Kubernetes and several other OSS projects to run. Some of the dependencies are satisfied with Google-managed services—for example, Google Kubernetes Engine (GKE) provides Kubernetes.

## Dependencies

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs)
  * [Tekton Pipelines](https://github.com/tektoncd/pipeline)



![](https://docs.cloud.google.com/migrate/kf/docs/2.8/images/kf-components-diagram.svg)

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

## Third-party libraries

Third-party library source code and licenses can be found in the `/third_party` directory of any Kf container image.

You can also run `kf third-party-licenses` to view the third-party licenses for the version of the Kf CLI that you downloaded.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
