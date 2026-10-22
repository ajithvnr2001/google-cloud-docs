---
url: https://docs.cloud.google.com/identity/docs/how-to/dynamic-groups-attributes/
title: Valid user fields for dynamic group queries \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:29.640296+00:00
---

# Valid user fields for dynamic group queries  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/dynamic-groups-attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Valid user fields for dynamic group queries

This page outlines supported fields and features of CEL that can be used in a membership query.

**Note:** Dynamic groups are only available to Google Workspace Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity premium accounts.

## User fields

The following fields from the Admin SDK's [`User`](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) resource can be used in membership queries.

**Note:** Custom user fields are also supported as long as the schema already exists in `user.custom_schemas`. See [Manage custom user fields](https://developers.google.com/admin-sdk/directory/v1/guides/manage-schemas) for more information about creating a custom schema.Field | Sub-field  
---|---  
`addresses` | `country`  
| `country_code`  
| `custom_type`  
| `extended_address`  
| `locality`  
| `po_box`  
| `postal_code`  
| `primary`  
| `region`  
| `street_address`  
| `type`  
`archived` | boolean  
`change_password_at_next_login` | boolean  
`is_2sv_enforced` | boolean  
`is_enrolled_in_2sv` | boolean  
`is_mailbox_setup` | boolean  
`locations` | `area`  
| `building_id`  
| `custom_type`  
| `desk_code`  
| `floor_name`  
| `floor_section`  
| `type`  
`organizations` | `cost_center`  
| `custom_type`  
| `department`  
| `description`  
| `domain`  
| `location`  
| `name`  
| `primary`  
| `symbol`  
| `title`  
| `type`  
`relations` | `custom_type`  
| `type`  
| `value`  
`emails` | `address`  
| `custom_type`  
| `primary`  
| `type`  
`external_ids` | `custom_type`  
| `type`  
| `value`  
`gender` | `address_me_as`  
| `custom_gender`  
| `type`  
`ims` | `custom_protocol`  
| `custom_type`  
| `standard_protocol`  
| `primary`  
| `type`  
| `value`  
`keywords` | `custom_type`  
| `type`  
| `value`  
`languages` | `language_code`  
`name` | `family_name`  
| `given_name`  
| `value`  
`phones` | `custom_type`  
| `primary`  
| `type`  
| `value`  
`suspended` | boolean  
`suspension_reason` | `custom_type`  
| `type`  
| `value`  
`websites` | `custom_type`  
| `primary`  
| `type`  
| `value`  
**Note:** When a field has a `primary` value, that value can only be evaluated as a true expression. For example:  
`user.addresses.exists(addr, addr.primary == true)"`

### Type attributes

The `type` attributes from the previous table are matched using enum values instead of their string representations. The following list documents each type's string representation to the corresponding enum value.

Attribute | Enum value | String representation  
---|---|---  
Addresses | `0` | unknown  
| `1` | custom  
| `2` | home  
| `3` | work  
| `4` | other  
Locations | `0` | default  
| `1` | custom  
| `2` | desk  
Organizations | `0` | unknown  
| `1` | work  
| `2` | school  
| `3` | domain-only  
Relations | `12` | manager  
Emails | `0` | unknown  
| `1` | custom  
| `2` | home  
| `3` | work  
| `4` | other  
External IDs | `0` | unknown  
| `1` | custom  
| `2` | account  
| `3` | customer  
| `4` | network  
| `5` | organization  
| `6` | login_id  
Gender | `0` | unknown  
| `1` | male  
| `2` | female  
| `3` | other  
IMS standard protocol | `0` | default  
| `1` | custom protocol  
| `2` | aim  
| `3` | msn  
| `4` | yahoo  
| `5` | skype  
| `6` | qq  
| `7` | gtalk  
| `8` | icq  
| `9` | jabber  
| `10` | net meeting  
IMS type | `0` | unknown  
| `1` | custom  
| `2` | home  
| `3` | work  
| `4` | other  
Keywords | `0` | unknown  
| `1` | custom  
| `2` | mission  
| `3` | occupation  
| `4` | outlook  
Phones | `0` | unknown  
| `1` | custom  
| `2` | home  
| `3` | work  
| `4` | other  
| `5` | home fax  
| `6` | work fax  
| `7` | mobile  
| `8` | pager  
| `9` | other fax  
| `10` | company main  
| `11` | assistant  
| `12` | car  
| `13` | radio  
| `14` | isdn  
| `15` | callback  
| `16` | telex  
| `17` | tty tdd  
| `18` | work mobile  
| `19` | work pager  
| `20` | main  
| `21` | grand central  
| `22` | enterprise voice  
Suspension Reason | `1` | admin  
| `2` | under 13  
| `3` | web login required  
| `4` | abuse  
| `5` | abuse—recoverable by admin  
Websites | `0` | unknown  
| `1` | app install page  
| `2` | blog  
| `3` | custom  
| `4` | ftp  
| `5` | home  
| `6` | home page  
| `7` | other  
| `8` | profile  
| `9` | reservations  
| `10` | resume  
| `11` | work  
  
## Organizational unit fields

You can also query memberships using the `orgUnitId` field to include all users who are part of that organizational unit, directly or indirectly. For more information about retrieving the `orgUnitId` value, see the [Admin SDK reference documentation](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits).

### Sample queries

  * All direct users under a given organizational unit:
        
        user.org_unit_id==orgUnitId('03ph8a2z1enx4lx')
        

  * All direct and indirect users under a given organizational unit:
        
        user.org_units.exists(org_unit, org_unit.org_unit_id==orgUnitId('03ph8a2z1khexns'))
        




## Other query types

  * All users managed by a specific individual:
        
        user.managers.exists(manager, manager.user_id == userId('MANAGER_ID'))
        

Replace `MANAGER_ID` with the manager's unique user ID. You can retrieve this ID with the [AdminSDK Directory API](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/get) using the manager's email address as `userKey`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
