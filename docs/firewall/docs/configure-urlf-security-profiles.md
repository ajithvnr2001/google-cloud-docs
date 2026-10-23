---
url: https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles/
title: Create and manage URL filtering security profiles \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:39.364931+00:00
---

# Create and manage URL filtering security profiles  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-urlf-security-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create and manage URL filtering security profiles Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create, view, list, modify, and delete URL filtering security profiles by using the Google Cloud console and the Google Cloud CLI.

URL filtering security profiles are Layer 7 policy structures that evaluate domain names in network traffic to enforce allow or deny actions. Using URL filtering security profiles helps reduce your attack surface and control outbound traffic. For details about these concepts, see [URL filtering security profiles](https://docs.cloud.google.com/firewall/docs/about-security-profiles#url-filtering-profile).

This document is intended for network administrators and security engineers who configure and enforce Layer 7 network security policies.

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/firewall/docs/reference/network-security/rest) in your project.
  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.



### Roles

To get the permissions that you need to create, view, update, or delete security profiles, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-security-profiles#iam-roles) on your organization. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user account has the [Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`) permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



## Create a URL filtering security profile

To create a `url-filtering` security profile, specify a name as a string or as a unique URL identifier.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level URL filtering security profiles, and at either the project level or the organization level for project-level URL filtering security profiles 



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. In the project selector menu, select your organization or project where you want to create the security profile.

  3. Select the **Security profiles** tab.

  4. Click **Create profile**.

  5. Enter a name in the **Name** field. Don't include sensitive information such as personally identifiable information or security data in the security profile name.

  6. Optional: Enter a description in the **Description** field.

  7. To create a Cloud Next Generation Firewall Enterprise security profile, in the **Purpose** section, select **Cloud NGFW Enterprise**.

  8. To create a URL filtering security profile, in the **Type** section, select **URL Filtering**.

  9. In the **URL filters** section, click the **Create URL filter** button.

  10. In the **Create a URL filter** pane, specify the following details:

     * **Priority** : specify the priority of the URL filter.
     * **Action** : specify the action that Cloud NGFW performs on the traffic. 
       * **Allow** : allows the connections that matches a URL.
       * **Deny** : denies the connections that matches a URL.
     * **URL list** : specify a list of URLs or matcher strings. Each URL or matcher string entry must appear in its own line without any spaces or delimiters. Each entry can consist of a domain only. For more information about the matcher strings, see Matcher strings for URLs.
  11. Click **Create**.




###  gcloud 

  1. Create a YAML file with the following content:
         
         name: NAME
         type: url-filtering
         urlFilteringProfile:
           urlFilters:
             - filteringAction: ACTION
               priority: PRIORITY
               urls: [URL,URL,...]
         

Replace the following:

     * `NAME`: the name of the URL filtering security profile; you can specify the name as a string or as a unique URL identifier.

Don't include sensitive information such as personally identifiable information or security data in the security profile name.
     * `ACTION`: specify one of the following actions:

       * `ALLOW`: allows connections that match against a URL
       * `DENY`: denies connections that match against a URL
     * `PRIORITY`: priority of a URL filter ranging from 0 to 2147483647.

     * `URLs`: a comma-separated list of matcher strings. For example, `www.example.com` and `www.examplepetstore.com`.

  2. To create the URL filtering security profile, run the [`gcloud network-security security-profiles import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/import):
         
         gcloud network-security security-profiles import NAME \
           --source FILE_NAME \
           [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
           --location global
         

Alternatively, you can create a URL filtering security profile without a YAML file by using the [`gcloud network-security security-profiles url-filtering create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/url-filtering/create):
         
         gcloud network-security security-profiles url-filtering create NAME \
             [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
             --description DESCRIPTION \
             --location global
         

Replace the following:

     * `NAME`: the name of the URL filtering security profile.

If you don't use the [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications) for the name, you must specify the organization or the project name, and the location.

Don't include sensitive information such as personally identifiable information or security data in the security profile name.
     * `FILE_NAME`: the name of the YAML file. For example, `url-filtering-sp.yaml`.

     * `ORGANIZATION_ID`: the organization ID. Use this flag to create an organization-level security profile.

     * `PROJECT_ID`: the project ID. Use this flag to create a project-level security profile.

     * `DESCRIPTION`: an optional description for the URL filtering security profile.

For example, the following code snippet shows an example of a URL filtering security profile that allows requests to `www.example.com` and `www.examplepetstore.com`, but denies requests to all other domains:
    
    urlFilteringProfile:
      urlFilters:
        - filteringAction: ALLOW
          priority: 1000
          urls: ['www.example.com', 'www.examplepetstore.com']
        # the following URL filter is implicit and will be processed last
        - filteringAction: DENY
          priority: 2147483647
          urls: ['*']
    




## Implicit deny URL filter

The URL filtering security profile always includes a default URL filter with the lowest priority (2147483647) that denies all connections that don't match the higher priority URL filters. The following code snippet shows an example of the implicit deny URL filter:
    
    
      urlFilteringProfile:
        urlFilters:
          # user-specified URL filters
          - filteringAction: DENY
            priority: 1000
            urls: ['www.example.com','www.examplepetstore.com']
          - filteringAction: ALLOW
            priority: 2000
            urls: ['www.example.org','www.example.net']
          # implicit deny URL filter that will be processed last
          - filteringAction: DENY
            priority: 2147483647
            urls: ['*']
      

You can see the implicit deny URL filter when viewing or exporting a URL filtering security profile. You cannot modify or remove the implicit filter. For example, if you want to change the default action of a profile from `DENY` (enforced by implicit filter) to `ALLOW`, you must add an explicit filter that Cloud NGFW processes before the implicit filter.
    
    
      urlFilteringProfile:
        urlFilters:
          # user-specified filters
          - filteringAction: DENY
            priority: 1000
            urls: ['www.example.com','www.examplepetstore.com']
          # explicit allow URL filter that you can add
          - filteringAction: ALLOW
            priority: 2000
            urls: ['*']
          # implicit deny URL filter that will be processed last
          - filteringAction: DENY
            priority: 2147483647
            urls: ['*']
      

## Matcher strings for URLs

Matcher strings are the values that you specify in the `urls` field of a URL filter. You can specify one or more matcher strings inside a URL filter.

#### Wildcards

Each matcher string in a URL list supports a wildcard character (*) in a limited manner.

  * Each matcher string can support only a single asterisk (*) such that the asterisk is either the first or the only character.
  * The asterisk (*) can have the following interpretations:

    * An asterisk (*) before a period (.) indicates all subdomains of the domain.

For example, the matcher string `*.example.com` matches with `a.example.com` and `a.b.c.example.com` but doesn't match with `example.com`.
          
          urlFilteringProfile:
            urlFilters:
              # user-specified filters
              - filteringAction: ALLOW
                priority: 1000
                urls: ['*.example.com']
              # implicit deny URL filter that will be processed last
              - filteringAction: DENY
                priority: 2147483647
                urls: ['*']
          

In the preceding example, Cloud NGFW allows traffic towards the subdomains of `example.com` but denies the rest of the outbound traffic.

    * An asterisk (*) before a label indicates the domain and all the subdomains.

For example, the matcher string `*example.com` matches with `a.example.com`, `a.b.c.example.com`, as well as `example.com`.
          
          urlFilteringProfile:
            urlFilters:
              # user-specified filters
              - filteringAction: ALLOW
                priority: 1000
                urls: ['*example.com']
              # implicit deny URL filter that will be processed last
              - filteringAction: DENY
                priority: 2147483647
                urls: ['*']
          

In the preceding example, Cloud NGFW allows traffic towards `example.com` as well as the subdomains of `example.com` but denies the rest of the outbound traffic.

    * An asterisk (*) before a domain extension (such as `.com`) indicates all domains (and their subdomains) that use the domain extension.

For example, the matcher string `*.com` matches with `example.com` and `examplepetstore.com` and all their subdomains.

The following code snippet demonstrates how to allow all domains (and their subdomains) that end in `.com` but deny the remaining traffic.
          
          urlFilteringProfile:
            urlFilters:
              # Allow all domains (and their subdomains) that end in '.com'
              - filteringAction: ALLOW
                priority: 2000
                urls: ['*.com']
              # implicit deny URL filter that will be processed last
              - filteringAction: DENY
                priority: 2147483647
                urls: ['*']
          

The following code snippet demonstrates how to deny all subdomains of `example.com` and `examplepetstore.com` but allow these domains and all other domains (and their subdomains) that end in `.com`.
          
          urlFilteringProfile:
            urlFilters:
              # Deny all subdomains of example.com
              - filteringAction: DENY
                priority: 1000
                urls: ['*.example.com']
              # Deny all subdomains of examplepetstore.com
              - filteringAction: DENY
                priority: 1500
                urls: ['*.examplepetstore.com']
              # Allow all domains (and their subdomains) that end in '.com'
              - filteringAction: ALLOW
                priority: 2000
                urls: ['*.com']
              # implicit deny URL filter that will be processed last
              - filteringAction: DENY
                priority: 2147483647
                urls: ['*']
          

    * Cloud NGFW doesn't interpret the asterisk (*) as a regular expression wildcard.

For example, `*example.test` doesn't match with `newexample.test` or `a.newexample.test`. It only matches with `example.test` and the subdomains of `example.test`.

    * A single asterisk (*) with no other characters indicates a match for all requests.

For example, the matcher string in the lowest priority explicit allow URL filter contains only an asterisk (*) and has an `ALLOW` action that overrides the default action of `DENY`. This happens because the implicit deny URL filter enforces the default `DENY` for any requests that don't match higher priority URL filters.

The highest priority URL filter—which is either an explicit `ALLOW` or an implicit `DENY`—determines whether Cloud NGFW allows or denies connections when it lacks SNI or domain information. This can happen with unencrypted HTTP traffic, or when TLS inspection is disabled for encrypted message headers.
          
          urlFilteringProfile:
            urlFilters:
              # user-specified filters
              - filteringAction: DENY
                priority: 1000
                urls: ['www.example.com','www.examplepetstore.com']
              # explicit allow URL filter that you can add
              - filteringAction: ALLOW
                priority: 2000
                urls: ['*']
              # implicit deny URL filter that will be processed last
              - filteringAction: DENY
                priority: 2147483647
                urls: ['*']
          




#### Limitations

  * Matcher strings represent either domains or subdomains.
  * Matcher strings don't support the slash character (/). For example: `www.example.com/images`.
  * Matcher strings don't support schemes or protocol names. For example: `http://www.example.com`.
  * Matcher strings don't support port numbers. For example: `www.example.com:80`.
  * Matcher strings support only ASCII letters, numbers, and special characters: hyphen (-), dot (.), and asterisk (*).



You must use [Punycode](https://datatracker.ietf.org/doc/html/rfc3492) to convert domain names that contain characters other than ASCII letters, numbers, hyphens (-), periods (.), or asterisks (*). Punycode is an encoding standard that transforms Unicode domain names into an ASCII-compatible format.

  * If you have two or more labels, use periods (.) to separate them. A label can contain one or more hyphens (-); however, the label must not start or end with a hyphen. Each label can include a maximum of 63 characters.

  * A URL filter doesn't support using a period at the beginning of a domain name or consecutive periods within a matcher string. A URL filter allows trailing periods, but Cloud NGFW removes them before saving a URL filter.

  * Cloud NGFW converts the matcher strings to lowercase before it saves the URL filter. Cloud NGFW doesn't perform any other normalization.

  * Each domain name can include a maximum of 255 characters.




## URL filters for multi-level subdomains

You can use URL filters with different priorities and actions to control network traffic to multi-level subdomains. You can also use the wildcard character (*) in matcher strings to specify domains and subdomains.

For example, consider a scenario where you implement the following behavior:

  * Allow `a.b.c.example.com`
  * Deny `*.b.c.example.com` (deny all other subdomains of `b.c.example.com`)
  * Allow `*.c.example.com` (allow all other subdomains of `c.example.com`)
  * Deny `*.example.com` (deny all other subdomains of `example.com`)
  * Allow `example.com`
  * Allow everything else



The following code snippet implements this scenario:
    
    
      urlFilteringProfile:
        urlFilters:
          # Allow 'a.b.c.example.com'
          - filteringAction: ALLOW
            priority: 1000
            urls: ['a.b.c.example.com']
          # Deny all subdomains of 'b.c.example.com'
          - filteringAction: DENY
            priority: 2000
            urls: ['*.b.c.example.com']
          # Allow all subdomains of 'c.example.com'
          - filteringAction: ALLOW
            priority: 3000
            urls: ['*.c.example.com']
          # Deny all subdomains of 'example.com'
          - filteringAction: DENY
            priority: 4000
            urls: ['*.example.com']
          # explicit allow URL filter
          - filteringAction: ALLOW
            priority: 5000
            urls: ['*']
          # implicit deny URL filter that will be processed last
          - filteringAction: DENY
            priority: 2147483647
            urls: ['*']
      

## List and view details of a URL filtering security profile

You can list the URL filtering security profiles created in an organization or a project. You can also view the profile details, such as the type, purpose, and description.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.describe`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level URL filtering security profiles, and at either the project level or the organization level for project-level URL filtering security profiles 



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. Select the **Security profiles** tab to view a list of configured security profiles.

  3. To filter for URL filtering security profiles, in the **Filter** field, specify **Profile type** as **URL filtering**.

The tab shows a list of URL filtering security profiles.

  4. To view profile details, click a **URL filtering** security profile.




###  gcloud 

To list all the URL filtering security profiles, use the [`gcloud network-security security-profiles url-filtering list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/url-filtering/list):
    
    
    gcloud network-security security-profiles url-filtering list \
        [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
        [--billing-project QUOTA_PROJECT_ID]
        --location global
    

To view details of a URL filtering security profile, run the [`gcloud network-security security-profiles url-filtering describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/url-filtering/describe):
    
    
    gcloud network-security security-profiles url-filtering describe NAME \
        [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
        [--billing-project QUOTA_PROJECT_ID]
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't use the [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications) for the name, you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID where the security profile exists.

  * `PROJECT_ID`: the project ID where the security profile exists.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




## Delete a URL filtering security profile

You can delete a URL filtering security profile by specifying its name, location, and organization or project. If a security profile is referenced by a security profile group, you can't delete it.

To delete a URL filtering security profile, use the Google Cloud console or the gcloud CLI. However, if a security profile is referenced by a security profile group, that security profile cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.delete`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level URL filtering security profiles, and at either the project level or the organization level for project-level URL filtering security profiles 



###  Console 

  1. In the Google Cloud console, go to the **Security profiles** page.

[Go to Security profiles](https://console.cloud.google.com/net-security/security-profiles/profiles/list)

  2. Select the **Security profiles** tab. The tab shows a list of configured security profiles.

  3. Select the security profile that you want to delete, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a URL filtering security profile, use the [`gcloud network-security security-profiles url-filtering delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/url-filtering/delete):
    
    
    gcloud network-security security-profiles url-filtering delete NAME \
        [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
        --location global
    

Replace the following:

  * `NAME`: the name of the security profile.

If you don't specify the name in [the unique URL identifier format](https://docs.cloud.google.com/firewall/docs/about-security-profiles#specifications), you must specify the organization or the project name, and the location.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: your project ID. Use this flag for a project-level security profile.

  * `QUOTA_PROJECT_ID`: your quota project ID. Use this flag only for organization-level security profiles.




## Import a URL filtering security profile

You can import a URL filtering security profile (either custom-created or previously exported) from a YAML file. When importing a URL filtering security profile, if a profile with the same name already exists, Cloud NGFW updates the existing profile.

To import a URL filtering security profile from a YAML file, use the gcloud CLI. If a profile with the same name already exists when you import it, Cloud NGFW updates that profile.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.create`
  * `networksecurity.securityProfiles.update` (required only if a profile with the same name already exists)



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level URL filtering security profiles, and at either the project level or the organization level for project-level URL filtering security profiles 



###  gcloud 

To import a URL filtering security profile from a YAML file, use the [`gcloud network-security security-profiles import` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/import):
    
    
    gcloud network-security security-profiles import NAME \
        [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
        --location global \
        --source FILE_NAME
    

Replace the following:

  * `NAME`: the name of the security profile of type `url-filtering` that you want to import; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `FILE_NAME`: the path to the YAML file containing the configuration export data.




## Export a URL filtering security profile

You can export a URL filtering security profile to a YAML file. For example, instead of using the user-interface to modify a large security profile, you can use this functionality to export the security profile, modify it quickly, and import it back.

To export a URL filtering security profile to a YAML file, use the gcloud CLI.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.securityProfiles.describe`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Security Profile Admin (`roles/networksecurity.securityProfileAdmin`) granted at the organization level for organization-level URL filtering security profiles, and at either the project level or the organization level for project-level URL filtering security profiles 



###  gcloud 

To export a URL filtering security profile to a YAML file, use the [`gcloud network-security security-profiles export` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/export):
    
    
    gcloud network-security security-profiles export NAME \
        [ --organization ORGANIZATION_ID | --project PROJECT_ID ] \
        --location global \
        --destination FILE_NAME
    

Replace the following:

  * `NAME`: the name of the security profile of type `url-filtering` that you want to export; you can specify the name as a string or as a unique URL identifier.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level security profile.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level security profile.

  * `FILE_NAME`: the path to the YAML file into which Cloud NGFW will export the configuration.




## What's next

  * [Create security profile groups](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups)
  * [Manage security profile groups](https://docs.cloud.google.com/firewall/docs/manage-security-profile-groups)
  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Manage firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
