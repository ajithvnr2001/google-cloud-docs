---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/about-rotation-schedules-rs/
title: About secret rotation \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:10.260795+00:00
---

# About secret rotation  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/about-rotation-schedules-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  About secret rotation Stay organized with collections  Save and categorize content based on your preferences. 

Secret rotation is the process of periodically updating or replacing sensitive information (secrets) such as passwords, API keys, or encryption keys. Rotating secrets helps to miminimize the risk of unauthorized access or misuse of secrets, particularly if they have been compromised or leaked.

Periodic rotation helps in the following ways:

  * Limits the impact in the case of a leaked secret.

  * Ensures that individuals who no longer require access to a secret aren't able to use old secret values.

  * Minimizes the risk of service disruptions if you need to rotate secrets urgently.




Secret Manager has a concept of secrets, secret versions, and [rotation schedules](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets), which provide a foundation for building workloads that support rotated secrets.

This page provides recommendations for rotating secrets stored in Secret Manager. You'll learn how to do the following:

  * [Bind a secret version to your application](https://docs.cloud.google.com/secret-manager/regional-secrets/about-rotation-schedules-rs#bind-a-secret-version-to-your-application)

  * [Rotate secrets efficiently](https://docs.cloud.google.com/secret-manager/regional-secrets/about-rotation-schedules-rs#rotate-your-secret)




Before you begin, we recommend that you read the [platform overview](https://docs.cloud.google.com/docs/overview) to understand the overall Google Cloud landscape. We also recommend that you read the [Secret Manager product overview](https://docs.cloud.google.com/secret-manager/regional-secrets/overview-rs).

## Bind a secret version to your application

A secret in Secret Manager can have multiple secret versions. Secret versions contain the immutable payload (the actual secret byte string) and are ordered and numbered. To rotate a secret, add a new secret version to an existing secret.

The most recently added secret version on a secret can be referenced using the `latest` alias. The `latest` alias, while convenient for development, can be problematic for some production workloads since a bad value could be immediately rolled out and result in a service-wide outage. Alternate methods for binding to a secret version are described in the following scenarios.

### Gradual rollouts

Gradual rollouts are a guiding principle for the following scenarios. By choosing a slower secret rollout, there is lower risk of breakage, but also a slower time to recovery. Some secrets can be invalidated in external systems (such as APIs or databases that track valid secret values) that might or might not be in your control and recovery in these cases requires a rollout.

It's possible for a bad secret to be rolled out during either manual or automatic rotation. A strong rotation workflow should be able to automatically detect the breakage (HTTP error rates, for example) and rollback to use the older secret version (via a prior configuration deployment).

The rollout of the new secret version depends on how secrets are bound to your application.

### Approach 1: Resolve during an existing release process

Resolve and bind your secret version with your application's release. For most deployments, this involves resolving the latest secret version into the full secret version resource name and rolling it out with the application as a flag or in a configuration file. We recommend resolving the secret version name at rotation time, storing the resource name somewhere durable (for example, commit to Git), and pulling the version name into the deployment configuration during the push to prevent blocked deployments.

At application startup, call Secret Manager with the specific secret version name to access the secret value.

This approach has the following benefits:

  * Your application uses the same secret version across restarts, increasing predictability and reducing operational complexity.

  * Existing change management processes for rollouts and rollbacks can be reused for secret rotation and secret version deployment.

  * The value can be rolled out gradually, reducing the impact of deploying bad values.


**Note:** Resolving the latest version at deployment might block deployments if there is a bad secret version at latest. Resolving issues at deployment might be less isolated or reproducible as rollout success depends on the secret version state in Secret Manager. If the previous secret version is working, create a new secret version with the same value and wait for it to roll out. This is essentially a "roll forward" and requires `secretmanager.versions.access` permission on the secret to copy the value from the old to new version. 

### Approach 2: Resolve on application startup

Fetch the latest secret payload on application startup and continue to use the secret for the duration of the application.

The advantage of this approach is that it does not require modifying the CI/CD pipeline to resolve secret versions, but if a bad secret is rolled out then the application fails to start as instances restart or the service scales-up and might cascade into a service outage.

### Approach 3: Resolve continuously

Poll for the latest secret version continuously in the application and use the new secret value immediately.

This approach risks immediate, service-wide outage as there's no gradual adoption of the new secret value.

## Rotate your secret

If your secret can be dynamically updated (for example, if the external system validating the secret provides an Admin API), we recommend setting up a rotation job that runs periodically. The general steps are outlined in the following section with Cloud Run as a sample compute environment.

### Configure a rotation schedule on your secret

Set up a [rotation schedule](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets) for your secret. Pub/Sub topics must be configured on the secret to receive notifications when it's time to rotate your secret. See the [Event Notifications](https://docs.cloud.google.com/secret-manager/regional-secrets/notifications-regional-secrets) guide for configuring topics on your secrets.

### Launch a Cloud Run to create a new secret version

[Create and configure](https://docs.cloud.google.com/run/docs/tutorials/pubsub) a Cloud Run service to receive rotation notifications and execute rotation steps:

  1. Obtain or create a new secret in the external system (for example, database, API provider).

Ensure that this _doesn't_ invalidate existing secrets so that existing workloads are not affected.

  2. Update Secret Manager with the new secret.

[Create a new secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs) in Secret Manager. This also updates the `latest` alias to point to the newly created secret.




#### Retries and Concurrency

Since your rotation process could be terminated at any time, your Cloud Run service must be able to restart the process from where it left off (it must be reentrant).

We recommend [configuring retries](https://docs.cloud.google.com/pubsub/docs/retry-requests) so that failed or interrupted rotations can be re-executed. Additionally, configure the [max concurrency](https://docs.cloud.google.com/run/docs/about-concurrency) and [max instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) on your Cloud Run service to minimize the probability of concurrent rotation executions interfering with each other.

In order to build a reentrant rotation function, you might find it useful to save state to allow the rotation process to resume. There are two Secret Manager features that help with this:

  * Use labels on secrets to save state during rotation. Add a label to the secret to track the number of the last successfully added version during the rotation workflow (for example, `ROTATING_TO_NEW_VERSION_NUMBER=3`). Once the rotation has completed, remove the rotation tracking label.

  * Use etags to verify that other processes are not concurrently modifying the secret during the rotation workflow. Learn more about [secret and secret version etags](https://docs.cloud.google.com/secret-manager/regional-secrets/etags-regional-secrets).


**Note:** Etags for secrets and secret versions are independent of each other. In other words, adding a new version does not modify the etag of the parent secret. 

#### Identity and Access Management permissions

Your rotation process requires the `secretmanager.versions.add` permission to add a new secret version, and might require the `secretmanager.versions.access` permission to read the previous secret version.

Your rotation process requires the `secretmanager.versions.add` permission to add a new secret version, and might require the `secretmanager.versions.access` permission to read the previous secret version.

The default Cloud Run service account has the [Editor role](https://docs.cloud.google.com/run/docs/securing/service-identity#runtime_service_account), which includes permission to add, but not access secret versions. To follow the principle of least privilege, we recommend **not** using the default service account. Instead, set up a [separate service account](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) for your Cloud Run service with the [Secret Manager roles](https://docs.cloud.google.com/secret-manager/regional-secrets/access-control-rs) granted as necessary (might be one or multiple of):

  * `roles/secretmanager.secretVersionAdder`

  * `roles/secretmanager.secretVersionManager`

  * `roles/secretmanager.secretAdmin`

  * `roles/secretmanager.secretAccessor`




### Roll out the new secret version to workloads

Now that a new, valid secret version has been registered with the external system and is stored in Secret Manager, roll it out to your application. This rollout varies based on your approach to secret binding and generally does not require manual intervention.

### Clean up old secret versions

Once all applications are rotated off the old secret version, it can be safely cleaned up. The cleanup process depends on the type of secret, but generally:

  1. Ensure that the new secret version has been fully rolled out to all applications.

  2. Disable the old secret version in Secret Manager and verify that applications don't break (wait a reasonable amount of time to allow a human to intervene if disabling breaks a consumer).

  3. Remove or unregister the old secret version from the external system.

  4. Destroy the old secret version in Secret Manager




## What's next

  * [Create rotation schedules](https://docs.cloud.google.com/secret-manager/regional-secrets/rotate-regional-secrets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
