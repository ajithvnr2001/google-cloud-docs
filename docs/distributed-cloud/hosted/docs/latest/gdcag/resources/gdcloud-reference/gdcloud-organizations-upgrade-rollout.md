---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-organizations-upgrade-rollout/
title: gdcloud organizations upgrade rollout \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:36:39.497005+00:00
---

# gdcloud organizations upgrade rollout  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-organizations-upgrade-rollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud organizations upgrade rollout Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud organizations upgrade rollout - Trigger an upgrade to a new version for the specified organization(s).

## SYNOPSIS
    
    
    gdcloud organizations upgrade rollout [flags]
    

### EXAMPLES
    
    
    To upgrade the infra organization "root" to version "1.14.3-gdch.1000-1", run:
    
        gdcloud organization upgrade rollout --version=1.14.3-gdch.1000-1 --names=root
    
    To upgrade an organizations "org-1" and "org-2" to version "1.14.3-gdch.1000-1", run:
    
        gdcloud organization upgrade rollout --version=1.14.3-gdch.1000-1 --names=org-1,org-2,...
    
    To upgrade all eligible organizations in the current zone to version "1.14.3-gdch.1000-1", run:
    
        gdcloud organization upgrade rollout --version=1.14.3-gdch.1000-1 --all-organizations
    
    Root organization must be at the new version or greater, before a version is available to any other organizations in a zone.
    
    

### OPTIONAL FLAGS
    
    
          --all-organizations           Upgrade all organizations in the given zone.
          --direct                      Rollout OC changes to the specified organization(s) directly.
          --distribute-artifacts        Distribute artifacts to a tenant org before rolling out to the org directly.
          --ignore-maintenance-window   Ignore maintenance window for tenant organization upgrade.
          --names strings               Comma-separated list of organizations to trigger upgrade for.
          --skip-checks                 Skip preflight and postflight checks for organization upgrade.
          --version string              Version to upgrade to.
          --zone string                 Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
