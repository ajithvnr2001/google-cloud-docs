---
url: https://docs.cloud.google.com/identity/docs/how-to/turn-off-automatic-google-workspace-licensing-during-setup/
title: Turn off automatic Google Workspace licensing during setup \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:47.500222+00:00
---

# Turn off automatic Google Workspace licensing during setup  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/turn-off-automatic-google-workspace-licensing-during-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Turn off automatic Google Workspace licensing during setup

_These instructions apply during Cloud Identity free edition setup. If you already set up your free Cloud Identity subscription and need to turn off automatic licensing for Google Workspace,[follow these instructions](https://support.google.com/a/answer/6342682) instead._

After you sign up for Cloud Identity, all new users you add to your organization automatically become free Cloud Identity users. If you have automatic licensing turned on for Google Workspace, the users also automatically get a paid Google Workspace license. If they don't need Google Workspace services, such as Gmail, you can turn off automatic licensing and avoid paying for licenses that you don't need. The change applies to new users only. Existing licenses aren't affected.

## Turn off automatic licensing (recommended)

### I have one Google Workspace subscription (most common)

If you only have one Google Workspace subscription—for example, only Business Standard—when you add users, they're automatically assigned a license for that Google Workspace subscription. When you set up free Clou Cloud Identity recommend that you keep the **Switch off Auto-Assign** box checked to turn off automatic Google Workspace licensing. This way, any new users you add only receive a free Cloud Identity license.

### I have multiple Google Workspace subscriptions

If you have multiple Google Workspace subscriptions—for example, both Business Standard and Plus—and you have automatic licensing turned on for your top-level organization for one of those subscriptions, we recommend that you turn off top-level automatic licensing _before_ you complete the free Clou Cloud Identityup. This way, any users you add after setup only get a free Clou Cloud Identityense. During setup, be sure to leave the **Switch off Auto-Assign box** checked to turn off automatic Google Workspace licensing. For details, see the following example scenario.

If you've set automatic Google Workspace licensing options (Inherit, Override, On, or Off) for individual organizations within the top-level organization, turning off top-level automatic licensing doesn't affect these options.

#### Example scenario

If you have automatic licensing for Business Standard turned on for your top-level organization and turn it off during free Cloud Identity setup, here's what happens to new users you add to child organizations:

Organization | Setting | If you add a new user  
---|---|---  
A | Inherit |  Before you signed up, the organization inherited the "automatic licensing on" setting from the top-level organization. Therefore, all users you added to organization A were automatically assigned a Business Standard license. After you set up Cloud Identity, organization A keeps its **Inherit** setting. Because automatic licensing for Business Standard is now off at the top level, it's also off for organization A. Therefore, new users you create in organization A only get a free Cloud Identity license. If you want new users to have Business Standard licenses, change the **Inherit** setting to **Override** and turn automatic licensing **On**.  
B | Override > On |  Before you signed up, all users you added to organization B were automatically assigned a Business Standard license. After you set up Cloud Identity, organization B keeps its **Override > On** setting. Therefore, new users you add will continue to automatically get Business Standard licenses.  
C | Override > Off |  Before you signed up, you manually assigned each user a license for Business Standard or some other subscription. After you set up Cloud Identity, organization C keeps its **Override > Off** setting. Because Cloud Identity is the default for any organization where automatic licensing is turned off, new users you add to organization C automatically get only a free Cloud Identity license. If you want users to have a different license, you can assign it manually as before.  
  
## If you leave automatic licensing turned on

If you un-check the box and leave automatic licensing on, any new users you add automatically get a paid Google Workspace license. Make sure you want to do this—you might end up paying more for these users.

If you decide to leave automatic licensing on for Google Workspace, you can still add free Cloud Identity-only users. Just select or create an organization for your Cloud Identity users and [turn off Google Workspace automatic licensing for that organization](https://support.google.com/a/answer/7610656). Then add the users to the organization.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
