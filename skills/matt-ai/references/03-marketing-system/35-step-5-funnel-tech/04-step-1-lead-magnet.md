# Step #1: Lead Magnet

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=96d56aa09b57453cb237cbe40a6f9a36

---
Video: this lesson has a video in Skool (open the Skool link to watch).

When someone opts in for your lead magnet, you need an automation that tags them and sends them the lead magnet automatically, so you're not manually emailing every person who signs up.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/069d2611add746fa9ff9b2189215b8a074e0d3634f0749f5a3c8cb756265dd9f.png)

### Prerequisites

- [Step #1: Opt In Page](https://www.skool.com/leadgenerationacademy/classroom/94f7e3ec?md=7063959ac1fe4a32b1fa9a2de80315fc) (Funnel Pages Course)
- [Step #3: Lead Magnet Delivery Email](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=e7de308e5f8c4736956a330eb1f91c4c) (Funnel Emails Course)

### Links

- [Zapier](https://zapier.com)
- [Beehiiv Automations Page](https://app.beehiiv.com/automations)
- [Webflow](https://webflow.com)

### Framework & Criteria

1. **Automation Platform Connection:** Zapier connects your opt-in form to beehiiv.
2. **Subscriber Creation:** When someone submits the form, Zapier creates them as a subscriber in beehiiv and adds them to your Lead Magnet automation.
3. **Automatic Send:** beehiiv automatically sends the Lead Magnet Delivery Email to anyone added to that automation.

### Step-by-Step Instructions

1. **Open your [Beehiiv Automations page](https://app.beehiiv.com/automations), then click Create Automation.** You can also get there by clicking Automations in the left-hand navigation bar. This starts the automation that will send your Lead Magnet Delivery Email.
2. **Scroll down and click Added by API.** This lets Zapier add subscribers to this automation. If you choose any other trigger, this automation will not show up in Zapier later.
3. **Click the + button, then click Send email.** This adds the action that sends the email to every subscriber Zapier adds.
4. **Click Create email, then click New template.** This opens the template library and gives you a blank email to fill in.
5. **Fill in the email using [Step #3: Lead Magnet Delivery Email](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=e7de308e5f8c4736956a330eb1f91c4c).** If you haven't written your Lead Magnet Delivery Email yet, follow that step in the Funnel Emails course first.
6. **Click New Automation at the top of the page, change the name to "[Lead Magnet Name] Automation," then click Save.** This is so you can find the automation easily when you choose it in Zapier later.
7. **Click Publish.** An automation left as a draft will not send anything.
8. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. Zapier is the easiest to use if you're deciding between Zapier, Make, or n8n.
9. **Set your opt-in form platform (e.g. Webflow) as the trigger app, set the trigger event to New Form Submission, then connect your account.** Use whichever platform your opt-in form was actually built on. Every app used in a Zap needs its own account connection before you can configure it.
10. **Choose your specific opt-in form.** If you run multiple Lead Magnets with multiple forms, make sure you're connecting the correct one to this automation.
11. **Click Continue, then click Test trigger to confirm a submission is found.** Confirm this before you build the rest of the automation.
12. **Click the + button to add an action step. Set beehiiv as the action app, set the action event to Create a Subscriber, then connect your beehiiv account.** This is where Zapier sends the subscriber to beehiiv.
13. **Choose your publication in the Publications field.** This field is at the very top.
14. **Insert the Email, Name, and Phone from your form submission into the Email, Full Name, and Number fields.** Click into each field, then click the + button or press "/" to insert it. Scroll down between fields without changing anything else. Do not type these in manually. Typed text won't pull real submission data.
15. **Choose your automation in the Automation IDs field.** If you don't see your automation, double-check that its trigger in beehiiv is set to Added by API. With any other trigger, it will not show up here.
16. **Click Continue, then click Test step.** This sends the test submission to beehiiv to confirm the action works.
17. **Click Publish.** This turns the Zap on so it runs on every new opt-in.
18. **Submit your opt-in form yourself, then check whether you received the Lead Magnet Delivery Email.** Use your own email so you can check what arrives. This confirms the form, Zapier, the beehiiv automation, and the email all actually worked together.
19. **If it didn't work, ask ChatGPT or Claude to diagnose the problem.** Don't leave it half-tested. Either confirm it's live or get the failure diagnosed before moving on.

### Completion Audit

- Did you open your beehiiv Automations page and click Create Automation?
- Did you scroll down and click Added by API?
- Did you click the + button, then click Send email?
- Did you click Create email, then click New template?
- Did you fill in the email using Step #3: Lead Magnet Delivery Email?
- Did you rename your automation to "[Lead Magnet Name] Automation" and click Save?
- Did you click Publish in beehiiv?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set your opt-in form platform as the trigger app, set the trigger event to New Form Submission, and connect your account?
- Did you choose your specific opt-in form?
- Did you click Continue, then click Test trigger to confirm a submission is found?
- Did you add an action step, set beehiiv as the action app, set the action event to Create a Subscriber, and connect your beehiiv account?
- Did you choose your publication in the Publications field?
- Did you insert the Email, Name, and Phone from your form submission into the Email, Full Name, and Number fields?
- Did you choose your automation in the Automation IDs field?
- Did you click Continue, then click Test step?
- Did you click Publish in Zapier?
- Did you submit your opt-in form yourself and check whether you received the Lead Magnet Delivery Email?
- If it didn't work, did you ask ChatGPT or Claude to diagnose the problem?
