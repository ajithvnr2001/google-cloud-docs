---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime/
title: Step 9: Install hybrid runtime \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:52:41.495064+00:00
---

# Step 9: Install hybrid runtime  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 9: Install hybrid runtime Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-hybrid-runtime.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-hybrid-runtime.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-hybrid-runtime.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-hybrid-runtime.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-hybrid-runtime.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-hybrid-runtime.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-hybrid-runtime.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-hybrid-runtime.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-hybrid-runtime.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-hybrid-runtime.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-hybrid-runtime.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-hybrid-runtime.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-hybrid-runtime.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-hybrid-runtime.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-hybrid-runtime.html)



##  Apply the configuration to the cluster 

Use the following steps to install Apigee hybrid into your cluster: 

  1. Be sure that you are in the `hybrid-base-directory/hybrid-files` directory. 
         
         cd $HYBRID_FILES

**Note:** Because the overrides file specifies service account files using paths relative to your `hybrid-base-directory/hybrid-files` directory, you must execute the commands from within that directory.
  2. Verify that `kubectl` is set to the correct context using the following command. The current context should be set to the cluster to which you are deploying Apigee hybrid. 
         
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

  3.  _For**Anthos on bare metal** , **AWS on GKE** , **EKS** , and **GKE on prem** platforms only_, Verify that the [`KUBECONFIG`](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/#set-the-kubeconfig-environment-variable) variable is set using the following command: 
         
         echo ${KUBECONFIG}

  4. Do a _dry run_ initialization. Doing a dry run lets you check for any errors before any changes are made to the cluster. Execute the `init` command with the `--dry-run` flag as follows: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f overrides/overrides.yaml --dry-run=client

  5. If there are no errors, execute the `init` command as follows: 
         
         **${APIGEECTL_HOME}** /apigeectl init -f overrides/overrides.yaml

The `init` command installs the [Apigee deployment services](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services) Apigee Deployment Controller and Apigee Admission Webhook.

  6. To check the status of the deployment, you can use the following commands: 
         
         **${APIGEECTL_HOME}** /apigeectl check-ready -f overrides/overrides.yaml
         
         kubectl get pods -n apigee-system
         
         kubectl get pods -n apigee

When the pods are ready, go to the next step. 

  7. Do a _dry run_ install. Execute the `apply` command with the `--dry-run` flag. 
         
         **${APIGEECTL_HOME}** /apigeectl apply -f overrides/overrides.yaml --dry-run=client

  8. If there are no errors, you can apply the [ Apigee-specific runtime components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid#about-the-runtime-plane) to the cluster with the following command: 
         
         **${APIGEECTL_HOME}** /apigeectl apply -f overrides/overrides.yaml

  9. To check the status of the deployment, run the following command: 
         
         **${APIGEECTL_HOME}** /apigeectl check-ready -f overrides/overrides.yaml

Repeat this step until the pods are all ready. The pods may take several minutes to start up.

**Note:** If you set up your overrides file to use Workload Identity on GKE, you may see an error that `apigeeenvironment` is not running. Continue to the steps in the next section. `check-ready` will show your Apigee environment running after you complete the steps to enable Workload Identity.



## GKE with Workload Identity

For Apigee hybrid installations on GKE, Google Cloud offers an option called [Workload identity](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-workload-identity) to authenticate hybrid runtime components. 

**Note:** Apigee hybrid v.1.10 only supports Workload Identity federation on GKE.

### Google Cloud service accounts and Kubernetes service accounts

A Google Cloud service account is a special kind of account that can be used to make authorized API calls by authenticating as the service account itself. Google Cloud service accounts can be given roles and permissions similar to an individual user. When an application authenticates as a service account, it has access to all resources that the service account has permission to access. If you want to learn more about Google Cloud service accounts, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview). 

You created Google Cloud service accounts for your Apigee hybrid installation in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts). Apigee uses these service accounts to authenticate the hybrid components. 

Kubernetes service accounts are similar to Google Cloud service accounts. A Kubernetes service account provides an identity for processes that run in a Pod, and allows it to authenticate to the API server similarly to a user. If you want to learn more about Kubernetes service accounts, see [Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). 

The `apigeectl` tool created most of the Kubernetes service accounts needed by Apigee hybrid when you ran `apigeectl apply` in the previous procedure. 

When you configure Workload Identity on GKE, you associate the Google Cloud service accounts with the Kubernetes service accounts in the Kubernetes cluster. That way, the Kubernetes service accounts can impersonate the Google Cloud service accounts and use their assigned roles and permissions to authenticate with the hybrid components. 

Follow these instructions to configure Workload identity for your project. 

### Prepare to configure workload identity

These procedures make use of the following environment variables. Check that they are defined and define any that are not:
    
    
    echo $APIGEECTL_HOME
    echo $CLUSTER_LOCATION
    echo $ENV_NAME
    echo $HYBRID_FILES
    echo $NAMESPACE
    echo $PROJECT_ID
    echo $ORG_NAME
    

  1. Check that the current `gcloud` configuration is set to your Google Cloud project ID with the following command: 
         
         gcloud config get project

If needed, set the current `gcloud` configuration:
    
    gcloud config set project $PROJECT_ID

  2. Create the `apigee-cassandra-restore` Kubernetes service account. 

When you applied your configuration by running `apigeectl apply`, the command created most of the Kubernetes service accounts needed for workload identity. 

To create the `apigee-cassandra-restore` Kubernetes service account, run `apigeectl apply` with the `--restore` flag:
         
         $APIGEECTL_HOME/apigeectl apply -f $HYBRID_FILES/overrides/overrides.yaml --restore

  3. Verify that Workload Identity is enabled for your GKE Cluster. When you created the cluster in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster#gke), step 11 was to Enable Workload Identity. You can confirm if Workload Identity is enabled by running the following command: 

### Regional clusters
         
         gcloud container clusters describe $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten 'workloadIdentityConfig'

### Zonal clusters
         
         gcloud container clusters describe $CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten 'workloadIdentityConfig'

Your output should look like the following: 
         
         ---
           workloadPool: PROJECT_ID.svc.id.goog

If you see `null` instead in your results, run the following command to enable Workload identity for your cluster: 

### Regional clusters
         
         gcloud container clusters update $CLUSTER_NAME \
           --workload-pool=$PROJECT_ID.svc.id.goog \
           --project $PROJECT_ID \
           --region $CLUSTER_LOCATION

### Zonal clusters
         
         gcloud container clusters update  $CLUSTER_NAME \
           --workload-pool=$PROJECT_ID.svc.id.goog \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID

  4. Enable Workload identity for each node pool with the following commands. This operation can take up to 30 minutes for each node:

### Regional clusters
         
         gcloud container node-pools update NODE_POOL_NAME \
           --cluster=$CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --workload-metadata=GKE_METADATA

### Zonal clusters
         
         gcloud container node-pools update NODE_POOL_NAME \
           --cluster=$CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --workload-metadata=GKE_METADATA

Where NODE_POOL_NAME is the name of each node pool. In most Apigee hybrid installations, the two default node pools are named `apigee-data` and `apigee-runtime`.

  5. Verify that Workload identity is enabled on your node pools with the following commands: 

### Regional clusters
         
         gcloud container node-pools describe apigee-data \
           --cluster $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"
         
         gcloud container node-pools describe apigee-runtime \
           --cluster $CLUSTER_NAME \
           --region $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"

### Zonal clusters
         
         gcloud container node-pools describe apigee-data \
           --cluster $CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"
         
         gcloud container node-pools describe apigee-runtime \
           --cluster $CLUSTER_NAME \
           --zone $CLUSTER_LOCATION \
           --project $PROJECT_ID \
           --flatten "config:"

Your output should look something like:
         
         ---
         diskSizeGb: 100
         diskType: pd-standard
         ...
         **workloadMetadataConfig:
           mode: GKE_METADATA**
             

  6. Get a list of the names of the Google Cloud service accounts for your project. You will need these names to associate the Kubernetes service accounts to configure Workload identity. For non-production installations, there should be only one Google service account. For production installations there should be eight. 

Use the following command to get the list of names:
         
         gcloud iam service-accounts list --project $PROJECT_ID

Your output should look something like:

###  Non-prod 

For non-production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-non-prod      apigee-non-prod@my_project_id.iam.gserviceaccount.com      False
         

###  Production 

For non-production environments:
         
         DISPLAY NAME         EMAIL                                                      DISABLED
         apigee-cassandra     apigee-cassandra@my_project_id.iam.gserviceaccount.com     False
         apigee-logger        apigee-logger@my_project_id.iam.gserviceaccount.com        False
         apigee-mart          apigee-mart@my_project_id.iam.gserviceaccount.com          False
         apigee-metrics       apigee-metrics@my_project_id.iam.gserviceaccount.com       False
         apigee-runtime       apigee-runtime@my_project_id.iam.gserviceaccount.com       False
         apigee-synchronizer  apigee-synchronizer@my_project_id.iam.gserviceaccount.com  False
         apigee-udca          apigee-udca@my_project_id.iam.gserviceaccount.com          False
         apigee-watcher       apigee-watcher@my_project_id.iam.gserviceaccount.com       False
         

**Tip:** If you have custom names for your service accounts that do not correspond easily with the names of the Apigee components, you can determine the role of each service account by checking the roles assigned to it and comparing the roles with the roles recommended in [**About service accounts**](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/sa-about#recommended-sas). 

Use the following command to check the roles assigned to a service account:
         
         gcloud projects get-iam-policy ${PROJECT_ID}  \
           --flatten="bindings[].members" \
           --format='table(bindings.role)' \
           --filter="SERVICE_ACCOUNT_NAME"

  7. Get a list of names of the Kubernetes service accounts. You will need this list of names to associate with your Google Cloud service accounts later in this procedure. Use the following command: 
         
         kubectl get sa -n $NAMESPACE

Your output should look something like the following. The Kubernetes service accounts in **bold** are the ones you will need to associate with your Google cloud service accounts: 
         
         NAME                                                         SECRETS   AGE
         **apigee-cassandra-backup**                                      1         11m
         **apigee-cassandra-restore**                                     1         11m
         **apigee-cassandra-schema-setup- my-project-id-123abcd-sa**       1         11m
         **apigee-cassandra-schema-val- my-project-id-123abcd**            1         11m
         **apigee-cassandra-user-setup- my-project-id-123abcd-sa**         1         11m
         **apigee-connect-agent- my-project-id-123abcd-sa**                1         11m
         **apigee-datastore-default-sa**                                  1         11m
         apigee-ingressgateway                                        1         11m
         apigee-ingressgateway-my-project-id-123abcd                  1         11m
         apigee-ingressgateway-manager                                1         11m
         apigee-init                                                  1         11m
         **apigee-mart- my-project-id-123abcd-sa**                         1         11m
         **apigee-metrics-sa**                                            1         11m
         apigee-mint-task-scheduler-my-project-id-123abcd-sa          1         11m
         apigee-redis-default-sa                                      1         11m
         apigee-redis-envoy-default-sa                                1         11m
         **apigee-runtime- my-project-id-env-name-234bcde-sa**             1         11m
         **apigee-synchronizer- my-project-id-env-name-234bcde**-sa        1         11m
         **apigee-udca- my-project-id-123abcd-sa**                         1         11m
         **apigee-udca- my-project-id-env-name-234bcde-**sa                1         11m
         **apigee-watcher- my-project-id-123abcd-sa**                      1         11m
         default                                                      1         11m
             




### Configure workload identity

Use the following procedure to enable workload identity for your Hybrid installation:

  1. For each Apigee component annotate the corresponding Kubernetes service accounts with the Google service account for the component. **IMPORTANT:** If your service account names do not match the default names created by `create-service-account`, replace the red service account name with the correct service account name for the component in the following commands. For example, if your Cassandra service account is named `my-cassandra-accnt-1`, then replace `apigee-cassandra` with that name in the command.

The following steps use two environment variables. You will reset the values of these variables before each set of commands:

     * GSA_NAME: The name of a Google service account. These are the service accounts you created with the `create-service-account` tool in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts).
     * KSA_NAME: The name of a Kubernetes service account. These are the accounts you listed above with the `kubectl get sa -n $NAMESPACE` command, for example: `apigee-cassandra-schema-setup-hybrid-example-project-123abcd-sa`.
**Tip:** If you encounter an error saying the service account is "NOT FOUND," try running `gcloud init` to set the current configuration to the correct Google Cloud project ID and cluster location.
     * **Cassandra**

Configure Workload identity for the Cassandra component.

The Cassandra component has six associated Kubernetes service accounts:

       * `apigee-cassandra-backup`
       * `apigee-cassandra-restore`
       * `apigee-cassandra-schema-setup`
       * `apigee-cassandra-schema-val` _(`val` = validation)_
       * `apigee-cassandra-user-setup`
       * `apigee-datastore-default`

###  Non-prod 

**Configure the`apigee-cassandra-backup` Kubernetes service account**

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-non-prod"
              KSA_NAME="apigee-cassandra-backup"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

Your output should have a line describing the annotation, similar to:
              
              Annotations:         iam.gke.io/gcp-service-account: apigee-non-prod@my-project-id.iam.gserviceaccount.com

**Configure the`apigee-cassandra-restore` Kubernetes service account**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-restore"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

**Configure the`apigee-cassandra-schema-setup` Kubernetes service account**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-schema-setup-service-account-name-sa"

for example: `apigee-cassandra-schema-setup-_hybrid-example-project-123abcd_ -sa`.
       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

**Configure the`apigee-cassandra-schema-val` Kubernetes service account**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-schema-val-service-account-name"

for example: `apigee-cassandra-schema-val _-hybrid-example-project-123abcd_`.
       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

**Configure the`apigee-cassandra-user-setup` Kubernetes service account**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-cassandra-user-setup-service-account-name-sa"

for example: `apigee-cassandra-user-setup-_hybrid-example-project-123abcd_ -sa`.
       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

**Configure the`apigee-datastore-default-sa` Kubernetes service account**

       1. Redefine the `KSA_NAME`environment variable: 
              
              KSA_NAME="apigee-datastore-default-sa"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

###  Production 

**Configure the`apigee-cassandra-backup` Kubernetes service account**

       1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
              
              GSA_NAME="apigee-cassandra"
              KSA_NAME="apigee-cassandra-backup"

       2. Bind the IAM role: 
              
              gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser \
                --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
                $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
                --project $PROJECT_ID

       3. Annotate the service account: 
              
              kubectl annotate serviceaccount \
                --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

       4. Verify the annotation: 
              
              kubectl describe serviceaccount \
                --namespace $NAMESPACE $KSA_NAME

Your output should have a line describing the annotation, similar to:
    
    Annotations:         iam.gke.io/gcp-service-account: apigee-cassandra@my-project-id.iam.gserviceaccount.com

     * Verify the annotation: 
           
           kubectl describe serviceaccount \
             --namespace $NAMESPACE $KSA_NAME




**Configure the`apigee-cassandra-restore` Kubernetes service account**

  1. Redefine the `KSA_NAME` environment variable: 
         
         KSA_NAME="apigee-cassandra-restore"

  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com




**Configure the`apigee-cassandra-schema-setup` Kubernetes service account**

  1. Redefine the `KSA_NAME`environment variable: 
         
         KSA_NAME="apigee-cassandra-schema-setup-service-account-name-sa"

for example: `apigee-cassandra-schema-setup-_hybrid-example-project-123abcd_ -sa`.

Bind the IAM role:
    
    gcloud iam service-accounts add-iam-policy-binding \
      --role roles/iam.workloadIdentityUser \
      --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
      $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
      --project $PROJECT_ID

  2. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  3. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




**Configure the`apigee-cassandra-schema-val` Kubernetes service account**

  1. Redefine the `KSA_NAME`environment variable: 
         
         KSA_NAME="apigee-cassandra-schema-val-service-account-name"

for example: `apigee-cassandra-schema-val-_hybrid-example-project-123abcd_`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




**Configure the`apigee-cassandra-user-setup` Kubernetes service account**

  1. Redefine the `KSA_NAME`environment variable: 
         
         KSA_NAME="apigee-cassandra-user-setup-service-account-name-sa"

for example: `apigee-cassandra-user-setup-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




**Configure the`apigee-datastore-default-sa` Kubernetes service account**

  1. Redefine the `KSA_NAME`environment variable: 
         
         KSA_NAME="apigee-datastore-default-sa"

  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **Apigee Connect**

Configure Workload identity for the Apigee Connect component.

###  Non-prod 

  1. Define the `KSA_NAME` environment variable: 
         
         KSA_NAME="apigee-connect-agent-service-account-name-sa"

for example: `apigee-connect-agent-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-mart"
         KSA_NAME="apigee-connect-agent-service-account-name-sa"

for example: `apigee-connect-agent-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **MART**

Configure Workload identity for the MART component.

###  Non-prod 

  1. Define the `KSA_NAME` environment variable: 
         
         KSA_NAME="apigee-mart-service-account-name-sa"

for example: `apigee-mart-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-mart"
         KSA_NAME="apigee-mart-service-account-name-sa"

for example: `apigee-mart-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **Apigee metrics**

Configure Workload identity for the Apigee metrics component.

###  Non-prod 

  1. Define the `KSA_NAME`environment variables: 
         
         KSA_NAME="apigee-metrics-sa"

  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-metrics"
         KSA_NAME="apigee-metrics-sa"

  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
         --role roles/iam.workloadIdentityUser \
         --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
         $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
         --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
         --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **UDCA (org-level)**

Configure Workload identity for the organization-level UDCA component.

UDCA is implemented in both organization-level and environment-level scopes. Therefore, there are two separate Kubernetes service accounts for UDCA, one for each scope. You can tell them apart by the name of the account. The env-scope account includes the environment name in the service account name. For example: 

  * Org-level: `apigee-udca-**my-project-id** -123abcd-sa` where `**my-project-id**` is the name project ID.
  * Env-level: `apigee-udca-**my-project-id** -**my-env** -234bcde-sa` where `**my-env**` is the name of the environment.



###  Non-prod 

  1. Define the `KSA_NAME`environment variables: 
         
         KSA_NAME="apigee-udca-service-account-name-sa"

for example: `apigee-udca-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
             --role roles/iam.workloadIdentityUser \
             --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
             $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
             --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
             --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-udca"
         KSA_NAME="apigee-udca-service-account-name-sa"

for example: `apigee-udca-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **Apigee Watcher**

Configure Workload identity for the Apigee Watcher component.

###  Non-prod 

  1. Define the `KSA_NAME`environment variables: 
         
         KSA_NAME="apigee-watcher-service-account-name-sa"

for example: `apigee-watcher-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-watcher"
         KSA_NAME="apigee-watcher-service-account-name-sa"

for example: `apigee-watcher-_hybrid-example-project-123abcd_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **Runtime**

Configure Workload identity for the Apigee Runtime component.

###  Non-prod 

  1. Define the `KSA_NAME`environment variables: 
         
         KSA_NAME="apigee-runtime-env-level-service-account-name-sa"

for example: `apigee-runtime-_hybrid-example-project-example-env-234bcde_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-runtime"
         KSA_NAME="apigee-runtime-env-level-service-account-name-sa"

for example: `apigee-runtime-_hybrid-example-project-example-env-234bcde_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **Synchronizer**

Configure Workload identity for the Synchronizer component.

###  Non-prod 

  1. Define the `KSA_NAME`environment variables: 
         
         KSA_NAME="apigee-synchronizer-env-level-service-account-name-sa"

for example: `apigee-synchronizer-_hybrid-example-project-example-env-234bcde_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-synchronizer"
         KSA_NAME="apigee-synchronizer-env-level-service-account-name-sa"

for example: `apigee-synchronizer-_hybrid-example-project-example-env-234bcde_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **UDCA (env-level)**

Configure Workload identity for the environment-level UDCA component.

###  Non-prod 

  1. Define the `KSA_NAME`environment variables: 
         
         KSA_NAME="apigee-udca-env-level-service-account-name-sa"

for example: `apigee-udca-_hybrid-example-project-example-env-234bcde_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME




###  Production 

  1. Define the `KSA_NAME` and `GSA_NAME` environment variables: 
         
         GSA_NAME="apigee-udca"
         KSA_NAME="apigee-udca-env-level-service-account-name-sa"

for example: `apigee-udca-_hybrid-example-project-example-env-234bcde_ -sa`.
  2. Bind the IAM role: 
         
         gcloud iam service-accounts add-iam-policy-binding \
           --role roles/iam.workloadIdentityUser \
           --member "serviceAccount:$PROJECT_ID.svc.id.goog[$NAMESPACE/$KSA_NAME]" \
           $GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com \
           --project $PROJECT_ID

  3. Annotate the service account: 
         
         kubectl annotate serviceaccount \
           --namespace $NAMESPACE $KSA_NAME iam.gke.io/gcp-service-account=$GSA_NAME@$PROJECT_ID.iam.gserviceaccount.com

  4. Verify the annotation: 
         
         kubectl describe serviceaccount \
           --namespace $NAMESPACE $KSA_NAME



* **Optional:** Delete the any downloaded service account key files. 

If you created the Google service accounts with the `create-service-account` tool, it may have created service account keys and downloaded the `.json` key files. When using Workload Identity on GKE, you do not need these key files.

You can delete the key files with the following command:
    
    
    rm $HYBRID_FILES/service-accounts/*.json

### Verify workload identity

  1. (Optional) You can see the status of your Kubernetes service accounts in the **Kubernetes: Workloads Overview** page in the Google Cloud console. 

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

**Note:** You may see an error status for the `apigee-cassandra-backup` and `apigee-cassandra-restore` service accounts. This is because you are not currently running backup or restore, and these processes have not been fully configured yet. For more information on Cassandra backup and restore, see [feedbackCassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-backup-overview).
  2. To check the status of the deployment again with `apigeectl check-ready`: 
         
         **${APIGEECTL_HOME}** /apigeectl check-ready -f ${HYBRID_FILES}/overrides/overrides.yaml


**Congratulations!**

You've successfully installed and configured the Apigee hybrid runtime plane. In the next step, you will configure the Apigee ingress gateway.

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-check-cluster) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-hybrid-runtime) [(NEXT) Step 10: Expose Apigee ingress](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-expose-apigee-ingress) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
