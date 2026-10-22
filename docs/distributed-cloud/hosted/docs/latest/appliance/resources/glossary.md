---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/glossary/
title: Google Distributed Cloud air-gapped appliance glossary \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:24.601781+00:00
---

# Google Distributed Cloud air-gapped appliance glossary  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Google Distributed Cloud air-gapped appliance glossary Stay organized with collections  Save and categorize content based on your preferences. 

This page provides definitions for Google Distributed Cloud (GDC) air-gapped appliance terms.

## A

API endpoint link
     A service config aspect that specifies the network address, also known as a service endpoint. For example, `aiplatform.googleapis.com`. 
Artifact registry link
     A single place for your organization to manage system container images, operating system (OS) images for bootstrapping bare metal hosts, Debian packages and kernels for in-place OS upgrade, OS images for KubeVirt virtual machines that form a Kubernetes cluster, and bundles to support GDC services. 

## C

cell config link
     Set of YAML-formatted Kubernetes resource definitions that specify the initial GDC configuration. 
cluster link
     A set of nodes that run containerized applications. In Kubernetes, a cluster is a grouping of multiple nodes that runs containerized applications. In GDC, a single cluster encompasses all three of its bare metal nodes. A dedicated Management API server, which runs as pod workloads on the cluster, hosts management plane APIs. User workloads, which include both VMs and Kubernetes pods, can run on this cluster. 
ClusterSelector link
     A `ClusterSelector` custom resource is a special type of config that uses Kubernetes label selectors. You can use a `ClusterSelector` custom resource to limit which clusters a particular config applies to, based on the cluster's labels. You can also use a `ClusterSelector` custom resource to limit which clusters instantiate a namespace-scoped object. 
config link
     A config is a Kubernetes configuration declaration written in YAML or JSON. To read and apply a config to a cluster to create or configure a Kubernetes object or resource in that cluster, GDC uses Config Sync. Config Sync is an open source tool that lets Application Operators and Platform Administrators deploy consistent configurations and policies. A config contains configuration details you apply to a Kubernetes cluster using `kubectl edit` or `kubectl apply`. You must store configs in a repository. 
config sync link
     A config sync lets Application Operators and Platform Administrators deploy consistent configurations and policies. You deploy these configurations and policies to individual Kubernetes clusters, and multiple namespaces within clusters. 
constraint link
     A constraint is a set of rules and parameters that govern interaction with a Kubernetes cluster. By defining one or more constraints, Policy Controller lets you enforce a policy for a Kubernetes cluster. After a constraint is installed, requests to the API server are checked against the constraint and are rejected if they don't comply. 
constraint template link
     A constraint template defines the schema and logic of the constraint. You source constraint templates from Google and third parties or write your own. 
constraint template library link
     The constraint template library is a collection of prebuilt policies included with Policy Controller for common security and compliance controls. 
control plane link
     A cluster's controlling unit, consisting of a set of components that schedule and manage workloads, communicate with clusters, and ensure that clusters are functioning. Control planes include the etcd key-value datastore, the Kubernetes API server, the scheduler, and the controller manager. 
custom resource link
     A custom resource is an instance of a kind defined by a custom resource definition. 

## D

deployment model for a workload link
     A plan to deploy one or multiple instances of the workload, and how GDC distributes those instances. 
data plane link
     In networking, the data plane is where the action takes place. It includes forwarding tables, routing tables, Address Resolution Protocol (ARP) tables, queues, tagging, and re-tagging. The data plane carries out the commands of the control plane. In the data plane, the routers and switches use what the control plane built to dispose of incoming and outgoing frames and packets. Some get sent to another router, for example. Some might get queued up when congested. Some might get dropped if congestion gets poor. 

## G

Google Distributed Cloud (GDC) air-gapped appliance link
     A human-portable device that has Google Distributed Cloud air-gapped deployed on it, for use outside of data centers, such as in the field or in other remote sites. 
Google Distributed Cloud air-gapped link
     A Google Cloud product that delivers a managed software platform running on certified hardware to deliver Google Cloud services and other services. 
GKE link
     Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling your containerized applications using Google infrastructure. The GKE environment consists of multiple machines grouped together to form a cluster. 

## I

infrastructure cluster link
     A bare metal Kubernetes cluster that runs the control plane and data plane components of the device. It also hosts the management API server where all non-container workloads and services are deployed. For GDC, the infrastructure cluster runs all container workloads. 

## K

Kubernetes-based workload link
     A user workload that deploys Kubernetes `Pod` objects. The Application Operator creates pods that run on the Kubernetes cluster. 
Kubernetes namespace link
     A Kubernetes namespace helps different projects, teams, or customers share a Kubernetes cluster. 

## L

long-running operation link
     A long-running operation is a running program that takes a long time to complete. For some API calls, Vertex AI returns operation names. Use helper methods along with these operation names to get the status of or cancel a long-running operation. For example, creating a glossary is a long-running operation. 

## M

management API server link
     An API server running on the infrastructure cluster. All non-container workloads and services are deployed to the management API server. 
management plane link
     A service or API surface used to manage resources which host your data or workload. It represents service components that control the lifecycle of a resource such as create, read, update, and delete. 

## N

node link
     A machine in a Kubernetes cluster. In the context of GDC, a node is either a bare metal machine or a virtual machine. A node might run on VM-based workloads directly, or a node might be part of a cluster that runs Kubernetes-based workloads. 
node pool link
     A node pool is a group of nodes within a cluster that all have the same configuration. 

## O

organization link
     A root resource for all resources a single customer owns. GDC has one organization per device. An organization might contain multiple projects. 

## P

project link
     A logical grouping of related resources into a single access boundary. Multiple projects within an organization share the underlying compute, storage, and network resources. A project might contain workloads with multiple virtual machines or Kubernetes resources. One project aligns to one Kubernetes namespace. 

## S

service link
     A Kubernetes object that logically groups a set of pods and defines a policy by which to access them. 
single-tenancy link
     A single instance of the software and supporting infrastructure that serves a single customer. 
SKU link
     A Stock Keeping Unit (SKU). In GDC air-gapped appliance, a SKU represents a purchasable service, such as Object storage and Block storage. Each SKU is billable to you. 
StatefulSet link
     A Kubernetes object meant for stateful applications. Pods managed by a `StatefulSet` object get a unique, permanent identity in their cluster. 

## U

user workloads link
     Any custom code that the Application Operator deploys to GDC. This can include VM-based workloads or container-based workloads. 

## V

VM-based workload link
     A user workload that deploys to virtual machines (VM). The Application Operator creates VMs that run directly on the management API server. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
