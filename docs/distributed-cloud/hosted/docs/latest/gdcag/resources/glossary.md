---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/glossary/
title: Google Distributed Cloud air-gapped glossary \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:19:48.572121+00:00
---

# Google Distributed Cloud air-gapped glossary  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Google Distributed Cloud air-gapped glossary Stay organized with collections  Save and categorize content based on your preferences. 

This page provides definitions for Google Distributed Cloud (GDC) air-gapped terms.

## A

anchor zone link
     A zone that is already part of the global control plane. This must be the zone that whose GitLab instance is used to apply infrastructure-as-code (IaC) changes to the universe's global API. This concept was introduced with multi-zone universes. 
API endpoint link
     A service config aspect that specifies the network address, also known as a service endpoint. For example, `aiplatform.googleapis.com`. 
Artifact registry link
     A single place for your organization to manage system container images, operating system (OS) images for bootstrapping bare metal hosts, Debian packages and kernels for in-place OS upgrade, OS images for KubeVirt virtual machines that form a Kubernetes cluster, and bundles to support Distributed Cloud services. 

## B

backup site link
     The site where backup data is being stored. For control plane disaster recovery, the backup site is not the site used to restore the data. For the recovery of workloads in the case of a disaster, this site may or may not be the site used to restore the data. 

## C

cell config link
     Set of YAML-formatted Kubernetes resource definitions that specify the initial Distributed Cloud configuration. 
cluster link
     A set of nodes that run containerized applications. In Kubernetes, a cluster is a grouping of multiple nodes that runs containerized applications. 
ClusterSelector link
     A `ClusterSelector` custom resource is a special type of config that uses Kubernetes label selectors. You can use a `ClusterSelector` custom resource to limit which clusters a particular config applies to, based on the cluster's labels. You can also use a `ClusterSelector` custom resource to limit which clusters instantiate a namespace-scoped object. 
config link
     A config is a Kubernetes configuration declaration written in YAML or JSON. To read and apply a config to a cluster to create or configure a Kubernetes object or resource in that cluster, Distributed Cloud uses Config Sync. Config Sync is an open source tool that lets Application Operators and Platform Administrators deploy consistent configurations and policies. A config contains configuration details you apply to a Kubernetes cluster using `kubectl edit` or `kubectl apply`. You must store configs in a repository. 
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
     A plan to deploy one or multiple instances of the workload, and how Distributed Cloud distributes those instances. 
data plane link
     In networking, the data plane is where the action takes place. It includes forwarding tables, routing tables, Address Resolution Protocol (ARP) tables, queues, tagging, and re-tagging. The data plane carries out the commands of the control plane. In the data plane, the routers and switches use what the control plane built to dispose of incoming and outgoing frames and packets. Some get sent to another router, for example. Some might get queued up when congested. Some might get dropped if congestion gets poor. 
disaster domain link
     A disaster domain represents a collection of buildings that might be impacted at the same time due to physical proximity of the buildings. Thus, it is a durability-related construct used to simplify the requirements for zone separation. Usually, a single disaster domain corresponds to a single campus and is often referred to as a failure domain. 

## G

GKE link
     Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling your containerized applications using Google infrastructure. The GKE environment consists of multiple machines grouped together to form a cluster. 
Google Distributed Cloud (GDC) air-gapped link
     A Google Cloud product that delivers a managed software platform running on certified hardware to deliver Google Cloud services and other services. 
GDC rack link
     A collection of physical servers deployed in a server rack. 

## J

joining zone link
     The zone that is joining the global control plane. This concept was introduced with multi-zone universes. 

## K

Kubernetes-based workload link
     A user workload that deploys Kubernetes `Pod` objects. The Application Operator creates pods that run on a single Kubernetes cluster. 
Kubernetes cluster link
     A cluster composed of multiple virtual machine nodes running on the org infrastructure cluster. Multiple Kubernetes clusters can be provisioned based on available compute capacity. Kubernetes workloads deploy to a Kubernetes cluster. A Kubernetes cluster is sometimes referred to as a user cluster. 
Kubernetes namespace link
     A Kubernetes namespace helps different projects, teams, or customers share a Kubernetes cluster. 

## L

long-running operation link
     A long-running operation is a running program that takes a long time to complete. For some API calls, Vertex AI returns operation names. Use helper methods along with these operation names to get the status of or cancel a long-running operation. For example, creating a glossary is a long-running operation. 

## M

management API server link
     An API server running on the org infrastructure cluster. There is one management API server per organization, per zone. All non-container workloads and services are deployed to the management API server. 
management plane link
     A service or API surface used to manage resources which host your data or workload. It represents service components that control the lifecycle of a resource such as create, read, update, and delete. 
multi-tenancy link
     A conceptual state where multiple, logically unrelated applications are hosted on the same process or unit of execution that results in them sharing fate. Examples include multiple processes running on the same core, or multiple machine learning models served on the same binary. 

## N

node link
     A machine in a Kubernetes cluster. In the context of Distributed Cloud, a node is either a bare metal machine or a virtual machine. A node might run on VM-based workloads directly, or a node might be part of a cluster that runs Kubernetes-based workloads. 
node pool link
     A node pool is a group of nodes within a cluster that all have the same configuration. 

## O

organization link
     A root resource for all resources a single customer owns. Each organization has a separate set of physical servers from other organizations in the same Distributed Cloud universe. An organization might contain multiple projects. 
org infrastructure cluster link
     A cluster that runs the control plane and data plane components of the organization. It also hosts the management API server where all non-container workloads and services are deployed. Each organization has exactly one org infrastructure cluster. 

## P

project link
     A logical grouping of related resources into a single access boundary. Multiple projects within an organization share the underlying compute, storage, and network resources. A project might contain workloads with multiple virtual machines or Kubernetes resources. One project aligns to one Kubernetes namespace. Projects can span across one or multiple Kubernetes clusters. 

## R

region link
     A grouping of zones in a universe with defined latency requirements. A zone with no peers close enough is considered its own region. Zones in a region must be separated by a set geographic distance to ensure they are separate disaster domains. 
root admin cluster link
     A cluster used in the initial provisioning of the Distributed Cloud universe and for creating additional organizations. Only the Infrastructure Operator uses the root admin cluster, which is not tied to a specific customer organization and has dedicated hardware and virtual resources. The root admin cluster is made up of bare metal nodes. 

## S

service link
     A Kubernetes object that logically groups a set of pods and defines a policy by which to access them. 
single-tenancy link
     A single zone of the software and supporting infrastructure that serves a single customer. 
Security information and event management (SIEM, SEM, and SIM) link
     The real-time analysis of security alerts generated by network hardware and applications. Vendors sell SIEM as software, as appliances, or as managed services. These products are also used to log security data and generate reports for compliance purposes. This segment of security management deals with real-time monitoring, correlation of events, notifications, and console views. 
SKU link
     A Stock Keeping Unit (SKU). In Distributed Cloud, a SKU represents a purchasable service, such as Object storage and Block storage. Each SKU is billable to you. 
source site link
     The site that is having its data backed up. Use this data to recover from a disaster. This site may or may not be the site to which the backed up data is restored. 
StatefulSet link
     A Kubernetes object meant for stateful applications. Pods managed by a `StatefulSet` object get a unique, permanent identity in their cluster. 

## U

universe link
     An isolated and self-contained unit of GDC containing all services available on GDC. It consists of one or more zones organized into regions that are interconnected and share a control plane. 
user workloads link
     Any custom code that the Application Operator deploys to Distributed Cloud. This can include VM-based workloads or container-based workloads. 

## V

VM-based workload link
     A user workload that deploys to virtual machines (VM). The Application Operator creates VMs that run on the management API server. 

## Z

zone link
     An independent disaster domain. It is a full implementation of GDC – a hardware and software solution that does not require connectivity to Google Cloud at any time. A zone manages infrastructure, services, APIs, and tooling that use a local control plane. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
