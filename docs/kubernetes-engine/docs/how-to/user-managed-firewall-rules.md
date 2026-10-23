---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules/
title: User-managed firewall rules for GKE LoadBalancer Services \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:39.319551+00:00
---

# User-managed firewall rules for GKE LoadBalancer Services  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  User-managed firewall rules for GKE LoadBalancer Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how to disable the ingress allow [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that GKE creates for LoadBalancer Services.

Disabling these automatically created firewall rules for LoadBalancer Services can be useful in the following situations:

  * If you have multiple LoadBalancer Services in two or more GKE clusters, managing firewall rules yourself can be more efficient. For example, instead of having GKE create a unique firewall rule for each LoadBalancer Service, your manually created firewall rules can allow inbound traffic for multiple LoadBalancerServices.
  * You can use [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies), [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies), or [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies) instead of VPC firewall rules. Rules in these firewall policies support [additional actions](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#action_on_match), [more flexible targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets), and features like [geolocation](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview), [threat intelligence](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview), [address groups](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies), and [FQDNs](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview).



To disable automatically created firewall rules for LoadBalancer Services, you must specify the `--disable-l4-lb-firewall-reconciliation` flag when you create or update a cluster. The `--disable-l4-lb-firewall-reconciliation` flag does not affect other automatically created VPC firewall rules, such as those facilitating communication between nodes or those that permit health checks for your Services.

## Requirements

  * To use User-managed firewall rules for LoadBalancer Services, your GKE clusters must use version 1.31.3-gke.105600 or later.



## Limitations

GKE supports disabling the automatic creation of firewall rules for these types of LoadBalancer Services:

  * [Internal LoadBalancer Services using GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)
  * [Backend service-based external LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer)



You cannot disable the automatic creation of firewall rules for these types of LoadBalancer Services:

  * Internal LoadBalancer Services not using GKE subsetting
  * Target pool-based external LoadBalancer Services



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Strategies for manual firewall rule management

Before you disable automatic creation of VPC firewall rules for LoadBalancer Services in your GKE cluster, work with a Security Admin to develop a strategy for configuring firewall rules manually.

  1. Decide which type of firewall policy to use: a hierarchical firewall policy, a global network firewall policy, or a regional network firewall policy. For steps to create a firewall policy, see:

     * [Use hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies)
     * [Use global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies)
     * [Use regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies)

You can also use VPC firewall rules, which don't use any policy.

  2. Your manually created firewall rules must be ingress allow rules because the [implied deny ingress firewall rule](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules) prohibits incoming traffic. When you've disabled the automatic creation of VPC firewall rules, incoming traffic won't reach your nodes unless you've created ingress allow firewall rules that match traffic for your LoadBalancer Services.

Depending on the firewall rule's parameters, a single ingress allow firewall rule can apply to one or more LoadBalancer Services. For each ingress allow firewall rule you create, define the following parameters:

     * _Target parameter_ : Ensure that the firewall rule at least includes all nodes of the cluster that contains the LoadBalancer Services. Supported targets depend on what type of firewall policy a rule is located in or if you're using a VPC firewall rule. For information about the target parameter of a rule in a firewall policy, see [Targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets).

     * _Protocols and ports_ : Include all protocols and destination ports used by the LoadBalancer Services to which the firewall rule needs to apply.

     * _Destination parameter_ : You can employ one of the following strategies for the [destination parameter](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest):

       * Include the IP addresses of all LoadBalancer Services to which the firewall rule needs to apply in the destination parameter. To find the IP address of a LoadBalancer Service, use the following command:
    
    kubectl get svc LOADBALANCER_NAME \
          -n NAMESPACE_NAME \
          -o jsonpath='{.status.loadBalancer.ingress[0].ip}
    

       * You can choose to omit the destination parameter. When the destination parameter is omitted, the target parameter defines the destinations implicitly. For more information, see [Targets and IP addresses for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets_and_ips_ingress).
     * _Source parameter_ : Specify the sources (for example, IP addresses) used by clients that need to connect to the Load Balancer Serfices to which the firewall rule needs to apply.

For steps to create firewall rules, see:

     * [Create firewall rules in a hierarchical firewall policy](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-rules)
     * [Create global network firewall policy rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-rules)
     * [Create regional network firewall policy rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-rules)
     * [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules)
  3. To ensure that your manually created firewall rules are working correctly, run a [Network Intelligence Center (NIC) Connectivity Test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests#testing-lb). When running the Connectivity Test:

     * Set the destination to the IP address of the LoadBalancer Service.
     * Set the source to the IP address of the client.

For more information, see Troubleshoot connectivity issues.




## Disable creation of VPC firewall rules for your LoadBalancer Services

This section describes steps to disable the automatic creation of VPC firewall rules for LoadBalancer Services.

### Create a new GKE cluster with VPC firewall rules creation disabled

  1. To disable the automatically created VPC firewall rules for LoadBalancer Services in a newly created cluster, create the cluster with the `--disable-l4-lb-firewall-reconciliation` flag:

**Autopilot:**
         
         gcloud container clusters create-auto CLUSTER_NAME \
           --disable-l4-lb-firewall-reconciliation \
           --cluster-version=VERSION
         

**Standard:**
         
         gcloud container clusters create CLUSTER_NAME \
           --disable-l4-lb-firewall-reconciliation \
           --enable-l4-ilb-subsetting \
           --cluster-version=VERSION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the new cluster.
     * `VERSION`: the GKE version.
  2. Create an external or internal LoadBalancer Service:

     * [Create a backend service-based external load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).

     * [Create an internal load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).

  3. Verify that GKE doesn't create an ingress allow firewall rule for the LoadBalancer Service. (Automatically created ingress allow firewall rules have names of the following form: `k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]`).

The following command returns a list of firewall rules that contain `k8s2`:
         
         gcloud compute firewall-rules list --format="value(name)" | grep "k8s2"
         

The response should return only the health check firewall rule of the form `k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-fw` if the `externalTrafficPolicy` parameter is set to `Local`. It uses the TCP port defined by the `spec.healthCheckNodePort` parameter. If unspecified, the Kubernetes control plane assigns a health check port from the node port range.
         
         k8s2-rkdld6go-default-ilb-svc-dluvsefq-fw  default  INGRESS  1000  tcp:30868  False
         

If the `externalTrafficPolicy` parameter is set to `Cluster`, the following health check firewall rule is returned instead.
         
         k8s2-rkdld6go-l4-shared-hc-fw  default  INGRESS  1000  tcp:10256  False
         

For more information about generated firewall rules for GKE Services, see [Automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws).




### Update an existing GKE cluster to disable VPC firewall rules creation

Before disabling VPC firewall rules creation, note the following points about updating an existing cluster:

  * When you update an existing cluster to disable VPC firewall rules creation, GKE doesn't delete any existing firewall rules that GKE automatically created for your LoadBalancer Services.
  * GKE stops updating the existing rules and won't create new ones for the new LoadBalancer Services.
  * To turn VPC firewall rules creation back on, you can use the `--enable-l4-lb-firewall-reconciliation` flag with the `gcloud_name container clusters update` command.



To disable the automatic firewall rule creation on an existing cluster:

  1. Update the cluster to disable the automatic creation and management of firewall rules for LoadBalancer Services:
         
         gcloud container clusters update CLUSTER_NAME \
         --disable-l4-lb-firewall-reconciliation \
         --cluster-version=supported_version
         

Replace the following:

     * `CLUSTER_NAME`: the name of the new cluster.
     * `VERSION`: the GKE version.
  2. Create an external or internal LoadBalancer Service:

     * [Create a backend service-based external load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).

     * [Create an internal load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).

  3. Verify that GKE doesn't create an ingress allow firewall rule for the LoadBalancer Service. (Automatically created ingress allow firewall rules have names of the following form: `k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]`).

The following command returns a list of firewall rules that contain `k8s2`:
         
         gcloud compute firewall-rules list --format="value(name)" | grep "k8s2"
         

The response should return only the health check firewall rule of the form `k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-fw` if the `externalTrafficPolicy` parameter is set to `Local`. It uses the TCP port defined by the `spec.healthCheckNodePort` parameter. If unspecified, the Kubernetes control plane assigns a health check port from the node port range.
         
         k8s2-rkdld6go-default-ilb-svc-dluvsefq-fw  default  INGRESS  1000  tcp:30868  False
         

If the `externalTrafficPolicy` parameter is set to `Cluster`, the following health check firewall rule is returned instead.
         
         k8s2-rkdld6go-l4-shared-hc-fw  default  INGRESS  1000  tcp:10256  False
         

For more information about generated firewall rules for GKE Services, see [Automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#service-fws).




## Troubleshoot connectivity issues

The following examples illustrate how to use Network Intelligence Center Connectivity Tests to test connectivity to an external LoadBalancer Service:cluster:

  * Network Intelligence Center:

    1. In the Google Cloud console, go to the Network Intelligence Center and start a new connectivity test.
    2. From the drop-down menu, choose **Any external public IP address** as the source and select your load balancer from the destination.
    3. Re-run the connectivity test.
  * The gcloud CLI:

The following example command creates and runs a test with your local workstation's public IP address as the source and the external load balancer's external IP address as the destination:
        
        gcloud network-management connectivity-tests create TEST_NAME \
        --source-ip-address=SOURCE_IP_ADDRESS \
        --source-network-type=NON_GCP_NETWORK \
        --destination-ip-address=$(kubectl get svc LOADBALANCER_NAME -o jsonpath='{.status.loadBalancer.ingress[0].ip}') \
        --destination-port=$(kubectl get svc LOADBALANCER_NAME -o jsonpath='{.spec.ports[0].targetPort}') \
        --destination-network=projects/PROJECT_ID/global/networks/NETWORK_NAME \
        --round-trip
        

Replace the following:

    * `TEST_NAME`: A name for the connectivity test.
    * `SOURCE_IP_ADDRESS`: The IP address of the system that needs to connect to the external LoadBalancer Service. For example
    * `LOADBALANCER_NAME`: The name of the external LoadBalancer Service.
    * `PROJECT_ID`: The project ID of the project that contains the cluster's VPC network. If your cluster uses a Shared VPC network, use the project ID of the host project.
    * `NETWORK_NAME`: The name of your cluster's VPC network.

Check test results:
    
    gcloud network-management connectivity-tests describe TEST_NAME
    




## What's next

  * Learn more about [Firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).
  * Read [Automatically created firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules) for an overview of the ingress allow VPC firewall rules that GKE automatically creates by default.
  * Read [LoadBalancer Service parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters) for a description of parameters for LoadBalancer Services.
  * Learn about other [Pre-populated firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc) in Google Cloud.
  * Learn more about [Creating firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#creating_firewall_rules) in projects that use Shared VPC.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
