# Step #8: Setup Partnership Integrations

Course: Step #10: Partnerships Setup
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/b0606dd1?md=70f260f8a12a4ecb81cf8c3d69a4c990

---
It's very good if you set up your partnership call booking, respond to everything that comes in, and integrate notifications from your LinkedIn, your email, and everything else into Slack so that you don't miss anything.

With partnerships, speed to lead isn't quite as essential as it is with clients and ad funnels. It's generally more forgiving, but you still don't want to miss anything.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/0c8a7c2e7da04c81a349d0e6b4e7c4b2aac65858c6934a57b223e7ccb97654bc.png)

### Prerequisites

- [Step #7: Setup Prospecting Campaigns](https://www.skool.com/leadgenerationacademy/classroom/b0606dd1?md=c51fd4fc00d843e3baa1aa2f2b146bad) (Current Course)

### Step-by-Step Instructions

1. **Set up a call booking system for partnership calls.** Partners who respond and want to talk need a fast, simple way to get on your calendar.
2. **Set up a process for responding to partner replies.** Speed to lead isn't as critical here as it is with clients, but you still need a real process so nothing sits unanswered.
3. **Create a "Partnership Outreach" label in Gmail or Outlook.** This is what lets Slack pull in only your partnership emails instead of everything in your inbox.
4. **Label every partnership outreach email with that label.** If it's not labeled, it won't trigger a notification.
5. **Build a Zap that triggers on new emails with that label and sends a Slack message.** Do this in order:
  1. **Add Gmail or Outlook as the trigger app.** This is the starting point of the automation.
  2. **Set the trigger event to New Email.** This tells Zapier what kind of event to watch for.
  3. **Connect your email account.** Zapier needs access to actually read your inbox.
  4. **Set the Label or mailbox field to "Partnership Outreach."** This limits the trigger to only the emails you've labeled.
  5. **Click Test Trigger and select the record that pops up.** Click Continue With Selected Record to confirm the trigger is pulling real data.
  6. **Add a Slack action set to Send Channel Message.** Use Send Private Channel Message instead if your notification channel is private.
  7. **Create a Slack channel for this (e.g. "Email Partnership Outreach Notifications").** Keep it separate from your other channels so it's obvious what these notifications are for.
  8. **Connect your Slack account and choose that channel.** This tells Zapier where to send the message.
  9. **Set the Message Text field to Body Plain.** Click the "+" in the top right of the box, or type "/" in the box, and select Body Plain from the list.
  10. **Set "Send Channel Message" to Yes.** Scroll down until you see this option and toggle it on.
6. **Test the Zap and publish it once it works.** Click Continue, then Test Step, and confirm you actually receive the notification in Slack. If it doesn't work, ask ChatGPT or Claude to help diagnose the problem before you publish.
7. **Ask ChatGPT or Claude how to get LinkedIn, Twitter, or any other outreach channel's notifications into Slack.** These platforms don't work through Zapier the same way email does, so have it walk you through whatever method actually works for that channel.

### Completion Audit

- Is a call booking system set up for partnership calls?
- Is there a process for responding to partner replies?
- Did you create a "Partnership Outreach" label in Gmail or Outlook?
- Are you labeling every partnership outreach email with it?
- Did you build and test the Zap that sends labeled emails to Slack?
- Did you publish the Zap once it worked?
- Did you get LinkedIn, Twitter, or other channels' notifications into Slack?
