---
url: https://docs.cloud.google.com/identity/docs/how-to/how-licensing-works-for-cloud-identity/
title: How licensing works for Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:18.170570+00:00
---

# How licensing works for Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/how-licensing-works-for-cloud-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# How licensing works for Cloud Identity

How you assign, add, remove, and reduce licenses depends on whether you have:

  * The free or Premium edition of Cloud Identity
  * One edition of Cloud Identity, both editions, or Cloud Identity with another paid service, such as Google Workspace.



## Cloud Identity free edition

Review this information to learn about assigning, adding, removing, and reducing licenses for the free edition of Cloud Identity.

#### Assign licenses

The free edition of Cloud Identity uses site-based licensing, which means you don't need to assign licenses. When you add a new user, they automatically get a free Cloud Identity license. They also get any licenses you assign for a different service, such as Google Workspace or Cloud Identity Premium.

#### Add licenses

If you need more free Cloud Identity users, add the users you want. They're assigned a Cloud Identity license automatically. Go to [Add users individually](https://support.google.com/a/answer/33310).

The number of free Cloud Identity users you can create depends on your user cap. Go to Cloud Identity free edition user cap.

#### Remove or reduce licenses 

You can't remove a user's free Cloud Identity license or cancel your free Cloud Identity subscription to reduce the number of licenses.

If a user no longer needs free Cloud Identity features, you can [delete the user](https://support.google.com/a/answer/33314).

If the user needs more features, you can assign the user a Google Workspace or Cloud Identity Premium license. Go to [Assign, remove, and reassign licenses](https://support.google.com/a/answer/1727173).

#### Cloud Identity free edition user cap

Your Cloud Identity free edition user cap is the total number of free Cloud Identity users you can add. When you sign up for a free Cloud Identity account, your user cap increases by 50. Therefore, you can add up to 50 more Cloud Identity users. If you purchase additional licenses for paid Google Cloud services, such as Google Workspace, your user cap automatically increases. If you reach your user cap, you'll get an error message when you try to add users.

#### How many more users can I add?

_You must be signed in as a[super administrator](https://support.google.com/a/answer/2405986#super_admin) for this task._

To see the remaining number of free Cloud Identity users you can create:

  1. In the Google Admin console, go to the **Billing > Subscriptions** page. 

[Go to Subscriptions](https://admin.google.com/ac/billing/subscriptions)

Requires having the [Billing management privilege](https://support.google.com/a/answer/1219251#api). If you aren't using a super administrator account, you can't complete these steps.

  2. Under **Subscriptions** , go to **Cloud Identity** to see the number of remaining users.



#### Request an increase to your user cap

_You must be signed in as a[super administrator](https://support.google.com/a/answer/2405986#super_admin) for this task._

You submit a form to request an increase to your free Cloud Identity user cap. After you submit the form, Google reviews it and decides whether to increase your cap.

  1. Go to the [Cloud Identity user increase form](https://support.google.com/a/contact/cloud_id_increase). 

If you can't access the form, make sure you're signed out of all personal and managed Google Accounts except your super administrator account.




## Cloud Identity Premium

Review this information to learn about assigning, adding, removing, and reducing licenses for the paid Cloud Identity Premium edition.

#### Assign licenses 

Cloud Identity Premium uses user-based licensing. If Cloud Identity Premium is your only Google service, everyone in your organization automatically gets a Cloud Identity Premium license.

Otherwise, assign licenses to users after you sign up for Cloud Identity Premium. You can automatically or manually assign licenses to individual users, everyone in an organizational unit, or everyone in your entire organization.

With Cloud Identity on the Annual Plan, you can assign as many licenses as you bought. If you try to manually assign more, you get an error message. If you need more licenses, you can:

  * [Delete or remove a user from your organization](https://support.google.com/a/answer/33314)
  * [Purchase more user licenses](https://support.google.com/a/answer/33387)



#### Automatic license assignment

If licenses aren't assigned by default and everyone in your organization needs Cloud Identity Premium, you can turn on automatic license assignment. This provides a license to users in your account who don't have a Premium license and any new users you add later. Go to [Automatically assign a license to every user in your organization](https://support.google.com/a/answer/1727173#auto).

Existing user licenses for other services don't change on any level.

If you have organizational units under your top-level organization, you can [set automatic licensing options for specific organizational units](https://support.google.com/a/answer/6342682).

#### Manual license assignment

You can manually assign Cloud Identity Premium licenses to individual users, an uploaded list of users, or an entire organizational unit.

For details, go to [Assign, remove, and reassign licenses](https://support.google.com/a/answer/1727173).

If you manually assign licenses to an organizational unit, users in child organizational units automatically receive a license, unless you set the child to override the parent. For details, go to [Set automatic licensing for organizational units](https://support.google.com/a/answer/7610656). 

#### Add licenses

If you need more Cloud Identity Premium users, the way that you add licenses depends on whether you signed up on the Annual or Flexible Plan. For details, go to [Purchase more user licenses](https://support.google.com/a/answer/33387).

During your free trial period for Cloud Identity Premium, you can add up to 50 users. Go to [About your free Cloud Identity Premium trial](https://docs.cloud.google.com/identity/docs/how-to/about-your-free-cloud-identity-premium-trial).

#### Remove or reduce licenses 

If a user no longer needs access to the Cloud Identity Premium features, you can remove the user's license following the steps in [Assign, remove, and reassign licenses](https://support.google.com/a/answer/1727173).

The way to reduce your Cloud Identity Premium license count depends on whether you signed up on the Annual or Flexible Plan. For details, go to [Reduce user licenses](https://support.google.com/a/answer/6154359).

## If you have multiple services

The licensing rules for Cloud Identity vary based on the combination of subscriptions.

If you have Google Workspace for Education or Google Workspace for Nonprofits, you can't add Cloud Identity licenses.

####  Cloud Identity free edition & Premium

If you have both the Premium and free editions of Cloud Identity, all new users automatically get free Cloud Identity licenses. If some users need to use features, like listing allowed applications and rules-based management, assign those users a paid Cloud Identity Premium license.

If you have automatic licensing turned on for Cloud Identity Premium for your entire organization, all new users automatically get paid Premium licenses. To ensure that new users get only free Cloud Identity licenses, we recommend that you turn off automatic licensing for Cloud Identity Premium.

You can set different automatic licensing options for specific organizational units for assigning paid Premium licenses to those users. You can also manually assign Premium licenses to individual users. If you remove a user's Premium license, the user gets a free Cloud Identity license automatically.

**Example:** Say you have 250 total users, and you assign Cloud Identity Premium licenses to 100 of them. You now have:

  * 100 users with both free Cloud Identity and Cloud Identity Premium
  * 150 users with free Cloud Identity only



#### Related topics

  * [Turn off automatic Google Workspace licensing during setup](https://docs.cloud.google.com/identity/docs/how-to/turn-off-automatic-google-workspace-licensing-during-setup)
  * [About automatic licensing for organizational units](https://support.google.com/a/answer/6342682)
  * [Assign, remove, and reassign licenses](https://support.google.com/a/answer/1727173)



####  Cloud Identity free edition & Google Workspace

If you have both Google Workspace and the free edition of Cloud Identity, all new users automatically get free Cloud Identity licenses. If some users need access to features like Gmail and Google Calendar, assign those users a paid Google Workspace license.

If you have automatic licensing turned on for Google Workspace for your entire organization, all new users automatically get paid Google Workspace licenses. To ensure that new users get only free Cloud Identity licenses, we recommend that you turn off automatic licensing for Google Workspace during Cloud Identity setup.

After Cloud Identity setup, you can set different automatic licensing options for specific organizational units to automatically assign paid Google Workspace licenses to those users. You can also manually assign Google Workspace licenses to individual users. If you remove a user's Google Workspace license, they keep their free Cloud Identity license.

**Example:** Say you have 250 total users, and you assign Google Workspace licenses to 100 of them. You now have:

  * 100 users with both free Cloud Identity and Google Workspace
  * 150 users with free Cloud Identity only



#### Related topics

  * [Turn off automatic Google Workspace licensing during setup](https://docs.cloud.google.com/identity/docs/how-to/turn-off-automatic-google-workspace-licensing-during-setup)
  * [Set automatic licensing for organizational units](https://support.google.com/a/answer/7610656)
  * [Assign, remove, and reassign licenses](https://support.google.com/a/answer/1727173)



####  Cloud Identity Premium & Google Workspace

If you have both Google Workspace and Cloud Identity Premium, all new users automatically get paid licenses to whichever service you signed up for first. After you sign up for the second service, you can automatically or manually assign licenses to that service. You can assign a user both types of licenses.

You can change your automatic licensing settings at any time from the Billing page. You can turn automatic licensing on or off for either or both services for your entire organization or an organizational unit.

#### Related topics

  * [Assign, remove, and reassign licenses](https://support.google.com/a/answer/1727173)
  * [Set automatic licensing for organizational units](https://support.google.com/a/answer/7610656)



####  Cloud Identity free edition & Premium & Google Workspace

If you have both editions of Cloud Identity and Google Workspace, all users get a free Cloud Identity license automatically. You can assign a user licenses to one or both of the paid services.

You can't remove a user's free Cloud Identity license. It stays in effect even if you assign licenses to one or both of the paid services.

You can turn on automatic license assignment for one or both of the paid services for your top-level organization. This means all new users in your organization automatically get a license for that service.

You can also set different automatic licensing options for specific organizational units. This way, users in an organizational unit get only the free or paid licenses they need.

If you have automatic licensing turned on for Google Workspace at the top level and then sign up for the free edition of Cloud Identity, during signup, you're prompted to turn off Google Workspace automatic licensing. This ensures that users who only need the free Cloud Identity features are assigned only that license.

If you remove all of a user's paid licenses, the user keeps their free Cloud Identity license.

#### Related topics

  * [Automatically assign a license to every user in your organization](https://support.google.com/a/answer/1727173#auto)
  * [Set automatic licensing for organizational units](https://support.google.com/a/answer/7610656)
  * [Turn off automatic Google Workspace licensing during setup](https://docs.cloud.google.com/identity/docs/how-to/turn-off-automatic-google-workspace-licensing-during-setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
