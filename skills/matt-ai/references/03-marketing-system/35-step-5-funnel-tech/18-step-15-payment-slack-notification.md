# Step #15: Payment > Slack Notification

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=5d072c8cf7344461a56f6fdcef389621

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Continuing off the same automation you built in Step #14, this step adds a Slack notification the moment a new payment comes through, so your whole team knows a deal closed without anyone having to check Stripe or your CRM.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/e10efe275e9d4b73b420f7e0b406c152c675fe7176144fd98f9ef919b1dfdfde.png)

### Prerequisites

- [Step #14: Payment > Onboarding Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=3137dd50589c4e95a3ee25e3309174ea) (Current Course)

### Links

- [Zapier](https://zapier.com)
- [Slack](https://slack.com)
- [Stripe](https://dashboard.stripe.com)

### Framework & Criteria

Paste this message template into your Slack action step's Message Text field. You can add or remove from this template to fit your business.

New Client Payment

Name:
Email:
Amount Received:

Date of Payment:

### Step-by-Step Instructions

1. **Create a "New Client Payment" channel in [Slack](https://slack.com).** This is where every payment notification will land, so it needs to exist before you build the automation.
2. **Go back into the Zap you built in [Step #14: Payment > Onboarding Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=3137dd50589c4e95a3ee25e3309174ea).** You're not starting over. The New Payment trigger and the tag step should already be built.
3. **Click the + button after the tag step to add an action step. Set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, then connect your Slack account.** This way the Slack message only goes out after the tag has already been applied. Use Send Channel Message for a public channel and Send Private Channel Message for a private one.
4. **Choose the "New Client Payment" channel you created.** This keeps every payment notification in one place.
5. **Paste the message template into the Message Text field.** Use the template from the Framework & Criteria section above. The fields you insert in the next steps go right after each label.
6. **Insert Customer > Name after "Name:" and Customer > Email after "Email:".** Click the + button, or press "/", and search "customer name" and "customer email" to find them. Use the Email field nested under Customer, the same one you used in Step #14. Do not type these in manually. Typed text won't pull real payment data.
7. **Insert Amount Received Formatted after "Amount Received:" and Created Formatted after "Date of Payment:".** Amount Received Formatted already comes with the currency symbol attached, so there's nothing to type next to it. Created Formatted is the date and time the payment came through in Stripe.
8. **Scroll to the bottom without changing anything else, then confirm Send Channel Message is set to Yes.** Every other field can stay at its default setting. This is what actually allows the message to send.
9. **Click Continue, then click Test step and check whether the message arrived in the correct Slack channel with every field filled in.** Confirm every label has its matching data next to it.
10. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** You're publishing the same Zap from Step #14, just with this notification added on top.

### Completion Audit

- Did you create a "New Client Payment" channel in Slack?
- Did you go back into the Zap you built in Step #14?
- Did you add an action step after the tag step, set Slack as the action app, set the action event, and connect your Slack account?
- Did you choose the "New Client Payment" channel you created?
- Did you paste the message template into the Message Text field?
- Did you insert Customer > Name after "Name:" and Customer > Email after "Email:"?
- Did you insert Amount Received Formatted after "Amount Received:" and Created Formatted after "Date of Payment:"?
- Did you scroll to the bottom and confirm Send Channel Message is set to Yes?
- Did you click Test step and check whether the message arrived with every field filled in?
- Did you publish the automation, or diagnose the problem if it didn't work?
