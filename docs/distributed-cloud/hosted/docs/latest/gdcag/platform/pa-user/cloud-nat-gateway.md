---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-gateway/
title: Create a Cloud NAT gateway \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:53.719376+00:00
---

# Create a Cloud NAT gateway  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a Cloud NAT gateway Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

In this use case we will create a Cloud NAT gateway with multiple egress IPs assigned. These gateways will egress traffic from the pods and VMs that match the matching labels configured in the gateway. The gateway will automatically assign an egress IP to each endpoint that can egress traffic through it.

![Example gateway setup with multiple egress IPs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/images/cloudnat-gateway.png)

## Prerequisites

Before setting up a gateway, you must get appropriate Identity and Access Management (IAM) permissions ensure that your project has an appropriate network policy, and enable egress.

See [Before you begin with Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-prereqs) for details.

The Cloud NAT gateway uses external `leaf` subnets as inputs. For more information about configuring external subnets for Cloud NAT, see [Create external subnets for Cloud NAT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-subnets).

**Note:** Leaf subnets can be of any size, `/32`, `/30`, or `/20`, as long as the parent subnet has enough available IP addresses.

## Ensure a compatible pod or VM configuration

As mentioned in the [NAT Overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-overview), Cloud NAT is not compatible with the default project egress configuration. Ensure that any pod or VM that you want to use with Cloud NAT does NOT have the label `egress.networking.gke.io/enabled:true`.

By default, a Virtual Machine External Access (VMEA) configures a VM to egress traffic using the default project egress configuration. In other words it automatically adds the label `egress.networking.gke.io/enabled:"true"` to the VM. If said VM is configured to egress traffic using a Cloud NAT gateway as well, this results in a collision between NAT configurations. To avoid this collision: for every VMEA associated with a VM that is configured to egress traffic through a Cloud NAT gateway, ensure that the VMEA associated with that VM has the annotation `egress.networking.gke.io/use-cloud-nat:"true"`. The associated VM will then egress traffic exclusively through the Cloud NAT gateway.

## Create the Cloud NAT gateways

The following example defines a Cloud NAT gateway with two external leaf subnets (`subnet-1` and `subnet-2`). The gateway will use all the IPs in those subnets, one from `subnet-1` and four from the `subnet-2`, and automatically assign them to the endpoints from each VM or pod with the specified labels. Multiple pods or VMs can get the same egress IP assigned.
    
    
    apiVersion: networking.gdc.goog/v1
    kind: CloudNATGateway
    metadata:
      namespace: project-1
      name: gateway-1
    spec:
      workloadSelector:  # Immutable
        labelSelector:
          workloads:
            matchLabels:
              app: aa
      subnetRefs:        # Mutable
      - subnet-1
      - subnet-2
    

## Check the status of the gateways

Check the status of the gateways by running the following `kubectl` command.
    
    
    export MGMT_KUBECONFIG=<path_to_management_kubeconfig>
    kubectl get cloudnatgateways gateway-1 -n project-1 --kubeconfig "${MGMT_KUBECONFIG:?}"
    

If configured correctly, the Cloud NAT gateway's status condition field should show the condition of the type `Ready` set to `true` and the subnets marked as `OK`, as shown in the following example output.
    
    
    apiVersion: networking.gdc.goog/v1
    kind: CloudNATGateway
    metadata:
      namespace: project-1
      name: gateway-1
    spec:
      workloadSelector:
        labelSelector:
          workloads:
            matchLabels:
              app: aa
      subnetRefs:
      - subnet-1
      - subnet-2
    status:
      conditions:
      - lastTransitionTime: "2025-08-20T21:31:36Z"
        message: ""
        observedGeneration: 1
        reason: Ready
        status: "True"
        type: Ready
      - lastTransitionTime: "2025-08-20T21:31:36Z"
        message: ""
        observedGeneration: 1
        reason: Ready
        status: "True"
        type: SubnetsReady
      - lastTransitionTime: "2025-08-20T21:31:36Z"
        message: ""
        observedGeneration: 1
        reason: Ready
        status: "True"
        type: PerimeterConfigurationReady
      - lastTransitionTime: "2025-08-20T21:31:36Z"
        message: ""
        observedGeneration: 1
        reason: Ready
        status: "True"
        type: EgressRoutesReady
      subnets:
      - name: subnet-1
        status: OK
      - name: subnet-2
        status: OK
    

The Cloud NAT gateway status contains 4 conditions of the following types:

  * `Ready`: This condition summarizes the status of the Cloud NAT gateway. This condition is set to true if the gateway is fully set up.
  * `SubnetsReady`: This condition indicates whether the subnets assigned to the gateway are valid.
  * `PerimeterConfigurationReady`: This condition indicates whether the perimeter configuration has already been configured (e.g. external IPs assigned to externally-facing nodes, etc).
  * `EgressRoutesReady`: This condition indicates whether the routes to egress traffic from the source endpoints have been already configured.



## Test Traffic

We can test the traffic by issuing a `curl` command from one of the pods or VMs assigned to the gateway towards an external endpoint. The receiving endpoint should see one of the egress IPs associated with the gateway.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
