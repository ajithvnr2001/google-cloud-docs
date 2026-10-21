---
url: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/mail/
title: Package google.golang.org/appengine/v2/mail (v2.0.6) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:50.036092+00:00
---

# Package google.golang.org/appengine/v2/mail (v2.0.6)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/go/reference/services/bundled/latest/mail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package google.golang.org/appengine/v2/mail (v2.0.6) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To get more information about this package, such as access to older versions, view [this package on pkg.go.dev](https://pkg.go.dev/google.golang.org/appengine/v2/mail). 

Package mail provides the means of sending email from an App Engine application. 

Example:
    
    
    msg := &mail.Message{
        Sender:  "romeo@montague.com",
        To:      []string{"Juliet <juliet@capulet.org>"},
        Subject: "See you tonight",
        Body:    "Don't forget our plans. Hark, 'til later.",
    }
    if err := mail.Send(c, msg); err != nil {
        log.Errorf(c, "Alas, my user, the email failed to sendeth: %v", err)
    }

## Functions 

### func Send 
    
    
    func Send(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), msg *Message) [error](https://pkg.go.dev/builtin#error)

Send sends an email message.

### func SendToAdmins 
    
    
    func SendToAdmins(c [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), msg *Message) [error](https://pkg.go.dev/builtin#error)

SendToAdmins sends an email message to the application's administrators.

## Attachment
    
    
    type Attachment struct {
    	// Name must be set to a valid file name.
    	Name      [string](https://pkg.go.dev/builtin#string)
    	Data      [][byte](https://pkg.go.dev/builtin#byte)
    	ContentID [string](https://pkg.go.dev/builtin#string)
    }

An Attachment represents an email attachment.

## Message
    
    
    type Message struct {
    	// Sender must be set, and must be either an application admin
    	// or the currently signed-in user.
    	Sender  [string](https://pkg.go.dev/builtin#string)
    	ReplyTo [string](https://pkg.go.dev/builtin#string) // may be empty
    
    	// At least one of these slices must have a non-zero length,
    	// except when calling SendToAdmins.
    	To, Cc, Bcc [][string](https://pkg.go.dev/builtin#string)
    
    	Subject [string](https://pkg.go.dev/builtin#string)
    
    	// At least one of Body or HTMLBody must be non-empty.
    	Body     [string](https://pkg.go.dev/builtin#string)
    	HTMLBody [string](https://pkg.go.dev/builtin#string)
    
    	Attachments []Attachment
    
    	// Extra mail headers.
    	// See https://cloud.google.com/appengine/docs/standard/go/mail/
    	// for permissible headers.
    	Headers [mail](https://pkg.go.dev/net/mail).[Header](https://pkg.go.dev/net/mail#Header)
    }

A Message represents an email message. Addresses may be of any form permitted by RFC 822.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
