---
url: https://docs.cloud.google.com/iap/docs/enabling-gcs-cloud-run/
title: Enable IAP for Cloud Storage buckets \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:25.814104+00:00
---

# Enable IAP for Cloud Storage buckets  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/enabling-gcs-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Enable IAP for Cloud Storage buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to serve secure static content from Cloud Storage using Cloud Run and Identity-Aware Proxy.

Cloud Run lets you host a web server that serves static content from a private Cloud Storage bucket. Adding IAP helps you secure the Cloud Run service, preventing unauthorized access while avoiding the need to rebuild your container image when the content changes.

Cloud Storage static website hosting only serves public content and requires granting read access to `allUsers`. If your organization restricts public buckets using policies such as [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) or [domain-restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains), the built-in Cloud Storage static website hosting feature is unavailable. Instead, keep your bucket private, deploy an NGINX web server on Cloud Run with the bucket mounted as a volume, and use IAP to control access to the Cloud Run service.

## Before you begin

To complete the instructions in this document, you need the following:

  * A Google Cloud project with billing enabled. [Go to Google Cloud console](https://console.cloud.google.com/)
  * A private Cloud Storage bucket that contains your static files (for example, `index.html`, CSS, and images). Ensure the bucket is not public.
  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) installed.



## Grant access to the Cloud Storage bucket

Cloud Run needs permission to read files from your private Cloud Storage bucket. You must grant the Cloud Run service identity the Storage Object Viewer (`roles/storage.objectViewer`) role on the bucket.

We recommend that you use a user-managed service account for your Cloud Run service instead of the default Compute Engine service account.

  1. Create a service account to use as the service identity:
         
         gcloud iam service-accounts create RUN_SERVICE_ACCOUNT \
             --description="Service account for Cloud Run serving Cloud Storage" \
             --display-name="Cloud Run Cloud Storage Reader"
         

  2. Grant the service account the Storage Object Viewer (`roles/storage.objectViewer`) role on the bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member="serviceAccount:RUN_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/storage.objectViewer"
         




## Deploy the Cloud Run service

Deploy the NGINX web server to Cloud Run and mount the Cloud Storage bucket. You must use the second-generation execution environment to support volume mounts.

To mount the bucket, deploy the service with volume flags:
    
    
    gcloud run deploy SERVICE_NAME \
        --image=nginx \
        --port=80 \
        --execution-environment=gen2 \
        --service-account=RUN_SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com \
        --add-volume=name=static,type=cloud-storage,bucket=BUCKET_NAME,readonly=true \
        --add-volume-mount=volume=static,mount-path=/usr/share/nginx/html \
        --no-allow-unauthenticated
    

Replace the following:

  * `SERVICE_NAME`: the name of your Cloud Run service
  * `RUN_SERVICE_ACCOUNT`: the service account that you created in the previous step
  * `PROJECT_ID`: your Google Cloud project ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket



The bucket is mounted to `/usr/share/nginx/html`, which is the default directory where NGINX looks for static assets. This means that the files in your bucket are mapped directly to the root path of your service. For example, a file stored at `gs://BUCKET_NAME/index.html` is accessible at `https://SERVICE_URL/index.html`.

To verify the deployment, check that the service blocks unauthenticated access and returns a `403 Forbidden` status when accessed without credentials:
    
    
    curl -I SERVICE_URL
    

Alternatively, you can test whether the container is correctly rendering files from your private Cloud Storage bucket before you configure IAP access. To do this, run the following command to send an authenticated request using your developer credentials:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" SERVICE_URL
    

Replace `SERVICE_URL` with the URL of your Cloud Run service.

## Enable IAP

After you deploy your Cloud Run service, you can enable IAP to secure it.

We recommend that you enable IAP directly on the Cloud Run service. For instructions, see [Configure IAP for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run).

Alternatively, if you use an external HTTPS load balancer in front of your Cloud Run service, you can enable IAP on the backend service. For instructions, see [Enable IAP from a backend service or load balancer](https://docs.cloud.google.com/iap/docs/enabling-cloud-run#enable-from-iap).

## Caching and performance

When you use Cloud Storage volume mounts, each file read by Cloud Run translates to a Cloud Storage API call. To minimize latency and API costs, you can configure caching in your web server (for example, using NGINX caching directives) or configure [Cloud Storage FUSE mount options](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts#specify-mount-options).

If you use an external HTTPS load balancer, you can also enable [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) on the backend service. IAP isn't compatible with Cloud CDN on the same backend service, so you might need to structure your architecture accordingly if you need both.

## Limitations

Reading files from a Cloud Storage volume mount might be slower than accessing a local file system. To mitigate read latency, configure caching.

## Other use cases

You can also use Cloud Storage volume mounts for other scenarios:

  * **Event-driven functions** : A function reads uploaded files directly from the file system.
  * **Generative AI applications** : An application loads a vector database (such as Chroma) from a Cloud Storage bucket using standard file system reads.



## Alternative: Mounting NFS volumes

If your files are stored on Filestore or a self-hosted NFS server, you can mount NFS volumes to your Cloud Run service instead of Cloud Storage buckets. For more information, see [Mounting NFS volumes](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
