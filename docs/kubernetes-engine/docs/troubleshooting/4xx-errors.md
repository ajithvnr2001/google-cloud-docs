---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/4xx-errors/
title: Troubleshoot 4xx errors \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:34:46.755493+00:00
---

# Troubleshoot 4xx errors  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/4xx-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshoot 4xx errors Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page helps you resolve 400, 401, 403, and 404 errors that you might encounter when using Google Kubernetes Engine (GKE).

## Issue: Authentication and authorization errors

When connecting to GKE clusters, you can get an authentication and authorization error with HTTP status code `401 (Unauthorized)`. This issue might occur when you try to run a `kubectl` command in your GKE cluster from a local environment.

The cause of this issue might be one of the following:

  * The `gke-gcloud-auth-plugin` authentication plugin is not correctly installed or configured.
  * You lack the permissions to connect to the cluster API server and run `kubectl` commands.



To diagnose the cause, complete the steps in the following sections:

  1. Connect to the cluster using `curl`
  2. Configure the plugin in kubeconfig



### Connect to the cluster using `curl`

To diagnose the cause of the authentication and authorization error, connect to the cluster using `curl`. Using `curl` bypasses the `kubectl` command-line tool and the `gke-gcloud-auth-plugin` plugin.

  1. Set environment variables:
         
         APISERVER=https://$(gcloud container clusters describe CLUSTER_NAME \
             --location=COMPUTE_LOCATION --format "value(endpoint)")
         TOKEN=$(gcloud auth print-access-token)
         

  2. Verify that your access token is valid:
         
         curl https://oauth2.googleapis.com/tokeninfo?access_token=$TOKEN
         

When you have a valid access token, this command sends a request to Google's OAuth 2.0 server and the server responds with information about the token.

  3. Try to connect to the core API endpoint in the API server:
         
         # Get cluster CA certificate
         gcloud container clusters describe CLUSTER_NAME \
             --location=COMPUTE_LOCATION \
             --format "value(masterAuth.clusterCaCertificate)" | \
             base64 -d > /tmp/ca.crt
         
         # Make API call with authentication and CA certificate
         curl -s -X GET "${APISERVER}/api/v1/namespaces" \
             --header "Authorization: Bearer $TOKEN" \
             --cacert /tmp/ca.crt
         

If the `curl` command succeeds, you'll see a list of namespaces. Proceed to check whether the plugin is the cause using the steps in the Configure the plugin in kubeconfig section.

If the `curl` command fails with an output that is similar to the following, then you don't have the correct permissions to access the cluster:
         
         {
         "kind": "Status",
         "apiVersion": "v1",
         "metadata": {},
         "status": "Failure",
         "message": "Unauthorized",
         "reason": "Unauthorized",
         "code": 401
         }
         

To resolve this issue, consult your administrator to get the correct permissions to access the cluster.




### Configure use of the plugin in kubeconfig

If you're getting authentication and authorization errors when connecting to your clusters but were able to connect to the cluster using `curl`, then ensure that you can access your cluster without needing the `gke-gcloud-auth-plugin` plugin.

To resolve this issue, configure your local environment to ignore the `gke-gcloud-auth-plugin` binary when authenticating to the cluster. In Kubernetes clients running version 1.25 and later, the `gke-gcloud-auth-plugin` binary is _required_ , so you need to use a version of 1.24 or earlier for the `kubectl` command-line tool.

Follow these steps to access your cluster without needing the plugin:

  1. Install the `kubectl` command-line tool with version 1.24 or earlier using `curl`. The following example installs the tool with version 1.24:
         
         curl -LO https://dl.k8s.io/release/v1.24.0/bin/linux/amd64/kubectl
         

  2. Open your shell startup script file in a text editor. For example, open `.bashrc` for the Bash shell:
         
         vi ~/.bashrc
         

If you are using macOS, use `~/.bash_profile` instead of `.bashrc` in these instructions.

  3. Add the following line to the startup script file and save it:
         
         export USE_GKE_GCLOUD_AUTH_PLUGIN=False
         

  4. Run the startup script:
         
         source ~/.bashrc
         

  5. Get credentials for your cluster, which sets up your `.kube/config` file:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=COMPUTE_LOCATION
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster.
     * `COMPUTE_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).
  6. Run a `kubectl` command. For example:
         
         kubectl cluster-info
         

If you get a 401 error or a similar authorization error after running these commands, ensure that you have the correct permissions, then rerun the step that returned the error.




## Error 400: Node pool requires recreation

The following error can occur when you try to perform an action that recreates your control plane and nodes:
    
    
    ERROR: (gcloud.container.clusters.update) ResponseError: code=400, message=Node pool "test-pool-1" requires recreation.
    

For example, this error can occur when you [complete an ongoing credential rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#completing_the_rotation).

On the backend, node pools are marked for recreation, but the actual recreation operation might take some time to begin. Because of this, the operation fails because GKE has not recreated one or more node pools in your cluster yet.

To resolve this issue, choose one of the following solutions:

  * Wait for the recreation to happen. This might take hours, days, or weeks depending on factors such as existing maintenance windows and exclusions.
  * Manually start a recreation of the affected node pools by starting a version upgrade to the same version as the control plane.

To start a recreation, run the following command:
        
        gcloud container clusters upgrade CLUSTER_NAME \
            --node-pool=POOL_NAME
        

After the upgrade completes, try the operation again.




## Error 401: Unauthorized

### Identify clusters with node service accounts missing critical permissions

To identify clusters with node service accounts missing critical permissions, use [GKE recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) of `NODE_SA_MISSING_PERMISSIONS` [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype):

  * Use the Google Cloud console. Go to the [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list) page and check for **Grant critical permissions** recommendation in the **Notifications** column for specific clusters.
  * Use the gcloud CLI or Recommender API, by specifying the `NODE_SA_MISSING_PERMISSIONS` recommender subtype.

To query recommendations, run the following command:
        
        gcloud recommender recommendations list \
            --recommender=google.container.DiagnosisRecommender \
            --location LOCATION \
            --project PROJECT_ID \
            --format yaml \
            --filter="recommenderSubtype:NODE_SA_MISSING_PERMISSIONS"
        




Note, it may take up to 24 hours for the recommendation to appear. For detailed instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation, grant the `roles/container.defaultNodeServiceAccount` role to the node's service account.

You can run a script that searches node pools in your project's Standard and Autopilot clusters for any node service accounts that don't have the required permissions for GKE. This script uses the gcloud CLI and the `jq` utility. To view the script, expand the following section:

View the script
    
    
    #!/bin/bash
    
    # Set your project ID
    project_id=PROJECT_ID
    project_number=$(gcloud projects describe "$project_id" --format="value(projectNumber)")
    declare -a all_service_accounts
    declare -a sa_missing_permissions
    
    # Function to check if a service account has a specific permission
    # $1: project_id
    # $2: service_account
    # $3: permission
    service_account_has_permission() {
      local project_id="$1"
      local service_account="$2"
      local permission="$3"
    
      local roles=$(gcloud projects get-iam-policy "$project_id" \
              --flatten="bindings[].members" \
              --format="table[no-heading](bindings.role)" \
              --filter="bindings.members:\"$service_account\"")
    
      for role in $roles; do
        if role_has_permission "$role" "$permission"; then
          echo "Yes" # Has permission
          return
        fi
      done
    
      echo "No" # Does not have permission
    }
    
    # Function to check if a role has the specific permission
    # $1: role
    # $2: permission
    role_has_permission() {
      local role="$1"
      local permission="$2"
      gcloud iam roles describe "$role" --format="json" | \
      jq -r ".includedPermissions" | \
      grep -q "$permission"
    }
    
    # Function to add $1 into the service account array all_service_accounts
    # $1: service account
    add_service_account() {
      local service_account="$1"
      all_service_accounts+=( ${service_account} )
    }
    
    # Function to add service accounts into the global array all_service_accounts for a Standard GKE cluster
    # $1: project_id
    # $2: location
    # $3: cluster_name
    add_service_accounts_for_standard() {
      local project_id="$1"
      local cluster_location="$2"
      local cluster_name="$3"
    
      while read nodepool; do
        nodepool_name=$(echo "$nodepool" | awk '{print $1}')
        if [[ "$nodepool_name" == "" ]]; then
          # skip the empty line which is from running `gcloud container node-pools list` in GCP console
          continue
        fi
        while read nodepool_details; do
          service_account=$(echo "$nodepool_details" | awk '{print $1}')
    
          if [[ "$service_account" == "default" ]]; then
            service_account="${project_number}-compute@developer.gserviceaccount.com"
          fi
          if [[ -n "$service_account" ]]; then
            printf "%-60s| %-40s| %-40s| %-10s| %-20s\n" $service_account $project_id  $cluster_name $cluster_location $nodepool_name
            add_service_account "${service_account}"
          else
            echo "cannot find service account for node pool $project_id\t$cluster_name\t$cluster_location\t$nodepool_details"
          fi
        done <<< "$(gcloud container node-pools describe "$nodepool_name" --cluster "$cluster_name" --zone "$cluster_location" --project "$project_id" --format="table[no-heading](config.serviceAccount)")"
      done <<< "$(gcloud container node-pools list --cluster "$cluster_name" --zone "$cluster_location" --project "$project_id" --format="table[no-heading](name)")"
    
    }
    
    # Function to add service accounts into the global array all_service_accounts for an Autopilot GKE cluster
    # Autopilot cluster only has one node service account.
    # $1: project_id
    # $2: location
    # $3: cluster_name
    add_service_account_for_autopilot(){
      local project_id="$1"
      local cluster_location="$2"
      local cluster_name="$3"
    
      while read service_account; do
          if [[ "$service_account" == "default" ]]; then
            service_account="${project_number}-compute@developer.gserviceaccount.com"
          fi
          if [[ -n "$service_account" ]]; then
            printf "%-60s| %-40s| %-40s| %-10s| %-20s\n" $service_account $project_id  $cluster_name $cluster_location $nodepool_name
            add_service_account "${service_account}"
          else
            echo "cannot find service account" for cluster  "$project_id\t$cluster_name\t$cluster_location\t"
          fi
      done <<< "$(gcloud container clusters describe "$cluster_name" --location "$cluster_location" --project "$project_id" --format="table[no-heading](autoscaling.autoprovisioningNodePoolDefaults.serviceAccount)")"
    }
    
    
    # Function to check whether the cluster is an Autopilot cluster or not
    # $1: project_id
    # $2: location
    # $3: cluster_name
    is_autopilot_cluster() {
      local project_id="$1"
      local cluster_location="$2"
      local cluster_name="$3"
      autopilot=$(gcloud container clusters describe "$cluster_name" --location "$cluster_location" --format="table[no-heading](autopilot.enabled)")
      echo "$autopilot"
    }
    
    
    echo "--- 1. List all service accounts in all GKE node pools"
    printf "%-60s| %-40s| %-40s| %-10s| %-20s\n" "service_account" "project_id" "cluster_name" "cluster_location" "nodepool_name"
    while read cluster; do
      cluster_name=$(echo "$cluster" | awk '{print $1}')
      cluster_location=$(echo "$cluster" | awk '{print $2}')
      # how to find a cluster is a Standard cluster or an Autopilot cluster
      autopilot=$(is_autopilot_cluster "$project_id" "$cluster_location" "$cluster_name")
      if [[ "$autopilot" == "True" ]]; then
        add_service_account_for_autopilot "$project_id" "$cluster_location"  "$cluster_name"
      else
        add_service_accounts_for_standard "$project_id" "$cluster_location"  "$cluster_name"
      fi
    done <<< "$(gcloud container clusters list --project "$project_id" --format="value(name,location)")"
    
    echo "--- 2. Check if service accounts have permissions"
    unique_service_accounts=($(echo "${all_service_accounts[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
    
    echo "Service accounts: ${unique_service_accounts[@]}"
    printf "%-60s| %-40s| %-40s| %-20s\n" "service_account" "has_logging_permission" "has_monitoring_permission" "has_performance_hpa_metric_write_permission"
    for sa in "${unique_service_accounts[@]}"; do
      logging_permission=$(service_account_has_permission "$project_id" "$sa" "logging.logEntries.create")
      time_series_create_permission=$(service_account_has_permission "$project_id" "$sa" "monitoring.timeSeries.create")
      metric_descriptors_create_permission=$(service_account_has_permission "$project_id" "$sa" "monitoring.metricDescriptors.create")
      if [[ "$time_series_create_permission" == "No" || "$metric_descriptors_create_permission" == "No" ]]; then
        monitoring_permission="No"
      else
        monitoring_permission="Yes"
      fi
      performance_hpa_metric_write_permission=$(service_account_has_permission "$project_id" "$sa" "autoscaling.sites.writeMetrics")
      printf "%-60s| %-40s| %-40s| %-20s\n" $sa $logging_permission $monitoring_permission $performance_hpa_metric_write_permission
    
      if [[ "$logging_permission" == "No" || "$monitoring_permission" == "No" || "$performance_hpa_metric_write_permission" == "No" ]]; then
        sa_missing_permissions+=( ${sa} )
      fi
    done
    
    echo "--- 3. List all service accounts that don't have the above permissions"
    if [[ "${#sa_missing_permissions[@]}" -gt 0 ]]; then
      printf "Grant roles/container.defaultNodeServiceAccount to the following service accounts: %s\n" "${sa_missing_permissions[@]}"
    else
      echo "All service accounts have the above permissions"
    fi

### Identify node service accounts missing critical permissions in a cluster

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

If your organization enforces the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account in your project might not automatically get the required permissions for GKE. 

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

  1. Find the name of the service account that your nodes use:

### Console

     1. Go to the **Kubernetes clusters** page: 

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

     2. In the cluster list, click the name of the cluster that you want to inspect.
     3. Depending on the cluster mode of operation, do one of the following: 
        * For Autopilot mode clusters, in the **Security** section, find the **Service account** field.
        * For Standard mode clusters, do the following: 
          1. Click the **Nodes** tab.
          2. In the **Node pools** table, click a node pool name. The **Node pool details** page opens.
          3. In the **Security** section, find the **Service account** field.

If the value in the **Service account** field is `default`, your nodes use the Compute Engine default service account. If the value in this field is _not_ `default`, your nodes use a custom service account. To grant the required role to a custom service account, see [Use least privilege IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

### gcloud

For Autopilot mode clusters, run the following command:
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=autoscaling.autoprovisioningNodePoolDefaults.serviceAccount

For Standard mode clusters, run the following command:
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --format="table(nodePools.name,nodePools.config.serviceAccount)"

If the output is `default`, your nodes use the Compute Engine default service account. If the output is _not_ `default`, your nodes use a custom service account. To grant the required role to a custom service account, see [Use least privilege IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  2. To grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account, complete the following steps:

### Console

     1. Go to the **Welcome** page: 

[Go to Welcome](https://console.cloud.google.com/welcome)

     2. In the **Project number** field, click content_copy **Copy to clipboard**.
     3. Go to the **IAM** page: 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

     4. Click person_add **Grant access**.
     5. In the **New principals** field, specify the following value: 
            
            PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with the project number that you copied. 
     6. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
     7. Click **Save**.

### gcloud

     1. Find your Google Cloud project number: 
            
            gcloud projects describe PROJECT_ID \
                --format="value(projectNumber)"

Replace `PROJECT_ID` with your project ID.

The output is similar to the following:
            
            12345678901
            

     2. Grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
                --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
                --role="roles/container.defaultNodeServiceAccount"

Replace `PROJECT_NUMBER` with the project number from the previous step.




## Error 403: Insufficient permissions

The following error occurs when you try to connect to a GKE cluster using `gcloud container clusters get-credentials`, but the account doesn't have permission to access the Kubernetes API server:
    
    
    ERROR: (gcloud.container.clusters.get-credentials) ResponseError: code=403, message=Required "container.clusters.get" permission(s) for "projects/<your-project>/locations/<region>/clusters/<your-cluster>".
    

To resolve this issue, complete the following steps:

  1. Identify the account that has the access issue:
         
         gcloud auth list
         

  2. Grant the required access to the account using the instructions in [Authenticating to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication#applications_within).




## Error 403: Retry budget exhausted

The following error can occur when you try to create a GKE cluster:
    
    
    Error: googleapi: Error 403: Retry budget exhausted: Google Compute Engine:
    Required permission 'PERMISSION_NAME' for 'RESOURCE_NAME'.
    

In this error message, the following variables apply:

  * `PERMISSION_NAME`: the name of a permission, like `compute.regions.get`.
  * `RESOURCE_NAME`: the path to the Google Cloud resource that you were trying to access, like a Compute Engine region.



This error occurs if the IAM service account attached to the cluster doesn't have the minimum required permissions to create the cluster.

To resolve this issue, do the following:

  1. Create or modify an IAM service account to have all of the required permissions to run a GKE cluster. For instructions, see [Use least privilege IAM service accounts](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).
  2. Specify the updated IAM service account in your cluster creation command by using the `--service-account` flag. For instructions, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#create_an_autopilot_cluster).



Alternatively, omit the `--service-account` flag to let GKE use the Compute Engine default service account in the project, which has the required permissions by default.

## Error 404: Resource not found

If you get an error 404, resource not found, when calling `gcloud container` commands, resolve the issue by re-authenticating to the Google Cloud CLI:
    
    
    gcloud auth login
    

## Error 400/403: Missing edit permissions on account

A missing edit permissions on account error (error 400 or 403), indicates that one of the following has been deleted or edited manually:

  * Your [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
  * The [Google APIs Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent).
  * The [service account associated with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization).



When you enable the Compute Engine or GKE API, Google Cloud creates the following service accounts and agents:

  * _Compute Engine default service account_ in your project. GKE attaches this service account to nodes by default for system tasks like logging and monitoring.
  * _Google APIs Service Agent_ in a Google-managed project, with edit permissions on your project.
  * _Google Kubernetes Engine service agents_ in a Google-managed project, with the _Kubernetes Engine Service Agent_ and _Kubernetes Engine Default Node Service Agent_ on your project.



Cluster creation and all management fails if, at any point, someone edits those permissions, removes the role bindings on the project, removes the service account entirely, or disables the API.

**Note:** If you don't use custom IAM service accounts to create your GKE clusters or node pools, ensure that the default Compute Engine service account in your project has the required permissions for GKE. In organizations that enforce the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account won't automatically get the required permissions for GKE. This constraint is enforced by default for organizations that were created on or after May 3, 2024. For details, see [Default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent). 

### Verify permissions for the GKE service agents

Google Kubernetes Engine has the following service agents:

  * _Kubernetes Engine Service Agent_ , which is used to manage compute resources such as instances, disks, and load balancers.

  * _Kubernetes Engine Default Node Service Agent_ , which is used by Google Kubernetes Engine node system workloads to support standard capabilities such as logging and monitoring.




To verify whether the Google Kubernetes Engine service agents have the _Kubernetes Engine Service Agent_ role assigned on the project, complete the following steps:

  1. Determine the name of your Google Kubernetes Engine service agents. Service agents have the following format:

     * Kubernetes Engine Service Agent:
    
    service-PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com
    

     * Kubernetes Engine Default Node Service Agent:
    
    service-PROJECT_NUMBER@gcp-sa-gkenode.iam.gserviceaccount.com
    

Replace `PROJECT_NUMBER` with your [project number](https://console.cloud.google.com/).

  2. Verify that your Google Kubernetes Engine service agents have the _Kubernetes Engine Service Agent_ and the _Kubernetes Engine Default Node Service Agent_ roles assigned on the project:
         
         gcloud projects get-iam-policy PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.




If someone removed the _Kubernetes Engine Service Agent_ or the _Kubernetes Engine Default Node Service Agent_ from your Google Kubernetes Engine service agents, confirm that the Kubernetes Engine API is enabled and grant the necessary roles to your service agents:

### Console

  1. In the Google Cloud console, go to the **Kubernetes Engine API** page.

[Go to the **Kubernetes Engine API page**](https://console.cloud.google.com/apis/library/container.googleapis.com)

  2. Select your project.

  3. If you see an **Enable** button, click it to enable the Kubernetes Engine API. This process creates the required service agents and grants them the required roles on your project. It might take several minutes to complete.

  4. If you see a **Manage** button, the Kubernetes Engine API is already enabled. Click the **Manage** button.

     1. If you have the option to **Disable** the API, you should do so and then enable it again. This action re-creates the required service agents and grants them the required roles on your project.

     2. If you don't have the option to disable the API, then you must manually create the service agents and grant them the required roles. Follow the instructions in [Create and grant roles to service agents](https://docs.cloud.google.com/iam/docs/create-service-agents).




### gcloud

Run the following commands in the gcloud CLI:
    
    
    PROJECT_NUMBER=$(gcloud projects describe "PROJECT_ID"
        --format 'get(projectNumber)')
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:service-${PROJECT_NUMBER?}@container-engine-robot.iam.gserviceaccount.com" \
        --role roles/container.serviceAgent
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:service-${PROJECT_NUMBER?}@gcp-sa-gkenode.iam.gserviceaccount.com" \
        --role roles/container.defaultNodeServiceAgent
    

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
