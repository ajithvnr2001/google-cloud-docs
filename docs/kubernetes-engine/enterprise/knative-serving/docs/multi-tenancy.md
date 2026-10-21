---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/multi-tenancy/
title: Cross-project multi-tenancy for Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:52:18.229474+00:00
---

# Cross-project multi-tenancy for Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/multi-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Cross-project multi-tenancy for Knative serving Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide walks you through configuring Knative serving to allow one or more Google Cloud projects to run and manage the workloads that are running on an GKE cluster in a different Google Cloud project.

A common operating model with Knative serving is for a team of application developers to use their Google Cloud project to deploy and manage services that are running in disparate GKE clusters across other teams' Google Cloud projects. This capability, called [multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview), enables you, as a platform operator, to tailor your development teams access to only their services that are running in your organizations various environments (for example, production vs. staging).

Knative serving specifically supports [enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview#enterprise_multi-tenancy). This type of multi-tenancy enables a _cluster Google Cloud project_ , to allow access to specific resources of their GKE cluster. The Google Cloud project that is granted access to the cluster Google Cloud project is the _tenant Google Cloud project_. Tenants of cluster Google Cloud project are able to use Knative serving to access, operate on, and own those services and resources for which they are granted access.

Conceptually, there are four steps to configuring enterprise multi-tenancy with Knative serving:

  1. Configure tenant access to the cluster Google Cloud project using a Google Group and Identity and Access Management.
  2. Map each tenant Google Cloud project to the cluster Google Cloud project.
  3. Route the cluster Google Cloud project log data to the tenant Google Cloud projects using log buckets and sinks.
  4. Define cluster permissions for tenants using role-based access control.



## Before you begin

The platform operator who is responsible for configuring multi-tenancy must understand and meet the following requirements:

  * As explained in the GKE documentation, you must understand the following multi-tenancy concepts:

    * [Google Cloud folder and project hierarchy for multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#folder-hierarchy)
    * [IAM permissions for group access control](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#assign-iam-roles)
    * [GKE role-based access control (RBAC) for tenant provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#tenant_provisioning)
    * [Multi-tenant logging on GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/multi-tenant-logging)
  * This document assumes that the Google Cloud projects that you want to enable multi-tenancy for already exist.

  * You must have access to the following Google Cloud projects services and resources:

    * Identity and Access Management permissions in the tenant Google Cloud project:

      * [roles/logging.configWriter](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles)
      * [Tenant admin](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#tenant-rbac) of the Google group
    * Identity and Access Management permissions in the cluster Google Cloud project:

      * [roles/logging.configWriter](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles)
      * [roles/resourcemanager.projectIamAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager)
      * [roles/resourcesettings.admin](https://developers.google.com/resource-settings/docs/reference/rest)
**Tip:** After you set your local environment variables in the next section, there are commands that you should run to test and verify that you have these IAM permissions.
  * You must have or install the latest version of the [Google Cloud CLI]](/sdk/docs/install).




## Define local environment variables

To simplify the commands used in this process, define local environment variables for both the cluster Google Cloud project and tenant Google Cloud project:

  1. Replace `YOUR_CLUSTER_PROJECT_ID` with the ID of the cluster Google Cloud project and then run the following command:
         
         export CLUSTER_PROJECT_ID=YOUR_CLUSTER_PROJECT_ID
         

  2. Replace `YOUR_TENANT_PROJECT_ID` with the ID of the tenant Google Cloud project and then run the following command:
         
         export TENANT_PROJECT_ID=$YOUR_TENANT_PROJECT_ID
         

  3. Verify your local environment variables by running the following commands:
         
         echo "cluster Google Cloud project is:" $CLUSTER_PROJECT_ID
         echo "tenant Google Cloud project is:" $TENANT_PROJECT_ID
         




Your cluster Google Cloud project ID and tenant Google Cloud project ID are now used in all the following commands where `$CLUSTER_PROJECT_ID` and `$TENANT_PROJECT_ID` are specified.

### Verifying your IAM permissions

Run the following [testIamPermissions](https://docs.cloud.google.com/iam/docs/testing-permissions) commands to validate that you have the required IAM permissions to access the resources on the cluster Google Cloud project as well as the tenant Google Cloud projects.

Run the following command to validate your permissions on the cluster Google Cloud project:
    
    
    curl -X POST \
      -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
      --header "Content-Type: application/json" \
      --data '{"permissions":["logging.sinks.create", "logging.sinks.get", "resourcemanager.projects.setIamPolicy"]}' \
      https://cloudresourcemanager.googleapis.com/v1/projects/$CLUSTER_PROJECT_ID:testIamPermissions
    

Expected results for the cluster Google Cloud project:
    
    
    {
      "permissions": [
        "logging.sinks.create",
        "logging.sinks.get",
        "resourcemanager.projects.setIamPolicy"
      ]
    }
    

Run the following command to validate your permissions on each tenant Google Cloud project:
    
    
    curl -X POST \
      -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
      --header "Content-Type: application/json" \
      --data '{"permissions":["logging.buckets.create", "logging.buckets.get", "resourcemanager.projects.setIamPolicy", "resourcesettings.settingvalues.create", "serviceusage.services.enable"]}' \
      https://cloudresourcemanager.googleapis.com/v1/projects/$TENANT_PROJECT_ID:testIamPermissions
    

Expected results for each tenant Google Cloud project:
    
    
    {
      "permissions": [
        "logging.buckets.create",
        "logging.buckets.get",
        "resourcemanager.projects.setIamPolicy",
        "resourcesettings.settingvalues.create",
        "serviceusage.services.enable",
      ]
    }
    

## Use a Google Group and Identity and Access Management to configure tenant access

Use a Google Group to allow tenants to access the GKE cluster. The IAM permissions give tenants the permissions to get credentials but they won't be able do anything in the cluster until the Kubernetes role-based access control is configured in a later step.

You must create a Google Group that contains all of your tenant Google Cloud project's users. For more information about using a security group, see [Using Google Groups for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-setup-gsuite).

Create the following local environment variable for your Google Group:
    
    
    export SECURITY_GROUP=gke-security-groups@company.com
    

### Kubernetes Cluster Viewer

Run the following commands to allow the tenants to get credentials to the cluster, this does not allow the tenants to read or manipulate any resources on the GKE cluster.

[IAM Reference](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/iam#roles)
    
    
    gcloud projects add-iam-policy-binding $CLUSTER_PROJECT_ID \
       --member=group:$SECURITY_GROUP \
       --role='roles/container.clusterViewer' \
       --condition=None
    

To restrict access to a specific cluster, you can use a [IAM condition](https://docs.cloud.google.com/iam/docs/conditions-overview).
    
    
    gcloud projects add-iam-policy-binding $CLUSTER_PROJECT_ID \
       --member=group:$SECURITY_GROUP \
       --role='roles/container.clusterViewer' \
       --condition="expression=resource.name == 'cluster-name',title=Restrict cluster access"
    

### Monitoring Viewer

Run the following command to allow tenants to read monitoring metrics.

[Monitoring Roles Reference](https://docs.cloud.google.com/monitoring/access-control#predefined_roles)
    
    
    gcloud projects add-iam-policy-binding $CLUSTER_PROJECT_ID \
       --member=group:$SECURITY_GROUP \
       --role='roles/monitoring.viewer' \
       --condition=None
    

## Mapping each tenant Google Cloud project to the cluster Google Cloud project

You use resource setting values to map tenant Google Cloud projects to a cluster Google Cloud project.

The resource setting can be configured for each individual tenant Google Cloud project, or can be set at any level of the folder hierarchy. It is easier to set this on the single tenant folder level, but more flexible to set on each tenant project level. After this is setup, whenever tenants browse the Knative serving UI, they will also see their services on the cluster Google Cloud project. This does not change IAM permissions on the cluster Google Cloud project or the GKE clusters, it is only a mapping from a tenant project (or folder) to a cluster Google Cloud project.

  1. Enable the `resourcesettings` API on the tenant Google Cloud project.
         
         gcloud services enable resourcesettings.googleapis.com \
           --project=$TENANT_PROJECT_ID
         

  2. Add the Organization Admin privileges (`roles/resourcesettings.admin`) to your user ID by running the following command:
         
         gcloud organizations add-iam-policy-binding YOUR_ORGANIZATION_ID \
           --member=YOUR_ADMIN_MEMBER_ID \
           --role='roles/resourcesettings.admin'
         

Replace `YOUR_ORGANIZATION_ID` with the [ID of your organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) and `YOUR_ADMIN_MEMBER_ID` with your user ID, for example `user:my-email@my-domain.com`.

  3. Choose one of the following methods to define the mapping.

You can set the resource setting value on a parent Google Cloud folder, if all of the child Google Cloud projects and Google Cloud folders use that same value.




### Tenant projects

Set the resource setting value for each tenant Google Cloud project:

  1. Obtain the `name` of the tenant Google Cloud project and set that to a local environment variable: 
         
         export TENANT_PROJECT_NUMBER=$(gcloud projects describe $TENANT_PROJECT_ID --format="value(projectNumber)")

  2. Create a resource setting value file to define the mapping from the tenant Google Cloud project to the cluster Google Cloud project. Multiple cluster Google Cloud project IDs can be defined in this file and added to a single tenant Google Cloud project. 
         
         cat > value-file.json << EOF
         {
         "name": "projects/$TENANT_PROJECT_NUMBER/settings/cloudrun-multiTenancy/value",
         "value": {
           "stringSetValue": {
             "values": [ "projects/$CLUSTER_PROJECT_ID" ]
           }
         }
         }
         EOF

  3. Deploy the resource settings to the tenant Google Cloud project: 
         
         gcloud resource-settings set-value cloudrun-multiTenancy --value-file value-file.json --project $TENANT_PROJECT_ID




### Tenant folders

Set resource setting value for a parent tenant folder to set that value to all of the child tenant Google Cloud projects and folders:

  1. Obtain the `number` of the tenant folder and set that to a local environment variable: 
         
         export TENANT_FOLDER_NUMBER=$TENANT_FOLDER_NUMBER

  2. Create a resource setting value file to define the mapping from the tenant folder to the cluster Google Cloud project. Multiple cluster Google Cloud project IDs can be defined in this file and added to a single tenant folder. 
         
         cat > value-file.json << EOF
         {
         "name": "folders/$TENANT_FOLDER_NUMBER/settings/cloudrun-multiTenancy/value",
         "value": {
           "stringSetValue": {
             "values": [ "projects/$CLUSTER_PROJECT_ID" ]
           }
         }
         }
         EOF

  3. Deploy the resource settings to the tenant folder: 
         
         gcloud resource-settings set-value cloudrun-multiTenancy --value-file value-file.json --folder $TENANT_FOLDER_NUMBER




## Setting up the logs buckets and sinks to route log data

For each tenant, you create a log bucket, sink, and the permissions to route the cluster Google Cloud project log data to the tenant Google Cloud project. In the following steps, all logs from the namespace in cluster Google Cloud project are routed to the bucket. See the set below for details about how to limit which logs are shared.

Create the following local environment variables:

  * Specify the namespace of the GKE cluster that your tenants access.
  * The name of the sink. To simplify this step, the name is a combination of the cluster Google Cloud project and tenant Google Cloud project local environment variables that you previously created. You can modify this value.


    
    
    export NAMESPACE=$NAMESPACE
    export SINK_NAME=$CLUSTER_PROJECT_ID-$TENANT_PROJECT_ID
    

Run the following command to create the logs bucket in the tenant project. Note that the log bucket name must be the ID of the cluster Google Cloud project and cannot be changed or modified.
    
    
    gcloud logging buckets \
       create $CLUSTER_PROJECT_ID \
       --location=global \
       --project=$TENANT_PROJECT_ID
    

Run the following command to create the sink from the specified namespace in the cluster Google Cloud project, to the tenant Google Cloud project bucket. Note that you can narrow the scope of the logs, for example to share only individual GKE cluster or specific Knative serving resources by defining additional [`log-filter` values](https://docs.cloud.google.com/sdk/gcloud/reference/logging/sinks/create).
    
    
    gcloud logging sinks \
       create $SINK_NAME \
       logging.googleapis.com/projects/$TENANT_PROJECT_ID/locations/global/buckets/$CLUSTER_PROJECT_ID \
       --log-filter=resource.labels.namespace_name=$NAMESPACE \
       --project $CLUSTER_PROJECT_ID
    

Run the following commands to add the permission from the log sink service account to the bucket that you created.
    
    
    export SINK_SERVICE_ACCOUNT=$(gcloud logging sinks \
       describe $SINK_NAME \
       --project $CLUSTER_PROJECT_ID \
       --format="value(writerIdentity)")
    
    
    
    gcloud projects add-iam-policy-binding $TENANT_PROJECT_ID \
       --member=$SINK_SERVICE_ACCOUNT \
       --role='roles/logging.bucketWriter' \
       --condition="expression=resource.name.endsWith\
       (\"locations/global/buckets/$CLUSTER_PROJECT_ID\"),\
       title=Log bucket writer from $CLUSTER_PROJECT_ID"
    

## Setting up tenant permissions with role-based access control (RBAC)

You previously used Google Groups and IAM to configure permissions to allow tenants to access the Google Cloud project of the GKE cluster. To allow tenants access to the resources within the GKE cluster, you must define permissions with Kubernetes RBAC.

### Create Cluster Roles

After you define and create the following cluster roles, you can continue to use these in the future to add all subsequent tenants of the cluster Google Cloud project.

### UI Roles

This role allows tenants to query all namespaces. This is required to find which namespaces users have access to create `/sdk/gcloud/reference/logging/sinks/create` services.
    
    
    kubectl create clusterrole \
       namespace-lister \
       --verb=list \
       --resource=namespaces
    

This role allows tenants to view Knative serving services. This is required to list the services in the Knative serving UI.
    
    
    kubectl create clusterrole \
       ksvc-lister \
       --verb=list \
       --resource=services.serving.knative.dev
    

### Create Cluster Roles

Only one of these permissions are required. The first permission allows tenants to manipulate any resource in their namespace. The second permission allows for a more limited set of just creating Knative serving services.
    
    
    kubectl create clusterrole \
       kubernetes-developer \
       --verb="*" \
       --resource="*.*"
    

If the `kubernetes-developer` permission is too permissive, the following allows tenants to create Knative services on their namespaces and view the other Knative resources.
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: knative-developer
    rules:
    - apiGroups: ["serving.knative.dev"]
      resources: ["services"]
      verbs: ["*"]
    - apiGroups: ["serving.knative.dev"]
      resources: ["*"]
      verbs: ["get", "list", "watch"]
    EOF
    

### Create Tenant namespace and assign permissions.

Note this assumes you have setup using [Google Groups for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-create-cluster). This is necessary to do for each tenant.
    
    
    export TENANT_GROUP=tenant-a@company.com
    

> TENANT_GROUP must be a part of SECURITY_GROUP

#### Ability to view all namespaces

In order to query the GKE cluster, all tenants most have the ability to list namespaces. There is not currently an [auth can-i](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#groups-create-cluster) which returns namespaces for which an action is possible. The only work-around is to list namespaces and then query each namespace individually.
    
    
    kubectl create clusterrolebinding \
       all-namespace-listers \
       --clusterrole=namespace-lister \
       --group=$TENANT_GROUP
    

#### Ability to list Knative serving services
    
    
    kubectl create clusterrolebinding \
       all-ksvc-listers \
       --clusterrole=ksvc-lister \
       --group=$TENANT_GROUP
    

#### Ability to manipulate resources on the namespace

First create the namespace:
    
    
    kubectl create namespace $NAMESPACE
    

If using the kubernetes-developer role:
    
    
    kubectl create rolebinding \
       kubernetes-developer \
       --namespace=$NAMESPACE \
       --clusterrole=kubernetes-developer \
       --group=$TENANT_GROUP
    

If using the knative-developer role:
    
    
    kubectl create rolebinding \
       kubernetes-developer \
       --namespace=$NAMESPACE \
       --clusterrole=knative-developer \
       --group=$TENANT_GROUP
    

### Add ability for tenant to access external ip address
    
    
    cat <<EOF | kubectl apply -f -
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: ingress-reader
    rules:
    - apiGroups: [""]
      resources: ["services"]
      verbs: ["get"]
    EOF
    
    
    
    kubectl create rolebinding \
       ingress-reader-$TENANT_GROUP \
       --namespace=istio-system \
       --clusterrole=ingress-reader \
       --group=$TENANT_GROUP
    

## Verify

You can verify that you have successfully configured enterprise multi-tenancy by opening the tenant Google Cloud project in Knative serving and deploying a service to a GKE cluster.

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

Congratulations, your tenant can now interact with the services and resources within the GKE cluster namespace that they have been granted access.

## Multi-tenancy reference

  * [GKE multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview)
  * [GKE multi-tenancy best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)
  * [Namespace quota](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
