# Step #7: Pre-Call Email & SMS Confirmation

Course: Step #3: Funnel Emails
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=87532299dfb14818b050e76ca3059da0

---
The moment someone books a Sales Call, they get a confirmation email from Kit and a confirmation text from Roezan. Both have the call details, your One-Pager and your Loom.

Your closer gets a text and an email from Calendly at the same time, with who booked, their company, their website and when the call is.

This is a second confirmation on top of the one Calendly already sends. Leave Calendly's own confirmation email/sms reminders on.

How you frame the One-Pager matters. Tell them it takes 5 to 10 minutes to read and will save us 45 to 90 minutes if they just read it before the call.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/9df95616caae41109fc92a48b8bc46c52355dc3928ec47b3bce8ae4122006ebf.png)

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/969999bcddd74877a55338e4dd020b887925383bec5f4722bc9c6948a8437532.png)

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/91e790ad1cfc48edaa092298099a44e6ba5ec696cb964401ae95672bec1fd608.png)

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/0762744d926845949f61412f67bbe440123ff26d169c4ff48588d32865846e52.png)

Note: This is a new Calendly account shown in image, so that's why I have this warning message and cannot change the Text Reminder To Host message, but you should be able to.

### Prerequisites

- [Step #7: Create One-Pager](https://www.skool.com/leadgenerationacademy/classroom/840e7e5f?md=47264b77776f422e889dcffc1b21198c) (Offer Course)
- [Step #8: Create 3-Min Loom + Message](https://www.skool.com/leadgenerationacademy/classroom/840e7e5f?md=f7792b2c54204b4e9edaafc958d784c4) (Offer Course)
- [Step #4B: Call Booked Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=6ca6b510654b459e82772aade2c1881f) (Funnel Pages Course)
- [Step #0A: Platform Setup](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=9b9fcb9c1cf0431fae1cad256d8f8fdc) (Current Course)

### Links

- [Kit](https://app.kit.com/)
- [Roezan](https://www.roezan.com/)
- [Zapier](https://zapier.com/)
- [Calendly](https://calendly.com/)

### Framework

1. **Prospect Confirmation (Email and SMS):**
  1. Call date
  2. Call time
  3. Time Zone
  4. Closer's name
  5. One-Pager link
  6. Three-minute Loom link
2. **Closer Notification (separate from Prospect Confirmation):**
  1. Prospect's name
  2. Company
  3. Website
  4. Email
  5. Phone number
  6. Call date and time
  7. Application or CRM link
3. Both notifications send immediately after the call is booked
4. One Workflow: All three actions live inside the same Workflow, not three separate ones

**Use This Template**

**Prospect Email (Kit)**

Subject: Confirmed: {{ subscriber.event_name }} with {{ subscriber.event_organizer }} on {{ subscriber.event_date }}

Email Body:

You're booked in. Here are the details:

Date: {{ subscriber.event_date }}

Time: {{ subscriber.event_time }} {{ subscriber.event_timezone }}

Who you're talking to: {{ subscriber.event_organizer }}

Two things to go through before the call:

One-pager: [One-Pager Link]

Loom video: [Loom Link]

Read the one-pager before we talk. It takes 5 to 10 minutes and it saves us 45 to 90 minutes on the call itself. The video covers the same thing if you'd rather watch than read.

If you need to move the call, reply to this email and we'll sort it out.

{{ subscriber.event_organizer }}

**Prospect SMS (Roezan)**

Hi %FIRST_NAME%,
You're booked for %EVENT_NAME% with %EVENT_ORGANIZER% on %EVENT_DATE% at %EVENT_TIME% %EVENT_TIMEZONE%.

Please review this Loom and one-pager before the call. It takes 5-10min and saves us 45-90min.

Loom: [Loom Link]
One-Pager: [One-Pager Link]

**Closer Email (Calendly)**

Subject: New Call Booked: {Invitee Full Name} on {Event Date} at {Event Time}

Body:

New call booked.

Prospect: {Invitee Full Name}

Company: {Answer 1}

Website: {Answer 2}

Email: {Invitee Email}

Phone: {Answer 3}

Call: {Event Date}, {Event Time}

Application / CRM: [CRM Link]

**Closer SMS (Calendly)**

New Call Booked.
{Invitee Full Name}
{Answer 1}
{Answer 2}
{Invitee Email}
{Answer 3}
{Event Date}, {Event Time}
[CRM Link]

### Step-by-Step Instructions

1. **Create a "Call Booked" tag in Kit.** Go to Subscribers, press the + next to All Tags, type "Call Booked", then click Save. This tag is what starts your Kit automation.
2. **Create the five event fields in Kit.** Go to Subscribers, click any subscriber, click the three dots next to Custom Fields, then click Add new. Kit needs a value before it adds a field, so use these:
  - Event Name: Strategy Call
  - Event Organizer: John Smith
  - Event Date: Wednesday, September 23, 2026
  - Event Time: 9:00 AM
  - Event Timezone: America/New_York
3. **Create the same "Call Booked" tag and the same five fields in Roezan.** Go to Tags, click Add New, name it "Call Booked", then click Submit. Then go to Fields and add the same five fields, named exactly the same as in Kit.
4. **Create a new email sequence in Kit, paste in the Prospect Email template, then replace every {{ }} field using the Personalization button.** The Personalization button is the @ in the body toolbar. The subject line doesn't have one, so add the field in the body first, then cut and paste it into the subject line. Replace the links with your own, name the sequence something like "Pre-Call Confirmation", set Send this email to As soon as possible, and turn Published on. Then go to the sequence's Settings tab and turn on the option that lets subscribers restart the sequence. Without it, anyone who books a second call won't get a second confirmation.
5. **Create a new visual automation in Kit, set the trigger to Tag Is Added, then select "Call Booked".** Go to Automation, then Visual automations, click New automation, click Start from scratch, then click Start building. Choose Tag is added, search "Call Booked", then click Add Event.
6. **Press the + button, click Email Sequence, select your Pre-Call Confirmation sequence, add a second action that removes the "Call Booked" tag, then publish the automation.** Kit won't start the automation for someone who already has the tag. Removing it lets the automation fire again the next time they book.
7. **In Roezan, go to Automations, click Create Automation, name it, set the type to Multiple entry, then click Create Automation.** Name it something like "Pre-Call Confirmation". Multiple entry means someone who books a second call gets the confirmation again.
8. **Click Add a new trigger, choose Contact Tag Added, then select "Call Booked".** This is the tag you created in step 3.
9. **Press the + button, click Send a Message, paste in the Prospect SMS template, then replace every %FIELD% using the Personalize button.** Replace the links with your own too. Check that Segments (credits) says 2, click Insert, then turn the automation on.
10. **In Calendly, add Company, Website and Phone Number as the first three questions on your Sales Call booking form.** Keep them in that order. Calendly labels them Answer 1, Answer 2 and Answer 3 by position. Make Phone Number required, because Roezan can't text anyone without it.
11. **Click Workflows, click New Workflow, choose the Text booking confirmation to host template, select your Sales Call event type, then click Apply.** This template already fires the moment a call is booked.
12. **Click Add action, choose Send email to host, paste in the Closer Email template, then click Save.** Insert each field as a Calendly variable and replace [CRM Link] with the link to your CRM.
13. **Click Edit on Send text to host, confirm the phone number is your closer's, paste in the Closer SMS template, then click Save.** Same as the email: insert each field as a Calendly variable and swap in your CRM link.
14. **Log in to Zapier, click Create, then Zaps. Set Calendly as the trigger app and Invitee Created or Rescheduled as the trigger event, then connect your Calendly account.** This trigger only works on a paid Calendly plan (Standard, Teams or Enterprise).
15. **Set the webhook subscription scope to User, the event type to your Sales Call, and the invitee type to New invitees only, then click Continue and Test trigger.** You need a tested booking on file before you can map any fields in the next steps.
16. **Add a Formatter by Zapier step to format the date.** Set the action event to Date / Time, then Format. Insert Scheduled Event > Start Time into Input, set To Format to Custom and type dddd, MMMM D, YYYY, insert Calendly's Timezone into To Timezone, and set From Timezone to UTC. This turns the raw timestamp into "Wednesday, September 23, 2026".
17. **Duplicate that Formatter step and change only the To Format to h:mm A.** This gives you the time on its own, like "9:00 AM".
18. **Add a Kit step, set the action event to Add Tag to Subscriber, then map every field.** Set Tag to "Call Booked", then insert Email, First Name, Event Name (Scheduled Event > Name), Event Organizer (Scheduled Event > Event Memberships > User Name), Event Timezone (Timezone), Event Time (second Formatter) and Event Date (first Formatter). Use the + button or "/" to insert each one. Typed text won't pull real booking data.
19. **Add a Roezan SMS step, set the action event to Add a Contact Tag, then map every field.** Set Tag to "Call Booked" and insert the Phone Number answer into Contact Phone. Then map First Name, Email and the same five event fields as Kit. For First Name, use 1. Name. Event Memberships > User Name is your closer's name.
20. **Publish the Zap, then book two test calls using an email and phone number you can actually check.** Confirm all four messages arrive both times and every field fills in. The second booking proves repeat bookers get a confirmation too.
21. **If everything works, leave every automation and workflow on. If not, ask ChatGPT or Claude to diagnose the problem.** Don't launch until all four messages fire reliably every time.

### Completion Audit

- Did you create a "Call Booked" tag in Kit?
- Did you create the five event fields in Kit?
- Did you create the same "Call Booked" tag and the same five fields in Roezan?
- Did you create a new email sequence in Kit, paste in the Prospect Email template, and replace every {{ }} field using the Personalization button?
- Did you create a new visual automation in Kit, set the trigger to Tag Is Added, and select "Call Booked"?
- Did you add the Email Sequence action, add a second action that removes the "Call Booked" tag, and publish the automation?
- Did you create a Roezan automation, name it, and set the type to Multiple entry?
- Did you click Add a new trigger, choose Contact Tag Added, and select "Call Booked"?
- Did you add a Send a Message step, paste in the Prospect SMS template, and replace every %FIELD% using the Personalize button?
- Did you add Company, Website and Phone Number as the first three questions on your Sales Call booking form?
- Did you create a Calendly Workflow using the Text booking confirmation to host template and select your Sales Call event type?
- Did you click Add action, choose Send email to host, paste in the Closer Email template, and click Save?
- Did you confirm the phone number is your closer's, paste in the Closer SMS template, and click Save?
- Did you log in to Zapier, set Calendly as the trigger app, set the trigger event to Invitee Created or Rescheduled, and connect your Calendly account?
- Did you set the webhook subscription scope to User, the event type to your Sales Call, and the invitee type to New invitees only, then test the trigger?
- Did you add a Formatter by Zapier step to format the date?
- Did you duplicate that Formatter step and change only the To Format to h:mm A?
- Did you add a Kit step, set the action event to Add Tag to Subscriber, and map every field?
- Did you add a Roezan SMS step, set the action event to Add a Contact Tag, and map every field?
- Did you publish the Zap and book two test calls using an email and phone number you can actually check?
- Did you leave every automation and workflow on, or diagnose the problem if something didn't work?
