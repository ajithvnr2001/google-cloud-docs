---
url: https://docs.cloud.google.com/run/docs/configuring/instances/restart-policy/
title: Configure restart policy for instances \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:54:16.730387+00:00
---

# Configure restart policy for instances  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/restart-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure restart policy for instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud Run instance's restart policy determines if and when the instance should restart.

## Restart policy options

Select from the following restart policies:

  * `on-failure` (default): If any container exits with a non-zero status code, or if the container experiences infrastructure failures, the instance restarts. For multi-container instances this means any container failing causes the entire instance to restart.
  * `always`: When any container exits, the instance always restarts. This includes clean exits with code `0`.
  * `never`: The instance never restarts. When any container terminates, the instance transitions immediately to a `STOPPED` or `FAILED` state.



When you configure the `always` or `on-failure` restart policy for your instance, your instance automatically restarts at the end of an approximately 7-day lifecycle, therefore running indefinitely unless it's interrupted otherwise.

**Note:** When a multi-container Cloud Run instance has its restart policy set to `always` and any container exits with code `0`, Cloud Run stops the instance instead of restarting it.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run instances, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run instance
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run instance interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/instances/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure restart policy

Configure the restart policy for a Cloud Run instance using the Google Cloud CLI or YAML:

###  gcloud 

To specify a restart policy when deploying a new instance:
    
    
    gcloud beta run instances deploy INSTANCE \
        --image=IMAGE_URL \
        --restart-policy=POLICY

To update the restart policy of an existing instance:
    
    
    gcloud beta run instances update INSTANCE \
        --restart-policy=POLICY

Replace the following:

  * `INSTANCE`: the name of the instance.
  * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  * `POLICY`: the restart policy to apply. Choose from `on-failure`, `always`, or `never`.



### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - name: CONTAINER_NAME
             image: IMAGE_URL
           restartPolicy: POLICY

Replace the following:

     * `INSTANCE`: the name of your Cloud Run instance.
     * `CONTAINER_NAME`: the name of the container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
     * `POLICY`: the restart policy to apply. Choose from `on-failure`, `always`, or `never`.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
