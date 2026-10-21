---
url: https://docs.cloud.google.com/binary-authorization/docs/configure-policy-gke/
title: Quickstart: Configure a Binary Authorization policy with GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:25:50.375755+00:00
---

# Quickstart: Configure a Binary Authorization policy with GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/configure-policy-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure a Binary Authorization policy with GKE

This quickstart shows how to configure and test a basic [rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules) in a Binary Authorization [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies).

In this quickstart, you view and configure the default rule in the policy. The default rule allows all images to be deployed. You test this by deploying a container image on a Google Kubernetes Engine (GKE) cluster. You then set the default rule to disallow all images from being deployed and attempt to deploy an image.

**Note:** This is not a real-world policy. A typical policy requires an [attestation](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations) to accompany the image before the Binary Authorization enforcer allows the image to be deployed. For an end-to-end tutorial about attestations, see [Getting started using the CLI](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli) or [Getting started using the Console](https://docs.cloud.google.com/binary-authorization/docs/getting-started-console).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Artifact Registry, Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/configure-policy-gke)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Artifact Registry, Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/configure-policy-gke)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  16. Install [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl).



### Required roles

To get the permissions that you need to configure a Binary Authorization policy with GKE, ask your administrator to grant you the following IAM roles on your project: 

  * [Binary Authorization Policy Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/binaryauthorization#binaryauthorization.policyEditor) (`roles/binaryauthorization.policyEditor`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)
  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a cluster with Binary Authorization enforcement enabled

Now, you create a GKE cluster with Binary Authorization enabled. This is the cluster where you want your deployed container images to run.

Binary Authorization works with Autopilot or Standard clusters.

###  Google Cloud console 

The following steps configure an Autopilot cluster.

  1. In the Google Cloud console, go to the GKE **Kubernetes clusters** page:

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create**.

  3. In **Create an Autopilot cluster** , do the following:

     1. In the **Name** field, enter `test-cluster`.

     2. In the **Region** menu, select `us-central1`.

     3. Expand the **Advanced settings** section.

     4. Click the **Security** link to reveal the **Security** panel.

     5. In the **Security** panel, select the **Enable Binary Authorization** checkbox.

     6. Select **Enforce-only**.

     7. Click **Next** and then click **Next:Review and Create**.

     8. To begin creating the cluster, click **Create**.




###  gcloud 

Run `gcloud container clusters create` with the `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` flag enabled.
    
    
    gcloud container clusters create \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --zone us-central1-a \
        test-cluster
    

Creating a cluster can take several minutes.

## Default policy

By default, your Binary Authorization policy is configured to allow all container images to be deployed.

###  Google Cloud console 

To view the default policy, do the following:

  1. Go to the **Binary Authorization** page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

The console displays details about the policy.

  2. Click **Edit Policy**.

  3. In **Project Default Rule** , the option **Allow All Images** is selected.




###  gcloud 

To view the default policy, export the policy YAML file as follows:
    
    
    gcloud container binauthz policy export
    

By default, the file has the following contents:
    
    
    globalPolicyEvaluationMode: ENABLE
    defaultAdmissionRule:
      evaluationMode: ALWAYS_ALLOW
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
    name: projects/PROJECT_ID/policy
    

**Note:** `globalPolicyEvaluationMode: ENABLE` means that Google-managed system images are exempted. For details, see [`globalPolicyEvaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images).

###  REST API 

To view the default policy, retrieve it in JSON format as follows:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "x-goog-user-project: ${PROJECT_ID}" \
        "https://binaryauthorization.googleapis.com/v1/projects/${PROJECT_ID}/policy"
    

The command produces the following output:
    
    
    {
      "name": "projects/PROJECT_ID/policy",
      "globalPolicyEvaluationMode": "ENABLE",
      "defaultAdmissionRule": {
        "evaluationMode": "ALWAYS_ALLOW",
        "enforcementMode": "ENFORCED_BLOCK_AND_AUDIT_LOG"
      }
    }
    

**Note:** `globalPolicyEvaluationMode: ENABLE` means that Google-managed system images are exempted. For details, see [`globalPolicyEvaluationMode`](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images).

## Test the enforcement policy

You can test the enforcement policy by trying to deploy a sample container image to the cluster.

For this quickstart, you use the sample container image located at the path `us-docker.pkg.dev/google-samples/containers/gke/hello-app` in Artifact Registry. This is a public container image created by Google that contains a "Hello, World!" sample application.

###  Google Cloud console 

To test the policy, do the following:

  1. Go to the GKE **Clusters** page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Deploy**.

The console prompts you to enter details about the deployment.

  3. Enter `hello-server` in the **Deployment name** field.

  4. Click **Next: Container details**.

  5. Select **Existing Container Image**.

  6. Enter `us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0` as the container image path.

  7. Click **Deploy**.




###  kubectl 

To test the policy, do the following:

  1. Update the local `kubeconfig` file:
         
         gcloud container clusters get-credentials \
             --zone us-central1-a \
             test-cluster
         

This provides the credentials and endpoint information required to access the cluster in GKE.

  2. Deploy the image:
         
         kubectl run hello-server --image us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080
         




Now, verify that the deployment was allowed by Binary Authorization.

###  Google Cloud console 

To verify that the image was deployed, go to the GKE **Workloads** page in Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/workload?workload_list_tablesize=50)

A workload for the deployment appears with a green icon that indicates that the image was deployed successfully.

###  kubectl 

To verify that the image was deployed, do the following:
    
    
    kubectl get pods
    

The command prints a message similar to the following, which indicates that deployment was successful:
    
    
    NAME                            READY     STATUS    RESTARTS   AGE
    hello-server-579859fb5b-h2k8s   1/1       Running   0          1m
    

Make sure to delete the deployment so you can continue to the next step:

###  Google Cloud console 

To delete the deployment, do the following:

  1. Return to the GKE **Workloads** page in Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/workload?workload_list_tablesize=50)

  2. Select the `hello-server` workload.

  3. Click **Delete**.




###  kubectl 

To delete the deployment, do the following:
    
    
    kubectl delete deployment hello-server
    

## Configure the enforcement policy to disallow all images

Now, modify the policy to block instead of allow all images to be deployed.

###  Google Cloud console 

To modify the policy, do the following:

  1. Return to the **Binary Authorization** page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/policy)

  2. Click **Edit Policy**.

  3. Select **Disallow All Images**.

  4. Click **Save Policy**.




###  gcloud 

To modify the policy, do the following:

  1. Export the policy YAML file:
         
         gcloud container binauthz policy export  > /tmp/policy.yaml
         

  2. In a text editor, change the `evaluationMode` from `ALWAYS_ALLOW` to `ALWAYS_DENY`.

The policy YAML file should appear as follows:
         
         globalPolicyEvaluationMode: ENABLE
         defaultAdmissionRule:
           evaluationMode: ALWAYS_DENY
           enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
         name: projects/PROJECT_ID/policy
         

  3. Import the policy YAML file back into Binary Authorization:
         
         gcloud container binauthz policy import /tmp/policy.yaml
         




###  REST API 

To modify the policy, do the following:

  1. Create a text file with the updated policy in JSON format:
         
         cat > /tmp/policy.json << EOM
         {
           "name": "projects/${PROJECT_ID}/policy",
           "globalPolicyEvaluationMode": "ENABLE",
           "defaultAdmissionRule": {
             "evaluationMode": "ALWAYS_DENY",
             "enforcementMode": "ENFORCED_BLOCK_AND_AUDIT_LOG"
           }
         }
         EOM
         

  2. Send the updated policy to the REST API:
         
         curl -X PUT \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "x-goog-user-project: ${PROJECT_ID}" \
             --data-binary @/tmp/policy.json  \
             "https://binaryauthorization.googleapis.com/v1/projects/${PROJECT_ID}/policy"
         




## Retest the policy

Again, test the policy by deploying a sample container image to the cluster. This time, Binary Authorization blocks the image from being deployed.

###  Google Cloud console 

Deploy the image:

  1. Go to the GKE **Clusters** page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Click **Deploy**.

The console prompts you to enter details about the deployment.

  3. Enter `hello-server` in the **Deployment name** field.

  4. Click **Next: Container details**.

  5. Select **Existing Container Image**.

  6. Enter `us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0` as the container image path.

  7. Click **Deploy**.




###  kubectl 

Deploy the image:
    
    
    kubectl run hello-server --image us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080
    

You can now verify that the policy was blocked:

###  Google Cloud console 

To verify that the image was not deployed, do the following:

Return to the GKE **Workloads** page in Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/workload?workload_list_tablesize=50)

The workload for the container image appears with a red icon that indicates that the image failed to be deployed.

###  kubectl 

To verify that the image was not deployed, execute the following command:
    
    
    kubectl get pods
    

The command prints the following message, which indicates that the image was not deployed:
    
    
    No resources found.
    

You can get further details about the deployment:
    
    
    kubectl get event --template \
    '{{range.items}}{{"\033[0;36m"}}{{.reason}}:{{"\033[0m"}}{{.message}}{{"\n"}}{{end}}'
    

You see a response that resembles the following:
    
    
    FailedCreate: Error creating: pods POD_NAME is forbidden: admission webhook "imagepolicywebhook.image-policy.k8s.io" denied the request: Image IMAGE_NAME denied by Binary Authorization default admission rule. Denied by always_deny admission rule
    

In this output:

  * POD_NAME: the name of the Pod.
  * IMAGE_NAME: the name of the image.
  * ATTESTOR_NAME: the name of the attestor.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Delete the cluster you created in GKE:

###  Console 

To delete the cluster, do the following:

  1. Go to the GKE **Clusters** page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Select the `test-cluster` cluster and click **Delete**.




###  gcloud 

To delete the cluster, do the following:
    
    
    gcloud container clusters delete \
        --zone=us-central1-a \
        test-cluster
    

## What's next

  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build) ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * For an end-to-end tutorial about requiring attestations, see: 
    * [Getting started using the CLI](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli)
    * [Getting started using Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/getting-started-console)
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore the [DevOps Research and Assessment (DORA)](https://dora.dev/) research program.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
