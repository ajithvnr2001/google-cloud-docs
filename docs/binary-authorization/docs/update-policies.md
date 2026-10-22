---
url: https://docs.cloud.google.com/binary-authorization/docs/update-policies/
title: Quickstart: Update a Binary Authorization policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:34.026984+00:00
---

# Quickstart: Update a Binary Authorization policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/update-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update a Binary Authorization policy

**Note:** This document or section includes references to one or more terms that Google considers disrespectful or offensive. The terms are used because they are keywords in the software that's described in the document. 

The terms: `whitelist`

This document describes how to [exempt images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images) in [Binary Authorization policies](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies).

In this document, you update the policy to exempt container images in Artifact Registry from Binary Authorization enforcement and set the default rule to disallow all other containers from being deployed.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry, Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/update-policies)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Artifact Registry, Binary Authorization APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com,binaryauthorization.googleapis.com&redirect=https%3A//cloud.google.com/binary-authorization/docs/update-policies)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. If you are not using [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell), install [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl).



## Create a cluster with Binary Authorization enabled

Create a GKE cluster with Binary Authorization enabled. This is the cluster where you want your deployed container images to run.

###  Google Cloud console 

  1. Go to the GKE **Clusters** page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

The console displays a list of GKE clusters in your Google Cloud project.

  2. Click **Create Cluster**.

  3. Enter `test-cluster` in the **Name** field.

![Name field in the standard cluster template](https://docs.cloud.google.com/static/binary-authorization/docs/images/cluster-enable.png)

  4. Select **Zonal** in the **Location Type** options.

  5. Select `us-central1-a` from the **Zone** drop-down list.

  6. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  7. In the **Binary authorization** row, click _edit_ **Edit configuration**.

  8. Select **Enable Binary Authorization**.

![Enable Binary Authorization option](https://docs.cloud.google.com/static/binary-authorization/docs/images/cluster-enable-binary-authorization.png)

  9. Select **Enforce-only** , and then click **Save**.

  10. Click **Create**.


**Note:** Creating a cluster can take several minutes.

###  gcloud 

Run `gcloud container clusters create` with the `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` flag enabled.
    
    
    gcloud container clusters create \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --zone us-central1-a \
        test-cluster
    

## View the Default policy

By default, your Binary Authorization policy is configured to allow all container images to be deployed.

###  Google Cloud console 

To view the default policy, do the following:

  1. Go to the **Binary Authorization** page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

The console displays details about the policy.

  2. Click **Edit Policy**.

  3. In **Project Default Rule** , the option **Allow All Images** is selected.




###  gcloud 

To view the default policy, export the policy YAML file, do the following:
    
    
    gcloud container binauthz policy export
    

By default, the file has the following contents:
    
    
    globalPolicyEvaluationMode: ENABLE
    defaultAdmissionRule:
      evaluationMode: ALWAYS_ALLOW
      enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
    name: projects/<var>PROJECT_ID</var>/policy
    

###  REST API 

To view the default policy, retrieve it in JSON format as follows:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "x-goog-user-project: ${PROJECT_ID}" \
        "https://binaryauthorization.googleapis.com/v1/projects/${PROJECT_ID}/policy"
    

The REST API returns the following:
    
    
    {
      "name": "projects/PROJECT_ID/policy",
      "globalPolicyEvaluationMode": "ENABLE",
      "defaultAdmissionRule": {
        "evaluationMode": "ALWAYS_ALLOW",
        "enforcementMode": "ENFORCED_BLOCK_AND_AUDIT_LOG"
      }
    }
    

## Allow only exempt images

This section describes how to modify the policy to exempt images and disallow all other images from being deployed.

###  Google Cloud console 

To modify the policy, do the following:

  1. Return to the **Binary Authorization** page in the Google Cloud console.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/policy)

  2. Click **Edit Policy**.

  3. Select **Disallow All Images**.

  4. Under **Images exempt from deployment rules** , expand **Image paths**.

  5. Click **Add Image Paths**.

###  Artifact Registry 

In **New image path** , paste the following path from an Artifact Registry repository:
         
         us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         

  6. Click **Done** to save the image path.

  7. Click **Save Policy**.




###  gcloud 

To modify the policy to allow example images from Artifact Registry, do the following:

  1. Export the policy YAML file:
         
         gcloud container binauthz policy export  > /tmp/policy.yaml
         

  2. In a text editor, change the `evaluationMode` from `ALWAYS_ALLOW` to `ALWAYS_DENY` and add exempt images to `admissionWhitelistPatterns`.

To exempt the following example images from Artifact Registry, modify your policy YAML file as follows:
         
         admissionWhitelistPatterns:
         - namePattern: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         globalPolicyEvaluationMode: ENABLE
         defaultAdmissionRule:
           evaluationMode: ALWAYS_DENY
           enforcementMode: ENFORCED_BLOCK_AND_AUDIT_LOG
         name: projects/<var>PROJECT_ID</var>/policy
         

  3. Import the policy YAML file back into Binary Authorization:
         
         gcloud container binauthz policy import /tmp/policy.yaml
         




###  REST API 

To modify the policy, do the following:

  1. Create a text file with the updated policy in JSON format:
         
         cat > /tmp/policy.json << EOM
         {
           "name": "projects/${PROJECT_ID}/policy",
           "admissionWhitelistPatterns": [
             {
               "namePattern": "us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0"
             }
           ],
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
         




## Test the policy

To test the policy by deploying image you added to the `Exempt image` allowlist, do the following:

  1. Deploy an exempt image to the cluster.

###  Google Cloud console 

Deploy an exempt image:

     1. Go to the GKE **Clusters** page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

     2. Click **Deploy**.

The console prompts you to enter details about the deployment.

     3. Select **Existing Container Image**.

     4. Enter the container image path.

###  Artifact Registry 

To deploy an image from Artifact Registry enter the following:
            
            us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            

     5. Click **Continue**.

     6. Enter `hello-server` in the **Application Name** field.

     7. Click **Deploy**.

###  kubectl 

###  Artifact Registry 

Deploy the image from Artifact Registry:
    
    kubectl run hello-server --image us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0 --port 8080
    

  2. Verify that the image was allowed to deploy:

###  Google Cloud console 

To verify that the image was deployed, do the following:

     1. Go to the GKE page.

[Go to GKE](https://console.cloud.google.com/kubernetes/workload?workload_list_tablesize=50)

     1. Go to the **Workloads** page.

The `hello-server` workload appears with a green icon, indicating it is running.

###  kubectl 

To verify that the image was allowed to deploy, enter the following command:
    
    kubectl get pods
    

You see the image running.

  3. Delete the pod.

###  Google Cloud console 

In the GKE **Workloads** page:

     1. Select the **hello-server** workload.

     2. Click **Delete**.

     3. When prompted to delete resources, click **Delete**.

###  kubectl 
    
    kubectl delete pod hello-server
    




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Delete the cluster you created in GKE:

###  Console 

To delete the cluster, do the following:

  1. Go to the GKE **Clusters** page in the Google Cloud console.

[Go to GKE](https://console.cloud.google.com/kubernetes/list)

  2. Select the `test-cluster` cluster and click **Delete**.




###  gcloud 

To delete the cluster, enter the following command:
    
    
    gcloud container clusters delete \
        --zone=us-central1-a \
        test-cluster
    

## What's next

  * To learn more about exempting images, including using wildcards to exempt multiple images, see [Exempt images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images).
  * For end-to-end tutorials that describe how to set up and enforce a policy that requires attestations, see the following: 
    * [Get started using the Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/getting-started-cli)
    * [Get started using the Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/getting-started-console)
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore the [DevOps Research and Assessment (DORA)](https://dora.dev/) research program.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
