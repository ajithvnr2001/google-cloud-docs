---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/
title: gcloud alpha pam grants \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:34.030338+00:00
---

# gcloud alpha pam grants  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha pam grants Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha pam grants - manage Privileged Access Manager grants 
SYNOPSIS
    

`gcloud alpha pam grants` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The `[gcloud pam grants](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants)` command group lets you manage Privileged Access Manager (PAM) grants. 
EXAMPLES
     To create a new grant against an entitlement with the full name ``ENTITLEMENT_NAME``, a requested duration of `1 hour 30 minutes`, a justification of `some justification`, and two additional email recipients `abc@example.com` and `xyz@example.com`, run: 
    
    
    [gcloud alpha pam grants create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/create) --entitlement=ENTITLEMENT_NAME --requested-duration=5400s --justification="some justification" --additional-email-recipients=abc@example.com,xyz@example.com

To describe a grant with the full name ``GRANT_NAME``, run: 
    
    
    [gcloud alpha pam grants describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/describe) GRANT_NAME

To list all grants associated with an entitlement with the full name ``ENTITLEMENT_NAME``, run: 
    
    
    [gcloud alpha pam grants list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/list) --entitlement=ENTITLEMENT_NAME

To deny a grant with the full name ``GRANT_NAME`` and a reason `denial reason`, run: 
    
    
    [gcloud alpha pam grants deny](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/deny) GRANT_NAME --reason="denial reason"

To approve a grant with the full name ``GRANT_NAME`` and a reason `approval reason`, run: 
    
    
    [gcloud alpha pam grants approve](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/approve) GRANT_NAME --reason="approval reason"

To revoke a grant with the full name ``GRANT_NAME`` and a reason `revoke reason`, run: 
    
    
    [gcloud alpha pam grants revoke](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/revoke) GRANT_NAME --reason="revoke reason"

To search for and list all grants that you have created that are associated with an entitlement with the full name ``ENTITLEMENT_NAME``, run: 
    
    
    [gcloud alpha pam grants search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/search) --entitlement=ENTITLEMENT_NAME --caller-relationship=had-created

To search for and list all grants that you have approved or denied, that are associated with an entitlement with the full name ``ENTITLEMENT_NAME``, run: 
    
    
    [gcloud alpha pam grants search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/search) --entitlement=ENTITLEMENT_NAME --caller-relationship=had-approved

To search for and list all grants that you can approve that are associated with an entitlement with the full name ``ENTITLEMENT_NAME``, run: 
    
    
    [gcloud alpha pam grants search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/search) --entitlement=ENTITLEMENT_NAME --caller-relationship=can-approve

To withdraw a grant with the full name ``GRANT_NAME``, run: 
    
    
    [gcloud alpha pam grants withdraw](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/withdraw) GRANT_NAME

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[approve](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/approve)`
     `(ALPHA)` Approve a Privileged Access Manager (PAM) grant. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/create)`
     `(ALPHA)` Create a new Privileged Access Manager (PAM) grant. 
`[deny](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/deny)`
     `(ALPHA)` Deny a Privileged Access Manager (PAM) grant. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/describe)`
     `(ALPHA)` Show details of a Privileged Access Manager (PAM) grant. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/list)`
     `(ALPHA)` List all Privileged Access Manager (PAM) grants associated with an entitlement. 
`[revoke](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/revoke)`
     `(ALPHA)` Revoke a Privileged Access Manager (PAM) grant. 
`[search](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/search)`
     `(ALPHA)` Search for and list all Privileged Access Manager (PAM) grants you have created, have approved, or can approve. 
`[withdraw](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pam/grants/withdraw)`
     `(ALPHA)` Withdraw a Privileged Access Manager (PAM) grant. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud pam grants](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants)
    
    
    [gcloud beta pam grants](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pam/grants)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
