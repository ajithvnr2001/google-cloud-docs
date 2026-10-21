---
url: https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline-console/
title: Create and manage custom OS image pipelines using the Google Cloud console \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:29:53.359523+00:00
---

# Create and manage custom OS image pipelines using the Google Cloud console  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create and manage custom OS image pipelines using the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Note:** Image Builder is generally available, but your project must be added to an allowlist before you can use it. To request access, submit the [access request form](https://forms.gle/4NncEhwetZDjaPx9A) or contact your Google Cloud account team. The allowlist covers only the service accounts in your project and doesn't cover Google-owned service accounts. For more information, see [Service accounts covered by the allowlist](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#allowlist-coverage). 

Configure and launch an Image Builder pipeline directly in the Google Cloud console. The Google Cloud console provides an interactive interface where you can specify your base image source, output destinations, customization steps, and execution triggers.

## Before you begin

  * Complete the environment setup steps in [Prepare your environment](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites). 
  * If you intend to trigger builds automatically from a Git repository, connect your GitHub, GitLab, or Bitbucket repository by using either [Cloud Build repositories (`2nd gen`) or Developer Connect connection links](https://docs.cloud.google.com/build/docs/repositories). 



## Required roles

To get the permissions that you need to create and manage image customization pipelines using the Google Cloud console, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Build Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.editor) (`roles/cloudbuild.builds.editor`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create and manage a pipeline

In the Google Cloud console, you can create new custom OS image pipelines, edit existing configurations, duplicate an existing pipeline, or delete pipelines when they are no longer needed.

### Create a pipeline

To create a custom OS image pipeline using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Image Builder** to go to the Image Builder home page.

  3. In the region selector, select the region where you want to create your pipeline.

  4. Click **Create a pipeline**.

  5. In the **Pipeline settings** section, configure the core pipeline details:

     * **Name:** Enter a unique name for the pipeline.
     * **Description:** (Optional) Enter a description for the pipeline.
     * **Region:** Select the Google Cloud region for your pipeline. Image Builder is supported in every [region where Cloud Build is available](https://docs.cloud.google.com/build/docs/locations).
     * **Service account:** Select the service account [configured with the required IAM permissions](https://docs.cloud.google.com/compute/docs/images/image-builder/prerequisites#service-account), or create a new service account.
     * **Configuration source:** Select one of the following methods for where your customization configurations and scripts are stored: 
       * **Integrate with a repository:** Choose this option to retrieve your customization recipe and scripts from a Git repository. Because the repository's `imagebuilder.yaml` file defines the source base image, build zone, customization steps, and target image settings, the console proceeds directly to triggers. Configure the following fields: 
         * **Repository:** Select a connected repository, or click **Link repository** to connect a GitHub, GitLab, or Bitbucket repository.
         * **Path to image builder configuration:** Enter the relative path to your customization recipe file inside the repository, such as `imagebuilder.yaml`.
         * **Cloud Storage folder:** Click **Browse** to select the Cloud Storage folder where pipeline logs and build artifacts are uploaded.
       * **Store scripts in Google Cloud Storage:** Choose this alternative to configure your base image, target image details, and customization steps directly in the console interface. The console saves your scripts to Cloud Storage and guides you through the full step-by-step wizard. Configure the following field: 
         * **Customization script folder:** Click **Browse** to select the Cloud Storage folder to store your customization scripts.
     * **Artifact Registry:** (Optional) If you want to upload the target image archive and generate cryptographic SLSA build provenance attestations, select a generic repository from the **Artifact Registry repository** list. For more information, see [Verify image provenance](https://docs.cloud.google.com/compute/docs/images/image-builder/verify-image-provenance).
  6. Click **Next** to proceed to the remaining configuration panels based on the configuration source you selected:

     * **If you selected Integrate with a repository:**

The repository's `imagebuilder.yaml` recipe defines your source base image, target image settings, and customization steps. The console skips manual entry and proceeds directly to triggers:

       1. In the **Triggers** section, configure when your pipeline runs: 
          * **Run on schedule:** Specify a recurring schedule using cron syntax.
          * **Run on repository event:** Trigger builds automatically when repository events occur, such as a **Push to a branch** , **Push new tag** , or **Pull request** , and specify branch or tag filter patterns.
       2. Click **Next** to proceed to the **Summary** section.
       3. Review your pipeline configuration, and click **Create**.
     * **If you selected Store scripts in Google Cloud Storage:**

       1. In the **Source image details** section, specify the base OS image: 
          * **Use an image family:** Select a public OS family, such as Container-Optimized OS or Ubuntu. The pipeline automatically selects the latest non-deprecated image in that family for every build.
          * **Use an existing image:** Select a specific OS image.
       2. Click **Next** to proceed to the **Target image details** section: 
          * Enter a name for the generated custom OS image.
          * (Optional) Specify an image family, description, resource labels, and customer-managed encryption keys (CMEK).
       3. Click **Next** to proceed to the **Customization** section: 
          * Select **Customization actions** to add, edit, or reorder discrete customization steps, such as installing packages or running inline shell scripts.
          * Select **Add YAML** to write or paste raw recipe `steps` directly in YAML.
          * (Optional) Under **Advanced configurations** , select the specific **Zone** , **Machine type** , or **Reservation** to use for the worker and test VMs where build jobs run. Bare metal machine types are not supported. You can also specify custom VPC **Network** , **Subnetwork** , or **External IP** settings, such as `ephemeral` or `none`, in your recipe's `infrastructureConfig`.
       4. Click **Next** to proceed to the **Triggers** section: 
          * Select **Run on schedule** to define an automated recurring schedule, or leave unchecked for manual execution.
       5. Click **Next** to proceed to the **Summary** section.
       6. Review your pipeline configuration, and click **Create**.



After you create the pipeline:

  * If you did not configure automated triggers, you can run the pipeline manually: from the **Image Builder** pipelines list, click more_vert **More actions > Run** next to your pipeline.
  * If you configured **Run on schedule** or **Run on repository event** , the pipeline runs automatically when the trigger conditions or schedule are met.



### Edit a pipeline

To edit an existing Image Builder pipeline, complete the following steps:

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Image Builder** to view your list of pipelines.

  3. Next to the pipeline that you want to edit, click more_vert **More actions > Edit**.

  4. Update the pipeline settings, configuration source, target image details, customization steps, or trigger settings as needed.

**Note:** The **Pipeline name** and **Region** cannot be changed after creation and are locked in the console. To change these settings, you must create a new pipeline.
  5. Click **Save**.




### Duplicate a pipeline

To create a new pipeline by copying an existing configuration, complete the following steps:

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Image Builder** to view your list of pipelines.

  3. Next to the pipeline that you want to duplicate, click more_vert **More actions > Duplicate**.

  4. In the pipeline creation form, review the pre-filled parameters copied from the original pipeline. You can edit the **Pipeline name** field to specify a new unique name.

  5. Update any pipeline parameters or settings as needed.

  6. Click **Create**.




### Delete a pipeline

When you delete a pipeline, Image Builder stops future automated runs and permanently removes the pipeline configuration. Deleting a pipeline doesn't delete any custom OS images, Artifact Registry artifacts, or Cloud Storage buckets that you created previously.

To delete an Image Builder pipeline, complete the following steps:

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Image Builder** to view your list of pipelines.

  3. Next to the pipeline that you want to delete, click more_vert **More actions > Delete**.

  4. In the confirmation dialog, click **Delete** to permanently remove the pipeline.




## Verify and monitor the build

To track the progress of your build pipeline, complete the following steps:

  1. In the Google Cloud console, go to the **Cloud Build** page.

[Go to Cloud Build](https://console.cloud.google.com/cloud-build/builds)

  2. In the navigation menu, click **History** to view active or completed jobs.

  3. In the **Builds** list, click the **Build ID** of your build to inspect container run logs. The logs display steps being performed inside the worker VM such as system package updates or custom shell commands, followed by validation test results from the test VM, and final output registration.




## What's next

  * Learn how to define customization recipes in the [Customization recipe schema](https://docs.cloud.google.com/compute/docs/images/image-builder/customization-recipe-schema).
  * If you want to configure and run pipelines programmatically using configuration files, see [Create a custom OS image pipeline using gcloud CLI or Terraform](https://docs.cloud.google.com/compute/docs/images/image-builder/create-pipeline).
  * [Verify image provenance](https://docs.cloud.google.com/compute/docs/images/image-builder/verify-image-provenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
