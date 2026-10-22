---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-keep-looker-secure/
title: Best practice: Keeping Looker secure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:17.296132+00:00
---

# Best practice: Keeping Looker secure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-keep-looker-secure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Best practice: Keeping Looker secure Stay organized with collections  Save and categorize content based on your preferences. 

Protect your Looker instance and data by implementing security best practices. These recommendations help you secure your database, product, and content, guarding against unauthorized access and maintaining data integrity.

**Note:** View Looker's security posture on the [Our shared security partnership](https://cloud.google.com/looker/product/security) page.

_These best practices reflect recommendations shared by a cross-functional team of seasoned Looker experts. These insights come from years of experience working with Looker customers, from implementation to long-term success. The practices are written to work for most users and situations, but you should use your best judgment when implementing._

## Database security

Secure your database by limiting Looker to the minimum required access:

  * Configure secure access between the Looker application and your database. Looker documentation provides [several recommendations](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access), including adding Looker IPs to the allowlist, encrypting SSL transmissions, and connecting to databases using an SSH tunnel.
  * Set up the most locked-down database account permissions for Looker that will still allow the application to perform all needed functions. For database-specific setup requirements, see [Database configuration instructions](https://docs.cloud.google.com/looker/docs/dialects).



## Product security

Limit user access to Looker to the minimum functions and data access that each user requires:

  * Set up user authentication, either using Looker's built-in username and password option or, preferably, using a more robust authentication mechanism like [2FA](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-two-factor), [LDAP](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap), [Google OAuth](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google), or [SAML](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml). These methods are mutually exclusive and vary in security level. Google OAuth, for example, allows anyone in your email domain to sign in to Looker.
  * Never post API credentials publicly. API credentials should be stored as environment variables when possible, and should never be shared.
  * Regularly audit any [public access](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls#giving_public_access_to_specific_looks) links your users create, and restrict the permission to create them as necessary. The following [System Activity](https://docs.cloud.google.com/looker/docs/system-activity-pages) Explore can track public Looks:
        
        https://<instance_name.looker.com>/explore/system__activity/look?fields=look.id,look.title,look.public,user.name&f[look.public]=Yes&limit=500&query_timezone=America%2FLos_Angeles&vis=%7B%22type%22%3A%22table%22%7D&filter_config=%7B%22look.public%22%3A%5B%7B%22type%22%3A%22is%22%2C%22values%22%3A%5B%7B%22constant%22%3A%22Yes%22%7D%2C%7B%7D%5D%2C%22id%22%3A0%2C%22error%22%3Afalse%7D%5D%7D&dynamic_fields=%5B%5D&origin=share-expanded
        

  * Set up the most restrictive user permissions and content access that still allow users to carry out their work, paying special attention to who has admin privileges. For a more thorough explanation of these features, see [Secure your folders! A content access walkthrough](https://docs.cloud.google.com/looker/docs/best-practices/how-to-secure-your-folders).

  * Use the [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) parameter, in conjunction with [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes), for applying row-level data security by user or user group.

  * Use [`access_grants`](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant), in conjunction with user attributes, to control access to LookML structures such as Explores, joins, views, and fields by user or group.

  * Use [model sets](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) to apply dataset security within the Looker model. Users will be unable to see any content outside their assigned model set.

  * Avoid assigning users to roles individually whenever possible. Users who are given both individual roles and roles based on group membership _inherit all roles from both the individual and the group assignments_. This can result in users accumulating permissions beyond what they should have. The best practice is to assign roles based only on group membership whenever possible.

  * Most users should be [Viewers](https://docs.cloud.google.com/looker/docs/organizing-spaces#space_access_levels) of the Shared folder (except in closed system setups). This ensures that users will be able to see content in the Shared folders and any subfolders to which they have access. Providing users with Manage Access, Edit permission on the Shared folder means that they will retain those rights within any and all subfolders as well. It can be helpful to make changes lower in the tree first, and THEN revoke access higher up.




## Content security

Implement the appropriate type of Looker system based on the access controls you need to support:

  * **Completely open** : There are no limits to who can see and edit items within the system. The All Users group should be assigned to Manage Access, Edit within the root folder (called _Shared_). For more information about enabling a completely open access system, see [Configuring a completely open system](https://docs.cloud.google.com/looker/docs/access-levels#configuring_a_completely_open_system).
  * **Open with content restrictions** : Content needs to be locked down in some way, either so only certain people can edit certain content, or so certain content is entirely invisible to particular people. When possible, plan for a flatter hierarchy, as this is easier to manage than deeply nested folders. For more details on setting up an open system with restrictions, see [Configuring an open system with restrictions](https://docs.cloud.google.com/looker/docs/access-levels#configuring_an_open_system_with_restrictions).
  * **Closed system** : This system completely separates content across groups, preventing users from different groups from even knowing about the others. A closed system is best for multi-tenant Looker installations. **Before you pursue this option, make sure to read the discussion on[configuring a closed system](https://docs.cloud.google.com/looker/docs/access-levels#configuring_a_closed_system) on the [Designing and configuring a system of access levels](https://docs.cloud.google.com/looker/docs/access-levels) documentation page.** Once a closed system is enabled, it is difficult to change folder management access. This documentation page provides more information about enabling a setup for a Looker instance.



For more information, see the following:

  * [Looker access control and permission management](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management)
  * [Designing and configuring a system of access levels](https://docs.cloud.google.com/looker/docs/access-levels)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
