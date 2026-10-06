# Step #5: Client Onboarding Flow

Course: Step #12: Sales Process
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/b799ebc8?md=ea36b02951b246a7bd933a6e55267934

---
Video: this lesson has a video in Skool (about 2:32). Transcript is at the bottom of this file.

As soon as someone pays, it should automatically put them in the onboarding flow. From the payment link, they should automatically be redirected to an onboarding form that can sync with your Slack.

They should get one email per day for the seven-day onboarding flow, introducing them to the service and providing all the information they need. After that, they should get three emails per week for three weeks until the onboarding flow is done.

We also want to minimize our time to first value by providing five quick wins that they can do within 24 hours and that, as the name suggests, get them quick wins. These will tie them over until you get value from your service and make them a lot happier and less full of buyer's remorse.

By the end of this, a payment turns into a client who is already in your Slack, already has their 
package, and already has wins on the board inside the first 24 hours.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/52bca037a261486b92ead0337507a50ded08070157f84e91a00ec3e745f83645.png)

### Prerequisites

- [Step #0A: Platform Setup](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=9b9fcb9c1cf0431fae1cad256d8f8fdc) (Funnel Emails Course)
- [Step #4: One Pager + Contract + Payment](https://www.skool.com/leadgenerationacademy/classroom/b799ebc8?md=dd1106722d2e470998c85c56e60883fb) (Current Course)

### Make A Copy

- [Sales Call Plan Template](https://docs.google.com/document/d/1SoluV8ZhrksZTlpNAfY1qYEensGSo5UJPfbD_-xEWlE/edit?usp=sharing) [in this skill: assets/templates/sales-call-plan-template/]
- [Appointment Setting Message Template](https://docs.google.com/document/d/1vUKmnyABEi6_vFubefRIL7BJ56gbxd_mYA4V8F-hfLo/edit?usp=sharing) [in this skill: assets/templates/welcome-flow-template/]

### Framework & Criteria

1. **Payment:** The trigger for everything below it.
2. **Onboarding Form:** They get redirected here straight off the payment link.
3. **Slack:** The form syncs into Slack, and Slack is where the rest of onboarding happens.
4. **Onboarding Package:** Delivered to them in Slack.
5. **SMS + Email Flow:** One email per day for the first seven days, then three emails per week for the next three weeks.
6. **Five Quick Wins:** Each one balances something that helps them succeed with your service against something that takes them a reasonable amount of time. Selling Facebook ads, that would be:
  1. The [Appointment Setting Message Template](https://docs.google.com/document/d/1vUKmnyABEi6_vFubefRIL7BJ56gbxd_mYA4V8F-hfLo/edit?usp=sharing) to send [in this skill: assets/templates/welcome-flow-template/]
  2. The [Sales Call Opening](https://docs.google.com/document/d/1SoluV8ZhrksZTlpNAfY1qYEensGSo5UJPfbD_-xEWlE/edit?tab=t.yjz9mhsco18a) to use [in this skill: assets/templates/sales-call-plan-template/]
  3. The [Sales Call Plan Template](https://docs.google.com/document/d/1SoluV8ZhrksZTlpNAfY1qYEensGSo5UJPfbD_-xEWlE/edit?usp=sharing) to run [in this skill: assets/templates/sales-call-plan-template/]
  4. The [High-Domain Authority Websites](https://www.skool.com/leadgenerationacademy/classroom/5ab376c5?md=9038e237298f490aa995fb59e2e0c44e) to sign up for
  5. The [Instagram Setup](https://www.skool.com/leadgenerationacademy/classroom/1df452b8?md=e167f3d81da64b10b8343c377c61fc50) and [Facebook Setup](https://www.skool.com/leadgenerationacademy/classroom/1df452b8?md=1e16472a7f024daeb57239363b4eccce) to copy
7. **Onboarding Call:** Where the Objectives get set.
8. **Objectives:** What the client wants out of working with you.
9. **Key Results:** The specific things that have to become true for an Objective to happen.
10. **Assignments:** Every Assignment carries three things.
  1. Date
  2. Time Required
  3. Priority
11. **Morning Update:** Their Daily Plan.
12. **Evening Update:** Their Daily Progress.
13. **30 Minute Weekly Meeting:** Your employee and the client, every week.

### Step-by-Step Instructions

1. **Redirect The Payment Link To Your Onboarding Form**
  1. **Open the Payment Link you use in Stripe and click Edit.** Stripe supports this redirect directly, you do not need Zapier, an API, or custom code for it. If you use more than one payment link, every one of them needs this done.
  2. **Click "After the payment".** Stripe's own documentation identifies the section by that name, so look for that exact wording in the editor.
  3. **Change the Confirmation page from Stripe's page to the redirect option.** By default Stripe shows the customer its own hosted thank you page here, and the wording on the redirect option varies slightly in the dashboard.
  4. **Paste the full URL of your onboarding form.** Use the live form URL, not the edit URL. Google Forms and Typeform both work.
  5. **Save the Payment Link.** From here, paying redirects them to your onboarding form without you sending it to them.
2. **Set Up Your Email Platform**
  1. **Create a "New Client" tag in your email platform.** This tag is what starts your Onboarding Flow, so it needs to exist before you build anything else.
  2. **Create a new automation with the trigger set to "Tag Is Added" and the tag set to "New Client".** The tag name has to match exactly, it is the same one Zapier applies later in this build.
  3. **Add an action step that enrolls the subscriber into your Onboarding Flow.** This is where the seven daily emails, then three emails per week for three weeks, actually send from.
  4. **Confirm the automation is set to Active.** An automation left inactive will not enroll anyone, even when it is built correctly.
3. **Set Up Your SMS Platform**
  1. **Create the same "New Client" tag in your SMS platform.** The SMS side works exactly the same way the email side does.
  2. **Create a visual automation triggered by that tag, and add your onboarding SMS to it.** The trigger is the tag being added, same as email, only the message changes.
  3. **Confirm the automation is active.** Same rule as the email automation.
4. **Connect The Payment To Your Email And SMS Platforms**
  1. **Sign up for an automation platform like Zapier if you don't already have one.** This build uses Zapier, but any platform capable of the same trigger and actions works the same way.
  2. **Create a Stripe secret API key for Zapier.** In Stripe click Developers, then API keys, then Create secret key, choose "Providing this key to a third-party application," name it Zapier and put Zapier as the URL. Zapier can't connect to Stripe without its own key.
  3. **Create a new automation in Zapier with Stripe as the trigger app.** This is what actually catches the payment.
  4. **Set the trigger event to whichever option matches how you collect payment.** Checkout Session Completed, New Invoice, or New Subscription. All three carry the customer's email and name directly, so nothing extra is needed regardless of which one you pick.
  5. **Connect your Stripe account using the API key you just created.** Paste the secret key, not the publishable key.
  6. **Test the trigger and select a recent record.** You need a real record on file before you can map any of its fields into the steps below.
  7. **Add an action step that adds the "New Client" tag to the subscriber in your email platform.** This is the action that enrolls them into the email automation you built above, and the tag has to match it exactly.
  8. **Map the customer's email and first name into that action from the Customer object.** Use Customer > Email, not the flat "Customer Email" field sitting further down the list, that flat field can come back blank even when the real one is filled in.
  9. **Add another action step that adds the "New Client" tag to them in your SMS platform.** Same pattern as the email step, this is what starts the SMS automation.
  10. **Test every step, then publish the automation.** Check your email platform and your SMS platform separately, two systems are getting updated here, don't assume one working means both did.
5. **Send Every Onboarding Form Submission To Slack**
  1. **Create a second automation in Zapier with your form platform as the trigger app.** Google Forms or Typeform, whichever one your onboarding questions actually live on.
  2. **Set the trigger event to "New Form Response" or "New Entry".** Different platforms name this differently, so look for whichever option is closest if you don't see that exact wording.
  3. **Select your specific onboarding form as the trigger and test it.** Point it at the exact form your payment link now redirects to, and get a tested submission on file before mapping anything.
  4. **Add an action step with Slack as the app and Send Channel Message as the event.** Use Send Private Channel Message instead if the channel you created is private.
  5. **Choose the Slack channel your team watches for new onboarding submissions.** This keeps every new client's answers landing in one place.
  6. **Insert the mapped onboarding answers into the message.** Click into the field, then use the "+" button or press "/" to insert the real answers from the submission you tested. Typed text won't pull submission data.
  7. **Test the action, confirm the message landed correctly, then publish the automation.** Make sure every answer shows up and nothing is missing or mismatched.
6. **Deliver The Onboarding Package And Quick Wins**
  1. **Add every new client to your Slack.** This is the handoff out of the form and into the place the rest of onboarding happens.
  2. **Send them their Onboarding Package in Slack.** This is the first thing they receive from you after paying, and how you treat them in this phase tells them how you will treat them going forward.
  3. **Write your five Quick Wins.** Every one of them is a finished asset they copy, not advice they have to go work out, which is what keeps the time reasonable on their end.
  4. **Confirm every Quick Win can be completed within 24 hours.** A Quick Win that takes them a week is not a Quick Win.
  5. **Send the Quick Wins to them in Slack.** These tie them over until they get value from your service, which is what keeps them happy and out of buyer's remorse.
7. **Run The Onboarding Call**
  1. **Book the Onboarding Call.** Everything from the Objectives down gets set on this call.
  2. **Set their Objectives on the call.** These are what the client actually wants out of working with you, in their words, not yours.
  3. **Break every Objective into Key Results.** These are the specific things that have to become true for that Objective to actually happen.
  4. **Break every Key Result into Assignments.** These are the real pieces of work someone has to sit down and complete.
8. **Set Up The Assignments And Reporting**
  1. **Give every Assignment a date, a time required, and a priority.** Three Assignments that take 15 minutes each are very different from three that take two hours each, and without a date none of them make it into anyone's week.
  2. **Set up the Morning Update that gives you their Daily Plan.** This is what they are planning to get done that day, sent before the day starts.
  3. **Set up the Evening Update that gives you their Daily Progress.** This is what actually got done, checked against the plan they sent that morning.
  4. **Book the 30 Minute Weekly Meeting.** This is the recurring meeting between your employee and the client, and it runs off the Assignments.
9. **Test The Whole Flow**
  1. **Pay through your own payment link.** Use a real payment through the same link a client would use, not a test record inside Zapier.
  2. **Confirm the redirect, the form, and the Slack message all fired.** That covers everything you built in the first, fifth and sixth sections above.
  3. **Confirm both tags applied and both flows started sending.** Check the email platform and the SMS platform separately, the first email and the first SMS should both be on their way.

### Completion Audit

- Did you open your Payment Link in Stripe and click Edit?
- Did you click "After the payment"?
- Did you change the Confirmation page to the redirect option?
- Did you paste the full URL of your onboarding form?
- Did you save the Payment Link?
- Did you create a "New Client" tag in your email platform?
- Did you create an automation triggered by that tag being added?
- Did you add an action that enrolls the subscriber into your Onboarding Flow?
- Is the email automation set to Active?
- Did you create the same "New Client" tag in your SMS platform?
- Did you create a visual automation triggered by that tag with your onboarding SMS in it?
- Is the SMS automation active?
- Did you sign up for an automation platform like Zapier if you didn't already have one?
- Did you create a Stripe secret API key for Zapier?
- Did you create a new automation in Zapier with Stripe as the trigger app?
- Did you set the trigger event to the option that matches how you collect payment?
- Did you connect your Stripe account using the API key?
- Did you test the trigger and select a recent record?
- Did you add an action that adds the "New Client" tag in your email platform?
- Did you map the email and first name from the Customer object instead of the flat fields?
- Did you add an action that adds the "New Client" tag in your SMS platform?
- Did you test every step and publish the automation?
- Did you create a second automation with your form platform as the trigger app?
- Did you set the trigger event to "New Form Response" or "New Entry"?
- Did you select your onboarding form and test the trigger?
- Did you add a Slack action set to Send Channel Message?
- Did you choose the Slack channel your team watches?
- Did you insert the mapped onboarding answers using the "+" button instead of typing them?
- Did you test the action, confirm the message landed, and publish the automation?
- Are new clients being added to your Slack?
- Did you send them their Onboarding Package in Slack?
- Did you write your five Quick Wins?
- Can every Quick Win be completed within 24 hours?
- Did you send the Quick Wins to them in Slack?
- Did you book the Onboarding Call?
- Did you set their Objectives on the call?
- Did you break every Objective into Key Results?
- Did you break every Key Result into Assignments?
- Does every Assignment have a date, a time required, and a priority?
- Did you set up the Morning Update that gives you their Daily Plan?
- Did you set up the Evening Update that gives you their Daily Progress?
- Did you book the 30 Minute Weekly Meeting?
- Did you pay through your own payment link?
- Did you confirm the redirect, the form, and the Slack message all fired?
- Did you confirm both tags applied and both flows started sending?

---

## Video Transcript

Automatic captions. Timestamps are minutes:seconds into the video.

[0:00] Literally, the most important part in getting a customer is the onboarding process, and this is where you really need to give a shit and make it smooth as hell. So this is going to be something that you can zoom in, but when someone pays, they should automatically be redirected to an onboarding form, and they should get a text message and an email to that onboarding form. Once they fill out the onboarding form, they should automatically be redirected to Slack, and then in Slack, they should automatically receive via a welcome message, the onboarding package. That should happen as a series of redirects to ensure that they get every single thing that they need to get in the order they need to get it and to make sure to kind of force compliance that they actually do it.

[0:47] Inside that onboarding package should be two things. The first thing is to book the link to the onboarding call, and the second thing is to get them five quick wins or however many quick wins that you possibly can get them in a short amount of time. So these things ideally would be things that help you do your service, like that would be nice. So an example here. So if you're doing Facebook ads to lead generate for roofers, for example, an appointment setting message template to send the exact opening for their calls, the exact plan to use. I domain authority websites to sign up for so if someone sees your ad and Google them, they have better search results, and then the exact Instagram and Facebook set up to copy. These five quick wins help you do your service or they should ideally.

[1:36] And then number two, they take care of a pretty good thing like in psychology where someone pays you, presumably a lot of money, and then it's kind of like, oh my god, did I make the right choice? This is called buyers remorse usually. And because a lot of time, it's going to take you a while to get them their results, right? Their results are not going to happen in five seconds. It's going to take a week or two weeks or a month or who knows? So by getting them these quick wins, they feel like they're time to first values. Very, very, very fast, right? And that is going to reduce buyers remorse, reduce refunds, reduce chargebacks, get them to think that you are doing a lot better job, very little effort on your end after you create

[2:21] these things. And it really solves a big gap. Your turn rate is going to go down because your first impression is going to be higher and time to first value is going to be better. You're going to get more referrals. Every single thing is going to be better by having this exact onboarding flow.


# Step #13: Sales Assets
