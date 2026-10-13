---
url: https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard/
title: Configure artifact guard policies \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:14.895498+00:00
---

# Configure artifact guard policies  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/configure-artifact-guard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Configure artifact guard policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions.  Artifact guard and CI/CD integration will be shut down on October 30, 2026. 

This document describes how to create and manage artifact guard policies. For an overview of the service, see the [Artifact guard overview](https://docs.cloud.google.com/security-command-center/docs/artifact-guard-overview).

## Before you begin

Before you can create an artifact guard policy, you must enable artifact guard in Security Command Center and obtain the required Identity and Access Management (IAM) role.

Additionally, familiarize yourself with [artifact guard limits](https://docs.cloud.google.com/security-command-center/quotas#artifact-guard-limits).

If you plan to use the gcloud CLI to manage policies or CI/CD connectors, review the gcloud CLI prerequisites.

### Enable artifact guard

Follow the steps in [Configure Security Command Center services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) to enable artifact guard.

### Required role

To get the permissions that you need to use artifact guard, ask your administrator to grant you the following Identity and Access Management (IAM) role on your project or organization:

  * Artifact Scan Guard Evaluation Admin (`roles/artifactscanguard.policyEvaluator`)



This role can be granted using the Google Cloud console or by running the following gcloud CLI command:

###  project 
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
          --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
          --role="roles/artifactscanguard.policyEvaluator"
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email address of your service account.



###  organization 
    
    
      gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
          --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
          --role="roles/artifactscanguard.policyEvaluator"
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `SERVICE_ACCOUNT_EMAIL`: the email address of your service account.



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For more artifact guard roles, see [Artifact guard roles and permissions](https://docs.cloud.google.com/security-command-center/docs/artifact-guard-access-control).

### gcloud CLI prerequisites

To manage policies or CI/CD connectors using the gcloud CLI, make sure that your environment meets the following requirements:

  * Your gcloud CLI version is 559.0.0 or higher.
  * Your project is set as the configuration project.



To update the gcloud CLI and set your project, run the following commands:
    
    
    gcloud components update --version=559.0.0
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with your project ID.

## Create a policy

### Console

To create an artifact guard policy in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Security > Rules**, and click **Create artifact guard policy** or **Create policy**.
  2. Enter a policy ID and a description for the policy, then click **Continue**.
  3. Select policy scopes and actions: 
     * **CI/CD platform**
       * **Select connector(s)** : Select the connectors to associate with this policy. The scanner evaluates this policy for every CI/CD build associated with the selected connectors. **Tip:** If you have not already created a connector, click **Manage connectors** to open the [CI/CD integration](https://docs.cloud.google.com/security-command-center/docs/configure-cicd-integration) page. After you create a connector to your CI/CD environment, return to the **Create policy** page and click **Refresh** to update your connector options. 
       * **Policy action** : Select the action to take when the policy is violated. 
         * **Block builds failing the policy** : If the policy fails, the build is blocked.
         * **Pass builds with alerts** : Connected build pipelines display the CI/CD scanner policy evaluation results.
     * **Registry**
       * **Container Analysis Projects** : This setting applies only to organizations, not projects. Add the Google Cloud projects where you want to apply this policy.
       * **Artifact Registry repositories** : Select the repositories where you want to apply this policy. These must be valid Artifact Registry repositories. If left blank, artifact guard applies the policy to all repositories.
       * **Policy Action** : Select the action to take when the policy is violated. 
         * **Audit only** : Artifact guard evaluates the policy and logs any violations for auditing purposes without blocking the resource.
         * **Admission control** : If a violation occurs during policy evaluation, admission control blocks the resource from being deployed. 
           * **Set Binary Authorization policies to dry run mode** : For more information about dry-run mode, see [Enable dry-run mode](https://docs.cloud.google.com/binary-authorization/docs/enabling-dry-run).
           * **Binary Authorization Projects** : This setting applies only to organizations, not projects. Add the Google Cloud projects where you want to apply admission control.
           * **GKE clusters** : If left blank, admission control applies to all GKE clusters.
           * **Override Binary Authorization policies** : Select this checkbox to update the Binary Authorization policy for admission control.
     * **Runtime**
       * **Runtime projects** : This setting applies only to organizations, not projects. Add runtime projects that contain GKE clusters.
       * **GKE clusters** : Select the GKE clusters where you want to apply this policy. If left blank, artifact guard applies the policy to all GKE clusters in the selected projects.
  4. Define the policy rule. A policy rule is a set of criteria that determines which vulnerabilities and packages are allowed in your environment. A policy rule includes the following: 
     * **Severity threshold** : Set the minimum severity level for a vulnerability to be included in policy evaluation. Vulnerabilities must meet or exceed this threshold to be included. 

For example, configuring the rule to **Medium** includes all **Medium** , **High** , and **Critical** vulnerabilities in the assessment.

     * **Vulnerability count threshold** : Sets the maximum number of allowed vulnerabilities after other policy filters are applied. The policy is violated only if the count of these specific, filtered vulnerabilities exceeds the limit. 

For example, if you set a Severity threshold of **High** , exclude vulnerabilities with unavailable fixes, and set a count threshold of five, a build fails if it contains more than five fixable vulnerabilities that are rated **High** or **Critical**.

     * **Vulnerability status** : Specify whether to include only vulnerabilities for which a fix is available. This allows prioritized remediation by targeting all vulnerabilities or only fixable ones.
     * **Exceptions and Restrictions** : These sections let you create specific allowances or blocks that override the general policy. 
       * **Exempted CVEs** : Specify CVEs that are deemed acceptable in your environment for a specified duration. This is helpful for implementing temporary workarounds. You can set an expiration date for these exceptions. After this date, the vulnerability is no longer permitted and causes the policy to fail.
       * **Restricted CVEs** : Specify CVEs to always block, regardless of their severity rating. This is particularly useful for denoting vulnerabilities that present a unique risk to your specific application or infrastructure.
       * **Allowed packages** : List packages considered secure. Package version can be defined; otherwise, all versions are allowed.
       * **Restricted packages** : List packages to restrict. Restricted packages cause the policy to fail. Package version can be defined; otherwise, all versions are restricted.
  5. Click **Create**.



Available artifact guard policies are listed in the table on the **Rules** page.

### gcloud CLI

To create a policy using the gcloud CLI, run the following command:
    
    
    gcloud alpha scc artifact-guard policies create \
        (POLICY_ID --location=LOCATION (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER)) \
        --policy-file-path=PATH_TO_FILE

Replace the following:

  * POLICY_ID: An identifier for the policy (for example, `my-policy`).
  * LOCATION: The Security Command Center location where your data is stored. Only `global` is supported.
  * ORGANIZATION_ID: The organization ID.
  * PROJECT_NUMBER: The numeric project number.
  * PATH_TO_FILE: The local path to the YAML document containing the policy definition. See the YAML file section of this document for details on the YAML file structure.



## Update a policy

### Console

To update an artifact guard policy in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Security > Rules**.
  2. In the rules table, click the name of the policy that you want to edit.
  3. On the policy details page, click **Edit** or modify the fields that you want to update, such as scope, vulnerability rules, or enablement state.
  4. Click **Save** or **Update**.



### gcloud CLI

To view existing policies and update them using the gcloud CLI, use the following commands:

#### List policies
    
    
    gcloud alpha scc artifact-guard policies list PARENT

Replace the following:

PARENT: An organization or project. Acceptable formats for the parent resource include: 

  * `organizations/ORGANIZATION_ID/locations/LOCATION`
  * `projects/PROJECT_NUMBER/locations/LOCATION`



#### Describe a policy
    
    
    gcloud alpha scc artifact-guard policies describe \
        (POLICY --location=LOCATION (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER))

Replace the following:

POLICY: The complete identifier for the policy, in one of the following formats: 

  * `organizations/ORGANIZATION_ID/locations/LOCATION/policies/POLICY_ID`
  * `projects/PROJECT_NUMBER/locations/LOCATION/policies/POLICY_ID`
  * `POLICY_ID --location=LOCATION (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER)`



#### Update a policy
    
    
    gcloud alpha scc artifact-guard policies update \
        (POLICY --location=LOCATION (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER)) \
        --policy-file-path=PATH_TO_FILE [--allow-missing] \
        [--update-mask=UPDATE_MASK]

`--allow_missing` is an optional flag. When this flag is included, a new policy is created if the specified policy doesn't exist.

Replace the following:

UPDATE-MASK: A comma-separated list of fields to update. An empty string or `*` means a full policy update. Valid fields for the update mask include the following: 

  * `display_name`
  * `description`
  * `scope`
  * `enablement_state`
  * `vulnerability_policy`
  * `annotations`



## Policy validation

Artifact guard validates policy definitions when you create or update policies. If validation fails, artifact guard rejects the request and provides a detailed error message.

## Delete a policy

**Note:** Active policies cannot be deleted. To delete an active policy, first edit the policy to set its enablement state to **Inactive**.

### Console

To delete an artifact guard policy in the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to **Security > Rules**.
  2. In the rules table, click more_vert next to the policy that you want to delete and select **Delete**.
  3. Follow the confirmation prompts to delete the policy. Click **Cancel** to abort.



### gcloud CLI

To delete a policy using the gcloud CLI, run the following command:
    
    
    gcloud alpha scc artifact-guard policies delete \
        (POLICY --location=LOCATION (--organization=ORGANIZATION_ID | --project=PROJECT_NUMBER)) \
        [--etag=ETAG]

Replace the following:

ETAG: An optional entity tag used for concurrency control. If you provide a value, the request only proceeds if the resource's `etag` matches. 

## YAML file

When you use the gcloud CLI to create or manage an artifact guard policy, the YAML file must follow this template:
    
    
      displayName: <Human-readable display name for the policy>
      description: <Description of the policy>
    
      vulnerabilityPolicy: # (at least one of these rules must be defined)
        exemptedCves:
          - id: <cve-id-1>
            gracePeriodExpirationTime: <optional-grace-period-expiration-time>
          - id: <cve-id-2>
            gracePeriodExpirationTime: <optional-grace-period-expiration-time>
    
        maxAllowedSeverity: <The maximum severity allowed in the detected
        vulnerabilities. The severity values can be LOW, MEDIUM, HIGH, CRITICAL>
    
        maximumAllowedVulnerabilities: <The maximum number of vulnerabilities that
        can be detected>
    
        excludeUnfixable: <Whether to exclude the vulnerabilities without an
        available fix from the purview of the policy evaluation>
    
        restrictedCves:
          - <restricted-cve-id-1>
          - <restricted-cve-id-2>
    
        allowedPackages:
          - name: <allowed_package_name_1>
            version: <optional_version_of_allowed_package_1. If unspecified, all the
            versions of the package are allowed>
          - name: <allowed_package_name_2>
            version: <optional_version_of_allowed_package_2>
    
        restrictedPackages:
          - name: <restricted_package_name_1>
            version: <optional_version_of_restricted_package_1. If unspecified, all
            the versions of the package are restricted>
          - name: <restricted_package_name_2>
            version: <optional_version_of_restricted_package_2>
    
      scope:
        pipeline:
          connectorIds:
            - <connector_id_1>
            - <connector_id_2>
          enforcementAction: <action to take in case the policy evaluation fails.
          The supported values are AUDIT_ONLY or BLOCK_BUILD>
    
        registry:
          projectIds:
            - <project_id_1>
          garRepositoryNamePatterns:
            - <repository_name_pattern_1>
          imageNamePatterns:
            - <image_name_pattern_1>
          enforcementAction: <AUDIT_ONLY or ADMISSION_CONTROL>
          admissionControl:
            deploymentProjectIds:
              - <project_id_1>
            gkeClusterNames:
              - <cluster_name_1>
            dryRun: <bool>
            overrideBinauthzPolicy: <bool>
    
        runtime:
            deploymentProjectIds:
              - <project_id_1>
            gkeClusterNames:
              - <cluster_name_1>
            dryRun: <bool>
            overrideBinauthzPolicy: <bool>
            enforcementAction: <AUDIT_ONLY or BLOCK_DEPLOYMENT>
    
      enablementState: <The enablement state of the policy. The supported values are
      ACTIVE, INACTIVE>
    

The following is a sample artifact guard policy file:
    
    
      displayName: 'A sample policy'
      description: Vulnerability Policy
      vulnerabilityPolicy:
        exemptedCves:
          - id: CVE-2022-40897
            gracePeriodExpirationTime: '2026-09-10T18:58:08Z'
          - id: CVE-2024-6345
        maxAllowedSeverity: MEDIUM
        maximumAllowedVulnerabilities: 5
        excludeUnfixable: true
        restrictedCves:
          - CVE-2013-4392
          - CVE-2024-4143
        allowedPackages:
          - name: systemd
            version: '257.7'
          - name: util-linux
        restrictedPackages:
          - name: ncurses
            version: 6.5+20250216
          - name: setuptools
      scope:
        pipeline:
          connectorIds:
            - organizations/123/locations/global/connectors/demoConnector
          enforcementAction: BLOCK_BUILD
        registry:
          projectIds:
            - projects/my-registry-project-id
            - projects/another-registry-project
          garRepositoryNamePatterns:
            - us-west1-docker.pkg.dev/my-registry-project-id/my-repo
            - gcr.io/team-a/internal-artifacts
          imageNamePatterns:
            - my-repo/service-a:.*
            - my-repo/service-b:v1\..*
          enforcementAction: ADMISSION_CONTROL
          admissionControl:
            deploymentProjectIds:
              - projects/my-deployment-project
            gkeClusterNames:
              - //container.googleapis.com/projects/my-deployment-project/locations/us-central1/clusters/gke-cluster-a
              - //container.googleapis.com/projects/my-deployment-project/locations/us-central1/clusters/gke-cluster-b
            dryRun: true
            overrideBinauthzPolicy: true
        runtime:
          deploymentProjectIds:
            - projects/my-deployment-project
          gkeClusterNames:
            - //container.googleapis.com/projects/my-deployment-project/locations/us-central1/clusters/gke-cluster-a
            - //container.googleapis.com/projects/my-deployment-project/locations/us-central1/clusters/gke-cluster-b
          dryRun: false
          overrideBinauthzPolicy: false
          enforcementAction: BLOCK_DEPLOYMENT
      enablementState: ACTIVE
    

## Troubleshooting

This section outlines artifact guard policy fields and common errors with their resolutions.

#### General policy fields

**Name** | **Description** | **Required** | **Constraints** | **Sample Values**  
---|---|---|---|---  
**Parent** | Defines the policy's application scope. | Yes | Only policies in the `global` location are supported. | 

  * `organizations/123/locations/global`
  * `projects/123/locations/global`

  
**Policy ID** | A unique identifier for the policy. | Yes | Up to 100 characters. Must start with a letter, end with an alphanumeric character, and only contain letters, numbers, hyphens, or underscores. | `my-policy-1`  
**Display Name** | A human-readable name for the policy. | No | Up to 63 characters. Recommended to be unique. | `My vulnerability policy`  
**Description** | A description of the policy. | No | Up to 2048 characters. | `Checks for critical vulnerabilities.`  
**Policy Type** | The type of policy being defined. | Yes | Only `vulnerability_policy` is supported. | `vulnerability_policy`  
**Enablement State** | The enablement state of the policy. | Yes | Must be `ACTIVE` or `INACTIVE`. | `ACTIVE`  
  
#### Vulnerability Policy

**Note:** At least one vulnerability rule (maximumAllowedVulnerabilities, maxAllowedSeverity, exemptedCves, restrictedCves, allowedPackages, or restrictedPackages) must be specified.**Name** | **Description** | **Multi-valued** | **Constraints** | **Sample Values**  
---|---|---|---|---  
**maximumAllowedVulnerabilities** | Maximum number of vulnerabilities allowed before the policy is violated. | No | Must be a non-negative number if set. | `10`  
**maxAllowedSeverity** | Maximum severity of vulnerabilities that are allowed by the policy. | No | Must be either `LOW`, `MEDIUM`, `HIGH` or `CRITICAL`. |   
**exemptedCves** | List of CVEs that are exempt from this policy. | Yes | Up to 100 entries. Each ID must be in `CVE-YYYY-NNNN` format. Grace period expiration, if provided, must be a valid timestamp. Cannot overlap with `restrictedCves`. | `- id: CVE-2024-12345`  
`gracePeriodExpirationTime: 2027-01-01T00:00:00Z`  
`- id: CVE-2025-4000`  
**restrictedCves** | List of CVEs that are explicitly disallowed by this policy. | Yes | Up to 100 entries. Each ID must be in `CVE-YYYY-NNNN` format. Cannot overlap with `exemptedCves`. | `- CVE-2024-54321`  
`- CVE-2025-5001`  
**allowedPackages** | List of packages that are allowed, potentially overriding other rules. | Yes | Up to 100 entries. Package names cannot be empty. Cannot conflict with `restrictedPackages`. | `- name: nginx`  
`version: 1.0`  
`- name: python`  
`version: 3.12.4`  
**restrictedPackages** | List of packages that are explicitly disallowed. | Yes | Up to 100 entries. Package names cannot be empty. Cannot conflict with `allowedPackages`. | `- name: npm`  
`version: 9.0.0`  
**excludeUnfixable** | Whether to exclude vulnerabilities that have no available fix. | No | Boolean. Default is `false`. | `true`  
**exemptionDaysPostDisclosure** | Number of days to exempt vulnerabilities after their disclosure date. | No | Must be a non-negative number, if set. Default is `0`. | `30`  
  
#### Policy scope

**Note:** A scope (Pipeline, Registry, or Runtime) must be defined for the policy.

#### Pipeline scope

**Name** | **Description** | **Required** | **Constraints** | **Sample Values**  
---|---|---|---|---  
**connectorIds** | List of Connector IDs that the policy applies to during CI/CD pipeline scanning. | Yes | Minimum 1 entry, maximum 100 entries. Your organization or project must be onboarded to CI/CD scanning. Each ID must follow the correct format, belong to your organization or project, and point to an existing connector.  | 

  * `organizations/123/locations/global/connectors/connector-1`
  * `projects/123/locations/global/connectors/connector-1`

  
**enforcementAction** | Action to take when the policy is violated. | Yes | Must be either `AUDIT_ONLY` or `BLOCK_BUILD`. | `BLOCK_BUILD`  
  
#### Registry scope

**Note:** At least one of `projectIds`, `garRepositoryNamePatterns`, or `imageNamePatterns` must be set for the policy to be active.**Name** | **Description** | **Required** | **Constraints** | **Sample Values**  
---|---|---|---|---  
**projectIds** | List of project IDs where the policy applies. | No | Min 1 entry. Each ID must be a valid Google Cloud project ID.  | `projects/123, projects/456`  
**garRepositoryNamePatterns** | List of Google Cloud Artifact Registry repository name patterns. | No | Max 100 entries. Must be a valid Google Cloud Artifact Registry repository pattern. | `us-west1-docker.pkg.dev/my-project/my-repo, gcr.io/team-a/*`  
**imageNamePatterns** | Regular expression patterns for fully qualified image names. | No | Max 100 entries. Must be a valid regular expression. | `'my-repo/service-a:.*', 'my-repo/service-b:v1..*'`  
**enforcementAction** | The action to take when the policy is violated. | Yes | Must be either `AUDIT_ONLY` or `ADMISSION_CONTROL`. | `ADMISSION_CONTROL`  
**admissionControl** | Configuration details for admission control. | No | Must be present if `enforcementAction` is `ADMISSION_CONTROL`. |   
  
#### Runtime scope

The runtime scope enables artifact guard to monitor container images running in your GKE environment. When you apply a policy to this scope, Security Command Center vulnerability findings include policy metadata for images deployed in the specified projects or clusters.

**Name** | **Description** | **Required** | **Constraints** | **Sample Values**  
---|---|---|---|---  
**projectIds** | List of project IDs where GKE clusters are deployed and vulnerability assessment is enabled. | Yes | Must be selected at the organization level.  | `projects/my-gke-deployment-123`  
**gkeClusterNames** | Specific GKE clusters for which the policy needs to be evaluated. | No | Can be selected at the organization or project level. | `projects/prod-env/locations/us-central1/clusters/main-cluster`  
  
If a container image running in a monitored GKE cluster violates a policy, the `ArtifactGuardPolicies` metadata is added to the Security Command Center vulnerability finding message, as follows:

```none // Added to the SCC 'message Finding' ArtifactGuardPolicies artifact_guard_policies = X;

message ArtifactGuardPolicies { string resource_id = 1; // e.g., //us-docker.pkg.dev/google-samples/containers/gke/security/... repeated Policy failing_policies = 2; }

message Policy { enum Type { TYPE_UNSPECIFIED = 0; VULNERABILITY = 1; } Type type = 1; string policy_id = 2; // e.g., organizations/3392779/locations/global/policies/prod-policy string failure_reason = 3; // e.g., severity=HIGH AND max_vuln_count=2 } ```

### Enforcement action

For `BLOCK_BUILD` and `BLOCK_DEPLOYMENT` actions, the policy evaluation returns a recommended enforcement action. However, you must configure the actual enforcement in the pipeline configuration using this recommendation.

### Policy deletion

If you receive a `FAILED_PRECONDITION` error, it means you are trying to delete an active policy. To delete the policy, you must first change its state to `Inactive`.

### Common errors

The following table outlines some common errors and how to resolve them.

**Error Message Hint** | **Cause** | **Resolution**  
---|---|---  
**parent is required** | The parent field is missing from the request. | Provide a valid parent in one of the following formats: 

  * `organizations/{org_id}/locations/global`
  * `parents/{project_number}/locations/global`

  
**policy definition is required** | The policy object is missing from the request. | Provide a valid policy object in the request.  
**display name has a maximum length of...** | The display name exceeds 63 characters. | Shorten the display name to 63 characters or less.  
**description has a maximum length of...** | The description exceeds 2048 characters. | Shorten the description to 2048 characters or less.  
**policy type is required** | Policy type (for example, `vulnerabilityPolicy`) is missing from the request. | Add a `vulnerabilityPolicy` or other policy type to your policy.  
**enablement state is invalid** | An invalid or deprecated enablement state was used. | Use `ACTIVE` or `INACTIVE`.  
**scope is required** | No scope (Pipeline, Registry, or Runtime) was defined. | Add at least one valid scope to your policy.  
**CVE name must be in the format...** | A CVE ID in `exemptedCves` or `restrictedCves` is invalid. | Make sure that all CVE IDs follow the `CVE-YYYY-NNNN` format.  
**CVE ... cannot be exempted and restricted** | The same CVE ID exists in both `exemptedCves` and `restrictedCves`. | Remove the CVE from one of the lists.  
**package name cannot be empty** | A package in `allowedPackages` or `restrictedPackages` has an empty name. | Provide a name for all packages.  
**package ... cannot be allowed and restricted** | The same package is listed in both `allowedPackages` and `restrictedPackages`. | Remove the package from one of the lists.  
**connector IDs are required** | The `connectorIds` field is missing in a Pipeline scope. | Provide at least one Connector ID.  
**connector ID must be in the format...** | A Connector ID is malformed. | Make sure that IDs are in one of the following formats: 

  * `organizations/{org_id}/locations/global/connectors/{connector_id}`
  * `projects/{project_number}/locations/{location}/connectors/{connector_id}`

  
**connector ID ... does not exist** | A specified connector ID does not exist. | Verify that the connector exists or remove it from the list.  
**GAR repository name pattern must be...** | An invalid repository pattern was provided in a Registry scope. | Make sure that patterns match valid Google Cloud Artifact Registry repository formats.  
**project ID must be a valid GCP project ID...** | An invalid project ID was provided in a Registry or Runtime scope. | Provide valid Google Cloud project IDs.  
**enforcement action should be specified** | The `enforcementAction` is missing in a Pipeline or Runtime scope. | Set the enforcement action. Examples include, `AUDIT_ONLY`, `BLOCK_BUILD` (Pipeline only), or `BLOCK_DEPLOYMENT` (Runtime only).  
**number of policies per organization exceeds the limit...** | You have reached the maximum number of policies (1000) for your organization. | Delete unused policies before creating new ones.  
**number of vulnerability policies ... exceeds the limit...** | You have reached the maximum number of vulnerability policies (500). | Delete unused vulnerability policies before creating new ones.  
**number of policies per pipeline exceeds the limit...** | A connector is associated with more than 100 policies. | Reduce the number of policies associated with the connector.  
**number of policy revisions ... exceeds the limit...** | You have updated a policy more than 100 times in 7 days. | Wait or reduce update frequency.  
  
### Common operational issues

Besides policy content validation failures, issues can arise with the underlying Google Cloud control plane. These issues can affect API requests, long-running operations, and resource states, typically appearing as specific error codes or unusual behavior.

Issue | Symptom(s) | How to Troubleshoot  
---|---|---  
**Concurrent Modification** | `UpdatePolicy` or `DeletePolicy` fails with an `ABORTED` error code and `"Provided etag is out of date"` message. | **Troubleshooting** : This happens when the `etag` in your request doesn't match the policy's current server version, indicating a modification by another request.  
  
**Resolution** : Read the policy again to get the latest etag, then retry the request with the new etag.  
**Request Validated but Not Executed** | A `CreatePolicy`, `UpdatePolicy`, or `DeletePolicy` request returns successfully, but you observe no change to the resource. | **Troubleshooting** : This typically occurs when `validate_only: true` is set in the request. This flag instructs the service to perform all validations without committing any changes.  
  
**Resolution** : Set `validate_only` to `false` or omit the field in your request.  
**Update Creates a New Policy** | An `UpdatePolicy` request creates a policy instead of returning a "not found" error when the policy doesn't exist. | **Troubleshooting** : This is the intended behavior when `allow_missing: true` is included in an `UpdatePolicyRequest`.  
  
**Resolution** : If you only want to update an existing policy, set `allow_missing` to `false` or omit the field.  
**Permission Denied or API Not Enabled** | Requests fail with `PERMISSION_DENIED` or an error message like `"Artifact Guard API has not been used in the project before or it is disabled."` | **Troubleshooting** : The API might be disabled, or the caller may not have sufficient permissions.  
  
**Resolution** : In your Google Cloud project, enable the Artifact Guard API (`artifactscanguard.googleapis.com`). Confirm that the user or service account performing the operation has the necessary IAM roles.  
**Operation Timeout** | A request that returns a long-running operation (LRO) takes too long to complete or fails with `DEADLINE_EXCEEDED`. | **Troubleshooting** : This may indicate a temporary slowdown or issue in the backend service.  
  
**Resolution** : Poll the LRO status. If it fails or times out, retry the operation after a few moments. If the issue persists, check the [Google Cloud Status Dashboard](https://status.cloud.google.com/) for any ongoing incidents or contact Google Cloud Support.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
