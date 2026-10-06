# Step #3: Opt In > Slack Notification

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=5ca9f6532e394524b553eff174dd0ee3

---
Video: this lesson has a video in Skool (open the Skool link to watch).

When someone opts into your lead magnet, you want your team to know about it immediately, without anyone having to check the form platform itself.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/0cd0442404154a69a2ef201e53476e56001a7899f6e04529805c2fc8837ce018.png)

### Prerequisites

- [Step #1: Opt In Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=7063959ac1fe4a32b1fa9a2de80315fc) (Funnel Pages Course)

### Links

- [Zapier](https://zapier.com)
- [Webflow](https://webflow.com)
- [Slack](https://slack.com)

### Framework & Criteria

Paste this message template into your Slack action step's Message Text field:

New [Your Lead Magnet Name] Opt In

Full Name:
Email:
Phone:

Date Submitted:

### Step-by-Step Instructions

1. **Create a channel in [Slack](https://slack.com) for your opt-in notifications (e.g. "Lead Generation Opt In").** This is where every opt-in notification will land, so it needs to exist before you build the automation.
2. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. This step uses Zapier, but any automation platform capable of the same trigger and action works the same way.
3. **Set your opt-in form platform (e.g. Webflow) as the trigger app, set the trigger event to New Form Submission, then connect your account.** This should match wherever your opt-in form was actually built, whether that's Webflow or a form embedded directly through your email platform. Every app used in a Zap needs its own account connection before you can configure it.
4. **Choose the site your opt-in form is on, then choose the specific opt-in form.** If you manage more than one site, or a site has more than one form, make sure you're selecting the right one.
5. **Click Continue, then click Test trigger to confirm a submission is found.** Don't move on to the action step until a real submission is successfully found.
6. **Click the + button to add an action step. Set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, then connect your Slack account.** Use Send Channel Message for a public channel and Send Private Channel Message for a private one.
7. **Choose the channel you created.** This keeps every opt-in notification in one place.
8. **Paste the message template into the Message Text field, then insert the matching field from your form submission after each label.** Click the + button, or press "/", to insert the actual fields from the form response you tested earlier. For "Date Submitted:", insert the Date Submitted field from Step 1 (New Form Submission). Do not type these in manually. Typed text won't pull real submission data.
9. **Scroll to the bottom without changing anything else, then confirm Send Channel Message is set to Yes.** Every other field can stay at its default setting. This is what actually allows the message to send, and it's also where you confirm the channel you selected earlier is correct.
10. **Click Continue, then click Test step and check whether the message arrived in the correct Slack channel.** This confirms the trigger, the action, and the fields you inserted all worked together correctly.
11. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Don't leave it half-tested. Either confirm it's live or get the failure diagnosed before moving on.

**Completion Audit**

- Did you create a channel in Slack for your opt-in notifications?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set your opt-in form platform as the trigger app, set the trigger event to New Form Submission, and connect your account?
- Did you choose the site your opt-in form is on and the specific opt-in form?
- Did you click Continue, then click Test trigger to confirm a submission is found?
- Did you add an action step, set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, and connect your Slack account?
- Did you choose the channel you created?
- Did you paste the message template into the Message Text field and insert the matching field after each label?
- Did you scroll to the bottom and confirm Send Channel Message is set to Yes?
- Did you click Test step and check whether the message arrived in the correct Slack channel?
- Did you publish the automation, or diagnose the problem if it didn't work?
