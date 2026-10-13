---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ErrorReason
title: Enum ErrorReason (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:05.559592+00:00
---

# Enum ErrorReason (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ErrorReason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum ErrorReason (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum ErrorReason extends Enum<ErrorReason> implements ProtocolMessageEnum

Error reasons for Data Manager API. NOTE: This enum is not frozen and new values may be added in the future.

Protobuf enum `google.ads.datamanager.v1.ErrorReason`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`ACCOUNT_INELIGIBLE_FOR_STORE_SALES` |  Account is not eligible for Store Sales. `ACCOUNT_INELIGIBLE_FOR_STORE_SALES = 102;`  
`ACCOUNT_INELIGIBLE_FOR_STORE_SALES_VALUE` |  Account is not eligible for Store Sales. `ACCOUNT_INELIGIBLE_FOR_STORE_SALES = 102;`  
`ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA` |  The advertiser is not allowlisted for THIRD_PARTY_PARTNER_DATA. `ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA = 91;`  
`ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA_VALUE` |  The advertiser is not allowlisted for THIRD_PARTY_PARTNER_DATA. `ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA = 91;`  
`ADVERTISER_NOT_ALLOWLISTED_FOR_UPLOADED_DATA` |  The advertiser needs to be allowlisted to use remarketing lists created from advertiser uploaded data. `ADVERTISER_NOT_ALLOWLISTED_FOR_UPLOADED_DATA = 84;`  
`ADVERTISER_NOT_ALLOWLISTED_FOR_UPLOADED_DATA_VALUE` |  The advertiser needs to be allowlisted to use remarketing lists created from advertiser uploaded data. `ADVERTISER_NOT_ALLOWLISTED_FOR_UPLOADED_DATA = 84;`  
`ADVERTISER_TOS_NOT_ACCEPTED` |  The advertiser has not accepted the partner's terms of service. `ADVERTISER_TOS_NOT_ACCEPTED = 90;`  
`ADVERTISER_TOS_NOT_ACCEPTED_VALUE` |  The advertiser has not accepted the partner's terms of service. `ADVERTISER_TOS_NOT_ACCEPTED = 90;`  
`ALREADY_EXISTS` |  The resource already exists. `ALREADY_EXISTS = 52;`  
`ALREADY_EXISTS_VALUE` |  The resource already exists. `ALREADY_EXISTS = 52;`  
`BASELINE_LOCATION_AUTO_DETECTION_FAILED` |  The location_auto_detection_enabled field of the request was set to `true`, but auto detection of baseline location failed. `BASELINE_LOCATION_AUTO_DETECTION_FAILED = 122;`  
`BASELINE_LOCATION_AUTO_DETECTION_FAILED_VALUE` |  The location_auto_detection_enabled field of the request was set to `true`, but auto detection of baseline location failed. `BASELINE_LOCATION_AUTO_DETECTION_FAILED = 122;`  
`BILLABLE_RECORD_COUNT_IMMUTABLE` |  The remarketing user list's billable record field cannot be modified once it is set. `BILLABLE_RECORD_COUNT_IMMUTABLE = 82;`  
`BILLABLE_RECORD_COUNT_IMMUTABLE_VALUE` |  The remarketing user list's billable record field cannot be modified once it is set. `BILLABLE_RECORD_COUNT_IMMUTABLE = 82;`  
`BOTH_CLIENT_ID_AND_APP_INSTANCE_ID_NOT_ALLOWED` |  Both app_instance_id and client_id are set. `BOTH_CLIENT_ID_AND_APP_INSTANCE_ID_NOT_ALLOWED = 111;`  
`BOTH_CLIENT_ID_AND_APP_INSTANCE_ID_NOT_ALLOWED_VALUE` |  Both app_instance_id and client_id are set. `BOTH_CLIENT_ID_AND_APP_INSTANCE_ID_NOT_ALLOWED = 111;`  
`CANNOT_CREATE_LICENSE_FOR_SENSITIVE_USERLIST` |  Sensitive user lists cannot be licensed to this client. `CANNOT_CREATE_LICENSE_FOR_SENSITIVE_USERLIST = 59;`  
`CANNOT_CREATE_LICENSE_FOR_SENSITIVE_USERLIST_VALUE` |  Sensitive user lists cannot be licensed to this client. `CANNOT_CREATE_LICENSE_FOR_SENSITIVE_USERLIST = 59;`  
`CANNOT_DISABLE_LICENSE` |  Reseller license cannot be disabled since it is in use. `CANNOT_DISABLE_LICENSE = 61;`  
`CANNOT_DISABLE_LICENSE_VALUE` |  Reseller license cannot be disabled since it is in use. `CANNOT_DISABLE_LICENSE = 61;`  
`CANNOT_LICENSE_LOGICAL_LIST_WITH_LICENSED_OR_SHARED_SEGMENT` |  Logical user list with shared or licensed segment cannot be licensed. `CANNOT_LICENSE_LOGICAL_LIST_WITH_LICENSED_OR_SHARED_SEGMENT = 67;`  
`CANNOT_LICENSE_LOGICAL_LIST_WITH_LICENSED_OR_SHARED_SEGMENT_VALUE` |  Logical user list with shared or licensed segment cannot be licensed. `CANNOT_LICENSE_LOGICAL_LIST_WITH_LICENSED_OR_SHARED_SEGMENT = 67;`  
`CANNOT_UPDATE_DISABLED_LICENSE` |  Cannot update a license that has been disabled. `CANNOT_UPDATE_DISABLED_LICENSE = 58;`  
`CANNOT_UPDATE_DISABLED_LICENSE_VALUE` |  Cannot update a license that has been disabled. `CANNOT_UPDATE_DISABLED_LICENSE = 58;`  
`COMMERCE_AUDIENCE_CAN_ONLY_BE_DIRECTLY_LICENSED` |  Commerce audience can only be directly licensed. `COMMERCE_AUDIENCE_CAN_ONLY_BE_DIRECTLY_LICENSED = 75;`  
`COMMERCE_AUDIENCE_CAN_ONLY_BE_DIRECTLY_LICENSED_VALUE` |  Commerce audience can only be directly licensed. `COMMERCE_AUDIENCE_CAN_ONLY_BE_DIRECTLY_LICENSED = 75;`  
`COMMERCE_PARTNER_NOT_ALLOWED` |  Setting the `commerce_partner` field is only supported if the `partner_audience_source` is `COMMERCE_AUDIENCE`. `COMMERCE_PARTNER_NOT_ALLOWED = 86;`  
`COMMERCE_PARTNER_NOT_ALLOWED_VALUE` |  Setting the `commerce_partner` field is only supported if the `partner_audience_source` is `COMMERCE_AUDIENCE`. `COMMERCE_PARTNER_NOT_ALLOWED = 86;`  
`CONVERSION_ACTION_TOO_RECENTLY_CREATED` |  The conversion action was created too recently. `CONVERSION_ACTION_TOO_RECENTLY_CREATED = 127;`  
`CONVERSION_ACTION_TOO_RECENTLY_CREATED_VALUE` |  The conversion action was created too recently. `CONVERSION_ACTION_TOO_RECENTLY_CREATED = 127;`  
`CUSTOMER_NOT_ALLOWED_TO_CREATE_LICENSE` |  Customer not allowed to create license. `CUSTOMER_NOT_ALLOWED_TO_CREATE_LICENSE = 65;`  
`CUSTOMER_NOT_ALLOWED_TO_CREATE_LICENSE_VALUE` |  Customer not allowed to create license. `CUSTOMER_NOT_ALLOWED_TO_CREATE_LICENSE = 65;`  
`CUSTOMER_NOT_ALLOWLISTED_FOR_COMMERCE_AUDIENCE` |  The data provider is not allowlisted to create commerce audiences. `CUSTOMER_NOT_ALLOWLISTED_FOR_COMMERCE_AUDIENCE = 94;`  
`CUSTOMER_NOT_ALLOWLISTED_FOR_COMMERCE_AUDIENCE_VALUE` |  The data provider is not allowlisted to create commerce audiences. `CUSTOMER_NOT_ALLOWLISTED_FOR_COMMERCE_AUDIENCE = 94;`  
`CUSTOM_VARIABLE_NOT_ENABLED` |  The custom variable is not enabled. `CUSTOM_VARIABLE_NOT_ENABLED = 118;`  
`CUSTOM_VARIABLE_NOT_ENABLED_VALUE` |  The custom variable is not enabled. `CUSTOM_VARIABLE_NOT_ENABLED = 118;`  
`CUSTOM_VARIABLE_NOT_FOUND` |  The destination does not have a custom variable with a name that matches the specified `variable`. `CUSTOM_VARIABLE_NOT_FOUND = 120;`  
`CUSTOM_VARIABLE_NOT_FOUND_VALUE` |  The destination does not have a custom variable with a name that matches the specified `variable`. `CUSTOM_VARIABLE_NOT_FOUND = 120;`  
`CUSTOM_VARIABLE_VALUE_CONTAINS_PII` |  The custom variable value contains personally identifiable information (PII). `CUSTOM_VARIABLE_VALUE_CONTAINS_PII = 117;`  
`CUSTOM_VARIABLE_VALUE_CONTAINS_PII_VALUE` |  The custom variable value contains personally identifiable information (PII). `CUSTOM_VARIABLE_VALUE_CONTAINS_PII = 117;`  
`DATA_PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA` |  The data partner is not allowlisted for THIRD_PARTY_PARTNER_DATA. `DATA_PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA = 89;`  
`DATA_PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA_VALUE` |  The data partner is not allowlisted for THIRD_PARTY_PARTNER_DATA. `DATA_PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA = 89;`  
`DATA_PARTNER_USER_LIST_MUTATE_NOT_ALLOWED` |  Data Partner does not have access to the operating account owned userlist. `DATA_PARTNER_USER_LIST_MUTATE_NOT_ALLOWED = 21;`  
`DATA_PARTNER_USER_LIST_MUTATE_NOT_ALLOWED_VALUE` |  Data Partner does not have access to the operating account owned userlist. `DATA_PARTNER_USER_LIST_MUTATE_NOT_ALLOWED = 21;`  
`DEADLINE_EXCEEDED` |  The request took too long to respond. `DEADLINE_EXCEEDED = 2;`  
`DEADLINE_EXCEEDED_VALUE` |  The request took too long to respond. `DEADLINE_EXCEEDED = 2;`  
`DESTINATION_ACCOUNT_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS` |  Enhanced conversions can't be used for the destination account because of Google customer data policies. Contact your Google representative.. `DESTINATION_ACCOUNT_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS = 34;`  
`DESTINATION_ACCOUNT_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS_VALUE` |  Enhanced conversions can't be used for the destination account because of Google customer data policies. Contact your Google representative.. `DESTINATION_ACCOUNT_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS = 34;`  
`DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED` |  The destination account hasn't agreed to the terms for enhanced conversions. `DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED = 35;`  
`DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED_VALUE` |  The destination account hasn't agreed to the terms for enhanced conversions. `DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED = 35;`  
`DESTINATION_ACCOUNT_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS` |  The destination account is not enabled for enhanced conversions for leads. `DESTINATION_ACCOUNT_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS = 33;`  
`DESTINATION_ACCOUNT_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS_VALUE` |  The destination account is not enabled for enhanced conversions for leads. `DESTINATION_ACCOUNT_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS = 33;`  
`DESTINATION_ACCOUNT_TYPE_MISMATCH` |  The destination account type does not match the specified account id. `DESTINATION_ACCOUNT_TYPE_MISMATCH = 116;`  
`DESTINATION_ACCOUNT_TYPE_MISMATCH_VALUE` |  The destination account type does not match the specified account id. `DESTINATION_ACCOUNT_TYPE_MISMATCH = 116;`  
`DIFFERENT_LOGIN_ACCOUNTS_NOT_ALLOWED_FOR_DATA_PARTNER` |  Destination configs containing a DataPartner login account must have the same login account across all destination configs. `DIFFERENT_LOGIN_ACCOUNTS_NOT_ALLOWED_FOR_DATA_PARTNER = 25;`  
`DIFFERENT_LOGIN_ACCOUNTS_NOT_ALLOWED_FOR_DATA_PARTNER_VALUE` |  Destination configs containing a DataPartner login account must have the same login account across all destination configs. `DIFFERENT_LOGIN_ACCOUNTS_NOT_ALLOWED_FOR_DATA_PARTNER = 25;`  
`DISPLAY_NAME_ALREADY_USED` |  The display name is already being used for another user list for the account. `DISPLAY_NAME_ALREADY_USED = 78;`  
`DISPLAY_NAME_ALREADY_USED_VALUE` |  The display name is already being used for another user list for the account. `DISPLAY_NAME_ALREADY_USED = 78;`  
`DUPLICATE_DESTINATION_REFERENCE` |  Two or more destinations in the request have the same reference. `DUPLICATE_DESTINATION_REFERENCE = 36;`  
`DUPLICATE_DESTINATION_REFERENCE_VALUE` |  Two or more destinations in the request have the same reference. `DUPLICATE_DESTINATION_REFERENCE = 36;`  
`ERROR_REASON_UNSPECIFIED` |  Do not use this default value. `ERROR_REASON_UNSPECIFIED = 0;`  
`ERROR_REASON_UNSPECIFIED_VALUE` |  Do not use this default value. `ERROR_REASON_UNSPECIFIED = 0;`  
`EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED` |  The customer contains non-exempt campaigns without the EU political advertising declaration. `EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED = 101;`  
`EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED_VALUE` |  The customer contains non-exempt campaigns without the EU political advertising declaration. `EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED = 101;`  
`EVENT_SOURCE_AND_DESTINATION_MISMATCH` |  The event source type does not match the destination type. `EVENT_SOURCE_AND_DESTINATION_MISMATCH = 115;`  
`EVENT_SOURCE_AND_DESTINATION_MISMATCH_VALUE` |  The event source type does not match the destination type. `EVENT_SOURCE_AND_DESTINATION_MISMATCH = 115;`  
`EVENT_TIME_INVALID` |  Event did not occur within the acceptable time window. `EVENT_TIME_INVALID = 44;`  
`EVENT_TIME_INVALID_VALUE` |  Event did not occur within the acceptable time window. `EVENT_TIME_INVALID = 44;`  
`FIELD_VALUE_TOO_LONG` |  Length of the field value is too long. `FIELD_VALUE_TOO_LONG = 50;`  
`FIELD_VALUE_TOO_LONG_VALUE` |  Length of the field value is too long. `FIELD_VALUE_TOO_LONG = 50;`  
`FIELD_VALUE_TOO_SHORT` |  Length of the field value is too short. `FIELD_VALUE_TOO_SHORT = 106;`  
`FIELD_VALUE_TOO_SHORT_VALUE` |  Length of the field value is too short. `FIELD_VALUE_TOO_SHORT = 106;`  
`GOOGLE_ANALYTICS_SUBPROPERTY_OR_ROLLUP_PROPERTY_NOT_ALLOWED` |  The Google Analytics property is a subproperty or rollup property. `GOOGLE_ANALYTICS_SUBPROPERTY_OR_ROLLUP_PROPERTY_NOT_ALLOWED = 112;`  
`GOOGLE_ANALYTICS_SUBPROPERTY_OR_ROLLUP_PROPERTY_NOT_ALLOWED_VALUE` |  The Google Analytics property is a subproperty or rollup property. `GOOGLE_ANALYTICS_SUBPROPERTY_OR_ROLLUP_PROPERTY_NOT_ALLOWED = 112;`  
`IMMUTABLE_FIELD_FOR_UPDATE` |  Attempted to set an immutable field for an update request. `IMMUTABLE_FIELD_FOR_UPDATE = 53;`  
`IMMUTABLE_FIELD_FOR_UPDATE_VALUE` |  Attempted to set an immutable field for an update request. `IMMUTABLE_FIELD_FOR_UPDATE = 53;`  
`INSIGHTS_MISSING_FOR_DIMENSION` |  Insights missing for this dimension. `INSIGHTS_MISSING_FOR_DIMENSION = 123;`  
`INSIGHTS_MISSING_FOR_DIMENSION_VALUE` |  Insights missing for this dimension. `INSIGHTS_MISSING_FOR_DIMENSION = 123;`  
`INSUFFICIENT_COST` |  Cost too low for this license. `INSUFFICIENT_COST = 60;`  
`INSUFFICIENT_COST_VALUE` |  Cost too low for this license. `INSUFFICIENT_COST = 60;`  
`INTERNAL_ERROR` |  An internal error has occurred. `INTERNAL_ERROR = 1;`  
`INTERNAL_ERROR_VALUE` |  An internal error has occurred. `INTERNAL_ERROR = 1;`  
`INVALID_AD_IDENTIFIER_FOR_ACCOUNT` |  The ad identifier does not belong to the account. For example, the `gclid` isn't associated with the `operating_account` and `product_destination_id` of the destination. `INVALID_AD_IDENTIFIER_FOR_ACCOUNT = 128;`  
`INVALID_AD_IDENTIFIER_FOR_ACCOUNT_VALUE` |  The ad identifier does not belong to the account. For example, the `gclid` isn't associated with the `operating_account` and `product_destination_id` of the destination. `INVALID_AD_IDENTIFIER_FOR_ACCOUNT = 128;`  
`INVALID_ARGUMENT` |  There was a problem with the request. `INVALID_ARGUMENT = 6;`  
`INVALID_ARGUMENT_VALUE` |  There was a problem with the request. `INVALID_ARGUMENT = 6;`  
`INVALID_AUDIENCE_MEMBER` |  This audience member is not valid. `INVALID_AUDIENCE_MEMBER = 16;`  
`INVALID_AUDIENCE_MEMBER_VALUE` |  This audience member is not valid. `INVALID_AUDIENCE_MEMBER = 16;`  
`INVALID_BASE64_ENCODING` |  The base64 encoded value is malformed. `INVALID_BASE64_ENCODING = 10;`  
`INVALID_BASE64_ENCODING_VALUE` |  The base64 encoded value is malformed. `INVALID_BASE64_ENCODING = 10;`  
`INVALID_CLIENT_ACCOUNT_ID` |  Invalid client account id. `INVALID_CLIENT_ACCOUNT_ID = 62;`  
`INVALID_CLIENT_ACCOUNT_ID_VALUE` |  Invalid client account id. `INVALID_CLIENT_ACCOUNT_ID = 62;`  
`INVALID_COMMERCE_PARTNER` |  The `commerce_partner` field is invalid. `INVALID_COMMERCE_PARTNER = 93;`  
`INVALID_COMMERCE_PARTNER_VALUE` |  The `commerce_partner` field is invalid. `INVALID_COMMERCE_PARTNER = 93;`  
`INVALID_CONTINENT_CODE` |  The continent code is not valid. `INVALID_CONTINENT_CODE = 109;`  
`INVALID_CONTINENT_CODE_VALUE` |  The continent code is not valid. `INVALID_CONTINENT_CODE = 109;`  
`INVALID_CONVERSION_ACTION_ID` |  Conversion action ID is not valid. `INVALID_CONVERSION_ACTION_ID = 28;`  
`INVALID_CONVERSION_ACTION_ID_VALUE` |  Conversion action ID is not valid. `INVALID_CONVERSION_ACTION_ID = 28;`  
`INVALID_CONVERSION_ACTION_TYPE` |  The conversion action type is not valid. `INVALID_CONVERSION_ACTION_TYPE = 29;`  
`INVALID_CONVERSION_ACTION_TYPE_VALUE` |  The conversion action type is not valid. `INVALID_CONVERSION_ACTION_TYPE = 29;`  
`INVALID_COST_TYPE` |  Invalid cost type. `INVALID_COST_TYPE = 72;`  
`INVALID_COST_TYPE_VALUE` |  Invalid cost type. `INVALID_COST_TYPE = 72;`  
`INVALID_COUNTRY_CODE` |  Deprecated: Enum is unused in the Data Manager API. `INVALID_COUNTRY_CODE = 13 [deprecated = true];`  
`INVALID_COUNTRY_CODE_VALUE` |  Deprecated: Enum is unused in the Data Manager API. `INVALID_COUNTRY_CODE = 13 [deprecated = true];`  
`INVALID_COUPON_CODE` |  The coupon code is not valid. `INVALID_COUPON_CODE = 114;`  
`INVALID_COUPON_CODE_VALUE` |  The coupon code is not valid. `INVALID_COUPON_CODE = 114;`  
`INVALID_CURRENCY_CODE` |  The currency code is not supported. `INVALID_CURRENCY_CODE = 30;`  
`INVALID_CURRENCY_CODE_VALUE` |  The currency code is not supported. `INVALID_CURRENCY_CODE = 30;`  
`INVALID_CUSTOM_VARIABLE_VALUE` |  The custom variable's value is invalid. `INVALID_CUSTOM_VARIABLE_VALUE = 119;`  
`INVALID_CUSTOM_VARIABLE_VALUE_VALUE` |  The custom variable's value is invalid. `INVALID_CUSTOM_VARIABLE_VALUE = 119;`  
`INVALID_DESCRIPTION` |  The description is not valid. `INVALID_DESCRIPTION = 76;`  
`INVALID_DESCRIPTION_VALUE` |  The description is not valid. `INVALID_DESCRIPTION = 76;`  
`INVALID_DESTINATION` |  This Destination is not valid. `INVALID_DESTINATION = 20;`  
`INVALID_DESTINATION_VALUE` |  This Destination is not valid. `INVALID_DESTINATION = 20;`  
`INVALID_DEVICE_CATEGORY` |  The device category is not valid. `INVALID_DEVICE_CATEGORY = 110;`  
`INVALID_DEVICE_CATEGORY_VALUE` |  The device category is not valid. `INVALID_DEVICE_CATEGORY = 110;`  
`INVALID_DISPLAY_NAME` |  The display name is not valid. `INVALID_DISPLAY_NAME = 77;`  
`INVALID_DISPLAY_NAME_VALUE` |  The display name is not valid. `INVALID_DISPLAY_NAME = 77;`  
`INVALID_ENUM_VALUE` |  Enum value cannot be used. `INVALID_ENUM_VALUE = 14;`  
`INVALID_ENUM_VALUE_VALUE` |  Enum value cannot be used. `INVALID_ENUM_VALUE = 14;`  
`INVALID_EVENT` |  This event is not valid. `INVALID_EVENT = 31;`  
`INVALID_EVENT_NAME` |  The event name is not supported. `INVALID_EVENT_NAME = 46;`  
`INVALID_EVENT_NAME_VALUE` |  The event name is not supported. `INVALID_EVENT_NAME = 46;`  
`INVALID_EVENT_VALUE` |  This event is not valid. `INVALID_EVENT = 31;`  
`INVALID_FILTER` |  The query filter is invalid. `INVALID_FILTER = 55;`  
`INVALID_FILTER_VALUE` |  The query filter is invalid. `INVALID_FILTER = 55;`  
`INVALID_FORMAT` |  Format is invalid. `INVALID_FORMAT = 8;`  
`INVALID_FORMAT_VALUE` |  Format is invalid. `INVALID_FORMAT = 8;`  
`INVALID_HEX_ENCODING` |  The HEX encoded value is malformed. `INVALID_HEX_ENCODING = 9;`  
`INVALID_HEX_ENCODING_VALUE` |  The HEX encoded value is malformed. `INVALID_HEX_ENCODING = 9;`  
`INVALID_MEDIA_SHARE_COST` |  Invalid media share cost. `INVALID_MEDIA_SHARE_COST = 71;`  
`INVALID_MEDIA_SHARE_COST_VALUE` |  Invalid media share cost. `INVALID_MEDIA_SHARE_COST = 71;`  
`INVALID_MERCHANT_FEED_LANGUAGE_CODE` |  The merchant feed language code is not valid. `INVALID_MERCHANT_FEED_LANGUAGE_CODE = 103;`  
`INVALID_MERCHANT_FEED_LANGUAGE_CODE_VALUE` |  The merchant feed language code is not valid. `INVALID_MERCHANT_FEED_LANGUAGE_CODE = 103;`  
`INVALID_MERCHANT_ID` |  The `merchant_id` field is not valid. `INVALID_MERCHANT_ID = 100;`  
`INVALID_MERCHANT_ID_VALUE` |  The `merchant_id` field is not valid. `INVALID_MERCHANT_ID = 100;`  
`INVALID_MOBILE_ID_FORMAT` |  Mobile ID format is not valid. `INVALID_MOBILE_ID_FORMAT = 22;`  
`INVALID_MOBILE_ID_FORMAT_VALUE` |  Mobile ID format is not valid. `INVALID_MOBILE_ID_FORMAT = 22;`  
`INVALID_NUMBER_FORMAT` |  Invalid number format. `INVALID_NUMBER_FORMAT = 27;`  
`INVALID_NUMBER_FORMAT_VALUE` |  Invalid number format. `INVALID_NUMBER_FORMAT = 27;`  
`INVALID_PAGE_TOKEN` |  The page token is invalid. `INVALID_PAGE_TOKEN = 57;`  
`INVALID_PAGE_TOKEN_VALUE` |  The page token is invalid. `INVALID_PAGE_TOKEN = 57;`  
`INVALID_POSTAL_CODE` |  Postal code is not valid. `INVALID_POSTAL_CODE = 12;`  
`INVALID_POSTAL_CODE_VALUE` |  Postal code is not valid. `INVALID_POSTAL_CODE = 12;`  
`INVALID_PRICING_END_DATE` |  Pricing end date is invalid for this license. `INVALID_PRICING_END_DATE = 66;`  
`INVALID_PRICING_END_DATE_VALUE` |  Pricing end date is invalid for this license. `INVALID_PRICING_END_DATE = 66;`  
`INVALID_PROPERTY_TYPE` |  The property type is not supported. `INVALID_PROPERTY_TYPE = 40;`  
`INVALID_PROPERTY_TYPE_VALUE` |  The property type is not supported. `INVALID_PROPERTY_TYPE = 40;`  
`INVALID_REGION_CODE` |  The region code is not valid. `INVALID_REGION_CODE = 104;`  
`INVALID_REGION_CODE_VALUE` |  The region code is not valid. `INVALID_REGION_CODE = 104;`  
`INVALID_REMOVE_AS_OF_TIME` |  The remove as of time must be in the past or present. Future timestamps are not permitted for removing audience members. `INVALID_REMOVE_AS_OF_TIME = 125;`  
`INVALID_REMOVE_AS_OF_TIME_VALUE` |  The remove as of time must be in the past or present. Future timestamps are not permitted for removing audience members. `INVALID_REMOVE_AS_OF_TIME = 125;`  
`INVALID_REQUEST_ID` |  The request ID used to retrieve the status of a request is not valid. Status can only be retrieved for requests that succeed and don't have `validate_only=true`. `INVALID_REQUEST_ID = 48;`  
`INVALID_REQUEST_ID_VALUE` |  The request ID used to retrieve the status of a request is not valid. Status can only be retrieved for requests that succeed and don't have `validate_only=true`. `INVALID_REQUEST_ID = 48;`  
`INVALID_RESOURCE_NAME` |  The resource name is invalid. `INVALID_RESOURCE_NAME = 54;`  
`INVALID_RESOURCE_NAME_VALUE` |  The resource name is invalid. `INVALID_RESOURCE_NAME = 54;`  
`INVALID_SHA256_FORMAT` |  The SHA256 encoded value is malformed. `INVALID_SHA256_FORMAT = 11;`  
`INVALID_SHA256_FORMAT_VALUE` |  The SHA256 encoded value is malformed. `INVALID_SHA256_FORMAT = 11;`  
`INVALID_STREAM_TYPE` |  The stream type is not supported. `INVALID_STREAM_TYPE = 41;`  
`INVALID_STREAM_TYPE_VALUE` |  The stream type is not supported. `INVALID_STREAM_TYPE = 41;`  
`INVALID_SUBCONTINENT_CODE` |  The subcontinent code is not valid. `INVALID_SUBCONTINENT_CODE = 108;`  
`INVALID_SUBCONTINENT_CODE_VALUE` |  The subcontinent code is not valid. `INVALID_SUBCONTINENT_CODE = 108;`  
`INVALID_SUBDIVISION_CODE` |  The subdivision code is not valid. `INVALID_SUBDIVISION_CODE = 107;`  
`INVALID_SUBDIVISION_CODE_VALUE` |  The subdivision code is not valid. `INVALID_SUBDIVISION_CODE = 107;`  
`INVALID_UPDATE_MASK` |  The update mask is invalid. `INVALID_UPDATE_MASK = 56;`  
`INVALID_UPDATE_MASK_VALUE` |  The update mask is invalid. `INVALID_UPDATE_MASK = 56;`  
`INVALID_USER_LIST_ID` |  User list is not valid. `INVALID_USER_LIST_ID = 23;`  
`INVALID_USER_LIST_ID_VALUE` |  User list is not valid. `INVALID_USER_LIST_ID = 23;`  
`INVALID_USER_LIST_TYPE` |  Type of the user list is not applicable for this request. `INVALID_USER_LIST_TYPE = 15;`  
`INVALID_USER_LIST_TYPE_VALUE` |  Type of the user list is not applicable for this request. `INVALID_USER_LIST_TYPE = 15;`  
`LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT` |  Linked account is only supported when the login account is a `DATA_PARTNER` account. `LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT = 42;`  
`LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT_VALUE` |  Linked account is only supported when the login account is a `DATA_PARTNER` account. `LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT = 42;`  
`MAX_COST_NOT_ALLOWED` |  Max cost is only allowed for cost_type MEDIA_SHARE. `MAX_COST_NOT_ALLOWED = 74;`  
`MAX_COST_NOT_ALLOWED_VALUE` |  Max cost is only allowed for cost_type MEDIA_SHARE. `MAX_COST_NOT_ALLOWED = 74;`  
`MEDIA_SHARE_COST_NOT_ALLOWED_FOR_CLIENT_CUSTOMER` |  Client customer type does not support media share cost. `MEDIA_SHARE_COST_NOT_ALLOWED_FOR_CLIENT_CUSTOMER = 70;`  
`MEDIA_SHARE_COST_NOT_ALLOWED_FOR_CLIENT_CUSTOMER_VALUE` |  Client customer type does not support media share cost. `MEDIA_SHARE_COST_NOT_ALLOWED_FOR_CLIENT_CUSTOMER = 70;`  
`MEDIA_SHARE_COST_NOT_ALLOWED_FOR_LICENSE_TYPE` |  License type does not support media share cost. `MEDIA_SHARE_COST_NOT_ALLOWED_FOR_LICENSE_TYPE = 69;`  
`MEDIA_SHARE_COST_NOT_ALLOWED_FOR_LICENSE_TYPE_VALUE` |  License type does not support media share cost. `MEDIA_SHARE_COST_NOT_ALLOWED_FOR_LICENSE_TYPE = 69;`  
`MEDIA_SHARE_COST_NOT_ALLOWED_FOR_NON_COMMERCE_USER_LIST` |  UserList type does not support media share cost. `MEDIA_SHARE_COST_NOT_ALLOWED_FOR_NON_COMMERCE_USER_LIST = 73;`  
`MEDIA_SHARE_COST_NOT_ALLOWED_FOR_NON_COMMERCE_USER_LIST_VALUE` |  UserList type does not support media share cost. `MEDIA_SHARE_COST_NOT_ALLOWED_FOR_NON_COMMERCE_USER_LIST = 73;`  
`MEMBERSHIP_DURATION_TOO_LONG` |  The user list membership duration is too long. `MEMBERSHIP_DURATION_TOO_LONG = 99;`  
`MEMBERSHIP_DURATION_TOO_LONG_VALUE` |  The user list membership duration is too long. `MEMBERSHIP_DURATION_TOO_LONG = 99;`  
`MISMATCHED_ACCOUNT_TYPE` |  Client customer's account type in the request does not match the customer's actual account type. `MISMATCHED_ACCOUNT_TYPE = 68;`  
`MISMATCHED_ACCOUNT_TYPE_VALUE` |  Client customer's account type in the request does not match the customer's actual account type. `MISMATCHED_ACCOUNT_TYPE = 68;`  
`MULTIPLE_DATA_TYPES_NOT_ALLOWED` |  Multiple data types are not allowed to be ingested in a single request. `MULTIPLE_DATA_TYPES_NOT_ALLOWED = 24;`  
`MULTIPLE_DATA_TYPES_NOT_ALLOWED_VALUE` |  Multiple data types are not allowed to be ingested in a single request. `MULTIPLE_DATA_TYPES_NOT_ALLOWED = 24;`  
`MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT` |  An event had 2 or more Google Analytics destinations. `MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT = 49;`  
`MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT_VALUE` |  An event had 2 or more Google Analytics destinations. `MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT = 49;`  
`NOT_ALLOWLISTED` |  The account is not allowlisted for the given feature. `NOT_ALLOWLISTED = 47;`  
`NOT_ALLOWLISTED_VALUE` |  The account is not allowlisted for the given feature. `NOT_ALLOWLISTED = 47;`  
`NOT_FOUND` |  Resource not found. `NOT_FOUND = 4;`  
`NOT_FOUND_VALUE` |  Resource not found. `NOT_FOUND = 4;`  
`NO_IDENTIFIERS_PROVIDED` |  Events data contains no user identifiers or ad identifiers. For Floodlight Event ingestion this error indicates requests contains no ad identifiers. `NO_IDENTIFIERS_PROVIDED = 39;`  
`NO_IDENTIFIERS_PROVIDED_VALUE` |  Events data contains no user identifiers or ad identifiers. For Floodlight Event ingestion this error indicates requests contains no ad identifiers. `NO_IDENTIFIERS_PROVIDED = 39;`  
`OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH` |  The login account must be the same as the operating account for the given use case. `OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH = 43;`  
`OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH_VALUE` |  The login account must be the same as the operating account for the given use case. `OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH = 43;`  
`OWNERSHIP_REQUIRED_FOR_UPDATE` |  Ownership is required to modify the user list. `OWNERSHIP_REQUIRED_FOR_UPDATE = 79;`  
`OWNERSHIP_REQUIRED_FOR_UPDATE_VALUE` |  Ownership is required to modify the user list. `OWNERSHIP_REQUIRED_FOR_UPDATE = 79;`  
`PARTNER_MATCH_FOR_MANAGER_ACCOUNT_DISALLOWED` |  Partner Match user lists cannot be created by manager accounts. `PARTNER_MATCH_FOR_MANAGER_ACCOUNT_DISALLOWED = 88;`  
`PARTNER_MATCH_FOR_MANAGER_ACCOUNT_DISALLOWED_VALUE` |  Partner Match user lists cannot be created by manager accounts. `PARTNER_MATCH_FOR_MANAGER_ACCOUNT_DISALLOWED = 88;`  
`PERMISSION_DENIED` |  The user does not have permission or the resource is not found. `PERMISSION_DENIED = 5;`  
`PERMISSION_DENIED_VALUE` |  The user does not have permission or the resource is not found. `PERMISSION_DENIED = 5;`  
`PRICE_TOO_HIGH` |  Cost too high for this license. `PRICE_TOO_HIGH = 64;`  
`PRICE_TOO_HIGH_VALUE` |  Cost too high for this license. `PRICE_TOO_HIGH = 64;`  
`PRICING_ONLY_ZERO_COST_ALLOWED` |  Non-zero cost not allowed for this client account. `PRICING_ONLY_ZERO_COST_ALLOWED = 63;`  
`PRICING_ONLY_ZERO_COST_ALLOWED_VALUE` |  Non-zero cost not allowed for this client account. `PRICING_ONLY_ZERO_COST_ALLOWED = 63;`  
`REQUEST_TOO_OLD` |  Request status is only available for approximately 50 days after the API receives a request. `REQUEST_TOO_OLD = 126;`  
`REQUEST_TOO_OLD_VALUE` |  Request status is only available for approximately 50 days after the API receives a request. `REQUEST_TOO_OLD = 126;`  
`REQUIRED_FIELD_MISSING` |  Required field is missing. `REQUIRED_FIELD_MISSING = 7;`  
`REQUIRED_FIELD_MISSING_VALUE` |  Required field is missing. `REQUIRED_FIELD_MISSING = 7;`  
`REQUIRED_PREREQUISITE_LINK_MISSING` |  A required prerequisite link (such as a Google Ads link) must exist for the Google Analytics property to perform this operation. `REQUIRED_PREREQUISITE_LINK_MISSING = 124;`  
`REQUIRED_PREREQUISITE_LINK_MISSING_VALUE` |  A required prerequisite link (such as a Google Ads link) must exist for the Google Analytics property to perform this operation. `REQUIRED_PREREQUISITE_LINK_MISSING = 124;`  
`RESERVED_NAME_USED` |  Parameter uses a reserved name. `RESERVED_NAME_USED = 45;`  
`RESERVED_NAME_USED_VALUE` |  Parameter uses a reserved name. `RESERVED_NAME_USED = 45;`  
`RESOURCE_EXHAUSTED` |  Too many requests. `RESOURCE_EXHAUSTED = 3;`  
`RESOURCE_EXHAUSTED_VALUE` |  Too many requests. `RESOURCE_EXHAUSTED = 3;`  
`SENSITIVE_USER_LIST_IMMUTABLE` |  A user list which is privacy sensitive or legal rejected cannot be mutated by external users. `SENSITIVE_USER_LIST_IMMUTABLE = 81;`  
`SENSITIVE_USER_LIST_IMMUTABLE_VALUE` |  A user list which is privacy sensitive or legal rejected cannot be mutated by external users. `SENSITIVE_USER_LIST_IMMUTABLE = 81;`  
`TERMS_AND_CONDITIONS_NOT_SIGNED` |  Required terms and conditions are not accepted. `TERMS_AND_CONDITIONS_NOT_SIGNED = 26;`  
`TERMS_AND_CONDITIONS_NOT_SIGNED_VALUE` |  Required terms and conditions are not accepted. `TERMS_AND_CONDITIONS_NOT_SIGNED = 26;`  
`THIRD_PARTY_USER_DATA_NOT_ALLOWED` |  Third party user data can only be set by data partners. `THIRD_PARTY_USER_DATA_NOT_ALLOWED = 113;`  
`THIRD_PARTY_USER_DATA_NOT_ALLOWED_VALUE` |  Third party user data can only be set by data partners. `THIRD_PARTY_USER_DATA_NOT_ALLOWED = 113;`  
`TOO_FEW_ELEMENTS` |  Too few elements in a list in the request. `TOO_FEW_ELEMENTS = 105;`  
`TOO_FEW_ELEMENTS_VALUE` |  Too few elements in a list in the request. `TOO_FEW_ELEMENTS = 105;`  
`TOO_MANY_AUDIENCE_MEMBERS` |  Maximum number of audience members allowed per request is 10,000. `TOO_MANY_AUDIENCE_MEMBERS = 17;`  
`TOO_MANY_AUDIENCE_MEMBERS_VALUE` |  Maximum number of audience members allowed per request is 10,000. `TOO_MANY_AUDIENCE_MEMBERS = 17;`  
`TOO_MANY_DESTINATIONS` |  Maximum number of destinations allowed per request is 10. `TOO_MANY_DESTINATIONS = 19;`  
`TOO_MANY_DESTINATIONS_VALUE` |  Maximum number of destinations allowed per request is 10. `TOO_MANY_DESTINATIONS = 19;`  
`TOO_MANY_ELEMENTS` |  Too many elements in a list in the request. `TOO_MANY_ELEMENTS = 51;`  
`TOO_MANY_ELEMENTS_VALUE` |  Too many elements in a list in the request. `TOO_MANY_ELEMENTS = 51;`  
`TOO_MANY_EVENTS` |  Maximum number of events allowed per request is 10,000. `TOO_MANY_EVENTS = 32;`  
`TOO_MANY_EVENTS_VALUE` |  Maximum number of events allowed per request is 10,000. `TOO_MANY_EVENTS = 32;`  
`TOO_MANY_USERS` |  Maximum number of users allowed per request is 10,000. `TOO_MANY_USERS = 121;`  
`TOO_MANY_USERS_VALUE` |  Maximum number of users allowed per request is 10,000. `TOO_MANY_USERS = 121;`  
`TOO_MANY_USER_IDENTIFIERS` |  Maximum number of user identifiers allowed per audience member is 10. `TOO_MANY_USER_IDENTIFIERS = 18;`  
`TOO_MANY_USER_IDENTIFIERS_VALUE` |  Maximum number of user identifiers allowed per audience member is 10. `TOO_MANY_USER_IDENTIFIERS = 18;`  
`UNRECOGNIZED` |   
`UNSUPPORTED_ACCOUNT_TYPES_FOR_USER_LIST_TYPE` |  The account types are not supported for the user list type. `UNSUPPORTED_ACCOUNT_TYPES_FOR_USER_LIST_TYPE = 97;`  
`UNSUPPORTED_ACCOUNT_TYPES_FOR_USER_LIST_TYPE_VALUE` |  The account types are not supported for the user list type. `UNSUPPORTED_ACCOUNT_TYPES_FOR_USER_LIST_TYPE = 97;`  
`UNSUPPORTED_ACCOUNT_TYPE_FOR_PARTNER_LINK` |  The account types are not supported for the partner link. `UNSUPPORTED_ACCOUNT_TYPE_FOR_PARTNER_LINK = 98;`  
`UNSUPPORTED_ACCOUNT_TYPE_FOR_PARTNER_LINK_VALUE` |  The account types are not supported for the partner link. `UNSUPPORTED_ACCOUNT_TYPE_FOR_PARTNER_LINK = 98;`  
`UNSUPPORTED_INGESTED_USER_LIST_INFO_CONFIG` |  The ingested user list info config is not supported. `UNSUPPORTED_INGESTED_USER_LIST_INFO_CONFIG = 96;`  
`UNSUPPORTED_INGESTED_USER_LIST_INFO_CONFIG_VALUE` |  The ingested user list info config is not supported. `UNSUPPORTED_INGESTED_USER_LIST_INFO_CONFIG = 96;`  
`UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER` |  Unsupported linked account for data partner authorization. `UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER = 38;`  
`UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER_VALUE` |  Unsupported linked account for data partner authorization. `UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER = 38;`  
`UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER` |  Unsupported operating account for data partner authorization. `UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER = 37;`  
`UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER_VALUE` |  Unsupported operating account for data partner authorization. `UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER = 37;`  
`UNSUPPORTED_PARTNER_AUDIENCE_INFO` |  The `partner_audience_info` field is not supported for the user list type. `UNSUPPORTED_PARTNER_AUDIENCE_INFO = 87;`  
`UNSUPPORTED_PARTNER_AUDIENCE_INFO_VALUE` |  The `partner_audience_info` field is not supported for the user list type. `UNSUPPORTED_PARTNER_AUDIENCE_INFO = 87;`  
`UNSUPPORTED_PARTNER_AUDIENCE_SOURCE` |  The partner audience source is not supported for the user list type. `UNSUPPORTED_PARTNER_AUDIENCE_SOURCE = 85;`  
`UNSUPPORTED_PARTNER_AUDIENCE_SOURCE_VALUE` |  The partner audience source is not supported for the user list type. `UNSUPPORTED_PARTNER_AUDIENCE_SOURCE = 85;`  
`UNSUPPORTED_USER_LIST_UPLOAD_KEY_TYPES` |  The user list upload key types are not supported. `UNSUPPORTED_USER_LIST_UPLOAD_KEY_TYPES = 95;`  
`UNSUPPORTED_USER_LIST_UPLOAD_KEY_TYPES_VALUE` |  The user list upload key types are not supported. `UNSUPPORTED_USER_LIST_UPLOAD_KEY_TYPES = 95;`  
`USER_LIST_MUTATION_NOT_SUPPORTED` |  The user list type is read-only and does not support mutation. `USER_LIST_MUTATION_NOT_SUPPORTED = 80;`  
`USER_LIST_MUTATION_NOT_SUPPORTED_VALUE` |  The user list type is read-only and does not support mutation. `USER_LIST_MUTATION_NOT_SUPPORTED = 80;`  
`USER_LIST_NAME_RESERVED` |  The user list name is reserved for system lists. `USER_LIST_NAME_RESERVED = 83;`  
`USER_LIST_NAME_RESERVED_VALUE` |  The user list name is reserved for system lists. `USER_LIST_NAME_RESERVED = 83;`  
`USER_LIST_TYPE_NOT_SUPPORTED_FOR_ACCOUNT` |  This user list type is not supported for this account. `USER_LIST_TYPE_NOT_SUPPORTED_FOR_ACCOUNT = 92;`  
`USER_LIST_TYPE_NOT_SUPPORTED_FOR_ACCOUNT_VALUE` |  This user list type is not supported for this account. `USER_LIST_TYPE_NOT_SUPPORTED_FOR_ACCOUNT = 92;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.ErrorReason#com_google_ads_datamanager_v1_ErrorReason_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
