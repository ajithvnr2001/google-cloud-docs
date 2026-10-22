---
url: https://docs.cloud.google.com/identity/docs/concepts/policy-api-concepts/
title: Policy API concepts \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:04.791452+00:00
---

# Policy API concepts  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/policy-api-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Policy API concepts

This documentation describes Cloud Identity Policy API concepts and strategies.

**Important:** Starting September 1, 2026, an API update will change the `name` and `policyQuery.sortOrder` fields for system-type policies (`SYSTEM`) in the `Policies.list()` and `Policies.get()` methods. To ensure stability when customer SKU subscriptions change, policy resource names will change from edition-specific identifiers to stable, fixed-length priority digits. In addition, the integer portion of the decimal sort order decreases by 1 (for example, 101.00049 becomes 100.00049). This change affects only API response formatting; it does not alter settings, policy restrictions, or the end-user experience.

## Reduction

To list and get policies, see [Setting up the Policy API](https://docs.cloud.google.com/identity/docs/how-to/setup-policies) and [Listing and getting policies](https://docs.cloud.google.com/identity/docs/how-to/list-get-policies).

### Terminology

  * **Setting value** : setting values provided in the policy

  * **Reduced Setting value** : final setting values applied to a target, such as a user, an organization unit, or a group

  * **Reduction** : the process of reducing setting values on policies to a single setting value for a target, such as a user, an organization unit, or a group

  * **Reducer** : the type of rules that determine how setting values on policies are simplified down to a single setting for a user

  * **Admin policies** : policies created by administrators in the Admin console

  * **System policies** : policies provided by Google Workspace




### Reduction Process

To reduce a given setting for a given user:

  1. Filter out all policies that don't apply to the user.

     1. Filter out policies that don't contain the setting.

     2. Filter out policies that apply to the OU that the target user isn't in.

     3. Filter out policies that apply to the Group that the target user isn't in.

     4. Filter out policies that apply to the License that the target user doesn't have. To learn more information about licenses, see the Licenses section.

  2. Apply the Reducer of the given Setting.

     * **Max** : For each field on the reduced setting, the Max reducer chooses the value from the policy with the greatest [sortOrder](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies#policyquery).

     * **Merge** : For each field on the reduced setting, the Merge reducer chooses the value from the policy with the greatest [sortOrder](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies#policyquery) that has a value for that field. If the field is an array, the Merge reducer instead concatenates the values from all the policies.

     * **MaxMap** : The MaxMap reducer is used for settings where the array entries have a field that functions as a primary key. The MaxMap reducer doesn't concatenate the array entries with the same primary key. Instead, it updates the entry using the Max reducer on the other fields in the array entries that share the same primary key.

     * **MergeMap** : The MergeMap reducer is used for settings where the array entries have a field that functions as a primary key. The MergeMap reducer doesn't concatenate the array entries with the same primary key. Instead, it updates the entry using the Merge reducer on the other fields in the array entries that share the same primary key.

     * **List** : These settings are not reduced to a single setting. Instead, the entire sequence of settings is preserved and applied as a list.




### Reducers for settings

**Setting Name** | **Reducer**  
---|---  
`api_controls.custom_user_message` | Max   
`api_controls.google_services` | MaxMap   
`api_controls.internal_apps` | Max   
`api_controls.unconfigured_third_party_apps` | Merge   
`calendar.appointment_schedules` | Max   
`calendar.external_invitations` | Max   
`calendar.interoperability` | Merge   
`calendar.primary_calendar_max_allowed_external_sharing` | Merge   
`calendar.secondary_calendar_max_allowed_external_sharing` | Merge   
`chat.chat_apps_access` | Max   
`chat.chat_file_sharing` | Max   
`chat.chat_history` | Merge   
`chat.external_chat_restriction` | Merge   
`chat.space_history` | Max   
`classroom.api_data_access` | Max   
`classroom.class_membership` | Max   
`classroom.guardian_access` | Max   
`classroom.originality_reports` | Max   
`classroom.roster_import` | Max   
`classroom.student_unenrollment` | Max   
`classroom.teacher_permissions` | Max   
`cloud_sharing_options.cloud_data_sharing` | Max   
`detector.regular_expression` | List   
`detector.word_list` | List   
`drive_and_docs.drive_for_desktop` | Max   
`drive_and_docs.drive_sdk` | Merge   
`drive_and_docs.external_sharing` | Max   
`drive_and_docs.file_security_update` | Max   
`drive_and_docs.general_access_default` | Max   
`drive_and_docs.shared_drive_creation` | Max   
`gmail.attachment_compliance` | MaxMap   
`gmail.auto_forwarding` | Max   
`gmail.blocked_sender_lists` | MaxMap   
`gmail.comprehensive_mail_storage` | Max   
`gmail.confidential_mode` | Max   
`gmail.content_compliance` | MaxMap   
`gmail.email_address_lists` | MaxMap   
`gmail.email_attachment_safety` | Max   
`gmail.email_image_proxy_bypass` | Merge   
`gmail.email_spam_filter_ip_allowlist` | Max   
`gmail.enhanced_pre_delivery_message_scanning` | Max   
`gmail.enhanced_smime_encryption` | Max   
`gmail.imap_access` | Merge   
`gmail.links_and_external_images` | Max   
`gmail.mail_delegation` | Merge   
`gmail.name_format` | Merge   
`gmail.objectionable_content` | MaxMap   
`gmail.per_user_outbound_gateway` | Max   
`gmail.pop_access` | Max   
`gmail.rule_states` | MaxMap   
`gmail.spam_override_lists` | MaxMap   
`gmail.spoofing_and_authentication` | Max   
`gmail.user_email_uploads` | Max   
`gmail.workspace_sync_for_outlook` | Max   
`groups_for_business.groups_sharing` | Merge   
`meet.safety_access` | Max   
`meet.safety_domain` | Max   
`meet.safety_external_participants` | Max   
`meet.safety_host_management` | Max   
`meet.video_recording` | Max   
`rule.dlp` | List   
`rule.system_defined_alerts` | List   
`security.advanced_protection_program` | Max   
`security.less_secure_apps` | Merge   
`security.login_challenges` | Max   
`security.password` | Max   
`security.session_controls` | Max   
`security.super_admin_account_recovery` | Merge   
`security.two_step_verification_device_trust` | Max   
`security.two_step_verification_enforcement` | Max   
`security.two_step_verification_enforcement_factor` | Max   
`security.two_step_verification_enrollment` | Max   
`security.two_step_verification_grace_period` | Max   
`security.two_step_verification_sign_in_code` | Max   
`security.user_account_recovery` | Merge   
`SERVICE_STATUS_APP_NAME.service_status` | Max   
`sites.sites_creation_and_modification` | Max   
`user_takeout` | Max   
`workspace_marketplace.apps_access_options` | Merge   
`workspace_marketplace.apps_allowlist` | MergeMap (primary key is: application_id)   
  
### Licenses

Policies apply to users based on their Workspace licenses. The license condition is provided in `[PolicyQuery](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies#policyquery)`.

For a full list of all Workspace Product and SKU IDs, see [Google Product and SKU IDs](https://developers.google.com/admin-sdk/licensing/v1/how-tos/products).

The following examples demonstrate how policies can be applied to certain groups of users based on those users' licenses.

#### Example 1: Normal clause only

`entity.licenses.exists(license, license in ['/product/Google-Apps/sku/1010020027'])`

The policy applies to a user if they have a license for at least one of the SKUs in the list.

#### Example 2: Normal clause and inverted clause

`entity.licenses.exists(license, license in ['/product/Google-Apps/sku/1010020027']) && !entity.licenses.exists(license, license in ['/product/Google-Apps/sku/1010060005'])`

The policy applies to a user if they have a license for at least one of the SKUs in the first clause. However, if a user has a license for any of the SKUs in the second clause, the policy does not apply to that user at all.

#### Example 3: Inverted clause only

`!entity.licenses.exists(license, license in ['/product/Google-Apps/sku/1010060005'])`

The policy applies to a user if they don't have a license for any SKUs in the list.

### Default Field Values

When a field is not present on the Reduced Setting, its default value is as follows:

**Setting Name** | **Field** | **Default Field Value**  
---|---|---  
`api_controls.google_services` | services  | `[]` (empty list)   
`calendar.external_invitations` | warn_on_invite  | `true`  
`calendar.interoperability` | enable_interoperability  | `false`  
`calendar.primary_calendar_max_allowed_external_sharing` | max_allowed_external_sharing  | `EXTERNAL_FREE_BUSY_ONLY`  
`calendar.secondary_calendar_max_allowed_external_sharing` | max_allowed_external_sharing  | `EXTERNAL_ALL_INFO_READ_ONLY`  
`chat.chat_apps_access` | enable_apps  | `true` in EDU SKUs, `false` in non-EDU SKUs. EDU SKUs: 

  * `/product/Google-Apps/sku/Google-Apps-For-Education`
  * `/product/Google-Apps/sku/1010310002`
  * `/product/Google-Apps/sku/1010310003`
  * `/product/Google-Apps/sku/1010310005`
  * `/product/Google-Apps/sku/1010310006`
  * `/product/Google-Apps/sku/1010310007`
  * `/product/Google-Apps/sku/1010310008`
  * `/product/Google-Apps/sku/1010310009`
  * `/product/Google-Apps/sku/1010310010`
  * `/product/Google-Apps/sku/1010460001`
  * `/product/Google-Apps/sku/1010460002`

  
enable_webhooks  | `true` in EDU SKUs, `false` in non-EDU SKUs. EDU SKUs: 

  * `/product/Google-Apps/sku/Google-Apps-For-Education`
  * `/product/Google-Apps/sku/1010310002`
  * `/product/Google-Apps/sku/1010310003`
  * `/product/Google-Apps/sku/1010310005`
  * `/product/Google-Apps/sku/1010310006`
  * `/product/Google-Apps/sku/1010310007`
  * `/product/Google-Apps/sku/1010310008`
  * `/product/Google-Apps/sku/1010310009`
  * `/product/Google-Apps/sku/1010310010`
  * `/product/Google-Apps/sku/1010460001`
  * `/product/Google-Apps/sku/1010460002`

  
`chat.chat_history` | enable_chat_history  | `false`  
history_on_by_default  | `false`  
allow_user_modification  | `true`  
`chat.external_chat_restriction` | allow_external_chat  | `false`  
external_chat_restriction  | `NO_RESTRICTION`  
`chat.chat_and_space_restrictions` | restriction_level  | `UNRESTRICTED`  
`devices.android_available_apps` | playstore_installable_apps  | `ALL`  
`devices.android_verify_apps` | turnoff_google_play_protect_allowed  | `false`  
`devices.android_developer_options` | allowed  | `false`  
`devices.android_work_data_sync` | allowed  | `true`  
`devices.android_work_profile_sharing` | allowed  | `false`  
`devices.ios_apple_watch` | no_wrist_detection_usage_allowed  | `true`  
`devices.ios_backup_encryption` | required  | `false`  
`devices.ios_data_actions` | external_data_sharing_allowed  | `true`  
work_data_operation_type.non_workspace_apps_copy_paste_allowed  | `true`  
work_data_operation_type.non_workspace_apps_sharing_allowed  | `true`  
work_data_operation_type.personal_accounts_sharing_allowed  | `true`  
work_data_operation_type.airdrop_sharing_allowed  | `true`  
work_data_operation_type.files_printing_allowed  | `true`  
work_data_operation_type.files_access_allowed  | `true`  
work_data_operation_type.images_videos_saving_allowed  | `true`  
work_data_operation_type.contacts_items_assignment_allowed  | `true`  
`devices.ios_handoff` | allowed  | `true`  
`devices.ios_icloud_backup` | allowed  | `true`  
`devices.ios_lock_screen_control_center` | allowed  | `true`  
`devices.ios_lock_screen_notifications_view` | allowed  | `true`  
`devices.ios_safari_secure_browsing` | fraudulent_website_warning_enforced  | `true`  
`devices.android_google_play_private_apps` | access_allowed  | `false`  
publish_and_update_allowed  | `false`  
`devices.android_screen_capture` | allowed  | `true`  
`devices.compromised_devices` | compromised_android_devices_blocked  | `false`  
jailbroken_ios_devices_blocked  | `false`  
`devices.encryption` | device_encryption_option  | `NOT_REQUIRED`  
`devices.ios_icloud_storage` | managed_apps_sync_allowed  | `true`  
`devices.ios_screen_capture` | allowed  | `true`  
`devices.ios_keychain_sync` | icloud_sync_allowed  | `true`  
`devices.ios_document_sync` | icloud_data_sync_allowed  | `true`  
`devices.android_location_sharing` | allowed  | `true`  
`devices.android_apps_settings` | modification_allowed  | `true`  
`devices.android_trust_agents` | smart_lock_allowed  | `true`  
`devices.android_lock_screen_notifications` | allowed  | `true`  
`devices.android_lock_screen_notification_details` | allowed  | `true`  
`devices.android_unknown_source_apps` | work_profile_installation_allowed  | `false`  
personal_profile_installation_allowed  | `true`  
`directory.external_directory_setting` | sharing_option  | `ORGANIZATION_DIRECTORY_DATA`  
`drive_and_docs.drive_sdk` | enable_drive_sdk_api_access  | `true`  
`drive_and_docs.external_sharing` | external_sharing_mode  | `ALLOWED`  
allow_receiving_external_files  | `true`  
warn_for_sharing_outside_allowlisted_domains  | `true`  
allow_non_google_invites_in_allowlisted_domains  | `false`  
allow_receiving_files_outside_allowlisted_domains  | `true`  
warn_for_external_sharing  | `true`  
allow_non_google_invites  | `true`  
allow_publishing_files  | `true`  
access_checker_suggestions  | `RECIPIENTS_OR_AUDIENCE_OR_PUBLIC`  
allowed_parties_for_distributing_content  | `ALL_ELIGIBLE_USERS`  
`drive_and_docs.general_access_default` | default_file_access  | `LINK_SHARING_PRIVATE`  
`gmail.auto_forwarding` | enable_auto_forwarding  | `true`  
`gmail.email_image_proxy_bypass` | image_proxy_bypass_pattern  | `[]` (empty list)   
enable_image_proxy  | `true`  
`gmail.email_spam_filter_ip_allowlist` | allowed_ip_addresses  | `[]` (empty list)   
`gmail.links_and_external_images` | apply_future_settings_automatically  | `true`  
enable_aggressive_warnings_on_untrusted_links  | `false`  
`gmail.mail_delegation` | enable_mail_delegation  | `false`  
`gmail.smime_encryption` | enable_smime_encryption  | `STATUS_DISABLED`  
allow_sha1_globally_in_smime_signature  | `false`  
`gmail.spoofing_and_authentication` | apply_future_settings_automatically  | `true`  
`gmail.user_email_uploads` | enable_mail_and_contacts_import  | `false`  
`gmail.workspace_sync_for_outlook` | enable_google_workspace_sync_for_microsoft_outlook  | `true`  
`gmail.external_recipient_warning` | enabled  | `true`  
`groups_for_business.groups_sharing` | collaboration_capability  | `DOMAIN_USERS_ONLY`  
create_groups_access_level  | `USERS_IN_DOMAIN`  
view_topics_default_access_level  | `DOMAIN_USERS`  
owners_can_allow_external_members  | `false`  
owners_can_allow_incoming_mail_from_public  | `true`  
owners_can_hide_groups  | `false`  
new_groups_are_hidden  | `false`  
`security.less_secure_apps` | allow_less_secure_apps  | `false`  
`security.password` | allowed_strength  | `STRONG`  
minimum_length  | `8`  
maximum_length  | `100`  
enforce_requirements_at_login  | `false`  
allow_reuse  | `false`  
expiration_duration  | `0`  
`security.super_admin_account_recovery` | enable_account_recovery  | `false`  
`security.two_step_verification_device_trust` | allow_trusting_device  | `true`  
`security.two_step_verification_enforcement` | enforced_from  | Unset   
`security.two_step_verification_enforcement_factor` | allowed_sign_in_factor_set  | `ALL`  
`security.two_step_verification_enrollment` | allow_enrollment  | `true`  
`security.two_step_verification_grace_period` | enrollment_grace_period  | `0s`  
`security.user_account_recovery` | enable_account_recovery  | `false`  
`workspace_marketplace.apps_access_options` | access_level  | For K12 customers: `ALLOW_NONE` Otherwise: `ALLOW_ALL`  
allow_all_internal_apps  | `false`  
`workspace_marketplace.apps_allowlist` | apps  | `[]` (empty list)   
  
## System Groups

Google system groups are groups that aren't surfaced in the [Groups API](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/get) and are linked to system policies. Their group IDs aren't prefixed with `groups/`, unlike other group IDs. The following table lists these groups and the users that belong to them.

**GroupId** | **Users who are part of this group**  
---|---  
`WORKSPACE_ALL_ADMIN_GROUP` | All administrators.   
`UNCONSENTED_CHILD_GROUP` | [EDU](https://knowledge.workspace.google.com/admin/getting-started/editions/google-workspace-for-education-editions) users designated as under 18 lacking parental [consent](https://knowledge.workspace.google.com/admin/getting-started/editions/manage-access-to-additional-services-for-users-designated-as-under-18) confirmation for one or more additional services.   
  
## Unsupported SKU Licenses

SKUs that are not supported by the [license manager API](https://developers.google.com/workspace/admin/licensing/reference/rest?apix=true) are not present in the standard format:

`entity.licenses.exists(license, license in ['/product/{productId}/sku/{skuId}'])`

Instead, they are represented with a placeholder in the query string:

`entity.licenses.exists(license, license in ['{placeholder}'])`

For example:

`entity.licenses.exists(license, license in ['CHROMEBOOK-SOFTWARE'])`

The following table lists these SKUs and their corresponding placeholders.

**Product Name** | **Product ID** | **SKU ID** | **Placeholder**  
---|---|---|---  
Chromebook Software  | `Google-Chrome-Device-Management` | `Google-Chrome-Device-Management-Perpetual` | `CHROMEBOOK-SOFTWARE`  
`Google-Chrome-Device-Management`  
`Chrome-Active-Directory`  
Cloud Identity  | `101001` | `1010010001` | `GOOGLE-IDENTITY`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
