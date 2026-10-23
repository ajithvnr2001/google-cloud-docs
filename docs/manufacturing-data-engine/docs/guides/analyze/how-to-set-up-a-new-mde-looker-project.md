---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-set-up-a-new-mde-looker-project/
title: Set up a Looker project \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:02.988807+00:00
---

# Set up a Looker project  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-set-up-a-new-mde-looker-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a Looker project

MDE provides a _Looker Project Template_ git [repository](https://github.com/GoogleCloudPlatform/mde-looker-project-template) to help you bootstrap a new MDE Looker project. We also provide a library that includes MDE-specific LookML base components and starter configuration packages to reduce the time it takes to model your MDE data in LookML.

### Before you begin

To complete this guide, you need the following prerequisites:

  1. An active Looker instance.
  2. A Looker user account with the `Admin` role.
  3. An active MDE deployment in a Google Cloud project with the _default_ MDE configuration package applied.
  4. A user account with at least the following Identity and Access Management (IAM) roles for the Google Cloud project referenced: 
     * `roles/iam.serviceAccountCreator`
     * `roles/iam.serviceAccountKeyAdmin`
     * `roles/resourcemanager.projectIamAdmin`
     * `roles/source.admin`
  5. Workstation with a local installation of: 
     * git
     * Google Cloud CLI



## How to bootstrap a new LookML project

  1. Set the default `gcloud` project to your MDE deployment project.

All `gcloud` commands in this guide assume that the default project is set to the MDE deployment project. You can set the default project using the following command:
         
         gcloud config set project PROJECT_ID
         

Replace the following:

`PROJECT_ID` with the MDE deployment project ID.

  2. Create a service account that Looker uses to read data from BigQuery, and generate a JSON key for the created service account using the following commands:
         
         export SA_LOOKER="mde-looker"
         export PROJECT_ID=$(gcloud config get-value project)
         gcloud iam service-accounts create $SA_LOOKER --display-name "MDE Looker account"
         gcloud projects add-iam-policy-binding ${PROJECT_ID} --member serviceAccount:${SA_LOOKER}@${PROJECT_ID}.iam.gserviceaccount.com  --role "roles/bigquery.dataEditor"
         gcloud projects add-iam-policy-binding ${PROJECT_ID} --member serviceAccount:${SA_LOOKER}@${PROJECT_ID}.iam.gserviceaccount.com  --role "roles/bigquery.jobUser"
         
         export SA_LOOKER_KEY=~//mde-projects/$PROJECT_ID/${SA_LOOKER}_key.json
         gcloud iam service-accounts keys create $SA_LOOKER_KEY --iam-account ${SA_LOOKER}@${PROJECT_ID}.iam.gserviceaccount.com
         
         cat <<EOF
         ===========================================
         Connection credentials to be used in Looker
         ===========================================
         
         ConnectionName: mde-bigquery-connection
         ProjectName: ${PROJECT_ID}
         Dataset: mde_data
         ServiceAccount Email: ${SA_LOOKER}@${PROJECT_ID}.iam.gserviceaccount.com
         ServiceAccount JSON key location: ${SA_LOOKER_KEY}
         
         EOF
         

  3. [Create](https://docs.looker.com/setup-and-management/database-config/google-bigquery) a new BigQuery connection in Looker with the following specifications:

     * Name the connection as specified in the output of Step 2.
     * Set the dataset as specified in the output of Step 2.
     * Follow the [service account](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#authentication_with_bigquery_service_accounts) authentication path, and use the service account key available in the location specified in the output of Step 2.
     * Configuring PDTs for the purposes of this guide is unnecessary. You can always configure PDTs for this connection on a later stage.
     * Set the database timezone to UTC.
  4. Create a new git repository. This repository will host the LookML code of your Looker project.

The following command creates a GitHub repository using the GitHub CLI. However, you can create a repository with any [supported](https://docs.cloud.google.com/looker/docs/setting-up-git-connection) git service.
         
         gh repo create mde-looker --private --clone
         

  5. Navigate to the newly created repository it using the following command:
         
         cd mde-looker
         

  6. Pull the _MDE Looker Project Template_ files, and push them into your new Looker repository with the following commands:
         
         git checkout -b master
         git remote add project https://github.com/GoogleCloudPlatform/mde-looker-project-template.git
         git pull project master
         git push -u origin master
         

  7. [Create a blank Looker project](https://docs.cloud.google.com/looker/docs/create-projects#creating_a_blank_project).

  8. [Connect](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#connecting_to_git_using_ssh) the project you created in Step 6 with the git repository you created in Step 4, and [register](https://www.googlecloudcommunity.com/gc/Technical-Tips-Tricks/Using-Cloud-Source-Repositories-for-Version-Control-in-Looker/ta-p/587473) the SSH key that Looker generates with Cloud Source.

  9. Configure access to the _MDE LookML Library_.

The _MDE Project Template_ declares the _MDE LookML Library_ as a dependency. Since the _MDE LookML Library_ is hosted in a private [GitHub repository](https://github.com/GoogleCloudPlatform/mde-lookml-lib), the public SSH key of your Looker project must be allow before you can access it:

     1. Obtain the SSH key of your Looker project.

[Configure](https://docs.cloud.google.com/looker/docs/importing-projects#configuring_authentication_credentials_for_private_remote_repositories) authentication for the _MDE LookML Library_ using the SSH method and obtain the public SSH key of your Looker project.

     2. Request access to the _MDE LookML Library_. Once you have obtained an SSH key, fill out the [MDE LookML Library Access Form](https://docs.google.com/forms/d/e/1FAIpQLSd08cF-SLty6ZjTac727XiEM2G2N_Vu_g_F9O5-c6UWrSYBow/viewform?usp=header_link) for allowlisting. Your Looker project will have access to the library after the SSH key has been allow.

     3. Test access.

After the SSH key of your Looker project has been allow, you can [test](https://docs.cloud.google.com/looker/docs/importing-projects#configuring_authentication_credentials_for_private_remote_repositories) that your Looker project can connect to the GitHub repository where the _MDE LookML Library_ is hosted.

  10. Open the `manifest.lkml` file in Looker, and supply the required values:

     * Replace `<TAG_METADATA_BUCKET_NUMBER>` with the tag metadata bucket number.
     * Replace `<SOURCE_METADATA_BUCKET_NUMBER>` with the tag metadata bucket number.

You can look up the bucket numbers in the MDE web interface or by calling the `GET/metadata/v1/buckets/tag` and `GET /metadata/v1/buckets/source` API endpoints. Alternatively, you can look up the bucket numbers in the MDE UI or Manufacturing Connect.

  11. Congratulations, you have set up Looker for MDE.

The LookML model in _MDE Looker Project Template_ imports the LookML explore file and dashboards from the default configuration package in the _MDE LookML Library_. The default explore file contains an explore per default MDE type. If you are using the default configuration package in MDE, you can start analyzing your data right away. See the guide on [how to use the MDE LookML Library](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/analyze/how-to-use-the-mde-lookml-lib) for more details.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
