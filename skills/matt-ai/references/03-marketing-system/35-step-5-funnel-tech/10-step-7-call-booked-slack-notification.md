# Step #7: Call Booked > Slack Notification

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=3ac92efe200b4724bf702bd9c056f950

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Calendly's built-in notification doesn't give your team enough context to walk into the call prepared. A dedicated Slack notification makes sure whoever's picking up the call knows exactly who they're talking to before it starts.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/bb114e3c1feb45a8a24f768332a9c45b70c1be2e4c124d5e860fc6e7c69b2b4b.png)

### Prerequisites

- [Step #4B: Call Booked Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=6ca6b510654b459e82772aade2c1881f) (Funnel Pages Course)

### Links

- [Zapier](https://zapier.com)
- [Calendly](https://calendly.com)
- [Slack](https://slack.com)

### Framework & Criteria

Paste this message template into your Slack action step's Message Text field. Replace the questions in this template with the questions on your Calendly booking form.

New Call Booked

Name:
Email:
Phone:
Question #1:
Question #2:

Booking Date:
Call Date:

For the Formatter steps in Zapier, paste this in as custom text to get a 12-hour format for the Booking Date and Call Date:

MMMM D, YYYY h:mm A

### Step-by-Step Instructions

1. **Create a channel in [Slack](https://slack.com) for your booked call notifications (e.g. "Calls Booked").** This is where every booked call notification will land, so it needs to exist before you build the automation.
2. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. This is where you'll be building this automation.
3. **Set [Calendly](https://calendly.com) as the trigger app, set the trigger event to Invitee Created or Rescheduled, then connect your Calendly account.** This fires the automation whenever a new call is booked, or an existing one is moved.
4. **Set the webhook subscription scope to User, the event type to your specific Calendly event, and the invitee type to New invitees only.** User scopes the trigger to your individual Calendly account rather than an entire organization. The event type makes sure the automation only fires for your sales call, rather than every event type on your calendar. New invitees only keeps the trigger focused on brand-new bookings rather than every reschedule.
5. **Click Continue, then click Test trigger to confirm a recent invitee is found.** Don't move on to the action step until a real invitee is successfully found.
6. **Click the + button to add a Formatter by Zapier step, then set the action event to Date / Time.** The Formatter turns Calendly's hard-to-read times into times that are easy to read. It costs 0 tasks, so it's free to use.
7. **Insert Created At into the Input field.** Click the + button, or press "/", and search "created at" to find it. This becomes your Booking Date.
8. **Paste "MMMM D, YYYY h:mm A" into the To Format field, then change To Timezone to the timezone you're in.** The custom text from the Framework & Criteria section turns the time into a 12-hour clock format. The timezone makes it show in your own local time.
9. **Click Continue, then click Test step.** You should see the month, day, and year, followed by the time in 12-hour format with AM or PM.
10. **Duplicate the Formatter step.** Click the three dots on the Formatter step, click Duplicate, then click on the copy and go back to the Configure tab. You need a second Formatter step for the Call Date, and duplicating the first one saves you from setting it up again.
11. **Remove Created At from the Input field and insert Scheduled Event > Start Time instead, then click Continue and test the step.** This becomes your Call Date. Leave every other setting the same.
12. **Click the + button to add an action step. Set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, then connect your Slack account.** Use Send Channel Message for a public channel and Send Private Channel Message for a private one.
13. **Choose the channel you created.** This keeps every booked call notification in one place.
14. **Paste the message template into the Message Text field, then insert the invitee's name, email, phone number, and your Calendly questions after each label.** Click the + button, or press "/", to insert the actual fields from the invitee you tested earlier. Include any custom questions from your Calendly booking form that you want your team to see. Do not type these in manually. Typed text won't pull real submission data.
15. **Insert the Formatter outputs after "Booking Date:" and "Call Date:".** Use the Output from the first Formatter step for the Booking Date, and the Output from the duplicated Formatter step for the Call Date. Use these instead of the dates from Calendly, so both dates come through in the easy-to-read format.
16. **Scroll to the bottom without changing anything else, then confirm Send Channel Message is set to Yes.** Every other field can stay at its default setting. This is what actually allows the message to send.
17. **Click Continue, then click Test step and check whether the message arrived in the correct Slack channel.** This confirms the trigger, the Formatter steps, the action, and the fields you inserted all worked together correctly.
18. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Don't leave it half-tested. Either confirm it's live or get the failure diagnosed before moving on.

### Completion Audit

- Did you create a channel in Slack for your booked call notifications?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set Calendly as the trigger app, set the trigger event to Invitee Created or Rescheduled, and connect your Calendly account?
- Did you set the webhook subscription scope to User, the event type to your specific Calendly event, and the invitee type to New invitees only?
- Did you click Continue, then click Test trigger to confirm a recent invitee is found?
- Did you add a Formatter by Zapier step and set the action event to Date / Time?
- Did you insert Created At into the Input field?
- Did you paste "MMMM D, YYYY h:mm A" into the To Format field and change To Timezone to your timezone?
- Did you click Continue, then click Test step?
- Did you duplicate the Formatter step?
- Did you replace Created At with Scheduled Event > Start Time in the duplicated step and test it?
- Did you add an action step, set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, and connect your Slack account?
- Did you choose the channel you created?
- Did you paste the message template into the Message Text field and insert the invitee's name, email, phone number, and your Calendly questions?
- Did you insert the Formatter outputs after "Booking Date:" and "Call Date:"?
- Did you scroll to the bottom and confirm Send Channel Message is set to Yes?
- Did you click Test step and check whether the message arrived in the correct Slack channel?
- Did you publish the automation, or diagnose the problem if it didn't work?
