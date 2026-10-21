---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/upgrade-vmware/
title: Upgrading Knative serving on VMware to fleets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:21:25.637245+00:00
---

# Upgrading Knative serving on VMware to fleets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/upgrade-vmware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Upgrading Knative serving on VMware to fleets Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to migrate Knative serving on VMware to use fleets so that you can upgrade to Anthos Version 1.8.

**Important:** Anthos Version 1.8 requires that all past installations of Knative serving on VMware are migrated to use [fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets). You must migrate Knative serving before upgrading your GKE clusters to Version 1.8. 

If you choose to remain on Anthos Version 1.7 or earlier, you are not required to migrate your installation immediately. However, starting with Anthos 1.8, new installations and upgrades to Knative serving are only available through fleets. 

Knative serving is now a separate experience from the managed [Cloud Run](https://docs.cloud.google.com/run) product and is now provided as a fleet component in your clusters. Installing Knative serving on VMware features as a component of your fleet enables you to manage and upgrade your installation independently of other fleet components.

At a high-level, to migrate your Knative serving on VMware installation to use a fleet, you must:

  * Configure your Knative serving on VMware installation to meet the fleet requirements.
  * Enable the Knative serving feature component in your fleet.



Note that the Kubernetes API server is not impacted during this migration.

For details about how to perform a new installation of Knative serving on VMware, see [Installing Knative serving on VMware](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp).

## Before you begin

You must meet the following requirements:

  * These steps require that your Knative serving on VMware cluster is registered to a fleet and is visible in the Google Cloud console:

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  * Your installation of Knative serving on VMware is on a cluster running Anthos Version 1.7 or earlier.

  * Istio is no longer supported in Anthos 1.8. Cloud Service Mesh version 1.19 must be installed in your fleet and your installation of Knative serving must be configured before you upgrade that cluster to Version 1.8.

See the Cloud Service Mesh instructions for details about [installing on Google Distributed Cloud](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh#on-premises).

Note that Cloud Service Mesh requires that your cluster uses a machine type that has at least four vCPUs, such as `e2-standard-4`. If you need to change your cluster's machine type, see [Migrating workloads to different machine types](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrating-node-pool).

  * There are two options for migrating Knative serving to Cloud Service Mesh, you can either:

    * Obtain a new external IP address to which you configure the load balancer.

    * Reuse your existing load balancer IP address.

**Warning:** The process of reusing an existing IP address to configure Cloud Service Mesh causes approximately 2 minutes of connection downtime. You should plan to accommodate this period during which your Knative serving services are unable to connect.
  * [Ensure that your command-line environment is configured and up-to-date](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/command-line-tools).




## Migrate to fleets

In order to upgrade Anthos to Version 1.8, you must first perform the following steps to ensure that your existing Knative serving on VMware installation is migrated to using the fleet component.

**Important:** Most of the steps in this process require that you configure each of your user clusters and therefore, must repeat several steps for each of those clusters.

### Access your admin cluster

Obtain the path and file name of your admin cluster's kubeconfig file and then create the `ADMIN_KUBECONFIG` environment variable:
    
    
    export ADMIN_KUBECONFIG=[ADMIN_CLUSTER_KUBECONFIG]
    

Replace [ADMIN_CLUSTER_KUBECONFIG] with the path and file name to the [kubeconfig file of your admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/create-admin-cluster#create-admin-cluster).

### Configure each user cluster

**Important:** If you have multiple user clusters, you must repeat the steps in this section for each user cluster.

  1. Create the following local environment variables for the user cluster:

     1. Create the `USER_KUBECONFIG` environment variable with the path of your user cluster's kubeconfig file:
            
            export USER_KUBECONFIG=[USER_CLUSTER_KUBECONFIG]
            

Replace [USER_CLUSTER_KUBECONFIG] with the path and file name to the [kubeconfig file of your user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/how-to/create-user-cluster#create-user-cluster).

     2. Create environment variables for the following configurations:

        * ID of your Google Cloud project.
        * Location of your Google Cloud resources.
        * Name of the user cluster.
    
    export PROJECT_ID=$(kubectl get configmaps --namespace knative-serving config-observability --output jsonpath="{.data['metrics\.stackdriver-project-id']}")
    export CLUSTER_LOCATION=$(kubectl get configmaps --namespace knative-serving config-observability --output jsonpath="{.data['metrics\.stackdriver-gcp-location']}")
    export CLUSTER_NAME=$(kubectl get configmaps --namespace knative-serving config-observability --output jsonpath="{.data['metrics\.stackdriver-cluster-name']}")
    

  2. Remove the `cloudrun` configuration from the `OnPremUserCluster` custom resource of your user cluster:

     1. Verify that `cloudRun` is set in `OnPremUserCluster`:
            
            $ kubectl get onpremusercluster \
              "${CLUSTER_NAME}" \
              --namespace "${CLUSTER_NAME}-gke-onprem-mgmt" \
              --kubeconfig="${ADMIN_KUBECONFIG}" \
              --output=jsonpath="{.spec.cloudRun}"
            

Result:
            
            {"enabled":true}
            

     2. Remove `cloudRun` from `OnPremUserCluster`:
            
            kubectl patch onpremusercluster \
              "${CLUSTER_NAME}" \
              --namespace "${CLUSTER_NAME}-gke-onprem-mgmt" \
              --kubeconfig="${ADMIN_KUBECONFIG}" \
              --type="merge" \
              --patch '{"spec": {"cloudRun": null}}'
            

     3. Validate that `cloudRun` was successfully removed from `OnPremUserCluster` by running the same `get` command and verifying that no configuration is returned:
            
            kubectl get onpremusercluster \
              "${CLUSTER_NAME}" \
              --namespace "${CLUSTER_NAME}-gke-onprem-mgmt" \
              --kubeconfig="${ADMIN_KUBECONFIG}" \
              --output=jsonpath="{.spec.cloudRun}"
            

There should be no output to your terminal.

  3. Update the create-config secret of your user cluster:

     1. Create a local YAML copy of the create-config file:
            
            kubectl get secret create-config \
              --kubeconfig="${ADMIN_KUBECONFIG}" \
              --namespace "${CLUSTER_NAME}" \
              --output=jsonpath={.data.cfg} \
              | base64 -d > "${CLUSTER_NAME}_create_secret.yaml"
            

     2. Open the `${CLUSTER_NAME}_create_secret.yaml` file that you just created in an editor and then remove the `cloudrun` field from under `spec`.

     3. Base64 encode the `${CLUSTER_NAME}_cluster_create_secret.yaml` file into a `.b64` file:
            
            cat "${CLUSTER_NAME}_create_secret.yaml" | base64 -w0 > "${CLUSTER_NAME}_create_secret.b64"
            

     4. In your editor, open the local `.b64` file that you just created and then copy the string from under the `data.cfg` attribute for use in the next step.

You must ensure that you copy only the contents from the `cfg` attribute. For example, do not include any newlines (`\n`).

     5. Run the following command to [edit the secret](https://kubernetes.io/docs/concepts/configuration/secret/#editing-a-secret) on your user cluster:
            
            kubectl edit secret create-config --kubeconfig="${ADMIN_KUBECONFIG}" \
              --namespace "${CLUSTER_NAME}"
            

     6. In the editor that opens, replace the `data[cfg]` field with the the string that you copied from the local `.b64` file and then save your changes.

     7. Verify that your changes are deployed to your user cluster and that the `cloudrun` attribute was successfully removed from the `create-config` secrets:
            
            kubectl get secret create-config \
              --kubeconfig="${ADMIN_KUBECONFIG}" \
              --namespace ${CLUSTER_NAME} \
              --output=jsonpath={.data.cfg} \
              | base64 -d
            

  4. Configure the `knative-serving` namespace in your user cluster:

     1. Delete the `cloudrun-operator` operator from the `knative-serving` namespace:
            
            kubectl delete deployments.apps --kubeconfig=${USER_KUBECONFIG} --namespace knative-serving cloudrun-operator
            

     2. Patch the `config-network` configmap in the `knative-serving` namespace:
            
            kubectl patch configmap --kubeconfig=${USER_KUBECONFIG} --namespace knative-serving config-network --patch '{"metadata": {"annotations":{"knative.dev/example-checksum": null}}}'
            

  5. If you have multiple user clusters, you must repeat all the steps in this "_Configure each user cluster_" section for each user cluster.




### Configure your fleet component

  1. Enable the Knative serving component in your fleet:
         
         gcloud container fleet cloudrun enable --project=$PROJECT_ID
         

For details and additional options, see the [gcloud container fleet cloudrun enable](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun/enable) reference.

  2. Optional: Verify that the Knative serving feature component is enabled:

### Console

View if the Knative serving component is **Enabled** in the Google Cloud console:

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features)

### Command line

View if the `appdevexperience` state is `ENABLED`:
         
         gcloud container fleet features list --project=$PROJECT_ID
         

For details and additional options, see the [gcloud container fleet features list](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/features/list) reference.

Result:
         
         NAME               STATE
         appdevexperience   ENABLED
         

  3. Deploy the `CloudRun` custom resource to install Knative serving on VMware on each of your user clusters. By default, the `latest` version of Knative serving is deployed.

**Important:** If you have multiple user clusters, you must repeat this step for each user cluster.

Run the following `kubectl apply` command to deploy the default configuration of the `CloudRun` custom resource:
         
         cat <<EOF | kubectl apply -f -
         apiVersion: operator.run.cloud.google.com/v1alpha1
         kind: CloudRun
         metadata:
           name: cloud-run
         spec:
           metricscollector:
             stackdriver:
               projectid: $PROJECT_ID
               gcpzone: $CLUSTER_LOCATION
               clustername: $CLUSTER_NAME
               secretname: "stackdriver-service-account-key"
               secretkey: "key.json"
         EOF
         




### Configure Cloud Service Mesh

Configure the Cloud Service Mesh load balancer for each of your user clusters.

**Important:** If you have multiple user clusters, you must repeat the steps in this section for each user cluster.

You can configure the ingress gateway of Cloud Service Mesh by either configuring a new external IP address or reusing your existing IP address:

  * With the new external IP address that you obtained, you configure the load balancer by following the steps in the [Cloud Service Mesh documentation](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/external-ip-load-balance).

Note that this option ensures that your Knative serving services are [restarted without interruption](https://kubernetes.io/docs/concepts/workloads/pods/#pod-update-and-replacement).

  * Alternative: Use the following steps to configure the Cloud Service Mesh load balancer to your existing IP address.

**Warning:** Migrating to Cloud Service Mesh by using your existing IP address causes approximately 2 minutes of connection downtime. You should plan to accommodate this period during which your Knative serving services are unable to connect.
    1. Configure the gateway of your services to Cloud Service Mesh by running the following commands:
           
           export CURRENT_INGRESS_IP=$(kubectl get service --namespace gke-system istio-ingress --output jsonpath='{.spec.loadBalancerIP}')
           kubectl patch service --namespace istio-system istio-ingressgateway --patch "{\"spec\":{\"loadBalancerIP\": \"$CURRENT_INGRESS_IP\"}}"
           kubectl patch service --namespace gke-system istio-ingress --patch "{\"spec\":{\"loadBalancerIP\": null}}"
           

    2. Remove the current Istio configuration settings:
           
           kubectl patch configmap --namespace knative-serving config-istio --patch '{"data":{"local-gateway.cluster-local-gateway": null}}'
           kubectl patch configmap --namespace knative-serving config-istio --patch '{"data":{"gateway.gke-system-gateway": null}}'
           




### Verify migration

You can check to see if the `appdevexperience-operator` is up and running to verify that your Knative serving on VMware has been successfully migrated to your fleet.

For each user cluster, run the following command:
    
    
     kubectl get deployment -n appdevexperience appdevexperience-operator

The `appdevexperience-operator` [operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) should show `1/1` as ready, for example:
    
    
     NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
     appdevexperience-operator   1/1     1            1           1h
    

If the operator fails to achieve the ready state, you can view your cluster's workloads page in the Google Cloud console to identify resource issues:

[Go to Google Kubernetes Engine workloads](https://console.cloud.google.com/kubernetes/workload)

## Upgrade your cluster

Now that you have migrated your Knative serving on VMware installation to use the fleet component, you can upgrade your cluster to Anthos Version 1.8. Follow the detailed instructions in [Upgrading GKE On-Prem](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.8/how-to/upgrading).

### Troubleshooting

Upgrade process of your user cluster fails to complete
    

The `cluster-local-gateway` pod in the`gke-system` namespace might prevent your user cluster from completing the upgrade to Anthos Version 1.8. The `cluster-local-gateway` pod is no longer needed and can be safely removed.

To manually assist the upgrade process, you can manually remove the `cluster-local-gateway` pod by scaling down your deployment replicas to `0`. For example:

  1. Scale down the `cluster-local-gateway`:
         
         kubectl scale deployment cluster-local-gateway --replicas 0 --namespace gke-system
         

The `cluster-local-gateway` pod in the`gke-system` namespace and all workloads in the `knative-serving` namespace are removed.

  2. Wait for the upgrade process to complete.




[Learn more about scaling deployments](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps#scale).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
