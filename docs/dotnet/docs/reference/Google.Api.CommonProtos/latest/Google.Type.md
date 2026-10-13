---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type
title: Namespace Google.Type (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:10.474319+00:00
---

# Namespace Google.Type (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Namespace Google.Type (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.15.0/Google.Type)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.10.0/Google.Type)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/2.2.0/Google.Type)



## Classes 

### [CalendarPeriodReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.CalendarPeriodReflection)

Holder for reflection information generated from google/type/calendar_period.proto

### [Color](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Color)

Represents a color in the RGBA color space. This representation is designed for simplicity of conversion to/from color representations in various languages over compactness. For example, the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a little work, it can be easily formatted into a CSS `rgba()` string in JavaScript.

This reference page doesn't carry information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space.

When color equality needs to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green, blue, and alpha values each differ by at most 1e-5.

Example (Java):
    
    
     import com.google.type.Color;
    
     // ...
     public static java.awt.Color fromProto(Color protocolor) {
       float alpha = protocolor.hasAlpha()
           ? protocolor.getAlpha().getValue()
           : 1.0;
    
       return new java.awt.Color(
           protocolor.getRed(),
           protocolor.getGreen(),
           protocolor.getBlue(),
           alpha);
     }
    
     public static Color toProto(java.awt.Color color) {
       float red = (float) color.getRed();
       float green = (float) color.getGreen();
       float blue = (float) color.getBlue();
       float denominator = 255.0;
       Color.Builder resultBuilder =
           Color
               .newBuilder()
               .setRed(red / denominator)
               .setGreen(green / denominator)
               .setBlue(blue / denominator);
       int alpha = color.getAlpha();
       if (alpha != 255) {
         result.setAlpha(
             FloatValue
                 .newBuilder()
                 .setValue(((float) alpha) / denominator)
                 .build());
       }
       return resultBuilder.build();
     }
     // ...
    

Example (iOS / Obj-C):
    
    
     // ...
     static UIColor* fromProto(Color* protocolor) {
        float red = [protocolor red];
        float green = [protocolor green];
        float blue = [protocolor blue];
        FloatValue* alpha_wrapper = [protocolor alpha];
        float alpha = 1.0;
        if (alpha_wrapper != nil) {
          alpha = [alpha_wrapper value];
        }
        return [UIColor colorWithRed:red green:green blue:blue alpha:alpha];
     }
    
     static Color* toProto(UIColor* color) {
         CGFloat red, green, blue, alpha;
         if (![color getRed:&red green:&green blue:&blue alpha:&alpha]) {
           return nil;
         }
         Color* result = [[Color alloc] init];
         [result setRed:red];
         [result setGreen:green];
         [result setBlue:blue];
         if (alpha <= 0.9999) {
           [result setAlpha:floatWrapperWithValue(alpha)];
         }
         [result autorelease];
         return result;
    }
    // ...
    

Example (JavaScript):
    
    
    // ...
    
    var protoToCssColor = function(rgb_color) {
       var redFrac = rgb_color.red || 0.0;
       var greenFrac = rgb_color.green || 0.0;
       var blueFrac = rgb_color.blue || 0.0;
       var red = Math.floor(redFrac * 255);
       var green = Math.floor(greenFrac * 255);
       var blue = Math.floor(blueFrac * 255);
    
       if (!('alpha' in rgb_color)) {
          return rgbToCssColor(red, green, blue);
       }
    
       var alphaFrac = rgb_color.alpha.value || 0.0;
       var rgbParams = [red, green, blue].join(',');
       return ['rgba(', rgbParams, ',', alphaFrac, ')'].join('');
    };
    
    var rgbToCssColor = function(red, green, blue) {
      var rgbNumber = new Number((red << 16) | (green << 8) | blue);
      var hexString = rgbNumber.toString(16);
      var missingZeros = 6 - hexString.length;
      var resultBuilder = ['#'];
      for (var i = 0; i < missingZeros; i++) {
         resultBuilder.push('0');
      }
      resultBuilder.push(hexString);
      return resultBuilder.join('');
    };
    
    // ...
    

### [ColorReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.ColorReflection)

Holder for reflection information generated from google/type/color.proto

### [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date)

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values
  * A month and day value, with a zero year, such as an anniversary
  * A year on its own, with zero month and day values
  * A year and month value, with a zero day, such as a credit card expiration date



Related types are [google.type.TimeOfDay][google.type.TimeOfDay] and `google.protobuf.Timestamp`.

### [DateExtensions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DateExtensions)

Extension methods built for [Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date).

### [DateReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DateReflection)

Holder for reflection information generated from google/type/date.proto

### [DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DateTime)

Represents civil time (or occasionally physical time).

This type can represent a civil time in one of a few possible ways:

  * When utc_offset is set and time_zone is unset: a civil time on a calendar day with a particular offset from UTC.
  * When time_zone is set and utc_offset is unset: a civil time on a calendar day in a particular time zone.
  * When neither time_zone nor utc_offset is set: a civil time on a calendar day in local time.



The date is relative to the Proleptic Gregorian Calendar.

If year is 0, the DateTime is considered not to have a specific year. month and day must have valid, non-zero values.

This type may also be used to represent a physical time if all the date and time fields are set and either case of the `time_offset` oneof is set. Consider using `Timestamp` message for physical time instead. If your use case also would like to store the user's timezone, that can be done in another field.

This type is more flexible than some applications may want. Make sure to document and validate your application's limitations.

### [DatetimeReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DatetimeReflection)

Holder for reflection information generated from google/type/datetime.proto

### [DayofweekReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DayofweekReflection)

Holder for reflection information generated from google/type/dayofweek.proto

### [Decimal](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Decimal)

A representation of a decimal value, such as 2.5. Clients may convert values into language-native decimal formats, such as Java's [BigDecimal][] or Python's [decimal.Decimal](https://docs.python.org/3/library/decimal.html).

[BigDecimal]: <https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/math/BigDecimal.html>

### [DecimalReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DecimalReflection)

Holder for reflection information generated from google/type/decimal.proto

### [Expr](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Expr)

Represents a textual expression in the Common Expression Language (CEL) syntax. CEL is a C-like expression language. The syntax and semantics of CEL are documented at <https://github.com/google/cel-spec>.

Example (Comparison):
    
    
    title: "Summary size limit"
    description: "Determines if a summary is less than 100 chars"
    expression: "document.summary.size() < 100"
    

Example (Equality):
    
    
    title: "Requestor is owner"
    description: "Determines if requestor is the document owner"
    expression: "document.owner == request.auth.claims.email"
    

Example (Logic):
    
    
    title: "Public documents"
    description: "Determine whether the document should be publicly visible"
    expression: "document.type != 'private' && document.type != 'internal'"
    

Example (Data Manipulation):
    
    
    title: "Notification string"
    description: "Create a notification string with a timestamp."
    expression: "'New message received at ' + string(document.create_time)"
    

The exact variables and functions that may be referenced within an expression are determined by the service that evaluates it. See the service documentation for additional information.

### [ExprReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.ExprReflection)

Holder for reflection information generated from google/type/expr.proto

### [Fraction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Fraction)

Represents a fraction in terms of a numerator divided by a denominator.

### [FractionReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.FractionReflection)

Holder for reflection information generated from google/type/fraction.proto

### [Interval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Interval)

Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).

The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.

### [IntervalReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.IntervalReflection)

Holder for reflection information generated from google/type/interval.proto

### [LatLng](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.LatLng)

An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this must conform to the <a href="[http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf">WGS84](http://www.unoosa.org/pdf/icg/2012/template/WGS_84.pdf">WGS84) standard</a>. Values must be within normalized ranges.

### [LatlngReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.LatlngReflection)

Holder for reflection information generated from google/type/latlng.proto

### [LocalizedText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.LocalizedText)

Localized variant of a text in a particular language.

### [LocalizedTextReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.LocalizedTextReflection)

Holder for reflection information generated from google/type/localized_text.proto

### [Money](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Money)

Represents an amount of money with its currency type.

### [MoneyReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.MoneyReflection)

Holder for reflection information generated from google/type/money.proto

### [MonthReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.MonthReflection)

Holder for reflection information generated from google/type/month.proto

### [PhoneNumber](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber)

An object representing a phone number, suitable as an API wire format.

This representation:

  * should not be used for locale-specific formatting of a phone number, such as "+1 (650) 253-0000 ext. 123"

  * is not designed for efficient storage

  * may not be suitable for dialing - specialized libraries (see references) should be used to parse the number for that purpose



To do something meaningful with this number, such as format it for various use-cases, convert it to an `i18n.phonenumbers.PhoneNumber` object first.

For instance, in Java this would be:

com.google.type.PhoneNumber wireProto = com.google.type.PhoneNumber.newBuilder().build(); com.google.i18n.phonenumbers.Phonenumber.PhoneNumber phoneNumber = PhoneNumberUtil.getInstance().parse(wireProto.getE164Number(), "ZZ"); if (!wireProto.getExtension().isEmpty()) { phoneNumber.setExtension(wireProto.getExtension()); }

Reference(s):

  * <https://github.com/google/libphonenumber>



### [PhoneNumber.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber.Types)

Container for nested types declared in the PhoneNumber message type.

### [PhoneNumber.Types.ShortCode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber.Types.ShortCode)

An object representing a short code, which is a phone number that is typically much shorter than regular phone numbers and can be used to address messages in MMS and SMS systems, as well as for abbreviated dialing (e.g. "Text 611 to see how many minutes you have remaining on your plan.").

Short codes are restricted to a region and are not internationally dialable, which means the same short code can exist in different regions, with different usage and pricing, even if those regions share the same country calling code (e.g. US and CA).

### [PhoneNumberReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumberReflection)

Holder for reflection information generated from google/type/phone_number.proto

### [PostalAddress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PostalAddress)

Represents a postal address, e.g. for postal delivery or payments addresses. Given a postal address, a postal service can deliver items to a premise, P.O. Box or similar. It is not intended to model geographical locations (roads, towns, mountains).

In typical usage an address would be created via user input or from importing existing data, depending on the type of process.

Advice on address input / editing:

  * Use an i18n-ready address widget such as <https://github.com/google/libaddressinput>)
    * Users should not be presented with UI elements for input or editing of fields outside countries where that field is used.



For more guidance on how to use this schema, please see: <https://support.google.com/business/answer/6397478>

### [PostalAddressReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PostalAddressReflection)

Holder for reflection information generated from google/type/postal_address.proto

### [Quaternion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Quaternion)

A quaternion is defined as the quotient of two directed lines in a three-dimensional space or equivalently as the quotient of two Euclidean vectors (<https://en.wikipedia.org/wiki/Quaternion>).

Quaternions are often used in calculations involving three-dimensional rotations (<https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>), as they provide greater mathematical robustness by avoiding the gimbal lock problems that can be encountered when using Euler angles (<https://en.wikipedia.org/wiki/Gimbal_lock>).

Quaternions are generally represented in this form:
    
    
    w + xi + yj + zk
    

where x, y, z, and w are real numbers, and i, j, and k are three imaginary numbers.

Our naming choice `(x, y, z, w)` comes from the desire to avoid confusion for those interested in the geometric properties of the quaternion in the 3D Cartesian space. Other texts often use alternative names or subscripts, such as `(a, b, c, d)`, `(1, i, j, k)`, or `(0, 1, 2, 3)`, which are perhaps better suited for mathematical interpretations.

To avoid any confusion, as well as to maintain compatibility with a large number of software libraries, the quaternions represented using the protocol buffer below _must_ follow the Hamilton convention, which defines `ij = k` (i.e. a right-handed algebra), and therefore:
    
    
    i^2 = j^2 = k^2 = ijk = −1
    ij = −ji = k
    jk = −kj = i
    ki = −ik = j
    

Please DO NOT use this to represent quaternions that follow the JPL convention, or any of the other quaternion flavors out there.

Definitions:

  * Quaternion norm (or magnitude): `sqrt(x^2 + y^2 + z^2 + w^2)`.
  * Unit (or normalized) quaternion: a quaternion whose norm is 1.
  * Pure quaternion: a quaternion whose scalar component (`w`) is 0.
  * Rotation quaternion: a unit quaternion used to represent rotation.
  * Orientation quaternion: a unit quaternion used to represent orientation.



A quaternion can be normalized by dividing it by its norm. The resulting quaternion maintains the same direction, but has a norm of 1, i.e. it moves on the unit sphere. This is generally necessary for rotation and orientation quaternions, to avoid rounding errors: <https://en.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions>

Note that `(x, y, z, w)` and `(-x, -y, -z, -w)` represent the same rotation, but normalization would be even more useful, e.g. for comparison purposes, if it would produce a unique representation. It is thus recommended that `w` be kept positive, which can be achieved by changing all the signs when `w` is negative.

### [QuaternionReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.QuaternionReflection)

Holder for reflection information generated from google/type/quaternion.proto

### [TimeOfDay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay)

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are [google.type.Date][google.type.Date] and `google.protobuf.Timestamp`.

### [TimeZone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeZone)

Represents a time zone from the [IANA Time Zone Database](https://www.iana.org/time-zones).

### [TimeofdayReflection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeofdayReflection)

Holder for reflection information generated from google/type/timeofday.proto

## Enums 

### [CalendarPeriod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.CalendarPeriod)

A `CalendarPeriod` represents the abstract concept of a time period that has a canonical start. Grammatically, "the start of the current `CalendarPeriod`." All calendar times begin at midnight UTC.

### [DateTime.TimeOffsetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DateTime.TimeOffsetOneofCase)

Enum of possible cases for the "time_offset" oneof.

### [DayOfWeek](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DayOfWeek)

Represents a day of the week.

### [Month](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Month)

Represents a month in the Gregorian calendar.

### [PhoneNumber.KindOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.PhoneNumber.KindOneofCase)

Enum of possible cases for the "kind" oneof.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
