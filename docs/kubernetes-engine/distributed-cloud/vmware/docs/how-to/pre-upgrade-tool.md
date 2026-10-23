---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/pre-upgrade-tool/
title: Run the pre-upgrade tool \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:28.259640+00:00
---

# Run the pre-upgrade tool  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/pre-upgrade-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Run the pre-upgrade tool Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how run a standalone tool in preparation for an upgrade. Before upgrading an admin or user cluster that is at Google Distributed Cloud **version 1.9 and later versions** , we recommend that you run the pre-upgrade tool.

To run the tool, use the bash script in this document that uses a hard-coded Secure Hash Algorithms (SHA). For each release of the tool, this document will be updated with the new SHA. The script creates a Kubernetes Job to run a specific version of preflight checks depending on the version that you are upgrading to.

## Pre-upgrade checks

The tool checks the following before you upgrade a user cluster:

Category | Description  
---|---  
Cluster Health | 

  * Validates the PDBs in all namespaces of the admin cluster. 


  * Validates the PDBs in all namespaces of the user cluster.


  * Validates that a previous upgrade of the admin cluster finished successfully. 

  
Configurations | 

  * Recommends the patch version to upgrade to.


  * Checks whether the component access SA key is wiped out as described in the [related known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#component-access-service-account-key-wiped-out-after-admin-cluster-upgraded-from-1.11.x).


  * If you are upgrading to 1.10, warns if you will need to apply the workaround in this [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#upgrading-the-first-user-cluster-from-1.9-to-1.10-recreates-nodes-in-other-user-clusters).

  
  
The tool checks the following before you upgrade an admin cluster:

Category | Description  
---|---  
Cluster Health | Validates the `PodDisruptionBudgets` (PDBs) in all namespaces of the admin cluster.  
Configurations | 

  * Recommends the patch version to upgrade to.
  * Recommends [admin cluster backup ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl).
  * Warns if you might be affected by this [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/known-issues#upgrading-an-admin-cluster-with-always-on-secrets-encryption-enabled-fails).

  
  
## Prepare to run the tool

  1. [Upgrade your admin workstation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#upgrade_awstation) if you have not done so.

  2. Run `gkectl prepare` to import OS images to vSphere if you have not done so:
         
         gkectl prepare \
             --bundle-path /var/lib/gke/bundles/gke-onprem-vsphere-TARGET_VERSION.tgz \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * `TARGET_VERSION`: The [Google Distributed Cloud patch version](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/version-history#supported-versions) that you want to upgrade to. The format for the version number must be a complete patch version, like `1.13.10-gke.42`.

     * `ADMIN_CLUSTER_KUBECONFIG`: The path to the admin cluster kubeconfig.

**Note:** You don't need to re-run `gkectl prepare` when you are ready to upgrade the cluster.
  3. If you are using a private registry, download the preflight container image with the provided docker digest and upload the image into the private registry. If you aren't using a private registry, skip to the next step.
         
         export SRC_IMAGE=gcr.io/gke-on-prem-release/preflight@sha256:9704315c6637750a014d0079ca04a8f97d0ca3735e175020377107c3181f6234
         export DST_IMAGE=REGISTRY_ADDRESS/preflight:$(date +%Y-%m%d-%H%M%S)
         docker pull $SRC_IMAGE
         docker tag $SRC_IMAGE $DST_IMAGE
         docker push $DST_IMAGE
         

Replace `REGISTRY_ADDRESS` with the private registry address.

  4. In the following bash script, set values for these placeholders:

     * `ADMIN_CLUSTER_KUBECONFIG`: The path to the admin cluster kubeconfig.

     * `REGISTRY_ADDRESS`: If the admin cluster uses a private registry, this is the private registry address that you specified in the previous step. If you aren't using a private registry, specify the public registry: `gcr.io/gke-on-prem-release`
    
    #!/bin/bash
    UPGRADE_TARGET_VERSION=${1}
    CLUSTER_NAME=${2}
    ADMIN_KUBECONFIG=ADMIN_CLUSTER_KUBECONFIG
    REGISTRY_ADDRESS=REGISTRY_ADDRESS
    pre_upgrade_namespace=kube-system
    if [[ -z "$CLUSTER_NAME" ]]
    then
      echo "Running the pre-ugprade tool before admin cluster upgrade"
    else
      echo "Running the pre-ugprade tool before user cluster upgrade"
      pre_upgrade_namespace=$CLUSTER_NAME-gke-onprem-mgmt
    fi
    kubectl apply --kubeconfig ${ADMIN_KUBECONFIG} -f - <<EOF
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: pre-upgrade-job
      namespace: $pre_upgrade_namespace
    EOF
    kubectl apply --kubeconfig ${ADMIN_KUBECONFIG} -f - <<EOF
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      creationTimestamp: null
      name: pre-upgrade-job-rolebinding-in-$pre_upgrade_namespace
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: onprem-user-cluster-controller-role
    subjects:
      - kind: ServiceAccount
        name: pre-upgrade-job
        namespace: $pre_upgrade_namespace
    EOF
    kubectl apply --kubeconfig ${ADMIN_KUBECONFIG} -f - <<EOF
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: pre-upgrade-$(date +%Y-%m%d-%H%M%S)
      namespace: $pre_upgrade_namespace
      labels:
        onprem.cluster.gke.io/job-usage: preflight
    spec:
      ttlSecondsAfterFinished: 2592000
      backoffLimit: 2
      template:
        metadata:
          labels:
            onprem.cluster.gke.io/pod-usage: preflight
        spec:
          containers:
          - name: preflight
            image: $REGISTRY_ADDRESS/preflight@sha256:9704315c6637750a014d0079ca04a8f97d0ca3735e175020377107c3181f6234
            imagePullPolicy: Always
            command:
            - /preflight
            - --upgrade-target-version
            - "$UPGRADE_TARGET_VERSION"
            - --cluster-name
            - "$CLUSTER_NAME"
            - --scenario
            - pre-upgrade
          restartPolicy: Never
          serviceAccountName: pre-upgrade-job
          imagePullSecrets:
          - name: private-registry-creds
    EOF
    

  5. Save the above bash script to a file called `pre-upgrade.sh` and make it executable:
         
         chmod +x pre-upgrade.sh
         




## Run the script

  1. The arguments that you provide when you run the script depends on whether you are upgrading a user cluster or an admin cluster:

     * Before upgrading an admin cluster run the script as follows:
    
    ./pre-upgrade.sh TARGET_VERSION
    

     * Before upgrading a user cluster:
    
    ./pre-upgrade.sh TARGET_VERSION USER_CLUSTER_NAME
    

Replace `USER_CLUSTER_NAME` with the name of the user cluster you will be upgrading.

The output is similar to the following:
    
    job.batch/pre-upgrade-2023-0822-213551 created
    

  2. Run the following command on the Pods controlled by the job to get a list of validation results.
         
         kubectl logs -n JOB_NAMESPACE jobs/JOB_NAME \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * `JOB_NAME`: This is the name of the job that the script outputs from the previous step.

     * `JOB_NAMESPACE`: The value that you set depends on whether you are upgrading an admin or user cluster. If you are upgrading an admin cluster, specify `kube-system`. If you are upgrading a user cluster, specify `USER_CLUSTER_NAME-gke-onprem-mgmt`.

Wait a few minutes for the job to complete or to reach the backoff limit and fail. In the results, review the `Reason` for any check with the status `Warning`, `Unknown` or `Failure` to see if you can resolve the issue.

**Important:** We recommend that you resolve all issues with a `Failure` status because these issues will cause the upgrade to fail. Contact Google support if needed.
  3. Before upgrading clusters, run the following command to delete the Job:
         
         kubectl delete jobs JOB_NAME -n JOB_NAMESPACE \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
