# Step #8: Set up Slack Notifications

Course: Step #8: Paid Ads Setup
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/c0a462fb?md=7db362a1942c4264bcf436ffac94f63a

---
![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/da210bb138284384877d0bf3569385e4c2e14a801e9d4226a23b2008257b0797.png)

### Prerequisites

- [Step #3: Clone Calendar Tool](https://www.skool.com/leadgenerationacademy/classroom/c0a462fb?md=bc29b4542cff4e9095e09f832790dd69) (Current Course)

### Sign up

- [Zapier](https://zapier.com/)
- [Calendly](https://calendly.com/)
- [Slack](https://slack.com/)

### Step-by-Step Instructions

1. **Check whether you already built this automation in [Step #7: Call Booked > Slack Notification](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=3ac92efe200b4724bf702bd9c056f950).** If you have, duplicate the workflow in zapier and set the trigger to the Facebook calendar event you cloned in [Step #3: Clone Calendar Tool](https://www.skool.com/leadgenerationacademy/classroom/c0a462fb?md=bc29b4542cff4e9095e09f832790dd69), and you are done with this page. If you have not built it yet, go through the rest of the steps below.
2. **Sign up for an automation platform like [Zapier](https://zapier.com/) if you don't already have one.** This step uses Zapier, but any automation platform capable of the same trigger and action works the same way.
3. **Create a new automation.** This is where you'll build the trigger and action together.
4. **Set [Calendly](https://calendly.com/) as the trigger app.** Calendly is the most common scheduling platform, so this covers the vast majority of setups.
5. **Set the trigger event to "Invitee created or rescheduled".** This fires the automation whenever a new call is booked, or an existing one is moved.
6. **Connect your Calendly account.** Every platform used in an automation, both the trigger and the action, needs its own account connection before you can configure it.
7. **Set the webhook subscription scope to "User".** This scopes the trigger to your individual Calendly account rather than an entire organization.
8. **Set the event type to your Facebook calendar event.** This is the /fb calendar you cloned in Step #3: Clone Calendar Tool. Setting it here makes sure the automation only fires for calls booked off your Facebook ads rather than every event type on your calendar.
9. **Set the invitee type to "New invitees only".** This keeps the trigger focused on brand-new bookings rather than every reschedule.
10. **Test the trigger to confirm a recent invitee is found.** Don't move on to the action step until a real invitee is successfully found.
11. **Set Slack as the action app.** This is what actually sends the notification.
12. **Connect your Slack account.** Same as the trigger, this needs its own connection before you can configure the action.
13. **Set the action event to Send channel message or Send private channel message.** Use whichever version matches the channel you're sending to, a private channel requires the private channel version of this event.
14. **Choose the channel you want the notification sent to.** For example, a channel named something like "Calls Booked."
15. **Click into the Message Text field and insert the invitee's full name, email, and phone number.** Click into the field, then use the "+" button, or press "/", to insert the actual name, email, and phone fields from the invitee you tested earlier. Do not type these in manually, typed text won't pull real submission data.
16. **Insert any additional fields you've set up on Calendly that you want included.** Calendly lets you add custom questions to your booking form, insert any of those you want your team to see in the notification.
17. **Scroll to the bottom without changing anything else.** Every other field above this point can stay at its default setting.
18. **Confirm Send channel message is set to "Yes".** This is what actually allows the message to send, and it's also where you confirm the channel you selected earlier is correct.
19. **Test the action step.** Run this before publishing to confirm the whole automation actually works end to end.
20. **Check whether the message arrived in the correct Slack channel.** This confirms the trigger, the action, and the fields you inserted all worked together correctly.
21. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Don't leave it half-tested, either confirm it's live or get the failure diagnosed before moving on.

### Completion Audit

- Did you check whether you already built this automation in Step #7: Call Booked > Slack Notification?
- Did you sign up for an automation platform like Zapier if you didn't already have one?
- Did you create a new automation?
- Did you set Calendly as the trigger app?
- Did you set the trigger event to "Invitee created or rescheduled"?
- Did you connect your Calendly account?
- Did you set the webhook subscription scope to "User"?
- Did you set the event type to your Facebook calendar event?
- Did you set the invitee type to "New invitees only"?
- Did you test the trigger to confirm a recent invitee is found?
- Did you set Slack as the action app?
- Did you connect your Slack account?
- Did you set the action event to Send channel message or Send private channel message?
- Did you choose the channel you want the notification sent to?
- Did you click into the Message Text field and insert the invitee's full name, email, and phone number?
- Did you insert any additional fields you've set up on Calendly that you want included?
- Did you scroll to the bottom without changing anything else?
- Did you confirm Send channel message is set to "Yes"?
- Did you test the action step?
- Did you check whether the message arrived in the correct Slack channel?
- Did you publish the automation, or diagnose the problem if it didn't work?
