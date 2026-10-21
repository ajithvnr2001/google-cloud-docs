---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-check-cluster/
title: Step 10: Check cluster readiness \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:55:58.407372+00:00
---

# Step 10: Check cluster readiness  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-check-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 10: Check cluster readiness Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.12 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.12 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-check-cluster.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-check-cluster.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-check-cluster.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-check-cluster.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-check-cluster.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-check-cluster.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-check-cluster.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-check-cluster.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-check-cluster.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-check-cluster.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-check-cluster.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-check-cluster.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-check-cluster.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-check-cluster.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-check-cluster.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-check-cluster.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-check-cluster.html)



## Check hybrid cluster readiness

Before applying your configuration and installing the hybrid helm charts, you should check that your Kubernetes cluster is ready for Apigee hybrid installation.

To check the readiness of your cluster, you will create a YAML file with a Kubernetes Job definition and apply that file with `kubectl` commands to check the cluster. You then check the status of the Kubernetes test job with a `kubectl get jobs` command. 

  1. Verify that `kubectl` is set to the correct context using the following command. The current context should be set to the cluster to which you are deploying Apigee hybrid. 
         
         kubectl config current-context

The result should include the name of the cluster you are deploying Apigee hybrid in. For example, on GKE, the context name is usually in the form `gke_project-id_cluster-location_cluster-name`, as in: 
         
         gke_my-project_us-central1_my-cluster

If the name cluster name in the context does not match, the following command will get the `gcloud` credentials of the cluster and set the `kubectl` context:

### Regional clusters
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
         --region $CLUSTER_LOCATION \
         --project $PROJECT_ID

### Zonal clusters
         
         gcloud container clusters get-credentials $CLUSTER_NAME \
         --zone $CLUSTER_LOCATION \
         --project $PROJECT_ID

  2. In your helm-charts directory, create a `cluster-check` directory: 
         
         mkdir $APIGEE_HELM_CHARTS_HOME/cluster-check

  3. In the `$APIGEE_HELM_CHARTS_HOME/cluster-check` directory, create a file named `apigee-k8s-cluster-ready-check.yaml` with the following contents: 
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: apigee-k8s-cluster-ready-check
         ---
         apiVersion: rbac.authorization.k8s.io/v1
         kind: ClusterRoleBinding
         metadata:
           name: cluster-check-admin
         roleRef:
           apiGroup: rbac.authorization.k8s.io
           kind: ClusterRole
           name: cluster-admin
         subjects:
         - apiGroup: ""
           kind: ServiceAccount
           namespace: default
           name: apigee-k8s-cluster-ready-check
         ---
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: apigee-k8s-cluster-ready-check
         spec:
           template:
             spec:
               hostNetwork: true
               serviceAccountName: apigee-k8s-cluster-ready-check
               containers:
                 - name: manager
                   image: gcr.io/apigee-release/hybrid/apigee-operators:1.12.4
                   command:
                     - /manager
                   args:
                   - --k8s-cluster-ready-check
                   env:
                   - name: POD_IP
                     valueFrom:
                       fieldRef:
                         fieldPath: status.podIP
                   securityContext:
                     runAsGroup: 998
                     runAsNonRoot: true
                     runAsUser: 999
               restartPolicy: Never
           backoffLimit: 1
         

  4. Apply the `apigee-k8s-cluster-ready-check.yaml` with the following `kubectl` command. This will run the test: 
         
         kubectl apply -f $APIGEE_HELM_CHARTS_HOME/cluster-check/apigee-k8s-cluster-ready-check.yaml

The output should show that the service account and job were created. For example: 
         
         kubectl apply -f $APIGEE_HELM_CHARTS_HOME/cluster-check/apigee-k8s-cluster-ready-check.yaml
         serviceaccount/apigee-k8s-cluster-ready-check created
         job.batch/apigee-k8s-cluster-ready-check created

  5. Check the status of the Kubernetes job with the following command: 
         
         kubectl get jobs apigee-k8s-cluster-ready-check

If your cluster is ready, the output should look something like: 
         
         NAME                            COMPLETIONS   DURATION   AGE
         apigee-k8s-cluster-ready-check  **1/1**           8s         1h23m

If the test failed and your cluster is not ready, the output will look something like: 
         
         NAME                            COMPLETIONS   DURATION   AGE
         apigee-k8s-cluster-ready-check  **0/1**           44s         44s

Look for the number of completions: 

     * **1/1** Success, your cluster is ready for Apigee hybrid installation.
     * **0/1** The test failed. The cluster is not ready. Proceed to the following steps to troubleshoot the cluster.
  6. If the test did not succeed, check the logs with the following commands. 
     1. Get the name of the pod for the cluster pre-check job: 
            
            kubectl get pods | grep apigee-k8s-cluster-ready-check

     2. Get the Kubernetes logs for the pod: 
            
            kubectl logs pod_name

Where pod_name is the name of the apigee-k8s-cluster-ready-check pod. 

  7. Clean up before proceeding to the next step. Delete the Kubernetes job with the following command: 
         
         kubectl delete -f $APIGEE_HELM_CHARTS_HOME/cluster-check/apigee-k8s-cluster-ready-check.yaml

The output should show that the service account and job were deleted. For example: 
         
         kubectl delete -f $APIGEE_HELM_CHARTS_HOME/cluster-check/apigee-k8s-cluster-ready-check.yaml
         serviceaccount "apigee-k8s-cluster-ready-check" deleted
         job.batch "apigee-k8s-cluster-ready-check" deleted


**Tip:** On some platforms, like Google Distributed Cloud, you may see DNS resolution errors. If the DNS resolution is not working, try this workaround. 

Add a static host entry in `/etc/hosts` file of each cassandra worker node similar to the following: 
    
    
    echo -e "\\n127.0.1.1 ${HOSTNAME}" >> "/etc/hosts"

or 
    
    
    "\\nWORKER-NODE-IP ${HOSTNAME}" >> "/etc/hosts"

You have now made sure your Apigee hybrid cluster is ready. Next, let's install the charts to apply your configuration to the hybrid runtime.

## Troubleshooting

  1. Cassandra DNS check: If you find error logs similar to `DNS resolution was successful but IP doesn't match POD IP`, `could not resolve hostname` or `error determining hostname` it means your cluster DNS is not configured correctly for a multi-region setup. You can ignore this error if you do not intend to set up multi-region. 
  2. Control Plane connectivity check: If you find error logs similar to `error creating TCP connection with host` then you need to resolve the connectivity from cluster to apigee.googleapis.com and re-run the job. 



## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-overrides) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-check-cluster) [(NEXT) Step 11: Install Apigee hybrid using Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-helm-charts) [12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
