---
url: https://docs.cloud.google.com/binary-authorization/docs/overview-cv/
title: Continuous validation overview \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:12.864614+00:00
---

# Continuous validation overview  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/overview-cv/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Continuous validation overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Continuous validation (CV) with check-based platform policies is a feature of Binary Authorization that lets you monitor Pods that run on Google Kubernetes Engine (GKE) to ensure that their associated container images continue to conform to Binary Authorization check-based platform policies that you specify.

When CV determines that Pods violate platform policies, it logs the violations to Cloud Logging.

CV with platform policies supersedes legacy continuous validation ([deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy)).

## Why use CV?

Although Binary Authorization enforcement provides one-time image validations when you deploy container images, CV continuously monitors that images associated with running Pods continue to conform to your policies.

Because of this, when you enable both Binary Authorization enforcement and CV with check-based policies, you can ensure that policy conformance is validated throughout the entire orchestration lifecycle.

CV is useful in the following scenarios:

  * **Policy changes** : When you update your Binary Authorization [project-singleton enforcement policies](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies), Binary Authorization validates only images that are deployed after the update. Pods that are already running aren't affected. They continue to run even if Binary Authorization, using the updated policy, would now block the same image from being deployed.

Because of this, when you update the Binary Authorization project-singleton policy, we recommend that you also create or update a CV platform policy to match the project-singleton policy. That way CV informs you of running Pods that violate your updated policies.

  * **Monitoring image metadata** : CV provides specific checks for changes in image metadata, including the following:

    * Attestations: CV logs when the attestations on the Pods' images are no longer valid.
    * Freshness: CV logs when it detects that Pods' images are no longer fresh.
    * Provenance: CV can check that Pods' images were built with a trusted builder, using build configs that reside in a trusted source repository.
    * Sigstore signatures: CV logs when the on the Pods' images lack a valid Sigstore signature.
    * Trusted directory: CV logs when the Pods' images reside in a repository directory that isn't listed in your platform policy.
    * Vulnerabilities: CV logs when vulnerabilities are identified in Pods' images.
  * **Dry run monitoring** : When you enable dry run, Binary Authorization allows all images to be deployed. By enabling CV with a platform policy that matches your project-singleton policy, CV regularly logs images that violate the platform policy.

  * **Breakglass monitoring** : When you deploy Pods using [breakglass](https://docs.cloud.google.com/binary-authorization/docs/using-breakglass), Binary Authorization bypasses project-singleton policy enforcement and logs a single event to Cloud Audit Logs. By using a matching platform policy, however, CV continues to regularly log policy-violating Pods, including those Pods deployed using breakglass.




## How CV works

To use CV, you must enable it on your GKE clusters.

After you deploy images on your cluster, CV monitors the associated Pods to make sure they conform with your check-based platform policy.

CV doesn't support image tags, other than those specified in exempt images.

### CV regularly reviews running Pods

To monitor running Pods, CV reviews images associated with each Pod at least every 24 hours. CV also monitors init containers and ephemeral containers.

During each review, CV retrieves a list of images associated with each Pod. CV then verifies that image information satisfies the platform policy.

### CV logs violations of platform policies

When CV determines that images violate a platform policy, it logs the violations and other findings to [Cloud Logging](https://docs.cloud.google.com/logging). A separate log entry is written for each platform policy that is violated, for each Pod.

When CV evaluates a Pod's images using a platform policy, the images might satisfy some checks and violate others. CV produces a log entry whenever any image of a Pod violates any check. The log entry contains only the Pod images that violate the platform policy. If all images satisfy all checks, no log entries are produced.

CV continues to log policy violations until a Pod with non-policy-conformant images terminates. When non-policy-conformant Pods are terminated during the interval between validations, the final CV-generated log entries can appear after termination, during the next [CV evaluation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv#cv-reviews-pods).

Non-policy-conformant Pods should be logged at least once, even for short-lived Pods.

CV does not terminate running Pods.

### CV uses a feed resource

To retrieve information about Pods running on your GKE cluster, CV creates a feed resource called `binauthz-cv-cai-feed`.

**Important:** Deleting or modifying the `binauthz-cv-cai-feed` feed can cause CV to fail. CV automatically restores missing or altered feeds, but it can fail to log findings until it does so.

## CV platform policies

To use CV, you first configure platform policies.

Platform policies are different from [legacy Binary Authorization policies, also called project-singleton policies](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#project-singleton-policy). Although the deployment project can have only one legacy project-singleton policy, you can configure multiple platform policies. Each platform policy can reside in one or more projects.

Platform policies work only with CV and don't support Binary Authorization enforcement. Because of this, we recommend that if you want to use both Binary Authorization enforcement and CV monitoring, you create a project-singleton policy for enforcement and a platform policy for monitoring.

For example, suppose that you want to configure Binary Authorization to enforce that your images have an attestation before they are allowed to be deployed, and you also want to ensure that your running Pods conform to the same requirement. To do this, you configure a project-singleton enforcement policy with an [attestor](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors). You then create a platform policy with a simple signing attestation check. that has an authenticator based on the same note and public key as the attestor.

Platform policies are platform specific. GKE is the only supported platform.

You can configure checks in platform policies. Checks are grouped into one or more check sets. Each check set can specify one or more checks.

Platform policies can exempt images from evaluation by CV.

### Required permissions

To list or describe platform policies, you need the `binaryauthorization.policyViewer` role. To create, modify, and delete platform policies, you need the `binaryauthorization.policyEditor` role. For more information, see [Manage platform policies](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies).

### Policy updates

[Updating a platform policy](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies#update-platform-policy) overwrites the existing policy with a policy descriptor that you provide in the YAML file. To add a new check to an existing platform policy, we recommend that you [describe](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies#describe-platform-policy) the existing policy, saving it to a YAML file, add the new check, and then update the policy using the updated file.

### Multiple platform policies

You can create platform policies in the same project as the cluster (a local platform policy) or in any other project.

Because you can configure a number of platform policies, you name each one with a unique resource name. When you run a gcloud CLI command you refer to the local platform policy using its ID. When you refer to a platform policy in another project, you use the resource name, in the following format: `projects/POLICY_PROJECT_ID/platforms/gke/policies/POLICY_ID`

You can choose which platform policy to associate with each GKE cluster, whether it's a local platform policy or one in a different project.

### Multiple checks per platform policy

You can configure multiple checks in each platform policy by adding them to the `checks` block of the policy. To learn more about specific checks that you can configure, see checks.

When your CV platform policy specifies more than one check, images that are evaluated by one check continue to be evaluated by the other checks.

Binary Authorization evaluates all of the checks that are configured in the platform policy for each image unless the image matches an exempt images allowlist pattern. For more information, see Exempt images.

### Single-project setup

You can set up CV in a single project.

In a single-project setup, Binary Authorization automatically sets up its required roles in the Binary Authorization service agent.

If GKE clusters, platform policies bound to the clusters, and the metadata that is required by checks all reside in the same project, no additional Identity and Access Management (IAM) roles are required.

To learn more about configuring a multi-project setup for added security, see [Separation of concerns](https://docs.cloud.google.com/binary-authorization/docs/reference/organizational-and-iam-roles).

### Multi-project setup

When you configure a multi-project CV setup with platform policies, the platform policies, the images, the GKE cluster, and other types of CV-dependent resources can each reside in a different project.

In multi-project setup, it's important to know the purpose of each project and the resources that CV needs to access and set up required IAM roles and permissions accordingly.

## How to use CV

To use CV, you typically do the following:

  1. Decide which checks you want to use.
  2. Compose one or more platform policies using a policy YAML file. The file specifies which checks you want to use.
  3. Create the [platform policy](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies). The policy can be stored in a project of your choice.
  4. Choose whether to enable CV on [individual clusters](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies#manage-gke-clusters) or on a [fleet](https://docs.cloud.google.com/binary-authorization/docs/enable-cv-fleet).
  5. [Check CV logs](https://docs.cloud.google.com/binary-authorization/docs/cv-view-logs) in Logging for events.
  6. Review logs and update your build and other processes to produce images that satisfy the checks.

**Important:** When you update existing clusters to enable CV, they might already be using Binary Authorization for enforcement. In this case, use the following flag to ensure continued enforcement: `--binauthz-evaluation-mode=POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE`

## Checks

This section describes the specific checks that CV provides.

Check-based policies have the following canonical format:
    
    
    gkePolicy:
      checkSets:
      - checks:
        - CHECK_TYPE1:
            CHECK_TYPE1_PARAMETERS
          displayName: CHECK_TYPE1_DISPLAY_NAME
        - CHECK_TYPE2:
            CHECK_TYPE2_PARAMETERS
          displayName: CHECK_TYPE2_DISPLAY_NAME
        displayName: CHECK_SET_DISPLAY_NAME
    

The `displayName` field in `checks` and `checkSets` is optional. It is used only when CV logs policy violations. It is omitted in some of the examples later in this guide.

### Always-deny check

The always-deny check guarantees that all images subject to this check fail evaluation. Each time CV reviews running Pods with this check, it produces a log entry for each of the Pods.

You can combine the always-deny check with allowlists or multiple check sets to ensure that Binary Authorization always produces logs for Pods in certain cases.

To use the always-deny check, add `alwaysDeny: true` in the `checks` block, as follows:
    
    
    gkePolicy:
      checkSets:
        - displayName: "My check set"
          checks:
            - alwaysDeny: true
    

The value of `alwaysDeny` can't be set to `false`. Instead, remove the check.

For examples of how the always-deny check can be used, see Use multiple check sets.

### Image freshness check

The image freshness check computes the duration that an image has been running and logs when the duration has exceeded the threshold, `maxUploadAgeDays`.

In the following example platform policy YAML, CV logs Pods with images that were uploaded to the repository from which they were deployed more than 30 days ago.
    
    
    gkePolicy:
      checkSets:
        checks:
        - imageFreshnessCheck:
            maxUploadAgeDays: 30
          displayName: "My image freshness check"
        displayName: "My check set"
    

### Simple signing attestation check

You can use the CV simple signing attestation check to check that each of a Pod's images have a valid, signed attestation.

This check is equivalent to the attestation evaluation in a Binary Authorization enforcement policy. You can configure this check with the same notes and keys that you used in your attestor. We recommend that you use this check instead of legacy continuous validation ([deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy)).

The following is an example of a platform policy with a simple signing attestation check:
    
    
    gkePolicy:
      checkSets:
        checks:
          simpleSigningAttestationCheck:
            containerAnalysisAttestationProjects:
            - "projects/my-attestation-project1"
            - "projects/my-attestation-project2"
            attestationAuthenticators:
              pkixPublicKeySet:
                pkixPublicKeys:
                  publicKeyPem: |
                    -----BEGIN PUBLIC KEY-----
                    MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQxXxgAEvgQuW1FHYZPB2PTQfOJKUkS9sjMO/1os10xOWrhl1kQo4EnzMOovROWVLo+m9mcwp7nRQ2qQDThZdSFi0nFJ1A==
                    -----END PUBLIC KEY-----
                  signatureAlgorithm: ECDSA_P256_SHA256
    

Instead of [Binary Authorization attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors), CV attestation checks have _authenticators_. You specify authenticators directly in the policy, in the `attestationAuthenticators` block.

In a platform policy, `simpleSigningAttestationCheck` can have multiple `attestationAuthenticators` and multiple keys in each `pkixPublicKeySet`. The check is satisfied when each of the Pods' images have a valid attestation signed with _any_ key in _any_ authenticator's `pkixPublicKeySet`.

**Important:** Although Binary Authorization project-singleton policies require a valid attestation from any key of every attestor, the simple signing attestation check requires an attestation from any key in any authenticator. To configure the equivalent of a project-singleton policy with multiple attestors, you must configure multiple attestation checks in your platform policy. It is not sufficient to configure multiple authenticators or multiple keys.

CV platform policies are different from project-singleton enforcement policies in the following ways:

  * PGP keys are not supported.
  * Attestors are not needed. Instead, you manually create keys and then [describe](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies#describe-platform-policy) a platform policy to retrieve the key ID that you then use to create the attestation.
  * You manually create and sign the payload, create the attestation JSON file, and create the attestation using the Artifact Analysis API.
  * You still create an Artifact Analysis Note, but you don't specify it in the policy. Instead CV looks for attestations in every project that is listed in the `containerAnalysisAttestationProjects` field.
  * Attestations are still stored in Artifact Analysis occurrences, but they can be stored in more than one project.
  * You must explicitly specify one or more projects that contain attestations by using the resource name `projects/ATTESTATION_PROJECT_ID`.



CV doesn't support image tags, except those specified in exempt images.

If images are deployed with an image tag instead of a digest, CV first evaluates it against exempt images, since allowlists can include tags. If the image isn't exempted, then CV attempts to find the image digest. Because there isn't one, the image violates the check.

### SLSA check

The SLSA check checks the [SLSA-specified provenance](https://slsa.dev/provenance) of Pods' images.

The following is an example of a CV platform policy YAML configuration:
    
    
    gkePolicy:
      checkSets:
        checks:
          imageAllowlist:
            allowPattern: "gcr.io/my-images/not-built-by-GCB/**"
        - slsaCheck:
            rules:
              trustedBuilder: GOOGLE_CLOUD_BUILD
              attestationSource:
              - containerAnalysisAttestationProjects: "projects/attestation-project1"
              - containerAnalysisAttestationProjects: "projects/attestation-project2"
              # Require that images were built using a checked-in top-level config file.
              configBasedBuildRequired: true
              # Which repos the config file can be from.
              trustedSourceRepoPatterns:
              - "source.cloud.google.com/my-project/my-source-repo"
              - "github.com/my-github-user/*"
          displayName: "My SLSA check"
        displayName: "My check set"
    

When CV reviews images using this platform policy, it checks the following:

  * The images must have been built by a trusted builder. Cloud Build is the only trusted builder that the SLSA check supports.

  * Cloud Build must have generated the attestations in either `attestation-project1` or `attestation-project2`.

  * The images must be built using a top-level config file from either of the following trusted repositories:

    * The repository `source.cloud.google.com/my-project/my-source-repo/`
    * Any repositories in `github.com/my-github-user/`
  * The images in `gcr.io/my-images/not-built-by-GCB/` or its subdirectories (that were not built by Cloud Build) are exempted from the check as they would violate it.




### Sigstore signature check

The Sigstore signature check verifies that images have been signed using [Sigstore](https://www.sigstore.dev/) signatures.

This check supports only images hosted in Artifact Registry. It checks if any signature fetched from Artifact Registry can be successfully verified by any key in the policy.

The following example platform policy describes how to configure a Sigstore signature check:
    
    
      gkePolicy:
        checkSets:
        - checks:
          - displayName: sigstore-signature-check
            sigstoreSignatureCheck:
              sigstoreAuthorities:
              - displayName: sigstore-authority
                publicKeySet:
                  publicKeys:
                    publicKeyPem: |
                      -----BEGIN PUBLIC KEY-----
                      MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQxXxgAEvgQuW1FHYZPB2PTQfOJKUkS9sjMO/1os10xOWrhl1kQo4EnzMOovROWVLo+m9mcwp7nRQ2qQDThZdSFi0nFJ1A==
                      -----END PUBLIC KEY-----
    

In the platform policy, `sigstoreSignatureCheck` can have multiple `sigstoreAuthorities` and multiple keys in each `publicKeySet`. The check is satisfied when each of the Pods' images have a valid attestation signed with _any_ key in _any_ authenticator's `publicKeySet`.

**Important:** Although Binary Authorization project-singleton policies require a valid attestation from any key of every attestor, the Sigstore signature check requires an attestation from any key in any authority. To configure the equivalent of a project-singleton policy with multiple authorities, you must configure multiple Sigstore signature checks in your platform policy. It is not sufficient to configure multiple authenticators or multiple keys.

### Trusted directory check

The trusted directory check checks that Pods' images reside in one of the provided trusted directories that you specify in a platform policy.

When you use this check, we recommend that you also safeguard the repositories that you list as trusted directories in your policy against unauthorized access.

The following example platform policy describes how to configure a trusted directory check:
    
    
    gkePolicy:
      checkSets:
        checks:
          trustedDirectoryCheck:
            trustedDirPatterns:
            - "gcr.io/my-project/gcr-directory"
            - "us-central1-docker.pkg.dev/my-project/ar-directory"
            displayName: "My trusted directory check"
        displayName: "My check set"
    

In the example platform policy, `trustedDirPatterns` lists the trusted directories. If all of the Pods' images reside in the listed directories, they conform to the policy. Pods' images that don't reside in the listed directories violate the policy, and CV logs the violations.

### Vulnerability check

The vulnerability check uses Artifact Analysis vulnerability scanning to check whether Pods's images contain vulnerabilities. This includes new vulnerabilities that are identified by vulnerability scanning since the Pod was deployed. In the vulnerability check, you can configure [vulnerability severity level](https://docs.cloud.google.com/artifact-analysis/docs/severity-levels) thresholds and specific vulnerabilities (as CVEs). Images with vulnerabilities that violate the vulnerability check are logged to Logging.

To use this check, you must first enable vulnerability scanning in Artifact Analysis.

The following example platform policy configuration contains a vulnerability check:
    
    
    gkePolicy:
      checkSets:
        - displayName: "Default check set"
          checks:
            - vulnerabilityCheck:
               maximumFixableSeverity: MEDIUM
               maximumUnfixableSeverity: HIGH
               allowedCves:
                 - "CVE-2022-11111"
                 - "CVE-2022-22222"
               blockedCves:
                 - "CVE-2022-33333"
                 - "CVE-2022-44444"
               containerAnalysisVulnerabilityProjects: "projects/my-project"
    

In the example, `maximumUnfixableSeverity` and `maximumFixableSeverity` define Common Vulnerability Scoring System (CVSS) severity levels that are associated with any vulnerability that Artifact Analysis can identify. Additionally, `blockedCves` lists specific Common Vulnerability Exposures (CVEs). If an identified vulnerability exceeds one of the specified severity levels or matches one of the CVEs listed in `blockedCves`, and it doesn't match one of the CVEs listed in `allowedCves`, then CV logs an entry to Logging.

## Validate updated policies

After you update a CV platform policy, we strongly recommend that you validate that Binary Authorization and CV continue to operate as you expect.

### Validate your configuration

To check your configuration, inspect both your [Binary Authorization project-singleton policies](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli) and [CV platform policies](https://docs.cloud.google.com/binary-authorization/docs/manage-platform-policies#list-policies).

### Validate operation

To validate that Binary Authorization and CV are operating as you expect, you can deploy test Pods and then check Binary Authorization entries in Logging.

## Exempt images with allowlists

When you create a platform policy, you can exempt images from checks by adding their URLs to an allowlist. An allowlist at the policy level exempts images from the entire policy. An allowlist at the check set level exempts from the check set, and it applies only when that check set is evaluated. An allowlist within a check exempts images only from that check.

Allowlist patterns are patterns that match one or more image URLs. An allowlist pattern can be one of the following:

  * An image name prefix, ending with the wildcard `*` or `**`.
  * Just an image name, with no tag or digest.
  * An image name with a tag (or tag prefix with the wildcard `*`).
  * An image name with a digest.
  * An image name with both a tag and a digest.



The following are examples of allowlist patterns:

  * `us-central1.pkg.dev/my-project/my-image:latest@sha256:77b0b75136b9bd0fd36fb50f4c92ae0dbdbbe164ab67885e736fa4374e0cbb8c` matches an exact image name, tag, and digest.
  * `us-central1.pkg.dev/my-project/my-image:latest` matches the name and tag, with any digest (or no digest).
  * `us-central1.pkg.dev/my-image:foo*` matches the name and tag prefix (such as `myimage:foo` and `myimage:foobar`), with any digest (or no digest).
  * `us-central1.pkg.dev/my-project/my-image@sha256:77b0b75136b9bd0fd36fb50f4c92ae0dbdbbe164ab67885e736fa4374e0cbb8c` matches the name and digest, with any tag (or no tag).
  * `us-central1.pkg.dev/my-project/my-image` matches the name, with any tag and/or digest.



The wildcard characters `*` and `**` can be used to match any name with a certain prefix. `*` matches suffixes that don't include `/`. `**` matches suffixes that can include `/`, but `**` can only be used after a `/`. Note that `*` and `**` cannot be used with tags or digests.

For example:

  * `us-central1.pkg.dev/my-project/my-image*` matches `us-central1.pkg.dev/myproject/my-image`, `us-central1.pkg.dev/myproject/my-image1`, and `us-central1.pkg.dev/myproject/my-image2`, with any tag and/or digest.
  * `us-central1.pkg.dev/my-project/**` matches `us-central1.pkg.dev/myproject/my-image` and `us-central1.pkg.dev/my-project/some-directory/other-image`, with any tag and/or digest.



Note that name prefixes and tag prefixes must not be empty. So `*` or `**` alone is not a valid pattern, and neither is `us-central1.pkg.dev/my-image:*`.

### gkePolicy-level exemption

The following example shows you how to exempt images at a platform policy level. All of the images in the `exempt-images1` and `exempt-images2` directories and their subdirectories are excluded from CV monitoring.
    
    
    gkePolicy:
      imageAllowlist:
      - allowPattern: "us-central1-docker.pkg.dev/PROJECT_ID/exempt-images1/**"
      - allowPattern: "us-central1-docker.pkg.dev/PROJECT_ID/exempt-images2/**"
      checkSets:
          checks:
            ...
    

In the policy, images listed under `imageAllowlist` are exempted from all of the check sets (`checkSets`) that are listed under `gkePolicy`.

### checkSet-level exemption

The following example shows you how to exempt images at the check set level:
    
    
    gkePolicy:
      checkSets:
        imageAllowlist:
        - allowPattern: "us-central1-docker.pkg.dev/PROJECT_ID/exempt-images1/**"
        - allowPattern: "us-central1-docker.pkg.dev/PROJECT_ID/exempt-images2/**"
        checks:
          ...
    

In the policy, images listed under `imageAllowlist` are exempted from all of the checks that are listed under `checkSets`.

### checks-level exemption

The following example shows you how to exempt images at the check level:
    
    
    gkePolicy:
      checkSets:
        checks:
          imageAllowlist:
          - allowPattern: "us-central1-docker.pkg.dev/PROJECT_ID/exempt-images1/**"
          - allowPattern: "us-central1-docker.pkg.dev/PROJECT_ID/exempt-images2/**"
          ...
    

## Use multiple check sets

A CV check-based policy can contain more than one check set. CV evaluates one check set each time it evaluates the policy. You can think of check sets as sub-policies that should be evaluated in different situations. For example, if you want to apply different checks in development environments than you do in production environments, you can put the checks for each environment in a separate check set, one that gets evaluated only in the development environment, and one that gets evaluated in production.

Each check set is scoped to either a Kubernetes namespace or a Kubernetes service account. The scope determines which Pods the check set applies to.

When a check set is configured with a scope, it applies only to Pods running in that scope.

When a check set has no scope, it's called a _default check set_ , which means that the checks apply to all Pods, regardless of their Kubernetes namespace or service account scope.

Most of the example policies in the CV guides use only a default check set.

The following example policy configuration configures three check sets:
    
    
    gkePolicy:
      checkSets:
        - displayName: "Prod check set"
          scope:
            kubernetesNamespace: "prod-namespace"
          checks:
            - trustedDirectoryCheck:
                trustedDirPatterns: "gcr.io/my-project/prod-images"
            - imageFreshnessCheck:
                maxUploadAgeDays: 30
        - displayName: "Dev check set"
          scope:
            kubernetesNamespace: "dev-namespace"
          checks:
            - trustedDirectoryCheck:
                trustedDirPatterns: "gcr.io/my-project/dev-images"
        - displayName: "Default check set"
          checks:
            - alwaysDeny: true
    

In the example configuration, the first check set is scoped to `prod-namespace`, so its checks affect only Pods running in that scope. The second check set is scoped to `dev-namespace`, so its checks affect only Pods running in that scope. The third check set is a default check set. Its checks apply to all Pods in the cluster running outside of the `prod-namespace` and `dev-namespace` scopes.

When CV evaluates the check set called `Prod check set` it checks the following for Pods' images running in the `prod-namespace` Kubernetes namespace:

  * The images are stored in the trusted `prod-images` directory.
  * The images were uploaded in the last 30 days.



When CV evaluates the check set called `Dev check set` it evaluates Pods running in the `dev-namespace` Kubernetes namespace, checking whether images in the Pod come from the `dev-images` directory.

The default check set acts as a catch-all. The always-deny check ensures that CV logs all Pods that are running in any other namespace.

To use a Kubernetes service account as the scope of a check set, replace the key `kubernetesNamespace` in the example with `kubernetesServiceAccount`. The value has the format `my-namespace:my-service-account`.

Check set scopes have the following rules:

  * There can be only one check set per scope in a platform policy.

  * If a policy contains both namespace-scoped and service account-scoped check sets, the service account-scoped check set must be listed first, followed by the namespace-scoped check set.

  * There can be only one default check set, and it must listed last.




If a platform policy contains any check sets, it must contain at least a default check set. A platform policy with no check sets is allowed, but since there are no checks to violate, CV doesn't produce any log entries.

## Legacy CV

**Caution:** Legacy continuous validation (legacy CV) with project-singleton policies is [deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy). As of April 15, 2024, you can no longer enable legacy CV with project-singleton policies on new projects, and support for existing projects will be removed on May 1, 2025. Instead, use [continuous validation (CV) with check-based platform policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv). Existing legacy CV users can migrate project-singleton policies to platform policies. To learn how, see [Migration](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy#migration). 

This section describes legacy CV policies. If you're new to CV, we recommend that you instead use [CV with check-based policies](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).

To support legacy CV users, CV can be enabled on projects that run GKE. CV then uses the Binary Authorization enforcement policy to check all Pods running on all of the clusters in the project, including clusters for which Binary Authorization enforcement isn't enabled.

Learn how to [use legacy CV](https://docs.cloud.google.com/binary-authorization/docs/using-cv) ([deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy)) and [view legacy CV events in Cloud Logging](https://docs.cloud.google.com/binary-authorization/docs/using-cv#view_cv_events_in_logging).

## What's next

  * [Use the image freshness check](https://docs.cloud.google.com/binary-authorization/docs/cv-freshness-check)
  * [Use the simple signing attestation check](https://docs.cloud.google.com/binary-authorization/docs/cv-attestation-check)
  * [Use the Sigstore signature check](https://docs.cloud.google.com/binary-authorization/docs/cv-sigstore-check)
  * [Use the SLSA check](https://docs.cloud.google.com/binary-authorization/docs/cv-slsa-check)
  * [Use the trusted directory check](https://docs.cloud.google.com/binary-authorization/docs/cv-trusted-directory-check)
  * [Use the vulnerability check](https://docs.cloud.google.com/binary-authorization/docs/cv-vulnerability-check)
  * [View CV logs](https://docs.cloud.google.com/binary-authorization/docs/cv-view-logs)
  * Learn about [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
