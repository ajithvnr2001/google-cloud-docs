---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/push-container-image/
title: Push and pull container images from a cluster \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:50.864461+00:00
---

# Push and pull container images from a cluster  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations-30/push-container-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Push and pull container images from a cluster Stay organized with collections  Save and categorize content based on your preferences. 

System artifacts exist in the Artifact Registry of the org infrastructure cluster. When a Platform Administrator (PA) creates an organization in Google Distributed Cloud (GDC) air-gapped appliance, all of the system artifacts are replicated from the org infrastructure cluster.

The Infrastructure Operator (IO) must push new system artifacts to the org infrastructure cluster. Pushing new system artifacts happens only when the PA requests to enable optional features, or when the system shows bugs or outages that you can fix by patching new artifacts.

## Before you begin

To get the permissions that you need to access resources in system Artifact Registry projects as an administrator, ask your Security Admin to grant you the following roles depending on the cluster you want to push the container image to.

After obtaining the necessary permissions, work through the following steps before pushing an image to the system Artifact Registry of the infrastructure cluster:

  1. Download and install the Distributed Cloud CLI following the instructions of [gdcloud command-line interface (CLI)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview).

  2. Install the `docker-credential-gdcloud` component following the instructions of [Install components](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-install#install-components):
         
         gdcloud components install docker-credential-gdcloud
         

  3. [Sign in with the configured identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth):
         
         gdcloud auth login
         

  4. Export the kubeconfig file:
         
         gdcloud clusters get-credentials CLUSTER_NAME
         

Replace `CLUSTER_NAME` with the name of the cluster.

  5. Configure Docker:
         
         gdcloud auth configure-docker
         




## Download a container image from a storage bucket

**Note:** Refer to this section if the container image to upload is stored in a storage bucket. Otherwise, if the container image is in your workstation, you can skip to Push the image to the system Artifact Registry.

Follow the instructions in this section when the PA requests to download the image from a storage bucket and upload the image to the system Artifact Registry. The PA must provide details such as the project and bucket names.

As an IO, you need permissions to download the container image from the storage bucket:

  * Ask your Security Admin to grant you the Project Bucket Object Viewer (`project-bucket-object-viewer`) role in the project's namespace.



For more details, see the [IAM R0005](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/gdch-io/service-manual/iam/runbooks/iam-r0005) runbook.

You get read-only access on the bucket within the project and the objects in that bucket.

After obtaining the necessary permissions, follow these steps to download the container image from the storage bucket of the PA project's namespace:

  1. Ask the PA for the secret name of the bucket. The secret name looks like the following example:
         
         object-storage-key-std-user-ID
         

The secret name includes a unique `ID` value to access the bucket.

  2. Copy the secret name of the bucket.

  3. Get bucket access credentials and configure the gdcloud CLI:
         
         SECRET_NAME=SECRET_NAME ACCESS_KEY=$(kubectl get secret ${SECRET_NAME} -n object-storage-access-keys -o=jsonpath='{.data.access-key-id}' | base64 -d)
         SECRET_KEY=$(kubectl get secret ${SECRET_NAME} -n object-storage-access-keys -o=jsonpath='{.data.secret-access-key}' | base64 -d)
         S3_ENDPOINT=objectstorage.$(kubectl get configmap dnssuffix -n gpc-system -o jsonpath='{.data.dnsSuffix}')
         
         echo "Access Key: ${ACCESS_KEY}" \
         && echo "Secret Key: ${SECRET_KEY}" \
         && echo "S3 Endpoint: ${S3_ENDPOINT}"
         
         gdcloud config set storage/s3_access_key_id ${ACCESS_KEY}
         gdcloud config set storage/s3_secret_access_key ${SECRET_KEY}
         gdcloud config set storage/s3_endpoint ${S3_ENDPOINT}
         

Replace `SECRET_NAME` with the value you copied on the previous step.

  4. Download the container image from the storage bucket to your workstation:
         
         gdcloud cp s3://BUCKET_NAME/g/CONTAINER_IMAGE_NAME
         

Replace the following:

     * `BUCKET_NAME`: The name of the storage bucket that has the container image. The PA provides this name.
     * `CONTAINER_IMAGE_NAME`: The name of the container image file that you want to download from the storage bucket.



## Push the image to the System Artifact Registry

Follow these steps to push the file of the container image that you have in your workstation to the system Artifact Registry in the Management API server:

  1. Open the console.

  2. Get the path to the System Artifact Registry endpoint of the cluster where you want to push the container image:
         
         export REGISTRY_ENDPOINT=harbor.$(kubectl get configmap dnssuffix -n gpc-system -o jsonpath='{.data.dnsSuffix}')
         

  3. Load, tag, and push the container image to the System Artifact Registry endpoint of the cluster:
         
         docker load --input CONTAINER_IMAGE_PATH
         
         docker tag CONTAINER_IMAGE_PATH ${REGISTRY_ENDPOINT}/CONTAINER_IMAGE_PATH
         
         docker push ${REGISTRY_ENDPOINT}/CONTAINER_IMAGE_PATH
         

Replace `CONTAINER_IMAGE_PATH` with the path of the container image file in your local file system. A valid value for this path is, for example, `oracle_db.tar`.


**Note:** If the image is not signed by trusted entities, it can't be pulled and fails with a package validation error. Follow the [SAR-R2004](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/sar/runbooks/sar-r2004) runbook to exempt the image from the package validation process.

## Pull Harbor artifact

**Note:** The contents of SAR are confidential and proprietary to Google. Keep them confidential and use them only for the purpose for which you have access. Do not share the contents or permissions with other users or personas.

In most cases, the GDC system interacts with the System Artifact Registry (SAR) automatically to pull the latest artifact from Harbor. For some edge cases, you may perform this operation manually. Follow these steps to manually pull the artifact image from Harbor:

  1. Set the artifact details you define by each application:
         
         APP_NAME=APP
         HARBOR_PROJECT=HARBOR_PROJECT_NAME
         REPOSITORY=REPOSITORY
         

Replace the following:

     * `APP`: the name of the application.
     * `HARBOR_PROJECT_NAME`: the Harbor project name.
     * `REPOSITORY`: the name of the repository.
  2. Get the Harbor information:
         
         HARBOR_URL=$(kubectl --kubeconfig=${ADMIN_KUBECONFIG} get harborcluster harbor -n harbor-system -o=jsonpath='{.spec.externalURL}')
         HARBOR_IP=${HARBOR_URL#https://}
         

  3. Get the artifact tag. There are two methods to retrieve the tag:

     * **Method one** : This is the preferred option:

       1. List the artifacts in the local bundle and get the corresponding tag:
    
    TAG=$(gdcloud artifacts tree ${BUNDLE_SUB_FOLDER:?} | grep ${HARBOR_PROJECT:?}/${REPOSITORY:?} | cut -d ":" -f2 | grep -v '.sig')
    

     * **Method two** : Only use this method if method one does not function as expected:

       1. List the tags in Harbor and select the most recent one:
              
              ADMIN_PASS=$(kubectl --kubeconfig=${ADMIN_KUBECONFIG} -n harbor-system get secret harbor-admin -o jsonpath="{.data.secret}" | base64 -d)
              
                curl -k -X GET \
                  --header 'Accept: application/json' \
                  --header "authorization: Basic $(echo -n admin:${ADMIN_PASS:?} | base64)" \
                "${HARBOR_URL}/api/v2.0/projects/${HARBOR_PROJECT:?}/repositories/${REPOSITORY:?}/artifacts?with_tag=true" | jq -r '.[] | select(.tags != null) | .tags[] | {tag: .name, updated:.push_time}'
              

Your output must look similar to the following example:
              
              {
                "tag": "<tag1>",
                "updated": "<date1>"
              }
              {
                "tag": "<tag2>",
                "updated": "<date2>"
              }
              

       2. Export the value of the tag with the most recent updated time:
              
              TAG=MOST_RECENT_TAG
              

Replace `MOST_RECENT_TAG` with the tag with the most recent updated time.

  4. Download the artifacts from Harbor:
         
         gdcloud artifacts pull --single-manifest-repo \
         ${HARBOR_IP:?}/${HARBOR_PROJECT:?}/${REPOSITORY:?}:${TAG:?} \
         ${APP_NAME:?}-${TAG:?}
         

If you see the following error message, it can be safely ignored:
         
         tee: '/root/logs/artifacts_pull_--single-manifest-repo_2023.07.13:14.59.24.log': Permission denied
         




### Known issues

There are several known issues associated with pulling the Harbor artifact:

  * You might need to add the argument: `--kubeconfig ${INFRA_ORG_KUBECONFIG:?}`.
  * The `curl` command might show the following error message: `certificate signed by unknown authority`. Mitigate this error using one of the following methods:

    * **Temporary fix** : Add the `--insecure` flag to the `gdcloud artifacts pull` command.
    * **Reliable fix** : Trust the org infrastructure CA. For more information, see [Image pull error](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/artifact-registry#image-pull-error).
  * You might need to extract the contents:
        
        gdcloud artifacts extract ${APP_NAME:?}-${TAG:?} ${APP_NAME:?}-${TAG:?}-extracted
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
