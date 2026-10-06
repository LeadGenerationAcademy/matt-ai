# Step #9: Call Booked > Pre Call Flow

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=a785359da1c4428b927b71c35dad0c94

---
Video: this lesson has a video in Skool (open the Skool link to watch).

This step connects your booking platform to your finished Pre-Call Flow, so it starts automatically the moment someone books a call.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/70bac24c726742c798a9c5570c1cbbd139d74072c5f045a9bc0cab85269d7b95.png)

### Prerequisites

- [Step #4B: Call Booked Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=6ca6b510654b459e82772aade2c1881f) (Funnel Pages Course)
- [Step #6A: Pre-Call Email Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=3b28b1dd935148b89ef719f783ffe2db) (Funnel Emails Course)

### Links

- [Zapier](https://zapier.com)
- [Calendly](https://calendly.com)
- [Kit](https://kit.com)

### Step-by-Step Instructions

1. **Create a "Call Booked" tag in your email platform.** This tag is what starts your Pre-Call Flow, so it needs to exist first, whether you end up using a native integration or Zapier.
2. **Check if your email platform has a native Calendly integration or template.** Some email platforms, like [Kit](https://kit.com), offer a premium visual automation template built specifically for Calendly.
3. **If a native integration exists, connect Calendly and set the trigger to the correct event type.** Choose the specific Calendly event type that matches the call this flow should be tied to.
4. **Add the "Call Booked" tag as the first action in the automation.** Even if you're using the native integration, the tag still needs to be applied first.
5. **Set the next action to enroll the subscriber into your finished Pre-Call Flow, then confirm the automation is set to Active.** This is the sequence you already built inside your email platform. An inactive automation will not run.
6. **If no native integration exists, log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** This is your fallback path any time your email platform doesn't offer a direct Calendly connection.
7. **Set Calendly as the trigger app, set the trigger event to Invitee Created or Rescheduled, then connect your Calendly account.** This is the same trigger used in [Step #7: Call Booked > Slack Notification](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=3ac92efe200b4724bf702bd9c056f950).
8. **Set the webhook subscription scope to User, the event type to your specific Calendly event, and the invitee type to New invitees only.** This makes sure the automation only fires for the exact call type you want it tied to, and doesn't re-fire every time someone reschedules an existing call.
9. **Click Continue, then click Test trigger.** You need a real, tested booking on file before you can map any data in the next step.
10. **Click the + button to add an action step. Set your email platform as the action app, set the action event to Add Tag to Subscriber, then connect your account.** This applies the same "Call Booked" tag from step 1, through Zapier instead of natively.
11. **Set the Tag field to "Call Booked".** This has to match the exact tag your Pre-Call Flow is watching for.
12. **Insert the invitee's data from your tested booking into the tag action.** Click into each field, then click the + button or press "/" to insert the actual invitee fields from the trigger you already tested. Do not type these in manually. Typed text won't pull real invitee data.
13. **Click Continue, then click Test step.** Confirm the step runs successfully before checking anything else.
14. **Confirm the "Call Booked" tag triggers your Pre-Call Flow inside your email platform.** The tag itself doesn't send anything. It just starts the flow you already built natively.
15. **Book a real test call, then confirm the tag gets applied and the Pre-Call Flow actually starts sending.** This tests the full flow end to end.
16. **If it works, publish the automation or leave the workflow active. If not, ask ChatGPT or Claude to diagnose the problem.** Only publish once you've confirmed the tag applies correctly and the Pre-Call Flow actually fires from it.

### Completion Audit

- Did you create a "Call Booked" tag in your email platform?
- Did you check whether your email platform has a native Calendly integration or template?
- If using a native integration, did you connect Calendly and set the correct event type?
- Did you add the "Call Booked" tag as the first action in the automation?
- Did you set the next action to enroll the subscriber into your Pre-Call Flow and confirm the automation is set to Active?
- If no native integration exists, did you log in to Zapier, then click Create, then click Zaps?
- Did you set Calendly as the trigger app, set the trigger event to Invitee Created or Rescheduled, and connect your Calendly account?
- Did you set the webhook subscription scope to User, the event type to your specific Calendly event, and the invitee type to New invitees only?
- Did you click Continue, then click Test trigger?
- Did you add an action step, set your email platform as the action app, set the action event to Add Tag to Subscriber, and connect your account?
- Did you set the Tag field to "Call Booked"?
- Did you insert the invitee's data from your tested booking into the tag action?
- Did you click Continue, then click Test step?
- Did you confirm the "Call Booked" tag triggers your Pre-Call Flow?
- Did you book a real test call and confirm the Pre-Call Flow started sending?
- Did you publish the automation or leave the workflow active, or diagnose the problem if it didn't work?
