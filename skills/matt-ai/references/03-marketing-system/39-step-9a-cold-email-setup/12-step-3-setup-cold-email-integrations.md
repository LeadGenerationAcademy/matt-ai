# Step #3: Setup Cold Email Integrations

Course: Step #9A: Cold Email Setup
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/25ab2241?md=dbb45011c8d74c83b7787a34ec211e94

---
We are going to want to set up several integrations so replies get routed to the right place automatically instead of sitting in an inbox unnoticed.

1. A Slack integration to notify you when somebody replies
2. A CRM sync so positive replies get tagged as cold email
3. An appointment-setting channel so whoever's calling these leads gets notified fast

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/55668c2c1070453c9f7dab4b7deab8a936bac8621b0b48f19c2edb245ea2badf-md.png)

### Prerequisites

- [Step #2: CRM](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=868dc5749079446eb83660516b92dd8a) (Funnel Tech Course)
- [Step #1C: Buy Cold Email Tool](https://www.skool.com/leadgenerationacademy/classroom/25ab2241?md=5c208b347208462e81c28318fc712d13) (Current Course)

### Framework & Criteria

1. **Plan Requirement:** Instantly's native Slack integration requires the Hyper Growth plan or above.
2. **Trackable Events:** lead marked as Interested, Not Interested, or Neutral, meeting booked, completed, or closed, reply received, email opened, bounced, or sent, campaign completed, and more.
3. **Other Platforms:** if you're not using Instantly, look for a similar integration on your platform, or ask AI to walk you through the equivalent setup.

### Step-by-Step Instructions

1. **Set up the native Instantly Slack integration for interested leads.** This is Instantly's built-in feature and requires the Hyper Growth plan or above.
  1. **Go to Settings > Integrations.** This is where every third-party connection for your Instantly account lives.
  2. **Click on Slack and create a Slack webhook.** The webhook is what actually lets Instantly push messages into your Slack workspace.
  3. **Click Add to Slack and sign in.** This authorizes Instantly to post into your workspace.
  4. **Choose your Slack workspace and channel.** Pick the channel you and your team actually check regularly, not one that gets buried.
  5. **Select "Lead is marked as Interested" from the events list.** You can track other events here too, but this is the one that matters most for catching positive replies.
2. **Build a Zapier multi-step zap to sync interested leads to your CRM and tag them as cold email.** This one Zap handles both the CRM sync and the tag, all triggered off the same positive reply.
  1. **Go to Settings > Integrations and copy your Zapier API key.** You'll need this key to connect Instantly to Zapier, it's different from the Slack webhook you created earlier.
  2. **Create a new Zap in Zapier.** This is the container that will hold your trigger and both actions.
  3. **Set the trigger to Instantly, event "Lead is marked as Interested," and connect with your API key.** Select the campaign to watch, or all campaigns if you want this to apply account-wide.
  4. **Add an action to create the lead in your CRM and map the lead fields.** HubSpot, Close, and Pipedrive all work here, match up name, email, company, and reply text so nothing lands in the wrong field.
  5. **Add a second action in the same Zap to tag the lead as "cold email" in your CRM.** Keeping this in the same Zap as the CRM sync means both happen automatically off the same trigger, you don't need a second Zap for this part.
  6. **Test and publish the Zap.** Testing confirms real data flows through correctly before you rely on it going forward.
3. **Build a second Zap to send a custom Slack notification tagging your appointment setter.** This is a separate Zap from the CRM one, dedicated to alerting whoever is calling these leads.
  1. **Set the trigger to Instantly, event "Lead is marked as Interested," connected with your API key.** Choose the campaign(s) to watch, or all campaigns if you want every interested lead across your whole account to trigger this.
  2. **Add a Slack action set to Send Channel Message.** Sign in and connect your Slack workspace if you haven't already from the earlier Zap.
  3. **Choose your appointment-setting Slack channel.** This should be the dedicated channel your appointment setter actually watches, not your general reply channel, so these alerts don't get buried.
  4. **Add the lead's name, email, phone, and website to the message.** These are the exact details your appointment setter needs to make the call without having to go dig through the CRM first.
  5. **Insert each field by clicking into the message box and typing "/" or using the plus button.** This searches for the matching Instantly field, the curly brackets in the example are just placeholders, you're not typing those yourself.
  6. **Tag your appointment setter by typing @ followed by their Slack username.** Use a Slack User Group instead if you have multiple setters, so Zapier sends it as a real mention.
  7. **Click Test.** Make sure you have at least one lead marked as Interested in Instantly so Zapier has real data to pull, and check that the message looks right in Slack.
  8. **Click Publish to go live.** Once published, this runs automatically every time a lead gets marked as Interested going forward.
4. **If you're using a different sending platform, find the equivalent integration or ask AI for help.** Most platforms have something similar built in or available through Zapier, the exact menu names will just differ from what's shown here.
5. **Ask ChatGPT, Claude, or the AI built into these platforms if you get stuck on any step.** Interfaces change constantly, so if something on screen doesn't match what's described here, let AI walk you through the current version.

### Completion Audit

- Did you set up the native Instantly Slack integration for interested leads?
- Did you build a Zapier multi-step zap to sync interested leads to your CRM and tag them as cold email?
- Did you build a second Zap to send a custom Slack notification tagging your appointment setter?
- If you're using a different platform, did you find the equivalent integration or ask AI for help?
- Did you ask ChatGPT, Claude, or the AI built into these platforms if you got stuck on any step?
