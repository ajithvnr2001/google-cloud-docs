---
url: https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem/
title: Set up for on-premises clusters \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:11.427562+00:00
---

# Set up for on-premises clusters  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/setting-up-on-prem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Set up for on-premises clusters Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This manual installation guide is deprecated. For modern clusters, Binary Authorization is managed automatically through cluster configuration. For Distributed Cloud for VMware (version 1.28 or later), see [Set up Binary Authorization policy enforcement on VMware](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy). For Distributed Cloud on bare metal (version 1.16 or later), see [Set up Binary Authorization policy enforcement on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/binary-authorization-policy).

If you previously followed this manual guide, you must clean up the legacy resources before enabling the feature in your cluster configuration.

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This document shows you how to set up [Binary Authorization for on-premises clusters](https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem) created as part of Google Distributed Cloud. It then shows you how to configure a sample Binary Authorization policy.

## Before you begin

  1. Ensure your clusters have a supported Google Distributed Cloud version. Binary Authorization supports the following environments.

###  Bare metal 

[Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/creating-clusters/create-clusters-overview) 1.14 or 1.15. For version 1.16 or later, Binary Authorization can be [configured during a cluster creation or update](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/binary-authorization-policy).

###  VMware 

[Google Distributed Cloud software only for VMware (Google Distributed Cloud)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview) 1.4 to 1.27. For version 1.28 or later, Binary Authorization can be [configured during a cluster creation or update](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/binary-authorization-policy).

  2. The Binary Authorization service uses a external IP address, accessible through a regular internet connection. Configure your firewall rules for HTTPS to let the user cluster access the endpoint `binaryauthorization.googleapis.com`.

###  Bare metal 

Configure [Google Distributed Cloud firewall rules](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/proxy#firewall_rules).

###  VMware 

Configure [Google Distributed Cloud firewall rules](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/firewall-rules).

  3. If you want to use centralized [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) to view audit log entries, including those from Binary Authorization for clusters outside Google Cloud, you must configure Cloud Audit Logs in your cluster configuration.

###  Bare metal 

Configure Cloud Audit Logs in [Google Distributed Cloud software only for bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/audit-logging).

###  VMware 

Configure Cloud Audit Logs in [Google Distributed Cloud](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/audit-logging).

  4. You must enable the Binary Authorization API as follows:

     1. Go to Google Cloud console.

[ Enable APIs ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,containeranalysis.googleapis.com,binaryauthorization.googleapis.com)

     2. In the project drop-down list, select your fleet host project. You can find this in the [`gkeConnect` section](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file#gkeconnect-section) of your user cluster configuration file. This is the Google Cloud project that connects your user cluster to Google Cloud.




## Set up Binary Authorization

In this section, you set up Binary Authorization in your on-premises cluster.

### Specify installation environment variables

To specify the environment variables, do the following:

###  Using Workload Identity 

  1. Specify your fleet host project:
         
         export PROJECT_ID=PROJECT_ID
         

  2. Set the fleet membership ID to your cluster ID:

The membership ID is listed in the `NAME` column when you run `gcloud container fleet memberships list` command.
         
         export MEMBERSHIP_ID=CLUSTER_NAME
         




###  Using service account key 

  1. Specify your fleet host project:
         
         export PROJECT_ID=PROJECT_ID
         

Replace PROJECT_ID with the Google Cloud project in the [`gkeConnect` section](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file#gkeconnect-section) of your user cluster configuration file.

  2. Specify the path of the user cluster's kubeconfig file:
         
         export KUBECONFIG=PATH
         

Replace PATH with the path of your user cluster kubeconfig file.

  3. Choose a name for the Binary Authorization API access service account:
         
         export SA_NAME=SERVICE_ACCOUNT_NAME
         

Replace SERVICE_ACCOUNT_NAME with the service account name of your choice. The Binary Authorization module uses this service account to access the Binary Authorization API.

  4. Specify the path to the service account key file you download later in this guide:
         
         export SA_JSON_PATH=SA_KEY_FILE_PATH
         

Replace SA_KEY_FILE_PATH with the path of the JSON key file for the service account.




### Install the Binary Authorization module in your user cluster

To install the Binary Authorization module, do the following:

###  Using Workload Identity 

Fleet Workload Identity lets the workloads in your cluster authenticate to Google without requiring you to download, manually rotate, and generally manage Google Cloud service account keys. You can find out more about how fleet Workload Identity works and the advantages of using it in [Use fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity).

  1. Grant the `binaryauthorization.policyEvaluator` role to the Kubernetes service account on your fleet host project:
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
             --member="serviceAccount:${PROJECT_ID}.svc.id.goog[binauthz-system/binauthz-admin]" \
             --role="roles/binaryauthorization.policyEvaluator"
         

  2. Create a working directory:

     1. Make a directory called `binauthz`.

     2. Change to the directory.

  3. Download the `manifest-wi-0.2.6.yaml.tmpl` file, which you use to install the Binary Authorization Module in your user cluster:

###  Bare metal 
         
         gcloud storage cp gs://anthos-baremetal-release/binauthz/manifest-wi-0.2.6.yaml.tmpl .
         

###  VMware 
         
         gcloud storage cp gs://gke-on-prem-release/binauthz/manifest-wi-0.2.6.yaml.tmpl .
         

  4. Substitute the environment variables in the template:
         
         envsubst < manifest-wi-0.2.6.yaml.tmpl > manifest-0.2.6.yaml
         

  5. Install the Binary Authorization Module in your user cluster:
         
         kubectl apply -f manifest-0.2.6.yaml
         

  6. Verify the Deployment was created:
         
         kubectl get pod --namespace binauthz-system
         

You see the Pod `binauthz-module-deployment-*` listed with `Status` of `Running` and 1/1 Pods ready, similar to this output:
         
         NAME                                          READY   STATUS    RESTARTS   AGE
         binauthz-module-deployment-5fddf9594f-qjprz   1/1     Running   0          11s
         




###  Using service account key 

  1. Set the default project for the Google Cloud CLI:
         
         gcloud config set project ${PROJECT_ID}
         

  2. Create a Binary Authorization API access service account:
         
         gcloud iam service-accounts create ${SA_NAME}
         

  3. Grant the `binaryauthorization.policyEvaluator` role to the Binary Authorization API access service account on your fleet host project:
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID}\
             --member="serviceAccount:${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
             --role="roles/binaryauthorization.policyEvaluator"
         

  4. Create a working directory:

     1. Make a directory called `binauthz`.

     2. Change to the directory.

  5. Download the `manifest-0.2.6.yaml` file, which you use to install the Binary Authorization Module in your user cluster:

###  Bare metal 
         
         gcloud storage cp gs://anthos-baremetal-release/binauthz/manifest-0.2.6.yaml .
         

###  VMware 
         
         gcloud storage cp gs://gke-on-prem-release/binauthz/manifest-0.2.6.yaml .
         

  6. Create a YAML file for the `binauthz-system` namespace.

Copy the following to a file called `namespace.yaml`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           labels:
             control-plane: binauthz-controller
           name: binauthz-system
         

  7. Create the namespace in your user cluster:
         
         kubectl apply -f namespace.yaml
         

You see output similar to the following:
         
         namespace/binauthz-system created
         

  8. Download a JSON key file for your service account:
         
         gcloud iam service-accounts keys create ${SA_JSON_PATH} --iam-account ${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
         

  9. Save the service account key as a Kubernetes Secret in your user cluster:
         
         kubectl --namespace binauthz-system create secret generic binauthz-sa --from-file=key.json=${SA_JSON_PATH}
         

  10. Install the Binary Authorization Module in your user cluster:
         
         kubectl apply -f manifest-0.2.6.yaml
         

  11. Verify the Deployment was created:
         
         kubectl get pod --namespace binauthz-system
         

You see the Pod `binauthz-module-deployment-*` listed with `Status` of `Running` and 1/1 Pods ready, similar to this output:
         
         NAME                                          READY   STATUS    RESTARTS   AGE
         binauthz-module-deployment-5fddf9594f-qjprz   1/1     Running   0          11s
         




## Set up and use Binary Authorization policies

This section shows you how to set up and use Binary Authorization policies for on-premises clusters.

In each example, you configure the policy and then test it by attempting to deploy a container image in your cluster.

### Allow all

This section demonstrates a success case. You configure the Binary Authorization policy so that a container image satisfies the policy and is deployed.

**Caution:** This policy allows all container images to deploy.

In Google Cloud, do the following:

###  Console 

  1. In the Google Cloud console, go to the Binary Authorization page.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. Make sure to select your fleet host project ID.

  3. Click **Edit Policy**.

  4. Under **Project default rule** , select **Allow all images**.

  5. Click **Save Policy**.




###  gcloud 

  1. Set the `PROJECT_ID` for your fleet host project. You can find this project ID in the `gkeConnect` field in your user cluster configuration file.
         
         export PROJECT_ID=PROJECT_ID
         

Set the default Google Cloud project.
         
         gcloud config set project ${PROJECT_ID}
         

  2. Export the policy YAML file to your local system:
         
         gcloud container binauthz policy export  > policy.yaml
         

Your YAML file looks like the following:
         
         defaultAdmissionRule:
           enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
           evaluationMode: ALWAYS_ALLOW
         globalPolicyEvaluationMode: ENABLE
         name: projects/<var>PROJECT_ID</var>/policy
         

  3. Edit `policy.yaml`.

  4. Set `evaluationMode` to `ALWAYS_ALLOW`.

  5. If you have a `requireAttestationsBy` block in the file, delete this block.

  6. Save the file.

  7. Import `policy.yaml` as follows:
         
         gcloud container binauthz policy import policy.yaml
         




To add an exempt image to the allowlist, add the following to the policy file: 
    
    
    admissionWhitelistPatterns:
      - namePattern: EXEMPT_IMAGE_PATH

Replace `EXEMPT_IMAGE_PATH` with the path to am image to exempt. To exempt additional images, add additional `- namePattern` entries. Learn more about [`admissionWhitelistPatterns`](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#allowlistpatterns). 

On your admin workstation, do the following:

  1. Create a manifest file for a Pod.

Save the following to a file called `pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: test-pod
         spec:
           containers:
           - name: test-container
             image: us-docker.pkg.dev/google-samples/containers/gke/hello-app@sha256:c62ead5b8c15c231f9e786250b07909daf6c266d0fcddd93fea882eb722c3be4
         

  2. Create the Pod:
         
         kubectl apply -f pod.yaml
         

You see that the Pod was successfully deployed.

  3. Delete the Pod:
         
         kubectl delete -f pod.yaml
         




### Disallow all

This section demonstrates a failure case. In this section, you configure the default policy to disallow your container image from being deployed.

**Caution:** This policy disallows all container images from deploying.

In Google Cloud, do the following:

###  Console 

  1. In the Google Cloud console, go to the Binary Authorization page.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. Make sure your fleet host project is selected.

  3. Click **Edit Policy**.

  4. Under **Project default rule** , select **Disallow all images**.

  5. Click **Save policy**.




###  gcloud 

  1. Set the `PROJECT_ID` to your fleet host project ID.
         
         export PROJECT_ID=PROJECT_ID
         

  2. Set the default Google Cloud project.
         
         gcloud config set project ${PROJECT_ID}
         

  3. Export the policy YAML file:
         
         gcloud container binauthz policy export  > policy.yaml
         

  4. Edit `policy.yaml`.

  5. Set `evaluationMode` to `ALWAYS_DENY`.

  6. If you have a `requireAttestationsBy` block in the file, delete this block.

  7. Save the file.

  8. Import `policy.yaml` as follows:
         
         gcloud container binauthz policy import policy.yaml
         




**Note:** It can take a few minutes for the policy to take effect.

On your admin workstation, do the following:

  1. Create a manifest file for a Pod.

Save the following to a file called `pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: test-pod
         spec:
           containers:
           - name: test-container
             image: us-docker.pkg.dev/google-samples/containers/gke/hello-app@sha256:c62ead5b8c15c231f9e786250b07909daf6c266d0fcddd93fea882eb722c3be4
         

  2. Create the Pod:
         
         kubectl apply -f pod.yaml
         

You see that the Pod was blocked from being deployed. The output looks like the following:
         
         Error from server (VIOLATES_POLICY): error when creating "pod.yaml": admission webhook "binaryauthorization.googleapis.com" denied the request: Denied by default admission rule. Overridden by evaluation mode
         




## Get the user cluster resource ID

This section shows you how to compose the cluster resource ID for your user cluster. In your Binary Authorization policy, you can create cluster-specific rules. You associate these rules with a cluster-specific resource ID, which is based on your cluster ID.

You get the resource ID as follows:

###  Console 

  1. In the **Google Cloud console** , go to the GKE **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the fleet host project ID for your clusters. You can find this project ID in the [`gkeConnect` section](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/user-cluster-configuration-file#gkeconnect-section) of your user cluster configuration file.

  3. In the cluster list, find your cluster ID under the **Name** column.

  4. To create the resource ID, add the prefix `global.` to the cluster ID so that the resource ID has the following format: `global.CLUSTER_ID`.




###  gcloud 

  1. Use SSH to connect to your admin workstation.

  2. On the admin workstation, run the following command:
         
         kubectl get membership -o yaml
         

  3. Get the cluster ID from `spec.owner.id` field of the output. Example output follows:
         
         apiVersion: v1
         items:
         - apiVersion: hub.gke.io/v1
           kind: Membership
           ...
           spec:
             owner:
               id: //gkehub.googleapis.com/projects/PROJECT_NUMBER/locations/global/memberships/**my-cluster-id**
         

In the example output, the cluster ID is `my-cluster-id`.

  4. To create the resource ID, add the prefix `global.` to the cluster ID. In the example, the resource ID is `global.my-cluster-id`.




You use this resource ID when you define cluster-specific rules. Learn how to set cluster-specific rules by using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#set_cluster_specific_rules) or the [gcloud CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#set_cluster_specific_rules).

## Update the failure policy

The Binary Authorization Module webhook can be configured to _fail open_ or _fail close_.

### Fail close

To update the failure policy to fail close, do the following:

  1. Edit the manifest-0.2.6.yaml file and set failurePolicy to `Fail`

  2. Re-enable the webhook:
         
         kubectl apply -f manifest-0.2.6.yaml
         

You see output similar to the following:
         
         serviceaccount/binauthz-admin unchanged
         role.rbac.authorization.k8s.io/binauthz-role configured
         clusterrole.rbac.authorization.k8s.io/binauthz-role configured
         rolebinding.rbac.authorization.k8s.io/binauthz-rolebinding unchanged
         clusterrolebinding.rbac.authorization.k8s.io/binauthz-rolebinding unchanged
         secret/binauthz-tls unchanged
         service/binauthz unchanged
         deployment.apps/binauthz-module-deployment unchanged
         validatingwebhookconfiguration.admissionregistration.k8s.io/binauthz-validating-webhook-configuration configured
         




### Fail open

To update the failure policy to fail open, do the following:

  1. Edit the manifest-0.2.6.yaml file and set failurePolicy to `Ignore`

  2. Re-enable the webhook:
         
         kubectl apply -f manifest-0.2.6.yaml
         

You see output similar to the following:
         
         serviceaccount/binauthz-admin unchanged
         role.rbac.authorization.k8s.io/binauthz-role configured
         clusterrole.rbac.authorization.k8s.io/binauthz-role configured
         rolebinding.rbac.authorization.k8s.io/binauthz-rolebinding unchanged
         clusterrolebinding.rbac.authorization.k8s.io/binauthz-rolebinding unchanged
         secret/binauthz-tls unchanged
         service/binauthz unchanged
         deployment.apps/binauthz-module-deployment unchanged
         validatingwebhookconfiguration.admissionregistration.k8s.io/binauthz-validating-webhook-configuration configured
         




To learn more, see [webhook failure policy](https://docs.cloud.google.com/binary-authorization/docs/overview-on-prem#webhook-failure-policy).

## Clean up

  1. The following code sample shows how to disable the webhook:
         
         kubectl delete ValidatingWebhookConfiguration/binauthz-validating-webhook-configuration
         

  2. The following code sample shows how to re-enable the webhook:
         
         kubectl apply -f manifest-0.2.6.yaml
         

  3. The following code sample shows how to delete all of the resources related to Binary Authorization:
         
         kubectl delete -f manifest-0.2.6.yaml
         kubectl delete namespace binauthz-system
         




## What's next

  * To check policy compliance at Pod creation time without actually blocking the Pod from being created, see [Enable dry run](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run).
  * To force a Pod to be created that the Binary Authorization enforcer would otherwise block, see [Use breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass).
  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build).
  * To implement an attestor-based Binary Authorization policy, see the following: 
    * Configure a policy using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli). Set the default or cluster-specific rule to require attestations.
    * Create an attestor using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console) or the [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).
    * [Create an attestation](https://docs.cloud.google.com/binary-authorization/docs/making-attestations).
  * To see log events related to Binary Authorization for Distributed Cloud, see [View Cloud Audit Logs events](https://docs.cloud.google.com/binary-authorization/docs/viewing-on-prem-logs).
  * [Monitor metrics](https://docs.cloud.google.com/binary-authorization/docs/on-prem-cloud-monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
