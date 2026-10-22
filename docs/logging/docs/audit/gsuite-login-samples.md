---
url: https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples/
title: Google Workspace login audit samples \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:36.474329+00:00
---

# Google Workspace login audit samples  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Google Workspace login audit samples Stay organized with collections  Save and categorize content based on your preferences. 

This document provides samples of [audit logs sent to Google Cloud](https://docs.cloud.google.com/logging/docs/audit/configure-gsuite-audit-logs) by Google Workspace Login Audit. These logs are crucial for observability, monitoring security, authentication, and other user activity events. The samples cover various scenarios, including changes to 2-step verification settings, which can trigger notifications.

For more information about the events and parameters for various types of Login Audit activity events, see the [Login Audit Activity Events](https://developers.google.com/admin-sdk/reports/v1/appendix/activity/login) reference.

## Available Login Audit logs

The following table lists the audit logs produced by Login Audit and their corresponding `AuditLog.method_name`. For more information, see [Audit log format](https://docs.cloud.google.com/logging/docs/audit/gsuite-audit-logging#format):

Description | Event name | `AuditLog.method_name`  
---|---|---  
[Event type: 2-step verification enrollment changed](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-1)  
2-step verification disable | `2sv_disable` | `google.login.LoginService.2svDisable`  
2-step verification enroll | `2sv_enroll` | `google.login.LoginService.2svEnroll`  
[Event type: Account password changed](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-2)  
Account password change | `password_edit` | `google.login.LoginService.passwordEdit`  
[Event type: Account recovery information changed](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-3)  
Account recovery email change | `recovery_email_edit` | `google.login.LoginService.recoveryEmailEdit`  
Account recovery phone change | `recovery_phone_edit` | `google.login.LoginService.recoveryPhoneEdit`  
Account recovery secret question/answer change | `recovery_secret_qa_edit` | `google.login.LoginService.recoverySecretQaEdit`  
[Event type: Account warning](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-4)  
Leaked password | `account_disabled_password_leak` | `google.login.LoginService.accountDisabledPasswordLeak`  
Risky, sensitive action allowed | `risky_sensitive_action_allowed` | `google.login.LoginService.riskySensitiveActionAllowed`  
Risky, sensitive action_blocked | `risky_sensitive_action_blocked` | `google.login.LoginService.riskySensitiveActionBlocked`  
Suspicious login blocked | `suspicious_login` | `google.login.LoginService.suspiciousLogin`  
Suspicious login from less secure app blocked | `suspicious_login_less_secure_app` | `google.login.LoginService.suspiciousLoginLessSecureApp`  
Suspicious programmatic login blocked | `suspicious_programmatic_login` | `google.login.LoginService.suspiciousProgrammaticLogin`  
User suspended | `account_disabled_generic` | `google.login.LoginService.accountDisabledGeneric`  
User suspended (spam through relay) | `account_disabled_spamming_through_relay` | `google.login.LoginService.accountDisabledSpammingThroughRelay`  
User suspended (spam) | `account_disabled_spamming` | `google.login.LoginService.accountDisabledSpamming`  
User suspended (suspicious activity) | `account_disabled_hijacked` | `google.login.LoginService.accountDisabledHijacked`  
[Event type: Advanced Protection enrollment changed](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-5)  
Advanced Protection enroll | `titanium_enroll` | `google.login.LoginService.titaniumEnroll`  
Advanced Protection unenroll | `titanium_unenroll` | `google.login.LoginService.titaniumUnenroll`  
[Event type: Attack warning](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-6)  
Government-backed attack | `gov_attack_warning` | `google.login.LoginService.govAttackWarning`  
[Event type: Email forwarding settings changed](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-7)  
Out of domain email forwarding enabled | `email_forwarding_out_of_domain` | `google.login.LoginService.emailForwardingOutOfDomain`  
[Event type: Login](https://docs.cloud.google.com/logging/docs/audit/gsuite-login-samples?reload=true#expandable-8)  
Failed login | `login_failure` | `google.login.LoginService.loginFailure`  
Login challenge | `login_challenge` | `google.login.LoginService.loginChallenge`  
Login verification | `login_verification` | `google.login.LoginService.loginVerification`  
Logout | `logout` | `google.login.LoginService.logout`  
Successful login | `login_success` | `google.login.LoginService.loginSuccess`  
  
## Audit log samples for activity events

The following are samples of audit logs for Login Audit according to event type and event name:

### Event type: 2-step verification enrollment changed

#### Event name: `2sv_disable`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.2svDisable",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "uniqQualifier": "-7789616625639281959",
            "timeUsec": "1632459962686000"
          },
          "event": [
            {
              "status": {
                "success": true
              },
              "parameter": [
                {
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL",
                  "value": "INfDlrzP9IH8_QE",
                  "name": "dusi"
                }
              ],
              "eventName": "2sv_disable",
              "eventType": "2sv_change"
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-tn3jrd3lko",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.2svDisable"
        }
      },
      "timestamp": "2021-09-24T05:06:02.686Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T05:06:03.845372592Z"
    }

#### Event name: `2sv_enroll`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.2svEnroll",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "uniqQualifier": "1624031130844323135",
            "timeUsec": "1632458745769000"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventType": "2sv_change",
              "status": {
                "success": true
              },
              "eventName": "2sv_enroll",
              "parameter": [
                {
                  "value": "INfDlrzP9IH8_QE",
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL",
                  "name": "dusi"
                }
              ]
            }
          ]
        }
      },
      "insertId": "g3k8gid3b3p",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.2svEnroll",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-09-24T04:45:45.769Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T04:45:46.331843829Z"
    }

### Event type: Account password changed

#### Event name: `password_edit`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.passwordEdit",
        "resourceName": "organizations/123",
        "metadata": {
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventName": "password_edit",
              "status": {
                "success": true
              },
              "parameter": [
                {
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL",
                  "value": "INfDlrzP9IH8_QE",
                  "name": "dusi"
                }
              ],
              "eventType": "password_change"
            }
          ],
          "activityId": {
            "uniqQualifier": "8894052787391296929",
            "timeUsec": "1632803013900566"
          }
        }
      },
      "insertId": "-u8coc0d6n78",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.passwordEdit"
        }
      },
      "timestamp": "2021-09-28T04:23:33.900566Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-28T04:23:37.724654918Z"
    }

### Event type: Account recovery info changed

#### Event name: `recovery_email_edit`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.recoveryEmailEdit",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1632802942940979",
            "uniqQualifier": "-7373127890859496609"
          },
          "event": [
            {
              "eventType": "recovery_info_change",
              "eventName": "recovery_email_edit",
              "parameter": [
                {
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING",
                  "value": "INfDlrzP9IH8_QE",
                  "name": "dusi"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-nkwfupd26zt",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.recoveryEmailEdit"
        }
      },
      "timestamp": "2021-09-28T04:22:22.940979Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-28T04:22:26.523242112Z"
    }

#### Event name: `recovery_phone_edit`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.recoveryPhoneEdit",
        "resourceName": "organizations/123",
        "metadata": {
          "event": [
            {
              "status": {
                "success": true
              },
              "eventType": "recovery_info_change",
              "eventName": "recovery_phone_edit",
              "parameter": [
                {
                  "label": "LABEL_OPTIONAL",
                  "value": "INfDlrzP9IH8_QE",
                  "type": "TYPE_STRING",
                  "name": "dusi"
                }
              ]
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "activityId": {
            "timeUsec": "1632804439611095",
            "uniqQualifier": "1470137036135837564"
          }
        }
      },
      "insertId": "-1xtrgbd2vl2",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.recoveryPhoneEdit"
        }
      },
      "timestamp": "2021-09-28T04:47:19.611095Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-28T04:47:25.741574446Z"

#### Event name: `recovery_secret_qa_edit`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.recoverySecretQaEdit",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "uniqQualifier": "8328506129139272243",
            "timeUsec": "1632804455273424"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventName": "recovery_secret_qa_edit",
              "eventType": "recovery_info_change",
              "status": {
                "success": true
              },
              "parameter": [
                {
                  "type": "TYPE_STRING",
                  "value": "INfDlrzP9IH8_QE",
                  "name": "dusi",
                  "label": "LABEL_OPTIONAL"
                }
              ]
            }
          ]
        }
      },
      "insertId": "vn31slcpmy",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.recoverySecretQaEdit",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-09-28T04:47:35.273424Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-28T04:47:37.650432219Z"

### Event type: Account warning

#### Event name: `account_disabled_password_leak`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.accountDisabledPasswordLeak",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1619808083475000",
            "uniqQualifier": "6286848759980589624"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "account_disabled_password_leak",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-xkklkzcxkl",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.accountDisabledPasswordLeak",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-04-30T18:41:23.475Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-04-30T18:41:24.650965796Z"
    }

#### Event name: `suspicious_login`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.suspiciousLogin",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1620095181000000",
            "uniqQualifier": "-2034771694824799453"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "suspicious_login",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-778d70d2n5b",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.suspiciousLogin"
        }
      },
      "timestamp": "2021-05-04T02:26:21Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-05-04T02:56:23.806722355Z"
    }

#### Event name: `suspicious_login_less_secure_app`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.suspiciousLoginLessSecureApp",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1620095181000000",
            "uniqQualifier": "-2034771694824799453"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "suspicious_login_less_secure_app",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-778d70d2n5b",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.suspiciousLoginLessSecureApp"
        }
      },
      "timestamp": "2021-05-04T02:26:21Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-05-04T02:56:23.806722355Z"
    }

#### Event name: `suspicious_programmatic_login`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.suspiciousProgrammaticLogin",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1620095181000000",
            "uniqQualifier": "-2034771694824799453"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "suspicious_programmatic_login",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-778d70d2n5b",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.suspiciousProgrammaticLogin"
        }
      },
      "timestamp": "2021-05-04T02:26:21Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-05-04T02:56:23.806722355Z"
    }

#### Event name: `account_disabled_generic`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.accountDisabledGeneric",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1619825589352000",
            "uniqQualifier": "-3303614929287073633"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "account_disabled_generic",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "nlgrf8d6ygj",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.accountDisabledGeneric",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-04-30T23:33:09.352Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-04-30T23:33:10.673412983Z"
    }

#### Event name: `account_disabled_spamming_through_relay`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.accountDisabledSpammingThroughRelay",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1619808083475000",
            "uniqQualifier": "6286848759980589624"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "account_disabled_spamming_through_relay",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-xkklkzcxkl",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.accountDisabledSpammingThroughRelay",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-04-30T18:41:23.475Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-04-30T18:41:24.650965796Z"
    }

#### Event name: `account_disabled_spamming`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.accountDisabledSpamming",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1619808083475000",
            "uniqQualifier": "6286848759980589624"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "account_disabled_spamming",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-xkklkzcxkl",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.accountDisabledSpamming",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-04-30T18:41:23.475Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-04-30T18:41:24.650965796Z"
    }

#### Event name: `account_disabled_hijacked`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {},
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff"
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.accountDisabledHijacked",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1619825589352000",
            "uniqQualifier": "-3303614929287073633"
          },
          "event": [
            {
              "eventType": "account_warning",
              "eventName": "account_disabled_hijacked",
              "parameter": [
                {
                  "name": "affected_email_address",
                  "value": "test-user@example.com",
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING"
                }
              ],
              "status": {
                "success": true
              }
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "nlgrf8d6ygj",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.accountDisabledHijacked",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-04-30T23:33:09.352Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-04-30T23:33:10.673412983Z"
    }

### Event type: Advanced Protection enrollment changed

#### Event name: `titanium_enroll`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.titaniumEnroll",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "uniqQualifier": "4206430548119220064",
            "timeUsec": "1632843484846000"
          },
          "event": [
            {
              "eventName": "titanium_enroll",
              "status": {
                "success": true
              },
              "parameter": [
                {
                  "label": "LABEL_OPTIONAL",
                  "value": "INfDlrzP9IH8_QE",
                  "type": "TYPE_STRING",
                  "name": "dusi"
                }
              ],
              "eventType": "titanium_change"
            }
          ],
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-bxbn5bd167i",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.titaniumEnroll"
        }
      },
      "timestamp": "2021-09-28T15:38:04.846Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-28T15:38:05.969683854Z"
    }

#### Event name: `titanium_unenroll`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.titaniumUnenroll",
        "resourceName": "organizations/123",
        "metadata": {
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventType": "titanium_change",
              "status": {
                "success": true
              },
              "eventName": "titanium_unenroll",
              "parameter": [
                {
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL",
                  "value": "INfDlrzP9IH8_QE",
                  "name": "dusi"
                }
              ]
            }
          ],
          "activityId": {
            "timeUsec": "1632843914653434",
            "uniqQualifier": "-6706492269209711994"
          }
        }
      },
      "insertId": "-vw60qad1861",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.titaniumUnenroll"
        }
      },
      "timestamp": "2021-09-28T15:45:14.653434Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-28T15:45:15.862755277Z"
    }

### Event type: Attack warning

#### Event name: `gov_attack_warning`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.govAttackWarning",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "timeUsec": "1619825837106000",
            "uniqQualifier": "7230131091737932677"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventName": "gov_attack_warning",
              "eventType": "attack_warning",
              "status": {
                "success": true
              }
            }
          ]
        }
      },
      "insertId": "bxuophd1vlw",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.govAttackWarning"
        }
      },
      "timestamp": "2021-04-30T23:37:17.106Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-04-30T23:37:18.488559815Z"
    }

### Event type: Email forwarding settings changed

#### Event name: `email_forwarding_out_of_domain`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.emailForwardingOutOfDomain",
        "resourceName": "organizations/123",
        "metadata": {
          "activityId": {
            "uniqQualifier": "-5683698025624301037",
            "timeUsec": "1632501152256000"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventName": "email_forwarding_out_of_domain",
              "status": {
                "success": true
              },
              "parameter": [
                {
                  "name": "dusi",
                  "type": "TYPE_STRING",
                  "value": "INfDlrzP9IH8_QE",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL",
                  "value": "test-user@google.com",
                  "name": "email_forwarding_destination_address"
                }
              ],
              "eventType": "email_forwarding_change"
            }
          ]
        }
      },
      "insertId": "rrcp9gd3y2f",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.emailForwardingOutOfDomain",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-09-24T16:32:32.256Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T16:32:33.319260836Z"
    }

### Event type: Login

#### Event name: `login_failure`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.loginFailure",
        "resourceName": "organizations/123",
        "metadata": {
          "event": [
            {
              "eventName": "login_failure",
              "eventType": "login",
              "parameter": [
                {
                  "value": "google_password",
                  "type": "TYPE_STRING",
                  "name": "login_type",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "name": "login_challenge_method",
                  "type": "TYPE_STRING",
                  "label": "LABEL_REPEATED",
                  "multiStrValue": [
                    "password",
                    "idv_preregistered_phone",
                    "idv_preregistered_phone"
                  ]
                },
                {
                  "label": "LABEL_OPTIONAL",
                  "name": "dusi",
                  "type": "TYPE_STRING",
                  "value": "IOWJlfPwgvrTfg"
                }
              ]
            }
          ],
          "activityId": {
            "uniqQualifier": "358068855354",
            "timeUsec": "1632500217183212"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "-nahbepd4l1x",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.loginFailure",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-09-24T16:16:57.183212Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T17:51:25.034361197Z"
    }

#### Event name: `login_challenge`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "2001:db8:ffff:ffff:ffff:ffff:ffff:ffff",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.loginChallenge",
        "resourceName": "organizations/123",
        "metadata": {
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventName": "login_challenge",
              "parameter": [
                {
                  "name": "login_type",
                  "value": "google_password",
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "type": "TYPE_STRING",
                  "label": "LABEL_REPEATED",
                  "name": "login_challenge_method",
                  "multiStrValue": [
                    "idv_preregistered_phone"
                  ]
                },
                {
                  "label": "LABEL_OPTIONAL",
                  "type": "TYPE_STRING",
                  "value": "incorrect_answer_entered",
                  "name": "login_challenge_status"
                },
                {
                  "type": "TYPE_STRING",
                  "name": "dusi",
                  "label": "LABEL_OPTIONAL",
                  "value": "IOWJlfPwgvrTfg"
                }
              ],
              "eventType": "login"
            }
          ],
          "activityId": {
            "timeUsec": "1632500217183211",
            "uniqQualifier": "358068855354"
          }
        }
      },
      "insertId": "-nahbepd4l2j",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.loginChallenge"
        }
      },
      "timestamp": "2021-09-24T16:16:57.183211Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T17:51:28.041126044Z"

#### Event name: `login_verification`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.loginVerification",
        "resourceName": "organizations/123",
        "metadata": {
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "event": [
            {
              "eventName": "login_verification",
              "parameter": [
                {
                  "name": "login_type",
                  "type": "TYPE_STRING",
                  "value": "google_password",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "name": "login_challenge_method",
                  "multiStrValue": [
                    "idv_preregistered_phone"
                  ],
                  "label": "LABEL_REPEATED",
                  "type": "TYPE_STRING"
                },
                {
                  "value": "passed",
                  "name": "login_challenge_status",
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "value": "INfDlrzP9IH8_QE",
                  "label": "LABEL_OPTIONAL",
                  "name": "dusi",
                  "type": "TYPE_STRING"
                },
                {
                  "label": "LABEL_OPTIONAL",
                  "boolValue": true,
                  "type": "TYPE_BOOL",
                  "name": "is_second_factor"
                }
              ],
              "eventType": "login"
            }
          ],
          "activityId": {
            "uniqQualifier": "358068855354",
            "timeUsec": "1632459936762000"
          }
        }
      },
      "insertId": "ivb9z4d41rh",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "method": "google.login.LoginService.loginVerification",
          "service": "login.googleapis.com"
        }
      },
      "timestamp": "2021-09-24T05:05:36.762Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T06:39:22.386813664Z"
    }

#### Event name: `logout`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.logout",
        "resourceName": "organizations/123",
        "metadata": {
          "event": [
            {
              "eventName": "logout",
              "eventType": "login",
              "parameter": [
                {
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL",
                  "name": "login_type",
                  "value": "google_password"
                },
                {
                  "type": "TYPE_STRING",
                  "name": "dusi",
                  "label": "LABEL_OPTIONAL",
                  "value": "INfDlrzP9IH8_QE"
                }
              ]
            }
          ],
          "activityId": {
            "uniqQualifier": "358068855354",
            "timeUsec": "1632459903014598"
          },
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto"
        }
      },
      "insertId": "v37ytid14th",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.logout"
        }
      },
      "timestamp": "2021-09-24T05:05:03.014598Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T06:39:22.229734504Z"
    }

#### Event name: `login_success`
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "test-user@example.com"
        },
        "requestMetadata": {
          "callerIp": "203.0.113.255",
          "requestAttributes": {},
          "destinationAttributes": {}
        },
        "serviceName": "login.googleapis.com",
        "methodName": "google.login.LoginService.loginSuccess",
        "resourceName": "organizations/123",
        "metadata": {
          "@type": "type.googleapis.com/ccc_hosted_reporting.ActivityProto",
          "activityId": {
            "timeUsec": "1632458429811809",
            "uniqQualifier": "358068855354"
          },
          "event": [
            {
              "parameter": [
                {
                  "type": "TYPE_STRING",
                  "value": "google_password",
                  "name": "login_type",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "name": "login_challenge_method",
                  "label": "LABEL_REPEATED",
                  "type": "TYPE_STRING",
                  "multiStrValue": [
                    "password"
                  ]
                },
                {
                  "type": "TYPE_BOOL",
                  "boolValue": false,
                  "name": "is_suspicious",
                  "label": "LABEL_OPTIONAL"
                },
                {
                  "value": "INfDlrzP9IH8_QE",
                  "name": "dusi",
                  "type": "TYPE_STRING",
                  "label": "LABEL_OPTIONAL"
                }
              ],
              "eventType": "login",
              "eventName": "login_success"
            }
          ]
        }
      },
      "insertId": "ci1svzd3hfk",
      "resource": {
        "type": "audited_resource",
        "labels": {
          "service": "login.googleapis.com",
          "method": "google.login.LoginService.loginSuccess"
        }
      },
      "timestamp": "2021-09-24T04:40:29.811809Z",
      "severity": "NOTICE",
      "logName": "organizations/123/logs/cloudaudit.googleapis.com%2Fdata_access",
      "receiveTimestamp": "2021-09-24T05:43:20.474338130Z"
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
