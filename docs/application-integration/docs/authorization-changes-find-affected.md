---
url: https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected/
title: Find integrations that need a run-as service account \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:58.297706+00:00
---

# Find integrations that need a run-as service account  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/authorization-changes-find-affected/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Find integrations that need a run-as service account

This page is part of [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes). It helps you find the integrations that need a run-as service account before the changes take effect.

## Determine whether an integration needs one

You only need a run-as service account when nobody's credentials are available for the whole run. That happens in two situations, and only two: 

How the integration runs | Are someone's credentials available? | Needs a run-as service account?  
---|---|---  
**Synchronously** — someone starts it and waits for the result | Yes, for the whole run | **No**  
**Asynchronously** — it's queued and finishes later | Only at the moment it's triggered | **Yes**  
**Unattended** — a schedule or an event starts it | No, there's never a person | **Yes**  
**Note:** Asynchronous runs count even though a person triggered them: queued work doesn't carry that person's credentials, so by the time it runs there's nobody left to authorize it. An integration that only ever runs synchronously already has an identity and needs no change, unless it calls another integration asynchronously. That other integration needs its own run-as service account.

## Identify affected integrations

**First, does it ever run without a person?** It does if any of these are true:

  * It has any trigger other than an [API](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger) or [Private](https://docs.cloud.google.com/application-integration/docs/configure-private-trigger) trigger, for example a [Schedule](https://docs.cloud.google.com/application-integration/docs/configure-schedule-trigger), [Cloud Scheduler](https://docs.cloud.google.com/application-integration/docs/configure-cloud-scheduler-trigger), [Cloud Pub/Sub](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger), [Salesforce](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger), [Integration Connectors event](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks#event_triggers), or [Eventarc](https://docs.cloud.google.com/application-integration/docs/configure-eventarc-trigger) trigger.
  * Something schedules it through the API with `scheduleIntegrations`.
  * Another integration calls it as an asynchronous sub-integration, using the [Call Integration](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task) task. The sub-integration needs its own run-as service account even if the calling integration has one.
  * It uses the [Suspend](https://docs.cloud.google.com/application-integration/docs/configure-suspend-task) or [Approval](https://docs.cloud.google.com/application-integration/docs/configure-approval-task) task, where a run can sit waiting and then expire on its own.



**Second, is its run-as service account empty?** To list every published version in a region alongside its run-as service account, run the following command:
    
    
    curl -s -G -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      --data-urlencode "filter=state=ACTIVE" \
      --data-urlencode "pageSize=1000" \
      "https://REGION-integrations.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/integrations/-/versions" \
    | jq -r '.integrationVersions[]
             | [ .name, (.runAsServiceAccount // "NONE") ]
             | @tsv'
    

Replace the following:

  * `REGION`: the region of your integration. For the list of supported regions, see [Locations](https://docs.cloud.google.com/application-integration/docs/locations).
  * `PROJECT_ID`: the ID of your Google Cloud project


  * A row showing `NONE` needs action only if the first half applies to it too.
  * To check a single integration instead, open it in the integration editor and click settings (**Integration settings**) in the editor toolbar. The **Service account** field shows the run-as service account, and is empty if the integration doesn't have one.

**Caution:** Keep `filter=state=ACTIVE` on the request rather than filtering the output afterwards. The `-` wildcard returns one version per integration — the most recently modified one — so if you fetch everything and filter later, any integration whose newest version is an unpublished draft drops out of the results even when it has a published version that is still running. If the response contains a `nextPageToken`, repeat the request with `pageToken=TOKEN` until the token stops coming back.**Warning:** Don't wait for a warning in the Google Cloud console. Warnings depend partly on observed runs, so an integration on an infrequent schedule, or one nobody has triggered lately, can need action without ever showing one. Check your scheduled and event-driven integrations with the steps on this page instead.

## What's next

  * [Grant Service Account User](https://docs.cloud.google.com/application-integration/docs/authorization-changes-grant-access) on the run-as service accounts you already use.
  * [Set a run-as service account](https://docs.cloud.google.com/application-integration/docs/authorization-changes-set-run-as) on each integration you found.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
