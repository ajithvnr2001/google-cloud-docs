---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/keys/update/
title: gcloud alpha recaptcha keys update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:29:44.366631+00:00
---

# gcloud alpha recaptcha keys update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recaptcha/keys/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha recaptcha keys update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha recaptcha keys update - update a Key 
SYNOPSIS
    

`gcloud alpha recaptcha keys update` `KEY` [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--express` | `--universal` | `--android` (`--allow-all-package-names` | `--package-names`=[`PACKAGE_NAMES`,…]) | [`--ios` : `--allow-all-bundle-ids` | `--bundle-ids`=[`BUNDLE_IDS`,…] `--key-id`=`KEY_ID` `--private-key-file`=`PATH_TO_FILE` `--team-id`=`TEAM_ID`] | [`--web` : `--allow-amp-traffic` `--security-preference`=`SECURITY_PREFERENCE` `--action-score-thresholds`=[`ACTION_SCORE_THRESHOLDS`,…] `--default-score-threshold`=`DEFAULT_SCORE_THRESHOLD` `--allow-all-domains` | `--domains`=[`DOMAINS`,…]]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a reCAPTCHA Key. 
EXAMPLES
     To update the information of a reCAPTCHA key, run: 
    
    
    gcloud alpha recaptcha keys update test-key --labels="foo=bar" --web --domains=test.com.mx

POSITIONAL ARGUMENTS
    

Key resource - The reCAPTCHA Key to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `key` attribute: 

  * provide the argument `key` on the command line. 


FLAGS
    

`--display-name`=`DISPLAY_NAME`
     A human-readable name for the key. Typically a site or app name. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
At most one of these can be specified: 

Options for an Express site key. 
`--express`
     Configures the Key for Express assessments. 
Options for a Universal site key. 
`--universal`
     Configures the Key as Universal. 
Options for an Android site key. 
`--android`
     Configures the Key for Android devices. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Exactly one of these must be specified: 

`--allow-all-package-names`
     If set, package name enforcement will NOT be enabled on this key. 
`--package-names`=[`PACKAGE_NAMES`,…]
     Android package names of apps allowed to use the key. 

Example of a valid package name: 'com.companyname.appname' 

Options for an iOS site key. 
`--ios`
     Configures the Key for iOS devices. 

This flag argument must be specified if any of the other arguments in this group are specified. 

At most one of these can be specified: 

`--allow-all-bundle-ids`
     If set, bundle id enforcement will NOT be enabled on this key. 
`--bundle-ids`=[`BUNDLE_IDS`,…]
     iOS bundle ids of apps allowed to use the key. 

Example of a valid bundle id: 'com.companyname.productname.appname' 

Fields that are required to perform Apple-specific integrity checks (recommended for iOS keys). 
`--key-id`=`KEY_ID`
     The Apple developer key ID (10-character string). 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--private-key-file`=`PATH_TO_FILE`
     File path to a private key (downloaded as a text file with a .p8 file extension) generated for your Apple Developer account. Ensure that DeviceCheck is enabled for the private key. Use a full or relative path to a local file containing the value of private_key_file. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--team-id`=`TEAM_ID`
     The Apple team ID (10-character string) owning the provisioning profile used to build your application. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Options for a web site key. 
`--web`
     Configures the Key for websites. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--allow-amp-traffic`
     Whether this key can be used on AMP (Accelerated Mobile Pages) websites. 
`--security-preference`=`SECURITY_PREFERENCE`
     Represents the possible challenge frequency and difficulty configurations for a web key. usability: show fewer and easier challenges. balance: show balanced (in amount and difficulty) challenges. security: show more and harder challenges. 

`SECURITY_PREFERENCE` must be one of: `balance`, `challenge-security-preference-unspecified`, `security`, `usability`. 

Configure if you want to use the POLICY_BASED_CHALLENGE option. 
`--action-score-thresholds`=[`ACTION_SCORE_THRESHOLDS`,…]
     The action to score threshold used for POLICY_BASED_CHALLENGE. For example: \--action-score-thresholds=login='{"scoreThreshold": "0.3"}',signup='{"scoreThreshold": "0.1"}' or \--action-score-thresholds=file_path.(json|yaml). 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 

`scoreThreshold`
     Sets `scoreThreshold` value. 
`Shorthand Example:`
    
    
    --action-score-thresholds=string={scoreThreshold=float}

`JSON Example:`
    
    
    --action-score-thresholds='{"string": {"scoreThreshold": float}}'

`File Example:`
    
    
    --action-score-thresholds=path_to_file.(yaml|json)

`--default-score-threshold`=`DEFAULT_SCORE_THRESHOLD`
     The global threshold to be used for POLICY_BASED_CHALLENGE if no action specific one exists. 
At most one of these can be specified: 

`--allow-all-domains`
     If set, domain name enforcement will NOT be enabled on this key. 
`--domains`=[`DOMAINS`,…]
     Domains or subdomains of websites allowed to use the key. All subdomains of an allowed domain are automatically allowed. A valid domain requires a host and must not include any path, port, query or fragment. 

Examples of valid domains: 'example.com' 'subdomain.example.com' 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `recaptchaenterprise/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/recaptcha-enterprise/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud recaptcha keys update](https://docs.cloud.google.com/sdk/gcloud/reference/recaptcha/keys/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
