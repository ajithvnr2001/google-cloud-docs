---
url: https://docs.cloud.google.com/secure-source-manager/docs/enable-data-loss-prevention/
title: Enable secret scanning \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:33.310154+00:00
---

# Enable secret scanning  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/enable-data-loss-prevention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Enable secret scanning Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to safeguard your sensitive information with integrated secret scanning in Secure Source Manager.

Secret scanning in Secure Source Manager improves your codebase security. It analyzes commits pushed to your repositories or merged through pull requests, actively scanning for sensitive information that you should encrypt or remove. If such data is detected, secret scanning automatically rejects the push or blocks the pull request merge, preventing sensitive details from being inadvertently merged.

**Note:** When using secret scanning, we recommend that your commit doesn't exceed 100 MB.

Secret scanning in Secure Source Manager treats the following categories of information as sensitive:

  * **Encryption keys** : This includes items like SSH private keys.
  * **AWS credentials** : Access keys and secret keys for Amazon Web Services.
  * **Google Cloud credentials** : Service account keys and other Google Cloud secrets.
  * **OAuth client secrets** : Secrets used for application authentication with OAuth.
  * **Secret keys** : Sensitive keys used for authentication or authorization.



## Enable secret scanning

Ensure that the following roles and settings are enabled for your repository.

### Required roles

To get the permissions that you need to enable secret scanning, ask your administrator to grant you the [Secure Source Manager Repository Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) IAM role on the Secure Source Manager instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

#### Service account permissions

If you configure secret scanning to use a custom Sensitive Data Protection inspection template, the service account used by Secure Source Manager must have permission to read the template (for example, the DLP Reader role, `roles/dlp.reader`).

  * If a per-repository service account is configured for the repository, Secure Source Manager uses that service account exclusively. You must grant the template read permission to the per-repository service account.
  * If no per-repository service account is configured, Secure Source Manager uses the instance service account.



### Update repository settings

You can activate secret scanning for your repositories through the Secure Source Manager interface:

  1. Navigate to the repository where you want to enable secret scanning.
  2. Click the **Settings** icon.
  3. Locate the **Secret scanning** toggle.
  4. Click the toggle to the **On** position.
  5. Optional: In the **Inspection template** field, enter the resource name of your Sensitive Data Protection inspection template.



## Working with secret scanning

Once secret scanning is enabled, it actively monitors commits to your repository. If sensitive information is identified in a commit pushed using Git or merged through a pull request in the web interface, the commit is rejected or the merge is blocked.

When pushing from the command line, you receive an error indicating the presence of sensitive data. At this point, you have two options:

### Revert the change

To remove the sensitive information, you can revert the problematic commit using the following command:
    
    
    git reset --soft COMMIT_ID
    

Replace COMMIT_ID with the actual commit ID.

Because Git retains the history of all commits, sensitive material can still be recovered from previous commits. To avoid this, use the `git reset --soft` command. Then, correct the files and commit them again to remove the data from the branch's recent history.

### Force-push the commit (bypass secret scanning)

In specific situations where the detected information is deemed acceptable, users with appropriate permissions can choose to bypass the secret scanning check and force-push the commit.

**Caution:** Use force-pushing with extreme care. It can overwrite remote history and bypass important security checks. Ensure that you fully understand the implications before using this option.
    
    
    git push -o dlpskip=true origin \
        BRANCH_NAME
    

Replace BRANCH_NAME with the name of the branch you're merging.

## What's next

  * [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview)
  * [Creating Sensitive Data Protection inspection templates](https://docs.cloud.google.com/dlp/docs/creating-templates-inspect)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
