# Step #14: Payment > Onboarding Flow

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=3137dd50589c4e95a3ee25e3309174ea

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Whenever you receive a new payment in Stripe, this automation will tag them in your email platform and start their email onboarding flow.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/d10dd1c34631489fa3ccfe0eabbfc500791515d383b046f2b64a463fc263de2d.png)

### Links

- [Zapier](https://zapier.com/)
- [Stripe API Keys](https://dashboard.stripe.com/apikeys)
- [Kit](https://kit.com/)

### Step-by-Step Instructions

1. **Create a "New Client" tag in your email platform.** This tag is what starts your Onboarding Flow, so it needs to exist before you build anything else.
2. **Create a new automation inside your email platform, set the trigger to Tag Is Added, then select the "New Client" tag.** This has to match exactly. It's the same tag Zapier applies later in this build.
3. **Add an action step to enroll the subscriber into your Onboarding Flow, then confirm the automation is set to Active.** An automation left inactive will not enroll anyone, even if it's built correctly.
4. **In [Stripe](https://dashboard.stripe.com/apikeys), click Developers in the bottom left, then [API keys](https://dashboard.stripe.com/acct_1PU7HtRsbbz0AUES/apikeys), then Create secret key.** Zapier needs its own key to connect to your Stripe account. You can't connect it without one.
5. **Choose Providing this key to a third-party application, name it "Zapier", put "Zapier" as the URL, then continue with the restricted key.** This keeps the key scoped to a named third party instead of a generic full-access key, which is safer if you ever need to revoke just Zapier's access later.
6. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** Sign up if you don't already have an account. This is where you'll build the trigger and every action together.
7. **Set Stripe as the trigger app, set the trigger event to New Payment, then connect your account using the secret key you just created.** This fires the automation every time a customer pays you. Paste the secret key from step 5, not the publishable key. Zapier needs the secret one.
8. **Leave every setting on the Configure tab as the default, then click Continue and click Test trigger to confirm a recent payment is found.** Nothing on the Configure tab needs to change.
9. **Click the + button to add an action step. Set your email platform as the action app, set the action event to Add Tag to Subscriber, then connect your account.** This is the specific action that enrolls the subscriber into the email platform automation you built in step 2.
10. **Set the Tag field to "New Client".** This has to match the exact tag your email platform automation is watching for.
11. **Insert Customer > Email into the Email field and Customer > Name into the First Name field.** Click the + button, or press "/", and search "customer email" and "customer name" to find them. Use the Email field nested under Customer, not the Customer Email under Invoice Data. That one can come back blank even when the real one is filled in. Do not type these in manually. Typed text won't pull real payment data.
12. **Click Continue, then click Test step and check your email platform to confirm the "New Client" tag was added to the test subscriber.** This confirms the Zapier side actually worked.
13. **Confirm the Onboarding Flow sequence actually started sending.** This proves the tag correctly triggered the automation you built inside your email platform.
14. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** This is also the foundation [Step #15: Payment > Slack Notification](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=5d072c8cf7344461a56f6fdcef389621) builds on, so get it working before moving on.

### Completion Audit

- Did you create a "New Client" tag in your email platform?
- Did you create a new automation inside your email platform, set the trigger to Tag Is Added, and select the "New Client" tag?
- Did you add an action step to enroll the subscriber into your Onboarding Flow and confirm the automation is set to Active?
- Did you click Developers, then API keys, then Create secret key in Stripe?
- Did you set up the key for Zapier as a restricted, third-party key?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set Stripe as the trigger app, set the trigger event to New Payment, and connect your account using the secret key?
- Did you leave the Configure tab as the default and test the trigger to confirm a recent payment is found?
- Did you add an action step, set your email platform as the action app, set the action event to Add Tag to Subscriber, and connect your account?
- Did you set the Tag field to "New Client"?
- Did you insert Customer > Email into the Email field and Customer > Name into the First Name field?
- Did you click Test step and confirm the "New Client" tag was added to the test subscriber?
- Did you confirm the Onboarding Flow sequence actually started sending?
- Did you publish the automation, or diagnose the problem if it didn't work?
