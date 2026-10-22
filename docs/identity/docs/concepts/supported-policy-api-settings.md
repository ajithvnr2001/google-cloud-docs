---
url: https://docs.cloud.google.com/identity/docs/concepts/supported-policy-api-settings/
title: Settings available in the API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:25.715681+00:00
---

# Settings available in the API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/supported-policy-api-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Settings available in the API

This document describes the settings that the Policy API supports.

If the supported settings are missing from the Cloud Identity Policy API response, see [Default field values](https://docs.cloud.google.com/identity/docs/concepts/policy-api-concepts#default_field_values). If the missing setting is not mentioned in [Default field values](https://docs.cloud.google.com/identity/docs/concepts/policy-api-concepts#default_field_values), contact [Cloud Customer Care](https://cloud.google.com/support-hub).

## API Controls

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**API controls** | **Settings > Custom user message** | `api_controls.custom_user_message` | No  | **Customize the message to show users when they can't access an app due to access settings.** | error_text  | string   
**Settings > Unconfigured third-party apps** | `api_controls.unconfigured_third_party_apps` | No  | **Unconfigured third-party apps are apps that haven't been configured with an access setting (like trusted, limited, or blocked).  
Select what happens when _users_ try to access unconfigured third-party apps with their account.** | access_level  | enum: 

  * `ACCESS_LEVEL_UNSPECIFIED`
  * `BLOCK_ALL`
  * `ALLOW_SIGN_IN_ONLY`

  
**Settings > Unconfigured third-party apps** | `api_controls.unconfigured_third_party_apps` | No  | **Unconfigured third-party apps are apps that haven't been configured with an access setting (like trusted, limited, or blocked).  
Select what happens when _users under 18_ try to access unconfigured third-party apps with their account.** | access_level_under18  | enum: 

  * `ACCESS_LEVEL_UNSPECIFIED`
  * `ALLOW_SIGN_IN_ONLY`

  
**Settings > Internal apps** | `api_controls.internal_apps` | No  | **Internal apps owned by your organization are automatically configured with trusted access. These apps can ask for API access to all Google data for users.** | trust_internal_apps  | boolean   
**Settings > User requests to access unconfigured apps** | `api_controls.app_approval_requests` | No  | **Allow users to request access to unconfigured third-party apps** | allowed_for_all  | enum: 

  * `OPTION_UNSPECIFIED`
  * `ENABLED`
  * `DISABLED`

  
**App access control > Manage Google Services > Google services** | `api_controls.google_services` | No  | **Select access settings for Google service APIs to control what kind of third-party apps can request access to these services.** | services  | Service[]   
**Note:** The field `access_level_under18` in the setting `api_controls.unconfigured_third_party_apps` is NO-OP for Workspace non-EDU customers.

### API Controls Sub-Settings

This table provides API Controls sub-settings that are referenced by other API Controls settings.

**Policy API sub-setting name** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---  
**Service** | **Access** | scopes_group  | enum: 

  * `UNSPECIFIED`
  * `DRIVE_ALL`
  * `DRIVE_HIGH_RISK`
  * `GMAIL_ALL`
  * `GMAIL_HIGH_RISK`
  * `CALENDAR_ALL`
  * `CONTACTS_ALL`
  * `GSUITE_ADMIN_ALL`
  * `VAULT_ALL`
  * `CLOUD_PLATFORM`
  * `CLOUD_BILLING`
  * `CLOUD_ML`
  * `APPS_SCRIPT_RUNTIME`
  * `APPS_SCRIPT_API`
  * `CLASSROOM_ALL`
  * `CLASSROOM_HIGH_RISK`
  * `COMMUNICATIONS`
  * `TASKS`
  * `GROUPS`
  * `KEEP`
  * `CLOUD_SEARCH`
  * `CHAT`
  * `SIGN_IN`
  * `CHAT_HIGH_RISK`
  * `MEET`

  
**Restricted/Unrestricted** | is_enabled  | boolean   
  
## Calendar Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Calendar** | **Advanced settings > Appointment schedules with payments** | `calendar.appointment_schedules` | No  | **Allow appointment schedule users to require payment for booked appointments through their own payment provider accounts.** | enable_payments  | boolean   
**Sharing settings > External Invitations** | `calendar.external_invitations` | No  | **Warn users when inviting guests outside of the domain ORGANIZATION_UNIT_NAME** | warn_on_invite  | boolean   
**Calendar Interop Management > Exchange availability in Calendar** | `calendar.interoperability` | No  | **Allow Google Calendar to display Exchange users availability** | enable_interoperability  | boolean   
**Show event details** | enable_full_event_details  | boolean   
**Calendar Interop Management > Exchange resource booking** | `calendar.interoperability` | No  | **Enable Google Calendar to book Microsoft Exchange rooms** | enable_exchange_room_booking  | boolean   
**Sharing settings > External sharing options for primary calendars** | `calendar.primary_calendar_max_allowed_external_sharing` | No  | **Outside ORGANIZATION_UNIT_NAME \- set user ability for primary calendars** | max_allowed_external_sharing  | enum: 

  * `EXTERNAL_FREE_BUSY_ONLY`
  * `EXTERNAL_ALL_INFO_READ_ONLY`
  * `EXTERNAL_ALL_INFO_READ_WRITE`
  * `EXTERNAL_ALL_INFO_READ_WRITE_MANAGE`

  
**Sharing settings > External sharing options for secondary calendars** | `calendar.secondary_calendar_max_allowed_external_sharing` | No  | **Outside <Org name> \- set user ability for secondary calendars** | max_allowed_external_sharing  | enum: 

  * `EXTERNAL_FREE_BUSY_ONLY`
  * `EXTERNAL_ALL_INFO_READ_ONLY`
  * `EXTERNAL_ALL_INFO_READ_WRITE`
  * `EXTERNAL_ALL_INFO_READ_WRITE_MANAGE`

  
  
## Chat Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Google Chat** | **History for chats** | `chat.chat_history` | No  | **History is ON/OFF** | history_on_by_default  | boolean   
**Allow users to change their history setting** | allow_user_modification  | boolean   
**Chat File Sharing** | `chat.chat_file_sharing` | No  | **External filesharing** | external_file_sharing  | enum: 

  * `ALL_FILES`
  * `IMAGES_ONLY`
  * `NO_FILES`
  * `FILE_SHARING_OPTION_UNSPECIFIED`

  
internal_file_sharing  | same   
**History for spaces** | `chat.space_history` | No  | **Conversation history settings for spaces** | history_state  | enum: 

  * `DEFAULT_HISTORY_ON`
  * `DEFAULT_HISTORY_OFF`
  * `HISTORY_ALWAYS_ON`
  * `HISTORY_ALWAYS_OFF`
  * `HISTORY_STATE_UNSPECIFIED`

  
**External Chat Settings** | `chat.external_chat_restriction` | No  | **Allow users to send messages outside organization in chats and spaces** | allow_external_chat  | boolean   
external_chat_restriction  | enum: 

  * `NO_RESTRICTION`
  * `TRUSTED_DOMAINS`
  * `RESTRICTION_UNSPECIFIED`

  
**Chat apps** | `chat.chat_apps_access` | No  | **Allow users to install Chat apps** | enable_apps  | boolean   
**Allow users to add and use incoming webhooks** | enable_webhooks  | boolean   
**Third party archiving** | `chat.third_party_archiving` | No  | **Enable third-party archiving** | enabled  | boolean   
**Specify an email address to which Chat contents should be delivered** | destination_email_address  | string   
**Specify how frequently Chat archiving messages should be sent (between 1-24 hours)** | archival_frequency  | [Duration](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto)  
**Comma-separated list of any custom headers required by the destination address** | custom_headers  | string   
**External Spaces** | `chat.external_spaces` | No  | **Allow users to create and join spaces with people outside their organization** | enabled  | boolean   
**Only allow users to add people from allowlisted domains** | domain_allowlist_mode  | enum: 

  * `DOMAIN_ALLOWLIST_MODE_UNSPECIFIED`
  * `TRUSTED_DOMAINS`
  * `ALL_DOMAINS`

  
**Sharing settings** > **Space access default** | `chat.space_access_default` | No  | **Default space access when users create new spaces.** | access_type  | enum: 

  * `ACCESS_TYPE_UNSPECIFIED`
  * `RESTRICTED`
  * `PRIMARY_TARGET_AUDIENCE`

  
**Content reporting** | `chat.content_reporting` | No  | **Allow users to report content in 1:1 direct messages** | one_on_one_direct_messages_reporting  | enum: 

  * `CONTENT_REPORTING_STATE_UNSPECIFIED`
  * `ENABLED`
  * `DISABLED`

  
**Allow users to report content in group direct messages** | group_direct_messages_reporting  | same   
**Allow users to report content in specified spaces** | spaces_reporting  | same   
spaces_reporting_type  | enum: 

  * `SPACES_REPORTING_TYPE_UNSPECIFIED`
  * `ALL_SPACES`
  * `DISCOVERABLE_SPACES_ONLY`

  
**Specify the categories that users can choose when reporting content** | reporting_categories  | repeated object: 

  * `category` (enum): 
    * `CATEGORY_UNSPECIFIED`
    * `HARASSMENT`
    * `DISCRIMINATION`
    * `EXPLICIT_CONTENT`
    * `SPAM`
    * `CONFIDENTIAL_INFO`
    * `SENSITIVE_INFO`
    * `OTHER`

  
**Specify a custom title and description for the reporting form** | reporting_form_customization_enabled  | boolean   
custom_reporting_form_title  | string   
custom_reporting_form_description  | string   
| **Chat and Space restrictions** | `chat.chat_and_space_restrictions` | No  | **Restrict creating messages, group messages, and spaces. Users with this restriction cannot manage members.** | restriction_level  | enum: 

  * `RESTRICTION_LEVEL_UNSPECIFIED`
  * `UNRESTRICTED`
  * `RESTRICTED`

  
  
## Classroom Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Classroom** | **General Settings > Teacher permissions** | `classroom.teacher_permissions` | No  | **Who can create classes** | whoCanCreateClasses  | enum: 

  * `ANYONE_IN_DOMAIN`
  * `ALL_PENDING_AND_VERIFIED_TEACHERS`
  * `VERIFIED_TEACHERS_ONLY`

  
**General Settings > Guardian access** | `classroom.guardian_access` | No  | **Allow parents and guardians to access Classroom information** | allowAccess  | boolean   
**Who can manage parents and guardians** | whoCanManageGuardianAccess  | enum: 

  * `VERIFIED_TEACHERS_AND_DOMAIN_ADMINS`
  * `DOMAIN_ADMINS_ONLY`

  
**Class settings > About class membership** | `classroom.class_membership` | No  | **Who can join classes in your domain** | whoCanJoinClasses  | enum: 

  * `ANYONE_IN_DOMAIN`
  * `ANYONE_IN_ALLOWLISTED_DOMAINS`
  * `ANY_GOOGLE_WORKSPACE_USER`
  * `ANYONE`

  
**Which classes can users in your domain join** | whichClassesCanUsersJoin  | enum: 

  * `CLASSES_IN_DOMAIN`
  * `CLASSES_IN_ALLOWLISTED_DOMAINS`
  * `ANY_GOOGLE_WORKSPACE_CLASS`

  
**Data access > Classroom API** | `classroom.api_data_access` | No  | **Users can authorize apps to access their Google Classroom data** | enableApiAccess  | boolean   
**Originality Reports > School Matches** | `classroom.originality_reports` | No  | **Enable originality reports school matches** | enableOriginalityReportsSchoolMatches  | boolean   
**Student unenrollment > Unenrollment permissions** | `classroom.student_unenrollment` | No  | **Who can unenroll students from classes** | whoCanUnenrollStudents  | enum 

  * `STUDENTS_AND_TEACHERS`
  * `TEACHERS_ONLY`

  
**Roster import > Settings** | `classroom.roster_import` | No  | **Roster import** | rosterImportOption  | enum: 

  * `OFF`
  * `ON_CLEVER`

  
**Gemini in Workspace apps** | **Gemini for Workspace > Feature Access in Classroom > Classroom** | `classroom.gemini_access` | No  | **Select whether users can access Gemini in Classroom** | enabled  | boolean   
**Note:** Roster import is only supported for users with Edu Plus.

## Data Compliance Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Access management** | **Access management** > **Access management policy** | `access_management.user_scoping` | No  | **Choose an Access Management policy for covered data** | allowed_audience  | enum: 

  * `PREFERENCE_UNSPECIFIED`
  * `CJIS_IRS_1075_GOOGLE_STAFF`
  * `US_GOOGLE_STAFF`
  * `EU_GOOGLE_STAFF`

  
**Data Regions** | **Region** > **Data at rest** | `data_regions.data_at_rest_region` | No  | **Region for storing data at rest** | region  | enum: 

  * `REGION_UNSPECIFIED`
  * `ANY_REGION`
  * `US`
  * `EUROPE`

  
**Region** > **Data processing** | `data_regions.data_processing_region` | No  | **Data region policy for data processing** | limit_to_storage_region  | boolean   
**Access Approvals** | **Access Approvals > Access Approvals policy** | `access_approval.axa_user_scoping` | No  | **Require Google staff to request approval before viewing data necessary for support services** | requires_customer_approval  | boolean   
  
## Devices Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported in v1beta1** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Universal settings** | **Data Access > Android sync** | `devices.android_work_data_sync` | No  | **Allow work data to sync on Android devices** | allowed  | boolean   
**Security > Encryption ** | `devices.encryption` | No  | **Require device encryption** | device_encryption_option  | enum: 

  * `ENCRYPTION_OPTION_UNSPECIFIED`
  * `NOT_REQUIRED`
  * `REQUIRED`

  
**Security > Compromised devices ** | `devices.compromised_devices` | No  | **Block compromised Android devices** | compromised_android_devices_blocked  | boolean   
**Block jailbroken iOS devices** | jailbroken_ios_devices_blocked  | boolean   
**Security > Device Approvals** | `devices.activation_approval` | No  | **Require admin approval** | admin_approval_required  | boolean   
**Send approval request emails to** | approver_email_address  | string   
**Android settings** | **Apps and data sharing > Sharing to other profiles** | `devices.android_work_profile_sharing` | No  | **Allow content sharing from the work profile to the personal space (work profile devices only)** | allowed  | boolean   
**Apps and data sharing > Cross profile copy** | `devices.android_cross_profile_copy_paste` | No  | **Allow pasting between the work profile and personal space (work profile devices only)** | enabled  | boolean   
**Apps and Data Sharing > Google Play Private Apps** | `devices.android_google_play_private_apps` | No  | **Allow users to access Google Play private apps** | access_allowed  | boolean   
**Allow users to publish and update Google Play private apps** | publish_and_update_allowed  | boolean   
**Apps and Data Sharing > Screen Capture** | `devices.android_screen_capture` | No  | **Allow screen capture** | allowed  | boolean   
**Apps and data sharing > Android Beam** | `devices.android_beam` | No  | **Allow outgoing Beam** | outgoing_beam_allowed  | boolean   
**Apps and Data sharing > Location sharing** |  `devices.android_location_sharing` | No  | **Allow location sharing.** | allowed  |  boolean   
**Apps and data sharing > Available apps** | `devices.android_available_apps` | No  | **Set which apps users can install from the Play Store** | playstore_installable_apps  | enum: 

  * `PLAYSTORE_INSTALLABLE_APPS_UNSPECIFIED`
  * `ALL`
  * `ALLOWLISTED`

  
**Apps and data sharing > Verify Apps** | `devices.android_verify_apps` | No  | **Allow users to turn off Google Play Protect (company-owned devices only)** | turnoff_google_play_protect_allowed  | boolean   
**Apps and data sharing > Developer Options** | `devices.android_developer_options` | No  | **Allow developer options** | allowed  | boolean   
**Lock screen features > Periodic authentication with pin, password, or pattern** | `devices.android_periodic_secure_authentication` | No  | **Require users who use face or fingerprint unlock to authenticate periodically with more secure methods like pin, password, or pattern** | required  | boolean   
**After the period of time set below, users have to use more secure authentication the next time they unlock the device** | expiration_period  | enum: 

  * `EXPIRATION_PERIOD_UNSPECIFIED`
  * `ONE_HOUR`
  * `THREE_HOURS`
  * `SIX_HOURS`
  * `EIGHT_HOURS`
  * `TWELVE_HOURS`
  * `TWENTY_FOUR_HOURS`
  * `FORTY_EIGHT_HOURS`
  * `SEVENTY_TWO_HOURS`

  
**Apps and Data sharing > Unknown sources** |  `devices.android_unknown_source_apps` | No  | **Block users from installing apps from unknown sources in their work profile.** | work_profile_installation_allowed  |  boolean   
**Block users from installing apps from unknown sources in their personal profile.** | personal_profile_installation_allowed  |  boolean   
**Apps and Data sharing > Apps settings** |  `devices.android_apps_settings` | No  | **Allow users to change app settings (company-owned devices only).** | modification_allowed  |  boolean   
**Apps and Data sharing > Lock screen features** |  `devices.android_trust_agents` | No  | **Allow Smart Lock to keep a device unlocked.** | smart_lock_allowed  |  boolean   
**Apps and Data sharing > Lock screen features** |  `devices.android_lock_screen_notifications` | No  | **Allow notifications on the lock screen.** | allowed  |  boolean   
**Apps and Data sharing > Lock screen features** |  `devices.android_lock_screen_notification_details` | No  | **Allow notification details.** | allowed  |  boolean   
**iOS settings** | **Advanced Security > Apple Watch** | `devices.ios_apple_watch` | No  | **Allow use of Apple Watch without wrist detection** | no_wrist_detection_usage_allowed  | boolean   
**Advanced Security > Siri** | `devices.ios_siri` | No  | **Allow Siri** | allowed  | boolean   
**Allow Siri on lock screen** | allowed_on_lock_screen  | boolean   
**Advanced Security > Handoff** | `devices.ios_handoff` | No  | **Allow Handoff (Supervised and Device Enrolled devices only)** | allowed  | boolean   
**Data sharing > iCloud Storage** |  `devices.ios_icloud_storage` | No  | **Allow managed apps to store data in iCloud** | managed_apps_sync_allowed  |  boolean   
**Advanced Security > Screen capture** |  `devices.ios_screen_capture` | No  | **Allow screenshots and screen recording** | allowed  |  boolean   
**Backup and iCloud Sync > iCloud backup** | `devices.ios_icloud_backup` | No  | **Allow user to backup device with iCloud (Supervised only)** | allowed  | boolean   
**Backup and iCloud Sync > Encrypted backup** | `devices.ios_backup_encryption` | No  | **Require encryption for backups** | required  | boolean   
**Lock Screen > Control Center** | `devices.ios_lock_screen_control_center` | No  | **Allow Control Center on lock screen** | allowed  | boolean   
**Apps and services > Files app** | `devices.ios_files_app` | No  | **Allow users to connect to USB drives in Files (iOS 13.1 and later, supervised only)** | usb_drives_connection_allowed  | boolean   
**Allow users to connect to network drives in Files (iOS 13.1 and later, supervised only)** | network_drives_connection_allowed  | boolean   
**Device features > Date and time** | `devices.ios_date_time` | No  | **Force automatic date and time (iOS 12 and later, supervised only)** | automatic_date_time_enforced  | boolean   
**Lock Screen > Notifications view** | `devices.ios_lock_screen_notifications_view` | No  | **Allow Notifications view on lock screen** | allowed  | boolean   
**Data sharing > Data actions** | `devices.ios_data_actions` | No  | **Select what actions users can take with applicable Google Workspace data on iOS devices** | external_data_sharing_allowed  | boolean   
**Allow copying and pasting of work data to personal accounts and apps** | work_data_operation_type.non_workspace_apps_copy_paste_allowed  | boolean   
**Allow sending of work data to personal apps, including all non-Google Workspace apps on the iOS share sheet** | work_data_operation_type.non_workspace_apps_sharing_allowed  | boolean   
**Allow sharing of work data to personal accounts or to iOS Mail on the iOS share sheet** | work_data_operation_type.personal_accounts_sharing_allowed  | boolean   
**Allow sharing of work data with AirDrop on the iOS share sheet** | work_data_operation_type.airdrop_sharing_allowed  | boolean   
**Allow printing of work files** | work_data_operation_type.files_printing_allowed  | boolean   
**Allow saving of work data to Files with iOS share sheet, and access work data directly from Files** | work_data_operation_type.files_access_allowed  | boolean   
**Allow saving of work images and videos to iOS photos** | work_data_operation_type.images_videos_saving_allowed  | boolean   
**Allow assigning items to Contacts with iOS share sheet** | work_data_operation_type.contacts_items_assignment_allowed  | boolean   
**Safari > Secure browsing** | `devices.ios_safari_secure_browsing` | No  | **Enforce the Safari fraudulent website warning** | fraudulent_website_warning_enforced  | boolean   
**Data Sharing > Apple Intelligence** | `devices.ios_apple_intelligence` | No  | **Allow users to use Apple Intelligence Writing Tools within Google Workspace apps on iOS devices** | writing_tools_allowed  | boolean   
**Backup and iCloud Sync > Keychain sync** |  `devices.ios_keychain_sync` | No  | **Allow users to sync keychains with iCloud (Supervised only).** | icloud_sync_allowed  |  boolean   
**Backup and iCloud Sync > Document sync** |  `devices.ios_document_sync` | No  | **Allow users to sync documents and data with iCloud.** | icloud_data_sync_allowed  |  boolean   
  
## Directory Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Directory settings** | **Sharing settings > External Directory sharing** | `directory.external_directory_sharing` | No  | **N/A** | sharing_option  | enum: 

  * `SHARING_OPTION_UNSPECIFIED`
  * `REQUESTER_BASIC_PROFILE_ONLY`
  * `ORGANIZATION_DIRECTORY_DATA`

  
  
## Drive and Docs Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Drive and Docs** | **Sharing settings > Sharing options** | `drive_and_docs.external_sharing` | No  | **Select the highest level of sharing outside of CUSTOMER_NAME that you want to allow** | external_sharing_mode  | enum: 

  * `DISALLOWED`
  * `ALLOWLISTED_DOMAINS`
  * `ALLOWED`

  
**Allow users in ORGANIZATION_UNIT_NAME to receive files from users or shared drives outside of CUSTOMER_NAME** | allow_receiving_external_files  | boolean   
**Warn when files owned by users or shared drives in ORGANIZATION_UNIT_NAME are shared with users in allowlisted domains** | warn_for_sharing_outside_allowlisted_domains  | boolean   
**Allow users in ORGANIZATION_UNIT_NAME to receive files from users or shared drives outside of allowlisted domains** | allow_receiving_files_outside_allowlisted_domains  | boolean   
**Allow users or shared drives in ORGANIZATION_UNIT_NAME to share items with non-Google users in trusted domains using visitor sharing** | allow_non_google_invites_in_allowlisted_domains  | boolean   
**Warn when files owned by users or shared drives in ORGANIZATION_UNIT_NAME are shared outside of CUSTOMER_NAME** | warn_for_external_sharing  | boolean   
**Allow users or shared drives in ORGANIZATION_UNIT_NAME to share items with people outside CUSTOMER_NAME who aren't using a Google Account** | allow_non_google_invites  | boolean   
**When sharing outside of CUSTOMER_NAME is allowed, users in ORGANIZATION_UNIT_NAME can make files and published web content visible to anyone with the link** | allow_publishing_files  | boolean   
**When a user shares a file via a Google product other than Docs or Drive (e.g. by pasting a link in Gmail), Google can check that the recipients have access. If not, when possible, Google will ask the user to pick if they want to share the file to** | access_checker_suggestions  | enum: 

  * `RECIPIENTS_OR_AUDIENCE_OR_PUBLIC`
  * `RECIPIENTS_OR_AUDIENCE`
  * `RECIPIENTS_ONLY`

  
**Select who should be allowed to distribute content in ORGANIZATION_UNIT_NAME outside of CUSTOMER_NAME. This restricts who can upload or move content to shared drives owned by another organization** | allowed_parties_for_distributing_content  | enum: 

  * `ALL_ELIGIBLE_USERS`
  * `ELIGIBLE_INTERNAL_USERS`
  * `NONE`

  
**Sharing settings > General access default** | `drive_and_docs.general_access_default` | No  | **When users in ORGANIZATION_UNIT_NAME create items, the default access will be** | default_file_access  | enum: 

  * `PRIVATE_TO_OWNER`
  * `PRIMARY_AUDIENCE_WITH_LINK`
  * `PRIMARY_AUDIENCE_WITH_LINK_OR_SEARCH`

  
**Sharing settings > Shared drive creation** | `drive_and_docs.shared_drive_creation` | No  | **Prevent users in ORGANIZATION_UNIT_NAME from creating new shared drives** | allow_shared_drive_creation  | boolean (The API response returns the opposite of the UI value)   
**When users in ORGANIZATION_UNIT_NAME create a shared drive, it will be assigned to the following organizational unit** | org_unit_for_new_shared_drives  | enum: 

  * `CREATOR_ORG_UNIT`
  * `CUSTOM_ORG_UNIT`

  
**Selected organizational unit** | custom_org_unit  | string   
**Allow members with manager access to override the settings below** | allow_managers_to_override_settings  | boolean   
**Allow users outside CUSTOMER_NAME to access files in shared drives** | allow_external_user_access  | boolean   
**Allow people who aren't shared drive members to be added to files** | allow_non_member_access  | boolean   
**Download, print, copy is enabled for** | allowed_parties_for_download_print_copy  | enum: 

  * `ALL`
  * `EDITORS_ONLY` (Managers, contributors and content managers)
  * `MANAGERS_ONLY`

  
**Allow content managers to share folders** | allow_content_managers_to_share_folders  | boolean   
**Sharing settings > Security update for files** | `drive_and_docs.file_security_update` | No  | **Applying this update will make file links more secure. This may cause users to receive file access requests** | security_update  | enum: 

  * `APPLY_TO_IMPACTED_FILES`
  * `REMOVE_FROM_IMPACTED_FILES`

  
**Allow users to remove/apply the security update for files they own or manage** | allow_users_to_manage_update  | boolean   
**Features and Applications > Drive SDK** | `drive_and_docs.drive_sdk` | No  | **Allow users to access Google Drive with the Drive SDK API** | enable_drive_sdk_api_access  | boolean   
**Google Drive for desktop > Enable Drive for desktop** | `drive_and_docs.drive_for_desktop` | No  | **Allow Google Drive for desktop in your organization** | allow_drive_for_desktop  | boolean   
**Only allow Google Drive for desktop on authorized devices** | restrict_to_authorized_devices  | boolean   
**Show Google Drive for desktop download link** | show_download_link  | boolean   
**Allow users to enable real-time presence in Microsoft Office from Google Drive for desktop** | allow_real_time_presence  | boolean   
**Sharing settings > Highlight external files** | `drive_and_docs.external_file_warning` | No  | **Mark files shared or owned externally as "external" to indicate that content may be viewable outside your organization. Applies to Drive, Docs, Sheets, Slides, Drawings, and Vids.** | highlighting_enabled  | boolean   
  
## Gemini App Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Gemini app** | **User access** | `gemini_app.unlicensed_user_access` | No  | **Allow all users to access the Gemini app, regardless of license** | enabled  | boolean   
  
## Gemini in Workspace Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Gemini in Workspace** | **Beta Gemini features > Beta features** | `gemini_for_workspace.beta_features` | No  | **Turn on access to Beta features in Gemini for Google Workspace** | enabled  | boolean   
**Allow Google to invite users in the selected org unit or group to participate in surveys and UX feedback studies for improving Gemini for Google Workspace** | feedback_and_testing_enabled  | boolean   
  
## Gmail Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Gmail** | **User Settings > Confidential mode** | `gmail.confidential_mode` | No  | **Enable confidential mode** | enable_confidential_mode  | boolean   
**User Settings > S/MIME** | `gmail.smime_encryption` | No  | **Enable S/MIME encryption for sending and receiving emails** | enable_smime_encryption  | enum: 

  * `STATUS_UNSPECIFIED`
  * `STATUS_DISABLED`
  * `STATUS_ENABLED`

  
**Allow SHA-1 globally (not recommended)** | allow_sha1_globally_in_smime_signature  | boolean   
`gmail.enhanced_smime_encryption` | No  | **Allow users to upload their own certificates** | allow_user_to_upload_certificates  | boolean   
**Accept these additional root certificates for specific domains:** | custom_root_certificates  | A list of CustomRootCertificates that contains a list of root certificates, a list of intermediate CA certificates, a list of restricted domain names, a boolean to allow address mismatch and an enum with different validation levels.   
**Spam, phishing, and malware > Enhanced pre-delivery message scanning** | `gmail.enhanced_pre_delivery_message_scanning` | No  | **Enables improved detection of suspicious content prior to delivery** | enable_improved_suspicious_content_detection  | boolean   
**Spam, phishing, and malware > Email allowlist** | `gmail.email_spam_filter_ip_allowlist` | No  | **Enter the IP addresses for your email allowlist** | allowed_ip_addresses  | A list of strings   
**Safety > Spoofing and authentication** | `gmail.spoofing_and_authentication` | No  | **Protect against domain spoofing based on similar domain names** | detect_domain_name_spoofing  | boolean   
**Choose an action** | domain_name_spoofing_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`
  * `NO_ACTION`

  
**Choose a quarantine** | domain_name_spoofing_quarantine_id  | integer   
**Protect against spoofing of employee names** | detect_employee_name_spoofing  | boolean   
**Choose an action** | employee_name_spoofing_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`
  * `NO_ACTION`

  
**Choose a quarantine** | employee_name_spoofing_quarantine_id  | integer   
**Protect against inbound emails spoofing your domain** | detect_domain_spoofing_from_unauthenticated_senders  | boolean   
**Choose an action** | domain_spoofing_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`
  * `NO_ACTION`

  
**Choose a quarantine** | domain_spoofing_quarantine_id  | integer   
**Protect against any unauthenticated emails** | detect_unauthenticated_emails  | boolean   
**Choose an action** | unauthenticated_email_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`
  * `NO_ACTION`

  
**Choose a quarantine** | unauthenticated_email_quarantine_id  | integer   
**Protect your Groups from inbound emails spoofing your domain** | detect_groups_spoofing  | boolean   
**Apply this setting to** | groups_spoofing_visibility_type  | enum: 

  * `PRIVATE_GROUPS_ONLY`
  * `ALL_GROUPS`

  
**Choose an action** | groups_spoofing_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`
  * `NO_ACTION`

  
**Choose a quarantine** | groups_spoofing_quarantine_id  | integer   
**Apply future recommended settings automatically** | apply_future_settings_automatically  | boolean   
**Safety > Links and external images** | `gmail.links_and_external_images` | No  | **Identify links behind shortened URLs** | enable_shortener_scanning  | boolean   
**Scan linked images** | enable_external_image_scanning  | boolean   
**Show warning prompt for any click on links to untrusted domains** | enable_aggressive_warnings_on_untrusted_links  | boolean   
**Apply future recommended settings automatically** | apply_future_settings_automatically  | boolean   
**Safety > Attachments** | `gmail.email_attachment_safety` | No  | **Protect against encrypted attachments from untrusted senders** | enable_encrypted_attachment_protection  | boolean   
**Choose an action** | encrypted_attachment_protection_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`

  
**Choose a quarantine** | encrypted_attachment_protection_quarantine_id  | integer   
**Protect against attachments with scripts from untrusted senders** | enable_attachment_with_scripts_protection  | boolean   
**Choose an action** | attachment_with_scripts_protection_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`

  
**Choose a quarantine** | attachment_with_scripts_protection_quarantine_id  | integer   
**Protect against anomalous attachment types in emails** | enable_anomalous_attachment_protection  | boolean   
**Choose an action** | anomalous_attachment_protection_consequence  | enum: 

  * `WARNING`
  * `SPAM_FOLDER`
  * `QUARANTINE`

  
**Choose a quarantine** | anomalous_attachment_protection_quarantine_id  | integer   
**Allowlist the following uncommon file types** | allowed_anomalous_attachment_filetypes  | string[]   
**Apply future recommended settings automatically** | apply_future_recommended_settings_automatically  | boolean   
**Routing > Manage address lists** | `gmail.email_address_lists` | No  | **Manage address lists** | email_address_list  | EmailAddressList[]   
**Spam, phishing and malware > Blocked senders** | `gmail.blocked_sender_lists` | No  | **Block or approve specific senders based on email address or domain** | blocked_senders  | BlockedSender[]   
**Spam, phishing and malware > Spam** | `gmail.spam_override_lists` | No  | **Create approved senders lists that bypass the spam folder.** | spam_override  | SpamOverride[]   
**Compliance > Content compliance** | `gmail.content_compliance` | No  | **Configure advanced content filters based on words, phrases or patterns** | content_compliance_rules  | ContentComplianceRule[]   
**Compliance > Restrict delivery** | `gmail.restrict_delivery` | No  | **Restrict the domains that your users are allowed to exchange email with.** | restrict_delivery_rules  | RestrictDeliveryRule[]   
**Compliance > Objectionable content** | `gmail.objectionable_content` | No  | **Configure content filters based on word lists** | objectionable_content_rules  | ObjectionableContentRule[]   
**Compliance > Attachment compliance** | `gmail.attachment_compliance` | No  | **Configure attachment filters based on file type, file name and message size** | attachment_compliance_rules  | AttachmentComplianceRule[]   
**Compliance > Comprehensive mail storage** | `gmail.comprehensive_mail_storage` | No  | **Ensure that a copy of all sent and received mail is stored in associated users' mailboxes** | rule_id  | string   
**N/A (For all rules)** | `gmail.rule_states` | No  | **N/A** | rule_states  | RuleState[]   
**Manage quarantines** | `gmail.email_quarantines` | No  | **Add quarantine** | email_quarantines  | EmailQuarantine[]   
**Setup > User email uploads** | `gmail.user_email_uploads` | No  | **Show users the option to import mail and contacts from Yahoo!, Hotmail, AOL, or other webmail or POP3 accounts from the Gmail settings page** | enable_mail_and_contacts_import  | boolean   
**End User Access > POP and IMAP access** | `gmail.pop_access` | No  | **Enable POP access for all users** | enable_pop_access  | boolean   
`gmail.imap_access` | No  | **Enable IMAP access for all users** | enable_imap_access  | boolean   
**Allow any mail client** | imap_access_restriction.allow_all_mail_clients  | boolean   
**Restrict which mail clients users can use (OAuth mail clients only)** | imap_access_restriction.allowed_oauth_mail_client_list  | OAuthMailClientList  
**End User Access > Google Workspace Sync** | `gmail.workspace_sync_for_outlook` | No  | **Enable Google Workspace Sync for Microsoft Outlook for my users** | enable_google_workspace_sync_for_microsoft_outlook  | boolean   
**End User Access > Automatic forwarding** | `gmail.auto_forwarding` | No  | **Allow users to automatically forward incoming email to another address** | enable_auto_forwarding  | boolean   
**Allowed forwarding destination** | allowed_forwarding_destination  | enum: 

  * `ANY_ADDRESS`
  * `INTERNAL_ADDRESSES`

  
**User Settings > Name format** | `gmail.name_format` | No  | **Allow users to customize this setting** | allow_custom_display_names  | boolean   
**First Last or Last, First** | default_display_name_format  | enum: 

  * `FIRSTNAME_LASTNAME`
  * `LASTNAME_COMMA_FIRSTNAME`

  
**End User Access > Allow per-user outbound gateways** | `gmail.per_user_outbound_gateway` | No  | **Allow users to send mail through an external SMTP server when configuring a "from" address hosted outside your email domain** | allow_users_to_use_external_smtp_servers  | boolean   
**End User Access > Warn for external recipients** | `gmail.external_recipient_warning` | No  | **Highlight any external recipients in a conversation. Warn users before they reply to email with external recipients who aren't in their contacts.** | enabled  | boolean   
**End User Access > Image URL proxy allowlist ** | `gmail.email_image_proxy_bypass` | No  | **Enter image URL patterns. Matching URLs bypass the image proxy.** | image_proxy_bypass_pattern  | string[]   
**N/A** | enable_image_proxy  | boolean   
**User Settings > Mail Delegation** | `gmail.mail_delegation` | No  | **Let users delegate access to their mailbox to other users in the domain** | enable_mail_delegation  | boolean   
**Allow users to customize this setting** | allow_custom_delegate_attribution  | boolean   
**Show the account owner and the delegate who sent the email** | enable_delegate_attribution  | boolean   
**Show the account owner only**  
**Allow users to grant their mailbox access to a Google group** | enable_mailbox_group_delegation  | boolean   
**User Settings > Gmail Web Offline** | `gmail.web_offline` | No  | **Enable Gmail web offline** | enabled  | boolean   
**Force deletion of offline data on sign out of Google account** | signout_data_deletion_enforced  | boolean   
  
### Gmail Sub-Settings

This table provides Gmail sub-settings that are referenced by other Gmail settings.

**Policy API sub-setting name** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---  
**EmailAddressList** | **N/A** | id  | string   
**Name** | name  | string   
**ADD ADDRESS LIST** | address_list  | AddressList  
**ADD BLOCKED LIST** | blocked_address_list  | AddressList  
**AddressList** | **Add address list** | address  | AddressListEntry[]   
**AddressListEntry** | **Address** | address  | string   
**Authentication required (received mail only)** | require_address_verification  | boolean   
**BlockedSender** | **Enter a short description that will appear within the setting's summary** | description  | string   
**Add addresses or domains that you want to automatically reject messages from** | sender_blocklist  | [StringValue](https://docs.cloud.google.com/nodejs/docs/reference/admin/7.3.0/admin/protos.google.protobuf.stringvalue)[]   
**Enter customized rejection notice** | rejection_response  | string   
**Bypass this setting for messages received from addresses or domains within these approved senders lists.** | bypass_approved_sender  | boolean   
**N/A** | bypass_approved_sender_allowlist  | [StringValue](https://docs.cloud.google.com/nodejs/docs/reference/admin/7.3.0/admin/protos.google.protobuf.stringvalue)[]   
**N/A** | rule_id  | string   
**SpamOverride** | **Enter a short description that will appear within the setting's summary** | description  | string   
**Be more aggressive when filtering spam.** | enable_aggressive_filtering  | boolean   
**Put spam in administrative quarantine** | add_to_quarantine  | boolean   
**N/A** | quarantine_id  | integer   
**Bypass spam filters for internal senders.** | bypass_internal_senders  | boolean   
**Bypass spam filters for messages from senders or domains in selected lists.** | bypass_selected_senders  | boolean   
**N/A** | bypass_sender_allowlist  | [StringValue](https://docs.cloud.google.com/nodejs/docs/reference/admin/7.3.0/admin/protos.google.protobuf.stringvalue)[]   
**Bypass spam filters and hide warnings for messages from senders or domains in selected lists.** | hide_warning_banner_from_selected_senders  | boolean   
**N/A** | hide_warning_banner_sender_allowlist  | [StringValue](https://docs.cloud.google.com/nodejs/docs/reference/admin/7.3.0/admin/protos.google.protobuf.stringvalue)[]   
**Bypass spam filters and hide warnings for all messages from internal and external senders (not recommended).** | hide_warning_banner_for_all  | boolean   
**N/A** | rule_id  | string   
**ContentComplianceRule** | **Enter a short description that will appear within the setting's summary** | description  | string   
**Email messages to affect** | condition  | RuleConditions  
**Add expressions that describe the content you want to search for in each message** | match_expressions  | MatchExpression[]   
**If ANY of the following match the message** | match_any_expression  | boolean   
**If the above expressions match, do the following** | consequence  | RuleConsequences  
**N/A** | rule_id  | string   
**RestrictDeliveryRule** | **Required: enter a short description that will appear within the setting's summary** | description  | string   
**Add addresses or domains that you want to allow** | allowed_addresses  | [StringValue](https://docs.cloud.google.com/nodejs/docs/reference/admin/7.3.0/admin/protos.google.protobuf.stringvalue)[]   
**All messages to or from other addresses and domains will be rejected. Edit the default rejection notice for these messages.** | rejection_notice_message  | string   
**Bypass this setting for internal messages** | internal_messages_rule_bypass_allowed  | boolean   
**N/A** | rule_id  | string   
**ObjectionableContentRule** | **Enter a short description that will appear within the setting's summary** | description  | string   
**Email messages to affect** | condition  | RuleConditions  
**Custom objectionable words** | objectionable_content_defined  | boolean   
**Enter words** | objectionable_words  | string[]   
**If the above expressions match, do the following** | consequence  | RuleConsequences  
**N/A** | rule_id  | string   
**AttachmentComplianceRule** | **Enter a short description that will appear within the setting's summary** | description  | string   
**Email messages to affect** | condition  | RuleConditions  
**Add expressions that describe the content you want to search for in each message** | match_expressions  | MatchExpression[]   
**If ANY of the following match the message** | match_any_expression  | boolean   
**If the above expressions match, do the following** | consequence  | RuleConsequences  
**N/A** | rule_id  | string   
**RuleState** | **N/A (For all rules)** | enabled  | boolean   
rule_id  | string   
**RuleConditions** | **Email messages to affect** | **Inbound messages** | affect_inbound_messages  | boolean   
**Outbound messages** | affect_outbound_messages  | boolean   
**Internal outbound messages** | affect_internal_sending_messages  | boolean   
**Internal inbound messages** | affect_internal_receiving_messages  | boolean   
**Address lists** | **Use address lists to bypass or control application of this setting** | address_list_option  | enum: 

  * `NO_EFFECT`
  * `EXCLUDED`
  * `REQUIRED`

  
**Bypass this setting for specific addresses / domains**  
**Only apply this setting for specific addresses / domains**  
**Use existing list / Create or edit list** | address_lists  | [StringValue](https://docs.cloud.google.com/nodejs/docs/reference/admin/7.3.0/admin/protos.google.protobuf.stringvalue)[]   
**Account types to affect** | **Users** | account_type_user  | boolean   
**Groups** | account_type_group  | boolean   
**Unrecognized / Catch-all** | account_type_unrecognized  | boolean   
**Envelope filter** | **Only affect specific envelope senders** | envelope_sender_filter  | AddressMatcher  
**Only affect specific envelope recipients** | envelope_recipient_filter  | AddressMatcher  
**AddressMatcher** | **Only affect specific envelope senders / Only affect specific envelope recipients** | enabled  | boolean   
**Single email address** | **N/A** | address_match_type  | enum: `EXACT`  
**Email address** | exact_address_match_value  | string   
**Pattern match** | **N/A** | address_match_type  | enum: `REGEXP`  
**Regexp** | regexp_match_value  | string   
**Group membership (only sent mail) / Group membership (only received mail)** | **N/A** | address_match_type  | enum: `GROUP_MEMBERSHIP`  
**Select groups** | group_ids  | string[]   
**MatchExpression** | **Simple content match** | **N/A** | match_expression_type  | enum: `SIMPLE_CONTENT`  
**Content** | match_content  | string   
**Advanced content match** | **N/A** | match_expression_type  | enum: `ADVANCED_CONTENT`  
**Content / Regex** | match_content  | string   
**N/A** | advanced_content_match  | AdvancedContentMatch  
**Metadata match** | match_expression_type  | enum: `METADATA`  
metadata_match  | MetadataMatch  
**Predefined content match** | match_expression_type  | enum: `PREDEFINED_CONTENT`  
predefined_content_match  | PredefinedContentMatch  
**File type** | match_expression_type  | enum: `FILE_TYPE`  
file_type_match  | FileTypeMatch  
**File name** | **N/A** | match_expression_type  | enum: `FILE_NAME`  
**The attachment file name contains** | file_name  | string   
**Message size** | **N/A** | match_expression_type  | enum: `MESSAGE_SIZE`  
**The overall message (body + attachment) is greater than the following (MB)** | message_size_threshold_in_megabytes  | integer   
**AdvancedContentMatch** | **Location** | **Headers + Body** | advanced_content_match_location  | enum: `HEADERS_AND_BODY`  
**Full headers** | enum: `FULL_HEADERS`  
**Body** | enum: `BODY`  
**Subject** | enum: `SUBJECT`  
**Sender header** | enum: `SENDER_HEADER`  
**Recipients header** | enum: `RECIPIENTS_HEADER`  
**Envelope sender** | enum: `ENVELOPE_SENDER`  
**Any envelope recipient** | enum: `ANY_ENVELOPE_RECIPIENT`  
**Raw message** | enum: `RAW_MESSAGE`  
**Match type** | **Starts with** | advanced_content_match_type  | enum: `STARTS_WITH`  
**Ends with** | enum: `ENDS_WITH`  
**Contains text** | enum: `CONTAINS_TEXT`  
**Not contains text** | enum: `NOT_CONTAINS_TEXT`  
**Equals** | enum: EQUALS   
**Is empty** | enum: `IS_EMPTY`  
**Matches regex** | enum: `MATCHES_REGEXP`  
**Not matches regex** | enum: `NOT_MATCHES_REGEXP`  
**Matches any word** | enum: `MATCH_ANY_WORD`  
**Matches all words** | enum: `MATCH_ALL_WORDS`  
**N/A** | regexp_match  | RegexpMatch  
**RegexpMatch** | **Regex Description** | description  | string   
**Minimum match count** | min_match_count  | integer   
**MetadataMatch** | **Attribute** | **Message authentication** | metadata_match_attribute  | enum: `MESSAGE_AUTHENTICATION`  
**Source IP** | enum: `SOURCE_IP`  
**Secure transport (TLS)** | enum: `TLS`  
**Message size** | enum: `MESSAGE_SIZE`  
**S/MIME encrypted** | enum: `SMIME_ENCRYPTED`  
**S/MIME signed** | enum: `SMIME_SIGNED`  
**Gmail confidential mode** | enum: `CONFIDENTIAL_MODE`  
**Spam** | enum: `SPAM`  
**Match type** | **the following range** | source_ip_range  | string   
**the following (MB)** | message_size_in_megabytes  | integer   
**Message is authenticated** | metadata_match_type  | enum: `MESSAGE_AUTHENTICATED`  
**Message is not authenticated** | enum: `MESSAGE_NOT_AUTHENTICATED`  
**Source IP is within** | enum: `SOURCE_IP_IN_RANGE`  
**Source IP is not within** | enum: `SOURCE_IP_NOT_IN_RANGE`  
**Connection is TLS encrypted** | enum: `TLS_ENCRYPTED`  
**Connection is not TLS encrypted** | enum: `TLS_NOT_ENCRYPTED`  
**Message size is greater than** | enum: `MESSAGE_SIZE_GREATER_THAN`  
**Message size is less than** | enum: `MESSAGE_SIZE_LESS_THAN`  
**Message is S/MIME encrypted** | enum: `MESSAGE_IS_SMIME_ENCRYPTED`  
**Message is not S/MIME encrypted** | enum: `MESSAGE_IS_NOT_SMIME_ENCRYPTED`  
**Message is S/MIME signed** | enum: `MESSAGE_IS_SMIME_SIGNED`  
**Message is not S/MIME signed** | enum: `MESSAGE_IS_NOT_SMIME_SIGNED`  
**Message is in Gmail confidential mode** | enum: `MESSAGE_IS_IN_CONFIDENTIAL_MODE`  
**Message is not in Gmail confidential mode** | enum: `MESSAGE_IS_NOT_IN_CONFIDENTIAL_MODE`  
**Malware detected from security sandbox** | enum: `MALWARE_DETECTED_FROM_SECURITY_SANDBOX`  
**PredefinedContentMatch** | **N/A (Predefined content match selector)** | predefined_content_match_name  | string   
**Minimum match count** | min_match_count  | integer   
**Confidence threshold** | confidence_threshold  | enum: 

  * `MEDIUM`
  * `HIGH`

  
**FileTypeMatch** | **Office documents which are encrypted** | encrypted_office_documents  | boolean   
**Office documents which are not encrypted** | unencrypted_office_documents  | boolean   
**Video and multimedia** | video  | boolean   
**Music and sound** | music  | boolean   
**Images** | image  | boolean   
**Compressed files and archives which are encrypted** | compressed_encrypted_files  | boolean   
**Compressed files and archives which are not encrypted** | compressed_unencrypted_files  | boolean   
**Custom file types - Match files based on file name extension** | custom_file_extensions  | string[]   
**Also match files based on file format** | match_file_format  | boolean   
**RuleConsequences** | **Modify message** | **N/A** | rule_consequence_type  | enum: `MODIFY_MESSAGE`  
**N/A** | primary_delivery  | Delivery  
**Add more recipients** | deliver_to_additional_recipients  | boolean   
**Recipients** | bcc_deliveries  | Delivery[]   
**Delivery** | **Add X-Gm-Original-To header** | add_x_gm_original_to_header  | boolean   
**Add X-Gm-Spam and X-Gm-Phishy headers** | add_x_gm_spam_header  | boolean   
**Add custom headers** | add_custom_headers  | boolean   
**Custom headers** | custom_headers  | string[]   
**Prepend custom subject** | prepend_custom_subject  | boolean   
**Enter new subject prefix** | custom_subject  | string   
**Change route** | change_default_route  | boolean   
**Also reroute spam** | reroute_spam  | boolean   
**Suppress bounces from this recipient** | suppress_bounces_from_recipient  | boolean   
**N/A (Routing selector)** | normal_routing  | boolean   
**Change envelope recipient** **N/A** | change_envelope_recipient  | boolean   
**Replace recipient** | replace_envelope_recipient_type  | enum: `REPLACE_ADDRESS`  
recipient_address  | string   
**Replace username** | replace_envelope_recipient_type  | enum: `REPLACE_USER`  
recipient_user  | string   
**Replace domain** | replace_envelope_recipient_type  | enum: `REPLACE_DOMAIN`  
recipient_domain  | string   
**Bypass spam filter for this message** | bypass_spam_filter  | boolean   
**Remove attachments from message** | remove_attachments  | boolean   
**Append this text to notify recipients that attachments have been removed** | attachment_removal_notice  | string   
**Require secure transport (TLS)** | require_tls  | boolean   
**Encrypt message if not encrypted (S/MIME)** | encrypt_outgoing_messages  | boolean   
**Bounce message if unable to sign and encrypt** | bounce_unencrypted_messages  | boolean   
**Do not deliver spam to this recipient** | do_not_deliver_spam_to_recipient  | boolean   
**OAuthMailClientList** | **Restrict which mail clients users can use (OAuth mail clients only)** | oauth_mail_client  | OAuthMailClient[]   
**OAuthMailClient** | **N/A** | oauth_mail_client_id  | string   
**EmailQuarantine** | **N/A** | quarantine_id  | integer   
**Name** | name  | string   
**Description** | description  | string   
**Inbound denial consequence** | inbound_denial_consequence  | enum: 

  * `DENIAL_CONSEQUENCE_UNSPECIFIED`
  * `DROP`
  * `REJECT`

  
**Outbound denial consequence** | outbound_denial_consequence  | enum: 

  * `DENIAL_CONSEQUENCE_UNSPECIFIED`
  * `DROP`
  * `REJECT`

  
**Notify periodically when messages are quarantined** | send_notifications  | boolean   
**Quarantine reviewers group** | quarantine_acl_group_ids  | string[]   
  
## Groups For Business Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Groups for Business** | **Sharing settings > Sharing options** | `groups_for_business.groups_sharing` | No  | **Set policies for changing group sharing settings** | collaborationCapability  | enum: 

  * `ANYONE_CAN_ACCESS`
  * `DOMAIN_USERS_ONLY`

  
**Creating groups** | createGroupsAccessLevel  | enum: 

  * `ADMIN_ONLY`
  * `USERS_IN_DOMAIN`
  * `ANYONE_CAN_CREATE`

  
**Group owners can allow external members** | ownersCanAllowExternalMembers  | boolean   
**Group owners can allow incoming email from outside the organization** | ownersCanAllowIncomingMailFromPublic  | boolean   
**Default for permission to view conversations** | viewTopicsDefaultAccessLevel  | enum: 

  * `OWNERS`
  * `MANAGERS`
  * `GROUP_MEMBERS`
  * `DOMAIN_USERS`
  * `ANYONE_CAN_VIEW_TOPICS`

  
**Group owners can hide groups from the directory** | ownersCanHideGroups  | boolean   
**Hide newly created groups from the directory** | newGroupsAreHidden  | boolean   
  
## Legal and Compliance

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Account settings** | **Sharing options** | `cloud_sharing_options.cloud_data_sharing` | No  | **Google Cloud Platform Sharing Options** | sharingOptions  | enum: 

  * `UNSUPPORTED`
  * `ENABLED`
  * `DISABLED`

  
  
## Marketplace Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Apps list** | **Apps list** | `workspace_marketplace.apps_allowlist` | No  | **Showing apps for users in all organizational units** | apps  | AppsAllowlistSetting[]   
**Settings** | **Manage access to apps > Manage Google Workspace Marketplace allowlist access** | `workspace_marketplace.apps_access_options` | No  | **Select which Marketplace apps users can run and install.** | access_level  | enum: 

  * `ALLOW_ALL`
  * `ALLOW_LISTED_APPS`
  * `ALLOW_NONE`

  
  
### Marketplace Sub-Settings

**Policy API sub-setting name** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---  
**AppsAllowlistSetting** | **N/A** | application_id  | string   
**N/A** | access  | enum: 

  * `ALLOWED`
  * `BLOCKED`

  
  
The `workspace_marketplace.apps_allowlist` setting in the API response exposes the Marketplace `application_id`, instead of `application_name`. The following Python script can be used to convert one or more `application_id` that are specified on the command line to `application_name`.
    
    
    import re
    import requests
    import sys
    
    output = {}
    app_ids = sys.argv[1:]
    
    for id in app_ids:
      url = f"https://workspace.google.com/marketplace/app/_/{id}"
      response = requests.get(url, allow_redirects=False)
      final_url = response.headers['Location']
      pattern = f"^https://workspace.google.com/marketplace/app/(.*)/{id}$"
      a = re.search(pattern, final_url)
      output[id] = a.group(1)
    
    # Output application name captured from returned URL
    print(output)
    

## Meet Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Google Meet** | **Meet video settings > Recording** | `meet.video_recording` | No  | **Let people record their meetings.** | enable_recording  | boolean   
**Meet video settings > Automatic transcription** | `meet.automatic_transcription` | No  | **Meetings are transcribed by default** | enabled  | boolean   
**Meet video settings > Automatic recording** | `meet.automatic_recording` | No  | **Meetings are recorded by default** | enabled  | boolean   
**Meet safety settings > Domain** | `meet.safety_domain` | No  | **Who can join meetings created by your organization.** | users_allowed_to_join  | enum: 

  * `SAME_ORGANIZATION_ONLY`
  * `LOGGED_IN`
  * `ALL`

  
**Meet safety settings > Access** | `meet.safety_access` | No  | **Which meetings or calls users in the organization can join. "Incoming call restrictions" can further limit the calls that users can receive** | meetings_allowed_to_join  | enum: 

  * `SAME_ORGANIZATION_ONLY`
  * `ANY_WORKSPACE_ORGANIZATION`
  * `ALL`

  
**Meet safety settings > Host management** | `meet.safety_host_management` | No  | **Default host management** | enable_host_management  | boolean   
**Meet safety settings > Warn for external participants** | `meet.safety_external_participants` | No  | **Indicates participants who are outside "Organization" or whose identities are unconfirmed.** | enable_external_label  | boolean   
**Meet safety settings** > **Joining** | `meet.joining` | No  | **Meeting access type (subject to restrictions set in domain)** | allowed_audience  | enum: 

  * `ALLOWED_AUDIENCE_UNSPECIFIED`
  * `OPEN`
  * `TRUSTED`
  * `RESTRICTED`

  
**Meet safety settings** > **Chat** | `meet.messaging` | No  | **Who can send in-call chat messages** | enabled  | boolean   
**Meet safety settings** > **Present** | `meet.presenting` | No  | **Who can share their screens in calls.** | enabled  | boolean   
**Meet safety settings** > **Q &A** | `meet.questions` | No  | **Who can participate in Q &A in calls** | enabled  | boolean   
**Meet safety settings** > **Polls** | `meet.polls` | No  | **Who can participate in polls in calls** | enabled  | boolean   
**Meet safety settings** > **Incoming call restrictions** | `meet.meet_incoming_call_restrictions` | No  | **This setting affects only Meet calling, not legacy services or calling in Google Chat. Restrictions set in "Access" can further limit the calls that users can receive.** | allowed_callers  | enum: 

  * `ALLOWED_CALLERS_UNSPECIFIED`
  * `ALL`
  * `CONTACTS_AND_ORGANIZATION_ONLY`
  * `NONE`

  
  
## Provisioning Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported in v1beta1** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Account settings** | **Conflicting accounts management** | `provisioning.conflicting_accounts_management` | No  | **Choose how to manage conflicting accounts** | option  | enum: 

  * `OPTION_UNSPECIFIED`
  * `AUTOMATICALLY_SEND_INVITATIONS`
  * `REPLACE_CONFLICTING_ACCOUNT`
  * `PRESERVE_CONFLICTING_ACCOUNT`

  
**Send daily follow-up emails for (specified) days** | automatic_invitations.invitation_count  | integer   
**If a user doesn't accept an invitation within the selected follow-up period** | automatic_invitations.unaccepted_invitation_resolution_option  | enum: 

  * `UNACCEPTED_INVITATION_RESOLUTION_OPTION_UNSPECIFIED`
  * `REPLACE_CONFLICTING_ACCOUNT_ON_NEXT_CREATION`
  * `PRESERVE_CONFLICTING_ACCOUNT_ON_NEXT_CREATION`

  
  
## Rules and Detectors Settings

This section describes settings for rules and detectors.

### Data Protection Rules Settings

For an overview of how to create data protection rules and detectors for the supported applications, see [Create data protection rules](https://knowledge.workspace.google.com/admin/security/create-data-protection-rules).

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Data protection** | **Security > Access and data control > Data Protection > Manage Rules** | `rule.dlp` | Yes  | **Name** | display_name  | string   
**Description** | description  | string   
**Apps** | triggers  | string[] - A list of application-specific trigger strings. Specify one or more triggers to monitor. The rule evaluates when any of the specified triggers occur. See the Triggers section for available values.   
**Conditions** | condition  | string - Common Expression Language (CEL) expression of the data conditions the rule scans for. The CEL syntax and some common examples are provided in the following Conditions section.   
**Actions** | action  | Struct - nested object representing app specific actions to take when the conditions are met. The available actions per app trigger are provided in the following Actions section.   
**State** | state  | enum: 

  * `ACTIVE`
  * `INACTIVE`

  
**Created** | create_time  | Timestamp   
**Last modified** | update_time  | Timestamp   
**Rule type specific metadata** | rule_type_metadata  | Struct - nested object representing rule type specific metadata. For Data Protection rules, this contains the severity level of the triggered events.   
  
#### Triggers

The following table provides the list of available platforms, applications, and triggers:

**Platform** | **Application** | **Trigger** | **API value**  
---|---|---|---  
Google Workspace  | Gmail  | Message sent  | `google.workspace.gmail.email.v1.send`  
Message received  | `google.workspace.gmail.email.v1.receive`  
Google Drive  | Drive files  | `google.workspace.drive.file.v1.share`  
Google Chat  | Message sent  | `google.workspace.chat.message.v1.send`  
File uploaded  | `google.workspace.chat.attachment.v1.upload`  
Chrome  | Chrome  | File uploaded  | `google.workspace.chrome.file.v1.upload`  
File downloaded  | `google.workspace.chrome.file.v1.download`  
Content pasted  | `google.workspace.chrome.web_content.v1.upload`  
Content printed  | `google.workspace.chrome.page.v1.print`  
URL visited  | `google.workspace.chrome.url.v1.navigation`  
ChromeOS  | ChromeOS  | File transfer restrictions  | `google.workspace.chromeos.file.v1.transfer`  
  
#### Conditions

To represent data conditions, the API uses Common Expressions Language (CEL) expressions. Each condition follows the pattern of `{match source}.{content to scan for}({additional scan parameters})`. For example, `all_content.contains('apple')` represents a data condition that matches if any of the scanned content (e.g. Drive doc, chat message, etc) contains the substring `apple`.

##### Match sources

The list of available match sources, corresponding to the matching configurations of the same names in the Admin Console.

  * `access_levels`
  * `all_content`
  * `all_headers`
  * `body`
  * `destination_type`
  * `destination_url`
  * `drive_enterprise_metadata`
  * `encryption_state`
  * `envelope_from`
  * `file_size_in_bytes`
  * `file_type`
  * `from_header`
  * `message_security_status`
  * `request_attributes`
  * `sender_header`
  * `source_chrome_context`
  * `source_url`
  * `source_url_category`
  * `subject`
  * `suggestion`
  * `target_user`
  * `title`
  * `to_header_recipients`
  * `url`
  * `url_category`



##### Content to scan for

The list of available content to scan for, corresponding to the matching configurations of the same names in the Admin Console.

  * `contains({string})`
  * `starts_with({string})`
  * `ends_with({string})`
  * `equals({string})`
  * `matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`
    * Corresponds to the **matches predefined data type** option in the Admin Console.
    * `{detector name}` denotes the predefined data type to scan for, which can be one of the built-in infotypes supported by Sensitive Data Protection: https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference (for example, `CREDIT_CARD_NUMBER` or `US_SOCIAL_SECURITY_NUMBER`). Some newer detector types aren't supported in this API and return an error if specified.
    * `{likelihood}` denotes the likelihood threshold of the match. For example, **google.privacy.dlp.v2.Likelihood.LIKELY** corresponds to the **High** threshold in the Admin Console.
  * `matches_regex_detector({detector name}, {minimum_match_count: {count}})`
    * Corresponds to the **matches regular expression** option in the Admin Console.
    * `{detector name}` is the resource name of the policy that represents the regular expression detector. See Data Protection Detector section on how to query detector policies in the API.
  * `matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`
    * Corresponds to the **matches words from word list** option in the Admin Console.
    * `{detector name}` is the resource name of the policy that represents the word list detector. See Data Protection Detector section on how to query detector policies in the API.
  * `matches_web_category({category})`
    * Corresponds to the **URL category matches** option in the Admin Console for Chrome URL visited trigger.
    * `{category}` denotes the URL category supported by the Admin Console configuration. For the list of available categories and their API representations, see [URL categories](https://support.google.com/a/answer/13306955).
  * `contains_word({string})`
    * Matches if the content contains `{string}` as a whole word.
  * `matches_file_extension({extension})`
    * Matches if the file extension is `{extension}`.
  * `matches_mime_types({categories}, {custom_types})`
    * Matches if the file's MIME type belongs to one of the specified `{categories}` or `{custom_types}`.
  * `matches_metadata({metadata_criteria})`
    * Matches Drive files based on `{metadata_criteria}` defined in Drive labels.
  * `matches_enum({enum_value})`
    * Matches enum-based fields against `{enum_value}`. For example, `encryption_state.matches_enum('ENCRYPTED')`.
  * `matches_url_list({url_list_id})`
    * Matches if the URL is present in the specified URL list `{url_list_id}`.
  * `matches_url_risk_level({risk_level})`
    * Matches if the URL risk level is `{risk_level}`.
  * `matches_address({email})`
    * Matches if the email address is `{email}`.
  * `matches_address_domain_name({domain})`
    * Matches if domain of the email address is `{domain}`.
  * `matches_address_regex({regex})`
    * Matches if the email address matches the regular expression `{regex}`.



##### Composite conditions

Multiple base conditions can be mixed with AND (&&), OR (||), or NOT (!) operators to form a composite condition. For example, `"all_content.contains('apple') && all_content.contains('banana')"` represents a condition that matches if any of the scanned content contains both 'apple' and 'banana' substrings.

##### CEL Expression Syntax for Rules

The Common Expression Language (CEL) expression that defines a rule's logic is found within the `condition` field of the `Rule` resource. This field is typically a `google.type.Expr` message, with the CEL expression in either an `expression` or `cel_expression` field.

To create a valid rule, you must use CEL functions that are supported by the specific application, trigger event, and match source that you're targeting.

The following table lists the available match sources and condition functions for each application and trigger for Data Protection (DLP) rules.

Application | Trigger Event | Match Source | Available CEL Condition Functions  
---|---|---|---  
**Gmail** | Message sent  
Message received | `all_content`, `body`, `subject`, `all_headers` | `contains({string})`  
`contains_word({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
|  | `file_name` | `contains({string})`  
`contains_word({string})`  
|  | `file_extension` | `matches_file_extension({extension})`  
|  | `file_type` | `matches_mime_types({categories}, {custom_types})`  
|  | `drive_enterprise_metadata` | `matches_metadata({metadata_criteria})`  
|  | `message_security_status` | `matches_enum({enum_value})` (e.g., `'CONFIDENTIAL_MODE_ENABLED'`)  
**Drive** | Drive files | `all_content`, `body` | `contains({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
|  | `title` | `contains({string})`  
`contains_word({string})`  
`ends_with({string})`  
`starts_with({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
|  | `suggestion` | `contains({string})`  
`contains_word({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
|  | `file_name` | `contains({string})`  
`contains_word({string})`  
|  | `file_extension` | `matches_file_extension({extension})`  
|  | `file_type` | `matches_mime_types({categories}, {custom_types})`  
|  | `drive_enterprise_metadata` | `matches_metadata({metadata_criteria})`  
|  | `encryption_state` | `matches_enum({enum_value})` (e.g., `'ENCRYPTED'`)  
**Chat** | Message sent  
File uploaded | `all_content` | `contains({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
| File uploaded only | `file_name` | `contains({string})`  
`contains_word({string})`  
|  | `file_extension` | `matches_file_extension({extension})`  
|  | `file_type` | `matches_mime_types({categories}, {custom_types})`  
**Chrome** | File uploaded  
File downloaded  
Content pasted  
Content printed | `all_content`, `body` | `contains({string})`  
`contains_word({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
| File uploaded  
File downloaded  
Content printed | `title` | `contains({string})`  
`contains_word({string})`  
`ends_with({string})`  
`starts_with({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
| All Chrome Triggers | `url`, `source_url` | `contains({string})`  
`ends_with({string})`  
`starts_with({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_url_list({url_list_id})`  
(Note: `url` also supports `matches_url_risk_level({risk_level})`)  
|  | `url_category`, `source_url_category` | `matches_web_category({category})`  
|  | `file_type` | `matches_mime_types({categories}, {custom_types})`  
|  | `file_size_in_bytes` | Standard comparison operators (e.g., `all_content.file_size_in_bytes > 1048576`)  
|  | `web_app_signed_in_account`, `source_web_app_signed_in_account` | `matches_address({email})`  
`matches_address_domain_name({domain})`  
`matches_address_regex({regex})`  
| Content pasted only | `source_chrome_context` | `matches_enum({enum_value})` (values: `'CLIPBOARD'`, `'INCOGNITO'`, `'OTHER_PROFILE'`)  
**ChromeOS** | File transfer restrictions | `all_content`, `body` | `contains({string})`  
`contains_word({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
|  | `title` | `contains({string})`  
`contains_word({string})`  
`ends_with({string})`  
`starts_with({string})`  
`matches_regex_detector({detector name}, {minimum_match_count: {count}})`  
`matches_dlp_detector({detector name}, {likelihood}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
`matches_word_list({detector name}, {minimum_match_count: {count}, minimum_unique_match_count: {count}})`  
|  | `file_type` | `matches_mime_types({categories}, {custom_types})`  
|  | `file_size_in_bytes` | Standard comparison operators  
  
#### Actions

Each application specifies the action to take when the data condition matches in a nested message. For example, `{ "driveAction" { "warnUser" { } } }` represents a Drive action that warns users on external sharing. The application specific actions available are the following:

**Application** | **Action key** | **Subaction** | **Admin console caption**  
---|---|---|---  
Drive  | driveAction  | blockAccess  | Block external sharing   
warnUser  | Warn on external sharing   
auditOnly  | no action   
restrictCopyPrintDownload  | Disable download, print, and copy   
applyLabels  | Apply Classification labels   
Gmail  | gmailAction  | blockContent  | Block message   
warnUser  | Warn users   
auditOnly  | Audit only   
quarantineMessage  | Quarantine message   
applyLabels  | Apply classification labels   
addFooter  | Add custom note (footer)   
Chat  | chatAction  | blockContent  | Block message   
warnUser  | Warn users   
auditOnly  | Audit only   
Google Chrome  | chromeAction  | blockContent  | Block   
warnUser  | Allow with warning   
ChromeOS  | chromeOsAction  | blockContent  | Block   
warnUser  | Allow with warning   
auditOnly  | Audit only   
  
### Action Parameters

Action parameters provide additional configuration for rule actions. The available parameters depend on the application.

#### Example of Setting Action Parameters

The following example demonstrates how to specify action parameters for a Chrome `blockContent` action, enabling the Evidence Locker (`saveContent`) and setting a watermark message (`watermarkMessage`). This uses the generic Struct representation used by the API.
    
    
    fields {
      key: "action"
      value {
        struct_value {
          fields {
            key: "chromeAction"
            value {
              struct_value {
                fields {
                  key: "blockContent"
                  value {
                    struct_value {
                      fields {
                        key: "actionParams"
                        value {
                          struct_value {
                            fields {
                              key: "saveContent"
                              value {
                                bool_value: true
                              }
                            }
                            fields {
                              key: "watermarkMessage"
                              value {
                                string_value: "CONFIDENTIAL"
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    

#### Drive Action Parameters

Drive actions generally don't take additional parameters. However, the `restrictCopyPrintDownload` action requires specifying a scope.

**Parameter** | **Data type** | **Description**  
---|---|---  
`restrict_copy_print_download.scope` | enum  | Specifies the scope of users to disable download, print, and copy for. 

  * `SCOPE_UNSPECIFIED`: Unspecified scope.
  * `VIEWERS_AND_COMMENTERS`: Disable for viewers and commenters.
  * `ALL_COLLABORATORS`: Disable for all collaborators (viewers, commenters, writers, owners).

  
  
#### Gmail Action Parameters

**Parameter** | **Data type** | **Description**  
---|---|---  
`apply_internal_messages` | boolean  | Applies the action to internal messages.   
`apply_external_messages` | boolean  | Applies the action to external messages.   
`apply_to_internal_receive_messages` | boolean  | Applies the action to internal received messages.   
`apply_to_external_receive_messages` | boolean  | Applies the action to external received messages.   
`custom_end_user_message.unsafe_html_message_body` | string  | HTML message content to display to the end user when a rule triggers. Only `<a>` tags are supported.   
`add_footer.footer.title` | string  | The title of the custom note (maximum 50 characters).   
`add_footer.footer.unsafe_html_message_body` | string  | HTML description text for the custom note. Only `<a>` tags are supported (maximum 300 characters).   
`add_footer.footer.banner_highlighted` | boolean  | Whether the custom note should be highlighted in a banner.   
`add_footer.footer.position` | enum  | The position of the custom note in the message: `TOP` or `BOTTOM`.   
`apply_labels.label_delta` | Struct[]  | List of label changes to apply. Each object contains: 

  * `label_id`: string
  * `field_delta`: Struct with fields: 
    * `field_id`: string
    * `selection`: string (for single selection fields)
    * `selection_list`: Struct with `operation` (`SET`, `MERGE`) and `values` (string[])

  
`apply_labels.conflict_resolution_strategy` | enum  | Strategy to resolve conflicts: `SYSTEM_OVERRIDE` or `ALLOW_USER_OVERRIDE`.   
`apply_labels.custom_end_user_message.unsafe_html_message_body` | string  | HTML message content to display to the end user when the apply labels action triggers. Only `<a>` tags are supported.   
`quarantine_message.quarantine_resource_name` | string  | The resource name of the quarantine. Follows the format `quarantines/obfuscated<id>` or `quarantines/default`.   
  
#### Chat Action Parameters

**Parameter** | **Data type** | **Description**  
---|---|---  
`apply_internal_direct_messages` | boolean  | Applies the action to messages sent using internal 1:1 direct messages.   
`apply_external_direct_messages` | boolean  | Applies the action to messages sent using external 1:1 direct messages.   
`apply_internal_rooms` | boolean  | Applies the action to messages sent to internal rooms.   
`apply_external_rooms` | boolean  | Applies the action to messages sent to external rooms.   
`apply_internal_group_chats` | boolean  | Applies the action to messages sent to internal group chats.   
`apply_external_group_chats` | boolean  | Applies the action to messages sent to external group chats.   
`custom_end_user_message.unsafe_html_message_body` | string  | HTML message content to display to the end user when a rule triggers. Only `<a>` tags are supported.   
  
#### Google Chrome Action Parameters

**Parameter** | **Data type** | **Description**  
---|---|---  
`save_content` | boolean  | Enables securely saving content that triggers this rule (Evidence Locker).   
`watermark_message` | string  | Text displayed as a watermark when a URL navigation rule triggers.   
`custom_end_user_message.unsafe_html_message_body` | string  | HTML message content to display to the end user when a rule triggers. Only `<a>` tags are supported.   
`block_screenshot` | boolean  | Blocks screenshots and screen sharing when set to `true`.   
`match_only_download_url` | boolean  | Evaluates the rule based only on the download URL, ignoring the tab URL.   
`force_save_to_cloud_sub_action.destination` | enum  | Cloud storage destination for forced saves instead of local file system. 

  * `DESTINATION_UNSPECIFIED`: Unspecified destination.
  * `GOOGLE_DRIVE_CORP`: Saves files to corporate Google Drive.
  * `ONEDRIVE_CORP`: Saves files to corporate Microsoft OneDrive.

  
`data_masking.regex_detector` | Struct[]  | A list of regular expression detectors used for data masking. Specify one or more detectors as a list of objects, each containing the fields described in the following table.   
`data_masking.regex_detector[].mask_type` | enum  | Type of masking to apply when the regular expression matches. 

  * `MASK_TYPE_LIGHT_OBFUSCATION`: Masked text can be revealed when holding the pointer over it.
  * `MASK_TYPE_HARD_OBFUSCATION`: Masked text can be revealed on mouse click.
  * `MASK_TYPE_REDACT`: Text is replaced entirely and cannot be recovered.

  
`data_masking.regex_detector[].resource_name` | string  | Identifier of the detector resource.   
`data_masking.regex_detector[].display_name` | string  | Name of the detector displayed in reporting tools (such as the Security Investigation Tool) when triggered.   
`data_masking.regex_detector[].regex_pattern` | string  | The regular expression pattern used for matching. This field is system-populated and shouldn't be set by the user.   
  
#### ChromeOS Action Parameters

**Parameter** | **Data type** | **Description**  
---|---|---  
`save_content` | boolean  | Enables securely saving content that triggers this rule.   
  
#### Rule type specific metadata

This attribute contains the metadata specific to the rule type. For Data Protection rules, it contains the alerting event severity when the event is reported under the security dashboard and alert center. An example value of the metadata representing LOW alert severity:
    
    
    fields {
      key: "ruleTypeMetadata"
      value {
        struct_value {
          fields {
            key: "dlpRuleMetadata"
            value {
              struct_value {
                fields {
                  key: "alertSeverity"
                  value {
                    string_value: "LOW"
                  }
                }
              }
            }
          }
        }
      }
    }
    

### Data Protection Detectors Settings

For an overview of data protection rules and detectors, see [Create DLP for Drive rules and custom content detectors](https://support.google.com/a/answer/9655387).

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Data protection** | **Security > Access and data control > Data Protection > Manage Detectors** | **detector.regular_expression** **detector.word_list** | Yes  | **Name** | display_name  | string   
**Description** | description  | string   
**Regular Expression** | regular_expression  | Struct - contains the regular expression string. Only set if the detector type is detector.regular_expression.   
**Word List** | word_list  | string - contains the list of word strings. Only set if the detector type is `detector.word_list`.   
**Created** | create_time  | Timestamp   
**Last modified** | update_time  | Timestamp   
  
### System Defined Alert Rules Settings

This section describes Google Workspace system-defined alert rules.

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Data protection** | **Rules (for "system defined' rule type)** | `rule.system_defined_alerts` | No  | **Name** | display_name  | string   
**Description** | description  | string   
**Actions** | action  | Struct - nested object representing notification settings when the system defined alert is triggered. Details are provided in the following Actions section.   
**State** | state  | enum: 

  * `ACTIVE`
  * `INACTIVE`

  
**Created** | create_time  | Timestamp   
**Last modified** | update_time  | Timestamp   
  
#### Actions

System defined alert rules have a single action that denotes the notification settings for the alert.

**Action key** | **Subaction** | **Admin console caption** | **Description**  
---|---|---|---  
alertCenterAction  | alertCenterConfig  | Send to alert center  | Configures the alert severity and whether the alert is sent to the alert center.   
recipients  | Send email notifications  | List of email addresses to send notifications to when the alert is triggered.   
  
### Action Parameters

The following table provides the parameters for the `alertCenterAction`:

**Parameter** | **Data type** | **Description**  
---|---|---  
`alertCenterConfig.severity` | enum  | The severity of the alert (e.g., `LOW`, `MEDIUM`, `HIGH`).   
`alertCenterConfig.status` | enum  | Whether the alert is sent to the alert center (e.g., `ENABLED`, `DISABLED`).   
`recipients` | string[]  | A list of email addresses to receive email notifications.   
  
## Security Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Account recovery** | **Super Admin Account Recovery** | `security.super_admin_account_recovery` | No  | **Allow super admins to recover their account** | enableAccountRecovery  | boolean   
**User Account Recovery** | `security.user_account_recovery` | No  | **Allow users and non-super admins to recover their account** | enableAccountRecovery  | boolean   
**Password management** | **Password Management** | `security.password` | No  | **Expiration** | expirationDuration  | Seconds (0 seconds means Never Expire)   
**Reuse** | allowReuse  | boolean   
**Strength and Length enforcement** | enforceRequirementsAtLogin  | boolean   
**Length (Maximum length)** | maximumLength  | integer   
**Length (Minimum length)** | minimumLength  | integer   
**Strength** | allowedStrength  | enum: 

  * `STRONG`
  * `WEAK`

  
**Google session control** | **Session Control** | `security.session_controls` | No  | **Web session duration** | webSessionDuration  | Seconds   
**Less secure apps** | **Less secure apps** | `security.less_secure_apps` | No  | **Control user access to apps that use less secure sign-in technology and make accounts more vulnerable.** | allowLessSecureApps  | boolean   
**Login challenges** | **Login Challenges** | `security.login_challenges` | No  | **Use employee ID to keep my users more secure** | enableEmployeeIdChallenge  | boolean   
**Passwordless** | **Passkeys restriction** | `security.passkeys_restriction` | No  | **Choose the passkey types that users can sign in with** | allowed_passkeys_type  | enum: 

  * `ALLOWED_PASSKEYS_TYPE_UNSPECIFIED`
  * `HARDWARE_SECURITY_KEYS_ONLY`
  * `ANY_DEVICE_OR_PLATFORM`

  
**Advanced Protection program** | **Enrollment** | `security.advanced_protection_program` | No  | **Use employee ID to keep my users more secure** | enableAdvancedProtectionSelfEnrollment  | boolean   
**Security Codes** | securityCodeOption  | enum: 

  * `ALLOWED_WITH_REMOTE_ACCESS`
  * `ALLOWED_WITHOUT_REMOTE_ACCESS`
  * `CODES_NOT_ALLOWED`

  
**2-Step verification** | **Authentication** | `security.two_step_verification_enrollment` | No  | **Allow users to turn on 2-Step Verification** | allowEnrollment  | boolean   
`security.two_step_verification_enforcement` | **Enforcement** | enforcedFrom  | Timestamp   
`security.two_step_verification_grace_period` | **New user enrollment period** | enrollmentGracePeriod  | [Duration](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto)  
`security.two_step_verification_device_trust` | **Allow user to trust the device** | allowTrustingDevice  | boolean   
`security.two_step_verification_enforcement_factor` | **Methods** | allowedSignInFactorSet  | enum: 

  * `ALL`
  * `PASSKEY_ONLY`
  * `PASSKEY_PLUS_SECURITY_CODE`
  * `PASSKEY_PLUS_IP_BOUND_SECURITY_CODE`
  * `NO_TELEPHONY`

  
`security.two_step_verification_sign_in_code` | **2-Step Verification policy suspension grace period** | backupCodeExceptionPeriod  | [Duration](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/duration.proto)  
**Multi-party approval settings** | **Multi-party approval settings** | `multi_party_approval.require_approvals` | No  | **Choose whether an admin with multi-party approval privileges needs to approve sensitive actions taken in the Admin console and Admin API** | multi_party_approval_state  | enum: 

  * `MULTI_PARTY_APPROVAL_STATE_UNSPECIFIED`
  * `ENABLED`
  * `DISABLED`

  
**Multi-party approval for security settings** | `multi_party_approval.security_actions` | No  | **2-step verification** | two_step_verification_multi_party_approval_state   
**Account recovery** | account_recovery_multi_party_approval_state   
**Google session control** | session_controls_multi_party_approval_state   
**Advanced protection program** | advanced_protection_program_multi_party_approval_state   
**Login challenges** | login_challenges_multi_party_approval_state   
**Passwordless** | passwordless_multi_party_approval_state   
**Domain-wide delegation** | domain_wide_delegation_multi_party_approval_state   
**SSO with third-party IDPs** | sso_with_third_party_idps_multi_party_approval_state   
**Context-Aware Access** | context_aware_access_multi_party_approval_state   
**Multi-party approval for API access to security settings** | `multi_party_approval.security_actions_api_access` | No  | **SSO with third-party IDPs** | sso_with_third_party_idps_multi_party_approval_state   
**Multi-party approval for calendar settings** | `multi_party_approval.calendar_actions` | No  | **Calendar Sharing** | calendar_sharing_multi_party_approval_state   
**General calendar settings** | general_calendar_settings_multi_party_approval_state   
**Calendar third party archiving settings** | third_party_archiving_settings_multi_party_approval_state   
**Multi-party approval for groups settings** | `multi_party_approval.groups_actions` | No  | **Groups sharing** | groups_sharing_multi_party_approval_state   
**Multi-party approval for domains admin settings** | `multi_party_approval.domains_actions` | No  | **Domains API** | domains_api_multi_party_approval_state   
  
## Service Status Settings

The `service_status` setting contains a boolean value implying if a service is enabled for a certain `OrgUnit` or `Group`.

The Policy API supports service status settings for **Google Workspace** , **Additional Google services** , and **Generative AI** services that are listed in the Admin Console.

### Google Workspace

**Service name in Admin console** | **Service name in Policy API**  
---|---  
AppSheet  | appsheet   
Calendar  | calendar   
Cloud Search  | cloud_search   
Drive and Docs  | drive_and_docs   
Gmail  | gmail   
Google Chat  | chat   
Google Meet  | meet   
Google Vault  | vault   
Google Voice  | voice   
Groups for Business  | groups_for_business   
Keep  | keep   
Sites  | sites   
Tasks  | tasks   
  
### Additional Google services

**Service name in Admin console** | **Service name in Policy API**  
---|---  
AI Studio  | ai_studio   
Applied Digital Skills  | applied_digital_skills   
Assignments  | assignments   
Blogger  | blogger   
Brand Accounts  | brand_accounts   
Campaign Manager 360  | campaign_manager   
Chrome Canvas  | chrome_canvas   
Chrome Cursive  | chrome_cursive   
Chrome Remote Desktop  | chrome_remote_desktop   
Chrome Web Store  | chrome_web_store   
Classroom  | classroom   
CS First  | cs_first   
Currents  | currents   
Early Access Apps  | early_access_apps   
Experimental Apps  | experimental_apps   
FeedBurner  | feedburner   
Google Ad Manager  | ad_manager   
Google Ads  | ads   
Google AdSense  | adsense   
Google Alerts  | alerts   
Google Analytics  | analytics   
Google Arts & Culture  | arts_and_culture   
Google Bookmarks  | bookmarks   
Google Books  | books   
Google Chrome Sync  | chrome_sync   
Google Cloud  | cloud   
Google Cloud Print  | cloud_print   
Google Colab  | Colab   
Google Developer  | developers   
Google Domains  | domains   
Google Earth  | earth   
Google Fi  | fi   
Google Groups  | groups   
Google Maps  | maps   
Google Messages  | messages   
Google My Business  | my_business   
Google My Maps  | my_maps   
Google News  | news   
Google Pay  | pay   
Google Photos  | photos   
Google Play  | play   
Google Play Console  | play_console   
Google Public Data Explorer  | public_data   
Google Read Along  | read_along   
Google Search Console  | search_console   
Google Takeout  | takeout   
Google Translate  | translate   
Google Trips  | trips   
Jamboard  | jamboard   
Location History  | location_history   
Data Studio  | data_studio   
Managed Google Play  | managed_play   
Material Gallery  | material_gallery   
Merchant Center  | merchant_center   
Partner Dash  | partner_dash   
Pinpoint  | pinpoint   
Play Books Partner Center  | play_books_partner_center   
Programmable Search Engine  | programmable_search_engine   
QuestionHub  | question_hub   
Scholar Profiles  | scholar_profiles   
Search Ads 360  | search_ads_360   
Search and Assistant  | search_and_assistant   
Socratic  | socratic   
Studio  | studio   
Third-party App Backups  | third_party_app_backups   
Tour Creator  | tour_creator   
Work Insights  | work_insights   
YouTube  | youtube   
  
### Generative AI

**Service name in Admin console** | **Service name in Policy API**  
---|---  
Gemini app  | gemini_app   
NotebookLM  | notebooklm   
  
## Sites Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Sites** | **New Sites > Site creation and editing** | `sites.sites_creation_and_modification` | No  | **Allow users to create new sites** | allowSitesCreation  | boolean   
| **Users can/cannot edit sites** | allowSitesModification  | boolean   
  
## UserTakeout Settings

**Page in Admin console** | **Specific setting in Admin console** | **Policy API setting type** | **Mutate supported** | **Admin console caption** | **Policy API field name** | **Data type**  
---|---|---|---|---|---|---  
**Data** | **Data import & export > Google Takeout > User access to Takeout for Google services** | 

  * `blogger.user_takeout`
  * `books.user_takeout`
  * `maps.user_takeout`
  * `pay.user_takeout`
  * `photos.user_takeout`
  * `play.user_takeout`
  * `play_console.user_takeout`
  * `location_history.user_takeout`
  * `youtube.user_takeout`

| No  | **Manage user access to Takeout for Google services** | takeout_status  | enum: 

  * `TAKEOUT_STATUS_UNSPECIFIED`
  * `ENABLED`
  * `DISABLED`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
