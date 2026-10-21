---
url: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/private-cluster-open-port/
title: Open ports on a private cluster \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:00.379846+00:00
---

# Open ports on a private cluster  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/private-cluster-open-port/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Open ports on a private cluster

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

If you are [installing in-cluster Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install-anthos-service-mesh) on a private cluster, you must open port 15017 in the firewall to get the webhooks used with [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-workloads#inject_sidecar_proxies) (auto-injection) and configuration validation to work.

The following steps describe how to [add a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules) to include the new ports that you want to open.

  1. Find the source range (`master-ipv4-cidr`) and targets of the cluster. In the following command, replace `CLUSTER_NAME` with the name of your cluster:
         
         gcloud compute firewall-rules list \
             --filter 'name~gke-CLUSTER_NAME-[0-9a-z]*-master' \
             --format 'table(
                 name,
                 network,
                 direction,
                 sourceRanges.list():label=SRC_RANGES,
                 allowed[].map().firewall_rule().list():label=ALLOW,
                 targetTags.list():label=TARGET_TAGS
             )'
         

  2. Create the firewall rule. Choose from the following commands and replace `CLUSTER_NAME` with the name of the cluster of the previous command.

     * To enable auto-injection, run the following command to open port 15017:
           
           gcloud compute firewall-rules create allow-api-server-to-webhook-CLUSTER_NAME \
             --action ALLOW \
             --direction INGRESS \
             --source-ranges CONTROL_PLANE_RANGE \
             --rules tcp:15017 \
             --target-tags TARGET
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster
       * `CONTROL_PLANE_RANGE`: the cluster control plane's IP address range (`masterIpv4CidrBlock`) that you collected previously.
       * `TARGET`: the target (`Targets`) value that you collected previously.
**Note** : To add a firewall rule for a Shared VPC, add the following flags to the command: 
    
    --project HOST_PROJECT_ID
    --network NETWORK_ID
    

For more information on Shared VPC, see [Setting up clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules).

     * If you also want to enable the `istioctl version` and `istioctl ps` commands, run the following command to open ports 15014, and 8080:
           
           gcloud compute firewall-rules create allow-debug-proxy-CLUSTER_NAME \
             --action ALLOW \
             --direction INGRESS \
             --source-ranges CONTROL_PLANE_RANGE \
             --rules tcp:15014,tcp:8080 \
             --target-tags TARGET
           

Replace the following:

       * `CLUSTER_NAME`: the name of your cluster
       * `CONTROL_PLANE_RANGE`: the cluster control plane's IP address range (`masterIpv4CidrBlock`) that you collected previously.
       * `TARGET`: the target (`Targets`) value that you collected previously.
**Note** : To add a firewall rule for a Shared VPC, add the following flags to the command: 
    
    --project HOST_PROJECT_ID
    --network NETWORK_ID
    

For more information on Shared VPC, see [Setting up clusters with Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#add_firewall_rules).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
