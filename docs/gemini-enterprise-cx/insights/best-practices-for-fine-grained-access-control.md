---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/best-practices-for-fine-grained-access-control/
title: Best practices for fine-grained access control \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:27.117696+00:00
---

# Best practices for fine-grained access control  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/best-practices-for-fine-grained-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Best practices for fine-grained access control Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can grant users access to specific portions of your conversation data, without giving them access to the entire dataset. This fine-grained access control is possible when you use authorized views. The following recommendations contain the best practices for implementing fine-grained access control with authorized views.

## Scope authorized views

Properly scoping authorized views ensures that users only have access to the data they need. Scoping views involves carefully defining the data that each authorized view exposes. A properly scoped view limits access to only the necessary data, while an improperly scoped view might expose more data than intended.

  * **Filter data carefully:** Use the filter expression to define the exact data that each authorized view should expose. Ensure that the filter is specific enough to meet the needs of the user.
  * **Use`agent_id` for agent-specific views:** When creating authorized views for agents, use the `agent_id` field to filter conversations. This ensures that each agent only has access to their own conversations. 
    * For example, a filter expression for an agent named Carol would be `agent_id = "agent-carol"`.
  * **Use`agent_id` for manager-specific views:** When creating authorized views for managers, use the `agent_id` field to filter conversations for their respective teams. 
    * For example, a manager responsible for agents Carol and Dave could use the filter expression `agent_id = "agent-carol" or agent_id = "agent-dave"`.
  * **Avoid empty filters:** Empty filters or `""` allow unrestricted access.



## Use authorized view sets for organization

Authorized view sets help you organize and manage related authorized views. Grouping related views into sets simplifies the process of granting access to multiple views at once.

Follow these guidelines for grouping your authorized views into sets:

  * **Group related views:** Use authorized view sets to group authorized views for related roles. 
    * For example, you can create an authorized view set called `manager-views` to group all authorized views for managers.
  * **Grant access through authorized view set level:** Instead of granting roles on individual authorized views, grant roles on authorized view sets. 
    * For example, grant the `roles/contactcenterinsights.viewer` role to the `agent-views` authorized view set, which contains all authorized views for agents.



## Grant project access

Granting project access is a prerequisite for users to use the console and interact with project resources.

  * **Grant`roles/browser` to all authorized users:** This role allows users to view the project and its resources. This is a prerequisite for using the console.



## Principle of least privilege

The principle of least privilege is a security best practice that ensures users only have the permissions necessary to perform their tasks. This principle helps to minimize the risk of unauthorized access to data and resources.

Follow these guidelines for applying the principle of least privilege:

  * **Grant the minimum necessary permissions:** Only grant the permissions required for a user to perform their tasks. Avoid giving overly broad access.
  * **Use predefined roles:** Use `roles/contactcenterinsights.editor` and `roles/contactcenterinsights.viewer` to grant project-level permission for authorized views. Use `roles/contactcenterinsights.authorizedEditor` and `roles/contactcenterinsights.authorizedViewer` for users on specific authorized views to grant them access through those views.
  * **Avoid project-level grants for authorized view set permissions:** Granting authorized view set permissions at the project level results in users having access to all authorized view sets. Instead, grant these roles on the specific authorized view sets.
  * **Use the principle of least privilege when granting project-level access for authorized views:** Only grant the minimum necessary permissions for an authorized view. A user's permissions cannot exceed the permissions of the authorized view to the project. Example: If authorized view `view-123` has `roles/contactcenterinsights.viewer` and a user has `roles/contactcenterinsights.authorizedEditor` on authorized `view-123`, the user can't edit anything because the view's permissions restrict the final permissions.
  * **Use the principle of least privilege when granting access to authorized views:** Only grant the minimum necessary permissions to authorized views. For example, if a user only needs to view data for a specific team, grant them the `roles/contactcenterinsights.authorizedViewer` role on the authorized view set for that team. 
    * By granting roles to authorized view sets, you can manage permissions for multiple views at once. This reduces the complexity of managing permissions and ensures that users only have access to the data they need.
    * For example, a manager might have the `roles/contactcenterinsights.authorizedEditor` role on an authorized view set for their team, while an agent might have the `roles/contactcenterinsights.authorizedViewer` role on an authorized view set for their own conversations.



## Use descriptive display names

Descriptive display names make it easier to understand and manage your authorized views and sets. Using meaningful names helps to quickly identify the purpose of each resource.

Follow these guidelines for using descriptive display names:

  * **Use meaningful display names:** When creating authorized views and authorized view sets, use descriptive display names that clearly indicate the purpose of the view or set. This makes it easier to understand and manage your resources. 
    * For example, instead of `view1`, use a display name like **Manager Team A Conversations** or **Agent Carol's Conversations**.
  * **Follow a consistent naming convention:** Establish a consistent naming convention for your authorized views and sets. This will make it easier to find and manage your resources. 
    * For example, you could use a convention like `[Role] - [Team/Agent]`.



## Minimize the amount of views per user

Minimizing the number of views per user helps to simplify access management and ensures that users only have access to the data they need.

  * **Isolate user access:** Avoid sharing authorized views between different users. This ensures that each user only has access to the data they need. 
    * Instead, combine filter expressions for a single user with `OR` into a single authorized view.
    * This reduces the need for a user to switch views.
  * **Create unique authorized views for each user per role:** Create a unique authorized view for each role per user. This ensures that each user has the appropriate level of access. 
    * For example, create a separate view for a manager's edit access to conversations and their view access to conversations.



## Specify derived identifiers

Derived identifiers help to identify resources without needing to store mappings. This can simplify the management of your authorized views.

  * **Use derived IDs:** Derive IDs from the role and the group of conversations. For example, an authorized view for a manager role for a specific team could have an ID like `manager-team-a`. This helps to identify the resource without having to store additional state. 
    * For example, an authorized view for a manager named Bob, managing team A, could have an ID like `manager-bob-team-a`. An authorized view for an agent named Carol could have an ID like `agent-carol`.



## Regularly review and update permissions

Regularly reviewing and updating permissions ensures that users have the appropriate level of access to the data they need. This helps to maintain security and compliance.

Follow these guidelines for updating permissions:

  * **Revoke unnecessary access:** Remove permissions from users who no longer require them.
  * **Update filters:** Update filter expressions on authorized views as needed to reflect changes in the organization or business needs.



## Understand limitations

Authorized views have certain limitations in terms of what they can be used for. It's important to understand these limitations when designing your access control strategy.

Authorized views have the following limitations:

  * **Cannot edit or import conversation data:** Authorized views cannot be used to edit or import conversation data.
  * **Cannot train topic models or create score cards:** Authorized views cannot be used to train topic models or create score cards.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
