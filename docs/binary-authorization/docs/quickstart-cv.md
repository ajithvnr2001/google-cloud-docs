---
url: https://docs.cloud.google.com/binary-authorization/docs/quickstart-cv/
title: Monitor Pod security with continuous validation \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:38.503380+00:00
---

# Monitor Pod security with continuous validation  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/quickstart-cv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quickstart: Monitor Pod security with continuous validation

Learn how to get started with Binary Authorization continuous validation (CV) with [check-based policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#platform-policies). In this quickstart, you use the following CV [_checks_](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#checks) to continuously validate running Pods for the following conditions:

  * [Trusted directory](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#trusted-directory-check): Checks that the images associated with the Pod reside in one or more trusted directories that you specify in the policy.
  * [Image freshness](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#freshness-check): Checks that the Pod's images were uploaded within a number of days that you specify in the policy.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Binary Authorization and Google Kubernetes Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com binaryauthorization.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the Binary Authorization and Google Kubernetes Engine APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com binaryauthorization.googleapis.com

  14. [Install the `kubectl` command-line tool.](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
  15. If your Binary Authorization policies and GKE clusters are in different projects, make sure that Binary Authorization is enabled in both projects.



## Create a platform policy

To set up a CV GKE platform policy, do the following:

  1. Create the platform policy YAML file:
         
         cat << EOF > /tmp/my-policy.yaml
         gkePolicy:
           checkSets:
           - checks:
             - trustedDirectoryCheck:
                 trustedDirPatterns:
                 - us-central1-docker.pkg.dev/my-project/my-directory
               displayName: My trusted directory check
             - imageFreshnessCheck:
                 maxUploadAgeDays: 30
               displayName: My image freshness check
             displayName: My trusted directory and image freshness check set
         EOF
         

This policy checks for the following conditions:

     * The Pods' images are stored in the Artifact Registry repository named `us-central1-docker.pkg.dev/my-project/my-directory`.

     * The Pods' images were uploaded to the Artifact Registry or Container Registry repositories within the last 30 days.

  2. Create the platform policy:
         
         gcloud beta container binauthz policy create POLICY_ID \
             --platform=gke \
             --policy-file=/tmp/my-policy.yaml \
             --project=POLICY_PROJECT_ID
         

Replace the following:

     * `POLICY_ID`: an ID of your choice
     * `POLICY_PROJECT_ID`: the policy project ID



## Create or update a cluster

To enable CV on a cluster you can create a new cluster or update an existing cluster.

  * To create a cluster with the check-based platform policy enabled, run the following command:
        
        gcloud beta container clusters create CLUSTER_NAME \
            --location=LOCATION \
            --binauthz-evaluation-mode=POLICY_BINDINGS \
            --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
            --project=CLUSTER_PROJECT_ID
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster
    * `LOCATION`: the location—for example: `us-central1` or `asia-south1`
    * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
    * `POLICY_ID`: the policy ID
    * `CLUSTER_PROJECT_ID`: the cluster project ID

Wait for the cluster to be created.

  * To update an existing cluster with check-based policies enabled, run the following command.

**Important:** If your cluster already has Binary Authorization enforcement enabled, set `--binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE`.
        
        gcloud beta container clusters update CLUSTER_NAME \
            --location=LOCATION \
            --binauthz-evaluation-mode=POLICY_BINDINGS \
            --binauthz-policy-bindings=name=projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID \
            --project=CLUSTER_PROJECT_ID
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster
    * `LOCATION`: the location—for example: `us-central1` or `asia-south1`
    * `POLICY_PROJECT_ID`: the ID of the project where the policy is stored
    * `POLICY_ID`: the policy ID
    * `CLUSTER_PROJECT_ID`: the cluster project ID

Wait for the cluster to be updated.




## Deploy an image

  1. Get the credential for `kubectl`:
         
         gcloud container clusters get-credentials CLUSTER_NAME
         

  2. Deploy an image:
         
         kubectl run hello-app \
             --image=us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
         

The image `us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0` satisfies the freshness check because it was uploaded to the repository within the last 30 days. But the image doesn't satisfy the trusted directory check because it's not in `us-central1-docker.pkg.dev/my-project/my-directory`. As a result, CV produces `TrustedDirectoryCheck` log entries in Cloud Logging.




## View the logs

The log entry appears in Cloud Logging within 24 hours after the Pod is deployed, but it can appear in as few as a couple of hours.

To view the log in Cloud Logging, use the following filter:
    
    
    logName:"binaryauthorization.googleapis.com%2Fcontinuous_validation"
    "policyName"
    

The log for the `hello-app` Pod is similar to the one below. Some fields might be different depending on your project ID, cluster name, etc.
    
    
    {
      "insertId": "637c2de7-0000-2b64-b671-24058876bb74",
      "jsonPayload": {
        "podEvent": {
          "endTime": "2022-11-22T01:14:30.430151Z",
          "policyName": "projects/1234567890/platforms/gke/policies/my-policy",
          "images": [
            {
              "result": "DENY",
              "checkResults": [
                {
                  "explanation": "TrustedDirectoryCheck at index 0 with display name \"My trusted directory check\" has verdict NOT_CONFORMANT. Image is not in a trusted directory",
                  "checkSetName": "Default check set",
                  "checkSetIndex": "0",
                  "checkName": "My trusted directory check",
                  "verdict": "NON_CONFORMANT",
                  "checkType": "TrustedDirectoryCheck",
                  "checkIndex": "0"
                }
              ],
              "image": "us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0"
            }
          ],
          "verdict": "VIOLATES_POLICY",
          "podNamespace": "default",
          "deployTime": "2022-11-22T01:06:53Z",
          "pod": "hello-app"
        },
        "@type": "type.googleapis.com/google.cloud.binaryauthorization.v1beta1.ContinuousValidationEvent"
      },
      "resource": {
        "type": "k8s_cluster",
        "labels": {
          "project_id": "my-project",
          "location": "us-central1-a",
          "cluster_name": "my-cluster"
        }
      },
      "timestamp": "2022-11-22T01:44:28.729881832Z",
      "severity": "WARNING",
      "logName": "projects/my-project/logs/binaryauthorization.googleapis.com%2Fcontinuous_validation",
      "receiveTimestamp": "2022-11-22T03:35:47.171905337Z"
    }
    

The log entry shows information about the policy violation, including the following fields:

  * `policyName`: a platform policy that CV was using when it identified the violation
  * `checkResults`: a block of results that includes the following fields:

    * `explanation`: an error message
    * `checkSetName`: the `displayName` value for the check set
    * `checkSetIndex`: the index of the check set in the policy
    * `checkName`: the name of the check
    * `checkIndex`: the index of the check in the check set
    * `verdict`: the verdict that resulted in the log entry, in this case `NOT_CONFORMANT` because the check wasn't satisfied.



Some checks can include additional information that can help you understand why the check was not satisfied.

Because the image satisfied the freshness check, the freshness check does not appear in the log.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

This section describes how to clean up the CV monitoring you configured earlier in this guide.

You can disable CV monitoring or both Binary Authorization and CV in your cluster.

### Disable Binary Authorization in a cluster

To disable both CV and Binary Authorization enforcement in your cluster, run the following command:
    
    
    gcloud beta container clusters update CLUSTER_NAME \
        --binauthz-evaluation-mode=DISABLED \
        --location=LOCATION \
        --project=CLUSTER_PROJECT_ID
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster
  * `LOCATION`: the cluster location
  * `CLUSTER_PROJECT_ID`: the cluster project ID



### Disable check-based policy monitoring in a cluster

To disable CV with check-based policies in the cluster, and re-enable enforcement using the Binary Authorization enforcement policy, run the following command:
    
    
    gcloud beta container clusters update CLUSTER_NAME  \
        --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE \
        --location=LOCATION \
        --project="CLUSTER_PROJECT_ID"
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster
  * `LOCATION`: the cluster location
  * `CLUSTER_PROJECT_ID`: the cluster project ID



Note that `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` is equivalent to the older flag `--enable-binauthz`.

### Delete the policy

To delete the policy, run the following command. It is not necessary to delete the check-based platform policy to disable check-based policy auditing.
    
    
    gcloud beta container binauthz policy delete POLICY_ID \
        --platform=gke \
        --project="POLICY_PROJECT_ID"
    

Replace the following:

  * `POLICY_ID`: the ID of the policy
  * `POLICY_PROJECT_ID`: the policy project ID



## What's next

  * [Use the image freshness check](https://docs.cloud.google.com/binary-authorization/docs/cv-freshness-check)
  * [Use the simple signing attestation check](https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check)
  * [Use the Sigstore signature check](https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check)
  * [Use the SLSA check](https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check)
  * [Use the trusted directory check](https://docs.cloud.google.com/binary-authorization/docs/cv-trusted-directory-check)
  * [Use the vulnerability check](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check)
  * [View CV logs](https://docs.cloud.google.com/binary-authorization/docs/cv-view-logs)

  * Learn about [CV](https://docs.cloud.google.com/binary-authorization/docs/overview-cv) and other [CV checks](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#checks). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
