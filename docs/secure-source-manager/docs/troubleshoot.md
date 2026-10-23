---
url: https://docs.cloud.google.com/secure-source-manager/docs/troubleshoot/
title: Troubleshoot \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:52.233798+00:00
---

# Troubleshoot  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Secure Source Manager.

## Error message when creating a repository

The following error appears when you try to create a repository:
    
    
    There was an error while loading /repo/create. Try refreshing the page.
    

This issue occurs when:

  * The Secure Source Manager API isn't enabled in your project.
  * You don't have the Repo Admin role on your project or permissions to create repositories in the Secure Source Manager instance.



To resolve this issue:

  * [Enable the Secure Source Manager API](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable) in your project.
  * Ask your administrator to grant you the following roles: 
    * Repo Admin (`roles/securesourcemanager.repoAdmin`) role on your project.
    * Instance Accessor (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance.
    * Instance Repository Creator (`roles/securesourcemanager.instanceRepositoryCreator`) on the Secure Source Manager instance.



See [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) for more details.

## Error message when cloning a repository on a Mac

The following error appears when you try to clone a repository:
    
    
    git: 'credential-gcloud.sh' is not a git command.  See 'git --help'.
    fatal: Authentication failed for [repo-url]
    

This issue occurs when:

  * gcloud CLI is installed using Homebrew or other non-standard installation.
  * `git-credential-gcloud.sh` is not added to your PATH.



To resolve this issue:

  * Run `source $HOMEBREW_PREFIX/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.zsh.inc`
  * Check that `git-credential-gcloud.sh` is in your path by running the following command:
        
        which git-credential-gcloud.sh
        




## SSH connection fails with "no matching" error

When attempting Git operations over SSH, you might receive one of the following error messages:

  * `Unable to negotiate with <host> port <port>: no matching key exchange method found.`
  * `Unable to negotiate with <host> port <port>: no matching cipher found.`
  * `Unable to negotiate with <host> port <port>: no matching MAC found.`



This issue occurs when your SSH client does not support the cryptographic algorithms required by Secure Source Manager. This can happen if you are using an older SSH client or if your client is not configured to use supported algorithms.

Secure Source Manager requires one of the following algorithms:

  * **Key Exchange Algorithms:** `curve25519-sha256`, `diffie-hellman-group14-sha256`
  * **Ciphers:** `chacha20-poly1305@openssh.com`, `aes128-ctr`, `aes192-ctr`, `aes256-ctr`, `aes128-gcm@openssh.com`, `aes256-gcm@openssh.com`
  * **MACs:** `hmac-sha2-256-etm@openssh.com`, `hmac-sha2-256`



To resolve this issue, update your SSH client to a recent version that supports these algorithms.

## Git HTTPS requests fail with permission denied or unauthorized error

When Git commands are attempted over HTTPS, a permission denied or unauthorized error message is given.

This issue occurs when one of the following occurs:

  * The global Git config file is missing the Secure Source Manager authentication helper.
  * Git's built-in credential store is being used instead of calling the Secure Source Manager authentication helper to get a fresh credential.
  * A system credential helper is being used instead of calling the Secure Source Manager authentication helper to get a fresh credential.
  * An older version of Google Cloud CLI is used when interacting with Secure Source Manager repositories using HTTPS. Secure Source Manager requires Google Cloud CLI version 395.0.0 or newer.



To resolve this issue:

  1. Run the following command to determine the contents of your global Git config.
         
         git config --list | grep credential
         

  2. If you see any line similar to `*credential*.helper=store` on macOS, or `credential.helper = manager` on Windows OS, then remove those lines, and then re-authenticate using `gcloud auth login` before trying the Git command again.

  3. If the response doesn't include `credential.https://*.*.sourcemanager.dev.helper=gcloud.sh` on macOS or Linux, or `credential.https://*.*.sourcemanager.dev.helper=gcloud.cmd` on Windows, then add the Secure Source Manager authentication helper to your global Git config:

###  Linux 

     1. To add the Secure Source Manager authentication helper to your global Git config, run the following command:
            
            git config --global credential.'https://*.*.sourcemanager.dev'.helper gcloud.sh
            

     2. Validate that the authentication helper line is added to your global Git config by running the following command:
            
            git config --list | grep credential
            

The output should include `credential.https://*.*.sourcemanager.dev.helper=gcloud.sh`.

     3. Authenticate by running `gcloud auth login`.

     4. Run a Git command to test the authentication.

###  Windows 

     1. Check your gcloud CLI version by following the [Install Git and Google Cloud CLI](https://docs.cloud.google.com/secure-source-manager/docs/use-git#install_git_and) instructions.
     2. To add the Secure Source Manager authentication helper to your global Git config, run the following command:
            
            git config --global credential.https://*.*.sourcemanager.dev.helper gcloud.cmd
            

     3. Validate that the authentication helper line is added to your global Git config by running the following command:
            
            git config --list | grep credential
            

The output should include `credential.https://*.*.sourcemanager.dev.helper=gcloud.cmd`.

     4. Authenticate by running `gcloud auth login`.

     5. Run a Git command to test the authentication.

  4. If you previously set the credential for your Git host to be `gcloud.sh`, but get an error like `'credential-gcloud.sh' is not a git command`, it indicates that Git is not able to find the `git-credential-gcloud.sh` script in the `PATH` for your machine. Update your `PATH` or replace the `gcloud.sh` in your gitconfig file with the absolute path instead.




## Git HTTPS requests fail with invalid token

A valid OAuth token is required as the password for Git HTTPS operations. This is normally handled by [Git credential helper](https://docs.cloud.google.com/secure-source-manager/docs/use-git#set_up_your_credentials), but it can also work with OAuth tokens generated using other approaches (for example, [application default credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials)).

If a Git request is rejected due to an invalid token, it normally means user information couldn't be extracted from the incoming token, there are multiple possible causes of this error:

  * Your gcloud CLI login might have expired.

Sign in again using `gcloud auth login`.

  * Your token doesn't have sufficient scope. OAuth tokens are expected to have the following scopes:

    * `https://www.googleapis.com/auth/cloud-platform`
    * `https://www.googleapis.com/auth/userinfo.email`

You can check the token scope by calling`curl https://oauth2.googleapis.com/tokeninfo?access_token=${TOKEN}`

  * You are using a token generated from [GKE fleet workload identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity):

    * Raw tokens generated from [GKE fleet workload identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity) are not supported. For more information, see SSM returns an error when using KSA tokens with GKE fleet workload identity.
  * You have org policies that prevent using tokens outside certain perimeters, for example Context-Aware Access.

To resolve this issue, set the `git_helper_use_adc` gcloud CLI configuration property to `true` and update your Application Default Credentials (ADC):

    1. Sign in using application-default:
           
           gcloud auth application-default login
           

    2. Set the `git_helper_use_adc` property:
           
           gcloud config set auth/git_helper_use_adc true
           




## Git HTTPS requests fail on macOS with 403 error due to stale credentials

When performing Git operations over HTTPS on macOS, you might receive a 403 error.

This issue can occur on macOS if you use iCloud Keychain, which can interfere with gcloud CLI authentication tokens by storing and syncing stale tokens. These stale tokens can cause authentication to fail with Secure Source Manager, even after you re-authenticate using `gcloud auth login`.

To resolve this issue, manually delete any stale credentials from Keychain Access:

  1. Open the **Keychain Access** application on your Mac (located in `/Applications/Utilities/`).
  2. Search for `sourcemanager.dev`.
  3. Delete any entries of kind "internet password" that match `*.*.sourcemanager.dev` or your Secure Source Manager instance URL by right-clicking the entry and selecting **Delete**.
  4. After deleting the entries, retry your Git operation. You might be prompted to re-authenticate with gcloud CLI. If Git operations continue to fail, run `gcloud auth login` before trying again.



## SSM returns an error when using Kubernetes Service Account (KSA) tokens with GKE fleet workload identity

When using [GKE fleet workload identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity), raw KSA tokens are not supported by Secure Source Manager. Using these tokens results in an error.

To resolve this issue, you must [impersonate a service account](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity#impersonate_a_service_account) and bind the workload to a Google service account. You also need to add the following annotation to your KSA configuration:
    
    
    iam.gke.io/gcp-service-account: SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com
    

## Project not showing up in web interface product selector

When using the Secure Source Manager web interface product selector, your project doesn't appear.

This issue occurs when you have multiple login credentials for Secure Source Manager.

To resolve this issue:

  * Clear your cookies by appending the following to your Secure Source Manager instance URL: `/_oauth/consent`

For example, if your instance URL is `https://my-instance-098765432123.us-central1.sourcemanager.dev/`, enter `https://my-instance-098765432123.us-central1.sourcemanager.dev/_oauth/consent` into your browser address bar and then sign in with the correct credentials.




## Triggers file doesn't trigger builds

If builds aren't triggered as expected after submitting your triggers file, you might have one of the following problems:

  * The triggers file isn't in the default branch. To resolve this, move your triggers file to your default branch.
  * The triggers file has an invalid format. This error is indicated by a banner in the repository page that reads `Build triggers configuration error: ...`. To fix this, read the [Triggers file schema](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema). When the triggers file configuration is correct, the banner in the repository page reads `Valid build triggers configuration`.



## Build triggers configuration error

After submitting your `triggers.yaml` file to your Secure Source Manager repository you get the following error displayed in a banner:
    
    
    Build cannot be created.
    

This issue occurs for the following reasons:

  * The Cloud Build configuration file has invalid options or format.
  * The Secure Source Manager Service Agent doesn't have the **Service Account Token Creator** role on the repository's user-managed service account.
  * The user-managed service account doesn't have the **Service Account User** role on the Cloud Build service account.
  * The user-managed service account doesn't have the **Cloud Build Editor** role on the project where builds run.
  * The organization policy `iam.disableCrossProjectServiceAccountUsage` is blocking the usage of the user-managed service account (if the service account is in a different project).



To fix this issue:

  * Make sure you're following the correct [Triggers file schema](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema).
  * Verify that all required roles are granted. See [Required service account roles](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build#required-sa-roles).
  * If using a user-managed service account in a different project, verify that the organization policy `iam.disableCrossProjectServiceAccountUsage` is disabled in the project hosting the service account.



## Build fails during execution

If a build is triggered successfully, but fails during execution, the associated commit has a Failure commit status.

To troubleshoot a failed build, in the repository page, next to the failed commit status, click **Details**.

The Cloud Build execution log opens. For more information on troubleshooting builds in Cloud Build, see [Troubleshooting build errors](https://docs.cloud.google.com/build/docs/troubleshooting).

## Git push rejected due to detected sensitive data

When pushing commits to a repository with secret scanning enabled, your push fails with an error message similar to the following:
    
    
    remote: Push rejected: Sensitive data detected.
    

This issue occurs when secret scanning or a custom inspection template identifies sensitive information in your commit history.

To resolve this issue:

  * Revert the problematic commit using `git reset --soft` and remove the sensitive information before committing again.
  * If the detected information is acceptable and you have appropriate permissions, bypass the check using the `-o dlpskip=true` push option:
        
        git push -o dlpskip=true origin BRANCH_NAME
        




## Daily quota not reset after recreation

After you delete a Secure Source Manager instance and recreate it with the same instance ID on the same day, you might receive a quota exhausted or limit reached error for secret scanning.

This issue occurs because the secret scanning quota is a daily **Rate** quota linked to the instance ID. If you delete and recreate an instance with the same ID on the same day, the quota usage isn't reset.

To resolve this issue, you can do one of the following:

  * Wait until the second day for the daily quota usage to automatically reset to 0.
  * Recreate the instance by using a different, unique instance ID.
  * Skip secret scanning temporarily, or request a quota increase. For more information, see [Increase available quota](https://docs.cloud.google.com/secure-source-manager/docs/quotas#increase_available_quota).



## Error when configuring repository service account

The following error appears when you try to create or update a repository with a user-managed service account:
    
    
    Permission denied on resource ...
    

This issue occurs when you don't have the **Service Account User** (`roles/iam.serviceAccountUser`) role on the service account you are trying to associate with the repository. Secure Source Manager verifies that you have permission to act as the service account before allowing you to associate it with the repository.

To resolve this issue, ask your administrator to grant you the Service Account User role on the service account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
