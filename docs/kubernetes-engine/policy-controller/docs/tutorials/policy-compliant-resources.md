---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/policy-compliant-resources/
title: Create policy-compliant Google Cloud resources \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:50.951438+00:00
---

# Create policy-compliant Google Cloud resources  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/policy-compliant-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Create policy-compliant Google Cloud resources Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how platform administrators can use [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview) policies to govern how to create Google Cloud resources using [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview).

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

The instructions in this tutorial assume that you have basic knowledge of [Kubernetes](http://kubernetes.io/) or [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs). In the tutorial, you define a policy that restricts permitted locations for [Cloud Storage](https://docs.cloud.google.com/storage/docs) buckets.

Policy Controller checks, audits, and enforces the compliance of your Kubernetes cluster resources with policies related to security, regulations, or business rules. Policy Controller is built from the [OPA Gatekeeper open source project](https://github.com/open-policy-agent/gatekeeper).

Config Connector creates and manages the lifecycle of [Google Cloud resources](https://docs.cloud.google.com/config-connector/docs/reference/overview), by describing them as [Kubernetes custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). To create a Google Cloud resource, you create a Kubernetes resource in a namespace that Config Connector manages. The following example shows how to describe a Cloud Storage bucket using Config Connector:
    
    
    apiVersion: storage.cnrm.cloud.google.com/v1beta1
    kind: StorageBucket
    metadata:
      name: my-bucket
    spec:
      location: us-east1
    

By managing your Google Cloud resources with Config Connector, you can apply Policy Controller policies to those resources as you create them in your Google Kubernetes Engine cluster. These policies let you prevent or report actions that create or modify resources in ways that violate your policies. For example, you can enforce a policy that restricts the locations of Cloud Storage buckets.

This approach, based on the [Kubernetes resource model (KRM)](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md#the-kubernetes-resource-model-krm), lets you use a consistent set of tools and workflows to manage both Kubernetes and Google Cloud resources. This tutorial demonstrates how you can complete the following tasks:

  * Define policies that govern your Google Cloud resources.
  * Implement controls that prevent developers and administrators from creating Google Cloud resources that violate your policies.
  * Implement controls that audit your existing Google Cloud resources against your policies, even if you created those resources outside Config Connector.
  * Provide fast feedback to developers and administrators as they create and update resource definitions.
  * Validate Google Cloud resource definitions against your policies before attempting to apply the definitions to a Kubernetes cluster.



## Objectives

  * Create a GKE cluster that includes the Config Connector add-on.
  * Install Policy Controller.
  * Create a policy to restrict permitted Cloud Storage bucket locations.
  * Verify that the policy prevents creation of Cloud Storage buckets in non-permitted locations.
  * Evaluate policy compliance of Cloud Storage bucket definition during development.
  * Audit existing Cloud Storage buckets for policy compliance. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Asset Inventory](https://cloud.google.com/asset-inventory/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  4. In Cloud Shell, set the Google Cloud project that you want to use for this tutorial:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the [Google Cloud project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your project. When you run this command, Cloud Shell creates an exported environment variable called `GOOGLE_CLOUD_PROJECT` that contains your project ID. If you do not use Cloud Shell, you can create the environment variable with this command:
         
         export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value core/project)
         

  5. Enable the GKE API:
         
         gcloud services enable container.googleapis.com
         

  6. Enable the Policy Controller API:
         
         gcloud services enable anthospolicycontroller.googleapis.com
         

  7. Create a directory to store the files created for this tutorial:
         
         mkdir -p ~/cnrm-gatekeeper-tutorial
         

  8. Go to the directory that you created:
         
         cd ~/cnrm-gatekeeper-tutorial
         




## Create a GKE cluster

  1. In Cloud Shell, create a GKE cluster with [the Config Connector add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall) and [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity):
         
         gcloud container clusters create CLUSTER_NAME \
           --addons ConfigConnector \
           --enable-ip-alias \
           --num-nodes 4 \
           --release-channel regular \
           --scopes cloud-platform \
           --workload-pool $GOOGLE_CLOUD_PROJECT.svc.id.goog \
           --zone ZONE
         

Replace the following:

     * `CLUSTER_NAME`: The name of the cluster that you want to use for this project, for example, `cnrm-gatekeeper-tutorial`.
     * `ZONE`: A [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones) close to your location, for example, `asia-southeast1-b`.

The Config Connector add-on installs [custom resource definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) for [Google Cloud resources](https://docs.cloud.google.com/config-connector/docs/concepts/resources) in your GKE cluster.

  2. Optional: If you use a [private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters) in your own environment, add a firewall rule that allows the GKE cluster control plane to connect to the Policy Controller webhook:
         
         gcloud compute firewall-rules create allow-cluster-control-plane-tcp-8443 \
           --allow tcp:8443 \
           --network default \
           --source-ranges CONTROL_PLANE_CIDR \
           --target-tags NODE_TAG
         

Replace the following:

     * `CONTROL_PLANE_CIDR`: The IP range for your GKE cluster control plane, for example, `172.16.0.16/28`.
     * `NODE_TAG`: A tag applied to all the nodes in your GKE cluster.

This optional firewall rule is required for the Policy Controller webhook to work when your cluster uses private nodes.




## Set up Config Connector

The Google Cloud Project where you install Config Connector is known as the _host project_. The projects where you use Config Connector to manage resources are known as _managed projects_. In this tutorial, you use Config Connector to create Google Cloud resources in the same project as your GKE cluster, so that the host project and the managed project are the same project.

  1. In Cloud Shell, create a [Google service account](https://docs.cloud.google.com/iam/docs/service-accounts) for Config Connector:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
           --display-name "Config Connector Gatekeeper tutorial"
         

Replace `SERVICE_ACCOUNT_NAME` with the name that you want to use for this service account, for example, `cnrm-gatekeeper-tutorial`. Config Connector uses this Google service account to create resources in your managed project.

  2. Grant the [Storage Admin role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) to the Google service account:
         
         gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
           --member "serviceAccount:SERVICE_ACCOUNT_NAME@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com" \
           --role roles/storage.admin
         

In this tutorial, you use the Storage Admin role because you use Config Connector to create Cloud Storage buckets. In your own environment, grant the roles that are required in order to manage the Google Cloud resources that you want to create for Config Connector. For more information about predefined roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) in the IAM documentation.

  3. Create a Kubernetes namespace for the Config Connector resources that you create in this tutorial:
         
         kubectl create namespace NAMESPACE
         

Replace NAMESPACE with the Kubernetes namespace that you want to use in the tutorial, for example, `tutorial`.

  4. Annotate the namespace to specify which project Config Connector should use to create Google Cloud resources (the managed project):
         
         kubectl annotate namespace NAMESPACE \
             cnrm.cloud.google.com/project-id=$GOOGLE_CLOUD_PROJECT
         

  5. Create a `ConfigConnectorContext` resource that enables Config Connector for the Kubernetes namespace and associates it with the Google service account you created:
         
         cat << EOF | kubectl apply -f -
         apiVersion: core.cnrm.cloud.google.com/v1beta1
         kind: ConfigConnectorContext
         metadata:
           name: configconnectorcontext.core.cnrm.cloud.google.com
           namespace: NAMESPACE
         spec:
           googleServiceAccount: SERVICE_ACCOUNT_NAME@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com
         EOF
         

When you create the `ConfigConnectorContext` resource, Config Connector creates a [Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) and [StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) in the `cnrm-system` namespace to manage the Config Connector resources in your namespace.

  6. Wait for the Config Connector controller Pod for your namespace:
         
         kubectl wait --namespace cnrm-system --for=condition=Ready pod \
           -l cnrm.cloud.google.com/component=cnrm-controller-manager,cnrm.cloud.google.com/scoped-namespace=NAMESPACE
         

When the Pod is ready, the Cloud Shell prompt appears. If you get the message `error: no matching resources found`, wait a minute and try again.

  7. Bind your Config Connector Kubernetes service account to your Google service account by creating an IAM policy binding:
         
         gcloud iam service-accounts add-iam-policy-binding \
           SERVICE_ACCOUNT_NAME@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com \
           --member "serviceAccount:$GOOGLE_CLOUD_PROJECT.svc.id.goog[cnrm-system/cnrm-controller-manager-NAMESPACE]" \
           --role roles/iam.workloadIdentityUser
         

This binding allows the `cnrm-controller-manager-NAMESPACE` Kubernetes service account in the `cnrm-system` namespace to act as the Google service account that you created.




## Install Policy Controller

Install Policy Controller by following the [installation instructions](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller#installing).

Use an audit interval of `60` seconds.

## Create a Google Cloud resource using Config Connector

  1. In Cloud Shell, create a Config Connector manifest that represents a Cloud Storage bucket in the `us-central1` region:
         
         cat << EOF > tutorial-storagebucket-us-central1.yaml
         apiVersion: storage.cnrm.cloud.google.com/v1beta1
         kind: StorageBucket
         metadata:
           name: tutorial-us-central1-$GOOGLE_CLOUD_PROJECT
           namespace: NAMESPACE
         spec:
           location: us-central1
           uniformBucketLevelAccess: true
         EOF
         

  2. To create the Cloud Storage bucket, apply the manifest:
         
         kubectl apply -f tutorial-storagebucket-us-central1.yaml
         

  3. Verify that Config Connector created the Cloud Storage bucket:
         
         gcloud storage ls | grep tutorial
         

The output is similar to the following:
         
         gs://tutorial-us-central1-PROJECT_ID/
         

This output includes `PROJECT_ID`, which is your Google Cloud project ID.

If you don't see this output, wait a minute and perform the step again.




## Create a policy

A policy in Policy Controller consists of a [constraint template](https://github.com/open-policy-agent/frameworks/tree/master/constraint#what-is-a-constraint-template) and a [constraint](https://github.com/open-policy-agent/frameworks/tree/master/constraint#what-is-a-constraint). The constraint template contains the policy logic. The constraint specifies where the policy applies and the input parameters to the policy logic.

  1. In Cloud Shell, create a constraint template that restricts Cloud Storage bucket locations:
         
         cat << EOF > tutorial-storagebucket-location-template.yaml
         apiVersion: templates.gatekeeper.sh/v1beta1
         kind: ConstraintTemplate
         metadata:
           name: gcpstoragelocationconstraintv1
         spec:
           crd:
             spec:
               names:
                 kind: GCPStorageLocationConstraintV1
               validation:
                 openAPIV3Schema:
                   properties:
                     locations:
                       type: array
                       items:
                         type: string
                     exemptions:
                       type: array
                       items:
                         type: string
           targets:
           - target: admission.k8s.gatekeeper.sh
             rego: |
               package gcpstoragelocationconstraintv1
         
               allowedLocation(reviewLocation) {
                   locations := input.parameters.locations
                   satisfied := [ good | location = locations[_]
                                         good = lower(location) == lower(reviewLocation)]
                   any(satisfied)
               }
         
               exempt(reviewName) {
                   input.parameters.exemptions[_] == reviewName
               }
         
               violation[{"msg": msg}] {
                   bucketName := input.review.object.metadata.name
                   bucketLocation := input.review.object.spec.location
                   not allowedLocation(bucketLocation)
                   not exempt(bucketName)
                   msg := sprintf("Cloud Storage bucket <%v> uses a disallowed location <%v>, allowed locations are %v", [bucketName, bucketLocation, input.parameters.locations])
               }
         
               violation[{"msg": msg}] {
                   not input.parameters.locations
                   bucketName := input.review.object.metadata.name
                   msg := sprintf("No permitted locations provided in constraint for Cloud Storage bucket <%v>", [bucketName])
               }
         EOF
         

  2. Apply the template to create the Cloud Storage bucket:
         
         kubectl apply -f tutorial-storagebucket-location-template.yaml
         

  3. Create a constraint that only allows buckets in the Singapore and Jakarta regions (`asia-southeast1` and `asia-southeast2`). The constraint applies to the namespace that you created earlier. It exempts the default Cloud Storage bucket for [Cloud Build](https://docs.cloud.google.com/build/docs).
         
         cat << EOF > tutorial-storagebucket-location-constraint.yaml
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: GCPStorageLocationConstraintV1
         metadata:
           name: singapore-and-jakarta-only
         spec:
           enforcementAction: deny
           match:
             kinds:
             - apiGroups:
               - storage.cnrm.cloud.google.com
               kinds:
               - StorageBucket
             namespaces:
             - NAMESPACE
           parameters:
             locations:
             - asia-southeast1
             - asia-southeast2
             exemptions:
             - ${GOOGLE_CLOUD_PROJECT}_cloudbuild
         EOF
         

  4. To limit the zones in which buckets can exist, apply the constraint:
         
         kubectl apply -f tutorial-storagebucket-location-constraint.yaml
         




## Verify the policy

  1. Create a manifest that represents a Cloud Storage bucket in a location that isn't allowed (`us-west1`):
         
         cat << EOF > tutorial-storagebucket-us-west1.yaml
         apiVersion: storage.cnrm.cloud.google.com/v1beta1
         kind: StorageBucket
         metadata:
           name: tutorial-us-west1-$GOOGLE_CLOUD_PROJECT
           namespace: NAMESPACE
         spec:
           location: us-west1
           uniformBucketLevelAccess: true
         EOF
         

  2. To create the Cloud Storage bucket, apply the manifest:
         
         kubectl apply -f tutorial-storagebucket-us-west1.yaml
         

The output is similar to the following:
         
         Error from server ([singapore-and-jakarta-only] Cloud Storage bucket
         <tutorial-us-west1-PROJECT_ID> uses a disallowed location
         <us-west1>, allowed locations are ["asia-southeast1",
         "asia-southeast2"]): error when creating
         "tutorial-storagebucket-us-west1.yaml": admission webhook
         "validation.gatekeeper.sh" denied the request: [singapore-and-jakarta-only]
         Cloud Storage bucket <tutorial-us-west1-PROJECT_ID> uses a
         disallowed location <us-west1>, allowed locations are
         ["asia-southeast1", "asia-southeast2"]
         

  3. Optional: You can view a record of the decision to deny the request in Cloud Audit Logs. Query the Admin Activity logs for your project:
         
         gcloud logging read --limit=1 \
             "logName=\"projects/$GOOGLE_CLOUD_PROJECT/logs/cloudaudit.googleapis.com%2Factivity\""'
             resource.type="k8s_cluster"
             resource.labels.cluster_name="CLUSTER_NAME"
             resource.labels.location="ZONE"
             protoPayload.authenticationInfo.principalEmail!~"system:serviceaccount:cnrm-system:.*"
             protoPayload.methodName:"com.google.cloud.cnrm."
             protoPayload.status.code=7'
         

The output is similar to the following:
         
         insertId: 3c6940bb-de14-4d18-ac4d-9a6becc70828
         labels:
           authorization.k8s.io/decision: allow
           authorization.k8s.io/reason: ''
           mutation.webhook.admission.k8s.io/round_0_index_0: '{"configuration":"mutating-webhook.cnrm.cloud.google.com","webhook":"container-annotation-handler.cnrm.cloud.google.com","mutated":true}'
           mutation.webhook.admission.k8s.io/round_0_index_1: '{"configuration":"mutating-webhook.cnrm.cloud.google.com","webhook":"management-conflict-annotation-defaulter.cnrm.cloud.google.com","mutated":true}'
         logName: projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity
         operation:
           first: true
           id: 3c6940bb-de14-4d18-ac4d-9a6becc70828
           last: true
           producer: k8s.io
         protoPayload:
           '@type': type.googleapis.com/google.cloud.audit.AuditLog
           authenticationInfo:
             principalEmail: user@example.com
           authorizationInfo:
           - permission: com.google.cloud.cnrm.storage.v1beta1.storagebuckets.create
             resource: storage.cnrm.cloud.google.com/v1beta1/namespaces/NAMESPACE/storagebuckets/tutorial-us-west1-PROJECT_ID
           methodName: com.google.cloud.cnrm.storage.v1beta1.storagebuckets.create
           requestMetadata:
             callerIp: 203.0.113.1
             callerSuppliedUserAgent: kubectl/v1.21.1 (linux/amd64) kubernetes/5e58841
           resourceName: storage.cnrm.cloud.google.com/v1beta1/namespaces/NAMESPACE/storagebuckets/tutorial-us-west1-PROJECT_ID
           serviceName: k8s.io
           status:
             code: 7
             message: Forbidden
         receiveTimestamp: '2021-05-21T06:56:24.940264678Z'
         resource:
           labels:
             cluster_name: CLUSTER_NAME
             location: CLUSTER_ZONE
             project_id: PROJECT_ID
           type: k8s_cluster
         timestamp: '2021-05-21T06:56:09.060635Z'

The `methodName` field shows the attempted operation, the `resourceName` shows the full name of the Config Connector resource, and the `status` section shows that the request was unsuccessful, with [error code](https://docs.cloud.google.com/apis/design/errors) `7` and message `Forbidden`.

  4. Create a manifest that represents a Cloud Storage bucket in a permitted location (`asia-southeast1`):
         
         cat << EOF > tutorial-storagebucket-asia-southeast1.yaml
         apiVersion: storage.cnrm.cloud.google.com/v1beta1
         kind: StorageBucket
         metadata:
           name: tutorial-asia-southeast1-$GOOGLE_CLOUD_PROJECT
           namespace: NAMESPACE
         spec:
           location: asia-southeast1
           uniformBucketLevelAccess: true
         EOF
         

  5. To create the Cloud Storage bucket, apply the manifest:
         
         kubectl apply -f tutorial-storagebucket-asia-southeast1.yaml
         

The output is similar to the following:
         
         storagebucket.storage.cnrm.cloud.google.com/tutorial-asia-southeast1-PROJECT_ID created
         

This output includes `PROJECT_ID`, which is your Google Cloud project ID.

  6. Check that Config Connector created the Cloud Storage bucket:
         
         gcloud storage ls | grep tutorial
         

The output is similar to the following:
         
         gs://tutorial-asia-southeast1-PROJECT_ID/
         gs://tutorial-us-central1-PROJECT_ID/
         

If you don't see this output, wait a minute and perform this step again.




## Audit constraints

The audit controller in Policy Controller periodically evaluates resources against their constraints. The controller detects policy violations for resources created before the constraint, and for resources created outside Config Connector.

  1. In Cloud Shell, view violations for all constraints that use the `GCPStorageLocationConstraintV1` constraint template:
         
         kubectl get gcpstoragelocationconstraintv1 -o json \
           | jq '.items[].status.violations'
         

The output is similar to the following:
         
         [
           {
             "enforcementAction": "deny",
             "kind": "StorageBucket",
             "message": "Cloud Storage bucket <tutorial-us-central1-PROJECT_ID>
             uses a disallowed location <us-central1>, allowed locations are
             \"asia-southeast1\", \"asia-southeast2\"",
             "name": "tutorial-us-central1-PROJECT_ID",
             "namespace": "NAMESPACE"
           }
         ]
         

You see the Cloud Storage bucket that you created in `us-central1` before you created the constraint.

**Note:** The default `status.violations` attribute shows up to 20 violations per constraint. If the audit controller finds more than 20 constraint violations, the remainder don't display. If you run into this limitation in your own environment, create multiple constraints. Scope each constraint to a different namespace.



## Validate resources during development

During development and continuous integration builds, it's helpful to validate resources against constraints before you apply those resources to your GKE cluster. Validating provides fast feedback and lets you discover issues with resources and constraints early. These steps show you how to validate resources with [kpt](https://kpt.dev). The kpt command-line tool lets you manage and apply Kubernetes resource manifests.

  1. In Cloud Shell, run the `gatekeeper` [KRM function](https://kpt.dev/book/02-concepts/03-functions) using kpt:
         
         kpt fn eval . --image=gcr.io/kpt-fn/gatekeeper:v0.2 --truncate-output=false
         

A KRM function is a program that can mutate or validate Kubernetes resources stored on the local file system as YAML files. The `gatekeeper` KRM function validates the Config Connector Cloud Storage bucket resources against the Gatekeeper policy. The `gatekeeper` KRM function is packaged as a container image that is available in Artifact Registry.

The function reports that the manifest files for Cloud Storage buckets in the `us-central1` and `us-west1` regions violate the constraint.

The output is similar to the following:
         
         [RUNNING] "gcr.io/kpt-fn/gatekeeper:v0.2"
         [FAIL] "gcr.io/kpt-fn/gatekeeper:v0.2"
           Results:
             [ERROR] Cloud Storage bucket <tutorial-us-central1-PROJECT_ID> uses a disallowed location <us-central1>, allowed locations are ["asia-southeast1", "asia-southeast2"] violatedConstraint: singapore-and-jakarta-only in object "storage.cnrm.cloud.google.com/v1beta1/StorageBucket/tutorial/tutorial-us-central1-GOOGLE_CLOUD_PROJECT" in file "tutorial-storagebucket-us-central1.yaml"
             [ERROR] Cloud Storage bucket <tutorial-us-west1-PROJECT_ID> uses a disallowed location <us-west1>, allowed locations are ["asia-southeast1", "asia-southeast2"] violatedConstraint: singapore-and-jakarta-only in object "storage.cnrm.cloud.google.com/v1beta1/StorageBucket/tutorial/tutorial-us-west1-GOOGLE_CLOUD_PROJECT" in file "tutorial-storagebucket-us-west1.yaml"
           Stderr:
             "[error] storage.cnrm.cloud.google.com/v1beta1/StorageBucket/test/tutorial-us-central1-PROJECT_ID : Cloud Storage bucket <tutorial-us-central1-PROJECT_ID> uses a disallowed location <us-central1>, allowed locations are [\"asia-southeast1\", \"asia-southeast2\"]"
             "violatedConstraint: singapore-and-jakarta-only"
             ""
             "[error] storage.cnrm.cloud.google.com/v1beta1/StorageBucket/test/tutorial-us-west1-PROJECT_IDT : Cloud Storage bucket <tutorial-us-west1-PROJECT_IDgt; uses a disallowed location <us-west1>, allowed locations are [\"asia-southeast1\", \"asia-southeast2\"]"
             "violatedConstraint: singapore-and-jakarta-only"
             ""
           Exit code: 1
         




## Validate resources created outside Config Connector

You can validate Google Cloud resources that were created outside Config Connector by exporting the resources. After you export the resources, use either of the following options to evaluate your Policy Controller policies against the exported resources:

  * Validate the resources using the `gatekeeper` KRM function.

  * Import the resources into Config Connector.




To export the resources, [you use Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/exporting-to-cloud-storage).

  1. In Cloud Shell, enable the Cloud Asset API:
         
         gcloud services enable cloudasset.googleapis.com
         

  2. Delete the Kubernetes resource manifest files for the Cloud Storage buckets in `us-central1` and `us-west1`:
         
         rm tutorial-storagebucket-us-*.yaml
         

  3. Export all Cloud Storage resources in your current project, and store the output in a file called `export.yaml`:
         
         gcloud beta resource-config bulk-export \
           --project $GOOGLE_CLOUD_PROJECT \
           --resource-format krm \
           --resource-types StorageBucket > export.yaml
         

The output is similar to the following:
         
         Exporting resource configurations to stdout...
         
         Export complete.
         

  4. Create a [kpt pipeline](https://kpt.dev/book/02-concepts/03-functions) by chaining together KRM functions. This pipeline validates the resources in the current directory against the Cloud Storage bucket location policy:
         
         kpt fn source . \
           | kpt fn eval - --image=gcr.io/kpt-fn/set-namespace:v0.1 -- namespace=NAMESPACE \
           | kpt fn eval - --image=gcr.io/kpt-fn/gatekeeper:v0.2 --truncate-output=false
         

The exported resources do not have a value for the `namespace` metadata attribute. This pipeline uses a KRM function called `set-namespace` to set the `namespace` value of all the resources.

The output is similar to the following and it shows violations for the resources that you exported:
         
         [RUNNING] "gcr.io/kpt-fn/set-namespace:v0.1"
         [PASS] "gcr.io/kpt-fn/set-namespace:v0.1"
         [RUNNING] "gcr.io/kpt-fn/gatekeeper:v0.2"
         [FAIL] "gcr.io/kpt-fn/gatekeeper:v0.2"
           Results:
             [ERROR] Cloud Storage bucket <tutorial-us-central1-PROJECT_ID> uses a disallowed location <us-central1>, allowed locations are ["asia-southeast1", "asia-southeast2"] violatedConstraint: singapore-and-jakarta-only in object "storage.cnrm.cloud.google.com/v1beta1/StorageBucket/tutorial/tutorial-us-central1-GOOGLE_CLOUD_PROJECT" in file "export.yaml"
           Stderr:
             "[error] storage.cnrm.cloud.google.com/v1beta1/StorageBucket/test/tutorial-us-central1-PROJECT_ID : Cloud Storage bucket <tutorial-us-central1-PROJECT_ID> uses a disallowed location <us-central1>, allowed locations are [\"asia-southeast1\", \"asia-southeast2\"]"
             "violatedConstraint: singapore-and-jakarta-only"
             ""
           Exit code: 1
         

If your Google Cloud project contains Cloud Storage buckets that you created before working on this tutorial, and their location violates the constraint, the previously created buckets appear in the output.




Congratulations, you have successfully set up a policy that governs the permitted location of Cloud Storage buckets. The tutorial is complete. You can now continue to add your own policies for other Google Cloud resources.

## Troubleshooting

If Config Connector doesn't create the expected Google Cloud resources, use the following command in Cloud Shell to view the logs of the Config Connector controller manager:
    
    
    kubectl logs --namespace cnrm-system --container manager \
      --selector cnrm.cloud.google.com/component=cnrm-controller-manager,cnrm.cloud.google.com/scoped-namespace=NAMESPACE
    

If Policy Controller doesn't enforce policies correctly, use the following command to view the logs of the controller manager:
    
    
    kubectl logs deployment/gatekeeper-controller-manager \
      --namespace gatekeeper-system
    

If Policy Controller doesn't report violations in the `status` field of the constraint objects, view the logs of the audit controller using this command:
    
    
    kubectl logs deployment/gatekeeper-audit --namespace gatekeeper-system
    

If you run into other problems with this tutorial, we recommend that you review these documents:

  * [Config Connector troubleshooting](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#troubleshooting)
  * [Config Connector resource reference](https://docs.cloud.google.com/config-connector/docs/reference/overview)
  * [Troubleshooting Kubernetes clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. If the project that you plan to delete is attached to an organization, expand the **Organization** list in the **Name** column. 
  3. In the project list, select the project that you want to delete, and then click **Delete**. 
  4. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the resources

If you want to keep the Google Cloud project you used in this tutorial, delete the individual resources.

  1. In Cloud Shell, delete the Cloud Storage bucket location constraint:
         
         kubectl delete -f tutorial-storagebucket-location-constraint.yaml
         

  2. Add the [`cnrm.cloud.google.com/force-destroy` annotation](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/storage/storagebucket#annotations) with a string value of `true` to all `storagebucket` resources in the namespace managed by Config Connector:
         
         kubectl annotate storagebucket --all --namespace NAMESPACE \
           cnrm.cloud.google.com/force-destroy=true
         

This annotation is a [directive](https://docs.cloud.google.com/config-connector/docs/concepts/resources#object_metadata) that allows Config Connector to delete a Cloud Storage bucket when you delete the corresponding `storagebucket` resource in the GKE cluster, [even if the bucket contains objects](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/storage/storagebucket).

  3. Delete the Config Connector resources that represent the Cloud Storage buckets:
         
         kubectl delete --namespace NAMESPACE storagebucket --all
         

  4. Delete the GKE cluster:
         
         gcloud container clusters delete CLUSTER_NAME \
           --zone ZONE --async --quiet
         

  5. Delete the Workload Identity policy binding in IAM:
         
         gcloud iam service-accounts remove-iam-policy-binding \
           SERVICE_ACCOUNT_NAME@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com \
           --member "serviceAccount:$GOOGLE_CLOUD_PROJECT.svc.id.goog[cnrm-system/cnrm-controller-manager-NAMESPACE]" \
           --role roles/iam.workloadIdentityUser
         

  6. Delete the Cloud Storage Admin role binding for the Google service account:
         
         gcloud projects remove-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
           --member "serviceAccount:SERVICE_ACCOUNT_NAME@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com" \
           --role roles/storage.admin
         

  7. Delete the Google service account that you created for Config Connector:
         
         gcloud iam service-accounts delete --quiet \
           SERVICE_ACCOUNT_NAME@$GOOGLE_CLOUD_PROJECT.iam.gserviceaccount.com
         




## What's next

  * Discover how to [run Policy Controller validation as part of a continuous integration pipeline in Cloud Build](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/tutorials/app-policy-validation-ci-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
