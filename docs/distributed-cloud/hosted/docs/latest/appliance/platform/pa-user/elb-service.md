---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/elb-service/
title: Configure external load balancers \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:56.534480+00:00
---

# Configure external load balancers  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/elb-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure external load balancers Stay organized with collections  Save and categorize content based on your preferences. 

External load balancers (ELB) expose services outside the project from a pool's IP addresses assigned to the project from the larger instance-external IP pool.

ELB Virtual IP (VIP) addresses don't conflict between organizations and are unique across all organizations. For this reason, you must use ELB services only for services that clients outside the project necessarily have to access.

Workloads running inside the project can access ELB services as long as you enable the workloads to exit the project. This traffic pattern effectively requires outbound traffic from the project before returning to the internal service.

## Before you begin

To configure ELB services, you must have the following:

  * Own the project you are configuring the load balancer for. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project).
  * A customized `ProjectNetworkPolicy` (PNP) ingress policy to allow traffic to this ELB service. For more information, see Configure PNP to allow traffic to ELB.
  * The necessary identity and access roles:

    * Project NetworkPolicy Admin: has access to manage project network policies in the project namespace Ask your Organization IAM Admin to grant you the Project NetworkPolicy Admin (`project-networkpolicy-admin`) role.
    * Load Balancer Admin: Ask your Organization IAM Admin to grant you the Load Balancer Admin (`load-balancer-admin`) role.



## Configure PNP to allow traffic to ELB

For ELB services to function, you must configure and apply your own customized `ProjectNetworkPolicy` ingress policy to allow traffic to this ELB service. Specify the external CIDR address to allow traffic to this ELB:
    
    
    kubectl --kubeconfig MANAGEMENT_API_SERVER apply -f - <<EOF
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT
      name: allow-inbound-traffic-from-external
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - ipBlock:
            cidr: CIDR
        ports:
        - protocol: TCP
          port: PORT
    EOF
    

Replace the following:

  * `MANAGEMENT_API_SERVER`: the kubeconfig path of the Management API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server in your targeted zone, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#cli) for details.
  * `PROJECT`: the name of your GDC project.
  * `CIDR`: the external CIDR that the ELB needs to be accessed from. This policy is required as the external load balancer uses Direct Server Return (DSR), which preserves the source external IP address and bypasses the load balancer on the return path.
  * `PORT`: the backend port on the pods behind the load balancer. This value is found in the `.spec.ports[].targetPort`field of the manifest for the `Service` resource.

**Note:** This configuration provides all of the resources inside of projects access to the specified CIDR range.

## Create an external load balancer

Create ELBs using three different methods in GDC:

  * Use the [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview) to create ELBs.
  * Use the [Networking Kubernetes Resource Model (KRM) API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/networking-api-overview) to create ELBs.



You can target pod or VM workloads using the KRM API and gdcloud CLI. You can only target workloads in the cluster where the `Service` object is created when you use the Kubernetes Service directly in Kubernetes cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
