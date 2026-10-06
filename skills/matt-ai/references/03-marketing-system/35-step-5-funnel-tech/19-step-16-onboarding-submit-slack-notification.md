# Step #16: Onboarding Submit > Slack Notification

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=68629028d1bb48e1a29d3dddcb798e5c

---
Video: this lesson has a video in Skool (open the Skool link to watch).

This step connects your onboarding form to Slack, so your team is notified the moment someone submits it.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/c8bb6f4dfc5e4b2db9d1ce7d88d3499a1f81bcfdcb594cd597dfc706fe3b9224.png)

### Links

- [Zapier](https://zapier.com)
- [Slack](https://slack.com)
- [Google Forms](https://forms.google.com)
- [Typeform](https://www.typeform.com)

### Framework & Criteria

Paste this message template into your slack action step message text field. Replace the questions in this template with the questions on your onboarding form.

New Onboarding Form Submitted:

[Question #1]: 
[Question #2]: 
[Question #3]:

Date Submitted:

### Step-by-Step Instructions

1. **Create a channel in [Slack](https://slack.com) for your onboarding submissions (e.g. "onboarding-form-submitted").** Pick a channel your team actually watches. It needs to exist before you build the automation.
2. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. This is where you'll be building the automation.
3. **Set Google Forms or Typeform as the trigger app, set the trigger event to New Form Response or New Entry, then connect your account.** Use whichever platform your onboarding questions actually live on. Different platforms name the event differently, so look for whichever option is closest if you don't see this exact wording.
4. **Select the specific onboarding form.** Make sure you're pointing at the exact form your new customers fill out.
5. **Click Continue, then click Test trigger.** You need a real, tested submission on file before you can map any of its fields in the action step.
6. **Click the + button to add an action step. Set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, then connect your Slack account.** Use Send Channel Message for a public channel and Send Private Channel Message for a private one.
7. **Choose the channel you created.** This keeps every onboarding notification in one place.
8. **Paste the message template into the Message Text field, then insert the matching field from your form submission after each label.** Click the + button, or press "/", to insert the actual onboarding answers from the submission you already tested. For "Date Submitted:", insert the Date Submitted field from Step 1. Do not type these in manually. Typed text won't pull real submission data.
9. **Scroll to the bottom without changing anything else, then confirm Send Channel Message is set to Yes.** This setting has to be correct or the message won't actually post.
10. **Click Continue, then click Test step and check whether the message arrived in the correct Slack channel.** Make sure the onboarding answers show up correctly and nothing is missing or mismatched.
11. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Only publish once you've confirmed the Slack message actually posts with the correct onboarding data.

### Completion Audit

- Did you create a channel in Slack for your onboarding submissions?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set Google Forms or Typeform as the trigger app, set the trigger event, and connect your account?
- Did you select the specific onboarding form?
- Did you click Continue, then click Test trigger?
- Did you add an action step, set Slack as the action app, set the action event to Send Channel Message or Send Private Channel Message, and connect your Slack account?
- Did you choose the channel you created?
- Did you paste the message template into the Message Text field and insert the matching field after each label?
- Did you scroll to the bottom and confirm Send Channel Message is set to Yes?
- Did you click Test step and check whether the message arrived in the correct Slack channel?
- Did you publish the automation, or diagnose the problem if it didn't work?
