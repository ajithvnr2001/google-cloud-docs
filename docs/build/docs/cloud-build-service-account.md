---
url: https://docs.cloud.google.com/build/docs/cloud-build-service-account/
title: Default Cloud Build service account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:24.978225+00:00
---

# Default Cloud Build service account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/cloud-build-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Default Cloud Build service account Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** We have introduced changes to the default service account used to run builds. As a best practice, we recommend that you [specify your own service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to run your builds. For more information see [Cloud Build default service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

Depending on your organization's settings, Cloud Build may use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or the legacy Cloud Build service account to execute builds on your behalf.

Default service accounts may have permissions that are unnecessarily broad for your use case. You can improve your security posture by following the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely). As part of this principle, we recommend [creating your own service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to execute builds on your behalf. This can reduce the potential impact of misconfigurations or malicious users.

To learn how to grant or revoke permissions to the Cloud Build default service accounts, see [Configure access for the Cloud Build default service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account).

## About the Compute Engine default service account

Your organization's policies might define the default Cloud Build service account to be the Compute Engine default service account. The email address for this service account is  
`PROJECT_NUMBER-compute@developer.gserviceaccount.com`.

For information on the Compute Engine default service account, see [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

## About the legacy Cloud Build service account

Your organization's policies might define the default Cloud Build service account to be the legacy service account. The email for the legacy Cloud Build service account is  
`PROJECT_NUMBER@cloudbuild.gserviceaccount.com`

This section explains all the permissions that the legacy Cloud Build service account has by default.

### Default permissions of the legacy Cloud Build service account

If your project settings allow the use of the legacy Cloud Build service account, the legacy service account is granted the **Cloud Build Service Account** role (`roles/cloudbuild.builds.builder`) for the resources in the project. This role contains a number of permissions, such as the ability to update builds or write logs. The service account uses these permissions only as required to perform actions when executing your build. For example, the service account uses the `artifactregistry.dockerimages.get` permission to get a docker image from Artifact Registry, if your build is configured to do so.

If you don't plan to perform an action as part of the build process, we recommend that you revoke the corresponding permission from the service account to comply with the [security principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely).

**Note:** The legacy Cloud Build service account is owned by Google and is not user managed. Because of this, you can't add an IAM policy binding on it, and therefore you can't have another principal (for example, another service account) [generate](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) access, ID, or JWT tokens for the legacy Cloud Build service account.

The following table lists the permissions that the **Cloud Build Service Account** role (`roles/cloudbuild.builds.builder`) contains and the purpose for which the legacy Cloud Build service account uses these permissions.

**Permission** | **Description** | **Purpose of the permission**  
---|---|---  
`cloudbuild.builds.create` | Can create builds and triggers | Required to:  


  * Use build triggers.
  * Create, list, get, or cancel builds.

  
`cloudbuild.builds.update` | Can update builds and triggers  
`cloudbuild.builds.list` | Can list builds and triggers  
`cloudbuild.builds.get` | Can get a build and a trigger  
`cloudbuild.workerpools.use` | Can use a private pool | Required to run builds in a private pool.  
`logging.logEntries.create` | Can write logs | Required to create and list build logs in Cloud Logging.  
`logging.logEntries.list` | Can list logs  
`logging.views.access` | Can view logs  
`pubsub.topics.create` | Can create Pub/Sub topics  | Required to push build updates to Pub/Sub.  
`pubsub.topics.publish` | Can publish to Pub/Sub  
`remotebuildexecution.blobs.get` | Can get get access to approve or reject builds. |  rowspan=3>Required to approve or reject pending builds  
`resourcemanager.projects.get` | Can get project information  
`resourcemanager.projects.list` | Can list projects  
`source.repos.get` | Can read source code from repositories in Cloud Source Repositories | Required to:  


  * Use Bitbucket and Cloud Source Repositories triggers. 
  * Pull source code from Cloud Source Repositories.

  
`source.repos.list` | Can list repositories in Cloud Source Repositories  
`storage.buckets.create` | Can create Cloud Storage buckets | Required to:  


  * Store and get artifacts in Cloud Storage.
  * Submit builds manually using `gcloud builds submit`.
  * Store build logs in user-created logs bucket.

  
`storage.buckets.get` | Can get Cloud Storage buckets  
`storage.buckets.list` | Can list Cloud Storage buckets  
`storage.objects.list` | Can list Cloud Storage objects  
`storage.objects.update` | Can update Cloud Storage objects  
`storage.objects.create` | Can write Cloud Storage objects  
`storage.objects.delete` | Can delete Cloud Storage objects  
`storage.objects.get` | Can read Cloud Storage objects  
`artifactregistry.repositories.uploadArtifacts` | Can upload artifacts to repositories in Artifact Registry | Required to manage artifacts in Artifact Registry.  
`artifactregistry.repositories.downloadArtifacts` | Can download artifacts from a repository in Artifact Registry  
`artifactregistry.aptartifacts.create` | Can upload Apt artifacts to Artifact Registry  
`artifactregistry.dockerimages.get` | Can get Docker images from Artifact Registry  
`artifactregistry.dockerimages.list` | Can list Docker images stored in Artifact Registry  
`artifactregistry.kfpartifacts.create` | Can upload a KFP artifact to Artifact Registry  
`artifactregistry.locations.get` | Can get information about a location for a resource in Artifact Registry  
`artifactregistry.locations.list` | Can list supported locations for Artifact Registry  
`artifactregistry.mavenartifacts.get` | Can get Maven packages from Artifact Registry  
`artifactregistry.mavenartifacts.list` | Can list Maven packages from Artifact Registry  
`artifactregistry.npmpackages.get` | Can get npm packages from Artifact Registry  
`artifactregistry.npmpackages.list` | Can list npm packages from Artifact Registry  
`artifactregistry.projectsettings.get` | Can get project settings from Artifact Registry  
`artifactregistry.pythonpackages.get` | Can get Python packages from Artifact Registry  
`artifactregistry.pythonpackages.list` | Can list Python packages from Artifact Registry  
`artifactregistry.yumartifacts.create` | Can upload Yum artifacts to Artifact Registry  
`artifactregistry.repositories.createOnPush` | Can create a gcr.io repository in Artifact Registry the first time an image is pushed to a gcr.io hostname in the project.  
`artifactregistry.repositories.get` | Can get a repository from Artifact Registry  
`artifactregistry.repositories.list` | Can list repositories in Artifact Registry  
`artifactregistry.repositories.listEffectiveTags` | Can list tags for artifacts in Artifact Registry | Required to manage tags for artifacts in Artifact Registry.   
`artifactregistry.repositories.listTagBindings` | Can list tag binding information for artifacts in Artifact Registry  
`artifactregistry.tags.create` | Can create tags in Artifact Registry  
`artifactregistry.tags.get` | Can get tags from Artifact Registry  
`artifactregistry.tags.list` | Can list tags in Artifact Registry  
`artifactregistry.tags.update` | Can update tags in Artifact Registry  
`artifactregistry.versions.list` | Can list versions in Artifact Registry  
`artifactregistry.versions.get` | Can get versions in Artifact Registry  
`containeranalysis.occurrences.create` | Can create an Artifact Analysis occurrence | Cloud Build service account does not use these permissions, but they're included for backwards compatibility.  
`containeranalysis.occurrences.delete` | Can delete an Artifact Analysis occurrence  
`containeranalysis.occurrences.get` | Can get an Artifact Analysis occurrence  
`containeranalysis.occurrences.list` | Can list Artifact Analysis occurrences  
`containeranalysis.occurrences.update` | Can update Artifact Analysis occurrences  
  
## Build triggers

When creating [build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers), you must choose the service account used to execute the build. You can configure each trigger with a different service account. The only exception is if your project has the legacy Cloud Build service account [enabled](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#disable-sa), in which case build triggers default to using the legacy service account when no other account is selected.

### User access to triggers

User access to triggers depends on the service account type configured for the trigger:

  * **Legacy Cloud Build service account** (if enabled): Any user with the Cloud Build Editor role can create and directly run a trigger. For example, a user can run the trigger manually. Any user with the Cloud Build Editor role can update a trigger as long as the trigger is using the Cloud Build legacy service account.

  * **User-specified service account or the Compute Engine default service account** : Any user with the Cloud Build Editor role who has the `iam.serviceAccounts.actAs` permission can create and directly run a trigger. For example, a user can run the trigger manually.

Any user with the Cloud Build Editor role can update a trigger as long as they have the `iam.serviceAccounts.actAs` permissions on both the previously configured service account and the new service account specified on the trigger. To give a user this permission, you can grant them a predefined role with the permission, like the **Service Account User** role (`roles/iam.serviceAccountUser`). Alternatively, you can create a custom IAM role with the `iam.serviceAccounts.actAs` permission, then grant that role to the user. To learn more about service account permissions, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions).

**Note:** If you use the same service account to trigger and run a build, then that service account must still have the `iam.serviceAccount.actAs` permission.



### Build-time privileges of triggers

The service account configured for a build trigger can provide elevated build-time permissions to users who employ triggers to invoke a build. This applies to both the legacy service account and user-specified service accounts. Keep in mind the following security implications when using build triggers:

  * A user with no access to your Google Cloud project but with write access to the repository associated with build triggers in the project will have permissions to change the code being built. For example, users can indirectly invoke a trigger when they push new source code to a connected repository.

  * If you're using GitHub pull request triggers, any user with read access to the repository can submit a pull request, which may trigger a build that includes changes to the code in the pull request. You can disable this behavior by choosing the **Comment control** option when creating a GitHub pull request trigger. Selecting this option will ensure that the build is started only if a repository owner or a collaborator comments `/gcbrun`. For information on using **Comment control** with **GitHub triggers** , see [Creating GitHub triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-github-app-triggers).




## Limitations on the legacy Cloud Build service account

  * If you need to authenticate between services using an ID token, you must run your builds with a user-specified service account. You can't use the legacy Cloud Build service account to generate ID tokens.

For example, if you use serverless platform applications such as Cloud Run functions, Cloud Run, or App Engine, and you want to invoke your application from Cloud Build, this requires a user-specified service account configured with required permissions for service-to-service authentication.

For instructions, see [Authorize service-to-service access](https://docs.cloud.google.com/build/docs/securing-builds/authorize-service-to-service-access).

  * You can't add an IAM policy binding on the legacy service account. For example, you can't create an IAM policy binding that grants another service account the `roles/iam.serviceAccountTokenCreator`role _on_ the legacy service account.




## What's next

  * Learn about [user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).
  * Learn about [configuring access for the Cloud Build default service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account).
  * Learn about [configuring access to Cloud Build resources](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-to-resources).
  * Learn about [the permissions required to view build logs](https://docs.cloud.google.com/build/docs/securing-builds/store-view-build-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
