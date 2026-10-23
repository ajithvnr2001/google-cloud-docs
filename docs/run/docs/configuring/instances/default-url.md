---
url: https://docs.cloud.google.com/run/docs/configuring/instances/default-url/
title: Default URL for Cloud Run instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:17.163780+00:00
---

# Default URL for Cloud Run instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/instances/default-url/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Default URL for Cloud Run instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, every Cloud Run instance receives a default `run.app` URL when created. This unique, addressable URL has the following format:
    
    
    https://INSTANCE_NAME-PROJECT_NUMBER.REGION.run.app

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud Run instance.
  * `PROJECT_NUMBER`: the Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * `REGION`: the name of the region, such as `europe-west1`.



If you want to remove access to the default URL endpoint, you can disable it. To further secure your instance from public access, you can also configure ingress settings to control and restrict network access. See instructions for [configuring ingress settings for Cloud Run instances](https://docs.cloud.google.com/run/docs/securing/ingress#set-ingress-for-instances).

When you disable the default URL, Cloud Run restricts ingress to private and Virtual Private Cloud paths, while maintaining an individual URL per instance.

## Disable the default URL for Cloud Run instances

Disable the default `run.app` URL of a Cloud Run instance to only allow traffic from the instance's other ingress paths: Cloud Load Balancing and any configured [domain mapping](https://docs.cloud.google.com/run/docs/mapping-custom-domains).

###  gcloud 

  * For an existing instance, run the `gcloud beta run instances update` command with the `--no-default-url` flag, for example:
        
        gcloud beta run instances update INSTANCE --no-default-url

  * For a new instance, run the `gcloud beta run instances deploy` command with the `--no-default-url` flag, for example:
        
        gcloud beta run instances deploy INSTANCE \
            --image IMAGE_URL \
            --no-default-url

Replace `INSTANCE` with the name of your Cloud Run instance.

In the output, the URL displays as `None`.




To restore the default URL, use the `--default-url` flag.

### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. To disable the default URL, set the `run.googleapis.com/default-url-disabled` annotation to `'true'`:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/default-url-disabled: 'true'
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - name: CONTAINER_NAME
             image: IMAGE_URL

Replace the following:

     * `INSTANCE`: the name of your Cloud Run instance.
     * `CONTAINER_NAME`: the name of the container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




To restore the default URL, set the `run.googleapis.com/default-url-disabled` annotation to `false` or remove it.

## What's Next

See [Restrict network endpoint ingress](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url-for-instances) for more details and instance configuration instructions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
