---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy/
title: Configure cleanup policies \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:19.308791+00:00
---

# Configure cleanup policies  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure cleanup policies Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry cleanup policies let you automate artifact retention and removal across your repositories. These processes can help you reduce artifact storage costs. Your policies can contain "delete" rules and "keep" rules based on a tag state, prefixes, or age, and you can preview changes with a dry run before applying them.

## Required roles

To get the permissions that you need to apply or remove cleanup policies, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on the repository project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to apply or remove cleanup policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to apply or remove cleanup policies:

  * `artifactregistry.repositories.update`
  * To delete artifacts that meet the criteria in a cleanup policy: `artifactregistry.versions.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The default role for the [Artifact Registry Service Agent](https://docs.cloud.google.com/artifact-registry/docs/ar-service-account) includes the permission `artifactregistry.versions.delete`, which is required to delete images that meet the criteria in a cleanup policy.

## Create a policy file

A policy file is a JSON file that defines your delete and keep policies. You can create a policy file by creating and editing a JSON file, then using the Google Cloud CLI to apply the policy, or by using the Google Cloud console. Delete policies specify conditions for deleting artifacts. Keep policies specify conditions to retain an artifact, or a number of recent versions to keep. You can't use conditions and most recent versions in the same keep policy.

### Create a delete policy

A delete policy lets you specify the minimum or maximum age for artifact deletion and additional filtering criteria to limit the policy to specific artifacts.

If you have certain artifacts that you don't want deleted for any reason, create a conditional keep policy, or a most recent versions keep policy as well as a delete policy. If an artifact matches the criteria in both the delete policy and the keep policy, the artifact is kept.

**Note:** Cleanup policies for Docker images don't delete images referenced by a parent manifest. If the parent manifest is deleted, then any related images are deleted when the cleanup policy is next run.

###  console 

You can create a delete policy for a new or existing repository.

To add a delete policy to an existing repository:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, select **Dry run** to test your new policy before committing to deleting any artifacts. For more information on seeing the results of the test, see dry run.

Once you are certain your policy is working as intended, edit your repository settings again, and select **Delete artifacts** to apply your cleanup policy and delete the selected artifacts.

  4. Click **Add a cleanup policy** and add the following:

     * **Name** : Give the cleanup policy a name. The name must be unique within the group of policies that you apply to a repository.
     * **Policy type** : Select **Conditional delete**.
     * **Tag state** : indicates if the policy should check for tagged artifacts or untagged artifacts. Artifacts are tagged when pushing or pulling an image to or from a repository. For more on Docker tags, see [Container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).

       * **Any tag state** : ignores tag state and applies to both tagged and untagged artifacts.
       * **Tagged** : only applies to tagged artifacts.
       * **Untagged** : only applies to untagged artifacts.

Formats that don't support tags are treated as `untagged`. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

For more information on tag state as it applies to cleanup policies, see the [TagState reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories#tagstate).

  5. The following are optional ways to define your delete policy:

     * **Tag prefixes** : is a comma-separated list of tag prefixes. For example, the prefixes `test`, and `staging` would match images with tags `testenv` and `staging-1.5`. `tagState` must be set to `TAGGED` to use tag prefixes.
     * **Version prefixes** : - is a comma-separated list of artifact version prefixes. For example `v1`, `v2` would match versions `v1.5`, `v2.0alpha`, and `v10.2`.
     * **Package prefixes** : is a list of artifact name prefixes. You can enter multiple prefixes by pressing `Enter` or `,` between the prefixes. For example `red, blue` would create two prefixes, `red` and `blue` and would match artifact names `red-team`, `redis`, and `bluebird`.
     * **Older than** : is the minimum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
     * **Newer than** : is the maximum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days.
  6. You can add more cleanup policies by clicking **Add a cleanup policy**.

  7. Click **Update**.

Your cleanup policy is applied to your repository. You can view your cleanup policies in the **Repository details** section by clicking **Show more**.




###  JSON 
    
    
    {
      "name": "DELETE_POLICY_NAME",
      "action": {"type": "Delete"},
      "condition": {
        "tagState": "TAG_STATUS",
        "tagPrefixes": ["TAG_PREFIXES"],
        "versionNamePrefixes": ["VERSION_PREFIXES"],
        "packageNamePrefixes": ["PACKAGE_PREFIXES"],
        "olderThan": "OLDER_THAN_DURATION",
        "newerThan": "NEWER_THAN_DURATION"
      }
    }
    

A delete policy must include a name, an action, and at least one condition.

`name`
    In the delete policy snippet, DELETE_POLICY_NAME is the name of the policy. The name must be unique within the group of policies that you apply to a repository.
`action`
    For a delete policy the value is `{"type": "Delete"}`.
`condition`
    Specify one or more of the following conditions:

  * `tagState`: TAG_STATUS indicates if the policy should check for tagged artifacts or untagged artifacts. Artifacts are tagged when pushing or pulling an image to or from a repository. Supported values are:

    * `tagged`: only applies to tagged artifacts.
    * `untagged`: only applies to untagged artifacts.
    * `any`: ignores tag state and applies to both tagged and untagged artifacts.

Formats that don't support tags are treated as `untagged`. If a repository has immutable tags enabled, tagged artifacts can't be deleted.

For more on Docker tags, see [Container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).

  * `tagPrefixes`: TAG_PREFIXES is a comma-separated list of tag prefixes. For example `"test", "staging"` would match images with tags `"testenv"` and `"staging-1.5"`. `tagState` must be set to `TAGGED` to use tag prefixes.

  * `versionNamePrefixes`: VERSION_PREFIXES is a comma-separated list of artifact version prefixes. For example `"v1", "v2"` would match versions `"v1.5"`, `"v2.0alpha"`, and `"v10.2"`.

  * `packageNamePrefixes`: PACKAGE_PREFIXES is a comma-separated list of artifact name prefixes. For example `"red", "blue"` would match artifact names `"red-team"`, `"redis"`, and `"bluebird"`.

  * `olderThan`: OLDER_THAN_DURATION is the minimum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.

  * `newerThan`: NEWER_THAN_DURATION is the maximum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days.




Artifact Registry performs dry runs and active runs of cleanup policies using a background job that runs periodically. Changes take effect within approximately one day. 

### Create a conditional keep policy

A conditional keep policy specifies criteria for retaining artifacts. Keep policies work with delete policies to keep artifacts that would be deleted according to the specifications of your delete policy, but that you want to keep. When an artifact matches the criteria for both a delete policy and a keep policy, the artifact is kept.

###  console 

You can create a keep policy for a new or existing repository.

To add a keep policy to an existing repository:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, select **Dry run** to test your new policy before committing to deleting any artifacts. You need to set at least one delete policy to view the results of your keep policy. For more information on seeing the results of the test, see dry run.

Once you are certain your policies are working as intended, edit your repository settings again, and select **Delete artifacts** to apply your cleanup policies and delete the selected artifacts.

  4. Click **Add a cleanup policy** and add the following:

     * **Name** : Give the cleanup policy a name. The name must be unique within the group of policies that you apply to a repository.
     * **Policy type** : Select **Conditional keep**.
     * **Tag state** : indicates if the policy should check for tagged artifacts or untagged artifacts. Artifacts are tagged when pushing or pulling an image to or from a repository. For more on Docker tags, see [Container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).

       * **Any tag state** : ignores tag state and applies to both tagged and untagged artifacts.
       * **Tagged** : only applies to tagged artifacts.
       * **Untagged** : only applies to untagged artifacts.

Formats that don't support tags are treated as `untagged`. If a repository has immutable tags enabled, tagged artifacts can't be deleted. For more information on tag state as it applies to cleanup policies, see the [TagState reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories#tagstate).

  5. The following are optional ways to define your keep policy:

     * **Tag prefixes** : is a comma-separated list of tag prefixes. For example, the prefixes `test`, and `staging` would match images with tags `testenv` and `staging-1.5`. `tagState` must be set to `TAGGED` to use tag prefixes.
     * **Version prefixes** : - is a comma-separated list of artifact version prefixes. For example `v1`, `v2` would match versions `v1.5`, `v2.0alpha`, and `v10.2`.
     * **Package prefixes** : is a comma-separated list of artifact name prefixes. For example `red, blue` would match artifact names `red-team`, `redis`, and `bluebird`.
**Caution:** If **Package prefixes** are specified, Artifact Registry will only keep the most recent versions of packages matching the specified package prefixes.
     * **Older than** : is the minimum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
     * **Newer than** : is the maximum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days.
  6. You can add more cleanup policies by clicking **Add a cleanup policy**.

  7. Click **Update**.

Your cleanup policy is applied to your repository.




###  JSON 

The format is similar to a delete policy. For a keep policy, the value for `action` is `{"type": "Keep"}`.
    
    
    {
      "name": "KEEP_POLICY_NAME",
      "action": {"type": "Keep"},
      "condition": {
        "tagState": "TAG_STATUS",
        "tagPrefixes": ["TAG_PREFIXES"],
        "versionNamePrefixes": ["VERSION_PREFIXES"],
        "packageNamePrefixes": ["PACKAGE_PREFIXES"],
        "olderThan": "OLDER_THAN_DURATION",
        "newerThan": "NEWER_THAN_DURATION"
      }
    }
    

Replace the following:

  * `KEEP_POLICY_NAME` with the cleanup policy a name. The name must be unique within the group of policies that you apply to a repository.
  * `TAG_STATUS` with the tag state, which indicates if the policy should check for tagged artifacts or untagged artifacts. Artifacts are tagged when pushing or pulling an image to or from a repository. For more on Docker tags, see [Container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).

The options are:

    * `tagged`: only applies to tagged artifacts.
    * `untagged`: only applies to untagged artifacts.
    * `any`: applies to all versions

Formats that don't support tags are treated as `untagged`. If a repository has immutable tags enabled, tagged artifacts can't be deleted. For more information on tag state as it applies to cleanup policies, see the [TagState reference](https://docs.cloud.google.com/artifact-registry/docs/reference/rest/v1/projects.locations.repositories#tagstate).

  * `TAG_PREFIXES` with a comma-separated list of tag prefixes. For example, the prefixes `test`, and `staging` would match images with tags `testenv` and `staging-1.5`. `tagState` must be set to `TAGGED` to use tag prefixes.

  * `VERSION_PREFIXES` with a comma-separated list of artifact version prefixes. For example `v1, v2` would match versions `v1.5`, `v2.0alpha`, and `v10.2`.

  * `PACKAGE_PREFIXES` with a comma-separated list of artifact name prefixes. For example `red, blue` would match artifact names `red-team`, `redis`, and `bluebird`.


**Caution:** If `packageNamePrefixes` is specified, Artifact Registry will only keep the most recent versions of packages matching the specified package prefixes.

  * `OLDER_THAN_DURATION` with the minimum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days. You can specify durations of seconds, minutes, hours, or days by appending `s`, `m`, `h`, or `d` respectively.
  * `NEWER_THAN_DURATION` with the maximum time since the version of an artifact was created in the repository, specified as a duration. For example, `30d` is 30 days.



Artifact Registry performs dry runs and active runs of cleanup policies using a background job that runs periodically. Changes take effect within approximately one day. 

### Create a keep policy for most recent versions

You can create a keep policy to keep a specific number of versions. You cannot use **Conditional keep** and **Keep most recent versions** criteria in the same keep policy.

Keep policies work with delete policies to keep artifacts that would be deleted according to the specifications of your delete policy, but that you want to keep. When an artifact matches the criteria for both a delete policy and a keep policy, the artifact is kept.

###  console 

You can create a keep most recent versions policy for a new or existing repository.

To add a keep most recent versions policy to an existing repository:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, select **Dry run** to test your new policy before committing to deleting any artifacts. You need to set at least one delete policy to view the results of your keep policy. For more information on seeing the results of the test, see dry run.

Once you are certain your policies are working as intended, edit your repository settings again, and select **Delete artifacts** to apply your cleanup policies and delete the selected artifacts.

  4. Click **Add a cleanup policy** and add the following:

     * **Name** : Give the cleanup policy a name. The name must be unique within the group of policies that you apply to a repository.
     * **Policy type** : Select **Keep most recent versions**.
  5. In the **Keep count** field, enter the number of versions of an artifact to keep in your repository.

  6. Optional: select **Package prefixes** to specify package prefixes to apply the keep policy to. For example `red, blue` would match artifact names `red-team`, `redis`, and `bluebird`.

**Caution:** If **Package prefixes** are specified, Artifact Registry will only keep the most recent versions of packages matching the specified package prefixes.
  7. You can add more cleanup policies by clicking **Add a cleanup policy**.

  8. Click **Update**.

Your cleanup policy is applied to your repository. You can view your cleanup policies in the **Repository details** section by clicking **Show more**.




###  JSON 

The format is similar to a delete policy. For a keep policy, the value for `action` is `{"type": "Keep"}`.

A keep policy for retaining a specific number of versions has a `mostRecentVersions` section instead of a `condition` section.
    
    
    {
      "name": "KEEP_POLICY_NAME",
      "action": {"type": "Keep"},
      "mostRecentVersions": {
        "packageNamePrefixes": ["PACKAGE_PREFIXES"],
        "keepCount": MINIMUM_NUMBER
      }
    }
    

Replace the following:

  * `KEEP_POLICY_NAME` with a name for your keep policy. The name must be unique within the group of policies that you apply to a repository.
  * `PACKAGE_PREFIXES` with the optional package prefixes to apply the keep policy to. For example `red, blue` would match artifact names `red-team`, `redis`, and `bluebird`.

**Caution:** If `packageNamePrefixes` is specified, Artifact Registry will only keep the most recent versions of packages matching the specified package prefixes.

  * `MINIMUM_NUMBER` with the number of versions of an artifact to keep in your repository.



To apply the keep policy to all packages in your repository, omit the `packageNamePrefixes` condition. The specified number of recent versions of each package in your repository are kept.

Artifact Registry performs dry runs and active runs of cleanup policies using a background job that runs periodically. Changes take effect within approximately one day. 

### Example policy file

The following policy file example has one delete policy and two keep policies.

  * The `delete-prerelease` policy removes artifact versions 30 days after upload if the artifact starts with the string `alpha` or `v0`.
  * The `keep-tagged-release` policy retains artifacts tagged with the prefix `release` that have a filename starting with `webapp` or `mobile`.
  * The `keep-minimum-versions` policy retains the five most recent versions of artifacts that have a filename starting with `webapp`, `mobile`, or `sandbox`.


    
    
    [
      {
        "name": "delete-prerelease",
        "action": {"type": "Delete"},
        "condition": {
          "tagState": "tagged",
          "tagPrefixes": ["alpha", "v0"],
          "olderThan": "30d"
        }
      },
      {
        "name": "keep-tagged-release",
        "action": {"type": "Keep"},
        "condition": {
          "tagState": "tagged",
          "tagPrefixes": ["release"],
          "packageNamePrefixes": ["webapp", "mobile"]
        }
      },
      {
        "name": "keep-minimum-versions",
        "action": {"type": "Keep"},
        "mostRecentVersions": {
          "packageNamePrefixes": ["webapp", "mobile", "sandbox"],
          "keepCount": 5
        }
      }
    ]
    

## Test your policies with a dry run

To test your cleanup policies, you can set your cleanup policy to dry run in the console, or run the `gcloud artifacts set-cleanup-policies` command with the `--dry-run` flag.

To analyze the effect of your cleanup policies you can view the Artifact Registry Data access [audit logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging). To receive Data Access audit logs for cleanup policies, you must explicitly enable the **data write** type of data access audit logs for the Artifact Registry service. To enable data access audit logs, see [Enable audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable).

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, select **Dry run**.

  4. Click **Add a cleanup policy** and configure the options for your **Conditional delete** , **Conditional keep** , or **Keep most recent versions** policies.

  5. Click **Update**.




When a delete policy results in a `BatchDeleteVersions` action, the parameter `validateOnly` evaluates to `"true"`.

Artifact Registry performs dry runs and active runs of cleanup policies using a background job that runs periodically. Changes take effect within approximately one day. 

Wait at least a day before you query audit logs for the dry run.

To query audit logs for dry runs of your cleanup policies, run the following command:
    
    
    gcloud logging read 'protoPayload.serviceName="artifactregistry.googleapis.com" AND protoPayload.request.parent="projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY/packages/-" AND protoPayload.request.validateOnly=true' \
        --resource-names="projects/PROJECT_ID" \
        --project=PROJECT_ID
    

The output resembles the following:
    
    
    insertId: qwe123ty3
    logName: projects/my-project/logs/cloudaudit.googleapis.com%2Fdata_access
    operation:
      first: true
      id: projects/my-project/locations/us-west1/operations/12345abc-fb9b-4b6f-b02c-9a397ee807d4
      producer: artifactregistry.googleapis.com
    protoPayload:
      '@type': type.googleapis.com/google.cloud.audit.AuditLog
      authenticationInfo:
        principalEmail: service-774919394028@gcp-sa-staging-artreg.iam.gserviceaccount.com
      authorizationInfo:
      - granted: true
        permission: artifactregistry.versions.delete
        resource: projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/-
        resourceAttributes: {}
      methodName: google.devtools.artifactregistry.v1.ArtifactRegistry.BatchDeleteVersions
      request:
        '@type': type.googleapis.com/google.devtools.artifactregistry.v1.BatchDeleteVersionsRequest
        names:
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:4bb3756e4e75dfbc3ced87521ed62b26d16fb4e17993ae6877165f2b6551fb55
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:e8185538b50df953529b300be4963b2c21158808becac7aa0d610f61de8ba701
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:7f7fb0a9453da49f831fe92eb8b1751be13acefe1bbd44cc3f0d63d41c422246
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:84ac871a34560b39dd7bde57b4d333f18a7e8c1b61c8d350c1fefeb1fcd2b3ac
    parent: projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/-
        validateOnly: true
      requestMetadata:
        callerIp: private
        callerSuppliedUserAgent: stubby_client
        destinationAttributes: {}
        requestAttributes:
          auth: {}
          time: '2023-05-26T04:31:21.909465579Z'
      resourceName: projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/-
      serviceName: artifactregistry.googleapis.com
    receiveTimestamp: '2023-05-26T04:31:22.641338594Z'
    resource:
      labels:
        method: google.devtools.artifactregistry.v1.ArtifactRegistry.BatchDeleteVersions
        project_id: my-project
        service: artifactregistry.googleapis.com
      type: audited_resource
    severity: INFO
    timestamp: '2023-05-26T04:31:21.909004200Z'
    

###  gcloud 

To do a dry run with your cleanup policies, run the following command:
    
    
    gcloud artifacts repositories set-cleanup-policies REPOSITORY \
        --project=PROJECT_ID \
        --location=LOCATION \
        --policy=POLICY_FILE \
        --dry-run
    

Replace the following:

  * `REPOSITORY` with the name of the repository.
  * `PROJECT_ID` with the ID of your Google Cloud project.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 



When a delete policy results in a `BatchDeleteVersions` action, the parameter `validateOnly` evaluates to `"true"`.

Artifact Registry performs dry runs and active runs of cleanup policies using a background job that runs periodically. Changes take effect within approximately one day. 

Wait at least a day before you query audit logs for the dry run.

To query audit logs for dry runs of your cleanup policies, run the following command:
    
    
    gcloud logging read 'protoPayload.serviceName="artifactregistry.googleapis.com" AND protoPayload.request.parent="projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY/packages/-" AND protoPayload.request.validateOnly=true' \
        --resource-names="projects/PROJECT_ID" \
        --project=PROJECT_ID
    

The output resembles the following:
    
    
    insertId: qwe123ty3
    logName: projects/my-project/logs/cloudaudit.googleapis.com%2Fdata_access
    operation:
      first: true
      id: projects/my-project/locations/us-west1/operations/12345abc-fb9b-4b6f-b02c-9a397ee807d4
      producer: artifactregistry.googleapis.com
    protoPayload:
      '@type': type.googleapis.com/google.cloud.audit.AuditLog
      authenticationInfo:
        principalEmail: service-774919394028@gcp-sa-staging-artreg.iam.gserviceaccount.com
      authorizationInfo:
      - granted: true
        permission: artifactregistry.versions.delete
        resource: projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/-
        resourceAttributes: {}
      methodName: google.devtools.artifactregistry.v1.ArtifactRegistry.BatchDeleteVersions
      request:
        '@type': type.googleapis.com/google.devtools.artifactregistry.v1.BatchDeleteVersionsRequest
        names:
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:4bb3756e4e75dfbc3ced87521ed62b26d16fb4e17993ae6877165f2b6551fb55
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:e8185538b50df953529b300be4963b2c21158808becac7aa0d610f61de8ba701
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:7f7fb0a9453da49f831fe92eb8b1751be13acefe1bbd44cc3f0d63d41c422246
        - projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/docker-load-thursday/versions/sha256:84ac871a34560b39dd7bde57b4d333f18a7e8c1b61c8d350c1fefeb1fcd2b3ac
    parent: projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/-
        validateOnly: true
      requestMetadata:
        callerIp: private
        callerSuppliedUserAgent: stubby_client
        destinationAttributes: {}
        requestAttributes:
          auth: {}
          time: '2023-05-26T04:31:21.909465579Z'
      resourceName: projects/my-project/locations/us-west1/repositories/docker-test-dryrun/packages/-
      serviceName: artifactregistry.googleapis.com
    receiveTimestamp: '2023-05-26T04:31:22.641338594Z'
    resource:
      labels:
        method: google.devtools.artifactregistry.v1.ArtifactRegistry.BatchDeleteVersions
        project_id: my-project
        service: artifactregistry.googleapis.com
      type: audited_resource
    severity: INFO
    timestamp: '2023-05-26T04:31:21.909004200Z'
    

## Apply policies to a repository

To use your cleanup policies defined in a local JSON file, apply them to repositories where you want Artifact Registry to handle automatic deletion of artifact versions by using the gcloud CLI.

To apply cleanup policies set to **Dry run** in the console, set the policy to **Delete artifacts**.

You can only apply cleanup policies to standard repositories. You cannot apply cleanup policies to:

  * A Google Cloud project.


  * [Virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo).



###  console 

To apply cleanup policies:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, select **Delete artifacts**.

Artifact Registry deletes and retains artifacts that match your policies using a background job that runs periodically. Changes should take effect within approximately one day.




###  gcloud 

To apply cleanup policies, run the following command in the directory with your cleanup policy file.
    
    
    gcloud artifacts repositories set-cleanup-policies REPOSITORY \
        --project=PROJECT_ID \
        --location=LOCATION \
        --policy=POLICY_FILE \
        --no-dry-run
    

Replace the following:

  * `REPOSITORY` with the name of the repository.
  * `PROJECT_ID` with the ID of your Google Cloud project.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `POLICY_FILE` is the name of the file with the cleanup policy.



The `--no-dry-run` flag disables dry run functionality for the repository.

For example, the following command applies policies in `policy.json` to the repository `my-repo` in the region `us-west1` in the project `my-project`.
    
    
    gcloud artifacts repositories set-cleanup-policies my-repo \
        --project=my-project \
        --location=us-west1 \
        --policy=policy.json
    

Artifact Registry deletes and retains artifacts that match your policies using a background job that runs periodically. Changes should take effect within approximately one day.

## Update a policy

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, click the name of the policy you want to set to modify.

  4. Edit the cleanup policy and click **Update**.

Your cleanup policy is applied to your repository.




###  gcloud 

To update existing policies, edit the settings in your policy file and then run the following command to apply the policies again.
    
    
    gcloud artifacts repositories set-cleanup-policies REPOSITORY \
        --project=PROJECT_ID \
        --location=LOCATION \
        --policy=POLICY_FILE \
        --no-dry-run
    

Replace the following:

  * `REPOSITORY` with the name of the repository.
  * `PROJECT_ID` with the ID of your Google Cloud project.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `POLICY_FILE` is the name of the file with the cleanup policy.



The `--no-dry-run` flag disables dry run functionality for the repository.

## List repository cleanup policies

You can view the cleanup policies associated with a repository.

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository you want to view.

  3. In the **Repository details** section, click **Show more**.

The cleanup policies names are displayed.

  4. To view or edit the details of the repository's cleanup policies, click **Edit Repository**.

Your existing cleanup policies details are listed in the **Cleanup policies** section.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts repositories list-cleanup-policies REPOSITORY \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `REPOSITORY` with the name of the repository.
  * `PROJECT_ID` with the ID of your Google Cloud project.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 



## Remove a policy from a repository

Remove a cleanup policy from a repository when you no longer want Artifact Registry to automatically delete artifact versions.

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repositories list, select the repository and click **Edit Repository**.

  3. In the **Cleanup policies** section, hover over the name of the policy you want to delete.

  4. Click the **Delete** icon.

  5. Click **Update**.

The cleanup policy is deleted.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts repositories delete-cleanup-policies REPOSITORY \
        --policynames=POLICY_NAMES \
        --project=PROJECT_ID \
        --location=LOCATION
    

Replace the following:

  * `REPOSITORY` is the name of the repository.
  * `PROJECT_ID`is the ID of your Google Cloud project.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `POLICY_NAMES` is a comma-separated list of policy names for the policies you want to remove.



For example, the following command removes a policy named `delete-test` from the repository `my-repo` in the region `us-west1` in the project `my-project`:
    
    
    gcloud artifacts repositories delete-cleanup-policies my-repo \
        --policynames=delete-test \
        --project=my-project \
        --location=us-west1
    

## Audit log entries for cleanup policies

To view cleanup policy log entries in Cloud Logging, you must [enable](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) `DATA_WRITE` logging.

When you set a cleanup policy on a repository, the operation is logged as an update to the repository (`UpdateRepository` operation).

When Artifact Registry deletes a version of an artifact, it logs the event in the [Cloud Logging Data Access logs](https://docs.cloud.google.com/artifact-registry/docs/audit-logging). The log entries show that the Artifact Registry service account performed the deletion. The Artifact Registry service account ID is in the format `service-PROJECT-NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
