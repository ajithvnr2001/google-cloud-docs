---
url: https://docs.cloud.google.com/artifact-analysis/docs/controlling-costs/
title: Control your vulnerability scanning costs \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:09.412960+00:00
---

# Control your vulnerability scanning costs  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/controlling-costs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Control your vulnerability scanning costs Stay organized with collections  Save and categorize content based on your preferences. 

Vulnerability scanning became a paid service with the [general availability release](https://docs.cloud.google.com/container-registry/docs/release-notes#September_20_2019) of Artifact Analysis. When you [enable the scanning API](https://docs.cloud.google.com/artifact-analysis/docs/enable-container-scanning), billing begins immediately. 

See the [pricing page](https://docs.cloud.google.com/artifact-analysis/pricing) for more information.

## Best practices for keeping your costs low

When you enable the Container Scanning API, every new image you push is automatically scanned. To keep your costs low, try the following:

  * Enable scanning on single repositories within a project.

  * Separate the container images that you want to scan into a different project.

  * Set up a new [Google Cloud project](https://docs.cloud.google.com/docs/overview#projects) and enable the Container Scanning API for that project. This project will incur normal [billing charges](https://docs.cloud.google.com/artifact-analysis/pricing) for Artifact Registry. Push the images you want to scan to this project.

  * Add the following steps in your CI/CD pipeline:

    1. Add a tag corresponding to the Artifact Registry project where Container Scanning is enabled.

    2. Push the images to the project.




## Estimate your scanning costs

To calculate the approximate cost for the images in a project, estimate the number of images you push in a timeframe and multiply that number by the price per scan. You can do this by running a shell script in [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. Open a Cloud Shell in your project.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Click the **Open Editor** icon and create a new file `cost-estimation.sh` with the following content:
         
         #!/bin/bash
         
             # Replace with price from https://cloud.google.com/artifact-analysis/pricing
             PRICE='PRICE'
         
             # Replace with your project data
             GC_PROJECT='PROJECT_REPOSITORY'
             START_DATE='START_DATE'
             END_DATE='END_DATE'
         
             REGION=$(echo $GC_PROJECT | sed -n 's/\/.*//p')
         
             if [ -z "$REGION" ];
             then
                 printf "'GC_PROJECT' value must be a valid GCR or AR repository (e.g. gcr.io/corp-staging or us-central1-docker.pkg.dev/myproj/myrepo"
                 exit 1
             fi
         
             IFS=$'\n'
             FILTER="timestamp.date('%Y-%m-%d', Z)>'$START_DATE' AND timestamp.date('%Y-%m-%d', Z)<'$END_DATE'"
         
             images=$( gcloud container images list --repository="$GC_PROJECT" | sed -n "/$REGION/p" | sed 's/NAME: //' )
         
             num_images=$(echo $images | wc -w)
         
             printf "Using gcloud to filter $num_images images from $START_DATE to $END_DATE (takes about 1 second per image)\n\n"
         
             total_digests=0
         
             for image in $images; do
             printf "querying $image\n"
             image_digests=$( gcloud container images list-tags --filter="$FILTER" "$image" 2> >(sed "s/Listed 0 items.//" | sed -n "/.\+/p" >&2) | wc -l)
         
             if [[ "$image_digests" -gt 1 ]]; then
                 total_digests=$(( total_digests + $image_digests - 1 ))
             fi
             done
         
             total_price=$( python -c "print($total_digests * $PRICE)" )
         
             echo ''
             echo "Number of images: $total_digests"
             echo "Estimated cost: $total_price"
         

Replace the following:

     * `PRICE`: the price for automatic vulnerability scanning found in [Pricing](https://cloud.google.com/artifact-analysis/pricing).
     * `PROJECT_REPOSITORY`: your project repository. For example, `gcr.io/corp-staging`.
     * `START_DATE`: the starting date for the period to estimate, in `Y-m-d` format. For example, `2020-03-01`.
     * `END_DATE`: the end date for the period to estimate, in `Y-m-d` format. For example, `2020-03-31`.
  3. Run the script:
         
         bash cost-estimation.sh
         

It shows the total number of images and the total estimated cost:
         
         Number of images: 53
         Estimated cost: 13.78
         




This is only an estimation, the actual cost may change due to other factors, for example:

  * Pushing the same image to different multi-regions in the same project does not generate additional costs.

  * Pushing the same image to two different repositories within two different projects does not generate additional costs.




## Check current vulnerability scanning costs

You can see this information in your [billing report](https://docs.cloud.google.com/billing/docs/how-to/reports).

## What's next

  * Learn more about [vulnerability scanning](https://docs.cloud.google.com/artifact-analysis/docs/vulnerability-scanning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
