# Step #6: Application > Slack Notification

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=384636e40daa4657a16cabf79b93ede9

---
Video: this lesson has a video in Skool (open the Skool link to watch).

When someone submits your application, you want your team to know about it immediately, without anyone having to check the form platform itself.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/6669582341aa495e82b32f11663790c3a4863001608c46d6a71d8ee4114c8ae6.png)

### Prerequisites

- [Step #4A: Application Form](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=ef780cefa17b4c27b6e83db128999d5c) (Funnel Pages Course)

### Links

- [Zapier](https://zapier.com)
- [Slack](https://slack.com)
- [Typeform](https://www.typeform.com)
- [Webflow](https://webflow.com)

### Framework & Criteria

Paste this message template into your Slack action step's Message Text field. Replace the questions in this template with the questions on your application form.

New Application Submitted

Name:
Email:
[Question #1]:
[Question #2]:
[Question #3]:

Date Submitted:

### Step-by-Step Instructions

1. **Create a channel in [Slack](https://slack.com) for your application notifications (e.g. "application-submitted").** This is where every application notification will land, so it needs to exist before you build the automation.
2. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. This step uses Zapier, but any automation platform capable of the same trigger and action works the same way.
3. **Set whichever platform hosts your application form (e.g. Typeform, Webflow) as the trigger app, set the trigger event to New Form Submission, then connect your account.** Some platforms label this event differently. Choose whatever event fires when a new application comes in. Every app used in a Zap needs its own account connection before you can configure it.
4. **Choose the specific application form.** If you run more than one form or site, confirm you're selecting the one your application actually lives on.
5. **Click Continue, then click Test trigger to confirm a submission is found.** Don't move on to the action step until a real submission is successfully found.
6. **Click the + button to add an action step. Set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, then connect your Slack account.** Use Send Channel Message for a public channel and Send Private Channel Message for a private one.
7. **Choose the channel you created.** This keeps every application notification in one place.
8. **Paste the message template into the Message Text field, then insert the matching field from your application after each label.** Click the + button, or press "/", to insert whichever fields your application actually collects. This could include more fields than a simple opt-in form. For "Date Submitted:", insert the Date Submitted field from Step 1 (New Form Submission). Do not type these in manually. Typed text won't pull real submission data.
9. **Scroll to the bottom without changing anything else, then confirm Send Channel Message is set to Yes.** Every other field can stay at its default setting. This is what actually allows the message to send, and it's also where you confirm the channel you selected earlier is correct.
10. **Click Continue, then click Test step and check whether the message arrived in the correct Slack channel.** This confirms the trigger, the action, and the fields you inserted all worked together correctly.
11. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Don't leave it half-tested. Either confirm it's live or get the failure diagnosed before moving on.

### Completion Audit

- Did you create a channel in Slack for your application notifications?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set your application form platform as the trigger app, set the trigger event to New Form Submission, and connect your account?
- Did you choose the specific application form?
- Did you click Continue, then click Test trigger to confirm a submission is found?
- Did you add an action step, set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, and connect your Slack account?
- Did you choose the channel you created?
- Did you paste the message template into the Message Text field and insert the matching field after each label?
- Did you scroll to the bottom and confirm Send Channel Message is set to Yes?
- Did you click Test step and check whether the message arrived in the correct Slack channel?
- Did you publish the automation, or diagnose the problem if it didn't work?
