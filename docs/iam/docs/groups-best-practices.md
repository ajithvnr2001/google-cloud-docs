---
url: https://docs.cloud.google.com/iam/docs/groups-best-practices/
title: Best practices for using Google groups \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:02.186314+00:00
---

# Best practices for using Google groups  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/groups-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Best practices for using Google groups Stay organized with collections  Save and categorize content based on your preferences. 

This document describes some best practices for using Google groups to manage access to Google Cloud resources with Identity and Access Management (IAM).

## Types of groups

The types of groups listed here are one way to think about, use, and manage Google groups. These group types aren't set by any Google group attribute. However, using these group types in your overall approach to Google group management can help you avoid some common security pitfalls.

This document uses the following types of groups:

  * **Organizational groups**

Organizational groups represent subsets of an organization's structure, and are typically sourced from human resources data. They might be based on department, reporting structure, geographic location, or other organizational groupings.

The members of an organizational group change when an employee joins the organization, moves to a different department, or leaves the organization.

The overall structure of organizational groups can change when the business reorganizes. A reorganization might lead to new groups being created, or existing groups being retired.

Some examples of organizational groups include `org.marketing-fte`, `org.finance-all`, `org.msmith-reports`, `org.apac-all`, and `org.summer-interns`.

Organizational groups are typically used for email communication.

  * **Collaboration groups**

Collaboration groups represent workgroups, project members, or users that want to collaborate on a project or discuss a specific topic.

The structure of collaboration groups isn't linked to any organizational structure. They are often created on an ad hoc, self-service basis.

Membership in collaboration groups can be unrestricted, allowing anybody in the organization to join. Alternatively, a collaboration group can be self-managed, meaning that certain members can decide who else to include in the group.

Some examples of collaboration groups include `collab.security-discuss` and `collab.website-relaunch`.

Collaboration groups are typically used for email communication.

  * **Access groups**

Access groups are used for the sole purpose of providing access. They represent job functions and are used to simplify the assignment of roles required to perform these job functions. Instead of granting roles to individual principals, you grant roles to the group, and then manage group membership.

The structure of access groups is influenced by the structure of the resources or workloads in your organization. The deployment of a new resource or workload might require the creation of new access groups.

Membership in access groups is generally controlled by one or more group owners, who either invite users to the group or approve users' requests to join the group.

Some examples of access groups include `access.prod-firewall-admins`, `access.finance-datamart-viewers`, and `access.billing-dashboard-users`.

Access groups are used only to provide access. They are not used for communication purposes.

  * **Enforcement groups**

Enforcement groups are similar to access groups, except that they're used to enforce access restriction policies rather than providing access.

The structure of enforcement groups is typically influenced by a combination of compliance requirements and organizational structure.

Membership in an enforcement group is typically determined by a set of predefined rules that look at a user's clearance level, location, or role in the organization.

Some examples of enforcement groups include `enforcement.users-in-restricted-locations`, `enforcement.fedramp-low`, and `enforcement.sso-users`.

Enforcement groups are used only to enforce access restriction policies. They are not used for communication purposes.




## Name your groups to reflect their type

To help you follow the best practices in the rest of this document, use group names that let you determine the type of a group from its name. You can use a naming convention or secondary domains.

### Naming convention

Here is one example of a naming convention to make the group type visible:

  * Organizational groups: `org.GROUP_NAME@example.com`. For example, `org.finance-all@example.com`.

  * Collaboration groups: `collab.TEAM_NAME@example.com`. For example, `collab.msmiths-team@example.com`.

  * Access groups: `access.JOB_FUNCTION@example.com`. For example, `access.billing-dashboard-users@example.com`.

  * Enforcement groups: `enforcement.GROUP_DESCRIPTION@example.com`. For example, `enforcement.sso-users@example.com`.




Adopt the convention that works for your organization and is supported by your group management software. Using a prefix alphabetizes your groups by function, but some group management systems, such as [Groups for Business](https://support.google.com/a/answer/9689189), support only suffixes. If you can't use prefixes, you can use suffixes or secondary domains.

### Secondary domains

As an alternative to naming conventions, you can use secondary domains to embed the group type into the name—for example, `access.example.com`. Secondary domains that are a subdomain of a verified domain don't require verification and don't need to exist in DNS. Furthermore, by not creating DNS Mail Exchange (MX) records for the secondary domains, you can block inbound emails from coming to groups that aren't intended for communication.

## Nesting rules

Different types of groups have different rules for whether nesting (accepting a group as a member) is allowed.

### Nesting rules for organizational groups

Nesting organizational groups to reflect your org chart is a best practice. This approach means that every employee is included in one group and then the groups include each other. For example, the `org.finance-all` group might contain the groups `org.finance-us`, `org.finance-germany`, and `org.finance-australia` as members.

You can add organizational groups to any of the other group types as members. This can be much easier than having to add every member of an organizational group to another group.

Don't add any other group type to an organizational group as a member. Don't use access, enforcement, or collaboration groups as part of an organizational hierarchy.

### Nesting rules for collaboration groups

Every collaboration group should have a well-defined set of policies that determine how members are added. If two collaboration groups follow the same membership policies, they can be nested. However, nesting collaboration groups with different membership policies can let members that don't meet the membership policies of a group become members. Review the membership policies carefully before nesting collaboration groups.

Collaboration groups can have organizational groups as members.

### Nesting rules for access groups

Typically, you shouldn't nest access groups. Nesting access groups can make it difficult to determine who has access to what resources. Additionally, nesting access groups with different access policies might let principals bypass strict access group membership policies.

Access groups can have organizational groups as members.

### Nesting rules for enforcement groups

Don't nest enforcement groups. Nesting enforcement groups can make it difficult to determine why a principal is being denied access. Additionally, nesting enforcement groups with different membership policies might cause some principals to be affected by unintended restrictions.

Enforcement groups can have organizational groups as members.

## Manage organizational groups

Use the following best practices to manage your organizational groups.

### Provision from a single source of truth

Because organizational groups are based on human resources data, it's best to provision these groups exclusively from a human resources information system or from an external source of truth—for example, an external identity provider (IdP) or an identity governance system such as Sailpoint, Okta, or Entra ID.

### Don't allow group modifications

Don't add or remove users from an organizational group manually, and don't let users remove themselves from an organizational group.

**Note:** Preventing users from leaving a Google group requires changing a default setting by using the [Groups Settings API](https://developers.google.com/admin-sdk/groups-settings/concepts) to set the `whoCanLeaveGroup` property to `NONE_CAN_LEAVE`.

### Avoid using organizational groups to provide access to resources

All users in an organizational group rarely need the same level of access to resources. For this reason, granting access to an organizational group is likely to result in some members of the group having more access than they actually need.

In addition, there can be a delay between when changes are made in an external IdP and when they are propagated to Cloud Identity, based on the synchronization frequency from the external IdP to Cloud Identity. This delay can lead to the proliferation of excess permissions. For example, it might lead resource owners to grant access to existing groups instead of creating a new group, even if those existing groups contain people who don't need to access the resource.

If you must provide access using an organizational group, add the organizational group as a member to an access group, rather than granting access directly, and only grant roles with limited permissions, such as Organization Viewer. Otherwise, use access groups to provide access to resources.

### Don't allow service accounts and external users in organizational groups

Don't include service accounts in organizational groups, because they don't represent people.

External users—users from a different Google Workspace or Cloud Identity account—typically aren't part of your organization, so there's no reason for them to be a member of an organizational group. If you onboard your external workforce to your own Google Workspace or Cloud Identity account, then they are considered internal users, and can be included in your organizational groups.

Use [Cloud Identity security groups](https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group) and [group restrictions](https://support.google.com/a/answer/11192679) to enforce these rules.

## Manage collaboration groups

Use the following best practices to manage your collaboration groups.

### Use Groups for Business to manage collaboration groups

If you're using Google Workspace, you can use [Groups for Business](https://support.google.com/a/answer/10308022) to manage collaboration groups. This lets users use [Google Groups](https://groups.google.com) to create, browse, and join groups. You must configure Groups for Business to let users create new collaboration groups.

### Disable Groups for Business if you don't use it

If you're using Cloud Identity but not Google Workspace, then there's no reason to have any collaboration groups in Cloud Identity, so it's best to [disable Groups for Business](https://support.google.com/a/answer/167096) to prevent your users from creating groups in Cloud Identity.

### Force a suffix for collaboration groups

If you are using Groups for Business, configure it to [enforce a suffix](https://support.google.com/a/answer/9689189). This is especially important if you allow everybody to create new Groups for Business groups.

Enforcing a suffix prevents users from creating a group with a name that intentionally collides with an access group or organizational group that is about to be provisioned from an external source. This scenario could allow the creator of the falsely-named collaboration group to escalate their privileges.

### Don't use collaboration groups for access control

Collaboration groups are meant to have loose access control, and typically don't follow a well-defined lifecycle. That makes them good for collaboration, but bad for access control.

If you've strictly followed a naming convention for your collaboration groups, then you can [create a custom organization policy constraint](https://docs.cloud.google.com/iam/docs/org-policy-custom-constraints) to prevent collaboration groups from being granted IAM roles. 

Similarly, if you provision and manage your collaboration groups externally, then don't provision them to Cloud Identity, which would let them be misused for access control purposes.

## Manage access groups

Use the following best practices to manage your access groups.

### Select the right tool to manage your access groups

Because access groups are managed by workload owners, use a tool suited to self-service. Your tool should let users find existing access groups, and enforce security guardrails that apply the following controls:

  * Who (members of which organizational group) is eligible to join an access group
  * What requirements must be met for a user to join a group

For example, do users need to provide justification?

  * Maximum lifetime for group membership

  * If membership must be approved, and by who

  * Audit trail support




One tool that fits these requirements is [JIT Groups](https://googlecloudplatform.github.io/jit-groups/).

### Use access groups to model job functions and grant access to resources

Create an access group for each job function and grant it access to all resources that users in that job function need. Then, you can add users in that job function to the group to give them the access they need instead of granting the same roles to each individual user.

You can use a single access group to provide access to multiple resources, or even multiple projects. However, make sure that each group member needs the access that you grant to the group. If some users don't need the additional access, create a new access group and grant that group the additional access instead.

### Use your access groups for a specific workload

Reusing access groups for multiple workloads leads to excessive permissioning and administration complexity.

### Remove barriers to creating access groups for workload owners

To reduce the temptation to reuse an existing access group, make access groups straightforward to create and maintain. Workload owners should be able to create access groups on a self-service basis, with support for proper naming.

### Empower users to find and join access groups

If users can discover existing access groups and join the ones they need, they will be less likely to accumulate unneeded privileges. If needed, you can use an invitation or approval process to control who can join the group.

### Let memberships auto-expire by default

Require users to re-join an access group or extend their membership after a period of time. This practice intentionally adds friction to remain a member of an access group, and creates an incentive to let unneeded memberships lapse. This best practice is critical for achieving the goal of Zero Standing Privileges (ZSP), and is especially important for external users.

Don't apply this rule to service accounts, however, because removing service accounts from an access group can result in service interruptions.

### Give each group designated owners

Every access group should have one or more designated owners. This encourages a sense of responsibility for group membership. The owners can be the same person or team that owns the workload associated with the group.

### Limit visibility of access groups

Don't make access groups visible in the Groups directory. (They _should_ be discoverable in your access group management tool.) In addition, allow only group members the ability to see who else is a member. These practices prevent bad actors from gaining valuable information.

### Limit external members

Because [domain-restricted sharing (DRS) policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) apply to groups, but not to group members, access groups that allow external members can create a loophole that undermines DRS.

Use [Cloud Identity security groups](https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group) and [group restrictions](https://support.google.com/a/answer/11192679) to allow or disallow external members for access groups. In addition, consider using a special naming convention, such as `external.access.GROUP_NAME@example.com`, for access groups that allow external members.

## Manage enforcement groups

Use the following best practices to manage your enforcement groups.

### Select the right tool to manage your enforcement groups

Because membership in enforcement groups is based on organizational rules, and used to apply security restrictions, don't let members opt out or remove themselves from an enforcement group.

Using [dynamic groups](https://docs.cloud.google.com/identity/docs/concepts/overview-dynamic-groups) lets you automate enforcement group provisioning. If you're using an external IdP, use the dynamic groups provided by the IdP and then provision them to Cloud Identity. Keep in mind that using an external IdP can introduce a delay for policy updates.

If you can't use dynamic groups, consider using Terraform or some other Infrastructure as Code (IaC) tool to provision your enforcement groups. If you use IaC to create enforcement groups, make sure you don't give unnecessarily broad access to the pipeline.

### Use enforcement groups for mandatory access control and authentication controls

Use enforcement groups to enforce [mandatory access control](https://en.wikipedia.org/wiki/Mandatory_access_control). Google Cloud supports mandatory access control with a number of services and tools, including the following:

  * [IAM deny policies](https://docs.cloud.google.com/iam/docs/deny-overview)
  * [IAM principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)
  * [Chrome Enterprise Premium access bindings](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-console-and-apis#create-access-binding)
  * [Google Workspace service turn off](https://support.google.com/a/answer/182442)



Enforcement groups are also used to apply authentication controls such as SAML profile assignment or 2-Step Verification (2SV).

Because these controls all restrict features or remove access, enforcement groups are the right choice.

### Don't allow users to leave an enforcement group

Allowing users to leave an enforcement group goes against the principles of mandatory access control. To disallow users from leaving the group, use the [Groups Settings API](https://developers.google.com/admin-sdk/groups-settings/concepts) to set the `whoCanLeaveGroup` property to `NONE_CAN_LEAVE`.

## Best practices for external IdPs

If you're using an external IdP for authentication, then it can be useful to also use that IdP for provisioning organizational groups and enforcement groups.

### Avoid using an external source for access groups

It's possible to manage access groups in the external IdP and provision them to Cloud Identity, but there are several disadvantages to this approach:

  * Provisioning delays

It can take up to several hours for changes made in the external IdP to be reflected in the access group.

  * Risk of divergence

Some IdPs don't take authoritative control of groups. For example, they might not delete a group in Cloud Identity after it's deleted externally, or actively delete group members that exist in Cloud Identity but not in the IdP.

Divergence can cause users to retain access they don't need, and gives them incorrect information about who has access. It can also add friction to creating access groups.




To avoid these pitfalls, use external IdPs to provision only organizational and enforcement groups, and use a tool such as [JIT Groups](https://googlecloudplatform.github.io/jit-groups/) to manage access groups _directly_ in Cloud Identity.

### Use a secondary domain if you're mapping groups by name

Cloud Identity identifies groups by email address, but groups in your external IdP might not have an email address.

Many IdPs let you work around this by letting you derive a pseudo email address from the group's name, such as using `my-group@example.com`. This works, but can lead to collisions when this email address is already used by a different group or user. In the worst case, this naming collision could be exploited by a bad actor to create security groups that masquerade as another, less scrutinized group type.

To avoid the risk of collisions, use a dedicated secondary domain for groups that you provision from the external source, such as `groups.example.com`.

## Avoid granting the Groups Admin role to deployment pipelines

If you use IaC to manage groups (for example, Terraform), your deployment pipeline must have the required permissions to accomplish its task. The Groups Admin role authorizes group creation, but it also lets any principal with that role manage all groups in the Cloud Identity account.

You can restrict the access given to a pipeline by creating a service account with just one permission (the ability to create a group) and then by making the pipeline the owner of any group it creates. That lets that pipeline manage any group it creates, and create more groups, without authorizing it to manage any group it did not create.

The following steps outline this approach:

  1. [Create a custom admin role](https://support.google.com/a/answer/2406043) that includes only the Admin API group create permission.

Give this role a descriptive name, such as Group Creator.

  2. Create a service account and assign it the Group Creator role.

  3. Use the service account for your pipeline and pass the `WITH_INITIAL_OWNER` flag at group creation time.




## Use Cloud Logging to audit and monitor your groups.

[Logging](https://docs.cloud.google.com/logging/docs/overview) lets you collect, monitor, and analyse group activity.

### Audit membership changes

Adding or removing a member of an organizational group, access group, or enforcement group can affect what resources the member has access to, so it's important to keep an audit trail that tracks these changes.

### Require justifications for joining access groups

To make your monitoring data more useful, require users to provide a justification when they join a group, or request to join a group, and log the justification. If there is an approval process, log details about who approved the request.

This additional metadata can later help you analyze why somebody was added to a group and by extension, why they were given access to certain resources.

### Enable Cloud Identity audit log sharing

Configure Cloud Identity to [route logs to Cloud Logging](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs) so that you can handle these audit logs the same way as other Google Cloud logs, including setting up alerts or use an external Security information and event management (SIEM) system.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
