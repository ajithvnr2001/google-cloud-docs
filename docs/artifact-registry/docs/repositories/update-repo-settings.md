---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/update-repo-settings/
title: Update repository settings \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:50.764797+00:00
---

# Update repository settings  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/update-repo-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Update repository settings Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you update repository settings for repository descriptions, [labels](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos), upstream authentication details, vulnerability [scanning settings](https://docs.cloud.google.com/artifact-analysis/docs/enable-automatic-scanning#disable-repo), and immutable image tags for Docker repositories.

**Note:** When you enable immutable image tags, an image tag always points to the same image digest, including the default `latest` tag. To learn more about image tags, image digests, and immutable image tags, see [Container image versions](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions).

### Required roles

To get the permissions that you need to update repository settings, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on the Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update settings

You can update settings using Google Cloud console or Google Cloud CLI.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the repository and click **Edit Repository**.

  3. Edit the settings that you want to change:

     * Change the repository description.
     * Update your remote repository upstream authentication details.
     * **Enable** or **disable** immutable image tags in the **Immutable image tags** section. If you enable this setting, the following actions are not permitted: 
       * Delete a tagged image.
       * Remove a tag from an image.
       * Push an image with a tag that is already used by another version of the image in the repository.
       * Add, remove, or update labels.
     * **Enable** or **disable** vulnerability scanning.
  4. Click **Save**.




###  gcloud 

To edit the repository description, run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --description="DESCRIPTION"
    

To update your remote repository upstream authentication details, run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT_ID \
        --location=LOCATION \
        --remote-username=USERNAME \
        --remote-password-secret-version=projects/PROJECT_ID/secrets/SECRET_ID/versions/SECRET_VERSION
    

To edit the image tag mutability, run one of the following commands:

To set image tags to immutable:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --immutable-tags
    

To set image tags to mutable:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --no-immutable-tags
    

To update labels, run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --update-labels="KEY=VALUE,..."
    

To edit the vulnerability scanning settings, run one of the following commands:

To disable scanning on the repository:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --disable-vulnerability-scanning
    

To allow scanning on the repository:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT-ID \
        --location=LOCATION \
        --allow-vulnerability-scanning
    

Replace the following values:

  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.
  * `PROJECT-ID` is the Google Cloud project ID. If this flag is omitted, the current or default project is used.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, you can omit this flag to use the default.
  * `DESCRIPTION` is a description for the repository.
  * `USERNAME` is your upstream repository username.
  * `SECRET_ID` is the name of your secret.
  * `SECRET_VERSION` is the secret version you want to use.
  * The two tag setting flags, `--no-immutable-tags` or `--immutable-tags`, indicate how tags are associated with versions of images.
    * `--no-immutable-tags`: the image version that tag points to can change. Deleting images, removing tags, and changing the version of an image that a tag points to are permitted.
    * `--immutable-tags`: in the repository, a tag always points to same version of an image. The following actions are not permitted: 
      * Delete a tagged image.
      * Remove a tag from an image.
      * Push an image with a tag that is already used by another version of the image in the repository.

  * `KEY=VALUE...` is a list of comma-separated labels specified as key-value pairs. For example: `team=team-1,product=example_product,stage=development`. For more information about working with labels, see [Label repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos).



## What's next

  * Learn to [restrict artifact downloads with download rules](https://docs.cloud.google.com/artifact-registry/docs/restrict-artifact-downloads). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
