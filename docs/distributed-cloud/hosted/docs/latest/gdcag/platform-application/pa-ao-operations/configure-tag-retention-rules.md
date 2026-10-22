---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-tag-retention-rules/
title: Configure tag retention rules \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:52.692702+00:00
---

# Configure tag retention rules  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/configure-tag-retention-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Configure tag retention rules Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create and manage tag retention rules for administrators or developers managing and maintaining Harbor repositories. Harbor tag retention rules are a set of policies that automatically manage and optimize image tags within Harbor repositories.

Use tag retention rules to perform the following actions:

  * **Free up storage space** : To avoid accumulating unnecessary data, define rules to retain artifacts for a specific period or manually delete unused image tags.
  * **Maintain a clean repository** : Keep only the most recent or relevant tags to improve organization and discoverability.
  * **Automate tag management** : Avoid manual deletion and streamline the maintenance of your image repositories.



Tag retention rules let you manage images within your repository by automatically deleting image tags you no longer need. Retention rules filters through your tags in three sequential steps to determine which images you want to keep and which to delete:

  1. **Repositories** : Enter the name of the repository. Harbor applies the repository filter first, and applies the retention rule to any repositories that match the repository name. Wildcards such as `*repo`, `repo*`, and `**` are permitted. For more information, see Apply filter with wildcard patterns. For example, you can set the repository filter to `**`, meaning all repositories in the project are included.
  2. **Quantity to retain** : Enter the maximum number of tags or specify a maximum period for which to retain tags. For example, you can set the retention policy to retain the 10 most recently pulled artifacts in each repository.
  3. **Tags to retain** : Enter the name of the image tags you would like to retain. Harbor applies the retention rule to image tags that match the input text. Use the checkbox to select whether you want to capture untagged artifacts as part of the set of artifacts eligible for tag retention or tags that don't have that name. Wild cards such as `*tag`, `tag*`, and `**` are permitted. For more information, see Apply filters with wildcard patterns.



## Before you begin

To manage tag retention rules, you must configure your environment with the necessary resources and permissions. You must also have an existing Harbor repository containing the image tags you want to manage.

### Required Harbor RBAC roles

Unlike GDC IAM roles, configuring tag retention requires specific permissions within Harbor's internal role-based access control (RBAC) system. Request the necessary permissions from your administrator. Enforce least privilege access by requesting only the roles required for your specific tasks.

  * **`ProjectAdmin`** : required to create, edit, disable, or delete tag retention policies within a project. The user that creates the Harbor project is automatically assigned the `ProjectAdmin` role for that project, and can assign roles to other users. For more information on all available roles, see the Harbor documentation on User permissions by role: <https://goharbor.io/docs/2.8.0/administration/managing-users/user-permissions-by-role/>.



## Create a tag retention rule

Harbor retention tag rules follow a specific order and logic. Follow these principles when creating Harbor tag retention rules:

  * Define tag retention rules for repositories, not projects. When you define a retention rule for a repository, you identify the tags to retain.
  * Don't define rules to explicitly remove tags. When you set a rule, the system discards any tags in a repository that you don't identify as being eligible for retention.
  * The `OR` algorithm is used between rules.



Create a tag retention rule using the Harbor console:

  1. Sign in to the Harbor console with an account that has project administrator privileges.
  2. Go to **Projects** and select a project.
  3. In the project window, click the **Policy** tab and then click **Tag Retention**.
  4. Click **Add Rule**.
  5. In the **Repositories** menu, select **matching** or **excluding**.

If you select **matching** , Harbor applies the rule to the repositories you specified. If you select **excluding** , Harbor applies the rule to all of the repositories in the project except for the ones that you identified.

  6. In the **Repositories** box, enter the name of the repositories on which to apply the rule. The following are example text inputs:

     * A repository name such as `example_repo_1`.
     * A comma-separated list of repository names such as `example_repo_1,example_repo_2,example_repo_3`.
     * A partial repository name with wildcards such as `example_*`, `*_3`, or `*_repo_*`.
     * To apply the rule to all of the repositories in the project, use the wildcard `**`.
     * For more information, see Apply filters with wildcard patterns.
  7. In the **By artifact count or number of days** menu, select how many tags to retain or the period to retain tags. Select from the following options:

     * **Retain the most recently pushed # artifacts** : Keep a specific number of artifacts, prioritizing the most recently pushed ones. No age limit applies for artifacts.
     * **Retain the most recently pulled # artifacts** : Keep a specific number of artifacts, prioritizing the most recently pulled ones. No age limit applies for artifacts.
     * **Retain the artifacts pushed within the last # days** : Keep artifacts pushed within a specified timeframe. There is no limit on the number of artifacts.
     * **Retain the artifacts pulled within the last # days** : Keep artifacts pulled within a specified timeframe. There is no limit on the number of artifacts.
     * **Retain always** : Always keep the artifacts matching this rule.
  8. In the **Tags** menu, select **matching** or **excluding**.

If you select **matching** , Harbor applies the rule to the tags you identified. If you select **excluding** , Harbor applies the rule to all of the tags in the repository except for the ones that you identified.

  9. In the **Tags** box, enter the names of the tags on which to apply the rule.

The following are example text inputs:

     * A tag name such as `example_tag_1`.
     * A comma-separated list of tag names such as `example_tag_1,example_tag_2,example_tag_3`.
     * A partial tag name with wildcards such as `example_*`, `*_3`, or `*_tag_*`.
     * To apply the rule to all of the tags in the project, use the wildcard `**`.
     * For more information, see Apply filters with wildcard patterns.
  10. To save the rule, click **Add**.

  11. Optional: To add more rules, click **Add Rule**. You can add a maximum of 15 rules per project.

  12. Optional: In the **Schedule** menu, click **Edit** and select how often to run the rule. If you select **Custom** , enter a cron job command to schedule the rule. If you define multiple rules, Harbor applies the schedule to all of the rules. You can't schedule different rules to run at different times.

  13. To test the rules that you have defined, click **Dry Run**.

  14. To run the rule immediately, click **Run Now**.


**Warning:** You can't revert a rule after you run it. Perform a dry run before you run rules.

### Apply filters with wildcard patterns

Harbor uses doublestar pattern matching. Wildcard patterns are special characters or sequences used to match or represent one or more characters in a string. Use wildcard patterns when you apply filters to your repository or tag names in the creation of tag retention rules. Wildcards offer the following capabilities:

  * Represent one or more characters without specifying them explicitly.
  * Use common wildcards like so:

    * `*`: matches zero or more characters.
    * `?`: matches any single character.

For example, `file*` matches any filename starting with `file`.

  * Allows flexible matching, which is useful when you don't know the exact characters.




Use the following supported wildcard patterns when specifying tag retention rules:

Pattern | Description  
---|---  
`*` | Matches any sequence of non-path separators.  
`**` | Matches zero or more directories.  
`?` | Matches any single non-path-separator character.  
`[class]` | Matches any single non-path-separator character against a class of characters. For more information, see Apply filters with character classes.  
`{alt1,...}` | Matches a sequence of characters if one of the comma-separated alternatives matches.  
  
For more information on doublestar pattern matching, see <https://github.com/bmatcuk/doublestar>.

#### Apply filters with character classes

Character classes and wildcards are both used for pattern matching. Use character classes when you apply filters to your repository or tag names in the creation of tag retention rules. Character classes offer the following capabilities compared to wildcard patterns:

  * Define a set of specific characters that can match at a particular position.
  * Use square brackets (`[]`) to enclose the set. For example, `[aeiou]` matches any single vowel.
  * Allows more precise matching, as you explicitly list the allowed characters.



Use the following character classes to filter through repositories and configure your retention rules:

Class | Description  
---|---  
`[abc]` | Matches any single character within the set.  
`[a-z]` | Matches any single character in the range.  
`[^class]` | Matches any single character that doesn't match the class.  
`[!class]` | Negates the class.  
  
## Update an existing tag retention rule

To modify an existing rule, use the **Action** menu next to a rule to deactivate, edit, or delete that rule.

Use the Harbor console to modify existing tag retention rules:

  1. Sign in to the Harbor interface with an account that has project administrator privileges.
  2. Go to **Projects** and select a project.
  3. In the project window, click the **Policy** tab and then click **Tag Retention**.
  4. To modify an existing rule, use the **Action** menu to select one of the following options:

     * **Disable** : Makes the rule inactive. You can reactivate this rule at a later time.
     * **Edit** : Update the settings of an existing rule.
     * **Delete** : Removes the rule completely.

**Warning:** A rule can't be recovered once it is deleted.

## What's next

After using tag retention rules to optimize your repository, you can check your remaining artifacts to ensure they are secure and ready for deployment. If your artifacts are verified and access permissions are set, you are ready to deploy your secure workloads.

  * [Scan for vulnerabilities](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/scan-vulnerabilities)
  * [Deploy a container app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
