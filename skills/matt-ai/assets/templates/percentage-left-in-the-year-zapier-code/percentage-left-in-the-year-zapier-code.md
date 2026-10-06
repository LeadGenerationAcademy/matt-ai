# Percentage Left In The Year Zapier Code

**Percentage Left In The Year Messages Zapier Code**

This document will help you create your zapier workflow that will send you a percentage left in the year message via Email and SMS every morning.

**Zapier workflow**

<img src="media/image3.png" style="width:2.50521in;height:4.23738in" />

**Code By Zapier (Run Javascript)**

Copy and paste code below into your Code by Zapier step.

---------------------------------------------------------------------------------------------

const now = new Date();

const year = now.getUTCFullYear();

const isLeapYear = (year % 4 === 0 && year % 100 !== 0) \|\| year % 400 === 0;

const totalDays = isLeapYear ? 366 : 365;

const startOfYear = Date.UTC(year, 0, 1);

const today = Date.UTC(year, now.getUTCMonth(), now.getUTCDate());

const daysElapsed = Math.round((today - startOfYear) / 86400000) + 1;

const daysRemaining = totalDays - daysElapsed;

const percentGone = ((daysElapsed / totalDays) \* 100).toFixed(2) + '%';

output = {

year: year,

days_elapsed: daysElapsed,

days_remaining: daysRemaining,

percent_gone: percentGone

};

---------------------------------------------------------------------------------------------

**Gmail (Send Email)**

You can change the text to whatever you want, these are just a default template that anyone can use.

Copy and paste this into the Subject field in Configure.

---------------------------------------------------------------------------------------------

{{=output\["379434083"\]\["percent_gone"\]}} of {{=output\["379434083"\]\["year"\]}} is gone

---------------------------------------------------------------------------------------------

It should look like this:

<img src="media/image4.png" style="width:4.06291in;height:1.21559in" />

Copy and paste this into the Body field in Configure.

---------------------------------------------------------------------------------------------

{{=output\["379434083"\]\["percent_gone"\]}} of {{=output\["379434083"\]\["year"\]}} is gone.

{{=output\["379434083"\]\["days_elapsed"\]}} days elapsed \| {{=output\["379434083"\]\["days_remaining"\]}} days remaining

Make today count.

---------------------------------------------------------------------------------------------

It should look like this:

<img src="media/image2.png" style="width:3.80729in;height:2.35437in" />

**SMS by Zapier (Send SMS)**

You can change the text to whatever you want, these are just a default template that anyone can use.

Copy and paste this into the Message field in Configure.

---------------------------------------------------------------------------------------------

{{=output\["379434083"\]\["percent_gone"\]}} of {{=output\["379434083"\]\["year"\]}} is gone.

{{=output\["379434083"\]\["days_elapsed"\]}} days elapsed.

{{=output\["379434083"\]\["days_remaining"\]}} days remaining.

Make today count.

---------------------------------------------------------------------------------------------

It should look like this:

<img src="media/image1.png" style="width:3.6952in;height:2.2511in" />
