---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/default-egress/
title: Manage project default egress NAT \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:51.935276+00:00
---

# Manage project default egress NAT  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/default-egress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manage project default egress NAT Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the now deprecated project default egress NAT configuration, which can be used to enable workloads to connect outside the organization. This page also contains instructions on how to migrate to the recommended solution, [Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat).

## Overview

This page describes egress connectivity actions you must take on a virtual machine (VM) or pod in a project to let workloads go out of the organization, using the (deprecated) project default egress NAT configuration option.

**Note:** this configuration option and the recommended solution, [Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat), are incompatible; you can only use one of these options for a given endpoint.

Default project egress NAT isn't compatible with [standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster). Use [Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat) if you need to control egress for standard clusters.

The procedure shows how to add a required label to deployments to explicitly enable outbound traffic and let workloads communicate outside of the organization.

By default, Google Distributed Cloud (GDC) air-gapped blocks workloads in a project from going out of the organization. Workloads can exit the organization if your Platform Administrator (PA) has disabled data exfiltration protection for the project. PAs can do so by attaching the label `networking.gdc.goog/enable-default-egress-allow-to-outside-the-org: "true"` to the project. In addition to disabling data exfiltration protection, the Application Operator (AO) must add the label `egress.networking.gke.io/enabled: true` on the pod workload to enable egress connectivity for that pod. When you allocate and use a well-known IP address for the project, it performs a source network address translation (NAT) on the outbound traffic from the organization.

You can manage egress connectivity from workloads in a pod or a VM.

## Manage outbound traffic from workloads in a pod

To configure workloads in a pod for egress connectivity, first you must ensure [data exfiltration protection is disabled for the project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/data-exfiltration#disable-data-exfiltration-protection). Then, ensure that the `egress.networking.gke.io/enabled: true` label is added on the pod. If you are using a higher-level construct like `Deployment` or `Daemonset` constructs to manage sets of pods, then you must configure the pod label in those specifications.

The following example shows how to create a `Deployment` from its manifest file. The sample file contains the value `egress.networking.gke.io/enabled: true` on the `labels` field to explicitly enable outbound traffic from the project. This label is added to each pod in the deployment and allows workloads in the pods to exit the organization.
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG \
        apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: DEPLOYMENT_NAME
    spec:
      replicas: NUMBER_OF_REPLICAS
      selector:
        matchLabels:
          run: APP_NAME
      template:
        metadata:
          labels: # The labels given to each pod in the deployment, which are used
                  # to manage all pods in the deployment.
            run: APP_NAME
            egress.networking.gke.io/enabled: true
        spec: # The pod specification, which defines how each pod runs in the deployment.
          containers:
          - name: CONTAINER_NAME
            image: CONTAINER_IMAGE
    EOF
    

Replace the following:

  * `USER_CLUSTER_KUBECONFIG`: the kubeconfig file for the user cluster to which you're deploying container workloads.

  * `DEPLOYMENT_NAME`: the kubeconfig file for the user cluster to which you're deploying container workloads.

  * `APP_NAME`: the name of the application to run within the deployment.

  * `NUMBER_OF_REPLICAS`: the number of replicated `Pod` objects that the deployment manages.

  * `CONTAINER_NAME`: the name of the container.

  * `CONTAINER_IMAGE`: the name of the container image. You must include the container registry path and version of the image, such as `REGISTRY_PATH/hello-app:1.0`.




For example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
      selector:
        matchLabels:
          run: my-app
      template:
        metadata:
          labels:
            run: my-app
            egress.networking.gke.io/enabled: true
        spec:
          containers:
          - name: hello-app
            image: REGISTRY_PATH/hello-app:1.0
    

## Manage outbound traffic from workloads in a VM

To configure workloads in a VM for egress connectivity, you can use the GDC console for VM configuration or create a `VirtualMachineExternalAccess` resource. For information about how to enable a VM with external access for data transfer, see [Enable external access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/ip-addresses#enable-external-access) on the _Connect to VMs_ section.

## Migrate to Cloud NAT

With Cloud NAT becoming available in version 1.15, the default project egress NAT configuration per project becomes deprecated. It's recommended that users migrate their egress configurations from the default project egress NAT configuration to Cloud NAT.

Default project egress NAT and Cloud NAT are not compatible with each other. In other words, a given pod or VM endpoint can only use one of the two. To migrate endpoints from one configuration to the other, you must disable them from one and then enable them in the other.

To begin your migration, disable the older configuration from the endpoints you want to migrate. There are two ways to do this:

  * **Disable project default egress NAT for the entire project** : disable project default egress NAT for all the endpoints that are in the project by assigning the label `networking.gdc.goog/allocate-egress-ip: "false"` to the project.
  * **Disable project default egress NAT per endpoint** : disable project default egress NAT for a particular pod or VM endpoint by removing the label `egress.networking.gke.io/enabled:"true"` from the pod or VM.



To continue the migration, as each endpoint is removed from the default egress NAT, it can be added to a Cloud NAT gateway by adding labels to the endpoint that match the label selectors of the chosen gateway.

See [Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat) and the following pages for instructions on how to set up Cloud NAT.

### Egress IP tracking

With default egress NAT the egress IPs used to NAT egress traffic are included in the Project's status. With Cloud NAT, the Project object won't contain any egress IPs. Instead the user will be able to list the IPs used by the Cloud NAT gateway by listing the subnets assigned to the gateway.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
